# Presentation only. Preserve native names, scene statements and menu actions.
init 1033 python in lssb_harmony:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_harmony_ru'
    strings = {'Ask Harmony on a date': 'Пригласить Хармони на свидание', 'Set up a date with Harmony and Lexi': 'Договориться о свидании с Хармони и Лекси', 'I liked it': 'Мне понравилось', 'I hated it': 'Мне не понравилось', 'Me too': 'Мне тоже', 'I am not that interested': 'Меня это не особо интересует', 'I like you too': 'Ты мне тоже нравишься', 'You should work on your small talk': 'Тебе стоит поработать над умением вести беседу', 'I agree': 'Я согласен', 'I disagree': 'Я не согласен', 'I feel the same': 'Я чувствую то же самое', "I don't feel the same": 'Я не чувствую того же', 'What about your friends at church': 'А как же твои друзья из церкви?', 'Keep your eyes on me': 'Смотри на меня', 'Flirt': 'Флиртовать', 'Blow her off': 'Отшить её', 'Not me': 'Не я', 'I am touched': 'Я тронут', 'I am irritated': 'Меня это раздражает', "It's your own fault": 'Ты сама виновата', 'You are a slut': 'Ты шлюха', 'I love it too': 'Мне тоже нравится', 'I believe in god': 'Я верю в Бога', "I don't know": 'Не знаю', "I don't believe in god": 'Я не верю в Бога', 'Agree': 'Согласиться', 'Disagree': 'Не согласиться', 'I would like that': 'Я был бы рад', 'No': 'Нет', 'That would be nice': 'Было бы здорово', 'Tell her she should not eat that much': 'Сказать, что ей не стоит столько есть', "Tell her she's too fat": 'Сказать, что она слишком толстая', '[hero.name] tells Harmony that he does not feel the same way': '[hero.name] говорит Хармони, что не испытывает того же', 'Be disgusted': 'Выразить отвращение', 'Good idea': 'Хорошая идея', "I'd love to": 'С удовольствием', 'Compliment': 'Сделать комплимент', 'Criticize': 'Раскритиковать', 'Play along': 'Подыграть', 'Protest': 'Возразить', 'Accept': 'Согласиться', 'Refuse': 'Отказаться', 'Agree that the verses have illuminated your own sins': 'Согласиться, что стихи открыли тебе глаза на собственные грехи', 'Question the verses': 'Усомниться в этих стихах', 'Find a deeper spiritual meaning in the story': 'Найти в истории более глубокий духовный смысл', 'Find fault with the moral of the story': 'Найти изъян в морали истории', 'Tell Harmony you understand the moral of the story': 'Сказать Хармони, что ты понял мораль истории', 'Offer Harmony an alternate moral to the story': 'Предложить Хармони другую мораль этой истории', 'Follow her lead': 'Следовать её примеру', 'Make it lewd': 'Добавить непристойности', 'Go to a Bridal boutique': 'Пойти в свадебный салон', 'Go to a lingerie store': 'Пойти в магазин белья', "Agree to meet Harmony's family": 'Согласиться познакомиться с семьёй Хармони', "Refuse to meet Harmony's family": 'Отказаться знакомиться с семьёй Хармони', 'Keep things respectful': 'Держаться уважительно', 'Flirt a little with Diane': 'Немного пофлиртовать с Дайан', 'Play it straight down the line': 'Вести себя прямо и серьёзно', 'Play it cool': 'Держаться непринуждённо', 'Let Harmony meet Angela': 'Позволить Хармони познакомиться с Анджелой', "Don't let Harmony meet Angela": 'Не знакомить Хармони с Анджелой', 'Fuck Harmony one last time': 'Трахнуть Хармони в последний раз', 'Kiss Harmony one last time': 'Поцеловать Хармони в последний раз', 'No way': 'Ни за что', 'Ok': 'Ладно', 'Keep things clean and wholesome': 'Соблюдать приличия', 'Pull Harmony close for the dance': 'Притянуть Хармони ближе во время танца', 'Pull back from the accidental kiss': 'Отстраниться от случайного поцелуя', 'Lean into the accidental kiss': 'Ответить на случайный поцелуй', 'We should keep it': 'Нам стоит оставить ребёнка', 'You should have a termination': 'Тебе стоит прервать беременность', "That's a great idea!": 'Отличная идея!', "I'm not sure...": 'Я не уверен...', "Tell her she's in time": 'Сказать, что она вовремя', "Tell her she's a little late": 'Сказать, что она немного опоздала', 'Help Harmony into her seat': 'Помочь Хармони сесть', 'Sit straight down in your seat': 'Сразу сесть самому', 'Compliment her outfit': 'Похвалить её наряд', "Tell her she's late": 'Сказать, что она опоздала', 'Buy everything she wants': 'Купить всё, что она хочет', 'Tell her to moderate herself': 'Попросить её быть умереннее', 'Finely balanced, as all things should be': 'Идеальный баланс, как и должно быть', "Wow there! You can't be serious about this one!": 'Ого! Ты же не серьёзно насчёт этого?', 'Ask for a titjob': 'Попросить поласкать грудью', 'Give her a cunnilingus': 'Поласкать её языком', 'Ask for a blowjob': 'Попросить минет', "Don't ask for anything": 'Ничего не просить', 'Missionary': 'Миссионерская поза', 'Doggy': 'Сзади', 'Use my tongue': 'Ласкать языком', 'Use the vibrator': 'Использовать вибратор', 'Finger her ass': 'Ввести палец ей в попку', 'Use the vibrator and my finger': 'Использовать вибратор и палец', 'Use the anal beads': 'Использовать анальные шарики', 'Fuck her ass': 'Трахнуть в попку', 'Fuck her pussy': 'Трахнуть в киску', 'Yes': 'Да', 'Cum inside': 'Кончить внутрь', 'Pull out': 'Вынуть', 'Call me My friend': 'Называй меня «мой друг»', 'Stop calling me My friend': 'Не называй меня «мой друг»', 'Call me Stallion': 'Называй меня жеребцом', 'Stop calling me Stallion': 'Не называй меня жеребцом', 'Call me Demon': 'Называй меня демоном', 'Stop calling me Demon': 'Не называй меня демоном', 'Call me My angel': 'Называй меня «мой ангел»', 'Stop calling me My angel': 'Не называй меня «мой ангел»', 'Cancel': 'Отмена'}
    nicknames = {'my friend':'мой друг','stallion':'жеребец','demon':'демон','my angel':'мой ангел',
        'master':'господин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'my friend':'my_friend','stallion':'stallion','demon':'demon','my angel':'my_angel'}

    def hero_name():
        value = store.hero.name
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.harmony.flags.mikeNickname
        if speaker == 'harmony' and store.hero.gender == 'male' and chosen:
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
        if filename.startswith('ch/harmony/'):return strings.get(value,value)
        return store.lssb_hanna.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1034 python:
    config.language_callbacks['russian'].append(lssb_harmony.enter)
    for _lssb_harmony_language in set(renpy.known_languages()) | {None}:
        if _lssb_harmony_language != 'russian':
            config.language_callbacks[_lssb_harmony_language].append(lssb_harmony.leave)

screen choice(items):
    variant 'lssb_harmony_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_harmony.caption(i.caption) action i.action
