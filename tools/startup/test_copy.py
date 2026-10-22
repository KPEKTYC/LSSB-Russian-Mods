"""Graph, memo, hook, and fallback tests for startup copy dispatch."""
import copy
import importlib.util
from pathlib import Path
import unittest

SOURCE = Path(__file__).resolve().parents[2] / 'work-in-progress/startup-copy-20261022/game/lssb_startup_copy.py'
SPEC = importlib.util.spec_from_file_location('startup_copy_under_test', SOURCE)
fast = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fast)


class CopyTests(unittest.TestCase):
    def setUp(self):
        self.dispatch = copy._deepcopy_dispatch.copy()
        self.optimizer = fast.CopyOptimizer()

    def tearDown(self):
        copy._deepcopy_dispatch.clear()
        copy._deepcopy_dispatch.update(self.dispatch)

    def install(self):
        self.assertTrue(self.optimizer.install(), 'Run these tests with the supported game Python runtime')

    def test_cycles_aliases_and_independence(self):
        self.install()
        shared = [1, {'mutable': []}]
        root = {'a': shared, 'b': shared}
        shared.append(root)
        result = copy.deepcopy(root)
        self.assertIs(result['a'], result['b'])
        self.assertIs(result['a'][-1], result)
        self.assertIsNot(result['a'], shared)
        result['a'][1]['mutable'].append(9)
        self.assertEqual(shared[1]['mutable'], [])

    def test_preseeded_atomic_memo_including_none(self):
        self.install()
        value = 'a unique memo value'
        self.assertEqual(copy.deepcopy([value], {id(value): None}), [None])
        self.assertEqual(copy.deepcopy({value: value}, {id(value): 'replacement'}), {'replacement': 'replacement'})
        self.assertEqual(copy.deepcopy([value], {id(value): copy.deepcopy.__defaults__[1]}), [value])

    def test_tuple_list_cycle(self):
        self.install()
        items = []
        root = (items,)
        items.append(root)
        clone = copy.deepcopy(root)
        self.assertIs(clone[0][0], clone)
        self.assertIsNot(clone[0], items)

    def test_install_cleanup_install(self):
        self.install()
        self.optimizer.cleanup()
        self.install()
        self.assertIsNot(copy._deepcopy_dispatch[dict], self.dispatch[dict])

    def test_tuple_identity_memo_and_dynamic_dispatch(self):
        self.install()
        source = ('unique tuple atom', 12345, None)
        self.assertIs(copy.deepcopy(source), source)
        self.assertEqual(copy.deepcopy(source, {id(source[0]): 'replacement'}), ('replacement', 12345, None))
        copy._deepcopy_dispatch[str] = lambda value, memo: 'changed'
        self.assertEqual(copy.deepcopy(source), ('changed', 12345, None))

    def test_tuple_recursive_hook_sets_memo(self):
        self.install()
        class Hook:
            def __deepcopy__(self, memo):
                memo[id(root)] = None
                return self
        root = (Hook(),)
        self.assertIsNone(copy.deepcopy(root))

    def test_hooks_subclasses_and_value_before_key(self):
        events = []
        class Hook:
            def __init__(self, name): self.name = name
            def __deepcopy__(self, memo):
                events.append(self.name)
                return Hook(self.name)
        class CustomList(list):
            def __deepcopy__(self, memo): return 'custom list hook'
        root = {Hook('key'): Hook('value')}
        copy.deepcopy(root)
        expected = events[:]
        events.clear()
        self.install()
        copy.deepcopy(root)
        self.assertEqual(events, expected)
        self.assertEqual(copy.deepcopy([CustomList([1])]), ['custom list hook'])

    def test_reducers_and_slots(self):
        class Slotted:
            __slots__ = ('value',)
            def __init__(self, value): self.value = value
        self.install()
        obj = Slotted([1, 2])
        result = copy.deepcopy([obj, obj])
        self.assertIs(result[0], result[1])
        self.assertEqual(result[0].value, obj.value)
        self.assertIsNot(result[0].value, obj.value)

    def test_late_atomic_dispatch_is_respected(self):
        self.install()
        copy._deepcopy_dispatch[str] = lambda value, memo: 'changed'
        self.assertEqual(copy.deepcopy(['text']), ['changed'])

    def test_unsupported_handler_falls_back(self):
        foreign = lambda source, memo: 'foreign'
        copy._deepcopy_dispatch[dict] = foreign
        self.assertFalse(self.optimizer.install())
        self.assertIs(copy._deepcopy_dispatch[dict], foreign)

    def test_changed_code_falls_back(self):
        original = copy._deepcopy_atomic
        try:
            copy._deepcopy_atomic = lambda source, memo: source
            self.assertFalse(self.optimizer.install())
        finally:
            copy._deepcopy_atomic = original

    def test_cleanup_does_not_overwrite_foreign_patch(self):
        self.install()
        foreign = lambda source, memo: 'foreign'
        copy._deepcopy_dispatch[list] = foreign
        self.optimizer.cleanup()
        self.assertIs(copy._deepcopy_dispatch[list], foreign)
        self.assertIs(copy._deepcopy_dispatch[dict], self.dispatch[dict])
        self.assertTrue(self.optimizer.restored())


if __name__ == '__main__':
    unittest.main()
