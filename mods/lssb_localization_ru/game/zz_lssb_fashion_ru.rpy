# Display-only translation; native game variables and branches stay unchanged.
init 1073 python in lssb_fashion:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_fashion_ru'
    strings = {'Better not interfere': 'Лучше не вмешиваться', 'Praise Sasha when she gets home': 'Похвалить Сашу, когда она вернётся домой', 'Head down to the mall': 'Отправиться в торговый центр', 'Ignore the voices': 'Проигнорировать голоса', 'Investigate the voices': 'Проверить, откуда голоса', 'Keep quiet and watch': 'Молчать и наблюдать', 'Get involved': 'Вмешаться', 'Swallow': 'Кончить ей в рот', 'Facial': 'Кончить на лицо'}
    aliases = {'Спуститься в торговый центр': 'Отправиться в торговый центр', 'Проглотить': 'Кончить ей в рот'}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith(('ch/harems_full/fashion/',)):
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_criminal.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1074 python:
    config.language_callbacks['russian'].append(lssb_fashion.enter)
    for _lssb_fashion_language in set(renpy.known_languages()) | {None}:
        if _lssb_fashion_language != 'russian':config.language_callbacks[_lssb_fashion_language].append(lssb_fashion.leave)

screen choice(items):
    variant 'lssb_fashion_ru'
    style_prefix 'choice'
    $ all_refused = bool(items) and all(choice_refused(i) for i in items)
    $ can_leave = all_refused and SceneExit.possible()
    vbox:
        for i in items:
            $ refuse = (i.kwargs or {}).get("refuse")
            if refuse and not refuse[0].accepts_act(refuse[1]) and (can_leave or not all_refused):
                $ refused_act = SexAct.get(refuse[1])
                textbutton lssb_fashion.caption(i.caption) action (None if refused_act.refused_now(refuse[0]) else Function(refused_act.refuse, refuse[0]))
            else:
                textbutton lssb_fashion.caption(i.caption) action i.action
        if can_leave:
            textbutton _("Stop") action Function(SceneExit.leave)
