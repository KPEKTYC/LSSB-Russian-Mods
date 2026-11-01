# Literal speaker labels on Russian dialogue lines only. A string table would also
# rewrite any on-screen text equal to the label, such as a player who is named Jeff.
# Runs after the review modules, whose guards compare the original speaker.
init 1180 python in lssb_speakers:
    import renpy as engine
    import store
    _constant = True
    names = {
        "Priest": "Священник", "Coworker": "Коллега", "Michaels": "Майклс", "Майклз": "Майклс",
        "Detective": "Детектив", "Shady guy": "Подозрительный тип", "Investigator": "Следователь",
        "Mr Blank": "Мистер Бланк", "Ray": "Рэй", "Guy": "Парень", "Girl": "Девушка",
        "Female fan": "Поклонница", "Male fan": "Поклонник", "Gwendoline": "Гвендолин",
        "Shop owner": "Владелец магазина", "Another Kid": "Другой мальчишка",
        "Handsome man": "Красавчик", "Vincent": "Винсент", "Edna": "Эдна",
        "Bear Chan": "Медведица-тян", "Manager": "Менеджер", "Judge": "Судья", "Gianna": "Джанна",
        "Inspector": "Инспектор", "Jeff": "Джефф", "Old pervert": "Старый извращенец",
        "Bather": "Отдыхающий", "Dylan": "Дилан", "Gwen": "Гвен", "Random Man": "Незнакомец",
        "Mrs White": "Миссис Уайт",
    }
    renamed = 0

    def rename(node):
        global renamed
        who = getattr(node, "who", None)
        if isinstance(who, str) and who[:1] == '"' and who[1:-1] in names:
            node.who = '"' + names[who[1:-1]] + '"'
            renamed += 1

    for (_identifier, _language), _node in engine.game.script.translator.language_translates.items():
        if _language == "russian":
            rename(_node)
            for _child in getattr(_node, "block", None) or ():
                rename(_child)

    # Default names only, on Russian screens. A name the player gave their own hero
    # stays exactly as typed, even when it matches a character's.
    persons = {
        "Aletta": "Алетта", "Alexis": "Алексис", "Amy": "Эми", "Angela": "Анджела", "Anna": "Анна",
        "Audrey": "Одри", "Ayesha": "Аиша", "Bree": "Бри", "Camila": "Камила", "Cassidy": "Кэссиди",
        "Cherie": "Шери", "Claire": "Клэр", "Danny": "Дэнни", "Dwayne": "Дуэйн", "Emma": "Эмма",
        "Hanna": "Ханна", "Harmony": "Хармони", "Jack": "Джек", "Kat": "Кэт", "Kiara": "Киара",
        "Kleio": "Клео", "Kylie": "Кайли", "Lavish": "Лавиш", "Lexi": "Лекси", "Master": "Мастер",
        "Minami": "Минами", "Morgan": "Морган", "Natalie": "Натали", "Palla": "Палла", "Reona": "Реона",
        "Ryan": "Райан", "Samantha": "Саманта", "Sasha": "Саша", "Scottie": "Скотти", "Shawn": "Шон",
        "Shiori": "Сиори", "Victor": "Виктор", "Violaine": "Виолен",
        "Applebaum": "Эпплбаум", "Cheese": "Чиз", "Foglio": "Фольо", "Jackson": "Джексон", "Yaga": "Яга",
    }

    def person_name(value):
        if engine.game.preferences.language != "russian" or not isinstance(value, str):
            return value
        hero = getattr(store, "hero", None)
        if hero is not None and value in (getattr(hero, "name", None), getattr(hero, "family_name", None)):
            return value
        return persons.get(value, value)

    store._lssb_person_name = person_name

    # A heroine's name box reads her live name, which no dialogue line carries.
    _native_prefix_suffix = getattr(engine.character.ADVCharacter, "prefix_suffix", None)
    if _native_prefix_suffix:
        def _prefix_suffix(self, thing, prefix, body, suffix):
            return _native_prefix_suffix(self, thing, prefix, person_name(body) if thing == "who" else body, suffix)
        engine.character.ADVCharacter.prefix_suffix = _prefix_suffix
