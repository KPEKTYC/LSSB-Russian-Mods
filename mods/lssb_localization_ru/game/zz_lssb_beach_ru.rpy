# Display-only translation; original menu values, labels and branches stay intact.
init 1099 python in lssb_beach:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_beach_ru'
    strings = {'Yes': 'Да', 'No': 'Нет', 'Choose to help [bree.name]': 'Помочь: [lssb_beach.bree_name()]', 'Choose to help Sasha': 'Помочь Саше', "Choose [bree.name]'s sandwich": 'Выбрать сэндвич: [lssb_beach.bree_name()]', "Choose Sasha's wrap": 'Выбрать ролл Саши', 'Tackle the crab yourself': 'Самому разобраться с крабом', 'Make [bree.name] tackle the crab': 'Пусть с крабом разберётся [lssb_beach.bree_name()]', "Lick the ice-cream off of [bree.name]'s chest": 'Слизать мороженое с её груди: [lssb_beach.bree_name()]', "Make Sasha lick the ice-cream off of [bree.name]'s chest": 'Пусть Саша слижет мороженое с её груди: [lssb_beach.bree_name()]', 'Choose the sun': 'Выбрать солнце', 'Choose the shade': 'Выбрать тень', 'Use a parasol': 'Использовать пляжный зонт', 'Choose a different spot': 'Выбрать другое место', 'Rub sun cream on [bree.name]': 'Нанести ей солнцезащитный крем: [lssb_beach.bree_name()]', 'Massage Lexi': 'Сделать Лекси массаж', 'I need sun cream too!': 'Мне тоже нужен крем от солнца!', 'Go for a stroll': 'Прогуляться', 'Play volleyball': 'Поиграть в волейбол', 'Get an ice cream': 'Купить мороженое', 'Play in the sea': 'Поплескаться в море', 'Make sandcastles': 'Строить замки из песка', 'Team up with [bree.name]': 'Моя напарница — [lssb_beach.bree_name()]', 'Team up with Lexi': 'Объединиться с Лекси', '[bree.name] and Lexi team together': '[lssb_beach.bree_name()] и Лекси в одной команде', 'Choose [bree.name]': 'Мой выбор — [lssb_beach.bree_name()]', 'Choose Lexi': 'Выбрать Лекси', 'Go to the family beach': 'Пойти на семейный пляж', 'Go to the topless beach': 'Пойти на пляж топлес', 'Go to the nudist beach': 'Пойти на нудистский пляж', 'Take a nap': 'Вздремнуть', 'Choose Minami': 'Выбрать Минами', 'Choose Samantha': 'Выбрать Саманту', 'Me against them': 'Я против них', 'Apply sunscreen on Lexi': 'Намазать Лекси солнцезащитным кремом', 'Apply sunscreen on Minami': 'Намазать Минами солнцезащитным кремом', 'Apply sunscreen on Samantha': 'Намазать Саманту солнцезащитным кремом', 'Apply sunscreen on all of them': 'Намазать всех солнцезащитным кремом', 'I need some cream too': 'Мне тоже нужен крем', 'Choose Sam': 'Выбрать Сэм', 'Cum in her mouth': 'Кончить ей в рот', 'Cum on her face': 'Кончить ей на лицо', 'Fuck her pussy': 'Трахнуть её в киску', 'Fuck her ass': 'Трахнуть её в задницу', 'Cum inside': 'Кончить внутрь', 'Pull out': 'Вынуть член', 'Side with Sasha': 'Поддержать Сашу', 'Side with Samantha': 'Поддержать Саманту', 'Help them': 'Помочь им', 'Let them carry everything': 'Пусть всё несут сами', 'Go grab an ice cream': 'Пойти купить мороженое', 'Stay here and enjoy the time that passes': 'Остаться здесь и отдохнуть', "I'm playing with Sasha": 'Я играю с Сашей', "I'm playing with Samantha": 'Я играю с Самантой', 'Go with Sasha': 'Пойти с Сашей', 'Stay with Samantha': 'Остаться с Самантой', 'Suggest a photo-shoot': 'Предложить фотосессию', 'Take a stroll': 'Прогуляться', 'Choose Sasha': 'Выбрать Сашу'}
    aliases = {'Выбрать помощь [bree.name]': 'Помочь: [lssb_beach.bree_name()]', 'Выбрать помощь Саше': 'Помочь Саше', 'Выбрать сэндвич [bree.name]': 'Выбрать сэндвич: [lssb_beach.bree_name()]', 'Заставить [bree.name] разобраться с крабом': 'Пусть с крабом разберётся [lssb_beach.bree_name()]', 'Слизать мороженое с груди [bree.name]': 'Слизать мороженое с её груди: [lssb_beach.bree_name()]', 'Заставить Сашу слизать мороженое с груди [bree.name]': 'Пусть Саша слижет мороженое с её груди: [lssb_beach.bree_name()]', 'Нанести крем от солнца на [bree.name]': 'Нанести ей солнцезащитный крем: [lssb_beach.bree_name()]', 'Поиграть в море': 'Поплескаться в море', 'Объединиться с [bree.name]': 'Моя напарница — [lssb_beach.bree_name()]', '[bree.name] и Лекси объединяются': '[lssb_beach.bree_name()] и Лекси в одной команде', 'Выбрать [bree.name]': 'Мой выбор — [lssb_beach.bree_name()]', 'Нанести солнцезащитный крем на Лекси': 'Намазать Лекси солнцезащитным кремом', 'Нанести солнцезащитный крем на Минами': 'Намазать Минами солнцезащитным кремом', 'Нанести солнцезащитный крем на Саманту': 'Намазать Саманту солнцезащитным кремом', 'Нанести солнцезащитный крем на всех': 'Намазать всех солнцезащитным кремом', 'Вытащить': 'Вынуть член', 'Остаться здесь и наслаждаться временем': 'Остаться здесь и отдохнуть'}
    names = {'Bree':'Бри','Lexi':'Лекси','Minami':'Минами','Samantha':'Саманта','Sasha':'Саша'}
    prompt = 'Should I set up a date at the beach ?'
    def bree_name(value=None):
        chosen=store.bree.name if value is None else value
        return 'Бри' if chosen in ('Bree','bree') else chosen
    def trip_caption(value, bree_name=None):
        prefix = 'Go to the beach with '
        if not isinstance(value,str) or not value.startswith(prefix):return value
        pair=value[len(prefix):].rsplit(' and ',1)
        if len(pair)!=2:return value
        members=pair[0].split(', ')+[pair[1]]
        if not 2<=len(members)<=5 or len(set(members))!=len(members) or any(n not in names for n in members):return value
        displayed=[]
        for name in members:
            if name=='Bree':
                chosen=store.bree.name if bree_name is None else bree_name
                displayed.append(names[name] if chosen in ('Bree','bree') else chosen)
            else:displayed.append(names[name])
        return 'Поехать на пляж: '+', '.join(displayed[:-1])+' и '+displayed[-1]
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems/home/events/home_harem_beach_date.rpy':
            dynamic=trip_caption(value)
            if dynamic!=value:return dynamic
            if value=='Cancel':return 'Отмена'
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_friendly.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1100 python:
    config.language_callbacks['russian'].append(lssb_beach.enter)
    for _lssb_beach_language in set(renpy.known_languages()) | {None}:
        if _lssb_beach_language != 'russian':config.language_callbacks[_lssb_beach_language].append(lssb_beach.leave)

translate russian strings:
    old 'Should I set up a date at the beach ?'
    new 'Устроить свидание на пляже?'

screen choice(items):
    variant 'lssb_beach_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_beach.caption(i.caption) action i.action
