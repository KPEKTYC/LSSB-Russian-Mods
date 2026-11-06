# Display-only translation; native game variables and branches stay unchanged.
init 1069 python in lssb_college:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_college_ru'
    strings = {'Barge into the room': 'Ворваться в комнату', 'Knock on the door': 'Постучать в дверь', 'Listen at the door': 'Подслушать у двери', 'I have a bad feeling about this': 'У меня плохое предчувствие', 'Go easy on me': 'Поосторожнее со мной', "I'm ready": 'Я готов', "Let them 'relax' you first": 'Сначала позволить им «расслабить» тебя', 'Get straight to the main experiment': 'Сразу перейти к главному эксперименту'}
    aliases = {'Будьте со мной полегче': 'Поосторожнее со мной'}
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith(('ch/harems_full/college/',)):
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_bitchy.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1070 python:
    config.language_callbacks['russian'].append(lssb_college.enter)
    for _lssb_college_language in set(renpy.known_languages()) | {None}:
        if _lssb_college_language != 'russian':config.language_callbacks[_lssb_college_language].append(lssb_college.leave)

screen choice(items):
    variant 'lssb_college_ru'
    style_prefix 'choice'
    $ all_refused = bool(items) and all(choice_refused(i) for i in items)
    $ can_leave = all_refused and SceneExit.possible()
    vbox:
        for i in items:
            $ refuse = (i.kwargs or {}).get("refuse")
            if refuse and not refuse[0].accepts_act(refuse[1]) and (can_leave or not all_refused):
                $ refused_act = SexAct.get(refuse[1])
                textbutton lssb_college.caption(i.caption) action (None if refused_act.refused_now(refuse[0]) else Function(refused_act.refuse, refuse[0]))
            else:
                textbutton lssb_college.caption(i.caption) action i.action
        if can_leave:
            textbutton _("Stop") action Function(SceneExit.leave)
