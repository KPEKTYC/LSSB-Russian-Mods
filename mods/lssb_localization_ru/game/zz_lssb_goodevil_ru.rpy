# Display-only translation; native game variables and branches stay unchanged.
init 1077 python in lssb_goodevil:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_goodevil_ru'
    strings = {'Cum on Harmony': 'Кончить на Хармони', 'Cum on Lexi': 'Кончить на Лекси', 'Cum in her mouth': 'Кончить ей в рот', 'Cum on her face': 'Кончить ей на лицо', 'You should have warn us Lexi!': 'Тебе стоило нас предупредить, Лекси!', 'You were not exactly on time either Harmony!': 'Ты тоже пришла не совсем вовремя, Хармони!', 'Scold them both.': 'Отругать обеих', 'Try to ease the tension.': 'Попытаться разрядить обстановку', 'You look stunning Harmony!': 'Ты потрясающе выглядишь, Хармони!', "That's quite any outfit Lexi!": 'Вот это наряд, Лекси!', "You're both incredible!": 'Вы обе невероятны!', 'Huh, you said something?': 'А? Ты что-то сказала?', 'What if we did it in alphabetical order?': 'А если по английскому алфавиту?', 'The eldest pays the first round': 'Старшая оплачивает первую порцию выпивки', "I'll buy the first round": 'Я оплачу первую порцию выпивки', "I'll let this to you two": 'Предоставлю это вам двоим', 'The first one, I think': 'Думаю, первая', 'The second one was great': 'Вторая была великолепна', "I'm not sure": 'Я не уверен', 'Tough choice': 'Сложный выбор', "It shouldn't be harder than a workout session": 'Вряд ли это сложнее тренировки', "It's just dance, should be easy": 'Это всего лишь танец, справлюсь', 'You should both go': 'Вам обеим стоит попробовать', "I'll pass": 'Я пас', 'No way!': 'Ни за что!', 'All right': 'Ладно', 'Fuck Harmony': 'Трахнуть Хармони', 'Fuck Lexi': 'Трахнуть Лекси', 'Fuck her pussy': 'Трахнуть её в киску', 'Fuck her ass': 'Трахнуть её в задницу', 'Cum on both girls': 'Кончить на обеих девушек', 'Go on with Harmony': 'Продолжить с Хармони', 'Go on with Lexi': 'Продолжить с Лекси', 'Fuck pussy': 'Трахнуть в киску', 'Fuck ass': 'Трахнуть в задницу', 'Cum inside her': 'Кончить внутрь неё', 'Pull out': 'Вынуть член', 'The girls seem to have something in mind': 'Кажется, девушки что-то задумали', 'Cum inside ass': 'Кончить в задницу', 'Pull out of ass': 'Вынуть член из её попки', 'Cum in ass': 'Кончить в задницу', 'Cum inside': 'Кончить внутрь', 'Cum on their faces': 'Кончить им на лица'}
    aliases = {'А если идти в алфавитном порядке?': 'А если по английскому алфавиту?', 'Старшая оплачивает первый раунд': 'Старшая оплачивает первую порцию выпивки', 'Я оплачу первый раунд': 'Я оплачу первую порцию выпивки', 'Оставлю это вам двоим': 'Предоставлю это вам двоим', 'Думаю, первый': 'Думаю, первая', 'Второй был отличным': 'Вторая была великолепна', 'Это не должно быть сложнее тренировки': 'Вряд ли это сложнее тренировки', 'Это всего лишь танец, должно быть легко': 'Это всего лишь танец, справлюсь', 'Вам обеим стоит пойти': 'Вам обеим стоит попробовать', 'Я пропущу': 'Я пас', 'Трахнуть киску': 'Трахнуть в киску', 'Вытащить': 'Вынуть член', 'Вытащить из задницы': 'Вынуть член из её попки'}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith(('ch/harems_full/goodevil/',)):
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_gaming.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1078 python:
    config.language_callbacks['russian'].append(lssb_goodevil.enter)
    for _lssb_goodevil_language in set(renpy.known_languages()) | {None}:
        if _lssb_goodevil_language != 'russian':config.language_callbacks[_lssb_goodevil_language].append(lssb_goodevil.leave)

screen choice(items):
    variant 'lssb_goodevil_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_goodevil.caption(i.caption) action i.action
