# Russian text for interface pieces added in game 26.10.0, and one game fix.
init 1005 python:
    # Game fix: only Activity builds its per-room cache, so an InteractActivity's "rooms"
    # was never checked and the 26.10.0 hangouts (TV, console, snacks...) showed everywhere.
    if isinstance(getattr(store, "InteractActivity", None), type) and callable(getattr(InteractActivity, "_iterate_over_rooms", None)):
        _lssb_native_interact_test = InteractActivity.test
        _lssb_interact_rooms = {}

        def _lssb_interact_test(self, debug=False):
            if self.rooms is not None:
                if self.name not in _lssb_interact_rooms:
                    _lssb_interact_rooms[self.name] = frozenset(type(self)._iterate_over_rooms(self.rooms))
                if game.room not in _lssb_interact_rooms[self.name]:
                    return False
            return _lssb_native_interact_test(self, debug)

        InteractActivity.test = _lssb_interact_test

    # 26.10.0c stat bar tooltips: "{b}" + ui_title + "{/b}\n" + ui_tooltip.format(name=girl.name).
    _lssb_stat_titles = {
        "Frustration": "Неудовлетворённость", "Love": "Любовь", "Dominance": "Доминирование",
        "Submissiveness": "Покорность", "Exhibitionism": "Эксгибиционизм", "Horniness": "Возбуждение",
        "Lesbian": "Лесбийские наклонности", "Masculinity": "Мужественность", "Vampire": "Вампир",
        "Yandere": "Одержимая любовь", "Siscon": "Сисконность", "Career": "Карьера", "Purity": "Невинность",
    }
    _lssb_stat_texts = {
        "Builds up when you tease {name} and leave her wanting. Makes her more willing for sex.":
            "Растёт, когда ты её дразнишь и оставляешь ни с чем. Чем выше, тем охотнее {name} соглашается на секс.",
        "How much {name} loves you. Dates, kisses and her story need it.":
            "Насколько сильно {name} тебя любит. Нужна для свиданий, поцелуев и её истории.",
        "How dominant {name} is with you. Opens acts where she takes charge.":
            "Насколько {name} доминирует с тобой. Открывает действия, где ведёт она.",
        "How submissive {name} is with you. Opens acts where you take charge.":
            "Насколько {name} покорна тебе. Открывает действия, где ведёшь ты.",
        "How far {name} goes with you in public. Opens what you can do around people.":
            "Как далеко {name} готова зайти с тобой на людях. Открывает то, что можно делать при посторонних.",
        "How much {name} wants sex. Opens acts and speeds up her frustration.":
            "Насколько сильно {name} хочет секса. Открывает действия и ускоряет рост неудовлетворённости.",
        "How much {name} is into girls. Opens scenes with them; too much holds her love back.":
            "Насколько {name} увлечена девушками. Открывает сцены с ними; если слишком много — мешает её любви к тебе.",
        "How masculine {name} is. Changes {name}'s look and outfits.":
            "Насколько {name} мужественна. Меняет её внешность и одежду.",
        "How much {name} lives her vampire act. Feed it, or reach the girl behind it.":
            "Насколько {name} вжилась в роль вампира. Подыгрывай ей или достучись до девушки за этой маской.",
        "How obsessed {name} is with you. Makes her jealous of the girls you see.":
            "Насколько {name} одержима тобой. Из-за этого она ревнует к девушкам, с которыми ты видишься.",
        "How far you see {name} as more than a sister. Opens kissing her and more.":
            "Насколько ты видишь в ней не просто сестру. Открывает поцелуи и не только.",
        "How far {name}'s career has got. Grows each day she works her job.":
            "Насколько {name} продвинулась в карьере. Растёт с каждым её рабочим днём.",
        "How innocent {name} still is. Sets the outfits she wears and slows her frustration.":
            "Насколько {name} ещё невинна. Определяет её одежду и замедляет рост неудовлетворённости.",
    }

    def _lssb_stat_tooltip(text):
        import re
        if _preferences.language != "russian":
            return None
        title = None
        m = re.match(r"\{b\}([^{}]+)\{/b\}\n(.*)\Z", text, re.S)
        if m:
            title, text = m.group(1), m.group(2)
            if title not in _lssb_stat_titles:
                return None
        for english, russian in _lssb_stat_texts.items():
            pattern = "^" + re.escape(english).replace(re.escape("{name}"), "(?P<name>.+?)", 1).replace(re.escape("{name}"), "(?P=name)") + r"\Z"
            hit = re.match(pattern, text, re.S)
            if hit:
                body = russian.replace("{name}", _lssb_person_name(hit.group("name")))
                return ("{b}" + _lssb_stat_titles[title] + "{/b}\n" + body) if title else body
        return None

    # Native tooltip_parts(), with each English piece translated before the game joins them.
    def _lssb_tooltip_parts(tooltip, in_inventory=False, keep_at_it=False):
        translate = _lssb_ui_translate
        if isinstance(tooltip, (tuple, list)):
            return None, tooltip_lines(translate(list(tooltip)))
        if isinstance(tooltip, str):
            return None, _lssb_stat_tooltip(tooltip) or translate(tooltip)
        if isinstance(tooltip, Person):
            title = translate("Talk to [tooltip.name]")
            if title == "Talk to [tooltip.name]" and _preferences.language == "russian":
                title = "Поговорить: [tooltip.name]"
            return title.replace("[tooltip.name]", _lssb_person_name(tooltip.name)), None
        if isinstance(tooltip, Room):
            title = _lssb_visual_go_to(tooltip.display_name)
        elif keep_at_it and isinstance(tooltip, BaseActivity):
            title = translate(tooltip.loop_display_name)
        else:
            title = translate(tooltip.display_name)
        details = tooltip.get_tooltip(in_inventory) if hasattr(tooltip, "get_tooltip") else None
        if isinstance(details, (tuple, list)):
            details = tooltip_lines(translate(list(details)))
        elif isinstance(details, str):
            details = translate(details)
        if details:
            details = details.replace("{image=gui/icons/icon_clock.png}", "{image=tooltip_clock}")
            if _preferences.language == "russian":
                # Gift effects arrive as one multi-line string, so translate the shared line inside it.
                for english, russian in _lssb_tooltip_fragments.items():
                    details = details.replace(english, russian)
        return title, details or None

    # 26.10.0 picks the hero's and the girls' nicknames by speaker from the game's yml files.
    # Values: one form, or (form for a male hero, form for a female hero).
    _lssb_nicknames = {
        'amour': ('любимый', 'любимая'), 'baby': 'малыш', 'big bro': 'братик', 'bitch': 'сучка', 'boi': 'парень',
        'boo': ('милый', 'милая'), 'boss': 'босс', 'boss buck': 'босс Бак', 'boy': 'мальчик', 'boytoy': 'мальчик-игрушка',
        'brah': 'бро', 'brainiac': 'умник', 'bro-bro': 'братишка', 'chad': 'альфач', 'champ': 'чемпион', 'chief': 'шеф',
        'coach': 'тренер', 'cochonet': 'поросёнок', 'cow-boy': 'ковбой', 'cuck': 'рогоносец', 'cutie': 'милашка',
        'daddy': 'папочка', 'dark knight': 'тёмный рыцарь', 'dearest': ('дорогой', 'дорогая'), 'demon': 'демон',
        'dick': 'хрен', 'dreamboat': 'мужчина мечты', 'dude': 'чувак', 'dumbass': 'придурок', 'fuck face': 'хреномордый',
        'fuckface': 'хреномордый', 'gamer': ('геймер', 'геймерша'), 'genius': 'гений', 'guapo': 'красавчик',
        'hanata': 'ханата', 'hermoso': 'красавец', 'hero': 'герой', 'honey': ('милый', 'милая'), 'hotshot': 'крутыш',
        'idiot': ('идиот', 'идиотка'), 'koibito': 'койбито', 'little man': 'малыш', 'little one': ('малыш', 'малышка'),
        'lord': 'милорд', 'love': ('любимый', 'любимая'), 'loverboy': 'сердцеед', 'master': 'господин',
        'mr.boss sir': 'господин босс', 'muffin': 'маффин', 'my big bear': 'мой большой мишка',
        'my heart': 'сердце моё', 'my king': 'мой король', 'my one and only': ('мой единственный', 'моя единственная'),
        'my prince': 'мой принц', 'my angel': 'мой ангел', 'my ball and chain': 'мои оковы',
        'my daylight delight': 'моя дневная радость', 'my friend': 'мой друг', 'my pretty': ('красавчик мой', 'красавица моя'),
        'my rock': 'моя опора', 'my sweet mortal meat': 'моё сладкое смертное мясо', 'naughty boy': 'шалун',
        'nii-san': 'нии-сан', 'onii-chan': 'онии-тян', 'owner': ('хозяин', 'хозяйка'), 'papi': 'папи',
        'papi chulo': 'папи чуло', 'partner': ('напарник', 'напарница'), 'peasant': 'простолюдин',
        'perv': ('извращенец', 'извращенка'), 'playboy': 'плейбой', 'player one': 'первый игрок',
        'player two': 'второй игрок', 'pumpkin': 'тыковка', 'roomie': ('сосед', 'соседка'), 'second string': 'запасной',
        'senpai': 'сэмпай', 'servant': ('слуга', 'служанка'), 'sir': 'сэр', 'slave': ('раб', 'рабыня'),
        'smooth rider': 'лихой наездник', 'stallion': 'жеребец', 'step-bro': 'сводный братик', 'studmuffin': 'жеребчик',
        'sugar': ('сладкий', 'сладкая'), 'superstar': 'суперзвезда', 'sweetheart': ('любимый', 'любимая'),
        'teach': 'учитель', 'twink': 'твинк', 'wallet': 'кошелёк', 'young man': 'молодой человек',
        'cupcake': 'кексик', 'step-sis': 'сводная сестрёнка',
    }

    def _lssb_nickname(value):
        # The player's own typed name passes unchanged, even when it equals a nickname.
        if _preferences.language != "russian" or not isinstance(value, str) or value == getattr(store, "heroname", None):
            return value
        for english, russian in (("Mister ", "мистер "), ("Miss ", "мисс ")):
            if value.startswith(english):
                return russian + value[len(english):]
        found = _lssb_nicknames.get(value.lower())
        if isinstance(found, tuple):
            found = found[hero.gender == "female"]
        return found or value

    if callable(globals().get("get_hero_nickname")) and callable(globals().get("get_npc_nickname")):
        _lssb_native_hero_nickname = get_hero_nickname
        _lssb_native_npc_nickname = get_npc_nickname
        # The game looks both up in the store on every call, so wrapping the names reaches
        # hero.name, Person.heronickname and Person.callname alike.
        def get_hero_nickname(person_name):
            return _lssb_nickname(_lssb_native_hero_nickname(person_name))
        def get_npc_nickname(person, default):
            value = _lssb_native_npc_nickname(person, default)
            return value if value is default else _lssb_nickname(value)

    _lssb_tooltip_fragments = {
        "raw points: what she gains depends on her level": "базовые очки: сколько она получит, зависит от её уровня",
    }

