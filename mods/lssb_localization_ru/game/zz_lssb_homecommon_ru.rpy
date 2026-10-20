# Display-only translation; native game variables and branches stay unchanged.
init 1105 python in lssb_homecommon:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_homecommon_ru'
    strings = {'Leave quietly': 'Тихо уйти', 'Stay and watch': 'Остаться и посмотреть', 'Masturbate': 'Помастурбировать', 'Just watch': 'Просто смотреть', 'Yes': 'Да', 'No': 'Нет', 'I want some time with Sasha and [bree.name]': 'Пусть со мной побудут Саша и [lssb_homecommon.bree_name()]', 'I want some time with [bree.name] and Minami': 'Пусть со мной побудут [lssb_homecommon.bree_name()] и Минами', 'I want some time with [bree.name] and Sasha': 'Пусть со мной побудут [lssb_homecommon.bree_name()] и Саша', 'I want to be alone with [bree.name]': 'Пусть со мной побудет только [lssb_homecommon.bree_name()]', 'I want some time with Sasha and Minami': 'Хочу побыть с Сашей и Минами', 'I want to be alone with Sasha': 'Хочу побыть наедине с Сашей', 'I want some time with Minami and Sasha': 'Хочу побыть с Минами и Сашей', 'I want some time with Minami and [bree.name]': 'Пусть со мной побудут Минами и [lssb_homecommon.bree_name()]', 'I want to be alone with Minami': 'Хочу побыть наедине с Минами'}
    aliases = {'Остаться и смотреть': 'Остаться и посмотреть', 'Мастурбировать': 'Помастурбировать', 'Я хочу побыть с Сашей и [bree.name]': 'Пусть со мной побудут Саша и [lssb_homecommon.bree_name()]', 'Я хочу побыть с [bree.name] и Минами': 'Пусть со мной побудут [lssb_homecommon.bree_name()] и Минами', 'Я хочу побыть с [bree.name] и Сашей': 'Пусть со мной побудут [lssb_homecommon.bree_name()] и Саша', 'Я хочу остаться наедине с [bree.name]': 'Пусть со мной побудет только [lssb_homecommon.bree_name()]', 'Я хочу побыть с Сашей и Минами': 'Хочу побыть с Сашей и Минами', 'Я хочу остаться наедине с Сашей': 'Хочу побыть наедине с Сашей', 'Я хочу побыть с Минами и Сашей': 'Хочу побыть с Минами и Сашей', 'Я хочу побыть с Минами и [bree.name]': 'Пусть со мной побудут Минами и [lssb_homecommon.bree_name()]', 'Я хочу остаться наедине с Минами': 'Хочу побыть наедине с Минами'}
    def bree_name():
        return store.lssb_beach.bree_name()
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename=='ch/harems/home/events/home_harem_common.rpy':
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_homepair.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1106 python:
    config.language_callbacks['russian'].append(lssb_homecommon.enter)
    for _lssb_homecommon_language in set(renpy.known_languages()) | {None}:
        if _lssb_homecommon_language != 'russian':config.language_callbacks[_lssb_homecommon_language].append(lssb_homecommon.leave)

screen choice(items):
    variant 'lssb_homecommon_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_homecommon.caption(i.caption) action i.action
