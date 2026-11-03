# Shared by the visual and localization archives; identical compiled payload.
init 970 python in lssb_compat:
    import renpy as engine
    import store, types, inspect, hashlib, ast, textwrap
    from store import renpy as api, config
    _constant = True
    disabled = {}
    native_hashes = {}
    expected = {'actions': '4db6b4a0a8791fc1e44094e0fb869215ca590ffaf035fd3a0dd8259f9fcc98d7', 'appearance': '1767600bd6c670bd50e9ab74c7566b2b06432a29acd9de9ca48260f2140600d3', 'cheats_attr_change': '6870c2497b1d08f7988fd4e28729428e98f2dc792614724eccb82c97596e9e48', 'choice': '6b678f85f8e83c32e505ef325bf4d6f6e7d9f7fdf3c974559471417fec74c94c', 'choose_gift': '9f522c786d34967f07d03f3df01c45cd4f4743ab99d48fc6c9a92aa385240f3e', 'contact_name_line': 'a16b27076f1f7419ffad7bf909ee5866e001c2bf733a7d128e72c422bac7e4df', 'file_slots': '38bc08f2cfb1aae9b0b72ffe8547da88cc901c219e86b017f41b06ba5489b52f', 'get_birthday_screen': 'e1f264fc927036532b25041523d0511dafce3ea68702a89dfffc5af87670db9c', 'get_start_date_screen': '79424a77e4731582c7f0c97fcdf20093e5762c506b06a545c3ac1d523966bad0', 'help': '59930efaed3d2c46b250abdaaede03a05cd87fa62dd7ef5913d6a8c33ab7f3eb', 'housemap': 'baf51fe886854bd661625a3d0939609126c159c26c2385a34303d1faee87c098', 'inventory': '8bb235f3e0e82859048497c929af78b8e2fb6b7badf12051a7c1c0886128dce5', 'mallmap': '4b20e715ae22b50b3119c0e076f9caac78d758e3fe9f3cfc7a670899682e79da', 'map': '646f2b31aeae0c533c092d575008d4d377bd88a8be49d2b85965712aa7a0dddd', 'notification_popup': 'c2fecf54c32c738c5aba7ceae2f64ed962e5e181ff511fa18fbaed97cf560ae5', 'npc_info': '6f6e8804a1d320eff8dd7212e1fc89745a565c007d345e58ed234fa41240ea33', 'old_ui_helper': '65beb96cd806acc6fe75be17277bd788006e46daf9720abb93891d7036a588af', 'overlay_ui': 'd44375422d75573025c824a99487596fc598e12a2ff8443b2eca3f78c9fe77ab', 'preferences': 'b4454199cfd1e58051b29ea0be9f01e5dae8681c668710032e877c738a09e25b', 'shopping': 'd6659b88eb4bd4f972200519500cc345eb05f514ad7a7c7a17a2a6482e9d4e14', 'smartphone': '92f2726c151d0488fdbb2572cf923b239a9d159b9919762b0a78aa6137c978c7', 'story_tracker': 'c876f39175d53606645f058575d934550b0bd50173dd7ed42907b7a6b5871086', 'tooltip': 'c462cafb5c4050627d19fea54f8bdc7092ee98936d01e132ce05c76fde809182', 'tooltip_old_ui': '4607fc48aec1e66e491b6a2031346a34e45ede39bcfc68bedc96beff42dc8245', 'nvl_phonetext': '12777b1c72b88368e7b6c4e95e6b9d5c4a14c8ac59001536469cf47c8503ac36', 'select': 'acb8ba40891b1e584d417406cf49e42caaf6295c2477e4ee1836e929dbe48cce'}
    _module = types.ModuleType('lssb_screen_contracts')
    exec(compile('"""Version-independent structural contracts for Ren\'Py screen trees.\n\nCapture before screen preparation. Ignore source coordinates and compilation\ncaches, never actions, conditions, defaults, parameters or screen-use arguments.\nUnknown types fail closed. No game expressions are evaluated by this module.\n"""\nimport hashlib\nimport json\nimport types\n\nIGNORED = frozenset((\'location\', \'serial\', \'analysis\', \'prepared\', \'ast\',\n                     \'bytecode\', \'hash\', \'docstring\', \'linenumber\', \'filename\'))\n\ndef normalize(value):\n    if value is None or isinstance(value, (str, int, float, bool)):\n        return value\n    if isinstance(value, (tuple, list)):\n        return [normalize(x) for x in value]\n    if isinstance(value, dict):\n        return {str(k): normalize(v) for k,v in sorted(value.items(), key=lambda p:str(p[0]))}\n    if isinstance(value, (set, frozenset)):\n        return sorted([normalize(x) for x in value], key=repr)\n    if isinstance(value, (types.FunctionType, types.BuiltinFunctionType, type)):\n        return [\'callable\', value.__module__, value.__qualname__]\n    cls = type(value)\n    if cls.__name__ == \'PyCode\':\n        return [\'PyCode\', value.source, value.mode]\n    if cls.__module__.startswith((\'renpy.sl2.\', \'renpy.parameter\', \'renpy.ast\', \'renpy.atl\')):\n        fields = vars(value) if hasattr(value, \'__dict__\') else {k:getattr(value,k) for k in cls.__slots__}\n        return [cls.__module__, cls.__name__, {k: normalize(v) for k,v in sorted(fields.items()) if k not in IGNORED}]\n    raise TypeError(\'Unsupported contract node: \'+cls.__module__+\'.\'+cls.__name__)\n\ndef fingerprint(value):\n    return hashlib.sha256(json.dumps(normalize(value),ensure_ascii=True,sort_keys=True).encode()).hexdigest()\n', 'lssb_screen_contracts', 'exec'), _module.__dict__)

    def resolve(path):
        value = store if path.startswith('store.') else engine
        for part in path.split('.')[1:]:
            value = getattr(value, part, None)
            if value is None:
                break
        return value

    def require(name, paths=(), lists=(), dimensions=False):
        missing = [p for p in paths if resolve(p) is None]
        missing.extend(p for p in lists if not hasattr(resolve(p), 'append'))
        if dimensions and (config.screen_width, config.screen_height) != (1280,720):
            missing.append('virtual resolution')
        if missing:
            disabled[name] = ', '.join(missing)
            return False
        return True

    def method_matches(value, expected_hash):
        try:
            source = ast.dump(ast.parse(textwrap.dedent(inspect.getsource(value))), include_attributes=False)
            return hashlib.sha256(source.encode()).hexdigest() == expected_hash
        except Exception:
            return False

    def messages():
        names = {'map':'Карта города','housemap':'Карта дома','mallmap':'Карта ТЦ',
            'smartphone':'Телефон','story_tracker':'Сюжетное меню','appearance':'Внешность',
            'inventory':'Инвентарь','choose_gift':'Подарки','npc_info':'Карточка персонажа',
            'preferences':'Настройки','tooltip':'Подсказки','tooltip_old_ui':'Подсказки старого интерфейса',
            'actions':'Активности','overlay_ui':'Панель интерфейса','choice':'Варианты ответа','nvl_phonetext':'Переписка','select':'Выбор в магазине'}
        return [names.get(name, name) + ': используется штатный вариант (' + reason + ').' for name,reason in sorted(disabled.items())]

    # A hash covers screen structure, predicates, actions and parameters; it
    # excludes line numbers, file paths and compiler caches. It is NOT a game
    # version hash. A changed screen falls back independently of other screens.
    for name in expected:
        native = engine.display.screen.screens.get((name, None))
        try:
            native_hashes[name] = _module.fingerprint(native.function) if native else None
        except Exception:
            native_hashes[name] = None
    for key in list(engine.display.screen.screens):
        name, variant = key
        if isinstance(variant, str) and variant.startswith('lssb_') and name in expected:
            if native_hashes[name] != expected[name] or (config.screen_width,config.screen_height)!=(1280,720):
                del engine.display.screen.screens[key]
                disabled[name] = 'экран игры изменён'

    for name, reason in disabled.items():
        api.log('LSSB compatibility: native fallback for '+name+': '+reason)
