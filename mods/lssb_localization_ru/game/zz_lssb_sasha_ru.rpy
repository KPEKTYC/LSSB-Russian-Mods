# Native presentation only. Scene statements and choice actions are untouched.
init -9 python in lssb_sasha:
    import renpy
    _constant = True
    version = "1.4.0"
    variant = "lssb_sasha_ru_26_8_0d"
    strings = {'Do it': 'Сделать это', "Don't do it": 'Не делать этого', 'Ask Sasha on a date': 'Пригласить Сашу на свидание', 'Ask Sasha and Audrey on a date': 'Пригласить Сашу и Одри на свидание', 'Visit Sasha and Palla at the store': 'Навестить Сашу и Паллу в магазине', "Meet Kleio, Anna and Sasha for a 'hot coffee'": 'Встретиться с Клео, Анной и Сашей за «горячим кофе»', 'Take Amy and Sasha to the amusement park': 'Сходить с Эми и Сашей в парк развлечений', 'Get the band together (Amy, Anna, Kleio and Sasha)': 'Собрать группу: Эми, Анна, Клео и Саша', 'See you in your room': 'Увидимся в твоей комнате', "Let's meet in my room": 'Встретимся в моей комнате', 'Take her out in the garden.': 'Отвести её в сад', 'Take her to the park.': 'Отвести её в парк', 'So come find out.': 'Тогда приходи и узнаешь', "Say that again and I'll put you on your knees.": 'Ещё раз так скажешь — поставлю тебя на колени', 'I love the thought of you and your bandmates.': 'Мне нравится представлять тебя с девушками из группы', 'Keep the groupies off my girl.': 'Не подпускай фанаток к моей девушке', 'Compliment': 'Сделать комплимент', 'Criticize': 'Раскритиковать', 'Defend Sasha': 'Защитить Сашу', 'Defend Scottie': 'Защитить Скотти', 'Side with Sasha': 'Встать на сторону Саши', 'Side with Scottie': 'Встать на сторону Скотти', 'Tell her to hurry up': 'Попросить её поторопиться', 'Let her take her time': 'Дать ей время', 'Take it': 'Взять', 'Give it to her': 'Отдать ей', 'Let her buy the first round': 'Пусть она угостит первой', 'Buy Sasha a drink': 'Угостить Сашу выпивкой', 'Invite her in': 'Пригласить её войти', 'Help her': 'Помочь ей', 'Take the boxes from her': 'Забрать у неё коробки', 'Go grab more boxes outside': 'Сходить за остальными коробками', 'Joke': 'Пошутить', 'Laugh': 'Рассмеяться', 'Be awkward': 'Смутиться', 'Tell her to keep it quiet': 'Попросить её вести себя потише', 'Offer to help': 'Предложить помощь', 'Accept': 'Согласиться', 'Refuse': 'Отказаться', 'Joke and agree': 'Отшутиться и согласиться', 'Just agree': 'Просто согласиться', 'No': 'Нет', 'Yes': 'Да', "Don't look at the toys": 'Не смотреть на игрушки', 'Look at the toys': 'Посмотреть на игрушки', 'Offer more help': 'Предложить ещё помощь', 'Stop helping': 'Закончить помогать', 'Be surprised': 'Удивиться', 'Be interested': 'Заинтересоваться', 'Talk to her': 'Поговорить с ней', 'Leave her alone': 'Оставить её в покое', 'Yes, later': 'Да, позже', 'Yes, now': 'Да, сейчас', 'Invite her': 'Пригласить её', 'Order food': 'Заказать еду', 'Leave': 'Уйти', 'Open the door': 'Открыть дверь', 'Knock on the door': 'Постучать в дверь', "Don't play too late.": 'Не играй допоздна', "That's great.": 'Это здорово', 'No, thank you.': 'Нет, спасибо', 'If that is what you want, then yes!': 'Если ты этого хочешь, то да!', 'Okay.': 'Хорошо', 'Well, I like that!': 'А мне нравится!', "I'm sure you can think of something to do.": 'Уверен, ты придумаешь, чем заняться', 'I can think of games we could play.': 'Я знаю, во что мы могли бы поиграть', 'I would love to do whatever you want.': 'С удовольствием сделаю всё, что захочешь', 'Sure, I can think of things we could do together.': 'Конечно, я придумаю, чем нам заняться вместе', "Nah, that doesn't sound like a good idea.": 'Не-а, не лучшая идея', 'I want you to come and do it with me.': 'Хочу, чтобы ты пришла и сделала это со мной', 'Whatever you want to do is just fine with me.': 'Меня устроит всё, что ты захочешь', "Yeah, I'd love to do something together with you.": 'Да, я с радостью провёл бы с тобой время', 'Nope. Just you!': 'Нет. Только ты!', "I give help, I don't need help.": 'Я помогаю другим, мне помощь не нужна', 'I do': 'Да', "No, but I don't need anyone.": 'Нет, но мне никто и не нужен', 'I never wanted to before, but now...': 'Раньше не хотелось, но теперь...', "It didn't seem important to me.": 'Мне это не казалось важным', 'I was waiting for a time of my choosing.': 'Я ждал подходящего момента', "I didn't want to offend you": 'Я не хотел тебя обидеть', 'I can play guitar': 'Я умею играть на гитаре', 'Say nothing': 'Промолчать', 'Ok': 'Ладно', 'No way': 'Ни за что', 'Sure': 'Конечно', 'Follow Sasha immediately': 'Сразу пойти за Сашей', 'Follow Sasha after a minute': 'Пойти за Сашей через минуту', 'Follow Sasha after five minutes': 'Пойти за Сашей через пять минут', "Tighten the dog collar round Sasha's neck": 'Затянуть ошейник на шее Саши', "Massage Sasha's tense muscles": 'Помассировать напряжённые мышцы Саши', 'Teach Sasha a breathing exercise': 'Научить Сашу дыхательному упражнению', 'Not as low as they were.': 'Не настолько, как раньше', "You're right. Sasha's a goddess.": 'Верно. Саша — богиня', "She'll be mine soon enough.": 'Скоро она будет моей', 'You should give him a second chance': 'Тебе стоит дать ему второй шанс', "Don't bother with the dude (Never meet Scottie again)": 'Забудь о нём (больше не встречаться со Скотти)', 'You already know': 'Ты и так знаешь', 'Watch': 'Посмотреть', 'Change your mind': 'Передумать', 'Stick with it': 'Настоять на своём', 'I prefer blondes': 'Мне больше нравятся блондинки', "I don't prefer blondes": 'Не отдаю предпочтения блондинкам', "I don't like it": 'Мне не нравится', 'I love it': 'Мне очень нравится', 'I like them small': 'Мне нравится маленькая грудь', 'I like them big': 'Мне нравится большая грудь', "I'll help you pay for it": 'Я помогу тебе оплатить операцию', "That's a great idea": 'Отличная идея', 'You should not do it': 'Не стоит этого делать', "It's not that good": 'Не так уж и здорово', 'You should have some of the pastries too': 'Тебе тоже стоит попробовать выпечку', "I'm happy that it pleases you": 'Рад, что тебе приятно', "I'm glad you like it": 'Рад, что тебе нравится', 'We will come here again': 'Мы ещё сюда придём', 'I would love to do that': 'Я бы с удовольствием', "I don't have time for that": 'У меня на это нет времени', 'Is that a come-on?': 'Ты ко мне подкатываешь?', "Let's keep the baby": 'Давай оставим ребёнка', 'Tell her to abort': 'Сказать ей сделать аборт', 'Dump Sasha': 'Бросить Сашу', 'Agree': 'Согласиться', 'Try to ignore the inconvenience': 'Постараться не замечать неудобства', "Let Sasha know what she's responsible for": 'Объяснить Саше, в чём она виновата', 'Admit it': 'Признаться', 'Taunt her': 'Поддразнить её', 'Ask for a rimjob': 'Попросить римминг', 'Ask for a handjob': 'Попросить подрочить', 'Fuck her tits': 'Трахнуть её между грудей', 'Eat her pussy': 'Полизать её киску', 'Use the anal beads': 'Взять анальные бусы', 'Use the rope': 'Взять верёвку', 'Just fuck her': 'Просто трахнуть её', 'Use the rope again': 'Снова взять верёвку', 'Missionary': 'Миссионерская поза', 'Cowgirl': 'Наездница', 'Standing': 'Стоя', 'Doggy': 'Раком', 'Keep spanking': 'Продолжать шлёпать', 'Get on with the beads': 'Перейти к бусам', 'Cum on her face': 'Кончить ей на лицо', 'Cum in her mouth': 'Кончить ей в рот', 'Use my tongue': 'Пустить в ход язык', 'Finger her ass': 'Ввести палец ей в попу', 'Use the dildo': 'Взять фаллоимитатор', 'Use dildo and my finger.': 'Взять фаллоимитатор и пустить в ход палец', "Cum in Sasha's mouth": 'Кончить Саше в рот', "Cum on Sasha's face": 'Кончить Саше на лицо', 'Fuck her ass': 'Трахнуть её в попу', 'Fuck her pussy': 'Трахнуть её в киску', 'Make her suck you off': 'Заставить её отсосать', 'Just go on': 'Просто продолжать', 'Choke her': 'Придушить её', 'Keep going': 'Продолжать', 'Do not choke Sasha': 'Не душить Сашу', 'Spank her': 'Отшлёпать её', 'Use the gag ball': 'Взять кляп-шарик', 'Fuck her ass instead': 'Вместо этого трахнуть её в попу', "Don't cum": 'Не кончать', 'Doggy style': 'Раком', 'Hand it over': 'Передать ей', 'Tease her': 'Поддразнить её', 'Call me Dumbass': 'Называй меня «Придурок»', 'Stop calling me Dumbass': 'Не называй меня «Придурок»', 'Call me Idiot': 'Называй меня «Идиот»', 'Stop calling me Idiot': 'Не называй меня «Идиот»', 'Call me Chad': 'Называй меня «Чад»', 'Stop calling me Chad': 'Не называй меня «Чад»', 'Call me Boo': 'Называй меня «Милый»', 'Stop calling me Boo': 'Не называй меня «Милый»', 'Call me Fuck Face': 'Называй меня «Хрен моржовый»', 'Stop calling me Fuck Face': 'Не называй меня «Хрен моржовый»', 'Call me My Big Bear': 'Называй меня «Мой большой мишка»', 'Stop calling me My Big Bear': 'Не называй меня «Мой большой мишка»', 'Cancel': 'Отмена', 'Finding love': 'Найти любовь', 'Becoming rich': 'Разбогатеть', 'Banging a lot of women': 'Переспать со множеством женщин', "Don't talk to her": 'Не разговаривать с ней', "Don't tease her": 'Не дразнить её', 'Maybe': 'Возможно'}
    seasons = {"spring":"весны", "summer":"лета", "fall":"осени", "autumn":"осени", "winter":"зимы"}
    weekdays = {"monday":"понедельник", "tuesday":"вторник", "wednesday":"среда", "thursday":"четверг",
        "friday":"пятница", "saturday":"суббота", "sunday":"воскресенье"}
    nicknames = {"dumbass":"придурок", "idiot":"идиот", "chad":"Чад", "boo":"милый",
        "fuck face":"хрен моржовый", "my big bear":"мой большой мишка", "master":"хозяин",
        "daddy":"папочка", "sweetie":"милый", "handsome":"красавчик", "bro":"братан",
        "stud":"жеребец", "husband":"муж", "sugar":"сладкий", "honey":"милый"}

    def nickname(value, speaker, chosen):
        if (speaker == "sasha" and renpy.store.hero.gender == "male" and chosen
                and str(chosen).lower() == str(value).lower()):
            return nicknames.get(str(value).lower(), value)
        return value

    def hero_name():
        # Translate only an explicitly selected nickname at this text substitution.
        # The native name property, nickname function and save flags remain intact.
        value = renpy.store.hero.name
        who = renpy.exports.last_say().who
        speaker = who.name.lower().replace("_name", "") if who and hasattr(who, "name") else None
        return nickname(value, speaker, renpy.store.sasha.flags.mikeNickname)

    def season(value):
        return seasons.get(value, value)

    def weekday(value):
        return weekdays.get(str(value).lower(), value)

    def caption(value):
        if renpy.game.preferences.language != "russian" or False:
            return value
        node = renpy.game.script.namemap.get(renpy.game.context().current)
        filename = getattr(node, "filename", "").replace("\\", "/").split("/game/")[-1]
        if filename.startswith("game/"):
            filename = filename[5:]
        if filename.startswith("ch/sasha/"):
            return strings.get(value, value)
        # The single choice screen composes the two personal-branch dictionaries.
        return renpy.store.lssb_bree.caption(value)

    def enter():
        if True and variant not in renpy.store.config.variants:
            renpy.store.config.variants.insert(0, variant)

    def leave():
        if variant in renpy.store.config.variants:
            renpy.store.config.variants.remove(variant)

init 1012 python:
    if True:
        config.language_callbacks["russian"].append(lssb_sasha.enter)
        for _lssb_sasha_language in set(renpy.known_languages()) | {None}:
            if _lssb_sasha_language != "russian":
                config.language_callbacks[_lssb_sasha_language].append(lssb_sasha.leave)

screen choice(items):
    variant "lssb_sasha_ru_26_8_0d"
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton lssb_sasha.caption(i.caption) action i.action
