# Presentation only. Preserve native names, scene statements and menu actions.
init 1037 python in lssb_kleio:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_kleio_ru'
    strings = {'Ask Kleio on a date': 'Пригласить Клео на свидание', "Meet Kleio and Anna for a 'hot coffee'": 'Встретиться с Клео и Анной за «горячим кофе»', "Meet Kleio, Anna and Sasha for a 'hot coffee'": 'Встретиться с Клео, Анной и Сашей за «горячим кофе»', 'Take Amy and Kleio out drinking': 'Пригласить Эми и Клео выпить', 'Get the band together (Amy, Anna, Kleio and Sasha)': 'Собрать группу вместе: Эми, Анну, Клео и Сашу', "See you in Sasha's room": 'Увидимся в комнате Саши', "Let's meet in my room": 'Давай встретимся в моей комнате', 'Just wanted to see you': 'Просто хотел тебя увидеть', 'Forget it': 'Забудь', 'Play it cool': 'Сохранять невозмутимость', 'Tell her to behave': 'Велеть ей вести себя прилично', 'Smile wider': 'Улыбнуться шире', 'Drop it': 'Оставить тему', 'Offer to take her': 'Предложить сходить вместе', 'Say her taste is basic': 'Назвать её вкус банальным', 'Be gentle with her': 'Проявить нежность', 'Brush her off': 'Отмахнуться от неё', 'Lead the way': 'Веди', 'Rain check': 'В другой раз', 'Talk music with her': 'Поговорить с ней о музыке', 'Ignore her': 'Игнорировать её', 'Take the compliment': 'Принять комплимент', 'Call her soft': 'Назвать её размякшей', 'Suggest something to do': 'Предложить занятие', 'Let her boss you around': 'Позволить ей командовать', 'Agree she was talented': 'Согласиться, что та девушка талантлива', 'Ask if she was your type': 'Спросить, в её ли она вкусе', 'Get possessive': 'Проявить собственничество', 'Change the subject': 'Сменить тему', 'Say yes': 'Сказать «да»', 'Dodge the question': 'Уклониться от вопроса', 'Tell her you love her too': 'Сказать, что тоже любишь её', 'Tease her about it': 'Подразнить её', 'Compliment': 'Сделать комплимент', 'Criticize': 'Раскритиковать', 'Defend Kleio': 'Защитить Клео', 'Defend [bree.name]': 'Защитить [bree.name]', 'Accept': 'Согласиться', 'Object': 'Возразить', 'Michael Johnson': 'Майкл Джонсон', 'Metallikea': 'Metallikea', 'Pelvis Resley': 'Пелвис Ресли', 'Disrupted': 'Disrupted', 'Wolf': 'Волк', 'Angel wings': 'Ангельские крылья', 'None': 'Ничего', 'No way': 'Ни за что', 'Yes': 'Да', 'Yeah': 'Ага', 'No': 'Нет', 'Not right now': 'Не сейчас', 'Sure': 'Конечно', 'Tattoo': 'Татуировка', 'Piercing': 'Пирсинг', 'Insist': 'Настоять', 'Go along': 'Подыграть', 'Tell her to slow down': 'Попросить её сбавить скорость', 'Enjoy the ride': 'Наслаждаться поездкой', 'Friends works for me': 'Дружба меня устраивает', 'Is this about the band?': 'Дело в группе?', 'Your loss': 'Сама виновата', 'Walk Sasha home': 'Проводить Сашу домой', 'Let her leave': 'Позволить ей уйти', 'Tell her to stay': 'Велеть ей остаться', 'Use a condom': 'Использовать презерватив', 'Do it raw': 'Без презерватива', 'No!': 'Нет!', 'Yes!': 'Да!', 'Be cool': 'Сохранять спокойствие', 'Be jealous': 'Ревновать', 'Bail Kleio out': 'Внести залог за Клео', "Don't bail Kleio out": 'Не вносить залог за Клео', 'Say no': 'Сказать «нет»', "For kids, not for kids... Noodles, don't noodles...": 'Для детей, не для детей... Лапша, не лапша...', 'Say whaaat?!?': 'Чего-о-о?!', 'Warn the lady your "Fury Road" mode is on!': 'Предупредить даму, что включён режим «Дорога ярости»!', "Impress the lady by telling her you're here with your kids": 'Впечатлить даму, сказав, что ты здесь со своими детьми', "Don't let her bother you. Pitch something": 'Не обращать на неё внимания и что-нибудь предложить', 'Anyway... follow her lead to please her': 'Всё же последовать за ней, чтобы порадовать', "Show her what it's like to be the best": 'Показать ей, что значит быть лучшим', "Let her win, it's her birthday after all": 'Позволить ей выиграть — всё-таки день рождения', "Let's race again!": 'Давай ещё заезд!', "Another time maybe, I don't feel like it": 'Может, в другой раз. Сейчас не хочется', "It's a deal": 'По рукам', 'Nonsense': 'Ерунда', 'Agree': 'Согласиться', 'Disagree': 'Не согласиться', 'Side with Sasha': 'Поддержать Сашу', 'Side with Kleio': 'Поддержать Клео', "Ask Anna's opinion": 'Спросить мнение Анны', "Let's keep the baby": 'Давай оставим ребёнка', 'Tell her to abort': 'Сказать ей прервать беременность', 'Play with [bree.name]': 'Играть с [bree.name]', 'Play with Kleio': 'Играть с Клео', 'Cum inside': 'Кончить внутрь', 'Cum outside': 'Кончить снаружи', 'Go down on her': 'Поласкать её языком', 'Let her go down on me': 'Позволить ей сделать минет', 'Skip': 'Пропустить', 'Missionary': 'Миссионерская поза', 'Cowgirl': 'Наездница', 'Doggy': 'Сзади', 'Reverse cowgirl': 'Обратная наездница', 'Fuck her pussy': 'Трахнуть в киску', 'Fuck her ass': 'Трахнуть в попку', 'Use my tongue': 'Ласкать языком', 'Finger her ass': 'Ввести палец ей в попку', 'Use the dildo': 'Использовать фаллоимитатор', 'Use the anal beads': 'Использовать анальные шарики', 'Use dildo and my finger.': 'Использовать фаллоимитатор и палец', 'Cum on her face': 'Кончить на лицо', 'Cum in her mouth': 'Кончить в рот', 'Stop before cumming': 'Остановиться до оргазма', 'Let Kleio have her way': 'Отдаться во власть Клео', 'Keep it professional': 'Заняться репетицией', 'Let go': 'Оставить тему', 'Ask about the women': 'Спросить о женщинах', "Tell her she's got you now": 'Сказать, что теперь у неё есть ты', 'I am a conservative': 'Я консерватор', 'I am a liberal': 'Я либерал', 'I can take you to fast food': 'Могу сводить тебя за фастфудом', 'I can cook for you.': 'Могу приготовить для тебя', "What's wrong with girls in pink dresses?": 'Что плохого в девушках в розовых платьях?', 'You look badass': 'Ты выглядишь круто', 'Tell her what to wear': 'Указать ей, что надеть', 'Say nothing': 'Промолчать', 'Call me Boy': 'Называй меня мальчиком', 'Stop calling me Boy': 'Не называй меня мальчиком', 'Call me Dumbass': 'Называй меня придурком', 'Stop calling me Dumbass': 'Не называй меня придурком', 'Call me Twink': 'Называй меня твинком', 'Stop calling me Twink': 'Не называй меня твинком', 'Call me Playboy': 'Называй меня плейбоем', 'Stop calling me Playboy': 'Не называй меня плейбоем', 'Call me Boytoy': 'Называй меня мальчиком-игрушкой', 'Stop calling me Boytoy': 'Не называй меня мальчиком-игрушкой', 'Call me Love': 'Называй меня любимым', 'Stop calling me Love': 'Не называй меня любимым', 'Cancel': 'Отмена'}
    nicknames = {'boy':'мальчик','dumbass':'придурок','twink':'твинк','playboy':'плейбой','boytoy':'мальчик-игрушка','love':'любимый',
        'master':'господин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'boy':'boy','dumbass':'dumbass','twink':'twink','playboy':'playboy','boytoy':'boytoy','love':'love'}

    def hero_name():
        value = store.hero.name
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.kleio.flags.mikeNickname
        if speaker == 'kleio' and store.hero.gender == 'male' and not chosen and store.kleio.sexperience == 0 and str(value).lower() == 'dumbass':
            return 'придурок'
        if speaker == 'kleio' and store.hero.gender == 'male' and chosen:
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
        if filename.startswith('ch/kleio/'):return strings.get(value,value)
        return store.lssb_jack.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1038 python:
    config.language_callbacks['russian'].append(lssb_kleio.enter)
    for _lssb_kleio_language in set(renpy.known_languages()) | {None}:
        if _lssb_kleio_language != 'russian':
            config.language_callbacks[_lssb_kleio_language].append(lssb_kleio.leave)

screen choice(items):
    variant 'lssb_kleio_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_kleio.caption(i.caption) action i.action
