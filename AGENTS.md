# Scope

This monorepo contains our Russian localization, in-game mod manager,
visual/map/interface improvements, and startup optimization for LSSB.

- Do not add, modify, or translate the third-party Daerty wiki mod.
- Do not commit original game archives, extracted native scripts, saves,
  credentials, caches, historical installers, or unrelated projects.
- Preserve installed game files. Build and validate in isolated directories.
- Compatibility uses structural/API contracts and safe fallback. Never remove
  guards merely to accept a new version string.
- Keep reviewed changes and uninstalled work in progress distinct.
- Only `mods/` enters the build. `work-in-progress/` is a saved checkpoint.
- Never shut down the computer unless the user explicitly requests it anew.

Run `python tools/verify_repository.py` and
`python -m unittest discover -s tools/manager -p "test_*.py"` before publishing.
