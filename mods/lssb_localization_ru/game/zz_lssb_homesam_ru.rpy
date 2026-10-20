# Display-only translation; native game variables and branches stay unchanged.
init 1113 python in lssb_homesam:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_homesam_ru'
    strings = {"Don't watch": 'Не смотреть', 'Watch': 'Смотреть', 'Masturbate': 'Мастурбировать', 'Just watch': 'Просто смотреть', 'Just keep watching': 'Продолжать смотреть', 'Turn her away': 'Отказать ей', "Take the bed, I'll sleep on the floor": 'Ложись на кровать, а я посплю на полу', "I'll make some space": 'Я подвинусь', 'Jab her in the ribs': 'Толкнуть её локтем под рёбра', 'Enjoy the moment': 'Насладиться моментом', 'Let her sleep': 'Дать ей поспать', 'Let Samantha play with you': 'Позволить Саманте ласкать тебя', 'Fuck Samantha': 'Трахнуть Саманту', "Cum in [bree.name]'s mouth": '[lssb_homesam.bree_name()]: кончить ей в рот', "Cum in Samantha's mouth": 'Кончить Саманте в рот', "Cum in Sasha's mouth": 'Кончить Саше в рот', 'Just cum': 'Просто кончить'}
    aliases = {'Просто продолжать смотреть': 'Продолжать смотреть', 'Отвернуть её': 'Отказать ей', 'Забирай кровать, я посплю на полу': 'Ложись на кровать, а я посплю на полу', 'Я освобожу немного места': 'Я подвинусь', 'Ткнуть её локтем в рёбра': 'Толкнуть её локтем под рёбра', 'Позволить ей спать': 'Дать ей поспать', 'Позволить Саманте поиграть с тобой': 'Позволить Саманте ласкать тебя', 'Кончить в рот [bree.name]': '[lssb_homesam.bree_name()]: кончить ей в рот', 'Кончить в рот Саманты': 'Кончить Саманте в рот', 'Кончить в рот Саши': 'Кончить Саше в рот'}
    def bree_name():
        return store.lssb_beach.bree_name()
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems/home/events/home_harem_samantha.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_homeminami.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1114 python:
    config.language_callbacks['russian'].append(lssb_homesam.enter)
    for _lssb_homesam_language in set(renpy.known_languages()) | {None}:
        if _lssb_homesam_language != 'russian':config.language_callbacks[_lssb_homesam_language].append(lssb_homesam.leave)

screen choice(items):
    variant 'lssb_homesam_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_homesam.caption(i.caption) action i.action
