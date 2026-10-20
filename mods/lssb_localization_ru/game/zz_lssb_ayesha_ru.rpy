# Presentation only. Preserve native names, scene statements and menu actions.
init 1021 python in lssb_ayesha:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_ayesha_ru'
    strings = {'Ask Ayesha on a date': 'Пригласить Айшу на свидание', 'Ask Ayesha and Kylie on a date': 'Пригласить Айшу и Кайли на свидание', 'Ask Ayesha and Hanna on a date': 'Пригласить Айшу и Ханну на свидание', 'Invite them to your bedroom': 'Пригласить их в свою спальню', 'Meet them at the gym': 'Встретиться с ними в спортзале', 'Yes': 'Да', 'No': 'Нет', "No. I'm exhausted.": 'Нет. Я вымотался.', 'Wrestling is fake!': 'Рестлинг — это постановка!', "I'm her tag-team partner": 'Я её партнёр по команде', 'Wait a little more': 'Подождать ещё немного', 'Go for it': 'Действовать', 'We should join in': 'Нам стоит присоединиться', 'Stay close': 'Держаться рядом', 'Compliment': 'Похвалить', 'Criticize': 'Раскритиковать', 'Defend Ayesha': 'Защитить Айшу', 'Defend Jack': 'Защитить Джека', 'Dance': 'Танцевать', 'Do not dance': 'Не танцевать', 'Continue the visit': 'Продолжить осмотр', 'Why not': 'Почему бы и нет', 'Agree that Ayesha should have a termination': 'Согласиться, что Айше стоит сделать аборт', "Disagree, Ayesha shouldn't have a termination": 'Возразить: Айше не стоит делать аборт', 'Compliment her muscles': 'Похвалить её мышцы', 'Compliment her beauty': 'Восхититься её красотой', 'Do nothing': 'Ничего не делать', "It's way faster this way.": 'Так гораздо быстрее.', 'Fine': 'Ладно', 'Tell Ayesha it was an accident': 'Сказать Айше, что это была случайность', 'Hide it from her': 'Скрыть от неё', 'Sci-Fi thriller': 'Фантастический триллер', 'Historical drama': 'Историческая драма', 'Tell Ayesha to go for it': 'Посоветовать Айше попробовать', 'Tell Ayesha not to do it': 'Отговорить Айшу', 'Refuse to manage Ayesha': 'Отказаться быть менеджером Айши', 'Agree to manage Ayesha': 'Согласиться быть менеджером Айши', 'Treat the matches as real': 'Относиться к боям как к настоящим', 'Treat the matches as "real"': 'Относиться к боям как к «настоящим»', 'Treat the matches as fake': 'Относиться к боям как к постановке', 'Talk about yourself': 'Рассказать о себе', "Ask her what's wrong": 'Спросить, что случилось', 'Defend Ayesha and yourself': 'Заступиться за Айшу и себя', 'Let Ayesha defend you': 'Позволить Айше тебя защитить', "I'm not into this kind of stuff": 'Мне такое не по душе', 'I might have some ideas': 'У меня есть кое-какие идеи', "I'm ok": 'Я не против', 'We should wait.': 'Нам стоит подождать.', "Let's start": 'Давай начнём', 'We should wait a little more.': 'Стоит ещё немного подождать.', "That's fine": 'Всё нормально', "I'll wait!": 'Я подожду!', 'Pull out her chair': 'Отодвинуть для неё стул', 'Sit first': 'Сесть первым', "Ask quietly for the waiter's attention": 'Спокойно подозвать официанта', "Make a scene to get the waiter's attention": 'Устроить сцену, чтобы привлечь официанта', 'Ask about her food': 'Спросить о её блюде', 'Tell Ayesha off': 'Отчитать Айшу', 'We can share': 'Можем поделиться', 'That seems reasonable': 'Звучит разумно', 'Take your time with her': 'Не торопиться с ней', 'Give her everything she asked for': 'Дать ей всё, о чём она просила', 'Continue her training': 'Продолжить её обучение', 'Not now': 'Не сейчас', 'Fuck her ass': 'Трахнуть её в попку', 'Fuck her pussy': 'Трахнуть её в киску', 'Ask Ayesha for a blowjob': 'Попросить Айшу сделать минет', 'Give Ayesha oral': 'Поласкать Айшу языком', 'Cum on her face': 'Кончить ей на лицо', 'Cum in her mouth': 'Кончить ей в рот', 'Continue': 'Продолжить', 'Lick her ass': 'Полизать её попку', 'Missionary': 'Миссионерская поза', 'Doggy': 'Раком', 'Reverse Cowgirl': 'Обратная наездница', 'Cowgirl': 'Наездница', 'Standing': 'Стоя', 'Go down on her': 'Поласкать её языком', 'Kiss your way up her body': 'Подниматься по её телу с поцелуями', 'Just take her': 'Просто взять её', 'Take her slow': 'Взять её медленно', 'Take her rough': 'Взять её грубо', 'Take her ass': 'Взять её в попку', 'Use the paddle': 'Использовать шлёпалку', 'Use the whip': 'Использовать плеть', 'Use the nipple clamps': 'Использовать зажимы для сосков', 'Use electrodes': 'Использовать электроды', "Ever wonder what it'd be like with another woman?": 'Не думала, каково было бы с другой женщиной?', 'The guys must still line up for you, though.': 'Но парни наверняка всё равно в очередь выстраиваются.', 'Call me Little man': 'Зови меня Малышом', 'Stop calling me Little man': 'Перестань звать меня Малышом', 'Call me Boi': 'Зови меня Парнем', 'Stop calling me Boi': 'Перестань звать меня Парнем', 'Call me Coach': 'Зови меня Тренером', 'Stop calling me Coach': 'Перестань звать меня Тренером', 'Cancel': 'Отмена'}
    nicknames = {'little man':'малыш','boi':'парень','coach':'тренер',
        'master':'хозяин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'little man':'little_man','boi':'boi','coach':'coach'}

    def hero_name():
        value = store.hero.name
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.ayesha.flags.mikeNickname
        if speaker == 'ayesha' and store.hero.gender == 'male' and chosen:
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
        if filename.startswith('ch/ayesha/'):return strings.get(value,value)
        return store.lssb_anna.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1022 python:
    config.language_callbacks['russian'].append(lssb_ayesha.enter)
    for _lssb_ayesha_language in set(renpy.known_languages()) | {None}:
        if _lssb_ayesha_language != 'russian':
            config.language_callbacks[_lssb_ayesha_language].append(lssb_ayesha.leave)

screen choice(items):
    variant 'lssb_ayesha_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_ayesha.caption(i.caption) action i.action
