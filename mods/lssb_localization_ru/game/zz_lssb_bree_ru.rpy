# Text presentation only. No scene, menu action, or save data is replaced.
init -10 python in lssb_bree:
    import renpy
    _constant = True
    version = "1.3.0"
    variant = "lssb_bree_ru_26_8_0d"
    strings = {'Take her out in the garden.': 'Отвести её в сад', 'Take her to the park.': 'Отвести её в парк', 'Ask [bree.name] on a date': 'Пригласить [bree.name] на свидание', 'Meet [bree.name] and Kat': 'Встретиться с [bree.name] и Кэт', "Invite [bree.name] and Anna for an 'experiment'": 'Пригласить [bree.name] и Анну на «эксперимент»', 'Gaming cumpetition': 'Соревнование на оргазмы', 'Simple fooling around': 'Просто подурачиться', 'Apologize': 'Извиниться', "Don't apologize": 'Не извиняться', 'Compliment': 'Сделать комплимент', 'Criticize': 'Раскритиковать', 'Save [bree.name]': 'Спасти [bree.name]', 'Back up Jack': 'Поддержать Джека', 'Accept': 'Согласиться', 'Refuse': 'Отказаться', 'I like it': 'Мне нравится', "I don't like it": 'Мне не нравится', 'You have nothing to be sorry about.': 'Тебе не за что извиняться', 'You should have told me.': 'Надо было мне сказать', "I'm sorry.": 'Прости', "I'll do what I want.": 'Буду делать что хочу', 'Mind lending a hand?': 'Не поможешь?', 'Help me look.': 'Помоги мне поискать', 'Tease her': 'Поддразнить её', "Hey, I don't care.": 'Да мне всё равно', "Don't help her": 'Не помогать ей', 'Help her': 'Помочь ей', 'No': 'Нет', 'Yes': 'Да', 'Action movie': 'Боевик', 'Romcom': 'Романтическая комедия', 'Salty': 'Солёный', 'Sweet': 'Сладкий', 'Tell her to shut up': 'Велеть ей замолчать', 'Let her keep talking': 'Пусть продолжает говорить', 'Agree': 'Согласиться', "I'll ask [bree.name] about the tour.": 'Я спрошу у [bree.name] про экскурсию', 'Sorry, but no.': 'Прости, но нет', 'No fucking way!!!': 'Да ни за что, блядь!!!', 'Cum in her mouth': 'Кончить ей в рот', 'Pull out': 'Вытащить', 'Try to ignore the inconvenience': 'Постараться не обращать внимания на неудобство', "Let [bree.name] know what she's responsible for": 'Дать [bree.name] понять, в чём она виновата', 'You should try': 'Тебе стоит попробовать', "That's a bad idea": 'Плохая идея', 'Pay the Fee': 'Оплатить взнос', 'No Way': 'Ни за что', "Fine, Let's Go": 'Ладно, пошли', 'Intimidate': 'Припугнуть', 'Persuade': 'Убедить', 'Stay out of it': 'Не вмешиваться', 'Fuck her ass': 'Трахнуть её в попку', 'Fuck her pussy': 'Трахнуть её в киску', 'Equip a shield': 'Взять щит', 'Nah defence is for losers. Swing that sword': 'Защита для слабаков. Бей мечом!', 'Report the cheater': 'Пожаловаться на читера', 'Be cautious': 'Действовать осторожно', 'Why not?': 'Почему бы и нет?', 'No, no way, never!': 'Нет, ни за что и никогда!', 'Love it': 'Мне очень нравится', 'What have you done?': 'Что ты натворила?', "Let's meet Thyra together": 'Давай встретимся с Тирой вместе', "Fine... I won't meet Thyra": 'Ладно... я не стану встречаться с Тирой', 'Leave immediately': 'Немедленно уйти', "Let's talk for a minute": 'Давай немного поговорим', 'Defend [bree.name]': 'Заступиться за [bree.name]', 'Keep quiet': 'Промолчать', 'Let [bree.name] stay': 'Позволить [bree.name] остаться', 'Ask [bree.name] to leave': 'Попросить [bree.name] уйти', "I'll help you": 'Я тебе помогу', 'You have to do it alone': 'Ты должна справиться сама', "No, you weren't": 'Нет, ты такой не была', 'Fat and ugly, indeed': 'И правда толстая и некрасивая', 'Agree to split in half': 'Скинуться пополам', 'Buy it alone': 'Купить самому', 'It might be challenging': 'Это может быть непросто', 'I need to end my level': 'Мне надо закончить уровень', "Let's try this new peripheral": 'Давай испытаем новую игрушку', 'I need to focus': 'Мне надо сосредоточиться', 'Cum inside': 'Кончить внутрь', 'Sure': 'Конечно', "Don't worry about it.": 'Не переживай', 'You kept me waiting.': 'Ты заставила меня ждать', 'Get yourself a drink.': 'Купить себе выпивку', 'Get yourself and [bree.name] a drink.': 'Купить выпивку себе и [bree.name]', "Don't worry, I'll cover the difference.": 'Не волнуйся, я доплачу', "I'll sort something out.": 'Я что-нибудь придумаю', 'You better have it.': 'Лучше бы деньги у тебя были', 'Be mean': 'Быть грубым', 'Be nice': 'Быть добрым', 'Was this a joke?': 'Это была шутка?', "That's really spicy!": 'Это очень остро!', 'Take the money': 'Взять деньги', "Don't": 'Не брать', "I can't accept": 'Я не могу это принять', 'Special you say?': 'Особенное, говоришь?', 'Watch': 'Смотреть', 'Help': 'Помочь', 'Show your appreciation instead': 'Лучше показать свою благодарность', 'Give [bree.name] some oral attention': 'Приласкать [bree.name] языком', 'Just fuck her': 'Просто трахнуть её', 'Anal': 'Анальный секс', 'Missionary': 'Миссионерская поза', 'Spoon': 'На боку', 'Doggy': 'Раком', 'Cowgirl': 'Наездница', 'Reverse cowgirl': 'Обратная наездница', 'Vanilla': 'Нежно', 'Rough': 'Жёстко', "Sneak in Sasha's room": 'Прокрасться в комнату Саши', 'Use my tongue': 'Приласкать языком', 'Finger her ass': 'Вставить палец ей в попку', 'Use the dildo': 'Использовать фаллоимитатор', 'Use dildo and my finger.': 'Использовать фаллоимитатор и палец', 'Keep going': 'Продолжать', 'Stop her': 'Остановить её', 'Pull out, Pull out!': 'Вытащить, скорее!', 'Not sorry!': 'Ничуть не жалею!', 'Sorry...': 'Прости...', "Let's start with a blowjob": 'Начнём с минета', "Let's find out": 'Давай проверим', 'Keep the pace': 'Держать темп', 'Cum on her face': 'Кончить ей на лицо', 'Use the anal beads': 'Использовать анальные шарики', 'Pull her hair': 'Потянуть её за волосы', 'Stay simple': 'Без излишеств', 'Use the vibrator': 'Использовать вибратор', "Spank [bree.name]'s ass": 'Отшлёпать [bree.name] по попке', 'Let her in charge': 'Отдать инициативу ей', "Not at all, it's kind of cute.": 'Вовсе нет, это даже мило', "Girls really aren't your thing though.": 'Но девушки тебе всё-таки не нравятся', 'Call me Roomie': 'Называй меня «сосед»', 'Stop calling me Roomie': 'Не называй меня «сосед»', 'Call me Hotshot': 'Называй меня «крутыш»', 'Stop calling me Hotshot': 'Не называй меня «крутыш»', 'Call me Cutie': 'Называй меня «милашка»', 'Stop calling me Cutie': 'Не называй меня «милашка»', 'Call me Player One': 'Называй меня «Первый игрок»', 'Stop calling me Player One': 'Не называй меня «Первый игрок»', 'Call me Daddy': 'Называй меня «папочка»', 'Stop calling me Daddy': 'Не называй меня «папочка»', 'Cancel': 'Отмена', 'Be serious': 'Ответить серьёзно', 'Disagree': 'Не согласиться', 'Do you ever peek?': 'Ты иногда подглядываешь?', "Doesn't it bother you?": 'Тебя это не смущает?', "Don't kiss her": 'Не целовать её', 'Go talk to her': 'Заговорить с ней', 'Half empty': 'Наполовину пуст', 'Half full': 'Наполовину полон', 'Joke': 'Пошутить', 'Kiss her': 'Поцеловать её', 'Mario.': 'Марио', 'Ms Pac-Man.': 'Мисс Пакман', "Neither, it's too big": 'Ни то ни другое: стакан слишком большой', 'Never': 'Никогда', 'Only I will remain.': 'Останусь только я.', 'Only Love will remain.': 'Останется только любовь.', 'Only the Force will remain.': 'Останется только Сила.', 'Samus.': 'Самус', 'Soon': 'Скоро', 'Wait for her to talk': 'Подождать, пока она заговорит', 'You make the first move': 'Сделай первый шаг сама'}
    seasons = {"spring": "весны", "summer": "лета", "fall": "осени", "autumn": "осени", "winter": "зимы"}
    actions = {"kissing": "целую", "groping": "лапаю"}

    def season(value):
        return seasons.get(value, value)

    def action_text(value):
        return actions.get(value, value)

    def caption(value):
        if renpy.game.preferences.language != "russian" or False:
            return value
        node = renpy.game.script.namemap.get(renpy.game.context().current)
        filename = getattr(node, "filename", "").replace("\\", "/").split("/game/")[-1]
        if filename.startswith("game/"):
            filename = filename[5:]
        if filename.startswith("ch/bree/"):
            return strings.get(value, value)
        return value

    def enter():
        if True and variant not in renpy.store.config.variants:
            renpy.store.config.variants.insert(0, variant)

    def leave():
        if variant in renpy.store.config.variants:
            renpy.store.config.variants.remove(variant)

init 1010 python:
    if True:
        config.language_callbacks["russian"].append(lssb_bree.enter)
        for _lssb_bree_language in set(renpy.known_languages()) | {None}:
            if _lssb_bree_language != "russian":
                config.language_callbacks[_lssb_bree_language].append(lssb_bree.leave)

screen choice(items):
    variant "lssb_bree_ru_26_8_0d"
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton lssb_bree.caption(i.caption) action i.action
