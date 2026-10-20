# Display-only translation; native game variables and branches stay unchanged.
init 1083 python in lssb_office_events:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_office_events_ru'
    strings = {'Agree': 'Согласиться', 'Refuse': 'Отказаться', 'Offer all three': 'Предложить всех троих', 'Offer Shiori': 'Предложить Сиори', 'Offer Audrey': 'Предложить Одри', 'Offer Lavish': 'Предложить Лавиш', 'Offer Aletta': 'Предложить Алетту', 'Fuck Audrey': 'Трахнуть Одри', 'Fuck Shiori': 'Трахнуть Сиори', 'Fuck her ass': 'Трахнуть её в задницу', 'Fuck her pussy': 'Трахнуть её в киску', 'Cum inside': 'Кончить внутрь', 'Cum outside': 'Кончить снаружи', 'Share the love': 'Поделиться любовью', 'Pull out': 'Вынуть член', 'Do not stop Audrey': 'Не останавливать Одри', 'Stop Audrey': 'Остановить Одри', 'Fuck Lavish': 'Трахнуть Лавиш', 'Use a condom': 'Использовать презерватив', 'Do not use a condom': 'Не использовать презерватив', 'Fuck Aletta': 'Трахнуть Алетту', 'Cum on Aletta': 'Кончить на Алетту', 'Cum on Audrey': 'Кончить на Одри', 'Cum on Lavish': 'Кончить на Лавиш', 'Cum on Shiori': 'Кончить на Сиори'}
    aliases = {'Вытащить': 'Вынуть член'}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems_full/office/events/events.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_jealous.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1084 python:
    config.language_callbacks['russian'].append(lssb_office_events.enter)
    for _lssb_office_events_language in set(renpy.known_languages()) | {None}:
        if _lssb_office_events_language != 'russian':config.language_callbacks[_lssb_office_events_language].append(lssb_office_events.leave)

screen choice(items):
    variant 'lssb_office_events_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_office_events.caption(i.caption) action i.action
