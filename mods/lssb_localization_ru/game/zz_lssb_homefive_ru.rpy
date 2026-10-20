# Display-only translation; native game variables and branches stay unchanged.
init 1101 python in lssb_homefive:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_homefive_ru'
    strings = {'Sasha': 'Саша', 'Samantha': 'Саманта', '[bree.name]': '[lssb_homefive.bree_name()]', 'Minami': 'Минами', 'Lexi': 'Лекси', 'Cum in her mouth.': 'Кончить ей в рот', 'Cum on her face.': 'Кончить ей на лицо', 'Fuck her ass': 'Трахнуть её в задницу', 'Fuck her pussy': 'Трахнуть её в киску', 'Cum inside': 'Кончить внутрь', 'Pull out': 'Вынуть член'}
    aliases = {'Вытащить': 'Вынуть член'}
    def bree_name():
        return store.lssb_beach.bree_name()
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems/home/events/home_harem_bree_lexi_minami_samantha_sasha.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_beach.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1102 python:
    config.language_callbacks['russian'].append(lssb_homefive.enter)
    for _lssb_homefive_language in set(renpy.known_languages()) | {None}:
        if _lssb_homefive_language != 'russian':config.language_callbacks[_lssb_homefive_language].append(lssb_homefive.leave)

screen choice(items):
    variant 'lssb_homefive_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_homefive.caption(i.caption) action i.action
