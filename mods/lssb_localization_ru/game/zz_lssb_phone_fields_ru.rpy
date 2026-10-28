# Display helpers for the structurally guarded Russian smartphone screen.
# Skill objects, appointments and saved names are never modified.
init 1004 python:
    _lssb_phone_skills = {
        "Hypnosis": "Гипноз", "Foodie": "Гурман",
        "High Libido": "Высокое либидо", "Low Libido": "Низкое либидо",
        "Fertility Assessment": "Оценка фертильности", "Investigator": "Сыщик",
        "Massage": "Массаж", "Guitar": "Игра на гитаре", "Kart Racing": "Картинг",
        "Dancer": "Танцор", "Night Owl": "Сова", "Gamer": "Геймер",
        "Iron Stomach": "Железный желудок", "Sneaky": "Скрытность",
        "Shibari": "Сибари", "S&M": "Садомазохизм",
        "Hated by Animals": "Нелюбовь животных", "Small Dick": "Маленький пенис",
    }
    _lssb_agenda_labels = {
        "Today": "Сегодня", "All Day": "Весь день",
        "Attend Kylie's execution": "Казнь Кайли",
        "Attend Kylie's trial": "Суд над Кайли",
        "Dwayne's Mansion Party": "Вечеринка в особняке Дуэйна",
        "Halloween Party": "Вечеринка на Хэллоуин",
        "Harder training with Ayesha": "Усиленная тренировка с Айешей",
        "Harmony meet Angela": "Знакомство Хармони с Анджелой",
        "Home Christmas Party": "Рождественская вечеринка дома",
        "Meet Anna and Kleio": "Встреча с Анной и Клео",
        "Meet Harmony parents": "Встреча с родителями Хармони",
        "Meet the master for my first lesson": "Первый урок у мастера",
        "Meet the master for the second lesson": "Второй урок у мастера",
        "Meet the master for the third lesson": "Третий урок у мастера",
        "Meet the master for the fourth lesson": "Четвёртый урок у мастера",
        "Meet the master for the fifth lesson": "Пятый урок у мастера",
        "Meet the master for the final lesson": "Последний урок у мастера",
        "Meet with Ayesha": "Встреча с Айешей",
        "Meet with Sam and Emma": "Встреча с Самантой и Эммой",
        "Meeting Cassidy": "Встреча с Кэссиди",
        "Office Christmas Party": "Рождественский корпоратив",
        "Office Party": "Корпоратив", "Office Tour": "Экскурсия по офису",
        "Ryan's funeral": "Похороны Райана",
        "Sam and Ryan's wedding": "Свадьба Саманты и Райана",
    }
    _lssb_agenda_prefixes = {
        "Birthday": "День рождения", "Date": "Свидание",
        "Harem Date:": "Групповое свидание", "Beach Date": "Свидание на пляже",
        "Date at home": "Свидание дома", "Date at restaurant": "Свидание в ресторане",
        "Date at the mall": "Свидание в торговом центре",
        "Date at the park": "Свидание в парке",
        "Date at the strip club": "Свидание в стрип-клубе",
        "High School Reunion": "Встреча выпускников",
        "Threesome": "Секс втроём", "Wrestling show": "Шоу рестлинга",
    }
    _lssb_phone_jobs = {
        "Church": "Церковь", "Gym reception": "Стойка спортзала",
        "homelessshelter": "Приют для бездомных", "Maid Cafe": "Мэйд-кафе",
        "model": "Модель", "pornstar": "Порноактриса", "prostitute": "Проститутка",
        "Night Club": "Ночной клуб", "Pub": "Паб", "Strip club": "Стрип-клуб",
    }

    def _lssb_phone_job_line(period, value):
        if _preferences.language != "russian":
            template = "{b}Job (day):{/b} [job_day]" if period == "day" else "{b}Job (night):{/b} [job_night]"
            return renpy.substitute(template, scope={"job_day": value, "job_night": value})
        title = "Работа (днём)" if period == "day" else "Работа (ночью)"
        job = _lssb_phone_jobs.get(value, _lssb_ui_translate(value))
        return "{b}" + title + ":{/b} " + job

    def _lssb_phone_skill(value):
        if _preferences.language != "russian":
            return value
        return _lssb_phone_skills.get(value, _lssb_ui_translate(value))

    def _lssb_agenda_text(value):
        if _preferences.language != "russian":
            return value
        return _lssb_agenda_labels.get(value, _lssb_ui_translate(value))

    def _lssb_agenda_name(value):
        if _preferences.language != "russian" or not isinstance(value, str):
            return value
        # Only native calendar formats are parsed; unknown titles pass through.
        import re
        for prefix, translated in _lssb_agenda_prefixes.items():
            if value.startswith(prefix + " (") and value.endswith(")"):
                names = value[len(prefix) + 2:-1]
                parts = re.split(r"(\s*&\s*|\s*,\s*)", names)
                names = "".join((" и " if "&" in part else ", ") if i % 2 else _lssb_story_text(part) for i, part in enumerate(parts))
                return translated + " (" + names + ")"
        return _lssb_agenda_text(value)

    def _lssb_agenda_alt(entry):
        if _preferences.language != "russian":
            return f'{entry.name}: {find_full_day_name(entry.day)} {entry.hour}'
        day = _lssb_agenda_text(entry.day)
        if entry.day_number:
            day += " " + str(entry.day_number)
        return _lssb_agenda_name(entry.name) + ": " + day + " " + _lssb_agenda_text(entry.hour)

