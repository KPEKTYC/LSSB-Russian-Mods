# Display-only translation; native game variables and branches stay unchanged.
init 1095 python in lssb_taphophile:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_taphophile_ru'
    strings = {'Accept': 'Согласиться', 'Refuse': 'Отказаться'}
    aliases = {}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems_full/taphophile/events.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_taming.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1096 python:
    config.language_callbacks['russian'].append(lssb_taphophile.enter)
    for _lssb_taphophile_language in set(renpy.known_languages()) | {None}:
        if _lssb_taphophile_language != 'russian':config.language_callbacks[_lssb_taphophile_language].append(lssb_taphophile.leave)

screen choice(items):
    variant 'lssb_taphophile_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            $ refuse = (i.kwargs or {}).get("refuse")
            if refuse and not refuse[0].accepts_act(refuse[1]):
                $ refused_act = SexAct.get(refuse[1])
                textbutton lssb_taphophile.caption(i.caption) action (None if refused_act.refused_now(refuse[0]) else Function(refused_act.refuse, refuse[0]))
            else:
                textbutton lssb_taphophile.caption(i.caption) action i.action
