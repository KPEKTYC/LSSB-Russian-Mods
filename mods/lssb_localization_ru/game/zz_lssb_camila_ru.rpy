# Presentation only. Preserve native names, scene statements and menu actions.
init 1023 python in lssb_camila:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_camila_ru'
    strings = {'No': 'Нет', 'Yes': 'Да', 'Ask Camila on a date': 'Пригласить Камилу на свидание', 'Ask Camila and Kiara for a ride in the limo': 'Пригласить Камилу и Киару прокатиться в лимузине', 'Set up a date with Camila and Lexi': 'Устроить свидание с Камилой и Лекси', 'Agree': 'Согласиться', 'Disagree': 'Не согласиться', 'Of course not': 'Конечно нет', "That's exactly what I was doing": 'Именно это я и делал', 'Be nice': 'Быть милым', 'Scold her': 'Отчитать её', 'Compliment': 'Сделать комплимент', 'Criticize': 'Раскритиковать', 'Defend Camila': 'Защитить Камилу', 'Defend Scottie': 'Защитить Скотти', 'Refuse': 'Отказаться', 'Be amused': 'Посмеяться', 'Get angry': 'Рассердиться', 'Side with Camila': 'Встать на сторону Камилы', 'Side with Laura': 'Встать на сторону Лоры', 'Tackle mugger': 'Повалить грабителя', 'Leap aside': 'Отскочить в сторону', 'Are you okay?': 'Ты в порядке?', 'Ignore Camila': 'Проигнорировать Камилу', 'Reassure Camila': 'Успокоить Камилу', 'Tease Camila': 'Поддразнить Камилу', 'I love It': 'Мне очень нравится', 'Meeeh...': 'Ну такое...', "It's Lexi": 'Это Лекси', "I don't know her": 'Я её не знаю', 'Pass for this time': 'На этот раз воздержаться', 'On it Officer': 'Слушаюсь, офицер', 'Fuck her pussy': 'Трахнуть её в киску', 'Fuck her ass': 'Трахнуть её в задницу', 'Cum inside': 'Кончить внутрь', 'Pull out': 'Вытащить', "Let's keep the baby": 'Давай оставим ребёнка', 'Tell her to abort': 'Сказать ей сделать аборт', 'So be it': 'Пусть будет так', 'Meh...': 'Ну такое...', 'Stools are fine': 'Табуреты вполне подойдут', 'Comfy sits are better': 'Удобные сиденья лучше', 'Order beers': 'Заказать пиво', 'Order wine': 'Заказать вино', "I'll buy": 'Я угощаю', 'I had enough': 'С меня хватит', 'Agree to help Camila undercover': 'Согласиться помочь Камиле под прикрытием', 'Refuse and walk away (You might never meet Camila again)': 'Отказаться и уйти (возможно, вы больше не встретите Камилу)', 'Who are we expecting to be at the meeting?': 'Кого мы ожидаем увидеть на встрече?', 'What is inside the package?': 'Что внутри посылки?', 'Am I being paid for this?': 'Мне за это заплатят?', 'Nah! I got this, easy!': 'Да нет! Я легко справлюсь!', "Keep the contacts in to match Luca's brown eyes": 'Оставить линзы, чтобы глаза были карими, как у Луки', "Remove them, it's a risk but being able to see is more important": 'Снять линзы: рискованно, но видеть важнее', 'I got this!': 'Я справлюсь!', "Yeah on second thought... I think I'm not ready for it yet...": 'Хотя, если подумать... кажется, я ещё не готов...', 'Make up an excuse': 'Придумать оправдание', 'Stay silent': 'Промолчать', 'Blame the long narrative from the game you were playing': 'Сослаться на затянутые диалоги в игре, в которую вы играли', 'Yeah, 2 years. Time flies uh!': 'Да, два года. Время летит, правда?', 'Something like that.': 'Вроде того.', "I haven't been counting.": 'Я не считал.', "3 years and 11 months actually. I'm a courier so time matters to me.": 'Вообще-то три года и одиннадцать месяцев. Я курьер, время для меня важно.', 'Take the cash': 'Взять деньги', "That is blood money, I'm not taking it.": 'Это кровавые деньги. Я их не возьму.', 'Make something up about a cough': 'Придумать что-нибудь про кашель', 'Make something up about a war wound': 'Придумать историю о военном ранении', 'Make something up about a bullet wound': 'Придумать историю о пулевом ранении', 'Be as vague as possible': 'Отвечать как можно более уклончиво', 'Peek inside': 'Заглянуть внутрь', "Don't open it": 'Не открывать', 'Hand the 5K over to her': 'Отдать ей пять тысяч', "She doesn't need to know about it...": 'Ей необязательно об этом знать...', "I'll be there Detective.": 'Я буду, детектив.', "This was...a lot... I don't think I can do it again...": 'Это было... слишком... Не думаю, что смогу повторить...', 'Stay hidden and wait for Camila to rescue me': 'Оставаться в укрытии и ждать помощи Камилы', "Time to use the gun I've got": 'Пора воспользоваться пистолетом', 'Shoot at the closest guard behind the wooden crate': 'Выстрелить в ближайшего охранника за деревянным ящиком', 'Shoot at the furthest guard by the loading door, behind the concrete pillar': 'Выстрелить в дальнего охранника за бетонной колонной у погрузочных ворот', 'Shoot at the security lead taking cover by the metal crates': 'Выстрелить в начальника охраны за металлическими ящиками', 'Shoot at the guard behind the wooden crate': 'Выстрелить в охранника за деревянным ящиком', 'Shoot at the guard by the loading door': 'Выстрелить в охранника у погрузочных ворот', "Not sure that's a good idea": 'Не уверен, что это хорошая идея', 'This could be beneficial for both of us': 'Это может понравиться нам обоим', 'Blowjob': 'Минет', 'Just fuck her': 'Просто трахнуть её', 'Cowgirl': 'Наездница', 'Doggy': 'Раком', 'Stand': 'Стоя', 'Cum in her mouth': 'Кончить ей в рот', 'Cum on her face': 'Кончить ей на лицо', 'Call me Papi Chulo': 'Зови меня «папи чуло»', 'Stop calling me Papi Chulo': 'Не называй меня «папи чуло»', 'Call me Papi': 'Зови меня «папи»', 'Stop calling me Papi': 'Не называй меня «папи»', 'Call me Guapo': 'Зови меня «красавчик»', 'Stop calling me Guapo': 'Не называй меня «красавчик»', 'Call me Hermoso': 'Зови меня «красавец»', 'Stop calling me Hermoso': 'Не называй меня «красавец»', 'Cancel': 'Отмена'}
    nicknames = {'papi chulo':'папи чуло','papi':'папи','guapo':'красавчик','hermoso':'красавец',
        'master':'хозяин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'papi chulo':'papi_chulo','papi':'papi','guapo':'guapo','hermoso':'hermoso'}

    def hero_name():
        value = store.hero.name
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.camila.flags.mikeNickname
        if speaker == 'camila' and store.hero.gender == 'male' and chosen:
            if str(chosen).lower() == str(value).lower():
                return nicknames.get(str(value).lower(),value)
            for key,group in aliases.items():
                if chosen in getattr(store,'nickname_'+group,()) and str(value).lower()==key:
                    return nicknames[key]
        return value

    def action_text(value):
        return {'kissing':'целую','groping':'лапаю'}.get(value,value)

    def target_text(value, case):
        if engine.game.preferences.language != 'russian':return value
        display = {
            'guard crouched behind the wooden crate':
                {'acc':'охранника за деревянным ящиком','nom':'Охранник за деревянным ящиком'},
            'guard by the loading door':
                {'acc':'охранника у погрузочных ворот','nom':'Охранник у погрузочных ворот'},
            'lead taking cover by the metal crates':
                {'acc':'начальника охраны за металлическими ящиками','nom':'Начальник охраны за металлическими ящиками'}}
        return display.get(value,{}).get(case,value)

    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node = engine.game.script.namemap.get(engine.game.context().current)
        filename = getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith('ch/camila/'):return strings.get(value,value)
        return store.lssb_ayesha.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1024 python:
    config.language_callbacks['russian'].append(lssb_camila.enter)
    for _lssb_camila_language in set(renpy.known_languages()) | {None}:
        if _lssb_camila_language != 'russian':
            config.language_callbacks[_lssb_camila_language].append(lssb_camila.leave)

screen choice(items):
    variant 'lssb_camila_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_camila.caption(i.caption) action i.action