# The optional wide phone has its own screen in the visual component.
# Adapt only six known display expressions; keep its geometry and actions.
init 1142 python in lssb_phone_fields:
    import copy
    import renpy as engine
    import store
    _constant = True
    patch_status = "wide phone absent"
    screen = engine.display.screen.screens.get(('smartphone', 'lssb_phone_26_8_0d'))
    if screen is not None:
        tree = copy.deepcopy(screen.function)
        counts = [0, 0, 0, 0, 0, 0]
        for original, node in zip(store.lssb_textinterface.walk(screen.function), store.lssb_textinterface.walk(tree)):
            code = getattr(original, 'code', None)
            if code is not None and type(code).__name__ == 'PyCode':
                node.code = code
            if type(node).__name__ != 'SLDisplayable':
                continue
            if node.name == 'text':
                for i, (old, new) in enumerate((
                    ('entry.day', '_lssb_agenda_text(entry.day)'),
                    ('entry.hour', '_lssb_agenda_text(entry.hour)'),
                    ('_lssb_phone_resize(entry.name, 314, 19)', '_lssb_phone_resize(_lssb_agenda_name(entry.name), 314, 19)'),
                    ('"{b}Job (day):{/b} [job_day]"', '_lssb_phone_job_line("day", job_day)'),
                    ('"{b}Job (night):{/b} [job_night]"', '_lssb_phone_job_line("night", job_night)'),
                )):
                    if node.positional == [old]:
                        node.positional = [new]
                        counts[i] += 1
            old_alt = "f'{entry.name}: {find_full_day_name(entry.day)} {entry.hour}'"
            if node.name == 'button' and dict(node.keyword).get('alt') == old_alt:
                node.keyword = [(key, '_lssb_agenda_alt(entry)' if key == 'alt' else value) for key, value in node.keyword]
                counts[5] += 1
        if counts == [1, 1, 1, 1, 1, 1]:
            # Do not reuse analysis cached for the unmodified visual screen.
            tree.variant = "'lssb_phone_fields_1_88_2'"
            tree.const_ast = None
            tree.not_const_ast = None
            tree.analysis = None
            tree.prepared = False
            screen.function = tree
            screen.ast = tree
            previous_translate = store._lssb_phone_translate
            def translate(value):
                if engine.game.preferences.language == 'russian' and value in store._lssb_phone_skills:
                    return store._lssb_phone_skills[value]
                return previous_translate(value)
            store._lssb_phone_translate = translate
            patch_status = "patched six display expressions and skill labels"
        else:
            patch_status = "wide phone changed; original screen retained"
            store.renpy.log('LSSB phone fields: ' + patch_status)
