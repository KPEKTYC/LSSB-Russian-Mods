# Presentation only. Preserve native names, scene statements and menu actions.
init 1015 python in lssb_aletta:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_aletta_ru'
    strings = {'Yes boss': 'Да, босс', 'I work enough': 'Я и так достаточно работаю', 'You can trust me': 'Можешь мне доверять', 'Let me handle things': 'Предоставь это мне', "I'll do them later": 'Я сделаю это позже', 'Of course': 'Конечно', "Don't worry": 'Не волнуйся', "She's lazy": 'Она ленивая', "She's hot": 'Она горячая штучка', 'I prefer older women': 'Мне нравятся женщины постарше', 'I prefer willful women': 'Мне нравятся женщины с характером', 'Working out': 'Тренируюсь', 'Picking up chicks': 'Цепляю девчонок', 'Reading': 'Читаю', 'Watching T.V.': 'Смотрю телевизор', 'Yes': 'Да', 'Fuck off': 'Отвали', 'I am manly already': 'Я и так достаточно мужественный', 'Let me show you': 'Давай покажу', 'Be Intrigued': 'Проявить интерес', "Don't Care": 'Остаться равнодушным', 'Maybe later': 'Может, позже', "I'll protect you": 'Я тебя защищу', 'Women are our leaders': 'Женщины должны нами руководить', 'What crap': 'Что за чушь', 'Some maybe': 'Может, некоторые', 'Not me': 'Только не я', 'No': 'Нет', 'A lot': 'Очень много', "It's not your business": 'Это не твоё дело', 'I can date you': 'Могу сходить на свидание с тобой', 'Sure': 'Конечно', 'I am more than enough': 'Меня тебе хватит с лихвой', 'On your knees, bitch': 'На колени, сучка', "That's too personal": 'Это слишком личное', 'Dozens': 'С десятками', 'Tell me about you': 'Расскажи лучше о себе', 'Enough': 'Достаточно', 'Anything you like': 'Что угодно на твой вкус', 'You': 'Ты', 'Whatever keeps you in line': 'Всё, что держит тебя в узде', 'Another woman, for you': 'Другая женщина — для тебя', 'You, on your knees': 'Ты, на коленях', "It's your choice": 'Это твой выбор', 'I only smoke while drunk': 'Я курю только по пьяни', "It's bad for the health": 'Это вредно для здоровья', "You shouldn't smoke": 'Тебе не стоит курить', 'We need women to lead us': 'Нам нужно, чтобы нами руководили женщины', 'I am better than any woman': 'Я лучше любой женщины', "She's flawed": 'С ней что-то не так', "It's not her place": 'Это не её место', "I don't judge": 'Я не осуждаю', "She's a slut": 'Она шлюха', 'The man is at fault': 'Виноват мужчина', 'She would be better with me': 'Со мной ей было бы лучше', 'You should ask me': 'Тебе стоит самой меня пригласить', 'When I do': 'Когда захочу', 'Be patient': 'Потерпи', 'When you are ready': 'Когда ты будешь готова', 'I already know the answer': 'Я уже знаю ответ', 'I would obey': 'Я бы подчинился', "I'd check my schedule": 'Я бы сверился со своим расписанием', 'I am the one who would ask': 'Приглашать должен я', 'It would be the best night for you': 'Это был бы твой лучший вечер', 'Compliment': 'Сделать комплимент', 'Criticize': 'Раскритиковать', 'Defend Aletta': 'Защитить Алетту', 'Defend [bree.name]': 'Защитить [bree.name]', 'Press on': 'Продолжать настаивать', 'Back down': 'Отступить', 'Agree': 'Согласиться', 'Refuse': 'Отказаться', 'We can do that': 'Мы можем это сделать', "I'm not sure": 'Я не уверен', 'Do nothing': 'Ничего не делать', 'Discipline her': 'Наказать её', 'Disagree': 'Не согласиться', 'Tell her not to do it': 'Сказать ей не делать этого', 'Help her': 'Помочь ей', 'Help her!': 'Помочь ей!', 'Be sophisticated': 'Изобразить гурмана', 'Be transparent': 'Сказать прямо', 'Kiss Aletta': 'Поцеловать Алетту', 'Take a step back': 'Отступить на шаг', "Tell her it's forbidden": 'Сказать, что это запрещено', "Tell her it's unhealthy": 'Сказать, что это вредно', 'Ask if she has an extra': 'Попросить сигарету', 'Say nothing': 'Промолчать', 'Stand up for Aletta': 'Заступиться за Алетту', 'Keep watching.': 'Продолжать наблюдать', 'Offer to give her a massage': 'Предложить ей массаж', 'Tell her she should go get a massage': 'Посоветовать ей сходить на массаж', 'Brush against her arm': 'Слегка коснуться её руки', 'Keep some space between each other': 'Держаться на расстоянии', 'Apologize': 'Извиниться', 'Play dumb': 'Прикинуться дурачком', "Think about Aletta's breasts": 'Думать о груди Алетты', "Think about Aletta's pussy": 'Думать о киске Алетты', 'Think about an office intern': 'Думать об офисной стажёрке', 'No thanks': 'Нет, спасибо', 'Talk dirty to her': 'Говорить ей пошлости', 'Pretend not to notice what she is doing': 'Сделать вид, что ничего не замечаешь', 'Push her skirt up gently': 'Осторожно приподнять её юбку', 'Be rough with her': 'Обойтись с ней грубо', 'Try to catch it in your mouth': 'Попробовать поймать ртом', 'Quickly shut your mouth': 'Быстро закрыть рот', 'Accept': 'Согласиться', 'Get up': 'Встать', 'Stay seated': 'Остаться сидеть', "Don't": 'Не делать этого', 'Do it': 'Сделать это', 'Reassure her': 'Успокоить её', 'Snap out of it!': 'Приди в себя!', 'Celebrate': 'Отпраздновать', 'Warn her': 'Предупредить её', 'I love you too': 'Я тоже тебя люблю', "I don't": 'А я тебя нет', 'Confront Dwayne': 'Дать отпор Дуэйну', 'Ease the tension': 'Разрядить обстановку', 'Insist': 'Настоять на своём', 'Let it go': 'Оставить всё как есть', 'I will leave them for you': 'Ради тебя я их брошу', "I can't do that to them": 'Я не могу так с ними поступить', 'I guess so': 'Пожалуй', "Let's use those tits": 'Пустим в ход эти сиськи', 'Play with her ass': 'Поиграть с её попкой', 'Just fuck her': 'Просто трахнуть её', 'Cowgirl': 'Наездница', 'Missionary': 'Миссионерская поза', 'Doggy': 'Раком', 'Cum on her breasts': 'Кончить ей на грудь', 'Cum on her face': 'Кончить ей на лицо', 'Cum in her mouth': 'Кончить ей в рот', 'Fuck her ass': 'Трахнуть её в задницу', 'Fuck her pussy': 'Трахнуть её в киску', 'Cum inside': 'Кончить внутрь', 'Pull out': 'Вытащить', 'Fuck Aletta in the ass': 'Трахнуть Алетту в задницу', 'Fuck Aletta in the pussy': 'Трахнуть Алетту в киску', "I'm up for a blowjob": 'Я бы не отказался от минета', "We'll use the desk again.": 'Снова воспользуемся столом', 'I just want to eat you.': 'Я просто хочу тебя вылизать', "It's time for your weekly training": 'Пора на твою еженедельную тренировку', "I'm a little stressed today": 'Я сегодня немного на взводе', 'You seem a little overstressed': 'Ты выглядишь напряжённой', 'Forget it': 'Забудь', 'Cum on her tits': 'Кончить ей на сиськи', 'Facial': 'Кончить ей на лицо', 'Swallow': 'Дать ей проглотить', 'So you look at the women too?': 'Значит, и на женщин заглядываешься?', 'Figured you only wanted a real man.': 'Думал, тебе нужен только настоящий мужчина', 'You never have anything interesting to say.': 'От тебя никогда не услышишь ничего интересного', 'Call me Young man': 'Называй меня молодым человеком', 'Stop calling me Young man': 'Не называй меня молодым человеком', 'Call me Boss Buck': 'Называй меня боссом Баком', 'Stop calling me Boss Buck': 'Не называй меня боссом Баком', 'Call me Cow-boy': 'Называй меня ковбоем', 'Stop calling me Cow-boy': 'Не называй меня ковбоем', 'Cancel': 'Отмена'}
    nicknames = {'young man':'молодой человек','boss buck':'босс Бак','cow-boy':'ковбой',
        'master':'хозяин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'young man':'young_man','boss buck':'boss_buck','cow-boy':'cow_boy'}

    def hero_name():
        value = store.hero.name
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.aletta.flags.mikeNickname
        if speaker == 'aletta' and store.hero.gender == 'male' and chosen:
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
        if filename.startswith('ch/aletta/'):return strings.get(value,value)
        return store.lssb_audrey.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1016 python:
    config.language_callbacks['russian'].append(lssb_aletta.enter)
    for _lssb_aletta_language in set(renpy.known_languages()) | {None}:
        if _lssb_aletta_language != 'russian':
            config.language_callbacks[_lssb_aletta_language].append(lssb_aletta.leave)

screen choice(items):
    variant 'lssb_aletta_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_aletta.caption(i.caption) action i.action
