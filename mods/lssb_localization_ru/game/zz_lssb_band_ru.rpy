# Display-only translation; native game variables and branches stay unchanged.
init 1065 python in lssb_band:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_band_ru'
    strings = {"Fuck Sasha's pussy": 'Трахнуть Сашу в киску', "Fuck Sasha's ass": 'Трахнуть Сашу в задницу', "Fuck Anna's mouth": 'Трахнуть Анну в рот', "Fuck Anna's pussy": 'Трахнуть Анну в киску', "Fuck Anna's ass": 'Трахнуть Анну в задницу', "Fuck Kleio's pussy": 'Трахнуть Клео в киску', "Fuck Kleio's ass": 'Трахнуть Клео в задницу', "Cum in Sasha's pussy": 'Кончить в киску Саши', "Cum in Sasha's ass": 'Кончить в задницу Саши', "Cum in Anna's mouth": 'Кончить Анне в рот', "Cum in Anna's pussy": 'Кончить Анне в киску', "Cum in Anna's ass": 'Кончить Анне в задницу', "Cum in Kleio's pussy": 'Кончить Клео в киску', "Cum in Kleio's ass": 'Кончить Клео в задницу', "Cum on Anna's face": 'Кончить Анне на лицо', "Show Sasha who's the boss": 'Показать Саше, кто здесь главный', "Fuck Sasha's mouth": 'Трахнуть Сашу в рот', 'Use protection': 'Использовать презерватив', "Don't use protection": 'Не использовать презерватив', "Cum in Sasha's mouth": 'Кончить Саше в рот', "Cum on Sasha's face": 'Кончить Саше на лицо', 'Order fruity cocktails': 'Заказать фруктовые коктейли', 'Order beers': 'Заказать пиво', 'Order spirits': 'Заказать крепкий алкоголь', 'Order tap water': 'Заказать воду из-под крана', 'Reach for a knife and fork': 'Взяться за нож и вилку', 'Reach for chopsticks': 'Взяться за палочки', 'Try to calm both girls down': 'Попытаться успокоить обеих девушек', "Return Anna's attentions": 'Ответить на ласки Анны', "Return Kleio's attentions": 'Ответить на ласки Клео', "Return both girls' attentions": 'Ответить на ласки обеих девушек', 'Offer to pick up the bill': 'Предложить оплатить счёт', 'Claim to have no money': 'Сказать, что денег нет', 'Suggest they split the bill': 'Предложить разделить счёт', "Cum inside Kleio's pussy": 'Кончить Клео в киску', "Cum inside Anna's mouth": 'Кончить Анне в рот', 'Fuck Amy': 'Трахнуть Эми', 'Fuck Anna': 'Трахнуть Анну', 'Fuck Kleio': 'Трахнуть Клео', 'Fuck Sasha': 'Трахнуть Сашу', 'I should try to convince Kleio': 'Стоит попробовать убедить Клео', 'I should try to convince Anna': 'Стоит попробовать убедить Анну', 'I should try to talk to Anna': 'Стоит попробовать поговорить с Анной', 'I should try to talk to Kleio': 'Стоит попробовать поговорить с Клео'}
    aliases = {'Трахнуть Клейо в киску': 'Трахнуть Клео в киску', 'Трахнуть Клейо в задницу': 'Трахнуть Клео в задницу', 'Кончить Клейо в киску': 'Кончить Клео в киску', 'Кончить Клейо в задницу': 'Кончить Клео в задницу', 'Использовать защиту': 'Использовать презерватив', 'Не использовать защиту': 'Не использовать презерватив', 'Кончить в рот Саши': 'Кончить Саше в рот', 'Ответить на внимание Анны': 'Ответить на ласки Анны', 'Ответить на внимание Клейо': 'Ответить на ласки Клео', 'Ответить на внимание обеих девушек': 'Ответить на ласки обеих девушек', 'Предложить им разделить счёт': 'Предложить разделить счёт', 'Кончить внутрь киски Клейо': 'Кончить Клео в киску', 'Трахнуть Клейо': 'Трахнуть Клео', 'Стоит попробовать убедить Клейо': 'Стоит попробовать убедить Клео', 'Стоит попробовать поговорить с Клейо': 'Стоит попробовать поговорить с Клео'}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith(('ch/harems_full/band/',)):
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_events.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1066 python:
    config.language_callbacks['russian'].append(lssb_band.enter)
    for _lssb_band_language in set(renpy.known_languages()) | {None}:
        if _lssb_band_language != 'russian':config.language_callbacks[_lssb_band_language].append(lssb_band.leave)

screen choice(items):
    variant 'lssb_band_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_band.caption(i.caption) action i.action
