# Russian text for interface pieces changed in game 26.10.0f-0i (legacy stats, tracker progress, phone).
init 1007 python:
    _lssb_story_strings.update({
        "Hire a PI to find the coach (call the Investigator from my phone)": "Нанять частного детектива, чтобы найти тренера (позвонить Сыщику с телефона)",
        "Meet up with Kylie in a public place.": "Встретиться с Кайли в людном месте.",
        # Cupid DLC tracker texts, missing since the DLC (its yml was never in the audits).
        "Angela and Bruce": "Анджела и Брюс",
        "Reona and Jack": "Реона и Джек",
        "Angela and Bruce's Cupid": "Купидон: Анджела и Брюс",
        "Anna and Gwen's Cupid": "Купидон: Анна и Гвен",
        "Cherie and Dwayne's Cupid": "Купидон: Шери и Дуэйн",
        "Hanna and the Master's Cupid": "Купидон: Ханна и Мастер",
        "Kleio and Morgan's Cupid": "Купидон: Клео и Морган",
        "Lexi and Danny's Cupid": "Купидон: Лекси и Дэнни",
        "Palla and Shawn's Cupid": "Купидон: Палла и Шон",
        "Reona and Jack's Cupid": "Купидон: Реона и Джек",
        "Sam and Ryan's Cupid": "Купидон: Сэм и Райан",
        "Sasha and Scottie's Cupid": "Купидон: Саша и Скотти",
        "Be at home in the afternoon or evening": "Быть дома днём или вечером",
        "Wait for Jack's call at home in the afternoon or evening": "Дождаться звонка Джека дома днём или вечером",
        "Anna and Gwen got married and live together now!": "Анна и Гвен поженились и теперь живут вместе!",
        "Hanna and the Master got married and left for the dojos of the Far East!": "Ханна и Мастер поженились и уехали в додзё Дальнего Востока!",
        "Kleio and Morgan got married in the aquarium theatre and left together!": "Клео и Морган поженились в театре океанариума и уехали вместе!",
        "Lexi and Danny got married and live together now!": "Лекси и Дэнни поженились и теперь живут вместе!",
        "Palla and Shawn got married!": "Палла и Шон поженились!",
        "Sam and Ryan got married and live together now!": "Сэм и Райан поженились и теперь живут вместе!",
        "Sasha and Scottie get married and live together now!": "Саша и Скотти поженились и теперь живут вместе!",
    })

init 1172 python:
    # 26.10.0f+ stat tooltips: legacy Sub/Dom and the Horniness text, with its purity cap suffix.
    _lssb_stat_titles["Sub/Dom"] = "Покорность/доминирование"
    _lssb_stat_texts.update({
        "{name}'s submissiveness or dominance, horniness and exhibitionism, all in one stat.":
            "Покорность или доминирование, возбуждение и эксгибиционизм {name} — в одном показателе.",
        "How much {name} wants sex. Opens acts and speeds up {name}'s frustration.":
            "Насколько сильно {name} хочет секса. Открывает действия и ускоряет рост неудовлетворённости.",
    })
    _lssb_stat_tooltip_2610e = _lssb_stat_tooltip

    def _lssb_stat_tooltip(text):
        import re
        cap = re.search(r" (\S+)'s purity holds it at (\d+)% at most\.\Z", text) if isinstance(text, str) else None
        if cap is None:
            return _lssb_stat_tooltip_2610e(text)
        shown = _lssb_stat_tooltip_2610e(text[:cap.start()])
        return shown and shown + " Невинность не даёт ему подняться выше %s%%." % cap.group(2)

    # Tracker progress bars (StoryStep.progress_for_ui): "[Name ]Love 40 / 60", "Sub 5 / max 10", "12 / 50".
    _lssb_progress_labels = {
        "Love": "Любовь", "Sub": "Покорность", "Dom": "Доминирование", "Horny": "Возбуждение",
        "Lesbian": "Лесби", "Purity": "Невинность", "Sexperience": "Опыт", "Siscon": "Сисконность",
        "Yandere": "Одержимость", "Sub/Dom": "Покорн./домин.",
    }

    def _lssb_progress_text(value):
        import re
        if _preferences.language != "russian" or not isinstance(value, str):
            return value
        m = re.fullmatch(r"(?:(.+) )?(Sub/Dom|[A-Z][a-z]+) (-?\d+) / (max )?(-?\d+)", value)
        if m is None or m.group(2) not in _lssb_progress_labels:
            return value
        name, label, current, top, target = m.groups()
        label = _lssb_progress_labels[label]
        if name:
            label = _lssb_person_name(name) + ": " + label.lower()
        return "%s %s / %s%s" % (label, current, "макс. " if top else "", target)

    # The phone's call button for the PI, named as the phone's agenda names him; a plain "Investigator"
    # string translation would also rename that speaker in dialogue.
    def _lssb_phone_investigator():
        return "Сыщик" if _preferences.language == "russian" else "Investigator"
