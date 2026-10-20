# Display-only translation; native game variables and branches stay unchanged.
init 1067 python in lssb_bitchy:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_bitchy_ru'
    strings = {"I'm out of here.": 'Я ухожу', 'Yeah, these girls deserve a spanking.': 'Да, эти девушки заслуживают порки', 'Spank Audrey': 'Шлёпать Одри', 'Spank Palla': 'Шлёпать Паллу', 'Fuck them both': 'Трахнуть их обеих', 'Sure, someday': 'Конечно, когда-нибудь', 'Not interested': 'Не интересует', 'Sure': 'Конечно', "Cum on Cassidy's face": 'Кончить Кэссиди на лицо', "Cum in Cassidy's mouth": 'Кончить Кэссиди в рот', "Cum on Palla's face": 'Кончить Палле на лицо', "Cum in Palla's mouth": 'Кончить Палле в рот', 'Let Cassidy take the lead': 'Передать инициативу Кэссиди', 'Let Palla take the lead': 'Передать инициативу Палле', 'Agree to ask Cassidy': 'Согласиться спросить Кэссиди', 'Refuse to ask Cassidy': 'Отказаться спрашивать Кэссиди', 'Fuck Cassidy': 'Трахнуть Кэссиди', 'Fuck Audrey': 'Трахнуть Одри', 'Fuck Palla': 'Трахнуть Паллу', 'Fuck her ass': 'Трахнуть её в задницу', 'Fuck her pussy': 'Трахнуть её в киску', 'Cum inside': 'Кончить внутрь', 'Pull out': 'Вытащить'}
    aliases = {'Не интересно': 'Не интересует'}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith(('ch/harems_full/bitchy/',)):
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_band.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1068 python:
    config.language_callbacks['russian'].append(lssb_bitchy.enter)
    for _lssb_bitchy_language in set(renpy.known_languages()) | {None}:
        if _lssb_bitchy_language != 'russian':config.language_callbacks[_lssb_bitchy_language].append(lssb_bitchy.leave)

screen choice(items):
    variant 'lssb_bitchy_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_bitchy.caption(i.caption) action i.action
