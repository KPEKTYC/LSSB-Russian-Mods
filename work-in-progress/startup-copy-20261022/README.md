# Startup copy experiment — uninstalled

This checkpoint is excluded from builds. The selected startup candidate only
changes image-prefix indexing; it does not patch `copy` or rollback containers.

The copy experiment passed 12 host tests and six cases against real Ren'Py
rollback containers. Complete gallery clones had identical pickle bytes in the
tested engine. These are bounded correctness checks, not proof of all gameplay.

Timing did not justify selecting this larger patch. On 2026-10-22 the controlled
three-run medians were 25.090 seconds with native copying, 24.802 with the full
experiment and 24.953 with only the built-in-container optimization. The separate
graph timing depended on order: copying the actual init input first with the
experiment took 2.069 seconds, then native copying took 1.798 seconds. An earlier
test in the opposite order favored the experiment. Allocator/cache/order effects
must not be reported as a proven startup improvement.

Engine/game: Ren'Py 8.5.3.26051504 / LSSB 26.9.0e. No original game archives,
saves, extracted native scripts or signing keys are included here.

Tests: `python -m unittest discover -s tools/startup -p "test_*.py"`.
The engine cases in `tools/startup/engine_copy_cases.py` need the isolated
engine harness. Full local logs remain outside this repository.

Copyright (c) 2026 KPEKTYC. LSSB Noncommercial Attribution License 1.0.
