# Display-only translation; native game variables and branches stay unchanged.
init 1111 python in lssb_homeminami:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_homeminami_ru'
    strings = {"Cum in [bree.name]'s ass": '[lssb_homeminami.bree_name()]: кончить в попку', "Cum in [bree.name]'s pussy": '[lssb_homeminami.bree_name()]: кончить в киску', 'Cum in her mouth': 'Кончить ей в рот', "Cum in Minami's ass": 'Кончить Минами в попку', "Cum in Minami's pussy": 'Кончить Минами в киску', "Cum in Sasha's ass": 'Кончить Саше в попку', "Cum in Sasha's pussy": 'Кончить Саше в киску', 'Cum inside': 'Кончить внутрь', 'Cum inside Minami': 'Кончить в Минами', 'Cum on her face': 'Кончить ей на лицо', 'Cum on their face': 'Кончить им на лица', 'Cum on their faces': 'Кончить им на лица', 'Cum outside': 'Кончить снаружи', 'Fuck [bree.name]': '[lssb_homeminami.bree_name()]: заняться сексом', "Fuck [bree.name]'s ass": '[lssb_homeminami.bree_name()]: трахнуть в попку', "Fuck [bree.name]'s pussy": '[lssb_homeminami.bree_name()]: трахнуть в киску', 'Fuck her ass': 'Трахнуть её в попку', 'Fuck her pussy': 'Трахнуть её в киску', 'Fuck Minami': 'Трахнуть Минами', "Fuck Minami's ass": 'Трахнуть Минами в попку', "Fuck Minami's pussy": 'Трахнуть Минами в киску', 'Fuck Sasha instead': 'Вместо этого трахнуть Сашу', "Fuck Sasha's ass": 'Трахнуть Сашу в попку', "Fuck Sasha's pussy": 'Трахнуть Сашу в киску', 'Fuck them': 'Трахнуть их', "I can't do that": 'Я не могу этого сделать', 'I have to ask the girls.': 'Мне нужно спросить девушек.', "I'm up for a sandwich": 'Я за сэндвич', 'Just get out!': 'Просто убирайся!', 'Just look': 'Просто смотреть', "Lick [bree.name]'s ass": '[lssb_homeminami.bree_name()]: вылизать попку', "Lick [bree.name]'s pussy": '[lssb_homeminami.bree_name()]: вылизать киску', "Lick Minami's ass": 'Вылизать попку Минами', "Lick Minami's pussy": 'Вылизать киску Минами', "Lick Sasha's ass": 'Вылизать попку Саши', "Lick Sasha's pussy": 'Вылизать киску Саши', 'Pull out': 'Вынуть', 'Stack them': 'Уложить их друг на друга', 'Use anal beads on [bree.name]': '[lssb_homeminami.bree_name()]: анальные шарики', 'Use anal beads on Minami': 'Использовать анальные шарики на Минами', 'Use anal beads on Sasha': 'Использовать анальные шарики на Саше', 'Use double dildo on [bree.name]': '[lssb_homeminami.bree_name()]: двойной фаллоимитатор', 'Use double dildo on both girls': 'Использовать двойной фаллоимитатор на обеих', 'Use double dildo on Minami': 'Использовать двойной фаллоимитатор на Минами', 'You will get what you deserve.': 'Ты получишь по заслугам.'}
    aliases = {'Я не могу так поступить': 'Я не могу этого сделать', 'Мне нужно спросить девушек': 'Мне нужно спросить девушек.', 'Ты получишь по заслугам': 'Ты получишь по заслугам.', 'Трахнуть [bree.name]': '[lssb_homeminami.bree_name()]: заняться сексом', 'Поставить их друг на друга': 'Уложить их друг на друга', 'Трахнуть её в задницу': 'Трахнуть её в попку', 'Лизать задницу [bree.name]': '[lssb_homeminami.bree_name()]: вылизать попку', 'Лизать киску [bree.name]': '[lssb_homeminami.bree_name()]: вылизать киску', 'Лизать задницу Минами': 'Вылизать попку Минами', 'Лизать киску Минами': 'Вылизать киску Минами', 'Использовать анальные шарики на [bree.name]': '[lssb_homeminami.bree_name()]: анальные шарики', 'Использовать двойной дилдо на [bree.name]': '[lssb_homeminami.bree_name()]: двойной фаллоимитатор', 'Использовать двойной дилдо на Минами': 'Использовать двойной фаллоимитатор на Минами', 'Использовать двойной дилдо на обеих девушках': 'Использовать двойной фаллоимитатор на обеих', 'Трахнуть [bree.name] в киску': '[lssb_homeminami.bree_name()]: трахнуть в киску', 'Трахнуть [bree.name] в задницу': '[lssb_homeminami.bree_name()]: трахнуть в попку', 'Трахнуть Минами в задницу': 'Трахнуть Минами в попку', 'Кончить в задницу [bree.name]': '[lssb_homeminami.bree_name()]: кончить в попку', 'Кончить в киску [bree.name]': '[lssb_homeminami.bree_name()]: кончить в киску', 'Кончить в задницу Минами': 'Кончить Минами в попку', 'Кончить в киску Минами': 'Кончить Минами в киску', 'Кончить им на лицо': 'Кончить им на лица', 'Я не против сэндвича': 'Я за сэндвич', 'Лизать киску Саши': 'Вылизать киску Саши', 'Лизать задницу Саши': 'Вылизать попку Саши', 'Вытащить': 'Вынуть', 'Трахнуть Сашу в задницу': 'Трахнуть Сашу в попку', 'Кончить в задницу Саши': 'Кончить Саше в попку', 'Кончить в киску Саши': 'Кончить Саше в киску', 'Кончить внутрь Минами': 'Кончить в Минами'}
    def bree_name():
        return store.lssb_beach.bree_name()
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems/home/events/home_harem_minami.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_homelexi.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1112 python:
    config.language_callbacks['russian'].append(lssb_homeminami.enter)
    for _lssb_homeminami_language in set(renpy.known_languages()) | {None}:
        if _lssb_homeminami_language != 'russian':config.language_callbacks[_lssb_homeminami_language].append(lssb_homeminami.leave)

screen choice(items):
    variant 'lssb_homeminami_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_homeminami.caption(i.caption) action i.action
