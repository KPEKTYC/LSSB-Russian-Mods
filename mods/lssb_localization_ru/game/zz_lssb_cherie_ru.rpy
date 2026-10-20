# Presentation only. Preserve native names, scene statements and menu actions.
init 1027 python in lssb_cherie:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_cherie_ru'
    strings = {'Ma Cherie, they are real!': 'Ма Шери, они настоящие!', "Look, it's complicated": 'Послушайте, всё сложно', 'Stop her physically': 'Остановить её силой', 'Ask her to wait': 'Попросить её подождать', "I'll make sure you're not alone": 'Я позабочусь о том, чтобы вы не остались одна', 'No promises, then': 'Тогда без обещаний', "Don't hesitate. Yes": 'Согласиться без колебаний', 'Hesitate. Yes': 'Согласиться после колебаний', 'No': 'Нет', 'Yes': 'Да', 'Okay': 'Хорошо', "That's not what you really want": 'На самом деле вы хотите не этого', 'Step in': 'Вмешаться', 'Wait': 'Подождать', 'It will be fine': 'Всё будет хорошо', 'Better find another place': 'Лучше найти другое место'}
    nicknames = {'amour':'любимый','cochonet':'поросёнок',
        'master':'хозяин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'amour':'amour','cochonet':'cochonet'}

    def hero_name():
        value = store.hero.name
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.cherie.flags.mikeNickname
        if speaker == 'cherie' and store.hero.gender == 'male' and chosen:
            if str(chosen).lower() == str(value).lower():
                return nicknames.get(str(value).lower(),value)
            for key,group in aliases.items():
                if chosen in getattr(store,'nickname_'+group,()) and str(value).lower()==key:
                    return nicknames[key]
        return value

    def action_text(value):
        return {'kissing':'целую','groping':'лапаю'}.get(value,value)

    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node = engine.game.script.namemap.get(engine.game.context().current)
        filename = getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith('ch/cherie/'):return strings.get(value,value)
        return store.lssb_cassidy.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1028 python:
    config.language_callbacks['russian'].append(lssb_cherie.enter)
    for _lssb_cherie_language in set(renpy.known_languages()) | {None}:
        if _lssb_cherie_language != 'russian':
            config.language_callbacks[_lssb_cherie_language].append(lssb_cherie.leave)

screen choice(items):
    variant 'lssb_cherie_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_cherie.caption(i.caption) action i.action
