# Presentation only. Preserve native names, scene statements and menu actions.
init 1031 python in lssb_hanna:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_hanna_ru'
    strings = {'Play fetch with Hanna': 'Поиграть с Ханной в «принеси»', 'Make Hanna walk to heel': 'Велеть Ханне идти рядом', 'Stop her': 'Остановить её', 'Let her continue': 'Позволить ей продолжить', 'Compliment': 'Похвалить', 'Criticize': 'Раскритиковать', 'Outdo Scottie': 'Превзойти Скотти', 'Tell Scottie and Hanna off': 'Отчитать Скотти и Ханну', 'Dance': 'Танцевать', 'Do not dance': 'Не танцевать', 'Yes': 'Да', "That's not my name": 'Меня зовут не так', 'How do you know my name?': 'Откуда ты знаешь моё имя?', 'See ya': 'Увидимся', 'You were checking me out': 'Ты меня разглядывала', 'I know what you did': 'Я знаю, что ты сделала', 'I mind': 'Я против', "I don't mind": 'Я не против', 'You should sell it': 'Тебе стоит его продать', 'I can lend you that money': 'Я могу одолжить тебе эти деньги', 'You could make it more attractive': 'Можно сделать его привлекательнее', 'Encourage Hanna to dance': 'Поощрить Ханну танцевать', 'Discourage Hanna from dancing': 'Отговорить Ханну от танцев', 'This is a date!': 'Это свидание!', "It's fine Hanna, you don't need to": 'Всё хорошо, Ханна, не нужно', 'I accept the money from Hanna': 'Принять деньги от Ханны', 'I do not accept the money from Hanna': 'Отказаться от денег Ханны', 'I insist Hanna reinvest the money in the gym': 'Настоять, чтобы Ханна вложила деньги обратно в спортзал', 'Fuck her ass': 'Трахнуть в попку', 'Fuck her pussy': 'Трахнуть в киску', "Let's get married!": 'Давай поженимся!', 'I need time to think about it.': 'Мне нужно время подумать', "Don't intervene": 'Не вмешиваться', 'Stop the patron touching Hanna': 'Помешать посетителю трогать Ханну', 'Accept': 'Согласиться', 'Refuse': 'Отказаться', 'Cum on her face': 'Кончить на лицо', 'Cum in her mouth': 'Кончить в рот', 'You should have a termination': 'Тебе стоит прервать беременность', 'We should keep it': 'Нам стоит оставить ребёнка', 'Be patient': 'Терпеливо ждать', 'Point at my watch': 'Указать на часы', 'Bribe the bouncer': 'Дать взятку вышибале', 'Argue with the bouncer': 'Спорить с вышибалой', 'Order another round': 'Заказать ещё выпивки', 'Slow down Hanna': 'Притормози, Ханна', 'Let her keep it': 'Позволить ей принять напиток', 'Send it back': 'Отправить обратно', 'Go down on her': 'Поласкать языком', 'Just fuck her': 'Сразу заняться сексом', 'Cowgirl': 'Наездница', 'Doggy': 'Сзади', 'Missionary': 'Миссионерская поза', 'You': 'Ты', 'Someone else': 'Кто-то другой', "I don't need love": 'Мне не нужна любовь', 'Myself': 'Я сам', 'Love it': 'Обожаю', 'Want You': 'Хочу тебя', 'I am a dom': 'Я люблю доминировать', 'I am a sub': 'Я люблю подчиняться', 'Agree': 'Согласиться', 'Disagree': 'Не согласиться', 'Both': 'И то и другое', "I don't know": 'Не знаю', 'Whatever': 'Что угодно', 'Junk Food': 'Вредная еда', 'Healthy Eating': 'Здоровое питание', "I'm a Vegan": 'Я веган', 'Hiking trail': 'Пеший поход', 'Different country': 'Другая страна', 'Theme park': 'Парк развлечений', 'Nope': 'Нет', 'In the Zone': 'Полная сосредоточенность', 'Soap Opera': 'Мыльные оперы', 'Nutflix and Chill': '«Натфликс» и отдых', 'Super Hero': 'Супергерои', 'Nope.': 'Нет', 'E-sports and speedrunning': 'Киберспорт и скоростные прохождения', 'Running': 'Бег', 'Sex': 'Секс', 'Cute': 'Милое', 'Slutty': 'Распутное', 'Sweaty': 'Пропотевшее', 'Nothing': 'Ничего', 'Fantasy': 'Фэнтези', 'Fitness': 'Фитнес', 'Romance': 'Любовные романы', 'Comics': 'Комиксы', 'Love people': 'Люблю людей', 'Hate people': 'Ненавижу людей', 'Depends': 'Зависит от людей', 'How about you': 'А ты?', 'Gym girls': 'Девушки из спортзала', 'Only me': 'Только я', 'Teach': 'Научить', 'Doubt': 'Усомниться', 'No': 'Нет', 'Inspirational 80s media': 'Вдохновляющая музыка из фильмов восьмидесятых', 'Anime soundtracks': 'Саундтреки аниме', 'Rock, metal': 'Рок, метал', 'Call me Champ': 'Называй меня чемпионом', 'Stop calling me Champ': 'Не называй меня чемпионом', 'Call me Partner': 'Называй меня напарником', 'Stop calling me Partner': 'Не называй меня напарником', 'Cancel': 'Отмена'}
    nicknames = {'champ':'чемпион','partner':'напарник',
        'master':'господин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'champ':'champ','partner':'partner'}

    def hero_name():
        value = store.hero.name
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.hanna.flags.mikeNickname
        if speaker == 'hanna' and store.hero.gender == 'male' and chosen:
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
        if filename.startswith('ch/hanna/'):return strings.get(value,value)
        return store.lssb_emma.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1032 python:
    config.language_callbacks['russian'].append(lssb_hanna.enter)
    for _lssb_hanna_language in set(renpy.known_languages()) | {None}:
        if _lssb_hanna_language != 'russian':
            config.language_callbacks[_lssb_hanna_language].append(lssb_hanna.leave)

screen choice(items):
    variant 'lssb_hanna_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_hanna.caption(i.caption) action i.action
