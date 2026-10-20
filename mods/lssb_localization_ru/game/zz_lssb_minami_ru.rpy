# Presentation only. Preserve native names, scene statements and menu actions.
init 1045 python in lssb_minami:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_minami_ru'
    strings = {'Leave': 'Уйти', 'Stay and watch': 'Остаться и посмотреть', 'Masturbate': 'Мастурбировать', 'Keep watching': 'Продолжать смотреть', 'Walk away': 'Отойти', "Check what's going on": 'Проверить, что происходит', 'No': 'Нет', 'Yes': 'Да', 'Be nice': 'Быть ласковым', 'Scold her': 'Отругать её', 'Tease her': 'Подразнить её', 'Ask if any girls have caught her eye': 'Спросить, приглянулась ли ей какая-нибудь девушка', 'Let her win': 'Поддаться', 'Brush her off': 'Отмахнуться от неё', 'Compliment': 'Сделать комплимент', 'Criticize': 'Раскритиковать', 'Flirt shamelessly': 'Беззастенчиво флиртовать', 'Tell off': 'Отчитать', 'Laugh it off': 'Отшутиться', 'Accept': 'Согласиться', 'Refuse': 'Отказаться', 'Agree': 'Согласиться', 'Stop dancing': 'Перестать танцевать', 'Continue': 'Продолжить', 'Agree to play': 'Согласиться сыграть', 'Compliment Minami': 'Сделать Минами комплимент', 'Tell Minami off': 'Отчитать Минами', 'Agree to help': 'Согласиться помочь', 'NO WAY!!': 'НИ ЗА ЧТО!', 'Go in the yard': 'Выйти во двор', 'Send her back': 'Отправить её обратно', 'Let her stay': 'Позволить ей остаться', 'Reject her': 'Отвергнуть её', 'Take responsibility': 'Взять на себя ответственность', 'Support Minami': 'Поддержать Минами', 'Support Sasha': 'Поддержать Сашу', 'Shrug it off': 'Не придать значения', 'Punish Minami': 'Наказать Минами', 'Kiss her': 'Поцеловать её', "Don't kiss her": 'Не целовать её', 'I do': 'Да', 'Not really': 'Не особо', 'I like': 'Мне нравится', "I don't like": 'Мне не нравится', 'Be bad': 'Повести себя плохо', 'Be good': 'Повести себя хорошо', 'Try to ignore the inconvenience': 'Попытаться не обращать внимания на неудобство', "Let Minami know what she's responsible for": 'Дать Минами понять, что она натворила', "I'm not in the mood.": 'Я не в настроении.', 'Come here.': 'Иди сюда.', "There's nothing between me and [bree.name] or Sasha!": 'Между мной и [bree.name] или Сашей ничего нет!', 'I sleep with [bree.name] and Sasha.': 'Я сплю с [bree.name] и Сашей.', "Don't react": 'Не реагировать', "We're here now aren't we?": 'Но мы ведь уже здесь?', 'Seahorses': 'Морские коньки', 'Jellyfish': 'Медузы', 'Listen to her idea': 'Выслушать её идею', 'Suggest an alternative': 'Предложить другой вариант', 'Propose an alternative to the show': 'Предложить кое-что вместо шоу', "It's depressing!": 'Это же депрессивно!', "It's more complex": 'Всё сложнее', 'Buy her plushies': 'Купить ей мягкие игрушки', 'Just leave': 'Просто уйти', 'Propose to use handcuffs': 'Предложить наручники', 'Spank her': 'Отшлёпать её', 'Give her oral': 'Сделать ей кунилингус', 'Let her suck you off': 'Позволить ей сделать минет', 'Fuck her': 'Трахнуть её', 'Reverse cowgirl': 'Обратная наездница', 'Missionary': 'Миссионерская поза', 'Doggy': 'Сзади', 'Fuck her ass': 'Трахнуть её в попку', 'Fuck her pussy': 'Трахнуть её в киску', 'Cum on her face': 'Кончить ей на лицо', 'Cum in her mouth': 'Кончить ей в рот', 'Use my tongue': 'Пустить в ход язык', 'Finger her ass': 'Вставить палец ей в попку', 'Use the dildo': 'Воспользоваться фаллоимитатором', 'Use dildo and my finger.': 'Использовать фаллоимитатор и палец', 'Cum inside': 'Кончить внутрь', 'Pull out': 'Вытащить', 'Call me Onii-chan': 'Называй меня «онии-тян»', 'Stop calling me Onii-chan': 'Больше не называй меня «онии-тян»', 'Call me Nii-san': 'Называй меня «нии-сан»', 'Stop calling me Nii-san': 'Больше не называй меня «нии-сан»', 'Call me Bro-bro': 'Называй меня «братишка»', 'Stop calling me Bro-bro': 'Больше не называй меня «братишка»', 'Call me [[hero.name]': 'Называй меня по имени', 'Stop calling me [[hero.name]': 'Больше не называй меня по имени', 'Cancel': 'Отмена'}
    nicknames = {'onii-chan':'онии-тян','nii-san':'нии-сан','bro-bro':'братишка',
        'master':'господин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'onii-chan':'onii_chan','nii-san':'nii_san','bro-bro':'bro_bro'}

    def hero_name():
        return display_name(store.hero.name)

    def display_name(value):
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.minami.flags.mikeNickname
        if speaker == 'minami' and store.hero.gender == 'male' and chosen:
            if chosen in store.nickname_hero_name and value == '[hero.name]':
                return store.heroname
            if str(chosen).lower() == str(value).lower():
                key = str(value).lower()
                return nicknames[key] if key in nicknames else value
            for key,group in aliases.items():
                if chosen in getattr(store,'nickname_'+group,()) and str(value).lower()==key:
                    return nicknames[key]
        return value

    def action_text(value):
        return {'kissing':'целую','groping':'лапаю'}.get(value,value)

    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node = engine.game.script.namemap.get(engine.game.context().current)
        filename = getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith('ch/minami/'):return strings.get(value,value)
        return store.lssb_lexi.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1046 python:
    config.language_callbacks['russian'].append(lssb_minami.enter)
    for _lssb_minami_language in set(renpy.known_languages()) | {None}:
        if _lssb_minami_language != 'russian':
            config.language_callbacks[_lssb_minami_language].append(lssb_minami.leave)

screen choice(items):
    variant 'lssb_minami_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_minami.caption(i.caption) action i.action
