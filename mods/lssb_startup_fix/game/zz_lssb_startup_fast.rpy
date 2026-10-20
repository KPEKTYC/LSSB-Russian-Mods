# LSSB Startup Fast 1.1.1. Native group execution, indexed candidate selection.
init 0 python in lssb_startup_fast:
    import renpy, hashlib, json, types, os
    import store
    li = getattr(store, "layeredimage", None)
    from store import config, renpy as api
    _constant = True

    """Prefix lookup for the append-only image-name registry used during init.

    The registry may contain duplicate names and its insertion order is significant.
    This class never mutates it. Replacing the registry or shrinking an observed
    registry invalidates the index. Arbitrary in-place replacement/reordering of
    existing entries is outside the append-only contract; call clear() after that.
    """

    from bisect import bisect_left


    class PrefixIndex:
        """Return the same names, in the same order, as a startswith list scan."""

        def __init__(self, tail_limit=1024):
            if not isinstance(tail_limit, int) or tail_limit < 0:
                raise ValueError("tail_limit must be a nonnegative integer")
            self.tail_limit = tail_limit
            self.queries = 0
            self.rebuilds = 0
            self._source = None
            self._sorted_pairs = []
            self._bulk_count = 0
            self._observed_count = 0

        def clear(self):
            """Release the registry and index, retaining the diagnostic counters."""
            self._source = None
            self._sorted_pairs = []
            self._bulk_count = 0
            self._observed_count = 0

        def _rebuild(self, names):
            self._source = names
            self._sorted_pairs = sorted((name, index) for index, name in enumerate(names))
            self._bulk_count = len(names)
            self.rebuilds += 1

        def candidates(self, names, prefix):
            """Select matching names without losing duplicate registrations.

            Most names live in a sorted bulk index. A small append-only tail is
            scanned directly; growing beyond tail_limit triggers a fresh bulk sort.
            The result is an independent list, ordered by original registry index.
            """
            self.queries += 1
            count = len(names)
            if (
                names is not self._source
                or count < self._observed_count
                or count - self._bulk_count > self.tail_limit
            ):
                self._rebuild(names)
            self._observed_count = count

            # Scanning until the prefix stops matching also handles U+10FFFF;
            # appending a synthetic maximum character is not a valid upper bound.
            cursor = bisect_left(self._sorted_pairs, (prefix, -1))
            matches = []
            while cursor < len(self._sorted_pairs):
                name, ordinal = self._sorted_pairs[cursor]
                if not name.startswith(prefix):
                    break
                matches.append((ordinal, name))
                cursor += 1

            for ordinal in range(self._bulk_count, count):
                name = names[ordinal]
                if name.startswith(prefix):
                    matches.append((ordinal, name))

            matches.sort(key=lambda pair: pair[0])
            return [name for ordinal, name in matches]


    original = getattr(getattr(li, "RawAttributeGroup", None), "execute", None)
    optimized = None
    enabled = False
    verified_queries = 0
    index = PrefixIndex()
    verify = os.environ.get('LSSB_STARTUP_VERIFY') == '1'
    native_source = 'def execute(self):\n    properties = self.final_properties | {k: eval(v) for k, v in self.expr_properties.items()}\n\n    auto = properties.pop("auto", False)\n    variant = properties.get("variant", None)\n    multiple = properties.pop("multiple", False)\n\n    rv = []\n\n    if multiple:\n        group_name_for_attributes = None\n    else:\n        group_name_for_attributes = self.group_name\n\n    for ra in self.children:\n        rv.extend(ra.execute(group_name=group_name_for_attributes, **properties))\n\n    if auto:\n        seen = set(a.raw_attribute for a in rv)\n\n        pattern = format_function(\n            what="auto group attribute",\n            name=self.li_name.replace(" ", "_"),\n            group=self.group_name or None,\n            variant=variant or None,\n            attribute="",\n            image=None,\n            image_format=None,\n        )\n\n        for i in renpy.list_images():\n            if i.startswith(pattern):\n                attr, *rest = i.removeprefix(pattern).split()\n                if (not rest) and (attr not in seen):\n                    rv.append(Attribute(group_name_for_attributes, attr, renpy.displayable(i), **properties))\n\n    return rv\n'
    fast_source = 'def execute(self):\n    properties = self.final_properties | {k: eval(v) for k, v in self.expr_properties.items()}\n\n    auto = properties.pop("auto", False)\n    variant = properties.get("variant", None)\n    multiple = properties.pop("multiple", False)\n\n    rv = []\n\n    if multiple:\n        group_name_for_attributes = None\n    else:\n        group_name_for_attributes = self.group_name\n\n    for ra in self.children:\n        rv.extend(ra.execute(group_name=group_name_for_attributes, **properties))\n\n    if auto:\n        seen = set(a.raw_attribute for a in rv)\n\n        pattern = format_function(\n            what="auto group attribute",\n            name=self.li_name.replace(" ", "_"),\n            group=self.group_name or None,\n            variant=variant or None,\n            attribute="",\n            image=None,\n            image_format=None,\n        )\n\n        for i in _lssb_startup_prefix_candidates(pattern):\n            if i.startswith(pattern):\n                attr, *rest = i.removeprefix(pattern).split()\n                if (not rest) and (attr not in seen):\n                    rv.append(Attribute(group_name_for_attributes, attr, renpy.displayable(i), **properties))\n\n    return rv\n'
    missing = object()
    previous_helper = missing

    def fingerprint(code):
        def describe(c):
            return [c.co_code.hex(), c.co_names, c.co_varnames, c.co_argcount, c.co_kwonlyargcount,
                    c.co_flags, [describe(v) if isinstance(v, types.CodeType) else repr(v) for v in c.co_consts]]
        return hashlib.sha256(json.dumps(describe(code),ensure_ascii=True).encode()).hexdigest()

    def candidates(pattern):
        global verified_queries
        names = api.list_images()
        result = index.candidates(names, pattern)
        if verify:
            expected = [name for name in names if name.startswith(pattern)]
            if result != expected:
                raise AssertionError('Image prefix candidates differ from the native scan: ' + pattern)
            verified_queries += 1
        return result

    def compile_method(source):
        # Use the engine's own compiler to preserve its container/eval transforms.
        namespace = {}
        code = renpy.python.py_compile(source, 'exec', filename='lssb_startup_native_group', cache=False)
        exec(code, original.__globals__, namespace)
        return namespace['execute']

    def cleanup():
        if optimized is not None and li.RawAttributeGroup.execute is optimized:
            li.RawAttributeGroup.execute = original
        if original is not None and getattr(original, '__globals__', {}).get('_lssb_startup_prefix_candidates') is candidates:
            if previous_helper is missing:
                del original.__globals__['_lssb_startup_prefix_candidates']
            else:
                original.__globals__['_lssb_startup_prefix_candidates'] = previous_helper
        index.clear()

    try:
        if callable(original) and hasattr(original, '__code__') and callable(getattr(renpy.python, 'py_compile', None)) and hasattr(renpy.game.post_init, 'append'):
            if fingerprint(original.__code__) == 'e4ba8954724202c5154fa777f39c8486afab4554b689bf56943bef0975e6f1d4':
                rebuilt = compile_method(native_source)
                if fingerprint(rebuilt.__code__) == fingerprint(original.__code__):
                    optimized = compile_method(fast_source)
                    previous_helper = original.__globals__.get('_lssb_startup_prefix_candidates', missing)
                    original.__globals__['_lssb_startup_prefix_candidates'] = candidates
                    li.RawAttributeGroup.execute = optimized
                    renpy.game.post_init.append(cleanup)
                    enabled = True
                    api.log('LSSB Startup Fast: native image-prefix index enabled for initialization.')
                else:
                    api.log('LSSB Startup Fast: compiler compatibility check failed; keeping native startup.')
            else:
                api.log('LSSB Startup Fast: another group implementation detected; keeping native startup.')

    except Exception as error:
        cleanup()
        enabled = False
        api.log('LSSB Startup Fast: native startup retained: ' + type(error).__name__)
