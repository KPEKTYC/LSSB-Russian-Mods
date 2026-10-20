# Presentation only. Preserve native names, scene statements and menu actions.
init 1041 python in lssb_lavish:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_lavish_ru'
    strings = {"She's cute": 'Она милая', "She's very professional": 'Она очень профессиональна', 'You two would make a cute couple': 'Из вас двоих вышла бы милая пара', 'You should keep it professional with your female coworkers': 'С коллегами-женщинами стоит сохранять деловые отношения', 'Compliment': 'Сделать комплимент', 'Criticize': 'Раскритиковать', 'Defend Lavish': 'Защитить Лавиш', 'Defend Sasha': 'Защитить Сашу', 'Press on': 'Настоять', 'Back down': 'Отступить', 'Say nothing': 'Промолчать', "Oh, I'll call!": 'О, я обязательно позвоню!', 'Call me [heroname]': 'Называй меня [heroname]', 'Let her stay formal': 'Сохранить официальное обращение', 'Throw in an innuendo': 'Добавить двусмысленный намёк', 'Keep it clean': 'Обойтись без пошлостей', 'Give her the easier but more important project': 'Дать ей более лёгкий, но важный проект', 'Give her the harder but less important project': 'Дать ей более сложный, но менее важный проект', "Don't give her a project": 'Не давать ей проект', 'Compliment her': 'Сделать ей комплимент', 'Play it cool': 'Держаться невозмутимо', 'Make an innuendo out of it': 'Ответить двусмысленным намёком', "I'm impressed!": 'Я впечатлён!', 'Like a kiss?': 'Например, поцелуй?', "I'll keep that in mind!": 'Я запомню!', 'Hug her back': 'Обнять её в ответ', 'Grab her ass': 'Схватить её за задницу', 'Great work!': 'Отличная работа!', 'Not bad': 'Неплохо', 'You deserve a naughty reward': 'Ты заслужила непристойную награду', 'Let it go': 'Оставить это без внимания', 'Unless you want me to': 'Если только ты сама не хочешь', 'I like it when you call me that outside work': 'Мне нравится, когда ты так называешь меня вне работы', 'Call me [hero.name]': 'Называй меня [hero.name]', 'Just say hi': 'Просто поздороваться', 'In general': 'Всегда', 'Outside of work': 'Вне работы', 'Compliment her looks': 'Похвалить её внешность', 'Compliment her work': 'Похвалить её работу', 'Of course': 'Конечно', 'Anything for you, Sweetheart': 'Для тебя что угодно, милая', 'Absolutely': 'Безусловно', 'You could be': 'Могла бы', "I don't know": 'Не знаю', 'No': 'Нет', 'Yes': 'Да', 'I will help': 'Я помогу', 'I will not help': 'Я не буду помогать', 'Whatever I want? Like...sex?': 'Всё, что захочу? Например... секс?', "I'll help but you'd better pay up": 'Я помогу, но с тебя причитается', "I'll help": 'Я помогу', "I can't": 'Не могу', "I'll help...for a kiss": 'Я помогу... за поцелуй', 'Fine': 'Ладно', 'For another kiss': 'За ещё один поцелуй', 'For a kiss...': 'За поцелуй...', 'Fantastic': 'Превосходная', "She's okay, I guess": 'Наверное, неплохая', "I wouldn't hire her": 'Я бы её не нанял', 'No!': 'Нет!', 'Remain professional': 'Сохранить деловой тон', 'Get amorous': 'Проявить нежность', 'Play it down': 'Не придавать этому значения', 'Call for the manager': 'Позвать управляющую', 'Beat the waiter': 'Избить официанта', 'Deny everything': 'Всё отрицать', 'Admit guilt': 'Признать вину', 'Advocate innocence': 'Настаивать на невиновности', 'Refuse to sign': 'Отказаться подписывать', 'Sign the document': 'Подписать документ', 'We should keep it': 'Нам стоит оставить ребёнка', 'You should have a termination': 'Тебе стоит сделать аборт', 'Cum on her face': 'Кончить на лицо', 'Cum in her mouth': 'Кончить в рот', 'Wave her out': 'Жестом велеть ей выйти', 'Take a deep breath and listen to her': 'Глубоко вдохнуть и выслушать её', "Don't spank her": 'Не шлёпать её', 'Spank her': 'Отшлёпать её', "It's okay Lavish, don't worry about it": 'Всё хорошо, Лавиш, не волнуйся', 'You are not prepared at all...': 'Ты совсем не подготовилась...', "Still, let's camp far": 'И всё же давай разобьём лагерь подальше', "You're right, let's camp close": 'Ты права, разобьём лагерь поближе', 'Show Lavish how to make a fire': 'Показать Лавиш, как развести костёр', 'Ask help from Lavish to light the fire': 'Попросить Лавиш помочь развести костёр', 'Wieners first!': 'Сначала сосиски!', 'Marshmallows first!': 'Сначала маршмеллоу!', 'Go down on her': 'Поласкать её языком', 'Make her suck you off': 'Заставить её сделать минет', 'Fuck her': 'Трахнуть её', 'Go missionary style': 'Миссионерская поза', 'Go cowgirl style': 'Наездница', 'Go doggy style': 'Сзади', 'Finish with tongue': 'Довести до оргазма языком', 'Finish with tongue and finger in ass': 'Ласкать языком и пальцем в попке', 'Finish with tongue and dildo in pussy': 'Ласкать языком и фаллоимитатором в киске', 'Finish with tongue and dildo in ass': 'Ласкать языком и фаллоимитатором в попке', 'Fuck her ass': 'Трахнуть в попку', 'Fuck her pussy': 'Трахнуть в киску', 'Give me a blowjob': 'Сделай мне минет', 'Forget it': 'Забудь', 'The women here seem lovely': 'Здешние женщины кажутся очень приятными', 'You keep it professional, especially with your female coworkers': 'Ты держишься профессионально, особенно с коллегами-женщинами', 'Call me Boss': 'Называй меня «босс»', 'Stop calling me Boss': 'Не называй меня «босс»', 'Call me Perv': 'Называй меня «извращенец»', 'Stop calling me Perv': 'Не называй меня «извращенец»', 'Cancel': 'Отмена'}
    nicknames = {'boss':'босс','perv':'извращенец',
        'master':'господин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'boss':'boss','perv':'perv'}

    def hero_name():
        return display_name(store.hero.name)

    def informal_name():
        value = store.lavish.flags.informalheroname
        return value if value == store.heroname else display_name(value)

    def season_text(value):
        return {'spring':'весны','summer':'лета','fall':'осени','autumn':'осени','winter':'зимы'}.get(value,value)

    def display_name(value):
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.lavish.flags.mikeNickname
        if speaker == 'lavish' and store.hero.gender == 'male' and chosen:
            if chosen == 'hero.family_name' and value == 'Mister ' + str(store.hero.family_name):
                return 'господин ' + str(store.hero.family_name)
            if str(chosen).lower() == str(value).lower():
                key = str(value).lower()
                return nicknames[key] if key in nicknames else value
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
        if filename.startswith('ch/lavish/'):return strings.get(value,value)
        return store.lssb_kylie.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1042 python:
    config.language_callbacks['russian'].append(lssb_lavish.enter)
    for _lssb_lavish_language in set(renpy.known_languages()) | {None}:
        if _lssb_lavish_language != 'russian':
            config.language_callbacks[_lssb_lavish_language].append(lssb_lavish.leave)

screen choice(items):
    variant 'lssb_lavish_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_lavish.caption(i.caption) action i.action
