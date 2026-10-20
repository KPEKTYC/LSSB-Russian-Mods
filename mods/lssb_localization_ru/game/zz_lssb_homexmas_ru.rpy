# Display-only translation; native game variables and branches stay unchanged.
init 1115 python in lssb_homexmas:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_homexmas_ru'
    strings = {'Offer style clothes': 'Подарить стильную одежду', 'Offer gym clothes': 'Подарить спортивную одежду', 'Offer ear-plugs': 'Подарить беруши', 'Offer an amp': 'Подарить усилитель', 'Offer warm clothes': 'Подарить тёплую одежду', 'Offer light clothes': 'Подарить лёгкую одежду', 'Offer white panties': 'Подарить белые трусики', 'Offer blue panties': 'Подарить синие трусы', 'Offer an old picture of you': 'Подарить вашу старую фотографию', 'Offer a new picture of you': 'Подарить вашу новую фотографию'}
    aliases = {'Предложить стильную одежду': 'Подарить стильную одежду', 'Предложить спортивную одежду': 'Подарить спортивную одежду', 'Предложить беруши': 'Подарить беруши', 'Предложить усилитель': 'Подарить усилитель', 'Предложить тёплую одежду': 'Подарить тёплую одежду', 'Предложить лёгкую одежду': 'Подарить лёгкую одежду', 'Предложить белые трусики': 'Подарить белые трусики', 'Предложить синие трусики': 'Подарить синие трусы', 'Предложить старую фотографию себя': 'Подарить вашу старую фотографию', 'Предложить новую фотографию себя': 'Подарить вашу новую фотографию'}
    def bree_name():
        return store.lssb_beach.bree_name()
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems/home/events/home_harem_xmas_party.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_homesam.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1116 python:
    config.language_callbacks['russian'].append(lssb_homexmas.enter)
    for _lssb_homexmas_language in set(renpy.known_languages()) | {None}:
        if _lssb_homexmas_language != 'russian':config.language_callbacks[_lssb_homexmas_language].append(lssb_homexmas.leave)

screen choice(items):
    variant 'lssb_homexmas_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_homexmas.caption(i.caption) action i.action
