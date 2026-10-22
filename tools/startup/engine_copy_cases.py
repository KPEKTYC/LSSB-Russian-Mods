"""Run against Ren'Py's real rollback classes in an isolated engine process."""
import copy
import copyreg
from types import SimpleNamespace


def verify(optimizer, revertable, game):
    checks = []
    rd, rl = revertable.RevertableDict, revertable.RevertableList

    def cases():
        result = []
        d, items = rd(), rl()
        d['items'] = items
        d['same'] = items
        items.extend([1, d])
        clone = copy.deepcopy(d)
        assert type(clone) is rd and type(clone['items']) is rl
        assert clone['items'] is clone['same'] and clone['items'][1] is clone
        assert clone['items'] is not items
        assert game.log.mutated[id(clone)][0]() is clone
        assert game.log.mutated[id(clone)][1] == []
        assert game.log.mutated[id(clone['items'])][1] == []
        result.append('cycles, aliases, independent rollback objects and clean snapshots')

        stateful = rd(a=1)
        stateful.extra = [stateful]
        clone = copy.deepcopy(stateful)
        assert clone.extra[0] is clone
        result.append('stateful reducer fallback')

        hooked = rl([1])
        hooked.__deepcopy__ = lambda memo: 'hook result'
        assert copy.deepcopy(hooked) == 'hook result'
        result.append('instance deepcopy hook')

        root = rd()
        class ResetLog:
            def __deepcopy__(self, memo):
                game.log.mutated.pop(id(memo[id(root)]), None)
                return 2
        root['first'] = 1
        root['second'] = ResetLog()
        clone = copy.deepcopy(root)
        assert clone == {'first': 1, 'second': 2}
        assert game.log.mutated[id(clone)][1] == [('first', 1)]
        result.append('rollback log invalidated by a deepcopy hook')

        old_append = rl.append
        class ChangeAppend:
            def __deepcopy__(self, memo):
                rl.append = lambda self, value: list.append(self, 'foreign')
                return 3
        try:
            clone = copy.deepcopy(rl([ChangeAppend(), 4]))
            assert clone == ['foreign', 'foreign']
        finally:
            rl.append = old_append
        result.append('native dynamic append semantics during hook mutation')

        old_reducer = copyreg.dispatch_table.get(rd)
        try:
            copyreg.pickle(rd, lambda value: (dict, (), None, None, iter([('registered', 5)])))
            assert copy.deepcopy(rd(a=1)) == {'registered': 5}
        finally:
            if old_reducer is None:
                copyreg.dispatch_table.pop(rd, None)
            else:
                copyreg.dispatch_table[rd] = old_reducer
        result.append('registered reducer fallback')
        return result

    optimizer.cleanup()
    original_log = game.log
    try:
        # Existing startup logs may retain IDs of freed objects. Give both
        # implementations the same fresh log; never clear the game's real log.
        game.log = SimpleNamespace(mutated={})
        expected = cases()
        game.log = SimpleNamespace(mutated={})
        assert optimizer.install()
        assert optimizer.install_containers(revertable, game)
        actual = cases()
        assert actual == expected
        checks.extend(actual)
    finally:
        optimizer.cleanup()
        game.log = original_log
    return checks
