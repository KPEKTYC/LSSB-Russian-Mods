# Display-only translation; native game variables and branches stay unchanged.
init 1093 python in lssb_taming:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_taming_ru'
    strings = {'Let Kylie rage at the waitress': 'Позволить Кайли наорать на официантку', 'Let Ayesha put Kylie in her place': 'Позволить Айше поставить Кайли на место', 'Take control of the situation': 'Взять ситуацию под контроль', 'Go home': 'Пойти домой', 'Go to the night club': 'Пойти в ночной клуб', 'Go to the bar': 'Пойти в бар', 'Go to the dance floor': 'Пойти на танцпол', 'Dance with Ayesha': 'Танцевать с Айшей', 'Dance with Kylie': 'Танцевать с Кайли', 'Stay longer': 'Остаться подольше', 'Call it a night': 'Закончить вечер', 'Ask for a blowjob': 'Попросить минет', 'Just fuck them': 'Просто трахнуть их', 'Fuck Ayesha': 'Трахнуть Айшу', 'Fuck Kylie': 'Трахнуть Кайли', 'Fuck Kylie too': 'Трахнуть и Кайли', "I'm too tired": 'Я слишком устал', 'Deny her tonight': 'Сегодня ей отказать', 'Fuck Ayesha too': 'Трахнуть и Айшу', 'Fuck her ass': 'Трахнуть её в задницу', 'Fuck her pussy': 'Трахнуть её в киску', 'Use the rope': 'Использовать верёвку', 'Cum inside': 'Кончить внутрь', 'Pull out': 'Вынуть член', 'Use protection': 'Использовать защиту', "Don't use protection": 'Не использовать защиту', 'Explain yourself': 'Объясниться', "Kylie's crazy": 'Кайли ненормальная', 'Ayesha needs to cool down': 'Айше нужно успокоиться', 'Shut up! Both of you': 'Заткнитесь! Обе', 'Shut Kylie up': 'Заткнуть Кайли', "Ayesha, it's just a joke": 'Айша, это просто шутка', 'A whale for Ayesha and a shark for Kylie': 'Кит для Айши и акула для Кайли', 'A mermaid for Ayesha and a mermaid for Kylie': 'Русалка для Айши и русалка для Кайли', 'A mermaid for Ayesha and a shark for Kylie': 'Русалка для Айши и акула для Кайли', 'A mermaid for Kylie and a whale for Ayesha': 'Русалка для Кайли и кит для Айши', 'Order something for everyone': 'Заказать что-нибудь для всех', 'Order seafood': 'Заказать морепродукты', 'Order steak': 'Заказать стейк', 'Deal with it': 'Разобраться с ситуацией', 'Blame Kylie': 'Обвинить Кайли', 'Blame Ayesha': 'Обвинить Айшу', 'Pick up the bill': 'Оплатить счёт', 'Split the bill': 'Разделить счёт', 'Let Ayesha pick up the tab': 'Позволить Айше оплатить счёт', 'Let Kylie pick up the tab': 'Позволить Кайли оплатить счёт', 'Ayesha! Shut up!': 'Айша! Заткнись!', 'Kylie! Shut up!': 'Кайли! Заткнись!', 'Show them a real stone skim': 'Показать, как пускают блинчики', 'Play peacemaker': 'Попытаться всех примирить', "Praise Ayesha's performance": 'Похвалить бросок Айши', 'Sympathise with Kylie': 'Посочувствовать Кайли', 'Make a wish': 'Загадать желание', "Don't make a wish": 'Не загадывать желание', "Ayesha, I'm disappointed": 'Айша, я разочарован', "Kylie, I'm disappointed": 'Кайли, я разочарован', 'Use blindfold': 'Использовать повязку на глаза', 'Do not use blindfold': 'Не использовать повязку на глаза', 'Let Ayesha use Kylie': 'Позволить Айше использовать Кайли', "Ayesha fucks Kylie's pussy": 'Айша трахает киску Кайли', "Ayesha fucks Kylie's ass": 'Айша трахает Кайли в задницу', 'Ayesha stays inside': 'Айша остаётся внутри', 'Ayesha pulls out': 'Айша вынимает страпон', "Pull out of Kylie's ass": 'Вынуть член из попки Кайли'}
    aliases = {'Позволить Айеше поставить Кайли на место': 'Позволить Айше поставить Кайли на место', 'Танцевать с Айешей': 'Танцевать с Айшей', 'Трахнуть Айешу': 'Трахнуть Айшу', 'Трахнуть и Айешу': 'Трахнуть и Айшу', 'Вытащить': 'Вынуть член', 'Айеше нужно остыть': 'Айше нужно успокоиться', 'Айеша, это просто шутка': 'Айша, это просто шутка', 'Кит для Айеши и акула для Кайли': 'Кит для Айши и акула для Кайли', 'Русалка для Айеши и русалка для Кайли': 'Русалка для Айши и русалка для Кайли', 'Русалка для Айеши и акула для Кайли': 'Русалка для Айши и акула для Кайли', 'Русалка для Кайли и кит для Айеши': 'Русалка для Кайли и кит для Айши', 'Смириться': 'Разобраться с ситуацией', 'Обвинить Айешу': 'Обвинить Айшу', 'Позволить Айеше оплатить счёт': 'Позволить Айше оплатить счёт', 'Айеша! Заткнись!': 'Айша! Заткнись!', 'Показать им настоящий бросок камня по воде': 'Показать, как пускают блинчики', 'Похвалить выступление Айеши': 'Похвалить бросок Айши', 'Айеша, я разочарован': 'Айша, я разочарован', 'Позволить Айеше использовать Кайли': 'Позволить Айше использовать Кайли', 'Айеша трахает киску Кайли': 'Айша трахает киску Кайли', 'Айеша трахает Кайли в задницу': 'Айша трахает Кайли в задницу', 'Айеша остаётся внутри': 'Айша остаётся внутри', 'Айеша вытаскивает': 'Айша вынимает страпон', 'Вытащить из задницы Кайли': 'Вынуть член из попки Кайли'}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems_full/taming/events.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_sporty.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1094 python:
    config.language_callbacks['russian'].append(lssb_taming.enter)
    for _lssb_taming_language in set(renpy.known_languages()) | {None}:
        if _lssb_taming_language != 'russian':config.language_callbacks[_lssb_taming_language].append(lssb_taming.leave)

screen choice(items):
    variant 'lssb_taming_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_taming.caption(i.caption) action i.action
