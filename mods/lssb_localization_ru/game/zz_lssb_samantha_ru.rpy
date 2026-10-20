# Presentation only. Preserve native names, scene statements and menu actions.
init 1053 python in lssb_samantha:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_samantha_ru'
    strings = {'Ask Samantha on a date': 'Пригласить Саманту на свидание', 'Ask Samantha and Emma on a date': 'Пригласить Саманту и Эмму на свидание', 'Ask if she looks': 'Спросить, смотрит ли она', 'Joke about it': 'Пошутить об этом', 'Be possessive': 'Проявить собственничество', 'Take charge': 'Взять инициативу', 'Defer to her': 'Уступить ей', 'Compliment him': 'Похвалить его', 'Criticize him': 'Раскритиковать его', 'Compliment': 'Похвалить', 'Criticise': 'Раскритиковать', 'Disagree': 'Не согласиться', 'Agree': 'Согласиться', 'Complain': 'Пожаловаться', 'Go over': 'Подойти', 'Stay away': 'Держаться подальше', 'Accept': 'Согласиться', 'Refuse': 'Отказаться', 'Keep your mouth shut': 'Промолчать', 'Tell her about the cheating': 'Рассказать ей об измене', 'Hug her': 'Обнять её', 'Back away': 'Отступить', "Tell her it's probably Ryan's": 'Сказать, что ребёнок, скорее всего, от Райана', 'Facial': 'Кончить на лицо', 'Swallow': 'Проглотить', 'Light Boxes': 'Лёгкие коробки', 'Heavy Boxes': 'Тяжёлые коробки', 'Take in the Desk': 'Занести стол', 'Wait': 'Подождать', 'Take in the Boxes': 'Занести коробки', 'The usual.': 'Как обычно.', 'Something new.': 'Что-нибудь новое.', 'No thanks.': 'Нет, спасибо.', 'Sure!': 'Конечно!', 'Entertaining.': 'Весело.', 'Just roommates.': 'Просто соседки.', 'Pretty attractive.': 'Довольно привлекательные.', "I've got other plans.": 'У меня другие планы.', "Alright. I'll come over later today.": 'Ладно. Зайду сегодня попозже.', 'Be supportive': 'Поддержать', 'Be disapproving': 'Выразить неодобрение', 'Hey, Samantha.': 'Привет, Саманта.', 'Scare': 'Напугать', "You look like you're having trouble.": 'Похоже, у тебя что-то не получается.', 'Sounds difficult. Need any help?': 'Звучит непросто. Помочь?', "Homework doesn't sound fun. Good luck with that!": 'Домашняя работа — не самое весёлое занятие. Удачи!', 'Were you listening to me at all?': 'Ты вообще меня слушала?', 'Good try, but you should do it like this.': 'Неплохая попытка, но делать нужно вот так.', 'You can always come to me if you need help.': 'Всегда обращайся ко мне, если нужна помощь.', 'Ask Ryan to help you next time.': 'В следующий раз попроси помочь Райана.', "You didn't bother me.": 'Ты мне не помешала.', 'Stay silent.': 'Промолчать.', 'Change the subject.': 'Сменить тему.', 'Think of an answer.': 'Придумать ответ.', 'Show Her the Pictures': 'Показать ей фотографии', 'Let Her Be Happy': 'Пусть она будет счастлива', 'I still love you.': 'Я всё ещё люблю тебя.', 'Say Nothing': 'Промолчать', 'Let her lead': 'Позволить ей вести', 'Take her': 'Взять её', 'Use a condom': 'Надеть презерватив', 'Do it raw': 'Без презерватива', "Yes, I'd love to go out with you": 'Да, я с радостью буду с тобой встречаться', "No, I don't see you that way": 'Нет, я не испытываю к тебе таких чувств', 'Movie Theatre': 'Кинотеатр', 'Shopping': 'По магазинам', 'Restaurant': 'Ресторан', 'Modest top': 'Скромный топ', 'Daring swimsuit': 'Смелый купальник', 'Sexy top': 'Соблазнительный топ', 'Spaghetti': 'Спагетти', 'Hamburger': 'Гамбургер', 'Salmon': 'Лосось', 'I admit.': 'Признаю.', "You're the only one Sam.": 'Ты у меня единственная, Сэм.', 'I will be faithful.': 'Я буду верен тебе.', "I can't promise.": 'Не могу обещать.', 'Support': 'Поддержать', 'Oppose': 'Возразить', 'Ask about their friendship': 'Спросить об их дружбе', 'Ask about the decoration': 'Спросить об украшениях', 'Ask about the food': 'Спросить о еде', 'Smile Back': 'Улыбнуться в ответ', 'Look Away': 'Отвести взгляд', 'Go for a walk': 'Пойти прогуляться', 'Go to the bathroom': 'Пойти в туалет', 'Dance': 'Потанцевать', 'Push her back': 'Оттолкнуть её', 'Accept Samantha': 'Принять Саманту', 'Fine': 'Ладно', 'I want to go home': 'Я хочу домой', 'Yes': 'Да', 'Ask about Ryan': 'Спросить о Райане', "It's beautiful": 'Это прекрасно', 'It could have used some more work.': 'Можно было ещё поработать.', 'Why are you looking for kids books?': 'Зачем ты ищешь детские книги?', 'Take Book': 'Взять книгу', 'Cooking': 'Кулинария', 'Sports': 'Спорт', 'Fiction': 'Художественная литература', 'Bake Something': 'Что-нибудь испечь', 'Have Drinks': 'Выпить', 'University': 'Университет', 'Work': 'Работа', 'Fun': 'Развлечения', 'Tiramisu': 'Тирамису', 'Cinnamon Rolls': 'Булочки с корицей', 'Funnel Cake': 'Хворост', 'Of course you can': 'Конечно можно', 'Too busy': 'Слишком занят', "What's wrong?": 'Что случилось?', 'Let her cry': 'Дать ей выплакаться', 'Play with the piercing': 'Поиграть с пирсингом', 'Ask her to take it out': 'Попросить её снять его', 'Go down on her': 'Сделать ей кунилингус', 'Just fuck her': 'Просто трахнуть её', 'Pull out': 'Вытащить', 'Cum inside': 'Кончить внутрь', 'Tell her Ryan cheated': 'Рассказать об измене Райана', 'Say nothing': 'Промолчать', "You're not much better": 'Ты не намного лучше', "I'm sorry": 'Прости', "I'll be there.": 'Я приду.', "There's no way.": 'Ни за что.', "They're great": 'Мне очень нравятся', "I'd rather you not wear them": 'Я бы предпочёл, чтобы ты их не носила', "I can't even count": 'Даже сосчитать не могу', 'A few': 'Несколько', 'Just you': 'Только ты', "I'm interested": 'Мне интересно', "That's not what I meant": 'Я не это имел в виду', 'Push her head': 'Надавить ей на голову', 'Cum on her face': 'Кончить ей на лицо', 'Fight': 'Драться', 'Leave': 'Уйти', 'Ask for the window table': 'Попросить столик у окна', 'Tell her to slow down': 'Сказать ей притормозить', 'Let her have her birthday fun': 'Пусть веселится в свой день рождения', 'Jump the queue': 'Пройти без очереди', "Let's dance": 'Потанцуем', "Let's drink": 'Выпьем', 'Sure': 'Конечно', "I'm quite busy right now": 'Я сейчас довольно занят', 'Accept invitation': 'Принять приглашение', 'Decline invitation': 'Отклонить приглашение', 'Fuck her': 'Трахнуть её', "I'll be there": 'Я приду', "I'm not coming": 'Я не приду', "I've got something on": 'У меня дела', 'Take her hand': 'Взять её за руку', "Tell her she's not alone": 'Сказать, что она не одна', 'Just nod': 'Просто кивнуть', 'Tell her what I did': 'Рассказать ей, что я сделал', 'Show her the photos': 'Показать ей фотографии', 'Keep them to myself': 'Оставить их у себя', "Let's not talk about him right now.": 'Давай сейчас не будем о нём.', "Tell me you're sure about this.": 'Скажи, что ты уверена.', "Say 'please'.": 'Скажи «пожалуйста».', 'Tell me how you want it.': 'Скажи, как ты этого хочешь.', 'Turn around.': 'Повернись.', "We shouldn't make a habit of this.": 'Не стоит превращать это в привычку.', "Tell me you'll call me.": 'Скажи, что позвонишь мне.', 'Are you okay with this?': 'Ты не против?', 'Let’s keep this our secret.': 'Пусть это останется нашей тайной.', 'You were great.': 'Ты была великолепна.', 'Be honest; we can do better.': 'Честно: мы можем лучше.', "Let's keep us separate from the rest.": 'Давай отделять наши отношения от всего остального.', 'I want to be gentle with you.': 'Хочу быть с тобой нежным.', 'I want you, all of you.': 'Я хочу тебя. Всю, без остатка.', 'I like them.': 'Мне нравятся.', 'Lose them for me.': 'Сними их для меня.', 'Kiss her belly.': 'Поцеловать её живот.', 'Eyes up here.': 'Смотри мне в глаза.', 'Let her suck you off': 'Дать ей отсосать', 'Fuck her tits': 'Трахнуть её между грудей', 'I want to eat something sweet': 'Хочу полакомиться сладеньким', 'Doggy': 'Сзади', 'Cowgirl': 'Наездница', 'Missionary': 'Миссионерская поза', 'Flat doggy': 'Сзади лёжа', 'Reverse cowgirl': 'Обратная наездница', 'Stop her': 'Остановить её', "Don't stop her": 'Не останавливать её', 'Cum in her mouth': 'Кончить ей в рот', 'Use my tongue': 'Использовать язык', 'Finger her ass': 'Ввести палец ей в попку', 'Use the vibrator': 'Использовать вибратор', 'Use vibrator and my finger.': 'Использовать вибратор и палец.', 'Use some toy': 'Использовать игрушку', "Don't use toys": 'Без игрушек', 'Anal beads': 'Анальные шарики', 'Dildo': 'Фаллоимитатор', 'Blindfold': 'Повязка на глаза', 'Fuck her ass': 'Трахнуть её в попку', 'Fuck her pussy': 'Трахнуть её в киску', 'Take the vibrator out': 'Вытащить вибратор', "Don't": 'Не надо', 'Take the beads out': 'Вытащить шарики', 'Cum in her ass': 'Кончить ей в попку', 'Pull out of her ass': 'Вытащить из её попки', 'Rough': 'Грубо', 'Gentle': 'Нежно', 'No': 'Нет', "They're okay": 'Нормально к ним отношусь', 'I love them': 'Я их люблю', "I can't stand kids.": 'Не выношу детей.', 'Cum on her back': 'Кончить ей на спину', 'Call me Sugar': 'Зови меня Сладким', 'Stop calling me Sugar': 'Не зови меня Сладким', 'Call me Baby': 'Зови меня Малышом', 'Stop calling me Baby': 'Не зови меня Малышом', 'Call me Smooth rider': 'Зови меня Лихим наездником', 'Stop calling me Smooth rider': 'Не зови меня Лихим наездником', 'Call me Sweetheart': 'Зови меня Любимым', 'Stop calling me Sweetheart': 'Не зови меня Любимым', 'Call me Muffin': 'Зови меня Маффином', 'Stop calling me Muffin': 'Не зови меня Маффином', 'From now on I will stop calling you Cupcake': 'Больше не буду звать тебя Кексиком', 'From now on I will call you Cupcake': 'Отныне буду звать тебя Кексиком', 'Cancel': 'Отмена', 'Not sure': 'Не уверен', 'Changing your hair color': 'Покрасить волосы', 'Getting pierced': 'Сделать пирсинг', 'Getting tattoos': 'Сделать татуировки', 'Getting cum on your face': 'Получить сперму на лицо', 'Propose to buy it': 'Предложить купить', 'Propose to help': 'Предложить помощь', 'Kiss her': 'Поцеловать её', "Don't kiss her": 'Не целовать её'}
    nicknames = {'sugar':'сладкий','baby':'малыш','smooth rider':'лихой наездник',
        'sweetheart':'любимый','muffin':'маффин','master':'господин',
        'daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'sugar':'sugar','baby':'baby','smooth rider':'smooth_rider',
        'sweetheart':'sweetheart','muffin':'muffin'}
    names = {'Mary':'Мэри','Patricia':'Патриция','Linda':'Линда','Barbara':'Барбара',
        'Elizabeth':'Элизабет','Jennifer':'Дженнифер','Maria':'Мария','Susan':'Сьюзан',
        'Sarah':'Сара','Kimberly':'Кимберли','Deborah':'Дебора','Shirley':'Ширли',
        'Cinthia':'Синтия','Margaret':'Маргарет','Dorothy':'Дороти','Lisa':'Лиза',
        'Nancy':'Нэнси','Karen':'Карен','Betty':'Бетти','Helen':'Хелен','Sandra':'Сандра',
        'Donna':'Донна','Carol':'Кэрол','Ruth':'Рут','Sharon':'Шэрон','Michelle':'Мишель','Laura':'Лора'}
    phrases = {
        'He spent the whole time looking at other girls.':'Он всё время пялился на других девушек.',
        'He is so sexy in a swimsuit.':'Он такой сексуальный в плавках.',
        "Don't tell anyone but I blew him in the lockers.":'Никому не говори, но я отсосала ему в раздевалке.',
        'He made me come with his fingers in the water.':'Он довёл меня пальцами до оргазма прямо в воде.',
        "I can't believe he hit on that girl while I was here.":'Не могу поверить, что он клеился к той девушке прямо при мне.',
        "I couldn't stop looking at his ass.":'Я не могла оторвать глаз от его задницы.',
        'We fucked behind a tree.':'Мы потрахались за деревом.',
        'He ate my pussy behind a bush.':'Он вылизал мне киску за кустом.'}
    def hero_name():
        return display_name(store.hero.name)
    def display_name(value):
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.samantha.flags.mikeNickname
        if speaker == 'samantha' and store.hero.gender == 'male' and chosen:
            if str(chosen).lower() == str(value).lower():
                key = str(value).lower()
                return nicknames[key] if key in nicknames else value
            for key,group in aliases.items():
                if chosen in getattr(store,'nickname_'+group,()) and str(value).lower()==key:
                    return nicknames[key]
        return value
    def action_text(value):
        return {'kissing':'целуемся','groping':'ласкаем друг друга'}.get(value,value)
    def random_name(value):
        return names.get(value,value)
    def clothes_text(value):
        return {'trouser':'брюки','shirt':'рубашка','cap':'кепка','vest':'жилет'}.get(value,value)
    def colour_text(value):
        return {'Blue':'Синий','Red':'Красный','Yellow':'Жёлтый','green':'зелёный','orange':'оранжевый','pink':'розовый'}.get(value,value)
    def phrase_text(value):
        return phrases.get(value,value)
    def season_text(value):
        return {'spring':'весны','summer':'лета','fall':'осени','autumn':'осени','winter':'зимы'}.get(value,value)
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node = engine.game.script.namemap.get(engine.game.context().current)
        filename = getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith('ch/samantha/'):return strings.get(value,value)
        return store.lssb_palla.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1054 python:
    config.language_callbacks['russian'].append(lssb_samantha.enter)
    for _lssb_samantha_language in set(renpy.known_languages()) | {None}:
        if _lssb_samantha_language != 'russian':
            config.language_callbacks[_lssb_samantha_language].append(lssb_samantha.leave)

screen choice(items):
    variant 'lssb_samantha_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_samantha.caption(i.caption) action i.action
