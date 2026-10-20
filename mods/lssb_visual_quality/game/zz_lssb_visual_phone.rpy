# Readable phone interface; no gameplay or persistent state changes.
init 1002 python:
    import builtins as _lssb_phone_builtins
    _lssb_phone_variant = "lssb_phone_26_8_0d"
    renpy.image("lssb_phone_shell_home", Image("lssb_visual_quality/phone/shell_home.svg", oversample=4))
    renpy.image("lssb_phone_shell_bar", Image("lssb_visual_quality/phone/shell_bar.svg", oversample=4))

    _lssb_phone_bar_images = {}

    def _lssb_phone_bar_image(kind, width, height=21):
        # Native bars crop the two full-width textures at the value boundary.
        # Supplying old 220px bitmaps to 300px/180px bars clips that geometry.
        # Render each texture at the exact logical width before native cropping.
        key = (kind, width, height)
        if key not in _lssb_phone_bar_images:
            colors = {"full": ("#6eccea", "#409dc3"),
                "empty": ("#177b9a", "#09627d"),
                "locked": ("#738e9a", "#536f7d")}
            svg = '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">' % (width * 4, height * 4, width, height)
            if kind != "thru":
                light, dark = colors[kind]
                svg += ('<defs><linearGradient id="fill" x1="0" y1="0" x2="0" y2="1">'
                    '<stop stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>'
                    '<rect x="1" y="1" width="%d" height="%d" rx="%s" fill="url(#fill)" stroke="#12617d" stroke-width="1.6"/>') % (
                    light, dark, width - 2, height - 2, (height - 2) / 2.0)
            svg += '</svg>'
            _lssb_phone_bar_images[key] = renpy.display.im.Data(svg.encode("utf-8"), "phone_bar.svg", oversample=4)
        return _lssb_phone_bar_images[key]

    class _LssbPhoneButtonBackground(renpy.Displayable):
        def __init__(self, fill, edge):
            super(_LssbPhoneButtonBackground, self).__init__()
            self.fill = fill
            self.edge = edge

        def render(self, width, height, st, at):
            width, height = max(2, int(width)), max(2, int(height))
            if getattr(self, "_size", None) != (width, height):
                svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">'
                    '<rect x="1" y="1" width="%d" height="%d" rx="12" fill="%s" stroke="%s" stroke-width="1.4"/></svg>') % (
                    width * 4, height * 4, width, height, width - 2, height - 2, self.fill, self.edge)
                self._surface = renpy.display.im.Data(svg.encode("utf-8"), "phone_button.svg", oversample=4)
                self._size = (width, height)
            return renpy.render(self._surface, width, height, st, at)

    def _lssb_phone_translate(value):
        if _preferences.language == "russian":
            local = {"Unknown": "Неизвестно", "Text": "Сообщения",
                "Send sexy text": "Флиртующее сообщение",
                "Send dirty text": "Интимное сообщение",
                "Send friendly text": "Дружеское сообщение",
                "Buy the house": "Купить дом",
                "Hire an Investigator": "Нанять детектива"}
            if value in local:
                return local[value]
        return renpy.translation.translate_string(value)

    def _lssb_phone_resize(value, width, size=None):
        if hasattr(store, "_lssb_ui_resize"):
            return _lssb_ui_resize(_lssb_phone_translate(value), width, size or 20)
        return text_tag_resize(_lssb_phone_translate(value), width, size or 20)

    def _lssb_phone_status(person):
        if _preferences.language == "russian" and hasattr(store, "_lssb_ui_status"):
            return _lssb_ui_status(person)
        return _lssb_phone_translate(person.status.capitalize())

    def _lssb_phone_birthday(person):
        birthday = person.birthday
        if not isinstance(birthday, (_lssb_phone_builtins.list, _lssb_phone_builtins.tuple)) or len(birthday) != 2:
            return _lssb_phone_translate("Unknown")
        season, day = birthday
        if not season or str(season).lower() == "unknown":
            return _lssb_phone_translate("Unknown")
        return _lssb_phone_translate(str(season).capitalize()) + ", " + str(day)

    def _lssb_phone_activate():
        if True:
            if _lssb_phone_variant in config.variants:
                config.variants.remove(_lssb_phone_variant)
            config.variants.insert(0, _lssb_phone_variant)

    # The localization changes variants on language selection. Reapply after it.
    for _phone_language in set(renpy.known_languages()) | {None, "russian"}:
        config.language_callbacks[_phone_language].append(_lssb_phone_activate)
    _lssb_phone_activate()

init 1003:
    style lssb_phone_text is smartphone_navigation_text:
        size 18
        xmaximum 350
        layout "greedy"
        line_spacing 2
    style lssb_phone_label_text is smartphone_navigation_label_text:
        size 24
        xmaximum 350
        layout "greedy"
    style lssb_phone_button is smartphone_navigation_button:
        idle_background _LssbPhoneButtonBackground("#419bc0", "#90d7ed")
        hover_background _LssbPhoneButtonBackground("#62b9d7", "#eefaff")
        insensitive_background _LssbPhoneButtonBackground("#326880", "#6997ab")
        xsize 350
        yminimum 40
        ymaximum None
        padding (12, 4)
    style lssb_phone_button_text is smartphone_navigation_button_text:
        size 20
        xpos 0
        xmaximum 326
        layout "greedy"
        line_spacing 0
    style lssb_phone_hbox is smartphone_navigation_hbox
    style lssb_phone_vbox is smartphone_navigation_vbox
    style lssb_phone_frame is empty:
        padding (0, 0)
    

