# Translation-only layer. No game-version gate, gameplay mutation or service calls.
init 1013 python in lssb_audrey:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_audrey_ru'
    strings = {'Accept': 'Согласиться', 'Accuse Aletta': 'Обвинить Алетту', 'Accuse Audrey': 'Обвинить Одри', 'Accuse Shiori': 'Обвинить Сиори', 'Agree': 'Согласиться', 'Ask Audrey and Palla on a date': 'Пригласить Одри и Паллу на свидание', 'Ask Audrey and Sasha on a date': 'Пригласить Одри и Сашу на свидание', 'Ask Audrey on a date': 'Пригласить Одри на свидание', 'Ask Audrey, Cassidy and Palla on a date': 'Пригласить Одри, Кэссиди и Паллу на свидание', 'Attack him': 'Напасть на него', 'Be gentle': 'Быть нежным', 'Be passive': 'Не проявлять инициативу', 'Blowjob': 'Минет', 'Call me Chief': 'Называй меня «Шеф»', 'Call me Dick': 'Называй меня «Хрен»', 'Call me Master': 'Называй меня «Хозяин»', 'Cancel': 'Отмена', 'Choke her': 'Придушить её', 'Compliment': 'Сделать комплимент', 'Continues spanking Audrey': 'Продолжать шлёпать Одри', 'Cowgirl': 'Наездница', 'Create a personal moment': 'Поговорить по душам', 'Create a romantic moment': 'Создать романтическую атмосферу', 'Criticize': 'Раскритиковать', 'Cum in her mouth': 'Кончить ей в рот', 'Cum inside': 'Кончить внутрь', 'Cum on her face': 'Кончить ей на лицо', 'Cunnilingus': 'Куннилингус', 'Defend Audrey': 'Вступиться за Одри', 'Defend Sasha': 'Вступиться за Сашу', 'Deny responsibility': 'Отрицать свою причастность', 'Disagree': 'Не согласиться', 'Do not choke her': 'Не душить её', 'Do nothing': 'Ничего не делать', 'Doggy': 'Раком', "Don't Grind": 'Не прижиматься к ней', "Don't choke her": 'Не душить её', "Don't feel her up": 'Не лапать её', "Don't get involved": 'Не вмешиваться', "Don't go": 'Не идти', "Don't go over to Audrey": 'Не подходить к Одри', "Don't let Audrey do whatever she wants": 'Не позволять Одри делать всё, что ей вздумается', "Don't slide hand up": 'Не поднимать руку выше', 'Feel her up': 'Полапать её', 'Fight fire with fire': 'Ответить тем же', 'Finger her pussy': 'Поласкать её киску пальцами', 'Fingers her ass': 'Поласкать её попу пальцами', 'Forget it': 'Забыть об этом', 'Fuck': 'Трахнуть её', "Fuck Audrey's ass": 'Трахнуть Одри в попу', "Fuck Audrey's pussy": 'Трахнуть Одри в киску', 'Fuck her ass': 'Трахнуть её в попу', 'Fuck her pussy': 'Трахнуть её в киску', 'Give her what she deserves': 'Дать ей по заслугам', 'Go': 'Пойти', 'Go over to Audrey': 'Подойти к Одри', 'Go to the bedroom.': 'Пойти в спальню', 'Grind on her': 'Прижаться к ней и потереться', 'Have her spit it out': 'Велеть ей выплюнуть', 'Help her': 'Помочь ей', 'Intimidate him': 'Припугнуть его', 'Investigate': 'Разобраться', 'Keep calm': 'Сохранять спокойствие', 'Keep going': 'Продолжать', 'Keep the kiss innocent': 'Ограничиться невинным поцелуем', 'Lash out': 'Сорваться на неё', 'Laugh it off': 'Отшутиться', 'Lay her on the couch': 'Уложить её на диван', 'Lead her on': 'Подыграть ей', 'Let Aletta stay': 'Позволить Алетте остаться', 'Let Audrey have her way': 'Уступить Одри', 'Let her keep doing it': 'Позволить ей продолжать', 'Let her swallow it': 'Позволить ей проглотить', 'Make her stop': 'Заставить её остановиться', 'Make the kiss heavier': 'Поцеловать её страстнее', "Meet Alexis, Audrey and Reona for a 'hot coffee'": 'Встретиться с Алексис, Одри и Реоной за «горячим кофе»', 'Missionary': 'Миссионерская поза', 'No': 'Нет', "No, I don't have time": 'Нет, у меня нет времени', 'Oral': 'Оральный секс', "Pretend she's yours": 'Притвориться, что она твоя девушка', 'Protest': 'Возразить', 'Pull out': 'Вынуть', 'Push Audrey gently': 'Мягко отстранить Одри', 'Push Audrey hard': 'С силой оттолкнуть Одри', 'Refuse': 'Отказаться', 'Restrain myself': 'Сдержаться', 'Reverse cowgirl': 'Обратная наездница', "Show her who's the boss": 'Показать ей, кто здесь главный', "Show her who's the boss.": 'Показать ей, кто здесь главный', 'Slide hand up': 'Поднять руку выше', 'Spank her': 'Отшлёпать её', 'Spoon': 'Ложечки', 'Stand': 'Стоя', 'Stay professional': 'Сохранять профессиональную дистанцию', 'Step in': 'Вмешаться', 'Stop': 'Остановиться', 'Stop Audrey': 'Остановить Одри', 'Stop calling me Chief': 'Не называй меня «Шеф»', 'Stop calling me Dick': 'Не называй меня «Хрен»', 'Stop calling me Master': 'Не называй меня «Хозяин»', 'Sure': 'Конечно', 'Take charge': 'Взять инициативу в свои руки', 'Take out a beer': 'Достать пиво', 'Take out the champagne': 'Достать шампанское', 'Tease her': 'Поддразнить её', 'Tell Aletta to leave': 'Сказать Алетте уйти', 'Tell her': 'Сказать ей', 'Tell her to never do that again': 'Сказать ей больше никогда так не делать', 'Tell her to spit it out': 'Сказать ей выплюнуть', 'Use her on the desk': 'Взять её на столе', 'Yes': 'Да'}
    nicknames = {'chief':'шеф','dick':'хрен','master':'хозяин',
        'daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    seasons = {'spring':'весны','summer':'лета','fall':'осени','autumn':'осени','winter':'зимы'}

    def nickname(value, speaker, chosen):
        if speaker == 'audrey' and store.hero.gender == 'male' and chosen:
            if str(chosen).lower() == str(value).lower():
                return nicknames.get(str(value).lower(), value)
            for key in ('chief','dick','master'):
                if chosen in getattr(store,'nickname_'+key,()) and str(value).lower()==key:
                    return nicknames[key]
        return value

    def hero_name():
        value=store.hero.name
        who=engine.exports.last_say().who
        speaker=who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        if (speaker == 'audrey' and value == 'Mister '+store.hero.family_name
                and store.audrey.heronickname.get('Mister hero.family_name') == 'audrey.love < 100'
                and store.audrey.love < 100):
            return 'мистер '+store.hero.family_name
        return nickname(value,speaker,store.audrey.flags.mikeNickname)

    def season(value):
        return seasons.get(value,value)

    def weekday(value):
        return {'monday':'понедельник','tuesday':'вторник','wednesday':'среда',
            'thursday':'четверг','friday':'пятница','saturday':'суббота',
            'sunday':'воскресенье'}.get(str(value).lower(),value)

    def greeting(value):
        return {'morning':'Доброе утро','afternoon':'Добрый день',
            'evening':'Добрый вечер','night':'Доброй ночи'}.get(str(value).lower(),'Здравствуй')

    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith('ch/audrey/'):return strings.get(value,value)
        return store.lssb_sasha.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1014 python:
    config.language_callbacks['russian'].append(lssb_audrey.enter)
    for _lssb_audrey_language in set(renpy.known_languages()) | {None}:
        if _lssb_audrey_language != 'russian':
            config.language_callbacks[_lssb_audrey_language].append(lssb_audrey.leave)

screen choice(items):
    variant 'lssb_audrey_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_audrey.caption(i.caption) action i.action
