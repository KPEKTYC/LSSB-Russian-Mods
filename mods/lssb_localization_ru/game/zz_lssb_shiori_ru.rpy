# Presentation only. Preserve native names, scene statements and menu actions.
init 1055 python in lssb_shiori:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_shiori_ru'
    strings = {'Archives': 'Архивы', 'Aletta': 'Алетта', 'Me': 'Я', "It's inappropriate": 'Это неуместно', 'Thank you': 'Спасибо', 'You too': 'Ты тоже', "I'll search": 'Я поищу', 'Not really': 'Не особо', 'Yes': 'Да', 'You have a good eye for it': 'У тебя хороший вкус', 'Dress for yourself, not the girls': 'Одевайся для себя, а не ради девушек', 'Thanks': 'Спасибо', 'Say nothing': 'Ничего не говорить', 'Not your business': 'Не твоё дело', 'Wow thanks Shiori': 'Ого, спасибо, Сиори', 'Back off': 'Отстань', 'That sounds great': 'Звучит отлично', "You're invading my personal space": 'Ты нарушаешь моё личное пространство', 'No': 'Нет', 'Not for me': 'Не для меня', 'We are not': 'Нет', 'Me too': 'Я тоже', 'You are a nice sextoy': 'Ты хорошая секс-игрушка', 'You are my prized sex slave': 'Ты моя драгоценная секс-рабыня', 'You are a nice person': 'Ты хороший человек', 'You are a burden': 'Ты обуза', 'I would enjoy fucking you again': 'Я бы с удовольствием снова тебя трахнул', 'That would be nice': 'Было бы здорово', 'No thanks': 'Нет, спасибо', 'Offer some meat': 'Предложить мясо', "I'd love to": 'С удовольствием', "I don't think so": 'Не думаю', 'I feel the same way': 'Я чувствую то же самое', 'What are you talking about': 'О чём ты говоришь?', 'I love you too, Shiori': 'Я тоже тебя люблю, Сиори', 'I think you got the wrong end of the stick': 'Кажется, ты неправильно меня поняла', 'Disagree': 'Не согласиться', 'Agree': 'Согласиться', 'Stay at the party': 'Остаться на вечеринке', 'Go trick or treating': 'Пойти собирать сладости', 'Tell scary story': 'Рассказать страшную историю', 'Knock on doors with Kanta': 'Ходить по домам вместе с Кантой', 'Defend Shiori': 'Защитить Сиори', 'Defend Scottie and Jack': 'Защитить Скотти и Джека', 'Ask Shiori to dance': 'Пригласить Сиори на танец', 'Offer Shiori a drink': 'Предложить Сиори выпить', 'Black': 'Чёрный', 'Milky': 'С молоком', 'Refuse': 'Отказаться', 'Accept': 'Согласиться', 'Spank her': 'Отшлёпать её', 'Let it go': 'Оставить это без внимания', 'Tell her to do her job': 'Сказать ей выполнять свою работу', 'Wake her up with kiss': 'Разбудить её поцелуем', 'Wake her up gently': 'Осторожно разбудить её', 'Scold her': 'Отругать её', 'Scold her harshly (this will never happen again)': 'Жёстко отругать её (это больше никогда не повторится)', 'Let her sleep': 'Дать ей поспать', 'Talk to Shiori about your idea.': 'Поговорить с Сиори о своей идее', 'Deal with her later': 'Разобраться с ней позже', 'You should abort': 'Тебе стоит сделать аборт', "That's wonderful": 'Это чудесно', 'Agree with Shiori': 'Согласиться с Сиори', 'Plead to keep the baby': 'Умолять оставить ребёнка', 'Tell her to have an abortion': 'Сказать ей сделать аборт', 'Tell her to keep the baby': 'Сказать ей оставить ребёнка', 'Pay him on the spot (-[shiori.flags.debt]$)': 'Заплатить ему сразу (-[shiori.flags.debt]$)', "I'll think about it": 'Я подумаю', "I'll be back with the money": 'Я вернусь с деньгами', 'Let Shiori call the babysitter': 'Позволить Сиори позвонить няне', 'Do not let Shiori call the babysitter': 'Не позволять Сиори звонить няне', 'Choose Sirens and Serenity': 'Выбрать «Сирены и безмятежность»', 'Choose Space Wars': 'Выбрать «Космические войны»', 'Suggest that you and Shiori share': 'Предложить поделиться с Сиори', 'Buy yourself something and not Shiori': 'Купить что-нибудь себе, но не Сиори', 'Forget about the post-credit scene': 'Забыть о сцене после титров', 'Make Shiori stay for the post-credit scene': 'Заставить Сиори остаться на сцену после титров', 'Cum inside': 'Кончить внутрь', 'Pull out': 'Вытащить', 'Tell her to suck you': 'Сказать ей отсосать', 'Tell her to give you a titty fuck': 'Сказать ей подрочить тебе сиськами', 'Just fuck her': 'Просто трахнуть её', 'Reverse cowgirl': 'Обратная наездница', 'Doggy': 'По-собачьи', 'Missionary': 'Миссионерская', 'Piledriver': 'Пайлдрайвер', 'Cum in her mouth': 'Кончить ей в рот', 'Cum on her face': 'Кончить ей на лицо', 'Hold back': 'Сдержаться', 'Comfort her': 'Утешить её', 'LOL!': 'Рассмеяться!', 'Fuck her ass': 'Трахнуть её в задницу', 'Fuck her pussy': 'Трахнуть её в киску', 'Use the dildo': 'Использовать дилдо', 'No vibrator': 'Без вибратора', 'Get me a coffee.': 'Принеси мне кофе', 'Give me a blowjob': 'Сделай мне минет', 'Fuck her doggystyle': 'Трахнуть её по-собачьи', 'Fuck her missionary style': 'Трахнуть её в миссионерской позе', 'Fuck her reverse cowgirl style': 'Трахнуть её в позе обратной наездницы', "Don't you think you need to be punished": 'Тебе не кажется, что тебя нужно наказать?', 'Forget it': 'Забудь', 'I hate them': 'Я их ненавижу', 'I love them': 'Я их обожаю', 'Ask her to help': 'Попросить её помочь', 'She would only mess it up': 'Она только всё испортит', 'Call me Hero': 'Называй меня героем', 'Stop calling me Hero': 'Перестань называть меня героем', 'Call me Owner': 'Называй меня хозяином', 'Stop calling me Owner': 'Перестань называть меня хозяином', 'Call me Koibito': 'Называй меня «койбито»', 'Stop calling me Koibito': 'Перестань называть меня «койбито»', 'Call me Hanata': 'Называй меня «ханата»', 'Stop calling me Hanata': 'Перестань называть меня «ханата»', 'Call me Mr.Boss sir': 'Называй меня «господин босс»', 'Stop calling me Mr.Boss sir': 'Перестань называть меня «господин босс»', 'Cancel': 'Отмена'}
    nicknames = {'hero':'герой','owner':'хозяин','koibito':'койбито',
        'hanata':'ханата','mr.boss sir':'господин босс','master':'господин',
        'daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'hero':'hero','owner':'owner','koibito':'koibito',
        'hanata':'hanata','mr.boss sir':'mr_boss_sir'}
    def hero_name():
        return display_name(store.hero.name)
    def display_name(value):
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.shiori.flags.mikeNickname
        if speaker == 'shiori' and store.hero.gender == 'male' and chosen:
            if str(chosen).lower() == str(value).lower():
                key = str(value).lower()
                return nicknames[key] if key in nicknames else value
            for key,group in aliases.items():
                if chosen in getattr(store,'nickname_'+group,()) and str(value).lower()==key:
                    return nicknames[key]
        if speaker == 'shiori' and store.hero.gender == 'male' and not chosen:
            for key,condition in store.shiori.heronickname.items():
                if store.safe_eval(condition):
                    if key == 'Sir' and value == 'Sir':return 'сэр'
                    if key == 'Mister hero.family_name' and value == 'Mister '+store.hero.family_name:
                        return 'мистер '+store.hero.family_name
                    break
        return value
    def action_text(value):
        return {'kissing':'целуемся','groping':'ласкаем друг друга'}.get(value,value)
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node = engine.game.script.namemap.get(engine.game.context().current)
        filename = getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith('ch/shiori/'):return strings.get(value,value)
        return store.lssb_samantha.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1056 python:
    config.language_callbacks['russian'].append(lssb_shiori.enter)
    for _lssb_shiori_language in set(renpy.known_languages()) | {None}:
        if _lssb_shiori_language != 'russian':
            config.language_callbacks[_lssb_shiori_language].append(lssb_shiori.leave)

screen choice(items):
    variant 'lssb_shiori_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_shiori.caption(i.caption) action i.action
