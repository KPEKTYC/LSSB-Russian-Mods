# Readable interaction card. Information visibility and stat calculations stay native.
init 1009 python:
    _lssb_npc_variant = "lssb_npc_card_26_8_0d"
    _lssb_npc_measure_cache = {}

    def _lssb_npc_label(key):
        if _preferences.language == "russian":
            return {"Name:": "Имя:", "Status:": "Статус:", "Age:": "Возраст:",
                "Birthday:": "День рождения:", "Birth control:": "Контрацепция:",
                "Fertility:": "Фертильность:", "Sex count:": "Интимных контактов:",
                "Babies:": "Дети:", "Job:": "Работа:", "Traits": "Черты"}[key]
        return renpy.translation.translate_string(key)

    def _lssb_npc_text_height(value, width, bold=False):
        key = (value, width, bold)
        if key not in _lssb_npc_measure_cache:
            if len(_lssb_npc_measure_cache) >= 256:
                _lssb_npc_measure_cache.clear()
            probe = Text(value, substitute=False, font="exo2_bold" if bold else "exo2_regular",
                size=16, line_spacing=2, xsize=width, layout="tex")
            _lssb_npc_measure_cache[key] = int(renpy.render(probe, width, 720, 0., 0.).get_size()[1])
        return _lssb_npc_measure_cache[key]

    def _lssb_npc_information(girl):
        header = [("name", "Name:", str(girl.name))]
        if girl.status:
            header.append(("status", "Status:", _lssb_phone_status(girl)))
        header.append(("age", "Age:", str(girl.age + girl.flags.age_increase)))
        fields = []
        if girl.flags.birthdayknown:
            fields.append(("birthday", "Birthday:", _lssb_phone_birthday(girl)))
        if girl.is_female:
            if (girl.sub >= 75 or girl.love >= 150) and girl.sexperience > 1:
                fields.append(("contraception", "Birth control:",
                    _lssb_inventory_text("Yes" if girl.flags.pill else "No")))
            if hero.has_skill("fertility_assessment"):
                fields.append(("fertility", "Fertility:", ("Беременна" if _preferences.language == "russian" else _lssb_inventory_text("Pregnant"))
                    if girl.is_visibly_pregnant or girl.flags.toldpreg else str(girl.fertility) + "%"))
        if girl.sexperience >= 1:
            fields.append(("sex_count", "Sex count:", str(girl.sexperience)))
        if girl.flags.mikeBabies or girl.flags.otherBabies:
            fields.append(("babies", "Babies:", str(girl.flags.mikeBabies + girl.flags.otherBabies)))
        job = girl.flags.job
        if job:
            fields.append(("job", "Job:", _lssb_inventory_text(JOBS[job].name)))
        # Let the font layout wrap complete words, rather than inserting breaks
        # from the number of characters in the untranslated strings.
        traits = ", ".join(_lssb_inventory_text(t.replace("_", " ").capitalize()) for t in sorted(girl.traits.known))
        header = [(key, "{b}" + _lssb_npc_label(label) + "{/b} " + value) for key, label, value in header]
        fields = [(key, _lssb_npc_label(label), value,
            max(22, _lssb_npc_text_height(_lssb_npc_label(label), 208, True),
                _lssb_npc_text_height(value, 154))) for key, label, value in fields]
        header_height = max(106, sum(_lssb_npc_text_height(value, 278) for key, value in header) + 4*(len(header)-1))
        content_height = header_height
        if fields:
            content_height += 10 + sum(row[3] for row in fields) + 4*(len(fields)-1)
        if traits:
            content_height += 10 + _lssb_npc_text_height(_lssb_npc_label("Traits"), 376, True) + 4 + _lssb_npc_text_height(traits, 376)
        attributes = [attr.for_ui() for attr in girl.get_attributes() if attr.visible()]
        dating = game.active_date.on_date(girl.id)
        budget = (520 if persistent.new_ui else 430) - 36*(len(attributes) + int(dating))
        panel_height = min(content_height + 28, max(140, budget))
        alt = ". ".join([value for key, value in header] + [label + " " + value for key, label, value, height in fields])
        if traits:
            alt += ". " + _lssb_npc_label("Traits") + ": " + traits
        return header, fields, traits, header_height, panel_height, attributes, dating, alt

    def _lssb_npc_activate():
        _lssb_npc_measure_cache.clear()
        if True:
            if _lssb_npc_variant in config.variants:
                config.variants.remove(_lssb_npc_variant)
            config.variants.insert(0, _lssb_npc_variant)

    for _lssb_npc_language in set(renpy.known_languages()) | {None, "russian"}:
        config.language_callbacks[_lssb_npc_language].append(_lssb_npc_activate)
    _lssb_npc_activate()

style lssb_npc_text is default:
    font "exo2_regular"
    size 16
    line_spacing 2
    layout "tex"
    outlines []

