# Display-only translation; native game variables and branches stay unchanged.
init 1085 python in lssb_office_christmas:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_office_christmas_ru'
    strings = {'Dance with Aletta': 'Танцевать с Алеттой', 'Dance with Audrey': 'Танцевать с Одри', 'Dance with Lavish': 'Танцевать с Лавиш', 'Dance with Shiori': 'Танцевать с Сиори', 'Dance with Cherie': 'Танцевать с Шери', 'Kiss Aletta': 'Поцеловать Алетту', 'Kiss Audrey': 'Поцеловать Одри', 'Kiss Lavish': 'Поцеловать Лавиш', 'Kiss Shiori': 'Поцеловать Сиори', 'Kiss Cherie': 'Поцеловать Шери', 'Help Aletta': 'Помочь Алетте', 'Ignore Aletta': 'Проигнорировать Алетту', 'Help Audrey': 'Помочь Одри', 'Ignore Audrey': 'Проигнорировать Одри', 'Help Lavish': 'Помочь Лавиш', 'Ignore Lavish': 'Проигнорировать Лавиш', 'Help Shiori': 'Помочь Сиори', 'Ignore Shiori': 'Проигнорировать Сиори', 'Approach Aletta': 'Подойти к Алетте', 'Approach Audrey': 'Подойти к Одри', 'Approach Lavish': 'Подойти к Лавиш', 'Approach Shiori': 'Подойти к Сиори', 'Approach Cassidy': 'Подойти к Кэссиди', 'Approach Cherie': 'Подойти к Шери', 'Walk away': 'Уйти', 'Step in': 'Вмешаться', 'Watch': 'Смотреть'}
    aliases = {}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems_full/office/events/office_christmas_party.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_office_events.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1086 python:
    config.language_callbacks['russian'].append(lssb_office_christmas.enter)
    for _lssb_office_christmas_language in set(renpy.known_languages()) | {None}:
        if _lssb_office_christmas_language != 'russian':config.language_callbacks[_lssb_office_christmas_language].append(lssb_office_christmas.leave)

screen choice(items):
    variant 'lssb_office_christmas_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_office_christmas.caption(i.caption) action i.action
