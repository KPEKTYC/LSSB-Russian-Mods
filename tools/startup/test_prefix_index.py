"""Behavioral checks against the original startswith scan."""

import random
import unittest

from pathlib import Path
import textwrap
_source = (Path(__file__).resolve().parents[2] / 'mods/lssb_startup_fix/game/zz_lssb_startup_fast.rpy').read_text(encoding='utf-8')
_start = _source.index('    from bisect import bisect_left')
_end = _source.index('    original =', _start)
_namespace = {}
exec(compile(textwrap.dedent(_source[_start:_end]), 'shipped_prefix_index', 'exec'), _namespace)
PrefixIndex = _namespace['PrefixIndex']


class PrefixIndexTests(unittest.TestCase):
    def assert_matches_scan(self, index, names, prefix):
        before = list(names)
        self.assertEqual(
            index.candidates(names, prefix),
            [name for name in names if name.startswith(prefix)],
        )
        self.assertEqual(names, before, "lookup must not change the registry")

    def test_duplicates_and_insertion_order_in_bulk_and_tail(self):
        index = PrefixIndex()
        names = ["npc_top_z", "other", "npc_top_a", "npc_top_z"]
        self.assert_matches_scan(index, names, "npc_top_")
        names.extend(["npc_top_0", "npc_top_a", "unrelated", "npc_top_z"])
        self.assert_matches_scan(index, names, "npc_top_")
        self.assertEqual(index.rebuilds, 1)
        self.assertEqual(index.queries, 2)

    def test_empty_exact_and_nonmatching_prefixes(self):
        index = PrefixIndex()
        names = ["foo", "foobar", "foo_", "foo_a", "", "foo a b", "bar"]
        for prefix in ("", "foo", "foo_", "foo_a", "foo a", "missing", "z"):
            self.assert_matches_scan(index, names, prefix)
        # Filtering invalid auto-group suffixes belongs to the native caller.
        self.assertIn("foo_", index.candidates(names, "foo_"))
        self.assertIn("foo a b", index.candidates(names, "foo"))

    def test_unicode_including_maximum_code_point(self):
        index = PrefixIndex()
        names = ["npc_\U0010ffffx", "npc_я", "npc_\U0010ffff", "\U0010ffffx", "я_а", "😀_x"]
        for prefix in ("", "npc_", "npc_\U0010ffff", "\U0010ffff", "я", "😀_", "不存在"):
            self.assert_matches_scan(index, names, prefix)

    def test_empty_registry_then_append(self):
        index = PrefixIndex()
        names = []
        self.assert_matches_scan(index, names, "npc_")
        names.append("npc_a")
        self.assert_matches_scan(index, names, "npc_")
        self.assertEqual(index.rebuilds, 1)

    def test_rebuild_only_after_tail_limit_is_exceeded(self):
        index = PrefixIndex()
        names = ["npc_base"]
        self.assert_matches_scan(index, names, "npc_")
        names.extend("npc_%04d" % number for number in range(1024))
        self.assert_matches_scan(index, names, "npc_")
        self.assertEqual(index.rebuilds, 1)
        names.append("npc_base")
        self.assert_matches_scan(index, names, "npc_")
        self.assertEqual(index.rebuilds, 2)

    def test_registry_identity_replacement(self):
        index = PrefixIndex()
        names = ["npc_a", "other"]
        self.assert_matches_scan(index, names, "npc_")
        replacement = list(names)
        self.assert_matches_scan(index, replacement, "npc_")
        self.assertEqual(index.rebuilds, 2)

    def test_shrink_detected_even_inside_unindexed_tail(self):
        index = PrefixIndex()
        names = ["npc_a", "npc_b"]
        self.assert_matches_scan(index, names, "npc_")
        names.extend(["npc_c", "npc_d", "npc_e"])
        self.assert_matches_scan(index, names, "npc_")
        del names[-2:]
        self.assert_matches_scan(index, names, "npc_")
        self.assertEqual(index.rebuilds, 2)
        names.clear()
        self.assert_matches_scan(index, names, "")
        self.assertEqual(index.rebuilds, 3)

    def test_clear_releases_references_and_reindexes(self):
        index = PrefixIndex()
        names = ["npc_b", "npc_a"]
        self.assert_matches_scan(index, names, "npc_")
        index.clear()
        self.assertIsNone(index._source)
        self.assertEqual(index._sorted_pairs, [])
        self.assertEqual(index._bulk_count, 0)
        self.assertEqual(index._observed_count, 0)
        self.assertEqual(index._tail_pairs, [])
        self.assertEqual(index._tail_count, 0)
        self.assertEqual((index.queries, index.rebuilds), (1, 1))
        names.reverse()
        self.assert_matches_scan(index, names, "npc_")
        self.assertEqual((index.queries, index.rebuilds), (2, 2))

    def test_returned_list_can_be_mutated_without_affecting_index(self):
        index = PrefixIndex()
        names = ["npc_a", "npc_b"]
        result = index.candidates(names, "npc_")
        result.clear()
        self.assert_matches_scan(index, names, "npc_")

    def test_zero_tail_limit(self):
        index = PrefixIndex(tail_limit=0)
        names = []
        for name in ["npc_b", "npc_a", "npc_b"]:
            names.append(name)
            self.assert_matches_scan(index, names, "npc_")
        self.assertEqual(index.rebuilds, 3)

    def test_multiple_queries_before_and_after_tail_append(self):
        index = PrefixIndex()
        names = ['npc_a']
        self.assert_matches_scan(index, names, 'npc_')
        names.extend(['npc_b', 'other', 'npc_b'])
        self.assert_matches_scan(index, names, 'npc_')
        self.assert_matches_scan(index, names, 'other')
        self.assert_matches_scan(index, names, 'missing')
        names.append('npc_c')
        self.assert_matches_scan(index, names, 'npc_')
        self.assert_matches_scan(index, names, 'npc_c')

    def test_invalid_tail_limit(self):
        for value in (-1, 1.5, "1024", None):
            with self.assertRaises(ValueError):
                PrefixIndex(value)

    def test_random_append_only_fuzz(self):
        alphabet = "abc_ я😀\U0010ffff"
        for seed in range(6):
            random_source = random.Random(seed)
            index = PrefixIndex(tail_limit=13 if seed % 2 else 1024)
            names = []
            for iteration in range(1200):
                for unused in range(random_source.randrange(4)):
                    if names and random_source.randrange(4) == 0:
                        names.append(random_source.choice(names))
                    else:
                        names.append("".join(random_source.choices(alphabet, k=random_source.randrange(12))))
                if names and random_source.randrange(5):
                    chosen = random_source.choice(names)
                    prefix = chosen[:random_source.randrange(len(chosen) + 1)]
                else:
                    prefix = "missing_%d" % iteration
                self.assert_matches_scan(index, names, prefix)


if __name__ == "__main__":
    unittest.main()
