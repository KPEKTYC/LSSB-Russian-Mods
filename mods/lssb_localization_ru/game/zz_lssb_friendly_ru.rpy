# Display-only translation; native game variables and branches stay unchanged.
init 1097 python in lssb_friendly:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_friendly_ru'
    strings = {'Blowjob': 'Минет', 'Fuck Samantha': 'Трахнуть Саманту', 'Fuck Emma': 'Трахнуть Эмму', 'Fuck her pussy': 'Трахнуть её в киску', 'Fuck her ass': 'Трахнуть её в задницу', 'Cum inside': 'Кончить внутрь', 'Cum outside': 'Кончить снаружи', "Pull out and cum in Emma's mouth": 'Вынуть член и кончить Эмме в рот', 'Pull out': 'Вынуть член'}
    aliases = {'Вытащить и кончить Эмме в рот': 'Вынуть член и кончить Эмме в рот', 'Вытащить': 'Вынуть член'}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems/friendly/events.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_taphophile.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1098 python:
    config.language_callbacks['russian'].append(lssb_friendly.enter)
    for _lssb_friendly_language in set(renpy.known_languages()) | {None}:
        if _lssb_friendly_language != 'russian':config.language_callbacks[_lssb_friendly_language].append(lssb_friendly.leave)

screen choice(items):
    variant 'lssb_friendly_ru'
    style_prefix 'choice'
    $ all_refused = bool(items) and all(choice_refused(i) for i in items)
    $ can_leave = all_refused and SceneExit.possible()
    vbox:
        for i in items:
            $ refuse = (i.kwargs or {}).get("refuse")
            if refuse and not refuse[0].accepts_act(refuse[1]) and (can_leave or not all_refused):
                $ refused_act = SexAct.get(refuse[1])
                textbutton lssb_friendly.caption(i.caption) action (None if refused_act.refused_now(refuse[0]) else Function(refused_act.refuse, refuse[0]))
            else:
                textbutton lssb_friendly.caption(i.caption) action i.action
        if can_leave:
            textbutton _("Stop") action Function(SceneExit.leave)
