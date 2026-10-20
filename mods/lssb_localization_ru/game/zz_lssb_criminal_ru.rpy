# Display-only translation; native game variables and branches stay unchanged.
init 1071 python in lssb_criminal:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_criminal_ru'
    strings = {'Agree': 'Согласиться', 'Refuse': 'Отказаться', 'Lie': 'Солгать', 'Tell the truth': 'Сказать правду', "We're waiting Camila": 'Мы ждём Камилу', "Let's grab a drink while we wait for her": 'Давай выпьем, пока ждём её', "Let's seat": 'Давай сядем', "Grab us seats, I'll wait Camila at the bar": 'Займи нам места, а я подожду Камилу у бара', 'Scold Lexi': 'Отругать Лекси', 'Scold Camila': 'Отругать Камилу', 'Scold both': 'Отругать обеих', 'Try a more subtle approach': 'Попробовать более тонкий подход', 'Camila will pay': 'Заплатит Камила', 'Lexi will pay': 'Заплатит Лекси', "I'll pay": 'Я заплачу', "Let's split": 'Давайте разделим счёт', 'Correct Camila': 'Поправить Камилу', 'Correct Lexi': 'Поправить Лекси', 'Correct Camila and Lexi': 'Поправить Камилу и Лекси', "Fun facts about 'Gravlax'": 'Интересные факты о гравлаксе', 'Camila, will you finish your plate?': 'Камила, ты доешь свою порцию?', 'Lexi, will you finish your plate?': 'Лекси, ты доешь свою порцию?', "You won't finish your plates, won't you?": 'Вы ведь не доедите свои порции?', 'Ask for a doggy bag': 'Попросить упаковать еду с собой', '25%%': '25%%', '10%%': '10%%', 'No tip': 'Без чаевых', 'Find a diplomatic solution': 'Найти дипломатическое решение', "I'd like a coffee": 'Я бы хотел кофе', 'Something stronger': 'Что-нибудь покрепче', 'We should leave': 'Нам стоит уйти', "Let's go somewhere else": 'Давайте пойдём куда-нибудь ещё', "Cum in Camila's mouth": 'Кончить Камиле в рот', "Cum in Lexi's mouth": 'Кончить Лекси в рот', 'Cum on their faces': 'Кончить им на лица', 'Fuck Camila': 'Трахнуть Камилу', 'Fuck Lexi': 'Трахнуть Лекси', 'Fuck her pussy': 'Трахнуть её в киску', 'Fuck her ass': 'Трахнуть её в задницу', 'Use protection': 'Использовать защиту', 'Do not use protection': 'Не использовать защиту'}
    aliases = {'Давай пойдём куда-нибудь ещё': 'Давайте пойдём куда-нибудь ещё'}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith(('ch/harems_full/criminal/',)):
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_college.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1072 python:
    config.language_callbacks['russian'].append(lssb_criminal.enter)
    for _lssb_criminal_language in set(renpy.known_languages()) | {None}:
        if _lssb_criminal_language != 'russian':config.language_callbacks[_lssb_criminal_language].append(lssb_criminal.leave)

screen choice(items):
    variant 'lssb_criminal_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_criminal.caption(i.caption) action i.action
