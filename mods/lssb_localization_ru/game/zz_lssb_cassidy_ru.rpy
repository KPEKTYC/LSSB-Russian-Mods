# Presentation only. Preserve native names, scene statements and menu actions.
init 1025 python in lssb_cassidy:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_cassidy_ru'
    strings = {'You do not have a choice': 'У тебя нет выбора', 'Only if you want to': 'Только если ты сама хочешь', 'Make Cassidy urinate in the park': 'Заставить Кэссиди помочиться в парке', 'Take Cassidy home': 'Отвести Кэссиди домой', 'Ask Cassidy on a date': 'Пригласить Кэссиди на свидание', 'Ask Cassidy, Audrey and Palla on a date': 'Пригласить Кэссиди, Одри и Паллу на свидание', 'Ask Cassidy and Palla for some fun': 'Предложить Кэссиди и Палле развлечься', "Bet you'd rather fill it with pretty girls": 'Спорим, ты бы предпочла наполнить его красотками', "You'd want a real man in the room": 'Тебе бы хотелось видеть в комнате настоящего мужчину', 'Just let her gloat': 'Просто дать ей похвастаться', 'Use a condom': 'Надеть презерватив', 'Ignore her': 'Проигнорировать её', 'Fuck her ass instead': 'Вместо этого трахнуть её в попку', "I don't have to fuck her": 'Я не обязан её трахать', 'Step aside': 'Отойти в сторону', 'Slap ass': 'Шлёпнуть по попке', 'Defend Cassidy': 'Защитить Кэссиди', 'Defend Jack and Scottie': 'Защитить Джека и Скотти', 'Refuse': 'Отказаться', 'Accept': 'Согласиться', 'Offer to back off': 'Предложить отступить', 'Wait patiently': 'Терпеливо ждать', 'Complain': 'Пожаловаться', 'Insist on getting pizza': 'Настоять на пицце', 'Agree to getting hot-dogs': 'Согласиться на хот-доги', 'Encourage her to get inked': 'Уговорить её сделать татуировку', 'Encourage her not to get inked': 'Отговорить её от татуировки', 'Side with Cassidy': 'Встать на сторону Кэссиди', 'Side with [bree.name]': 'Встать на сторону [bree.name]', 'I have important work to do (Never meet Cassidy again)': 'У меня важная работа (больше не встречаться с Кэссиди)', 'I will drop you off at the airport': 'Я отвезу тебя в аэропорт', "No! You can't!": 'Нет! Ты не можешь!', "It's for the best": 'Так будет лучше', 'Insist': 'Настоять', 'Let it go': 'Не настаивать', 'Yes': 'Да', 'No': 'Нет', 'Why should I believe you?': 'Почему я должен тебе верить?', 'What do you know about the investigation?': 'Что ты знаешь о расследовании?', 'Does your daddy know?': 'Твой папочка знает?', "You didn't just ask daddy": 'Ты ведь не просто попросила папочку', 'Who are you working with?': 'С кем ты работаешь?', 'Where is the money?': 'Где деньги?', 'I can always get another job': 'Я всегда могу найти другую работу', 'How bad can being her bitch be?': 'Так ли плохо быть её сучкой?', 'No, not worth it': 'Нет, оно того не стоит', 'Fine, you win': 'Ладно, ты победила', 'Bitch': 'Сучка', 'Slave': 'Раб', "I'm great at it": 'Я отлично справляюсь', 'I need more practice': 'Мне нужно больше практики', 'Obey': 'Подчиниться', 'Resist, playfully': 'Игриво сопротивляться', 'Resist, impudently': 'Дерзко сопротивляться', "I'm doing the training": 'Здесь я занимаюсь дрессировкой', 'Yes, Mistress': 'Да, госпожа', "It'll be okay.": 'Всё будет хорошо', 'Suck it up, Buttercup': 'Терпи, принцесса', "No, don't go!": 'Нет, не уходи!', 'Free at last!': 'Наконец-то свобода!', 'Yes!': 'Да!', 'No thanks': 'Нет, спасибо', 'Boyfriend/girlfriend instead?': 'Может, лучше будем парой?', "She's my sex slave": 'Она моя секс-рабыня', "She's someone I care about very much": 'Она мне очень дорога', "She's a total bitch": 'Она та ещё стерва', "She's a great boss": 'Она отличная начальница', 'Leave her alone': 'Оставить её в покое', 'Comfort her': 'Утешить её', 'Get rid of her': 'Избавиться от неё', "You're right": 'Ты права', 'You deserve it': 'Ты это заслужила', "Please don't do that": 'Пожалуйста, не делай этого', "That's hot! I want pictures": 'Это горячо! Хочу фотографии', 'No, you belong to me': 'Нет, ты принадлежишь мне', 'As you wish, but...': 'Как пожелаешь, но...', 'I care about you': 'Ты мне дорога', "Until then, you're my property": 'А до тех пор ты моя собственность', 'Gross!': 'Фу!', "Okay, that's hot": 'Ладно, это горячо', 'I live to serve': 'Живу, чтобы служить', 'I forgot': 'Я забыл', 'I got held up': 'Меня задержали', 'Make up a reason': 'Выдумать причину', "I'm worried this is going to hurt her": 'Боюсь, это причинит ей боль', 'She wants me and I want her': 'Она хочет меня, а я — её', 'I think I want the both of you': 'Кажется, я хочу вас обеих', 'Good idea': 'Хорошая идея', 'Bad idea': 'Плохая идея', 'We should move on from each other': 'Нам пора пойти разными путями', 'I want to keep you as my slave': 'Хочу, чтобы ты осталась моей рабыней', 'I want to stay your slave': 'Хочу остаться вашим рабом', 'You should be my girlfriend': 'Стань моей девушкой', 'I want you to stay my girlfriend': 'Хочу, чтобы ты осталась моей девушкой', "I won't leave Cherie all alone": 'Я не оставлю Шери совсем одну', 'But Aletta is special': 'Но Алетта особенная', 'They both need me too': 'Я тоже нужен им обеим', 'Of course, my love': 'Конечно, любимая', "Only because it's you then": 'Ладно, только ради тебя', "I won't do that": 'Я не стану этого делать', 'Put her on the spare leash': 'Пристегнуть к ней запасной поводок', 'Shoo her away': 'Прогнать её', 'Cum inside': 'Кончить внутрь', 'Pull out': 'Вытащить', 'Titty job': 'Ласки грудью', 'Slave play': 'Игры с рабыней', 'Fuck her': 'Трахнуть её', 'Missionary': 'Миссионерская поза', 'Doggy': 'Сзади', 'Cowgirl': 'Наездница', 'Reverse Cowgirl': 'Обратная наездница', 'Fuck her pussy': 'Трахнуть её в киску', 'Fuck her ass': 'Трахнуть её в попку', 'Go slow and gentle': 'Действовать медленно и нежно', 'A little pain is good for her': 'Немного боли ей не повредит', 'You may go': 'Можешь идти', 'Stay': 'Останься', 'You should go': 'Тебе лучше уйти', "I'd love that": 'С удовольствием', 'Get on the bed': 'Ложитесь на кровать', 'What do you want me to do?': 'Что вы хотите, чтобы я сделал?', 'Agree': 'Согласиться', 'Demand she stay': 'Потребовать, чтобы она осталась', 'Beg she stay': 'Умолять её остаться', 'Let her go': 'Позволить ей уйти', 'Finger her': 'Приласкать её пальцами', 'Fuck her tits': 'Трахнуть её между грудей', 'Reverse cowgirl': 'Обратная наездница', 'Cum in her mouth': 'Кончить ей в рот', 'Cum on her face': 'Кончить ей на лицо', 'Take me to one some time': 'Как-нибудь своди меня в такой ресторан', 'Too fancy for me': 'Для меня слишком роскошно', 'Sure, sounds like fun.': 'Конечно, звучит весело', 'No way!': 'Ни за что!', 'Anyone caught your eye lately?': 'Кто-нибудь недавно приглянулся?', 'Only guys for you, right?': 'Тебя интересуют только парни, да?', 'Call me Servant': 'Называй меня слугой', 'Stop calling me Servant': 'Перестань называть меня слугой', 'Call me Little one': 'Называй меня малышом', 'Stop calling me Little one': 'Перестань называть меня малышом', 'Call me Peasant': 'Называй меня простолюдином', 'Stop calling me Peasant': 'Перестань называть меня простолюдином', 'Call me My rock': 'Называй меня своей опорой', 'Stop calling me My rock': 'Перестань называть меня своей опорой', 'Call me Lord': 'Называй меня милордом', 'Stop calling me Lord': 'Перестань называть меня милордом', 'Cancel': 'Отмена'}
    nicknames = {'servant':'слуга','little one':'малыш','peasant':'простолюдин','my rock':'моя опора','lord':'милорд',
        'bitch':'сучка','slave':'раб','princess':'принцесса','master':'господин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'servant':'servant','little one':'little_one','peasant':'peasant','my rock':'my_rock','lord':'lord','master':'master'}

    def hero_name():
        value = store.hero.name
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.cassidy.flags.mikeNickname
        if (speaker == 'cassidy' and store.hero.gender == 'male' and not chosen
                and store.cassidy.status != 'mistress'
                and (store.cassidy.is_sex_slave or store.cassidy.sub >= 50)
                and str(value).lower() == 'master'):
            return 'господин'
        if speaker == 'cassidy' and store.hero.gender == 'male' and chosen:
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
        if filename.startswith('ch/cassidy/'):return strings.get(value,value)
        return store.lssb_camila.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1026 python:
    config.language_callbacks['russian'].append(lssb_cassidy.enter)
    for _lssb_cassidy_language in set(renpy.known_languages()) | {None}:
        if _lssb_cassidy_language != 'russian':
            config.language_callbacks[_lssb_cassidy_language].append(lssb_cassidy.leave)

screen choice(items):
    variant 'lssb_cassidy_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_cassidy.caption(i.caption) action i.action