# Menu captions the game builds around a character's name: bath at home, pet walk.
init 1171 python:
    import re as _lssb_re
    _lssb_update2610_previous_text = config.replace_text

    def _lssb_name_case(name, case):
        # Feminine names in -а/-я decline, the rest (Бри, Лекси, Кайли...) do not.
        # shortcut: a male name ending in a consonant stays nominative; only Mike, for a female hero, reaches the bath menu.
        name = getattr(store, "_lssb_person_name", lambda value: value)(name)
        if name[-1:] not in ("а", "я"):
            return name
        if case == "acc":
            return name[:-1] + ("ю" if name[-1:] == "я" else "у")
        return name[:-1] + ("ей" if name[-1:] == "я" or name[-2:-1] in ("ш", "ж", "ч", "щ", "ц") else "ой")

    def _lssb_update2610_text(value):
        if _lssb_update2610_previous_text is not None:
            value = _lssb_update2610_previous_text(value)
        if _preferences.language != "russian":
            return value
        match = _lssb_re.fullmatch(r"Take a bath with ([^\r\n]+)", value)
        if match:
            return "Принять ванну с " + _lssb_name_case(match.group(1), "ins")
        match = _lssb_re.fullmatch(r"Call ([^\r\n]+) to join us", value)
        if match:
            return "Позвать с нами " + _lssb_name_case(match.group(1), "acc")
        # An activity's keep-at-it name: "<activity> (repeat)".
        match = _lssb_re.fullmatch(r"([^\r\n]+) \(repeat\)", value)
        if match:
            name = _lssb_ui_translate(match.group(1))
            if name != match.group(1):
                return name + " (повторять)"
        return value

    config.replace_text = _lssb_update2610_text

    # config.replace_text only ever sees the text between tags, so the notification popup
    # translates its whole string here: "{size=20}Study{/size}", "{size=20}Cooking 60%{/size}",
    # "{size=20}+ Cooking{/size}", "{size=20}{image=gui/icons/icon_story_new.png} <story>{/size}".
    # Trait ids of data/stat_traits.yml, as the traits are named on the character card.
    _lssb_trait_names = {"dominant": "Доминирование", "exhibitionist": "Эксгибиционизм", "innocent": "Невинность",
                         "kinky": "Любовь к экспериментам", "rebel": "Бунтарство", "shy": "Застенчивость",
                         "slutty": "Распутность", "submissive": "Покорность"}

    def _lssb_notification_text(value):
        whole = _lssb_ui_translate(value)
        if whole != value or not isinstance(value, str) or _preferences.language != "russian":
            return whole
        # cl/class_stat_affinity.rpy StatTrait._announce: "{image=notify <id>} <name> is now|is no longer <trait id>".
        trait = _lssb_re.fullmatch(r"(\{image=notify [^}]+\} )(.+) is (now|no longer) ([a-z_ ]+)", value)
        if trait and trait.group(4) in _lssb_trait_names:
            icon, name, state, label = trait.groups()
            name = getattr(store, "_lssb_person_name", lambda v: v)(name)
            label = _lssb_trait_names[label]
            return icon + name + (": новая черта — «%s»" % label if state == "now" else ": черта «%s» пропала" % label)
        story = _lssb_re.fullmatch(r"(.*\{image=gui/icons/icon_story_(?:new|update|complete)\.png\} )(.+?)((?:\{/size\})?)", value, _lssb_re.S)
        if story:
            return story.group(1) + _lssb_story_text(story.group(2)) + story.group(3)

        def piece(body):
            skill = _lssb_re.fullmatch(r"(\+ |- )?([^{}%]+?)( [0-9]+%)?", body)
            if not skill:
                return body
            sign, name, percent = skill.groups()
            translated = globals().get("_lssb_phone_skills", {}).get(name) or _lssb_ui_translate(name)
            if translated == name and not (sign or percent):
                translated = _lssb_activity_text(name) if callable(globals().get("_lssb_activity_text")) else name
            return (sign or "") + translated + (percent or "")

        # Skills and activities sit in a size block, sometimes after an icon and an amount
        # ("{image=gui/icons/icon_money.png} -25 · {size=20}Buy a round{/size}"), or bare ("Study").
        if "{size=" not in value:
            return piece(value)
        return _lssb_re.sub(r"(\{size=\d+\})([^{}]+)(\{/size\})", lambda m: m.group(1) + piece(m.group(2)) + m.group(3), value)

    # The date spot picker (screen select, ev/romance.rpy) shows each spot's capitalized display_name.
    # A plain string table would mistranslate some of them: "Beach" is also a trait there.
    _lssb_date_spots = {
        "Date spots": "Где провести свидание", "Aquarium": "Океанариум", "Beach": "Пляж", "Forest": "Лес",
        "Home": "Дом", "Maid cafe": "Мейд-кафе", "Mall": "Торговый центр", "Nightclub": "Ночной клуб",
        "Park": "Парк", "Fancy restaurant": "Дорогой ресторан", "Water park": "Аквапарк", "Cinema": "Кинотеатр",
        "Nudist beach": "Нудистский пляж", "Pub": "Паб", "Strip club": "Стрип-клуб",
    }

    def _lssb_select_text(value):
        if _preferences.language == "russian" and value in _lssb_date_spots:
            return _lssb_date_spots[value]
        return _lssb_ui_translate(value)

    # Pets of 26.10.0 are Persons too: their default names and the names picked in ev/pets_extra.rpy.
    _lssb_pet_names = {"Dog": "Собака", "Cat": "Кошка", "Bunny": "Кролик", "Capybara": "Капибара", "Turtle": "Черепаха",
                       "Pancake": "Блинчик", "Clover": "Клевер", "Angel": "Ангел", "Sheldon": "Шелдон", "Tank": "Танк",
                       "Zack": "Зак", "Bruce": "Брюс", "François": "Франсуа", "Nicky": "Ники", "Lennie": "Ленни", "Joey": "Джои"}

    # On Easy, 26.10.0 appends a step's explicit hint to its name: "Step (date score 90+)".
    if callable(globals().get("_lssb_story_text")):
        _lssb_story_text_whole = _lssb_story_text

        def _lssb_story_text(value):
            shown = _lssb_story_text_whole(value)
            if shown == value and isinstance(value, str) and value.endswith(")") and " (" in value:
                step, hint = value.rsplit(" (", 1)
                return _lssb_story_text_whole(step) + " " + _lssb_story_text_whole("(" + hint)
            return shown

# lssb_speakers fills its name table at init 1180.
init 1181 python:
    if hasattr(store, "lssb_speakers") and isinstance(getattr(lssb_speakers, "persons", None), dict):
        for _lssb_pet_en, _lssb_pet_ru in _lssb_pet_names.items():
            lssb_speakers.persons.setdefault(_lssb_pet_en, _lssb_pet_ru)
