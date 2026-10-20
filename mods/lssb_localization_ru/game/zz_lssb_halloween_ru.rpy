# Display-only translation; native game variables and branches stay unchanged.
init 1107 python in lssb_halloween:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_halloween_ru'
    strings = {'Agree with [bree.name]': '[lssb_halloween.bree_name()] права', 'Agree with Sasha': 'Согласиться с Сашей', 'Dance with [bree.name]': '[lssb_halloween.bree_name()]: пригласить на танец', 'Dance with Lexi': 'Потанцевать с Лекси', 'Dance with Minami': 'Потанцевать с Минами', 'Dance with Samantha': 'Потанцевать с Самантой', 'Dance with Sasha': 'Потанцевать с Сашей', 'Jump at the chance of the party': 'С радостью согласиться на вечеринку', 'Side with [bree.name] and Sasha': '[lssb_halloween.bree_name()] и Саша правы', 'Side with Jack and Scottie': 'Поддержать Джека и Скотти', 'Turn down the party': 'Отказаться от вечеринки'}
    aliases = {'Согласиться с [bree.name]': '[lssb_halloween.bree_name()] права', 'Поддержать [bree.name] и Сашу': '[lssb_halloween.bree_name()] и Саша правы', 'Танцевать с [bree.name]': '[lssb_halloween.bree_name()]: пригласить на танец', 'Танцевать с Сашей': 'Потанцевать с Сашей', 'Танцевать с Минами': 'Потанцевать с Минами', 'Танцевать с Самантой': 'Потанцевать с Самантой', 'Танцевать с Лекси': 'Потанцевать с Лекси'}
    def bree_name():
        return store.lssb_beach.bree_name()
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems/home/events/home_harem_halloween_event.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_homecommon.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1108 python:
    config.language_callbacks['russian'].append(lssb_halloween.enter)
    for _lssb_halloween_language in set(renpy.known_languages()) | {None}:
        if _lssb_halloween_language != 'russian':config.language_callbacks[_lssb_halloween_language].append(lssb_halloween.leave)

screen choice(items):
    variant 'lssb_halloween_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_halloween.caption(i.caption) action i.action
