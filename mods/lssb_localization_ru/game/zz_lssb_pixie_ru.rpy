# Display-only translation; native game variables and branches stay unchanged.
init 1089 python in lssb_pixie:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_pixie_ru'
    strings = {"Take Morgan's side": 'Поддержать Морган', "Takes Kleio's side": 'Поддержать Клео', "Don't pick a side": 'Не выбирать сторону', 'Choose Morgan': 'Выбрать Морган', 'Choose Kleio': 'Выбрать Клео', 'Cum inside': 'Кончить внутрь', 'Share the love': 'Поделиться любовью', 'Accept': 'Согласиться', 'Refuse': 'Отказаться', 'Fuck her pussy': 'Трахнуть её в киску', 'Fuck her ass': 'Трахнуть её в задницу', 'Give Morgan some attention': 'Уделить внимание Морган', 'Ask for a blowjob': 'Попросить минет', 'Give Kleio some attention': 'Уделить внимание Клео', 'Go on for the main course': 'Перейти к главному блюду', 'They keep going!': 'Они продолжают!', 'They listen': 'Они слушаются', 'Fuck Morgan': 'Трахнуть Морган', 'Fuck Kleio': 'Трахнуть Клео', 'Pull out': 'Вынуть член'}
    aliases = {'Поддержать Клейо': 'Поддержать Клео', 'Выбрать Клейо': 'Выбрать Клео', 'Уделить внимание Клейо': 'Уделить внимание Клео', 'Трахнуть Клейо': 'Трахнуть Клео', 'Вытащить': 'Вынуть член'}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems_full/pixie/events.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_office_common.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1090 python:
    config.language_callbacks['russian'].append(lssb_pixie.enter)
    for _lssb_pixie_language in set(renpy.known_languages()) | {None}:
        if _lssb_pixie_language != 'russian':config.language_callbacks[_lssb_pixie_language].append(lssb_pixie.leave)

screen choice(items):
    variant 'lssb_pixie_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_pixie.caption(i.caption) action i.action
