# Display-only translation; native game variables and branches stay unchanged.
init 1075 python in lssb_gaming:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_gaming_ru'
    strings = {'Refuse': 'Отказаться', 'Accept': 'Согласиться', 'Fuck [bree.name]': 'Трахнуть [bree.name]', 'Fuck Kat': 'Трахнуть Кэт', 'Fuck her pussy': 'Трахнуть её в киску', 'Fuck her ass': 'Трахнуть её в задницу', 'Cum inside': 'Кончить внутрь', 'Pull out': 'Вынуть член'}
    aliases = {'Вытащить': 'Вынуть член'}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith(('ch/harems_full/gaming/',)):
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_fashion.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1076 python:
    config.language_callbacks['russian'].append(lssb_gaming.enter)
    for _lssb_gaming_language in set(renpy.known_languages()) | {None}:
        if _lssb_gaming_language != 'russian':config.language_callbacks[_lssb_gaming_language].append(lssb_gaming.leave)

screen choice(items):
    variant 'lssb_gaming_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_gaming.caption(i.caption) action i.action
