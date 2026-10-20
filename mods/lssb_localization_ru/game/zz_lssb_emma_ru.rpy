# Presentation only. Preserve native names, scene statements and menu actions.
init 1029 python in lssb_emma:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_emma_ru'
    strings = {'I insist': 'Я настаиваю', 'Okay. Next time?': 'Ладно. В следующий раз?', 'Ask Emma on a date': 'Пригласить Эмму на свидание', 'Ask Emma and Samantha on a date': 'Пригласить Эмму и Саманту на свидание', 'Meet Anna, Emma and Kat at the beach': 'Встретиться с Анной, Эммой и Кэт на пляже', 'I will': 'Обещаю', "I'm not really interested": 'Мне не очень интересно', "It's okay, I'm here for you": 'Всё хорошо, я рядом', "Then let's talk about something else": 'Тогда поговорим о другом', "Yes, it's weird": 'Да, это странно', "No, it's adorable": 'Нет, это мило', 'Pizza': 'Пицца', 'Burgers': 'Бургеры', 'Pasta': 'Паста', "It's cute, tell me more": 'Это мило, расскажи ещё', "That's a little weird": 'Это немного странно', 'Compliment': 'Похвалить', 'Criticise': 'Раскритиковать', 'Defend Emma': 'Защитить Эмму', 'Defend Sasha': 'Защитить Сашу', 'Dance': 'Танцевать', 'Do not dance': 'Не танцевать', "She's not real, it's just a dream (Never meet Emma again)": 'Она ненастоящая, это просто сон (больше не встречать Эмму)', "She's real. I have to find her": 'Она настоящая. Нужно её найти', 'Yes': 'Да', "No it's fine!": 'Нет, всё нормально!', 'Not interested (Never meet Emma again)': 'Неинтересно (больше не встречать Эмму)', 'Sure': 'Конечно', 'Aw, why not?': 'Ну почему?', 'A friend date, then': 'Тогда дружеское свидание', 'Yeah': 'Ага', 'No': 'Нет', 'I know he is': 'Я знаю, что он ей изменяет', 'I think he is': 'Думаю, он ей изменяет', "I don't think so": 'Не думаю', "I can't!": 'Не могу!', 'Okay': 'Ладно', 'Ryan, Sam and I have an arrangement': 'У нас с Райаном и Сэм есть договорённость', 'Yeah, she is': 'Да, она ему изменяет', 'Not interested': 'Неинтересно', 'Sure!': 'Конечно!', 'Telephone': 'Телефон', 'Speaker': 'Динамик', 'Game console': 'Игровая приставка', 'Computer': 'Компьютер', 'Television': 'Телевизор', 'Sim card': 'Сим-карта', 'Lamp': 'Фонарь', 'Bench': 'Скамейка', 'Cobblestone': 'Булыжник', 'Tree': 'Дерево', 'Office window': 'Окно офиса', 'Dildo': 'Фаллоимитатор', 'Vibrator': 'Вибратор', 'Rope': 'Верёвка', 'Whip': 'Плеть', 'Lingerie': 'Нижнее бельё', 'Collar': 'Ошейник', 'Butt plug': 'Анальная пробка', "I don't believe in fate": 'Я не верю в судьбу', "I don't believe in coincidence": 'Я не верю в совпадения', 'Admit it': 'Признаться', 'Lie and say no': 'Соврать и сказать «нет»', 'Relent': 'Уступить', "It's better this way": 'Так будет лучше', 'We should explore it': 'Нам стоит попробовать', 'Nothing': 'Ничего', 'Of course': 'Конечно', "I don't, really": 'Вообще-то, нет', 'No!': 'Нет!', 'I want to explore with Emma': 'Я хочу попробовать с Эммой', "I'm disgusted by the kiss": 'Поцелуй мне отвратителен', "I don't like the kiss, but I don't show it": 'Поцелуй не нравится, но я этого не показываю', 'I like the kiss': 'Поцелуй мне нравится', 'I feel the same way': 'Я чувствую то же самое', 'I like you, but not in the same way': 'Ты мне нравишься, но не в этом смысле', "You're right, it's unique.": 'Ты права, это нечто особенное', "Yeah, I guess it's different...": 'Да, наверное, это другое...', 'Tell Emma to keep it': 'Сказать Эмме оставить ребёнка', 'Tell Emma to get rid of it': 'Сказать Эмме прервать беременность', 'Sounds awesome!': 'Звучит здорово!', "I'd rather do something else": 'Я бы лучше занялся другим', 'Do I have to?': 'Обязательно?', "I'm just kidding, I didn't mean to upset you": 'Я просто шучу, не хотел тебя расстроить', "I'm not as into anime as you are": 'Я не так увлекаюсь аниме, как ты', "I guess we don't": 'Наверное, нет', 'Do you want to have some sexy time?': 'Хочешь немного пошалить?', "We're out of Benji episodes, what next?": 'Серии про Бэндзи закончились. Что дальше?', '[[LIE] No': '[[ЛОЖЬ] Нет', "Oh no, I've waited forever for this...": 'Ну уж нет, я так долго этого ждал...', 'As you wish, my Princess!': 'Как пожелаете, моя принцесса!', "I can't": 'Не могу', 'Hand job': 'Ласки рукой', 'Lick': 'Поласкать языком', 'Suggest a BJ': 'Предложить минет', 'Insist on sex': 'Настоять на сексе', 'Swallow': 'В рот', 'Facial': 'На лицо', 'Go ahead': 'Продолжить', 'Suggest something else': 'Предложить что-нибудь другое', 'Fuck her ass': 'Трахнуть в попку', 'Fuck her pussy': 'Трахнуть в киску', 'Propose handjob': 'Предложить ласки рукой', 'Propose blowjob': 'Предложить минет', 'Offer cunnilingus': 'Предложить куннилингус', 'Skip foreplay': 'Пропустить прелюдию', 'Missionary': 'Миссионерская поза', 'Cowgirl': 'Наездница', 'Reverse Cowgirl': 'Обратная наездница', 'Doggy': 'Сзади', 'Call me Honey': 'Называй меня милым', 'Stop calling me Honey': 'Не называй меня милым', 'Call me Dreamboat': 'Называй меня мужчиной мечты', 'Stop calling me Dreamboat': 'Не называй меня мужчиной мечты', 'Call me Senpai': 'Называй меня сэмпаем', 'Stop calling me Senpai': 'Не называй меня сэмпаем', 'Call me My Prince': 'Называй меня своим принцем', 'Stop calling me My Prince': 'Не называй меня своим принцем', 'Call me My King': 'Называй меня своим королём', 'Stop calling me My King': 'Не называй меня своим королём', 'Cancel': 'Отмена'}
    nicknames = {'dreamboat':'мужчина мечты','senpai':'сэмпай','my prince':'мой принц','my king':'мой король',
        'master':'господин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'honey':'honey','dreamboat':'dreamboat','senpai':'senpai','my prince':'my_prince','my king':'my_king'}

    def hero_name(bare=False):
        value = store.hero.name
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.emma.flags.mikeNickname
        def display(key):
            result = nicknames[key]
            return result[4:] if bare and result in ('мой принц','мой король') else result
        if speaker == 'emma' and store.hero.gender == 'male' and chosen:
            if str(chosen).lower() == str(value).lower():
                key = str(value).lower()
                return display(key) if key in nicknames else value
            for key,group in aliases.items():
                if chosen in getattr(store,'nickname_'+group,()) and str(value).lower()==key:
                    return display(key)
        if speaker == 'emma' and store.hero.gender == 'male' and not chosen:
            if str(value).lower() == 'my king' and store.emma.is_sex_slave:
                return display('my king')
            if str(value).lower() == 'my prince' and store.emma.sub >= 50 and not store.emma.is_sex_slave:
                return display('my prince')
        return value

    def action_text(value):
        return {'kissing':'целую','groping':'лапаю'}.get(value,value)

    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node = engine.game.script.namemap.get(engine.game.context().current)
        filename = getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith('ch/emma/'):return strings.get(value,value)
        return store.lssb_cherie.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1030 python:
    config.language_callbacks['russian'].append(lssb_emma.enter)
    for _lssb_emma_language in set(renpy.known_languages()) | {None}:
        if _lssb_emma_language != 'russian':
            config.language_callbacks[_lssb_emma_language].append(lssb_emma.leave)

screen choice(items):
    variant 'lssb_emma_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_emma.caption(i.caption) action i.action
