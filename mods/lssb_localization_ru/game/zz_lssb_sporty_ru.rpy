# Display-only translation; native game variables and branches stay unchanged.
init 1091 python in lssb_sporty:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_sporty_ru'
    strings = {"Cum in Ayesha's mouth": 'Кончить Айше в рот', "Cum in Hanna's mouth": 'Кончить Ханне в рот', 'Cum on their faces': 'Кончить им на лица', 'Double facial': 'Кончить на лица обеих'}
    aliases = {'Кончить Аише в рот': 'Кончить Айше в рот'}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems_full/sporty/events.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_pixie.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1092 python:
    config.language_callbacks['russian'].append(lssb_sporty.enter)
    for _lssb_sporty_language in set(renpy.known_languages()) | {None}:
        if _lssb_sporty_language != 'russian':config.language_callbacks[_lssb_sporty_language].append(lssb_sporty.leave)

screen choice(items):
    variant 'lssb_sporty_ru'
    style_prefix 'choice'
    $ all_refused = bool(items) and all(choice_refused(i) for i in items)
    $ can_leave = all_refused and SceneExit.possible()
    vbox:
        for i in items:
            $ refuse = (i.kwargs or {}).get("refuse")
            if refuse and not refuse[0].accepts_act(refuse[1]) and (can_leave or not all_refused):
                $ refused_act = SexAct.get(refuse[1])
                textbutton lssb_sporty.caption(i.caption) action (None if refused_act.refused_now(refuse[0]) else Function(refused_act.refuse, refuse[0]))
            else:
                textbutton lssb_sporty.caption(i.caption) action i.action
        if can_leave:
            textbutton _("Stop") action Function(SceneExit.leave)
