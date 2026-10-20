# Presentation-only fixes for native dynamic dialogue statements.
init 1169 python in lssb_textfragments:
    import renpy as engine
    import store
    import re
    _constant = True
    corrections = [{'girl': '_bg', 'identifier': 'generic_get_out_19d7fc07', 'id': 'generic_get_out_19d7fc07:0', 'source': '[verb] naked...', 'original_code': '"[verb] naked..."', 'before': '[verb] без одежды...', 'before_code': '"[verb] без одежды..."', 'who': None, 'target': '[lssb_textfragments.subject(verb)] без одежды...'}, {'girl': '_bg', 'identifier': 'generic_get_out_7bb7e497', 'id': 'generic_get_out_7bb7e497:0', 'source': '[verb] in [third_person] undies...', 'original_code': '"[verb] in [third_person] undies..."', 'before': '[verb] в нижнем белье [third_person]...', 'before_code': '"[verb] в нижнем белье [third_person]..."', 'who': None, 'target': '[lssb_textfragments.subject(verb)] в [lssb_textfragments.possessive(third_person)] нижнем белье...'}, {'girl': '_bg', 'identifier': 'generic_get_out_ae349af3', 'id': 'generic_get_out_ae349af3:0', 'source': '[verb] only wearing [towel]...', 'original_code': '"[verb] only wearing [towel]..."', 'before': '[verb], прикрывшись лишь [towel]...', 'before_code': '"[verb], прикрывшись лишь [towel]..."', 'who': None, 'target': '[lssb_textfragments.subject(verb)], прикрывшись лишь [lssb_textfragments.towel(towel)]...'}, {'girl': '_bg', 'identifier': 'generic_get_out_d998d858', 'id': 'generic_get_out_d998d858:0', 'source': '[verb] in various states of undress...', 'original_code': '"[verb] in various states of undress..."', 'before': '[verb] в разной степени раздетости...', 'before_code': '"[verb] в разной степени раздетости..."', 'who': None, 'target': '[lssb_textfragments.subject(verb)] в разной степени раздетости...'}, {'girl': '_ac', 'identifier': 'ask_birthday_914b3cf4', 'id': 'ask_birthday_914b3cf4:0', 'source': "It's on the [active_girl.birthday[1]] of [active_girl.birthday[0]].", 'original_code': 'active_girl.say "It\'s on the [active_girl.birthday[1]] of [active_girl.birthday[0]]."', 'before': 'Мой день рождения — [active_girl.birthday[1]] [active_girl.birthday[0]].', 'before_code': 'active_girl.say "Мой день рождения — [active_girl.birthday[1]] [active_girl.birthday[0]]."', 'who': 'active_girl.say', 'target': 'Мой день рождения — [active_girl.birthday[1]] [lssb_textfragments.season(active_girl.birthday[0])].'}, {'identifier': 'study_classroom_d9aaad99', 'file': 'bg/classroom/classroom.rpy', 'line': 60, 'source': '[s]', 'original_code': '"[s]"', 'before': '[s]', 'before_code': '"[s]"', 'who': None, 'target': '[lssb_textfragments.phrase(s)]'}, {'identifier': 'nightclub_party_d9aaad99', 'file': 'bg/nightclub/nightclub.rpy', 'line': 53, 'source': '[s]', 'original_code': '"[s]"', 'before': '[s]', 'before_code': '"[s]"', 'who': None, 'target': '[lssb_textfragments.phrase(s)]'}, {'identifier': 'smartphone_send_friendly_text_92c30ed9', 'file': 'ac/smartphone.rpy', 'line': 30, 'source': "[girl.subject_pronoun.capitalize()] doesn't answer...", 'original_code': '"[girl.subject_pronoun.capitalize()] doesn\'t answer..."', 'before': '[girl.subject_pronoun.capitalize()] не отвечает...', 'before_code': '"[girl.subject_pronoun.capitalize()] не отвечает..."', 'who': None, 'target': '[lssb_textfragments.pronoun(girl.subject_pronoun).capitalize()] не отвечает...'}, {'identifier': 'smartphone_send_flirty_text_92c30ed9', 'file': 'ac/smartphone.rpy', 'line': 71, 'source': "[girl.subject_pronoun.capitalize()] doesn't answer...", 'original_code': '"[girl.subject_pronoun.capitalize()] doesn\'t answer..."', 'before': '[girl.subject_pronoun.capitalize()] не отвечает...', 'before_code': '"[girl.subject_pronoun.capitalize()] не отвечает..."', 'who': None, 'target': '[lssb_textfragments.pronoun(girl.subject_pronoun).capitalize()] не отвечает...'}, {'identifier': 'smartphone_call_11c39609', 'file': 'ac/smartphone.rpy', 'line': 180, 'source': "[girl.subject_pronoun.capitalize()] doesn't pick up.", 'original_code': '"[girl.subject_pronoun.capitalize()] doesn\'t pick up."', 'before': '[girl.subject_pronoun.capitalize()] не берёт трубку.', 'before_code': '"[girl.subject_pronoun.capitalize()] не берёт трубку."', 'who': None, 'target': '[lssb_textfragments.pronoun(girl.subject_pronoun).capitalize()] не берёт трубку.'}, {'identifier': 'audrey_cheated_d917439e', 'file': 'ch/audrey/base.rpy', 'line': 58, 'source': 'I see Audrey looking at me [action] someone else with envy and lust in her eyes.', 'original_code': '"I see Audrey looking at me [action] someone else with envy and lust in her eyes."', 'before': 'Одри с завистью и похотью в глазах смотрит, как я [action] другую.', 'before_code': '"Одри с завистью и похотью в глазах смотрит, как я [action] другую."', 'who': None, 'target': 'Одри с завистью и похотью в глазах смотрит, как я [lssb_textfragments.action(action)] другую.'}, {'identifier': 'give_a_gift_ab412b1c', 'file': 'ac/gift.rpy', 'line': 70, 'source': "I don't think it's something I should give [active_girl.personal_pronoun]... At least not right now...", 'original_code': '"I don\'t think it\'s something I should give [active_girl.personal_pronoun]... At least not right now..."', 'before': 'Не думаю, что мне стоит дарить это [active_girl.personal_pronoun]... По крайней мере, пока...', 'before_code': '"Не думаю, что мне стоит дарить это [active_girl.personal_pronoun]... По крайней мере, пока..."', 'who': None, 'target': 'Не думаю, что мне стоит дарить это [lssb_textfragments.dative(active_girl.personal_pronoun)]... По крайней мере, пока...'}, {'identifier': 'generic_get_out_dialogues_2_male_eceeeb6e', 'file': 'bg/bathroom/bathroom.rpy', 'line': 258, 'source': "Sorry [name], I didn't know you would be in here.", 'original_code': 'mike.say "Sorry [name], I didn\'t know you would be in here."', 'before': 'Прости, [name], я не знал, что ты здесь.', 'before_code': 'mike.say "Прости, [name], я не знал, что ты здесь."', 'who': 'mike.say', 'target': '[lssb_textfragments.bath_apology(name)]'}, {'identifier': 'morgan_kleio_event_01_b81938ae', 'file': 'ch/harems_full/pixie/events.rpy', 'line': 411, 'source': "I was talking about one of my oldest friend's ex, and some girl that had dumped my [kleio.status].", 'original_code': 'mike.say "I was talking about one of my oldest friend\'s ex, and some girl that had dumped my [kleio.status]."', 'before': 'Моя [kleio.status] рассказала, что её бросила какая-то девушка, а давняя подруга — о своей бывшей. Вот о ком я говорил.', 'before_code': 'mike.say "Моя [kleio.status] рассказала, что её бросила какая-то девушка, а давняя подруга — о своей бывшей. Вот о ком я говорил."', 'who': 'mike.say', 'target': 'Я говорил о бывшей одной из моих давних подруг и о девушке, которая бросила мою [lssb_textfragments.status_acc(kleio.status)].'}, {'identifier': 'caught_peeping_dialogues_1_male_b0e0b6be', 'file': 'bg/secondfloor/secondfloor.rpy', 'line': 684, 'source': 'H...hey, [caught_girl]!', 'original_code': 'mike.say "H...hey, [caught_girl]!"', 'before': 'П... привет, [caught_girl]!', 'before_code': 'mike.say "П... привет, [caught_girl]!"', 'who': 'mike.say', 'target': 'П... привет, [caught_girl.name]!'}, {'identifier': 'date_buy_a_round_3e55ad0e', 'file': 'da/date_pub.rpy', 'line': 371, 'source': "But [active_girl] doesn't seem to want to drink, so I refrain from doing so.", 'original_code': '"But [active_girl] doesn\'t seem to want to drink, so I refrain from doing so."', 'before': 'Но [active_girl], похоже, не хочет пить, так что я воздерживаюсь.', 'before_code': '"Но [active_girl], похоже, не хочет пить, так что я воздерживаюсь."', 'who': None, 'target': 'Но [active_girl.name], похоже, не хочет пить, так что я воздерживаюсь.'}, {'identifier': 'movie_reactions_21f99641', 'file': 'ac/watch.rpy', 'line': 307, 'source': '[who] seem to enjoy themselves very much.', 'original_code': '"[who] seem to enjoy themselves very much."', 'before': 'Похоже, [who] получают огромное удовольствие.', 'before_code': '"Похоже, [who] получают огромное удовольствие."', 'who': None, 'target': 'Похоже, [lssb_textfragments.names(who,liked)] получают огромное удовольствие.'}, {'identifier': 'movie_reactions_4c3cc48b', 'file': 'ac/watch.rpy', 'line': 319, 'source': '[who] seem not to be paying too much attention to the movie.', 'original_code': '"[who] seem not to be paying too much attention to the movie."', 'before': 'Похоже, [who] почти не обращают внимания на фильм.', 'before_code': '"Похоже, [who] почти не обращают внимания на фильм."', 'who': None, 'target': 'Похоже, [lssb_textfragments.names(who,indifferent)] почти не обращают внимания на фильм.'}, {'identifier': 'movie_reactions_57c8224c', 'file': 'ac/watch.rpy', 'line': 301, 'source': '[who] seem mesmerized.', 'original_code': '"[who] seem mesmerized."', 'before': '[who], похоже, не могут оторвать взгляд.', 'before_code': '"[who], похоже, не могут оторвать взгляд."', 'who': None, 'target': '[lssb_textfragments.names(who,liked)], похоже, не могут оторвать взгляд.'}, {'identifier': 'movie_reactions_74020c9e', 'file': 'ac/watch.rpy', 'line': 335, 'source': '[who] seem completely bored.', 'original_code': '"[who] seem completely bored."', 'before': 'Похоже, [who] ужасно скучают.', 'before_code': '"Похоже, [who] ужасно скучают."', 'who': None, 'target': 'Похоже, [lssb_textfragments.names(who,disliked)] ужасно скучают.'}, {'identifier': 'movie_reactions_a7425c7f', 'file': 'ac/watch.rpy', 'line': 309, 'source': '[who] seem to enjoy themselves.', 'original_code': '"[who] seem to enjoy themselves."', 'before': 'Похоже, [who] получают удовольствие.', 'before_code': '"Похоже, [who] получают удовольствие."', 'who': None, 'target': 'Похоже, [lssb_textfragments.names(who,liked)] получают удовольствие.'}, {'identifier': 'movie_reactions_b5fd3a1b', 'file': 'ac/watch.rpy', 'line': 333, 'source': '[who] seem to be more scared than entertained.', 'original_code': '"[who] seem to be more scared than entertained."', 'before': 'Похоже, [who] скорее напуганы, чем развлекаются.', 'before_code': '"Похоже, [who] скорее напуганы, чем развлекаются."', 'who': None, 'target': 'Похоже, [lssb_textfragments.names(who,disliked)] скорее напуганы, чем развлекаются.'}, {'identifier': 'movie_reactions_d07d83bb', 'file': 'ac/watch.rpy', 'line': 305, 'source': '[who] seem to be quite excited by the sight.', 'original_code': '"[who] seem to be quite excited by the sight."', 'before': 'Похоже, [who] приходят в сильное возбуждение от увиденного.', 'before_code': '"Похоже, [who] приходят в сильное возбуждение от увиденного."', 'who': None, 'target': 'Похоже, [lssb_textfragments.names(who,liked)] приходят в сильное возбуждение от увиденного.'}, {'identifier': 'movie_reactions_e5bdc813', 'file': 'ac/watch.rpy', 'line': 303, 'source': '[who] seem beaming.', 'original_code': '"[who] seem beaming."', 'before': '[who] прямо сияют.', 'before_code': '"[who] прямо сияют."', 'who': None, 'target': '[lssb_textfragments.names(who,liked)] прямо сияют.'}]
    applied = []
    skipped = []
    strings = {'Ask to join you': 'Позвать сюда', 'Convince the employee': 'Уговорить сотрудника', 'Try to sneak in': 'Попробовать пробраться незаметно', 'Bribe the employee': 'Подкупить сотрудника', 'High School Reunion (Alexis)': 'Встреча выпускников (Алексис)', 'Wrestling show (Ayesha)': 'Шоу рестлинга (Айеша)', 'Meet with Ayesha': 'Встреча с Айешой', 'Harder training with Ayesha': 'Усиленная тренировка с Айешой', 'Date (Camila & Lexi)': 'Свидание: Камила и Лекси', "Dwayne's Mansion Party": 'Вечеринка в особняке Дуэйна', 'Meet with Sam and Emma': 'Встреча с Сэм и Эммой', 'Scavenger hunt (Emma)': 'Квест (Эмма)', 'Date at restaurant (Hanna)': 'Свидание в ресторане (Ханна)', 'Home Christmas Party': 'Рождественская вечеринка дома', 'Meet Anna and Kleio': 'Встреча с Анной и Клео', 'Threesome (Audrey,Sasha)': 'Секс втроём: Одри и Саша', 'Office Christmas Party': 'Рождественская вечеринка в офисе', 'Date (Harmony & Lexi)': 'Свидание: Хармони и Лекси', 'Date at the park (Harmony)': 'Свидание в парке (Хармони)', 'Date at the mall (Harmony)': 'Свидание в ТЦ (Хармони)', 'Date at home (Harmony)': 'Свидание дома (Хармони)', 'Meet Harmony parents': 'Встреча с родителями Хармони', 'Harmony meet Angela': 'Знакомство Хармони с Анджелой', 'Date at the strip club (Harmony)': 'Свидание в стриптиз-клубе (Хармони)', "Attend Kylie's trial": 'Суд над Кайли', "Attend Kylie's execution": 'Казнь Кайли', 'Date (Lexi & Reona)': 'Свидание: Лекси и Реона', "Sam and Ryan's wedding": 'Свадьба Сэм и Райана', "Palla's scene, performer fee": 'Сцена с Паллой: гонорар', "Palla's MainlyFans, my cut": 'MainlyFans Паллы: моя доля', "Palla's catalog day": 'Съёмка Паллы для каталога', 'Palla chipping in': 'Вклад Паллы', "She'll be fired": 'Её уволят', 'ERROR: Unable to connect. Switch to manual authentication': 'Ошибка: не удалось подключиться. Перейдите к ручной авторизации.', 'ERROR: Unable to check token validity\nRestart.': 'Ошибка: не удалось проверить токен доступа.\nПерезапустите игру.', 'monday': 'Понедельник', 'tuesday': 'Вторник', 'wednesday': 'Среда', 'thursday': 'Четверг', 'friday': 'Пятница', 'saturday': 'Суббота', 'sunday': 'Воскресенье', 'Ask about Viktor': 'Спросить о Викторе', 'Choose a new talk subject': 'Выбрать новую тему разговора'}
    previous_replace_text = store.config.replace_text
    phrases = {
        'I take a boring (and way too long) English class.': 'Сижу на скучном (и слишком долгом) занятии по английскому.',
        'I sit almost lost in an half-empty classroom.': 'Я сижу в полупустой аудитории и чувствую себя потерянно.',
        'A little Chinese man is teaching the basics of Spanish.': 'Невысокий китаец объясняет основы испанского.',
        'I listen to a guy talking about space, stars, suns and planets.': 'Слушаю, как какой-то парень рассказывает о космосе, звёздах, солнцах и планетах.',
        'I never knew that a hot teacher could make economy interesting.': 'Кто бы мог подумать, что привлекательный преподаватель сделает экономику интересной.',
        'Luckily, this class is very short.': 'К счастью, это занятие совсем короткое.',
        'I stare blankly at the walls.': 'Бессмысленно пялюсь на стены.',
        "Economy 101, that's something I'll tell my grandchildren about.": 'Введение в экономику — вот о чём я буду рассказывать внукам.',
        'Do they teach anything useful here?': 'Здесь вообще учат чему-нибудь полезному?',
        "The history of German porn...now there's a topic I won't get bored with.": 'История немецкого порно... вот уж с такой темой не соскучишься.',
        'I have a couple drinks with some friends.': 'Выпиваю с друзьями пару бокалов.',
        'I have a few too many then go home.': 'Перебираю с выпивкой и иду домой.',
        "I wonder if I'm an alcoholic...": 'Интересно, это уже алкоголизм?..',
        "Let's party!!": 'Пора тусить!!',
        'Whoa, that beer is fucking great.': 'Охренеть, какое классное пиво.'
    }

    def phrase(value):
        return phrases.get(value, value)

    def pronoun(value):
        return {'he':'он', 'she':'она'}.get(value, value)

    def action(value):
        return {'kissing':'целую', 'groping':'лапаю'}.get(value, value)

    def dative(value):
        return {'her':'ей', 'him':'ему', 'them':'им'}.get(value, value)

    def bath_apology(value):
        if value == 'everyone':
            return 'Простите, я не знал, что вы здесь.'
        return 'Прости, ' + str(value) + ', я не знал, что ты здесь.'

    def names(value, people):
        names = [person.name for person in people]
        if len(names) < 2:
            return value
        original = ', '.join(names[:-1]) + ' and ' + names[-1]
        if value != original:
            return value
        return ', '.join(names[:-1]) + ' и ' + names[-1]

    def status_acc(value):
        return {
            'friend':'подругу', 'just friend':'подругу', 'girlfriend':'девушку',
            'fiance':'невесту', 'wife':'жену', 'ex-girlfriend':'бывшую девушку',
            'ex-fiance':'бывшую невесту', 'ex-wife':'бывшую жену',
            'pet':'питомицу', 'sex slave':'секс-рабыню', 'mistress':'госпожу',
            'roommate':'соседку', 'boss':'начальницу', 'coworker':'коллегу',
            'employee':'сотрудницу'
        }.get(value, value)

    def replace_text(value):
        if previous_replace_text is not None:
            value = previous_replace_text(value)
        if engine.game.preferences.language != 'russian':
            return value
        if value in strings:
            return strings[value]
        match = re.fullmatch(r'([^\r\n]+) is off to negotiate with the landlord\.', value)
        if match:
            return match.group(1) + ' отправляется на переговоры с хозяином дома.'
        match = re.fullmatch(r'(\{size=20\})?Martial arts ([0-9]+)%(\{/size\})?', value)
        if match and bool(match.group(1)) == bool(match.group(3)):
            return (match.group(1) or '') + 'Боевые искусства ' + match.group(2) + '%' + (match.group(3) or '')
        return value

    def subject(value):
        if value == 'My roommates are':
            return 'Мои соседи'
        if isinstance(value, str) and value.endswith(' is'):
            return value[:-3]
        return value

    def possessive(value):
        return {'his':'своём', 'her':'своём', 'their':'своём'}.get(value, value)

    def towel(value):
        return {'a towel':'полотенцем', 'towels':'полотенцами'}.get(value, value)

    def season(value):
        return {'spring':'весны', 'summer':'лета', 'fall':'осени', 'autumn':'осени', 'winter':'зимы'}.get(value, value)

    def compatible(original, translated, row):
        return (isinstance(original, engine.ast.TranslateSay)
            and isinstance(translated, engine.ast.TranslateSay)
            and original.get_code() == row['original_code']
            and translated.get_code() == row['before_code'])

    def install():
        translator = engine.game.script.translator
        for row in corrections:
            original = translator.default_translates.get(row['identifier'])
            translated = translator.language_translates.get((row['identifier'], 'russian'))
            if compatible(original, translated, row):
                translated.what = row['target']
                applied.append(row['identifier'])
            else:
                skipped.append(row['identifier'])

