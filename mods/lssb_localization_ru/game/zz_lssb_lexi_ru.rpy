# Presentation only. Preserve native names, scene statements and menu actions.
init 1043 python in lssb_lexi:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_lexi_ru'
    strings = {'Ask Lexi on a date': 'Пригласить Лекси на свидание', 'Set up a date with Camila and Lexi': 'Устроить свидание с Камилой и Лекси', 'Set up a date with Harmony and Lexi': 'Устроить свидание с Хармони и Лекси', 'Set up a date with Lexi and Reona': 'Устроить свидание с Лекси и Реоной', 'Leave': 'Уйти', 'Watch Lexi masturbate': 'Посмотреть, как Лекси мастурбирует', 'Masturbate while watching her': 'Мастурбировать, наблюдая за ней', 'Join in': 'Присоединиться', 'Cum on her face': 'Кончить ей на лицо', 'Cum in her mouth': 'Кончить ей в рот', 'Compliment': 'Сделать комплимент', 'Criticize': 'Раскритиковать', 'Indulge Lexi': 'Подыграть Лекси', 'Chastise Lexi': 'Отчитать Лекси', 'Accept': 'Согласиться', 'Refuse': 'Отказаться', 'Sure, why not': 'Конечно, почему бы и нет', "Do it, I won't": 'Делай, я не буду', 'Not in this house': 'Не в этом доме', 'WTF Lexi!': 'Какого хрена, Лекси?!', 'Swallow': 'Проглотить', 'Facial': 'Кончить на лицо', 'Approach her directly.': 'Подойти к ней напрямую', 'Tell someone else.': 'Рассказать кому-нибудь ещё', 'Yes': 'Да', 'No': 'Нет', 'Mess her face up': 'Залить ей лицо', 'Let her do her thing': 'Дать ей продолжить', 'Pull her deeper': 'Насадить её глубже', 'Join her': 'Присоединиться к ней', 'Go back inside': 'Вернуться внутрь', 'Cum inside': 'Кончить внутрь', 'Pull out': 'Вытащить', 'Follow her': 'Пойти за ней', "Don't follow her": 'Не идти за ней', 'Back Off': 'Отступить', 'Stand up to Danny': 'Дать отпор Дэнни', 'Use Brains': 'Применить смекалку', 'Use Brawn': 'Применить силу', 'Call Camila': 'Позвонить Камиле', 'Go alone': 'Пойти одному', "Fuck Sasha's ass": 'Трахнуть Сашу в попку', "Fuck Sasha's pussy": 'Трахнуть Сашу в киску', "Cum in Lexi's mouth": 'Кончить Лекси в рот', "Cum inside of Sasha's ass": 'Кончить Саше в попку', "Cum over Lexi and Sasha's faces": 'Кончить на лица Лекси и Саши', "Cum inside of Sasha's pussy": 'Кончить Саше в киску', 'Tell her to abort': 'Сказать ей сделать аборт', 'Tell her to keep the baby and that you will support her': 'Сказать оставить ребёнка и обещать поддержку', "Tell her you'll pay for it": 'Сказать, что заплатишь', "Don't": 'Не делать этого', 'Not really': 'Не особо', 'No way!': 'Ни за что!', 'Ok': 'Ладно', 'BFF!': 'Лучшие друзья навеки!', 'Asshole...': 'Засранец...', 'Piss off!': 'Отвали!', "I'll send it": 'Я пришлю', 'Consider it': 'Обдумать', "That's a solid no": 'Однозначно нет', 'Just piss off': 'Просто отвали', 'Tell Lexi to give the Master a blow-job': 'Велеть Лекси сделать Мастеру минет', 'Tell the Master to fuck off': 'Послать Мастера нахер', 'Let the Master fuck Lexi': 'Позволить Мастеру трахнуть Лекси', 'Tell the Master to get lost': 'Велеть Мастеру проваливать', 'Of course you can come!': 'Конечно, можешь пойти!', "It's not possible.": 'Это невозможно', 'Do it': 'Сделать это', 'Shut Dwayne down': 'Осадить Дуэйна', "It's not a good idea": 'Плохая идея', 'Agree': 'Согласиться', "It's great": 'Великолепно', "It's fine": 'Нормально', 'As in this movie, "Wetty Prouman"': 'Как в фильме «Мокрая красотка»', 'As in this movie, "The Mall Pig"': 'Как в фильме «Свинья из торгового центра»', "She's damn right!": 'Она чертовски права!', "She's going too far!": 'Она заходит слишком далеко!', 'Sexier and scary': 'Сексуальнее и страшнее', 'Sexier and dangerous': 'Сексуальнее и опаснее', 'Let her suck you': 'Дать ей сделать минет', 'Fuck her': 'Трахнуть её', 'Take charge': 'Взять инициативу', 'Offer drugs': 'Предложить наркотики', 'Reject': 'Отвергнуть', 'Have her suck you off': 'Пусть сделает минет', 'Missionary': 'Миссионерская поза', 'Standing': 'Стоя', 'Cowgirl': 'Наездница', 'Doggy': 'Сзади', 'Let her finish': 'Дать ей закончить', 'Take control': 'Взять контроль', 'Time to let her have it!': 'Пора дать ей то, чего она хочет!', 'Maybe I should pace myself?': 'Может, стоит поберечь силы?', 'Fuck her ass': 'Трахнуть её в попку', 'Fuck her pussy': 'Трахнуть её в киску', 'Choke her': 'Придушить её', 'Pull her hair': 'Потянуть её за волосы', 'Fuck her from front': 'Трахнуть её спереди', 'Fuck her from behind': 'Трахнуть её сзади', 'She sounds like your type': 'Похоже, она в твоём вкусе', 'You only got eyes for me, right?': 'Ты ведь смотришь только на меня?', 'Call me Naughty boy': 'Называй меня «шалун»', 'Stop calling me Naughty boy': 'Не называй меня «шалун»', 'Call me Studmuffin': 'Называй меня «жеребчик»', 'Stop calling me Studmuffin': 'Не называй меня «жеребчик»', 'Cancel': 'Отмена'}
    nicknames = {'naughty boy':'шалун','studmuffin':'жеребчик',
        'master':'господин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'naughty boy':'naughty_boy','studmuffin':'studmuffin'}

    def hero_name():
        return display_name(store.hero.name)

    def upper_name(value):
        native = store.lexi.heroname
        return display_name(native).upper() if value == str(native).upper() else value

    def sasha_name():
        return store.lssb_sasha.nickname(store.sasha.heroname,'sasha',store.sasha.flags.mikeNickname)

    def display_name(value):
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.lexi.flags.mikeNickname
        if speaker == 'lexi' and store.hero.gender == 'male' and chosen:
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
        if filename.startswith('ch/lexi/'):return strings.get(value,value)
        return store.lssb_lavish.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1044 python:
    config.language_callbacks['russian'].append(lssb_lexi.enter)
    for _lssb_lexi_language in set(renpy.known_languages()) | {None}:
        if _lssb_lexi_language != 'russian':
            config.language_callbacks[_lssb_lexi_language].append(lssb_lexi.leave)

screen choice(items):
    variant 'lssb_lexi_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_lexi.caption(i.caption) action i.action
