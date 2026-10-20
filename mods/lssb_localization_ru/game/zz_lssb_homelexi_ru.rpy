# Display-only translation; native game variables and branches stay unchanged.
init 1109 python in lssb_homelexi:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_homelexi_ru'
    strings = {'Cum in her mouth': 'Кончить ей в рот', "Cum in Lexi's mouth": 'Кончить Лекси в рот', 'Cum inside': 'Кончить внутрь', "Cum over Lexi and Sasha's faces": 'Кончить Лекси и Саше на лица', 'Fuck [bree.name]': '[lssb_homelexi.bree_name()]: заняться сексом', 'Fuck her ass': 'Трахнуть её в попку', 'Fuck her pussy': 'Трахнуть её в киску', 'Fuck Lexi': 'Трахнуть Лекси', 'Go for Sasha': 'Выбрать Сашу', 'Let Lexi take the initiative': 'Отдать инициативу Лекси', 'Pull out': 'Вынуть'}
    aliases = {'Трахнуть [bree.name]': '[lssb_homelexi.bree_name()]: заняться сексом', 'Трахнуть её в задницу': 'Трахнуть её в попку', 'Вытащить': 'Вынуть', 'Позволить Лекси взять инициативу': 'Отдать инициативу Лекси', 'Кончить на лица Лекси и Саши': 'Кончить Лекси и Саше на лица'}
    def bree_name():
        return store.lssb_beach.bree_name()
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems/home/events/home_harem_lexi.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_halloween.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1110 python:
    config.language_callbacks['russian'].append(lssb_homelexi.enter)
    for _lssb_homelexi_language in set(renpy.known_languages()) | {None}:
        if _lssb_homelexi_language != 'russian':config.language_callbacks[_lssb_homelexi_language].append(lssb_homelexi.leave)

screen choice(items):
    variant 'lssb_homelexi_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_homelexi.caption(i.caption) action i.action
