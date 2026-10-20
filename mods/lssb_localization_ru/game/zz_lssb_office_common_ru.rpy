# Display-only translation; native game variables and branches stay unchanged.
init 1087 python in lssb_office_common:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_office_common_ru'
    strings = {'Doing it right now': 'Уже делаю', 'Not now': 'Не сейчас', "Shut up while I'm on the phone!": 'Заткнись, я разговариваю по телефону!', 'Call Lavish and Shiori': 'Позвонить Лавиш и Сиори', 'Call Lavish only': 'Позвонить только Лавиш', 'Call Shiori only': 'Позвонить только Сиори', "I'll deal with them later.": 'Я разберусь с ними позже', "Teamwork... Efficiency... I'm calling!": 'Командная работа... Эффективность... Звоню!', 'Call Audrey only': 'Позвонить только Одри', "That's a one to one meeting.": 'Это встреча один на один', "Let's start a team review.": 'Давайте начнём командный разбор', 'Hot coffee?': '«Горячий кофе»?', "I'll deal with her later.": 'Я разберусь с ней позже'}
    aliases = {}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems_full/office/events/office_harem_common.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_office_christmas.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1088 python:
    config.language_callbacks['russian'].append(lssb_office_common.enter)
    for _lssb_office_common_language in set(renpy.known_languages()) | {None}:
        if _lssb_office_common_language != 'russian':config.language_callbacks[_lssb_office_common_language].append(lssb_office_common.leave)

screen choice(items):
    variant 'lssb_office_common_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_office_common.caption(i.caption) action i.action
