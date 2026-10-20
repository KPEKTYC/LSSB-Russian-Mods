# Presentation only. Preserve native names, scene statements and menu actions.
init 1035 python in lssb_jack:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_jack_ru'
    strings = {'Defend [bree.name]': 'Защитить [bree.name]', 'Defend Sasha': 'Защитить Сашу', 'Side with [bree.name]': 'Поддержать [bree.name]', 'Side with Sasha': 'Поддержать Сашу', "Look at [bree.name]'s dice": 'Посмотреть на кубики [bree.name]', "Look at Sasha's dice": 'Посмотреть на кубики Саши', 'Jack gives [bree.name] enough XP to level up': 'Джек даёт [bree.name] достаточно опыта для повышения уровня', 'Jack gives Sasha enough XP to level up': 'Джек даёт Саше достаточно опыта для повышения уровня', "Ask to share [bree.name]'s bedroll": 'Попроситься в спальный мешок к [bree.name]', "Ask to share Sasha's bedroll": 'Попроситься в спальный мешок к Саше', "Ask to share Minami's bedroll": 'Попроситься в спальный мешок к Минами', 'I will rough it out alone': 'Переночевать одному'}
    def day_text(value):
        if engine.game.preferences.language != 'russian':return value
        return {'monday':'понедельник','tuesday':'вторник','wednesday':'среда',
            'thursday':'четверг','friday':'пятница','saturday':'суббота','sunday':'воскресенье'}.get(str(value).lower(),value)

    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node = engine.game.script.namemap.get(engine.game.context().current)
        filename = getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith('ch/jack/'):return strings.get(value,value)
        return store.lssb_harmony.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1036 python:
    config.language_callbacks['russian'].append(lssb_jack.enter)
    for _lssb_jack_language in set(renpy.known_languages()) | {None}:
        if _lssb_jack_language != 'russian':
            config.language_callbacks[_lssb_jack_language].append(lssb_jack.leave)

screen choice(items):
    variant 'lssb_jack_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_jack.caption(i.caption) action i.action