screen smartphone(char=None, selected_screen="home"):
    variant "lssb_phone_26_8_0d"
    predict False

    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Hide("smartphone")
    on "show" action [Hide("story_tracker"), Function(hide_people)]
    on "hide" action Function(show_people)
    default selected_char = char
    default smartphone_screen = selected_screen
    default hide_back = False

    $ hero_contacts = [k for k, v in sorted({i: Person.find(i).name for i in hero.smartphone_contacts if Person.find(i)}.items(), key=lambda x: x[1])]

    $ phone_busy = bool(renpy.get_screen("say") or renpy.get_screen("choice"))
    if not phone_busy:
        if phone_show_hero:
            add hero.layered_image() align (0.3, 1.0)

        if not hide_back and not renpy.variant([ "touch", "android" ]):
            button pos (0, 0) xysize (645, 720) action Hide("smartphone") style "invisible_button" keyboard_focus False
            button pos (1065, 0) xysize (215, 720) action Hide("smartphone") style "invisible_button" keyboard_focus False
        frame:
            id "lssb_phone_shell"
            style_prefix "lssb_phone"
            align (0.75, 0.55)
            xysize (420, 600)
            if smartphone_screen == "home":
                background "lssb_phone_shell_home"
                vbox:
                    xalign 0.5
                    ypos 75
                    ysize 350
                    spacing 10
                    hbox:
                        imagebutton auto "gui/phone/ico_char_%s.png" action SetScreenVariable("smartphone_screen", "character") alt "character" tooltip "" default_focus check_controller()
                        imagebutton auto "gui/phone/ico_contacts_%s.png" action SetScreenVariable("smartphone_screen", "contacts") alt "contacts" tooltip ""
                        imagebutton auto "gui/phone/ico_calendar_%s.png" action SetScreenVariable("smartphone_screen", "calendar") alt "calendar" tooltip ""
                    hbox:
                        if not bool(game.active_date):
                            imagebutton auto "gui/phone/ico_call_%s.png" action SetScreenVariable("smartphone_screen", "call") alt "call" tooltip ""
                            imagebutton auto "gui/phone/ico_messages_%s.png" action SetScreenVariable("smartphone_screen", "text") alt "text" tooltip ""
                        else:
                            imagebutton auto "gui/phone/ico_call_%s.png" action None
                            imagebutton auto "gui/phone/ico_messages_%s.png" action None
                        imagebutton auto "gui/phone/ico_services_%s.png" action SetScreenVariable("smartphone_screen", "services") alt "services" tooltip ""
                    hbox:
                        imagebutton auto "gui/phone/ico_wiki_%s.png" action SetScreenVariable("smartphone_screen", "wiki") alt "wiki" tooltip ""
                        if not game.flags.cheat or config.developer:
                            imagebutton auto "gui/phone/ico_achievements_%s.png" action SetScreenVariable("smartphone_screen", "achievements") alt "achievements" tooltip ""
                            for i in range(1):
                                null:
                                    width 80
                                    height 80
                        else:
                            for i in range(2):
                                null:
                                    width 80
                                    height 80
                    hbox:
                        for i in range(3):
                            null:
                                width 80
                                height 80
                    hbox:
                        for i in range(2):
                            null:
                                width 80
                                height 80
                        if CHEAT:
                            imagebutton auto "gui/phone/ico_cheat_on_%s.png" action SetVariable("CHEAT", False) alt "cheat is on" tooltip ""
                        else:
                            if not game.flags.cheat:
                                imagebutton auto "gui/phone/ico_cheat_off_%s.png" action SetScreenVariable("smartphone_screen", "cheats") alt "open cheat screen" tooltip ""
                            else:

                                imagebutton auto "gui/phone/ico_cheat_off_%s.png" action SetVariable("CHEAT", True) alt "cheat is off" tooltip ""

            elif smartphone_screen == "wiki":
                background "lssb_phone_shell_bar"
                label "Wiki" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (24, 104)
                    xysize (372, 448)
                    vbox spacing 8 xsize 350:
                        text "Hello,"
                        text "If you need help, you can visit the game's wiki page for detailed information and tips."
                        text ""
                        text "You can do so by clicking on the button below."

                    vbox:
                        spacing 3
                        pos (0, 448)
                        yanchor "bottom"
                        box_reverse True
                        textbutton "Back" action SetScreenVariable("smartphone_screen", "home") default_focus check_controller()
                        textbutton "Open web wiki" action OpenURL("https://wiki.andrealphusgames.com/wiki/Love_%26_Sex")

            elif smartphone_screen == "achievements":
                background "lssb_phone_shell_bar"
                label "Achievements ([round((Achievement.total_unlocked / Achievement.total) * 100)]%)" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (24, 104)
                    xysize (372, 448)
                    hbox:
                        viewport id "achievements":
                            draggable True
                            mousewheel True
                            xysize (350, 398)
                            has vbox spacing 5
                            for ach_dict in Achievement.all_sorted_achievements:
                                for ach in ach_dict:
                                    vbox:
                                        hbox:
                                            frame:
                                                style "empty"
                                                xysize (64, 64)
                                                add ach_dict[ach].image xoffset 5
                                                button:
                                                    style "empty"
                                                    action NullAction()
                                                    keyboard_focus False
                                                    alt f'{ach_dict[ach].name} {" unlocked" if ach_dict[ach].has() else " locked"} : {ach_dict[ach].description}'
                                            vbox:
                                                xsize 263
                                                textbutton ach_dict[ach].name:
                                                    style "empty"
                                                    text_size 18
                                                    text_xmaximum 250
                                                    xpos 9
                                                    text_bold True
                                                    action NullAction()
                                                    keyboard_focus False
                                                    alt f'{ach_dict[ach].name} {" unlocked" if ach_dict[ach].has() else " locked"} : {ach_dict[ach].description}'
                                                textbutton ach_dict[ach].description:
                                                    style "empty"
                                                    text_size 17
                                                    text_xmaximum 250
                                                    xoffset 9
                                                    xalign 0.0
                                                    text_italic True
                                                    action NullAction()
                                                    alt f'{ach_dict[ach].name} {" unlocked" if ach_dict[ach].has() else " locked"} : {ach_dict[ach].description}'
                                        null height 2
                                        add "gui/phone/phone_divider.png" xpos 5
                        use scrollbar_phone("achievements")
                    textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 410 default_focus check_controller()

            elif smartphone_screen == "cheats":
                background "lssb_phone_shell_bar"
                label "Cheat" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (24, 104)
                    xysize (372, 448)

                    text "Enabling cheats will disable the New Game+ and Achievements for this game's save.\n\nIf you want to unlock Achievements again, you need to start a new game and play without cheats." pos (0, 0) xmaximum 350
                    vbox:
                        spacing 3
                        pos (0, 448)
                        yanchor "bottom"
                        box_reverse True
                        textbutton "Back" action SetScreenVariable("smartphone_screen", "home") default_focus check_controller()
                        textbutton "I understand" action [SetVariable("CHEAT", True), SetVariable("game.flags.cheat", True), SetScreenVariable("smartphone_screen", "home")]

            elif smartphone_screen == "character":
                background "lssb_phone_shell_bar"
                python:
                    hero_birthday_display_name = _lssb_phone_birthday(hero)
                if hero.is_female:
                    add "bree smartphone" pos (264, 110) zoom 0.55
                else:
                    add "mike smartphone" pos (264, 110) zoom 0.55
                $ luck_value = 3 + hero.luck.val
                add f"gui/icons/icon_clover_small_{luck_value}.png" pos (363, 78) size (25, 25)
                if hero.stamina:
                    add f"gui/icons/icon_stamina_small_{hero.gender}.png" pos (332, 78)
                else:
                    add f"gui/icons/icon_stamina_small_{hero.gender}.png" pos (332, 78) matrixcolor SaturationMatrix(0)
                if hero.flags.pill:
                    add "gui/icons/icon_pill_small.png" pos (302, 78)
                $ heroname_ui = f"{hero.name.upper()} {hero.family_name.upper()}"
                label _lssb_phone_resize(heroname_ui, 300, 24) pos (26, 30) maximum (300, 36) text_layout "nobreak"
                text f"{hero.age + hero.flags.age_increase}" size 18 pos (365, 38) alt ""
                text _lssb_phone_resize(_lssb_phone_status(hero), 268, 18) pos (26, 78) alt ""
                label "Birthday" text_size 17 pos (26, 110) alt ""
                text hero_birthday_display_name pos (26, 138) xmaximum 225 size 17 alt ""
                $ character_self_voicing = f"{heroname_ui} . Status: {hero.status} . Birthday: {hero_birthday_display_name}"
                $ character_self_voicing += f". luck: {luck_value}. stamina: {'ready' if hero.stamina else 'unready'}"
                frame:
                    style "invisible_frame"
                    pos (24, 176)
                    xysize (372, 448)
                    viewport:
                        id "lssb_phone_hero_body"
                        pos (0, 0)
                        xysize (238, 332)
                        mousewheel True
                        draggable True
                        scrollbars "vertical"
                        vscrollbar_xsize 8
                        vscrollbar_base_bar Solid("#226580")
                        vscrollbar_thumb Solid("#b9e8f7")
                        vscrollbar_unscrollable "hide"
                        has vbox
                        box_reverse True
                        yfill False
                        spacing 3
                        xpos 0
                        xsize 220
                        $ attr_bar_ui = None
                        if hero.is_male and Person.is_not_hidden("minami"):
                            $ attr_bar_ui = minami.siscon.for_ui()
                        elif hero.is_female:
                            $ attr_bar_ui = hero.morality.for_ui()
                        if attr_bar_ui is not None:
                            hbox:
                                align (0.0, 1.0)
                                spacing 5
                                add attr_bar_ui['icon']
                                frame:
                                    style "invisible_frame"
                                    xysize (180, 28)
                                    bar:
                                        value attr_bar_ui['vbar']['value']
                                        range attr_bar_ui['vbar']['range']
                                        left_bar _lssb_phone_bar_image("full", 180)
                                        right_bar _lssb_phone_bar_image("empty", 180)
                                        xysize (180, 21)
                                        bar_resizing False
                                    bar:
                                        value attr_bar_ui['lbar']['value']
                                        range attr_bar_ui['lbar']['range']
                                        left_bar _lssb_phone_bar_image(attr_bar_ui["lbar"]["left"], 180)
                                        right_bar _lssb_phone_bar_image(attr_bar_ui["lbar"]["right"], 180)
                                        xysize (180, 21)
                                        bar_resizing False
                                    text attr_bar_ui['text'] align (0.5, 0.5) size 16 alt "" xmaximum 220
                                    if attr_bar_ui['lock']:
                                        add "gui/icons/icon_lock.png" align (0.87, 0.5)
                                    $ character_self_voicing += f". {replace_tags_alt(attr_bar_ui['icon'])} {attr_bar_ui['text']} {' is Lock' if attr_bar_ui['lock'] else ''}"

                        if any(hero.skills):
                            $ t = ", ".join([_lssb_phone_translate(s.display_name) for s in hero.skills])
                            text "{b}Skills:{/b} [t]" size 16 alt "" xmaximum 220
                            $ character_self_voicing += f". Skills: {t}"

                        if game.flags.ngplus and hero.min_sexperience < hero.sexperience:
                            text "{b}Sexperience:{/b} [hero.sexperience] ([hero.min_sexperience])" alt "" xmaximum 220
                            $ character_self_voicing += f". Sexperience: {hero.sexperience} ({hero.min_sexperience})"
                        else:
                            text "{b}Sexperience:{/b} [hero.sexperience]" alt "" xmaximum 220
                            $ character_self_voicing += f". Sexperience: {hero.sexperience}"

                        if hero.children:
                            text "{b}Children:{/b} [hero.children]" alt "" xmaximum 220
                            $ character_self_voicing += f". Children: {hero.children}"


                        $ job_day = game.flags.job_day
                        if not job_day:
                            if hero.is_male and not game.flags.fired:
                                if game.flags.isceo:
                                    $ job_day = "CEO"
                                elif game.flags.promoted:
                                    $ job_day = "Manager"
                                else:
                                    $ job_day = "Code Monkey"
                            else:
                                $ job_day = "Unemployed"
                        if Room.find(job_day) is not None:
                            $ job_day = Room.find(job_day).display_name
                        $ job_night = game.flags.job_night
                        if hero.is_female:
                            if not job_night:
                                $ job_night = "Unemployed"
                            if Room.find(job_night) is not None:
                                $ job_night = Room.find(job_night).display_name
                            text "{b}Job (night):{/b} [job_night]" alt "" xmaximum 220
                        $ character_self_voicing += f". Job (night): {job_night}"
                        text "{b}Job (day):{/b} [job_day]" alt "" xmaximum 220
                        $ character_self_voicing += f". Job (day): {job_day}"

                        if hero.is_female:
                            text "{b}Sex:{/b} Female" alt "" xmaximum 220
                            if hero.is_visibly_pregnant or [guy for guy in Guy.all() if guy.flags.toldpreg]:
                                text "{b}Fertility:{/b} Pregnant" alt "" xmaximum 220
                                $ character_self_voicing += f". Fertility: Pregnant"
                            else:
                                text "{b}Fertility:{/b} [hero.fertility]%" alt "" xmaximum 220
                                $ character_self_voicing += f". Fertility: {hero.fertility}%"
                        else:
                            text "{b}Sex:{/b} Male" alt "" xmaximum 220

                        button:
                            style "empty"
                            xysize (1, 1)
                            action NullAction()
                            keyboard_focus False
                            alt character_self_voicing
                    vbox:
                        pos (0, 338)
                        textbutton "Back" action [SetScreenVariable("selected_char", None), SetScreenVariable("smartphone_screen", "home")] default_focus check_controller()

            elif smartphone_screen == "calendar":
                $ hero_agenda = hero.calendar.get_agenda()
                background "lssb_phone_shell_bar"
                label "Appointments" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (24, 104)
                    xysize (372, 448)
                    hbox:
                        viewport id "calendar":
                            draggable True
                            mousewheel True
                            xysize (350, 398)
                            has vbox spacing 5
                            for entry in hero_agenda:
                                frame:
                                    style "empty"
                                    ysize 50
                                    vbox:
                                        hbox:
                                            xfill True
                                            hbox:
                                                xoffset 18
                                                spacing 5
                                                if entry.day_number:
                                                    text "[entry.day!t] [entry.day_number]" size 19 italic True alt ""
                                                    if entry.season:
                                                        add f"gui/icons/icon_{entry.season}.png" size (18, 18) yalign 0.5 alt ""
                                                else:
                                                    text entry.day size 19 italic True bold True alt ""
                                            text entry.hour size 19 xoffset -18 xalign 1.0 italic True alt ""
                                        text _lssb_phone_resize(entry.name, 314, 19) xpos 18 alt ""
                                        null height 2
                                        add "gui/phone/phone_divider.png" xpos 5
                                    button:
                                        style "empty"
                                        action NullAction()
                                        keyboard_focus False
                                        alt f'{entry.name}: {find_full_day_name(entry.day)} {entry.hour}'
                        use scrollbar_phone("calendar")
                    textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 410 default_focus check_controller()
            elif smartphone_screen == "services":
                python:
                    cleaningservices_status = f'{"✔" if game.flags.cleaningservices else "❌"}'
                    notexting_status = f'{"✔" if game.flags.noTexting else "❌"}'
                    reminders_status = f'{"✔" if game.flags.reminders else "❌"}'
                background "lssb_phone_shell_bar"
                label "Services" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (24, 104)
                    xysize (372, 448)
                    vbox spacing 5:
                        hbox:
                            spacing 0
                            frame:
                                style "empty"
                                xysize (306, 44)
                                label _lssb_phone_resize(" Cleaning ($100/week)", 294) align (0.0, 0.5) alt ""
                                button:
                                    style "empty"
                                    action ToggleVariable("game.flags.cleaningservices", True, False)
                                    alt f'Cleaning ($100/week): {"On" if game.flags.cleaningservices else "Off"}'
                            textbutton cleaningservices_status align (1.0, 0.5) style "story_type_button" action ToggleVariable("game.flags.cleaningservices", True, False) alt f'Cleaning ($100/week): {"On" if game.flags.cleaningservices else "Off"}'

                        hbox:
                            spacing 0
                            frame:
                                style "empty"
                                xysize (306, 44)
                                label _lssb_phone_resize(" Block text messages", 294) align (0.0, 0.5) alt ""
                                button:
                                    style "empty"
                                    action ToggleVariable("game.flags.noTexting", True, False)
                                    alt f'Block text messages: {"On" if game.flags.noTexting else "Off"}'
                            textbutton notexting_status align (1.0, 0.5) style "story_type_button" action ToggleVariable("game.flags.noTexting", True, False) alt f'Block text messages: {"On" if game.flags.noTexting else "Off"}'
                        hbox:
                            spacing 0
                            frame:
                                style "empty"
                                xysize (306, 44)
                                label _lssb_phone_resize(" Reminder notifications", 294) align (0.0, 0.5) alt ""
                                button:
                                    style "empty"
                                    action ToggleVariable("game.flags.reminders", True, False)
                                    alt f'Reminder notifications: {"On" if game.flags.reminders else "Off"}'
                            textbutton reminders_status align (1.0, 0.5) style "story_type_button" action ToggleVariable("game.flags.reminders", True, False) alt f'Reminder notifications: {"On" if game.flags.reminders else "Off"}'

                        text ""
                        if game.flags.hirePI:
                            textbutton _lssb_phone_resize("Hire an Investigator", 270) action [ToggleScreen("smartphone"), Call("call_hire_PI")]
                        if not game.flags.houseowned:
                            textbutton _lssb_phone_resize("Buy the house", 270) action [ToggleScreen("smartphone"), Call("call_buy_house")]
                        else:
                            textbutton _lssb_phone_resize("House rent", 350) action [ToggleScreen("smartphone"), Call("call_house_rules")]
                        if game.flags.debt > 0:
                            textbutton _lssb_phone_resize("Repayment plan", 270) action SetScreenVariable("smartphone_screen", "debt")
                    textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 410 default_focus check_controller()

            elif smartphone_screen == "debt":
                python:
                    debt_owed = int(game.flags.debt)
                    debt_installment = game.get_debt_installment()
                    debt_ceiling = game.get_debt_installment_ceiling()
                    debt_fee = int(game.DEBT_FEE * 100)
                    debt_settlement = game.get_debt_settlement()
                background "lssb_phone_shell_bar"
                label "Repayment plan" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (24, 104)
                    xysize (372, 448)
                    vbox spacing 5:
                        text " Owed: [debt_owed]{image=gui/icons/icon_money.png}" alt f"Owed: {debt_owed}"
                        text " A [debt_fee]% fee is taken out of every payment." size 16 alt f"A {debt_fee}% fee is taken out of every payment."
                        null height 10
                        hbox:
                            spacing 0
                            frame:
                                style "empty"
                                xysize (140, 40)
                                label _lssb_phone_resize(" Weekly payment", 140) align (0.0, 0.5) alt ""
                            textbutton "-" align (0.5, 0.5) style "story_type_button" sensitive debt_installment > game.DEBT_PAYMENT_MIN action Function(game.change_debt_installment, -100) alt f"Lower the weekly payment, currently {debt_installment}"
                            frame:
                                style "empty"
                                xysize (70, 40)
                                text f"{debt_installment}" align (0.5, 0.5) alt ""
                            textbutton "+" align (0.5, 0.5) style "story_type_button" sensitive debt_installment < debt_ceiling action Function(game.change_debt_installment, 100) alt f"Raise the weekly payment, currently {debt_installment}"
                        null height 10
                        textbutton _lssb_phone_resize(f"Pay it all off", 270) sensitive hero.money >= debt_settlement action [Function(game.settle_debt), SetScreenVariable("smartphone_screen", "services")] alt f"Pay it all off, {debt_settlement}"
                    textbutton "Back" action SetScreenVariable("smartphone_screen", "services") ypos 410 default_focus check_controller()

            elif smartphone_screen == "contacts":
                background "lssb_phone_shell_bar"
                label "Contacts" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (24, 104)
                    xysize (372, 448)
                    hbox:
                        viewport id "contacts":
                            draggable True
                            mousewheel True
                            xysize (350, 398)
                            has vbox spacing 5
                            for i in hero_contacts:
                                use contact_name_line(i, True)
                            null height 2
                        use scrollbar_phone("contacts")
                    textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 410 default_focus check_controller()
            elif not selected_char:
                background "lssb_phone_shell_bar"
                label "Contacts" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (24, 104)
                    xysize (372, 448)
                    hbox:
                        viewport id "contacts":
                            draggable True
                            mousewheel True
                            xysize (350, 398)
                            has vbox spacing 5
                            if game.flags.angelaBlow:
                                textbutton "Mom" action [ToggleScreen("smartphone"), Call("angela_afterblow_call")]
                                textbutton "Dad" action [ToggleScreen("smartphone"), Call("angela_afterblow_dad_call")]
                                if game.flags.bruceNumber:
                                    textbutton "Bruce (Bree's dad)" action [ToggleScreen("smartphone"), Call("angela_afterblow_bruce_call")]
                            for i in hero_contacts:
                                if smartphone_screen == "call":
                                    if i not in Room.find(game.room).get_present_girls() and Person.find(i):
                                        if (not Conditioned.done_today("smartphone_call_" + i)
                                            or not Conditioned.done_today("smartphone_booty_call_" + i)
                                            and Room.has_tag(game.room, 'home')):
                                            use contact_name_line(i)
                                elif smartphone_screen == "text":
                                    if (not Conditioned.done_today("smartphone_send_flirty_text_" + i) and hero.charm >= 15
                                        or not Conditioned.done_today("smartphone_send_dirty_text_" + i) and hero.charm >= 30
                                        or not Conditioned.done_today("smartphone_send_friendly_text_" + i)):
                                        use contact_name_line(i)
                                else:
                                    use contact_name_line(i)
                            null height 2
                        use scrollbar_phone("contacts")
                    textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 410 default_focus check_controller()

            else:
                $ info_self_voicing = f"{selected_char.name} . age: {selected_char.age + selected_char.flags.age_increase}"
                background "lssb_phone_shell_bar"
                $ charname_ui = f"{selected_char.name.upper()} {selected_char.family_name.upper()}"
                label _lssb_phone_resize(charname_ui, 300, 24) pos (26, 30)
                text f"{selected_char.age + selected_char.flags.age_increase}" pos (365, 38) alt ""
                if smartphone_screen != "job_change":
                    text _lssb_phone_resize(_lssb_phone_status(selected_char), 350, 18) pos (26, 78) alt ""
                    $ info_self_voicing += f". Status: {selected_char.status}"

                if smartphone_screen == "contact_hub":
                    $ _phone_footer_height = 40 + 44 * (int(selected_char.flags.managecareer) + int(selected_char not in Room.find(game.room).get_present_girls() and not selected_char.hidden and ((not Conditioned.done_today("smartphone_call_" + selected_char.id) or not Conditioned.done_today("smartphone_booty_call_" + selected_char.id) and Room.has_tag(game.room, 'home')) and not bool(game.active_date))) + int(selected_char not in Room.find(game.room).get_present_girls() and not selected_char.hidden and ((not Conditioned.done_today(f"smartphone_send_flirty_text_{selected_char.id}") and hero.charm >= 15 or not Conditioned.done_today(f"smartphone_send_dirty_text_{selected_char.id}") and hero.charm >= 30 or not Conditioned.done_today(f"smartphone_send_friendly_text_{selected_char.id}") and not bool(game.active_date)))))
                    viewport:
                        id "lssb_phone_body"
                        pos (24, 108)
                        xysize (372, 436 - _phone_footer_height)
                        mousewheel True
                        draggable True
                        scrollbars "vertical"
                        vscrollbar_xsize 8
                        vscrollbar_base_bar Solid("#226580")
                        vscrollbar_thumb Solid("#b9e8f7")
                        vscrollbar_unscrollable "hide"
                        has vbox
                        spacing 12
                        xsize 350
                        hbox:
                            spacing 10
                            vbox:
                                xsize 222
                                spacing 6
                                if selected_char.flags.birthdayknown:
                                    label "Birthday:" text_size 17
                                    text _lssb_phone_birthday(selected_char) size 17 xmaximum 222 alt ""
                                    $ info_self_voicing += f". Birthday: {selected_char.birthday_display_name}"
                                $ traits = ", ".join([_lssb_phone_translate(t.replace("_", " ").capitalize()) for t in sorted(selected_char.traits.known)])
                                if len(traits) > 0:
                                    null height 4
                                    label "Traits" text_size 19
                                    text traits size 16 xmaximum 222 alt ""
                                    $ info_self_voicing += f". Traits: {traits}"
                            fixed:
                                xysize (116, 180)
                                add Transform(f"{selected_char.id} smartphone", xysize=(116, 180), fit="contain") id "lssb_phone_portrait"
                                if selected_char.flags.pill and (selected_char.sub >= 75 or selected_char.love >= 150) and selected_char.sexperience > 1:
                                    add "gui/icons/icon_pill_small.png" pos (90, 4)
                                    $ info_self_voicing += ". Take contraceptives pill"
                        vbox:
                            spacing 5
                            for attr in selected_char.get_attributes():
                                if attr.visible():
                                    $ n = attr.scaled_val()
                                    $ m = attr.max
                                    $ mr = attr.scale
                                    $ change_love_icon = isinstance(attr, Love) and bool(selected_char.get_attention_needed())
                                    if change_love_icon:
                                        text "A date or a hot coffee should soften them up." size 13 italic True alt ""
                                    hbox:
                                        yalign 1.0
                                        spacing 4
                                        frame:
                                            style "invisible_frame"
                                            xysize (30, 30)
                                            if change_love_icon:
                                                add "gui/icons/icon_love_angry.png" align (0.5, 0.5)
                                            else:
                                                add attr.get_icon() align (0.5, 0.5)
                                        frame:
                                            style "invisible_frame"
                                            xysize (300, 28)
                                            bar value n range 100 left_bar _lssb_phone_bar_image("full", 300) right_bar _lssb_phone_bar_image("empty", 300) xysize (300, 21) bar_resizing False
                                            bar value m range mr left_bar _lssb_phone_bar_image("thru", 300) right_bar _lssb_phone_bar_image("locked", 300) xysize (300, 21) bar_resizing False
                                            text "[n]%" align (0.5, 0.5) size 16 alt ""
                                            $ info_self_voicing += f". {replace_tags_alt(attr.get_icon())}: {n}% {' is Lock' if attr.is_max else ''}"
                                            if attr.is_max and n < 100:
                                                add "gui/icons/icon_lock.png" align (0.87, 0.5)
                        button:
                            style "empty"
                            xysize (1, 1)
                            action NullAction()
                            keyboard_focus False
                            alt info_self_voicing
                    vbox:
                        id "lssb_phone_actions"
                        spacing 4
                        pos (24, 554)
                        yanchor 1.0
                        $ hub_buttons = []
                        if selected_char not in Room.find(game.room).get_present_girls() and not selected_char.hidden:
                            if ((not Conditioned.done_today("smartphone_call_" + selected_char.id)
                            or not Conditioned.done_today("smartphone_booty_call_" + selected_char.id)
                            and Room.has_tag(game.room, 'home'))
                            and not bool(game.active_date)):
                                textbutton "Call" action [SetScreenVariable("smartphone_screen", "call")]
                            if (((not Conditioned.done_today(f"smartphone_send_flirty_text_{selected_char.id}") and hero.charm >= 15
                            or not Conditioned.done_today(f"smartphone_send_dirty_text_{selected_char.id}") and hero.charm >= 30
                            or not Conditioned.done_today(f"smartphone_send_friendly_text_{selected_char.id}")
                            and not bool(game.active_date)))):
                                $ hub_buttons.append("text")
                        for i in hub_buttons:
                            textbutton _lssb_phone_translate(i.capitalize()) action [SetScreenVariable("smartphone_screen", i)]
                        if selected_char.flags.managecareer:
                            textbutton "Manage" action [SetScreenVariable("smartphone_screen", "manage")]
                        textbutton "Back" action [SetScreenVariable("selected_char", None), SetScreenVariable("smartphone_screen", "contacts")] default_focus check_controller()


                elif smartphone_screen == "call":
                    add Transform(f"{selected_char.id} smartphone", xysize=(200, 230), fit="contain") pos (110, 120)
                    vbox:
                        spacing 3
                        pos (24, 554)
                        yanchor 1.0
                        if selected_char not in Room.find(game.room).get_present_girls() and not selected_char.hidden:
                            if not Conditioned.done_today(f"smartphone_call_{selected_char.id}"):
                                textbutton "Call" action [ToggleScreen("smartphone"), Call("smartphone_call", selected_char)]
                            if (selected_char.id not in ["bree", "sasha", "minami"] or (selected_char.id in ("lexi", "samantha") and Person.find(selected_char.id).flags.schedule != "harem")) and not Conditioned.done_today(f"smartphone_booty_call_{selected_char.id}") and Room.has_tag(game.room, 'home') and game.room != "housemap" and hero.stamina:
                                textbutton "Booty call" action [ToggleScreen("smartphone"), Call("smartphone_booty_call", selected_char)]
                        textbutton "Back" action [SetScreenVariable("smartphone_screen", "contact_hub")] default_focus check_controller()

                elif smartphone_screen == "text":
                    add Transform(f"{selected_char.id} smartphone", xysize=(200, 230), fit="contain") pos (110, 120)
                    vbox:
                        spacing 3
                        pos (24, 554)
                        yanchor 1.0
                        if selected_char not in Room.find(game.room).get_present_girls() and not selected_char.hidden:
                            if not Conditioned.done_today(f"smartphone_send_flirty_text_{selected_char.id}") and hero.charm >= 15 and not selected_char.flags.noFlirtyText and selected_char.flags.kiss >= 1:
                                textbutton _lssb_phone_translate("Send sexy text") action [ToggleScreen("smartphone"), Call("smartphone_send_flirty_text", selected_char)]
                            if not Conditioned.done_today(f"smartphone_send_dirty_text_{selected_char.id}") and hero.charm >= 30 and not selected_char.flags.noDirtyText and selected_char.sexperience >= 1:
                                textbutton _lssb_phone_translate("Send dirty text") action [ToggleScreen("smartphone"), Call("smartphone_send_dirty_text", selected_char)]
                            if not Conditioned.done_today(f"smartphone_send_friendly_text_{selected_char.id}") and not selected_char.flags.noFriendlyText:
                                textbutton _lssb_phone_resize("Send friendly text", 270) action [ToggleScreen("smartphone"), Call("smartphone_send_friendly_text", selected_char)]
                        textbutton "Back" action [SetScreenVariable("smartphone_screen", "contact_hub")] default_focus check_controller()

                elif smartphone_screen == "manage":
                    python:

                        m_job = JOBS.get(selected_char.flags.job)
                        m_lines = [f"{{b}}Career{{/b}}  {selected_char.career.val} / 100"]
                        if m_job:
                            m_gain, m_days = m_job.daily_gain(selected_char)
                            m_lines.append(f"{{b}}Job{{/b}}  {m_job.name} · {{color={m_job.readiness_color(selected_char)}}}{m_job.readiness_label(selected_char)}{{/color}}")
                            m_lines.append(f"{{b}}Pay{{/b}}  {m_job.weekly_income(selected_char)}/wk · my cut {m_job.agent_cut(selected_char)}%")
                            m_lines.append(f"{{b}}Growth{{/b}}  +{m_gain} on {len(m_days)} days · caps at {m_job.career_max}")
                        else:
                            m_lines.append("{b}Job{/b}  None")
                        m_coach = "150/wk" if selected_char.flags.coach else "none"
                        m_loan = selected_char.flags.jobloan or "none"
                        m_lines.append(f"{{b}}Coach{{/b}}  {m_coach}    {{b}}Loan{{/b}}  {m_loan}")
                        if m_job:
                            m_lines.append("")
                            m_lines.append(f"{{size=15}}{m_job.description}{{/size}}")
                    frame:
                        style "invisible_frame"
                        pos (26, 100)
                        maximum (350, 300)
                        has vbox
                        spacing 1
                        for m_line in m_lines:
                            text m_line size 17 xalign 0.0 alt ""
                    vbox:


                        spacing 3
                        xpos 24
                        yanchor "bottom"
                        ypos 554
                        textbutton "Look for jobs" action [Call("smartphone_look_for_jobs", selected_char)]
                        textbutton "Change jobs" action [SetScreenVariable("smartphone_screen", "job_change")]
                        if selected_char.flags.job:
                            textbutton "Act" action [SetScreenVariable("smartphone_screen", "manage_act")]
                        textbutton "Back" action [SetScreenVariable("smartphone_screen", "contact_hub")] default_focus check_controller()

                elif smartphone_screen == "manage_act":
                    python:

                        a_job = JOBS.get(selected_char.flags.job)
                        a_tier = a_job.tier if a_job else 0
                        a_portfolio = 250 * max(1, a_tier)
                        a_can_pitch = game.week_day <= 5 and 9 <= game.hour < 18 and not Conditioned.done_this_week(f"smartphone_agent_pitch_{selected_char.id}")
                        a_can_portfolio = (selected_char.flags.portfolio_tier or 0) <= a_tier and hero.money >= a_portfolio
                        a_can_negotiate = bool(a_job) and selected_char.flags.rate_job != selected_char.flags.job
                        a_can_campaign = (selected_char.flags.campaign_tier or 0) <= a_tier and not selected_char.flags.jobloan
                        a_coach_label = "Cancel the coach" if selected_char.flags.coach else "Hire a coach (150/wk)"
                    frame:
                        style "invisible_frame"
                        pos (24, 110)
                        maximum (372, 430)
                        hbox:
                            viewport id "manage_act":
                                draggable True
                                mousewheel True
                                xysize (350, 370)
                                has vbox
                                spacing 3
                                xpos 6
                                textbutton _lssb_phone_resize("Pitch her to a client (1h)", 350) sensitive a_can_pitch action [ToggleScreen("smartphone"), Call("smartphone_agent_pitch", selected_char)]
                                textbutton _lssb_phone_resize(f"Book a portfolio shoot ({a_portfolio})", 350) sensitive a_can_portfolio action [ToggleScreen("smartphone"), Call("smartphone_agent_portfolio", selected_char)]
                                textbutton _lssb_phone_resize("Negotiate her rate (1h)", 350) sensitive a_can_negotiate action [ToggleScreen("smartphone"), Call("smartphone_agent_negotiate", selected_char)]
                                textbutton _lssb_phone_resize(a_coach_label, 350) action [ToggleScreen("smartphone"), Call("smartphone_agent_coach", selected_char)]
                                textbutton _lssb_phone_resize("Front a campaign (1000 loan)", 350) sensitive a_can_campaign action [ToggleScreen("smartphone"), Call("smartphone_agent_campaign", selected_char)]
                                textbutton _lssb_phone_resize("Set my cut", 350) action [ToggleScreen("smartphone"), Call("smartphone_agent_setcut", selected_char)]
                            use scrollbar_phone("manage_act")
                        textbutton "Back" action [SetScreenVariable("smartphone_screen", "manage")] ypos 410 default_focus check_controller()

                elif smartphone_screen == "job_change":
                    python:
                        jobs = []

                        alljobs = AVAILABLE_JOBS.get(selected_char.id)
                        if not alljobs:
                            alljobs = []
                            AVAILABLE_JOBS[selected_char.id] = []
                        for job in alljobs:
                            jobs.append(job)
                    frame:
                        style "invisible_frame"
                        pos (24, 110)
                        maximum (372, 430)
                        hbox:
                            viewport id "job_change":
                                draggable True
                                mousewheel True
                                xysize (350, 370)
                                has vbox
                                spacing 3
                                xpos 6
                                yalign 0.85
                                for job in jobs:
                                    python:
                                        j = JOBS[job]
                                        j_gain, j_days = j.daily_gain(selected_char)

                                        j_risk = j.readiness_label(selected_char).replace(" ", "\N{NO-BREAK SPACE}")
                                        j_line = f"{_lssb_phone_resize(j.name, 225)}\n{{size=14}}{j.weekly_income(selected_char)}/wk · +{j_gain}/day · cap {j.career_max} · {{color={j.readiness_color(selected_char)}}}{j_risk}{{/color}}{{/size}}"
                                    if selected_char.flags.job == job:
                                        textbutton j_line style "smartphone_tall_button"
                                    else:
                                        textbutton j_line style "smartphone_tall_button" action [SetScreenVariable("smartphone_screen", "manage"), Call("smartphone_change_job", selected_char, job)]

                            use scrollbar_phone("job_change")
                        textbutton "Back" action [SetScreenVariable("smartphone_screen", "manage")] ypos 410 default_focus check_controller()

screen contact_name_line(name, return_hub=False):
    variant "lssb_phone_26_8_0d"
    frame:
        xpos 0
        style "invisible_frame"
        xysize (350, 40)


        has button
        style "lssb_phone_button"
        xysize (350, 40)
        if return_hub:
            action [SetScreenVariable("selected_char", Person.find(name)), SetScreenVariable("smartphone_screen", "contact_hub")]
        else:
            action [SetScreenVariable("selected_char", Person.find(name))]


        text _lssb_phone_resize(Person.find(name).name, 292, 20) style "lssb_phone_button_text" xpos 0 xmaximum 294 yalign 0.5


        $ path_icon = f"gui/action_icons/button_" + Person.find(name).id + ".png"
        if renpy.exists(path_icon):
            add path_icon pos (296, -2) size (35, 35)

