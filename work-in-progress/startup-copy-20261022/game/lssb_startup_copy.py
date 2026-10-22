"""Temporary, guarded deepcopy dispatch for startup object graphs.

Copyright (c) 2026 KPEKTYC. LSSB Noncommercial Attribution License 1.0.
Keeps CPython's memo, reducers, custom hooks and rollback-aware containers.
Optimizes exact built-in and verified engine containers; mutable objects copy.
"""
import copy
import copyreg
import hashlib
import json
import types


def fingerprint(code):
    def describe(c):
        return [c.co_code.hex(), c.co_names, c.co_varnames, c.co_argcount,
                c.co_kwonlyargcount, c.co_flags,
                [describe(v) if isinstance(v, types.CodeType) else repr(v) for v in c.co_consts]]
    return hashlib.sha256(json.dumps(describe(code), ensure_ascii=True).encode()).hexdigest()


EXPECTED = {
    'deepcopy': 'e5b97e940974efc7bd4dae52f786496d6e71be5fa2a3e724bf8ff75f87837fee',
    '_deepcopy_dict': '605a263daaf7ca3b8d49f18c90ebd3b8de7d43182ae5ebad6ecc6d203edce964',
    '_deepcopy_list': 'd5fc954ae6e43eae2142139495406fd44d07b1dbe571f061f671883fe31c451e',
    '_deepcopy_tuple': '9340970cda7e8a604ac91feeac87267ff1e3fd92b03306dbcb537587adc065d0',
    '_deepcopy_atomic': '8c26095879065f4b60750ca79ecc7a7b44d776034a2cc7d278d03b7f10b3bac1',
    '_reconstruct': 'e69d57fbe2adac3fb36b7324b7f81d3ef8a954596d74c8bd3660117a64797fec',
}


