# Presentation only. Preserve native names, scene statements and menu actions.
init 1047 python in lssb_morgan:
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_morgan_ru'
    strings = {'We had so much fun': 'Нам было так весело', 'I guess we grew out of that': 'Наверное, мы из этого выросли', 'I should have learned more about you': 'Мне стоило лучше тебя узнать', 'You were some rider!': 'Ты здорово гоняла на велосипеде!', 'I ride an exercise bike': 'Я кручу педали на велотренажёре', 'Where would you have gone?': 'Куда бы ты уехала?', 'But you stayed!': 'Но ты осталась!', 'I liked it when you acted all tough': 'Мне нравилось, как ты строила из себя крутую', "You didn't need to pretend": 'Тебе не нужно было притворяться', "And it didn't work": 'И это не сработало', 'You just needed to try harder': 'Нужно было больше стараться', 'You just needed to be yourself': 'Нужно было просто быть собой', "You didn't really know who you were": 'Ты ещё сама не понимала, кто ты', "That's kinda hot, honestly": 'Честно, это довольно горячо', "As long as it's just me now": 'Лишь бы теперь у тебя был только я', 'I like the old you better': 'Раньше ты мне нравилась больше', 'You seem more confident': 'Ты стала увереннее', "I'm no good at this shit either!": 'Я тоже в этой хрени не разбираюсь!', "It's like a second chance": 'Это как второй шанс', 'You can tell me anything': 'Можешь рассказать мне что угодно', 'Geez, I sorta feel the same way too!': 'Блин, я чувствую примерно то же самое!', 'It was simply meant to be!': 'Это просто судьба!', 'He never looked back': 'С тех пор он не оглядывался назад', "He's still following his vision": 'Он по-прежнему верен себе', "He's still a greasy slob": 'Он всё ещё сальный неряха', 'You could have given her one from me': 'Могла бы врезать ей и от меня', 'It was a long time ago': 'Это было давно', "I don't think violence is the answer": 'Не думаю, что насилие — выход', "She hasn't changed much": 'Она почти не изменилась', 'She has a strange vibe': 'Она производит странное впечатление', "Don't worry, I'll protect you": 'Не бойся, я тебя защищу', 'You were a handful too!': 'С тобой тоже было непросто!', "I guess I just didn't really see you": 'Наверное, я просто тебя не замечал', 'I wish I had slowed down!': 'Надо было сбавить темп!', "You weren't just a tomboy!": 'Ты была не просто пацанкой!', 'A little bit of both': 'Всего понемногу', 'Does that make me gay?': 'Значит, я гей?', 'What are the chances': 'Каковы шансы?', "It's like happy ever after!": 'Как в сказке: жили долго и счастливо!', "We'll always be both": 'Мы всегда будем и друзьями, и любовниками', 'I think we were meant to be': 'Думаю, нам суждено быть вместе', 'Friends with benefits': 'Друзья с привилегиями', 'Agree': 'Согласиться', 'Disagree': 'Не согласиться', 'Compliment': 'Сделать комплимент', 'Criticize': 'Раскритиковать', 'Defend Morgan': 'Поддержать Морган', 'Defend Scottie': 'Поддержать Скотти', 'Insist on dancing': 'Настоять на танцах', 'Pass on dancing': 'Отказаться от танцев', 'Calm Morgan down': 'Успокоить Морган', 'Leave the mall': 'Уйти из торгового центра', "It's nothing...": 'Ничего такого...', "Something's up": 'Что-то не так', 'Refuse': 'Отказаться', 'Accept': 'Согласиться', 'Protest': 'Возразить', 'You should be a girl': 'Тебе стоит быть девушкой', 'You should be whatever you want to be': 'Будь кем хочешь', 'I laugh off Morgan being late': 'Отшутиться по поводу опоздания Морган', 'Lets Morgan know im upset at her being late': 'Сказать Морган, что её опоздание меня расстроило', 'Stop Morgan from confronting the family': 'Не дать Морган выяснять отношения с семьёй', 'Stick my foot out in front of the kid': 'Подставить ребёнку подножку', 'Race like a pro': 'Гонять как профессионал', 'Wait for an opening to pass': 'Дождаться возможности для обгона', 'I am a pro on arcade this should not be more complicated': 'Я ас в автоматах, здесь не должно быть сложнее', 'I try hard and try to beat Morgan': 'Постараться обогнать Морган', 'I try hard but decide to let Morgan win': 'Постараться, но поддаться Морган', 'Insist on getting a coffee': 'Настоять на кофе', 'Lets get a beer instead of a coffee': 'Выпить пива вместо кофе', 'Laugh off Morgan being late': 'Отшутиться по поводу опоздания Морган', 'Let Morgan know I am upset at her being late': 'Сказать Морган, что её опоздание меня расстроило', 'Passing a crowd to take it to a famous store': 'Провести её через толпу к известному магазину', 'Take Morgan to a store I saw last time': 'Отвести Морган в магазин, который видел раньше', 'Try something else': 'Попробовать что-нибудь другое', 'Agree to the Maid Cafe': 'Согласиться на кафе с горничными', 'Insist on the Coffee Shop': 'Настоять на обычной кофейне', 'Let Morgan keep me where I am': 'Остаться на месте по просьбе Морган', 'Pull away and do something about the shoplifter': 'Высвободиться и разобраться с магазинным вором', 'Buy Morgan a bunch of flowers': 'Купить Морган букет', 'Buy Morgan a cookie': 'Купить Морган печенье', 'Cum inside': 'Кончить внутрь', 'Pull out': 'Вытащить', 'Have her suck you off': 'Попросить её сделать минет', 'Give her some oral attention': 'Поласкать её языком', 'Fuck her': 'Трахнуть её', 'Standing': 'Стоя', 'Doggy': 'Сзади', 'Cowgirl': 'Наездница', 'Missionary': 'Миссионерская поза', 'Cum in her mouth': 'Кончить ей в рот', "Don't cum in her mouth": 'Не кончать ей в рот', 'Fuck her ass': 'Трахнуть в попку', 'Fuck her pussy': 'Трахнуть в киску', 'Call me Dude': 'Называй меня «чувак»', 'Stop calling me Dude': 'Не называй меня «чувак»', 'Call me Dearest': 'Называй меня «дорогой»', 'Stop calling me Dearest': 'Не называй меня «дорогой»', 'Call me Brah': 'Называй меня «бро»', 'Stop calling me Brah': 'Не называй меня «бро»', 'Cancel': 'Отмена'}
    nicknames = {'dude':'чувак','dearest':'дорогой','brah':'бро',
        'master':'господин','daddy':'папочка','honey':'милый','sweetie':'милый','husband':'муж'}
    aliases = {'dude':'dude','dearest':'dearest','brah':'brah'}

    def hero_name():
        return display_name(store.hero.name)

    def display_name(value):
        who = engine.exports.last_say().who
        speaker = who.name.lower().replace('_name','') if who and hasattr(who,'name') else None
        chosen = store.morgan.flags.mikeNickname
        if speaker == 'morgan' and store.hero.gender == 'male' and chosen:
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
        if filename.startswith('ch/morgan/'):return strings.get(value,value)
        return store.lssb_minami.caption(value)

    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)

    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1048 python:
    config.language_callbacks['russian'].append(lssb_morgan.enter)
    for _lssb_morgan_language in set(renpy.known_languages()) | {None}:
        if _lssb_morgan_language != 'russian':
            config.language_callbacks[_lssb_morgan_language].append(lssb_morgan.leave)

screen choice(items):
    variant 'lssb_morgan_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_morgan.caption(i.caption) action i.action