screen npc_info(girl, clear=False):
    variant "lssb_npc_card_26_8_0d"
    $ header, fields, traits, header_height, panel_height, attributes, dating, info_alt = _lssb_npc_information(girl)
    $ text_color = "#ffffff" if clear else gui.text_color
    vbox:
        id "lssb_npc_card"
        if persistent.new_ui:
            at npc_info
        else:
            at npc_info_old_ui
        ypos (90 if persistent.new_ui else 80)
        xsize 420
        spacing 6
        frame:
            id "lssb_npc_panel"
            xysize (420, panel_height)
            padding (0, 0)
            background _LssbInventoryPanel(opacity=".95")
            viewport:
                id "lssb_npc_scroll"
                pos (16, 14)
                xysize (376, panel_height - 28)
                mousewheel True
                draggable True
                arrowkeys True
                pagekeys True
                button:
                    style "empty"
                    action NullAction()
                    keyboard_focus False
                    alt info_alt
                    xsize 376
                    vbox:
                        id "lssb_npc_content"
                        xsize 376
                        fixed:
                            id "lssb_npc_header"
                            xysize (376, header_height)
                            add Transform("gui/id_chibi/" + girl.id + ".png", xysize=(84,106), fit="contain")
                            vbox:
                                xpos 98
                                xsize 278
                                spacing 4
                                for key, value in header:
                                    text value id ("lssb_npc_" + key) style "lssb_npc_text" xsize 278 color text_color substitute False alt ""
                        if fields:
                            null height 10
                            vbox:
                                id "lssb_npc_fields"
                                xsize 376
                                spacing 4
                                for key, label, value, row_height in fields:
                                    fixed:
                                        id ("lssb_npc_row_" + key)
                                        xysize (376, row_height)
                                        text label id ("lssb_npc_label_" + key) style "lssb_npc_text" font "exo2_bold" xsize 208 color text_color substitute False alt ""
                                        text value id ("lssb_npc_value_" + key) style "lssb_npc_text" xpos 222 xsize 154 color text_color substitute False alt ""
                        if traits:
                            null height 10
                            vbox:
                                id "lssb_npc_traits_block"
                                xsize 376
                                spacing 4
                                text _lssb_npc_label("Traits") style "lssb_npc_text" font "exo2_bold" xsize 376 color text_color substitute False alt ""
                                text traits id "lssb_npc_traits" style "lssb_npc_text" xsize 376 color text_color substitute False alt ""
            vbar:
                id "lssb_npc_scrollbar"
                value YScrollValue("lssb_npc_scroll")
                pos (401, 14)
                xysize (5, panel_height - 28)
                unscrollable "hide"
                base_bar Solid("#176984")
                thumb Solid("#c2f0ff")
                thumb_offset 0
        for index, attr_bar_ui in enumerate(attributes):
            fixed:
                id ("lssb_npc_stat_" + str(index))
                xysize (420, 30)
                bar:
                    id ("lssb_npc_vbar_" + str(index))
                    xysize (420, 30)
                    value attr_bar_ui['vbar']['value']
                    range attr_bar_ui['vbar']['range']
                    left_bar _lssb_phone_bar_image("full", 420, 30)
                    right_bar _lssb_phone_bar_image("empty", 420, 30)
                bar:
                    id ("lssb_npc_lbar_" + str(index))
                    xysize (420, 30)
                    value attr_bar_ui['lbar']['value']
                    range attr_bar_ui['lbar']['range']
                    left_bar _lssb_phone_bar_image(attr_bar_ui['lbar']['left'], 420, 30)
                    right_bar _lssb_phone_bar_image(attr_bar_ui['lbar']['right'], 420, 30)
                add attr_bar_ui['icon'] align (0.25, 0.5)
                text attr_bar_ui['text'] align (0.5, 0.5) size 23 color "#ffffff" font "exo2_regular" alt ""
                if attr_bar_ui['lock']:
                    add "gui/icons/icon_lock.png" align (0.87, 0.5)
                button:
                    style "empty"
                    action NullAction()
                    keyboard_focus False
                    alt replace_tags_alt(f"{attr_bar_ui['icon']} {attr_bar_ui['text']} {' is Lock' if attr_bar_ui['lock'] else ''}")
        if dating:
            $ score = max(-100, min(100, game.active_date.score))
            fixed:
                id "lssb_npc_date"
                xysize (420, 30)
                bar value score range 100 xysize (420, 30) left_bar _lssb_phone_bar_image("full", 420, 30) right_bar _lssb_phone_bar_image("empty", 420, 30)
                hbox spacing 10 xalign 0.5:
                    add "gui/icons/icon_dating.png" yalign 1.0
                    text (str(score) + "%") yalign 0.5 size 23 color "#ffffff" font "exo2_regular" alt ""