class CopyOptimizer:
    def __init__(self):
        self.enabled = False
        self.active = False
        self.containers_enabled = False
        self.original = {}
        self.replacements = {}

    def install(self):
        if self.active:
            return True
        for name, expected in EXPECTED.items():
            fn = getattr(copy, name, None)
            if not isinstance(fn, types.FunctionType) or fingerprint(fn.__code__) != expected:
                return False
        dispatch = copy._deepcopy_dispatch
        native = copy.deepcopy
        atomic = copy._deepcopy_atomic
        if not isinstance(native.__defaults__, tuple) or len(native.__defaults__) != 2 or native.__defaults__[0] is not None:
            return False
        nil = native.__defaults__[1]
        if copy._reconstruct.__kwdefaults__ != {'deepcopy': native}:
            return False
        for kind, name in ((dict, '_deepcopy_dict'), (list, '_deepcopy_list'), (tuple, '_deepcopy_tuple')):
            fn = getattr(copy, name)
            if dispatch.get(kind) is not fn or fn.__defaults__ != (native,):
                return False

        original_dict, original_list, original_tuple = dispatch[dict], dispatch[list], dispatch[tuple]
        def copy_dict(source, memo):
            if type(memo) is not dict:
                return original_dict(source, memo)
            result = {}
            memo[id(source)] = result
            get = memo.get
            select = dispatch.get
            for key, value in source.items():
                # Preserve assignment evaluation order: value before key.
                if select(type(value)) is atomic:
                    value_copy = get(id(value), nil)
                    if value_copy is nil:
                        value_copy = value
                else:
                    value_copy = native(value, memo)
                if select(type(key)) is atomic:
                    key_copy = get(id(key), nil)
                    if key_copy is nil:
                        key_copy = key
                else:
                    key_copy = native(key, memo)
                result[key_copy] = value_copy
            return result

        def copy_list(source, memo):
            if type(memo) is not dict:
                return original_list(source, memo)
            result = []
            memo[id(source)] = result
            get = memo.get
            select = dispatch.get
            for value in source:
                if select(type(value)) is atomic:
                    value_copy = get(id(value), nil)
                    if value_copy is nil:
                        value_copy = value
                else:
                    value_copy = native(value, memo)
                result.append(value_copy)
            return result

        def copy_tuple(source, memo):
            if type(memo) is not dict:
                return original_tuple(source, memo)
            values = []
            get = memo.get
            select = dispatch.get
            for value in source:
                if select(type(value)) is atomic:
                    value_copy = get(id(value), nil)
                    if value_copy is nil:
                        value_copy = value
                else:
                    value_copy = native(value, memo)
                values.append(value_copy)
            # A child may have completed a recursive copy of this same tuple.
            # Use subscription: a memo value equal to native's nil is valid here.
            try:
                return memo[id(source)]
            except KeyError:
                pass
            for value, value_copy in zip(source, values):
                if value is not value_copy:
                    return tuple(values)
            return source

        self.original = {dict: dispatch[dict], list: dispatch[list], tuple: dispatch[tuple]}
        self.replacements = {dict: copy_dict, list: copy_list, tuple: copy_tuple}
        dispatch.update(self.replacements)
        self.enabled = True
        self.active = True
        return True

    def install_containers(self, revertable, game):
        """Fast reconstruction of the engine's exact, stateless list/dict types.

        The native reducer and deepcopy hooks still run. Stateful instances,
        custom memo mappings and unexpected reduction forms use _reconstruct.
        The first mutation uses the native rollback hook. Later writes bypass
        its wrapper only while that exact object is already in the same log.
        """
        if not self.active:
            return False
        dispatch = copy._deepcopy_dispatch
        native = copy.deepcopy
        reconstruct = copy._reconstruct
        atomic = copy._deepcopy_atomic
        nil = native.__defaults__[1]
        kinds = ((revertable.RevertableDict, dict, '__setitem__'),
                 (revertable.RevertableList, list, 'append'))
        for cls, base, method_name in kinds:
            method = getattr(cls, method_name, None)
            if (cls in dispatch or cls.__new__ is not base.__new__
                    or not isinstance(method, types.FunctionType)
                    or fingerprint(method.__code__) != '02670b52b2297ad451b270e192fa3c3ce693261521af9f0643590a9020e62d3c'
                    or getattr(method, '__wrapped__', None) is not getattr(base, method_name)
                    or not method.__closure__ or len(method.__closure__) != 1
                    or method.__closure__[0].cell_contents is not getattr(base, method_name)):
                return False

        def handler_for(cls, base, method_name):
            expected_method = getattr(cls, method_name)
            raw_method = getattr(base, method_name)
            def clone(source, memo):
                hook = getattr(source, '__deepcopy__', None)
                if hook is not None:
                    return hook(memo)
                registered = copy.dispatch_table.get(cls)
                if registered is not None:
                    reduced = registered(source)
                else:
                    reducer = getattr(source, '__reduce_ex__', None)
                    reduced = reducer(4) if reducer is not None else source.__reduce__()
                if isinstance(reduced, str):
                    return source
                if (type(memo) is not dict or len(reduced) != 5
                        or reduced[0] is not copyreg.__newobj__ or reduced[1] != (cls,)
                        or reduced[2] is not None or memo.get(id(cls), cls) is not cls
                        or cls.__new__ is not base.__new__
                        or (base is dict and reduced[3] is not None)
                        or (base is list and reduced[4] is not None)):
                    return reconstruct(source, memo, *reduced)
                result = reduced[0](cls)
                result_id = id(result)
                memo[id(source)] = result
                get = memo.get
                select = dispatch.get
                iterator = reduced[4] if base is dict else reduced[3]
                if iterator is None:
                    return result
                for entry in iterator:
                    if base is dict:
                        key, value = entry
                        # Reducer reconstruction copies keys before values.
                        if select(type(key)) is atomic:
                            key_copy = get(id(key), nil)
                            if key_copy is nil:
                                key_copy = key
                        else:
                            key_copy = native(key, memo)
                    else:
                        value = entry
                    if select(type(value)) is atomic:
                        value_copy = get(id(value), nil)
                        if value_copy is nil:
                            value_copy = value
                    else:
                        value_copy = native(value, memo)
                    # Re-check after user hooks, including a replaced log/method.
                    append = result.append if base is list else None
                    method = getattr(cls, method_name) if base is dict else getattr(append, '__func__', None)
                    use_raw = method is expected_method and result_id in game.log.mutated
                    action = raw_method if use_raw else method
                    if base is dict:
                        action(result, key_copy, value_copy)
                    else:
                        if use_raw:
                            raw_method(result, value_copy)
                        else:
                            append(value_copy)
                return result
            return clone

        for cls, base, method_name in kinds:
            replacement = handler_for(cls, base, method_name)
            self.original[cls] = None
            self.replacements[cls] = replacement
            dispatch[cls] = replacement
        self.containers_enabled = True
        return True

    def cleanup(self):
        for kind, replacement in self.replacements.items():
            if copy._deepcopy_dispatch.get(kind) is replacement:
                if self.original[kind] is None:
                    del copy._deepcopy_dispatch[kind]
                else:
                    copy._deepcopy_dispatch[kind] = self.original[kind]
        self.active = False

    def restored(self):
        return all(copy._deepcopy_dispatch.get(kind) is not replacement
                   for kind, replacement in self.replacements.items())
