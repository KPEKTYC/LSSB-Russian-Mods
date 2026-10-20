# Display-only translation; native game variables and branches stay unchanged.
init 1103 python in lssb_homepair:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_homepair_ru'
    strings = {'Choose [bree.name]': 'Мой выбор — [lssb_homepair.bree_name()]', 'Choose the band': 'Выбрать группу', 'Yes': 'Да', 'No': 'Нет', 'Sasha eat [bree.name] out': '[lssb_homepair.bree_name()]: кунилингус от Саши', 'Sasha use a strap-on on [bree.name]': '[lssb_homepair.bree_name()]: секс со страпоном Саши', "Fuck Sasha's pussy": 'Трахнуть Сашу в киску', "Fuck Sasha's ass": 'Трахнуть Сашу в задницу', "Finger [bree.name]'s pussy": '[lssb_homepair.bree_name()]: поласкать киску пальцами', "Finger [bree.name]'s ass": '[lssb_homepair.bree_name()]: поласкать анус пальцами', "Use dildo on [bree.name]'s pussy": '[lssb_homepair.bree_name()]: ввести фаллоимитатор в киску', "Use dildo on [bree.name]'s ass": '[lssb_homepair.bree_name()]: ввести фаллоимитатор в задницу', 'Spank Sasha': 'Отшлёпать Сашу', 'Spank [bree.name]': '[lssb_homepair.bree_name()]: отшлёпать', 'Spank [bree.name] and Sasha': '[lssb_homepair.bree_name()] и Саша: отшлёпать обеих', 'Cum inside': 'Кончить внутрь', "Cum on Sasha's ass": 'Кончить Саше на попку', "Cum on [bree.name]'s ass": '[lssb_homepair.bree_name()]: кончить на попку', 'Remove their leashes': 'Отстегнуть поводки', 'Take them out for a walk': 'Вывести их на прогулку', 'Allow [bree.name] to speak': 'Пусть говорит [lssb_homepair.bree_name()]', 'Allow Sasha to speak': 'Разрешить Саше говорить', 'Take the girls out for their evening walk.': 'Вывести девушек на вечернюю прогулку.', 'Just watch some TV with the girls before bed.': 'Просто посмотреть с девушками телевизор перед сном.', 'Take them out in the garden.': 'Вывести их в сад.', 'Take them to the park.': 'Отвести их в парк.', 'Reach for Sasha': 'Потянуться к Саше', 'Keep it to the music': 'Ограничиться музыкой', 'Cum in pussy': 'Кончить в киску', 'Pull out of pussy': 'Вынуть член из киски', 'No really, no': 'Нет, серьёзно, нет', 'So be it': 'Будь что будет'}
    aliases = {'Выбрать [bree.name]': 'Мой выбор — [lssb_homepair.bree_name()]', 'Саша вылизывает [bree.name]': '[lssb_homepair.bree_name()]: кунилингус от Саши', 'Саша использует страпон на [bree.name]': '[lssb_homepair.bree_name()]: секс со страпоном Саши', 'Ласкать киску [bree.name] пальцами': '[lssb_homepair.bree_name()]: поласкать киску пальцами', 'Ласкать задницу [bree.name] пальцами': '[lssb_homepair.bree_name()]: поласкать анус пальцами', 'Использовать дилдо в киске [bree.name]': '[lssb_homepair.bree_name()]: ввести фаллоимитатор в киску', 'Использовать дилдо в заднице [bree.name]': '[lssb_homepair.bree_name()]: ввести фаллоимитатор в задницу', 'Шлёпать Сашу': 'Отшлёпать Сашу', 'Шлёпать [bree.name]': '[lssb_homepair.bree_name()]: отшлёпать', 'Шлёпать [bree.name] и Сашу': '[lssb_homepair.bree_name()] и Саша: отшлёпать обеих', 'Кончить на задницу Саши': 'Кончить Саше на попку', 'Кончить на задницу [bree.name]': '[lssb_homepair.bree_name()]: кончить на попку', 'Снять с них поводки': 'Отстегнуть поводки', 'Разрешить [bree.name] говорить': 'Пусть говорит [lssb_homepair.bree_name()]', 'Вывести их в сад': 'Вывести их в сад.', 'Отвести их в парк': 'Отвести их в парк.', 'Вытащить из киски': 'Вынуть член из киски', 'Нет, правда, нет': 'Нет, серьёзно, нет', 'Пусть будет так': 'Будь что будет'}
    def bree_name():
        return store.lssb_beach.bree_name()
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems/home/events/home_harem_bree_sasha.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_homefive.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1104 python:
    config.language_callbacks['russian'].append(lssb_homepair.enter)
    for _lssb_homepair_language in set(renpy.known_languages()) | {None}:
        if _lssb_homepair_language != 'russian':config.language_callbacks[_lssb_homepair_language].append(lssb_homepair.leave)

screen choice(items):
    variant 'lssb_homepair_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_homepair.caption(i.caption) action i.action
