# Display-only translation; native game variables and branches stay unchanged.
init 1081 python in lssb_jealous:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_jealous_ru'
    strings = {'Admit cheating': 'Признаться в измене', 'Deny cheating': 'Отрицать измену', "I'll see if Sasha is interested.": 'Я спрошу, согласна ли Саша.', 'I could never ask Sasha for that!': 'Я не могу предложить Саше такое!', 'Have Audrey give me a blowjob': 'Пусть Одри сделает мне минет', 'Have Sasha give me a blowjob': 'Пусть Саша сделает мне минет', "Cum in Audrey's mouth": 'Кончить Одри в рот', "Cum on Audrey's face": 'Кончить Одри на лицо', "Cum in Sasha's mouth": 'Кончить Саше в рот', "Cum on Sasha's face": 'Кончить Саше на лицо', 'Fuck Audrey': 'Трахнуть Одри', 'Fuck Sasha': 'Трахнуть Сашу', 'Fuck Audrey up the ass': 'Трахнуть Одри в задницу', 'Fuck Audrey in the pussy': 'Трахнуть Одри в киску', "Cum inside Audrey's ass": 'Кончить Одри в задницу', 'Cum outside': 'Кончить снаружи', "Cum inside Audrey's pussy": 'Кончить Одри в киску', 'Fuck Sasha up the ass': 'Трахнуть Сашу в задницу', 'Fuck Sasha in the pussy': 'Трахнуть Сашу в киску', "Cum in Sasha's ass": 'Кончить Саше в задницу', 'Cum over Sasha and Audrey': 'Кончить на Сашу и Одри', "Cum in Sasha's pussy": 'Кончить Саше в киску'}
    aliases = {'Я спрошу, интересно ли это Саше': 'Я спрошу, согласна ли Саша.', 'Я никогда не смогу попросить Сашу о таком!': 'Я не могу предложить Саше такое!', 'Кончить в рот Саши': 'Кончить Саше в рот', 'Кончить внутрь задницы Одри': 'Кончить Одри в задницу', 'Кончить внутрь киски Одри': 'Кончить Одри в киску', 'Кончить в задницу Саши': 'Кончить Саше в задницу', 'Кончить в киску Саши': 'Кончить Саше в киску'}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith(('ch/harems_full/jealous/',)):
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_jail.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1082 python:
    config.language_callbacks['russian'].append(lssb_jealous.enter)
    for _lssb_jealous_language in set(renpy.known_languages()) | {None}:
        if _lssb_jealous_language != 'russian':config.language_callbacks[_lssb_jealous_language].append(lssb_jealous.leave)

screen choice(items):
    variant 'lssb_jealous_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_jealous.caption(i.caption) action i.action
