# Display-only translation; native game variables and branches stay unchanged.
init 1079 python in lssb_jail:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_jail_ru'
    strings = {}
    aliases = {}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith(('ch/harems_full/jail/',)):
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_goodevil.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1080 python:
    config.language_callbacks['russian'].append(lssb_jail.enter)
    for _lssb_jail_language in set(renpy.known_languages()) | {None}:
        if _lssb_jail_language != 'russian':config.language_callbacks[_lssb_jail_language].append(lssb_jail.leave)

screen choice(items):
    variant 'lssb_jail_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_jail.caption(i.caption) action i.action
