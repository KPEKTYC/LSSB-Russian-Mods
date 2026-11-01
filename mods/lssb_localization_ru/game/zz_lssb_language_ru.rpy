# A forgotten loose base from 1.89.0 or earlier repeats every string, and the engine
# raises once per repeat. Only then let the later definition win, as dialogue does.
init -1000 python hide:
    import os
    import renpy as engine
    native_add = getattr(getattr(engine.translation, "StringTranslator", None), "add", None)
    if native_add and any(os.path.isfile(os.path.join(config.gamedir, "tl/russian/gamepatchanalyzer" + ext)) for ext in (".rpy", ".rpyc")):
        def add(self, old, new, newloc):
            self.translations.pop(old, None)
            native_add(self, old, new, newloc)
        engine.translation.StringTranslator.add = add

# Default language for the standalone Russian localization.
init 999 python:
    config.default_language = "russian"
    # Switch a profile from before the mod once; after that the player's choice stands.
    if not persistent.lssb_language_applied:
        persistent.lssb_language_applied = True
        config.language = "russian"
