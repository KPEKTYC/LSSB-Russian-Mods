# Presentation only. Preserve native names, scene statements and menu actions.
init 1017 python in lssb_alexis:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_alexis_ru'
    strings = {'You should leave': 'Тебе пора идти', 'You should sleep here': 'Останься ночевать здесь', 'Ask Alexis on a date': 'Пригласить Алексис на свидание', 'Set up a date with Alexis and Reona': 'Договориться о свидании с Алексис и Реоной', 'Meet Alexis and Reona for some pool fun': 'Развлечься с Алексис и Реоной в бассейне', "Meet Alexis, Audrey and Reona for a 'hot coffee'": 'Встретиться с Алексис, Одри и Реоной за «горячим кофе»', 'Agree': 'Согласиться', 'Disagree': 'Не согласиться', 'Admire the view': 'Полюбоваться видом', 'Disapprove': 'Выразить неодобрение', 'Be flattered': 'Принять как комплимент', 'Be offended': 'Обидеться', 'Agree and compliment Kylie': 'Согласиться и похвалить Кайли', 'Flirt back': 'Пофлиртовать в ответ', 'Blow her off': 'Отмахнуться от неё', 'Beg her for a private show': 'Упросить её станцевать только для тебя', 'Give Alexis a massage': 'Сделать Алексис массаж', 'Refuse to give Alexis a massage': 'Отказаться делать Алексис массаж', 'Agree to let Alexis cuddle': 'Разрешить Алексис прижаться', 'Refuse to let Alexis cuddle': 'Не дать Алексис прижаться', 'Reassure Alexis': 'Успокоить Алексис', "Don't reassure Alexis": 'Не успокаивать Алексис', 'Ask if she likes what she sees': 'Спросить, нравится ли ей то, что она видит', 'Tease her for being jealous': 'Поддразнить её за ревность', 'Agree with Alexis': 'Согласиться с Алексис', 'Disagree with Alexis': 'Не согласиться с Алексис', 'Compliment': 'Сделать комплимент', 'Criticize': 'Раскритиковать', 'Ignore it': 'Не обращать внимания', 'Call her out': 'Высказать ей претензии', 'React meekly': 'Отреагировать покорно', 'React strongly': 'Ответить решительно', 'Watch': 'Смотреть', 'Interfere': 'Вмешаться', 'Masturbate': 'Мастурбировать', 'Just watch': 'Просто смотреть', "Pull out Alexis' chair": 'Отодвинуть стул для Алексис', "Don't": 'Не делать этого', 'Say something': 'Что-нибудь сказать', 'Say nothing': 'Промолчать', 'Go check on her': 'Пойти проверить, где она', 'Wait': 'Подождать', 'Leave': 'Уйти', 'Agree (-2000$)': 'Согласиться (-2000$)', 'Refuse': 'Отказаться', 'Confront her': 'Потребовать от неё объяснений', 'Wait for her': 'Подождать её', 'Look for her': 'Пойти искать её', 'Tell her you forgive her': 'Сказать, что прощаешь её', 'Let her talk': 'Дать ей выговориться', "Don't believe her": 'Не поверить ей', 'Believe her': 'Поверить ей', 'Walk up and just introduce yourself': 'Подойти и просто представиться', 'Walk up and introduce yourself as a former student': 'Подойти и представиться бывшим учеником', 'Mike confesses how much he used to love gym class': 'Рассказать, как сильно любил уроки физкультуры', 'Claim you used to be a sporting prodigy': 'Заявить, что был спортивным вундеркиндом', 'Suggest to grab a beer': 'Предложить выпить пива', 'Suggest to grab a coffee': 'Предложить выпить кофе', 'Agree that things have changed for the worse': 'Согласиться, что всё изменилось к худшему', 'Ask about the coach being made to retire': 'Спросить, почему тренера вынудили уйти', 'Use a baseball bat': 'Использовать бейсбольную биту', 'Fight bare handed': 'Драться голыми руками', 'Accept': 'Согласиться', 'Ignore him': 'Не обращать на него внимания', 'You should buy a mirror': 'Тебе стоит купить зеркало', 'Suggest more dildos': 'Предложить ещё фаллоимитаторы', 'Suggest the glory-hole room': 'Предложить комнату с отверстиями в стенах', 'Talk dirty to her': 'Говорить ей пошлости', 'Palm yourself through your jeans': 'Потрогать себя через джинсы', 'Just let her get to it': 'Просто дать ей приступить к делу', 'Enter the booth with Alexis': 'Зайти в кабинку с Алексис', 'Watch from outside the booth': 'Смотреть снаружи кабинки', 'Watch the footage': 'Посмотреть запись', "Don't watch the footage": 'Не смотреть запись', 'Blackmail Dwayne': 'Шантажировать Дуэйна', 'Keep the footage as leverage': 'Сохранить запись как средство давления', 'Wipe the footage out of regret': 'Удалить запись из чувства вины', 'Ask for money': 'Потребовать деньги', 'Ask for a promotion': 'Потребовать повышения', 'We should report': 'Нужно заявить в полицию', "I'm ready": 'Я готов', 'Hide and watch': 'Спрятаться и смотреть', 'Step in': 'Войти', 'Whisper filth to her': 'Шептать ей пошлости', 'Call her dirty': 'Назвать её развратницей', 'Join in yourself': 'Присоединиться', 'Tell her to go and use him': 'Велеть ей пойти и воспользоваться им', 'Watch her claim him on her own terms': 'Смотреть, как она берёт его на своих условиях', 'Let her pick her own fun': 'Пусть сама выберет развлечение', 'Keep her at the table tonight': 'Сегодня оставить её за столиком', "I know you cheat on me and that's okay": 'Я знаю о твоих изменах и не против', "Don't cheat on me again": 'Больше мне не изменяй', 'Apologize and ignore the flirting': 'Извиниться и закрыть глаза на флирт', "I know you cheat and I don't want to see you again": 'Я знаю об изменах и больше не хочу тебя видеть', 'Apologize and ignore the cheating': 'Извиниться и закрыть глаза на измены', 'You should have a termination': 'Тебе стоит сделать аборт', 'I want to raise the child with you': 'Я хочу растить ребёнка вместе с тобой', 'Let her check': 'Дать ей посмотреть', 'Push her, we have an appointment': 'Поторопить её: нас ждут', 'No problem here': 'Никаких проблем', 'In fact, yes': 'Вообще-то да', '[hero.name] should be in the photo too': '[hero.name] тоже должен быть на фото', 'Alexis should wear less clothes': 'Алексис стоит снять часть одежды', 'Point her at someone yourself (you call the shots)': 'Самому выбрать для неё мужчину (решаешь ты)', 'Let her choose her own prey (she calls the shots)': 'Пусть сама выберет добычу (решает она)', 'Whisper filth in her ear': 'Шептать ей на ухо пошлости', 'Stroke yourself while you watch': 'Ласкать себя, наблюдая', 'Just keep watching': 'Просто продолжать смотреть', 'Give her the green light yourself (you call the shots)': 'Самому дать ей разрешение (решаешь ты)', 'Let her set the pace (she calls the shots)': 'Пусть сама задаёт темп (решает она)', 'Keep her to yourself today': 'Сегодня оставить её только для себя', 'Egg her on under your breath': 'Подбадривать её шёпотом', 'Reach into your shorts': 'Запустить руку в шорты', 'Watch in silence': 'Молча смотреть', 'Have her suck you off': 'Попросить у неё минет', 'Give her some oral attention': 'Поласкать её языком', 'Fuck her': 'Трахнуть её', 'Cowgirl': 'Наездница', 'Missionary': 'Миссионерская поза', 'Doggy': 'Раком', 'Reverse Cowgirl': 'Обратная наездница', 'Cum on her face': 'Кончить ей на лицо', 'Cum in her mouth': 'Кончить ей в рот', 'Let her swallow it': 'Дать ей проглотить', 'Have her spit it out': 'Велеть ей сплюнуть', 'Fuck her ass': 'Трахнуть её в задницу', 'Fuck her pussy': 'Трахнуть её в киску', 'Call me Wallet': 'Называй меня кошельком', 'Stop calling me Wallet': 'Не называй меня кошельком', 'Call me Cuck': 'Называй меня рогоносцем', 'Stop calling me Cuck': 'Не называй меня рогоносцем', 'Call me Dark knight': 'Называй меня тёмным рыцарем', 'Stop calling me Dark knight': 'Не называй меня тёмным рыцарем', 'Cancel': 'Отмена'}
    nicknames = {'wallet':'кошелёк','cuck':'рогоносец','dark knight':'тёмный рыцарь','loverboy':'сердцеед',
        'master':'хозяин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'wallet':'wallet','cuck':'cuck','dark knight':'dark_knight'}

    def hero_name():
        value = store.hero.name
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.alexis.flags.mikeNickname
        if speaker == 'alexis' and store.hero.gender == 'male' and chosen:
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
        if filename.startswith('ch/alexis/'):return strings.get(value,value)
        return store.lssb_aletta.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1018 python:
    config.language_callbacks['russian'].append(lssb_alexis.enter)
    for _lssb_alexis_language in set(renpy.known_languages()) | {None}:
        if _lssb_alexis_language != 'russian':
            config.language_callbacks[_lssb_alexis_language].append(lssb_alexis.leave)

screen choice(items):
    variant 'lssb_alexis_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_alexis.caption(i.caption) action i.action