init 1170 python:
    lssb_textfragments.install()
    config.replace_text = lssb_textfragments.replace_text

translate russian strings:
    old "Ask to join you"
    new "Позвать сюда"
    old "Convince the employee"
    new "Уговорить сотрудника"
    old "Try to sneak in"
    new "Попробовать пробраться незаметно"
    old "Bribe the employee"
    new "Подкупить сотрудника"
    old "High School Reunion (Alexis)"
    new "Встреча выпускников (Алексис)"
    old "Wrestling show (Ayesha)"
    new "Шоу рестлинга (Айеша)"
    old "Meet with Ayesha"
    new "Встреча с Айешой"
    old "Harder training with Ayesha"
    new "Усиленная тренировка с Айешой"
    old "Date (Camila & Lexi)"
    new "Свидание: Камила и Лекси"
    old "Dwayne's Mansion Party"
    new "Вечеринка в особняке Дуэйна"
    old "Meet with Sam and Emma"
    new "Встреча с Сэм и Эммой"
    old "Scavenger hunt (Emma)"
    new "Квест (Эмма)"
    old "Date at restaurant (Hanna)"
    new "Свидание в ресторане (Ханна)"
    old "Home Christmas Party"
    new "Рождественская вечеринка дома"
    old "Meet Anna and Kleio"
    new "Встреча с Анной и Клео"
    old "Threesome (Audrey,Sasha)"
    new "Секс втроём: Одри и Саша"
    old "Office Christmas Party"
    new "Рождественская вечеринка в офисе"
    old "Date (Harmony & Lexi)"
    new "Свидание: Хармони и Лекси"
    old "Date at the park (Harmony)"
    new "Свидание в парке (Хармони)"
    old "Date at the mall (Harmony)"
    new "Свидание в ТЦ (Хармони)"
    old "Date at home (Harmony)"
    new "Свидание дома (Хармони)"
    old "Meet Harmony parents"
    new "Встреча с родителями Хармони"
    old "Harmony meet Angela"
    new "Знакомство Хармони с Анджелой"
    old "Date at the strip club (Harmony)"
    new "Свидание в стриптиз-клубе (Хармони)"
    old "Attend Kylie's trial"
    new "Суд над Кайли"
    old "Attend Kylie's execution"
    new "Казнь Кайли"
    old "Date (Lexi & Reona)"
    new "Свидание: Лекси и Реона"
    old "Sam and Ryan's wedding"
    new "Свадьба Сэм и Райана"
    old "Palla's scene, performer fee"
    new "Сцена с Паллой: гонорар"
    old "Palla's MainlyFans, my cut"
    new "MainlyFans Паллы: моя доля"
    old "Palla's catalog day"
    new "Съёмка Паллы для каталога"
    old "Palla chipping in"
    new "Вклад Паллы"
    old "She'll be fired"
    new "Её уволят"
    old "ERROR: Unable to connect. Switch to manual authentication"
    new "Ошибка: не удалось подключиться. Перейдите к ручной авторизации."
    old "ERROR: Unable to check token validity\nRestart."
    new "Ошибка: не удалось проверить токен доступа.\nПерезапустите игру."
    old "monday"
    new "Понедельник"
    old "tuesday"
    new "Вторник"
    old "wednesday"
    new "Среда"
    old "thursday"
    new "Четверг"
    old "friday"
    new "Пятница"
    old "saturday"
    new "Суббота"
    old "sunday"
    new "Воскресенье"
    old "Ask about Viktor"
    new "Спросить о Викторе"
    old "Choose a new talk subject"
    new "Выбрать новую тему разговора"
