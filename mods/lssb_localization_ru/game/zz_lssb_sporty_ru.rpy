# Display-only translation; native game variables and branches stay unchanged.
init 1091 python in lssb_sporty:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_sporty_ru'
    strings = {"Cum in Ayesha's mouth": 'Кончить Айше в рот', "Cum in Hanna's mouth": 'Кончить Ханне в рот', 'Cum on their faces': 'Кончить им на лица', 'Double facial': 'Кончить на лица обеих'}
    aliases = {'Кончить Айеше в рот': 'Кончить Айше в рот'}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems_full/sporty/events.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_pixie.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1092 python:
    config.language_callbacks['russian'].append(lssb_sporty.enter)
    for _lssb_sporty_language in set(renpy.known_languages()) | {None}:
        if _lssb_sporty_language != 'russian':config.language_callbacks[_lssb_sporty_language].append(lssb_sporty.leave)

screen choice(items):
    variant 'lssb_sporty_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_sporty.caption(i.caption) action i.action
