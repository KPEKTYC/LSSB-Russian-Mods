# Presentation only. Preserve native names, scene statements and menu actions.
init 1019 python in lssb_anna:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_anna_ru'
    strings = {'Ask Anna on a date': 'Пригласить Анну на свидание', "Meet Anna and Kleio for a 'hot coffee'": 'Встретиться с Анной и Клео за «горячим кофе»', "Meet Anna, Kleio and Sasha for a 'hot coffee'": 'Встретиться с Анной, Клео и Сашей за «горячим кофе»', 'Meet Anna, Emma and Kat at the beach': 'Встретиться с Анной, Эммой и Кэт на пляже', "Invite Anna and Bree for an 'experiment'": 'Пригласить Анну и Бри на «эксперимент»', 'Take Amy and Anna to the waterpark': 'Сходить с Эми и Анной в аквапарк', 'Get the band together (Amy, Anna, Kleio and Sasha)': 'Собрать группу: Эми, Анну, Клео и Сашу', "See you in Sasha's room": 'Увидимся в комнате Саши', "Let's meet in my room": 'Давай встретимся в моей комнате', 'I just hope I will not screw up': 'Надеюсь, я ничего не испорчу', 'It was on a whim': 'Это был спонтанный порыв', 'We will make great music': 'Мы будем писать отличную музыку', "I'll take us to legendary status": 'Я сделаю нас легендой', 'It was shitty': 'Было паршиво', 'I prefer pop music': 'Мне больше нравится поп-музыка', 'Yes': 'Да', 'You should practice more': 'Тебе стоит больше репетировать', "She's mean": 'Она злая', "She's hot": 'Она горячая', "She's fun": 'С ней весело', 'Not much': 'Не особо', 'Working out': 'Тренируюсь', 'Picking up chicks': 'Клею девушек', 'Reading': 'Читаю', 'Watching T.V.': 'Смотрю телевизор', "She's annoying": 'Она раздражает', 'Be Intrigued': 'Заинтересоваться', "Don't Care": 'Не проявлять интереса', 'Maybe later': 'Может, позже', "It's just noise": 'Это просто шум', 'What crap': 'Что за дрянь', 'Me too': 'Я тоже', 'Power metal is the metal of metal': 'Пауэр-метал — металл из металлов', 'No': 'Нет', 'A lot': 'Много', "It's not your business": 'Это не твоё дело', 'I can date you': 'Могу встречаться с тобой', "That's too personal": 'Это слишком личное', 'Dozens': 'Десятки', 'Tell me about you': 'Расскажи о себе', 'Enough': 'Достаточно', 'Anything you like': 'Что угодно', 'You': 'Тебя', 'Let me show you': 'Давай покажу', 'Whatever keeps you in line': 'Всё, что поможет держать тебя в узде', "It's your choice": 'Тебе решать', "That's hot": 'Это возбуждает', 'Love is love': 'Любовь есть любовь', 'Do you ever swing that way?': 'Тебе тоже нравятся девушки?', "But you'd rather have me": 'Но со мной ты бы предпочла быть', "You shouldn't defile your body": 'Не стоит осквернять своё тело', "It's hot": 'Это возбуждает', 'The more the better': 'Чем больше, тем лучше', "I don't judge": 'Я не осуждаю', "They're sluts": 'Они шлюхи', 'They would be better with me': 'Со мной им было бы лучше', 'You are plenty smart': 'Ты очень даже умная', 'You should ask me': 'Тебе стоит спросить меня', 'When I do': 'Когда сам решу', 'Be patient': 'Наберись терпения', 'When you are ready': 'Когда будешь готова', 'I would accept': 'Я бы согласился', "I'd check my schedule": 'Я бы сверился со своим расписанием', 'I am the one who would ask': 'Я бы сам пригласил', 'It would be the best night for you': 'Это был бы лучший вечер в твоей жизни', 'Compliment': 'Похвалить', 'Criticize': 'Раскритиковать', 'Defend Anna': 'Защитить Анну', 'Side with Jack': 'Встать на сторону Джека', "Don't laugh": 'Не смеяться', 'Laugh anyway': 'Всё равно рассмеяться', 'Give her what she begged for and take her ass': 'Исполнить её просьбу и взять в попку', 'Sink into her pussy for a change': 'Для разнообразия войти в её киску', 'Can I join you?': 'Можно к вам?', 'Where are you?': 'Ты где?', 'Interrupt them': 'Прервать их', 'Do nothing': 'Ничего не делать', 'Invite her home': 'Пригласить её домой', 'Call a cab': 'Вызвать такси', 'Step in to save Anna': 'Вмешаться и спасти Анну', 'Stand back and watch': 'Стоять в стороне и смотреть', 'Agree with Kleio': 'Согласиться с Клео', 'Agree with Anna': 'Согласиться с Анной', 'Accept': 'Согласиться', 'Say you wanna record it': 'Сказать, что хочешь это записать', 'Say you want it for yourself': 'Сказать, что хочешь этого для себя', 'Say you want revenge on Gwen and Alexis': 'Сказать, что хочешь отомстить Гвен и Алексис', 'Watch': 'Смотреть', 'Protect Gwen': 'Защитить Гвен', 'We can try': 'Можем попробовать', "I'm not sure": 'Я не уверен', "Tell her that she'll be okay": 'Сказать ей, что всё будет хорошо', 'Quickly put her to her feet': 'Быстро поставить её на ноги', 'Massage her swollen foot': 'Помассировать её опухшую ступню', 'Change subject': 'Сменить тему', "Tell her how it's gonna be": 'Сказать ей, как всё будет', 'Apologize for earlier': 'Извиниться за случившееся', 'Chastise her': 'Отчитать её', 'Play guitar': 'Поиграть на гитаре', 'Cook something': 'Приготовить что-нибудь', 'Look for wild animals': 'Поискать диких животных', 'Help her out': 'Помочь ей', 'Laugh at the situation': 'Посмеяться над ситуацией', 'Dump her ass': 'Бросить её', 'Beg her to abort': 'Умолять её сделать аборт', 'Take responsibility': 'Взять на себя ответственность', 'Try to play peacemaker': 'Попытаться их помирить', 'Try to stay neutral': 'Постараться сохранить нейтралитет', 'Side with Sasha and Kleio against Anna': 'Поддержать Сашу и Клео против Анны', 'Say something to break the ice': 'Разрядить обстановку словами', 'Kiss her to break the ice': 'Поцеловать её, чтобы разрядить обстановку', 'Try to sound confident': 'Постараться говорить уверенно', 'Try to sound sensitive': 'Постараться проявить чуткость', 'Gasp in shock': 'Ошеломлённо ахнуть', 'Laugh in surprise': 'Удивлённо рассмеяться', 'Whistle and shake head': 'Присвистнуть и покачать головой', 'Go down on her': 'Поласкать её языком', 'Make her suck you off': 'Дать ей отсосать', 'Fuck her tits': 'Трахнуть между грудей', 'Just fuck her': 'Просто трахнуть её', 'Cowgirl': 'Наездница', 'Doggy': 'Раком', 'Missionary': 'Миссионерская поза', 'Standing': 'Стоя', 'Take her ass': 'Взять её в попку', 'Take her pussy': 'Взять её в киску', 'Use my tongue': 'Поработать языком', 'Finger her ass': 'Поласкать её попку пальцами', 'Use the anal beads': 'Использовать анальные бусы', 'Use the dildo': 'Использовать фаллоимитатор', 'Let Anna spoil you': 'Позволить Анне себя побаловать', 'Thrust up through her cleavage': 'Толкаться между её грудей', 'Fuck her ass': 'Трахнуть её в попку', 'Fuck her pussy': 'Трахнуть её в киску', 'Use anal beads': 'Использовать анальные бусы', 'Let Anna set her own pace': 'Позволить Анне самой задать темп', 'Take control of her head': 'Направлять движения её головы', 'Cum in her mouth': 'Кончить ей в рот', 'Cum on her face': 'Кончить ей на лицо', "You'd really date a girl again?": 'Ты правда стала бы снова встречаться с девушкой?', "But right now it's just me, yeah?": 'Но сейчас у тебя только я, да?', 'Disrupted': 'Disrupted', 'One and a half direction': 'One and a half direction', 'Tendancious B': 'Tendancious B', 'Anything but that racket you call music': 'Что угодно, кроме грохота, который ты зовёшь музыкой', 'Metallikea': 'Metallikea', 'Call me Superstar': 'Зови меня Суперзвездой', 'Stop calling me Superstar': 'Перестань звать меня Суперзвездой', 'Cancel': 'Отмена'}
    nicknames = {'superstar':'суперзвезда',
        'master':'хозяин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'superstar':'superstar'}

    def hero_name():
        value = store.hero.name
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.anna.flags.mikeNickname
        if speaker == 'anna' and store.hero.gender == 'male' and chosen:
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
        if filename.startswith('ch/anna/'):return strings.get(value,value)
        return store.lssb_alexis.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1020 python:
    config.language_callbacks['russian'].append(lssb_anna.enter)
    for _lssb_anna_language in set(renpy.known_languages()) | {None}:
        if _lssb_anna_language != 'russian':
            config.language_callbacks[_lssb_anna_language].append(lssb_anna.leave)

screen choice(items):
    variant 'lssb_anna_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_anna.caption(i.caption) action i.action
