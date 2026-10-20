# Presentation only. Preserve native names, scene statements and menu actions.
init 1039 python in lssb_kylie:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_kylie_ru'
    strings = {'Ask Kylie on a date': 'Пригласить Кайли на свидание', 'Ask Kylie and Ayesha on a date': 'Пригласить Кайли и Айшу на свидание', 'Insist': 'Настоять', 'Accept': 'Согласиться', 'Compliment': 'Сделать комплимент', 'Criticize': 'Раскритиковать', 'Back up Kylie': 'Поддержать Кайли', 'Back up [bree.name]': 'Поддержать [bree.name]', 'Refuse': 'Отказаться', 'Help [bree.name]': 'Помочь [bree.name]', 'Hide and watch': 'Спрятаться и наблюдать', "That's gross!": 'Это мерзко!', "That's hot!": 'Это возбуждает!', 'Sympathise with Kylie': 'Посочувствовать Кайли', 'Put Kylie in her place': 'Поставить Кайли на место', 'Agree to a conjugal visit': 'Согласиться на интимное свидание', 'Put Kylie off': 'Отказать Кайли', "Protest Kylie's innocence": 'Заявить о невиновности Кайли', "Plead Kylie's insanity": 'Сослаться на невменяемость Кайли', 'Describe Kylie as a cold-blooded killer': 'Назвать Кайли хладнокровной убийцей', 'Scream for help': 'Позвать на помощь', 'Stay silent': 'Молчать', 'Cum on her face': 'Кончить на лицо', 'Cum in her mouth': 'Кончить в рот', "I'll take responsibility": 'Я возьму на себя ответственность', "I don't want anything to do with it": 'Не хочу иметь к этому отношения', 'You should get an abortion': 'Тебе стоит сделать аборт', 'Say that you are happy for her': 'Сказать, что рад за неё', 'Say she disgusts you': 'Сказать, что она тебе противна', 'Say you are happy for her': 'Сказать, что рад за неё', 'Say she disgust you': 'Сказать, что она тебе противна', "Let's do it": 'Давай сделаем это', 'No way': 'Ни за что', 'Let her in': 'Впустить её', "Don't let her come in.": 'Не впускать её', 'Agree': 'Согласиться', "She's just a friend": 'Она просто подруга', 'I kinda like her': 'Она мне вроде нравится', "That's what friends are for": 'Для этого и нужны друзья', 'I could never say no to a pretty face': 'Не могу отказать красавице', "It's wrong": 'Это неправильно', 'I liked it': 'Мне понравилось', 'Tell Kylie off for climbing over the fence': 'Отругать Кайли за то, что перелезла через забор', 'Ignore it': 'Не обращать внимания', 'Agree to give Kylie a tour': 'Согласиться показать Кайли дом', 'Make up an excuse not to give Kylie a tour': 'Придумать предлог, чтобы не показывать Кайли дом', "Laugh off Kylie's comments": 'Отшутиться в ответ на слова Кайли', "Get offended at Kylie's comments": 'Обидеться на слова Кайли', 'Smooth things over with Kylie': 'Помириться с Кайли', 'Tell Kylie that you are mad at her': 'Сказать Кайли, что злишься на неё', 'Psychological thriller': 'Психологический триллер', 'Rom-com': 'Романтическая комедия', 'Cum inside': 'Кончить внутрь', 'Pull out': 'Вытащить', 'Have a taste of her': 'Поласкать её языком', 'Bring her to her knees': 'Поставить её на колени', 'Fuck her': 'Трахнуть её', 'Missionary': 'Миссионерская поза', 'Cowgirl': 'Наездница', 'Doggy': 'Сзади', 'Use ropes': 'Использовать верёвки', 'Spoon': 'На боку', 'Facial': 'Кончить на лицо', 'Swallow': 'Кончить в рот', 'Use my tongue': 'Ласкать языком', 'Finger her ass': 'Ввести палец ей в попку', 'Use the dildo': 'Использовать фаллоимитатор', 'Use the anal beads': 'Использовать анальные шарики', 'Fuck her ass': 'Трахнуть в попку', 'Fuck her pussy': 'Трахнуть в киску', 'Call me My One and Only': 'Называй меня «мой единственный»', 'Stop calling me My One and Only': 'Не называй меня «мой единственный»', 'Call me My Heart': 'Называй меня «сердце моё»', 'Stop calling me My Heart': 'Не называй меня «сердце моё»', 'Call me My ball and chain': 'Называй меня «мои оковы»', 'Stop calling me My ball and chain': 'Не называй меня «мои оковы»', 'Cancel': 'Отмена'}
    nicknames = {'my one and only':'мой единственный','my heart':'сердце моё','my ball and chain':'мои оковы',
        'master':'господин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'my one and only':'my_one_and_only','my heart':'my_heart','my ball and chain':'my_ball_and_chain'}

    def hero_name():
        value = store.hero.name
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.kylie.flags.mikeNickname
        if speaker == 'kylie' and store.hero.gender == 'male' and chosen:
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
        if filename.startswith('ch/kylie/'):return strings.get(value,value)
        return store.lssb_kleio.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1040 python:
    config.language_callbacks['russian'].append(lssb_kylie.enter)
    for _lssb_kylie_language in set(renpy.known_languages()) | {None}:
        if _lssb_kylie_language != 'russian':
            config.language_callbacks[_lssb_kylie_language].append(lssb_kylie.leave)

screen choice(items):
    variant 'lssb_kylie_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_kylie.caption(i.caption) action i.action
