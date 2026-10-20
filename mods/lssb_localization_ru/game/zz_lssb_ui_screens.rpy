# Russian-only screen variants for game 26.8.0d.

screen smartphone(char=None, selected_screen="home"):
    variant "lssb_ui_ru_26_8_0d"
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
            button pos (0, 0) xysize (730, 720) action Hide("smartphone") style "invisible_button" keyboard_focus False
            button pos (1100, 0) xysize (180, 720) action Hide("smartphone") style "invisible_button" keyboard_focus False
        frame:
            style_prefix "smartphone_navigation"
            align (0.75, 0.7)
            xysize (313, 573)
            if smartphone_screen == "home":
                background "gui/phone/phone_bg_home.png"
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
                background "gui/phone/phone_bg_bar.png"
                label "Wiki" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (1, 85)
                    maximum (290, 370)
                    vbox spacing 5 xoffset 10:
                        text "Hello,"
                        text "If you need help, you can visit the game's wiki page for detailed information and tips."
                        text ""
                        text "You can do so by clicking on the button below."

                    vbox:
                        spacing 3
                        pos (0, 400)
                        yanchor "bottom"
                        box_reverse True
                        textbutton "Back" action SetScreenVariable("smartphone_screen", "home") default_focus check_controller()
                        textbutton "Open web wiki" action OpenURL("https://wiki.andrealphusgames.com/wiki/Love_%26_Sex")

            elif smartphone_screen == "achievements":
                background "gui/phone/phone_bg_bar.png"
                label "Achievements ([round((Achievement.total_unlocked / Achievement.total) * 100)]%)" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (1, 85)
                    maximum (290, 370)
                    hbox:
                        viewport id "achievements":
                            draggable True
                            mousewheel True
                            xysize (270, 370)
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
                                                xsize 195
                                                textbutton ach_dict[ach].name:
                                                    style "empty"
                                                    text_size 18
                                                    xpos 9
                                                    text_bold True
                                                    action NullAction()
                                                    keyboard_focus False
                                                    alt f'{ach_dict[ach].name} {" unlocked" if ach_dict[ach].has() else " locked"} : {ach_dict[ach].description}'
                                                textbutton ach_dict[ach].description:
                                                    style "empty"
                                                    text_size 17
                                                    xoffset 9
                                                    xalign 0.0
                                                    text_italic True
                                                    action NullAction()
                                                    alt f'{ach_dict[ach].name} {" unlocked" if ach_dict[ach].has() else " locked"} : {ach_dict[ach].description}'
                                        null height 2
                                        add "gui/phone/phone_divider.png" xpos 5
                        use scrollbar_phone("achievements")
                    textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 375 default_focus check_controller()

            elif smartphone_screen == "cheats":
                background "gui/phone/phone_bg_bar.png"
                label "Cheat" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (1, 85)
                    maximum (290, 370)

                    text "Enabling cheats will disable the New Game+ and Achievements for this game's save.\n\nIf you want to unlock Achievements again, you need to start a new game and play without cheats." pos (10, 0)
                    vbox:
                        spacing 3
                        pos (0, 400)
                        yanchor "bottom"
                        box_reverse True
                        textbutton "Back" action SetScreenVariable("smartphone_screen", "home") default_focus check_controller()
                        textbutton "I understand" action [SetVariable("CHEAT", True), SetVariable("game.flags.cheat", True), SetScreenVariable("smartphone_screen", "home")]

            elif smartphone_screen == "character":
                background "gui/phone/phone_bg_bar.png"
                python:
                    hero_birthday_display_name = _lssb_ui_birthday(hero)
                if hero.is_female:
                    add "bree smartphone" pos (100, 85)
                else:
                    add "mike smartphone" pos (100, 85)
                $ luck_value = 3 + hero.luck.val
                add f"gui/icons/icon_clover_small_{luck_value}.png" pos (250, 75) size (25, 25)
                if hero.stamina:
                    add f"gui/icons/icon_stamina_small_{hero.gender}.png" pos (220, 75)
                else:
                    add f"gui/icons/icon_stamina_small_{hero.gender}.png" pos (220, 75) matrixcolor SaturationMatrix(0)
                if hero.flags.pill:
                    add "gui/icons/icon_pill_small.png" pos 190, 75
                $ heroname_ui = f"{hero.name.upper()} {hero.family_name.upper()}"
                label _lssb_ui_resize(heroname_ui, 222, style.smartphone_label_text.size) pos (26, 30) maximum (220, 20) text_layout "nobreak"
                text f"{hero.age + hero.flags.age_increase}" size 18 pos (249, 41) alt ""
                text _lssb_ui_status(hero) pos (30, 70) alt ""
                label "Birthday" text_size 21 pos (30, 85) alt ""
                text hero_birthday_display_name pos (30, 114) alt ""
                $ character_self_voicing = f"{heroname_ui} . Status: {hero.status} . Birthday: {hero_birthday_display_name}"
                $ character_self_voicing += f". luck: {luck_value}. stamina: {'ready' if hero.stamina else 'unready'}"
                frame:
                    style "invisible_frame"
                    pos (1, 130)
                    xysize (290, 370)
                    has vbox
                    yalign 1.0
                    spacing 3
                    vbox:
                        box_reverse True
                        spacing 3
                        xpos 20
                        xmaximum 270
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
                                    xysize (220, 28)
                                    bar:
                                        value attr_bar_ui['vbar']['value']
                                        range attr_bar_ui['vbar']['range']
                                        left_bar "gui/phone/bar_full.png"
                                        right_bar "gui/phone/bar_empty.png"
                                        ymaximum 21
                                    bar:
                                        value attr_bar_ui['lbar']['value']
                                        range attr_bar_ui['lbar']['range']
                                        left_bar f"gui/phone/bar_{attr_bar_ui['lbar']['left']}.png"
                                        right_bar f"gui/phone/bar_{attr_bar_ui['lbar']['right']}.png"
                                        ymaximum 21
                                    text attr_bar_ui['text'] align (0.5, 0.5) size 16 alt ""
                                    if attr_bar_ui['lock']:
                                        add "gui/icons/icon_lock.png" align (0.87, 0.5)
                                    $ character_self_voicing += f". {replace_tags_alt(attr_bar_ui['icon'])} {attr_bar_ui['text']} {' is Lock' if attr_bar_ui['lock'] else ''}"

                        if any(hero.skills):
                            $ t = ", ".join([_lssb_ui_translate(s.display_name) for s in hero.skills])
                            text "{b}Skills:{/b} [t]" size 16 alt ""
                            $ character_self_voicing += f". Skills: {t}"

                        if game.flags.ngplus and hero.min_sexperience < hero.sexperience:
                            text "{b}Sexperience:{/b} [hero.sexperience] ([hero.min_sexperience])" alt ""
                            $ character_self_voicing += f". Sexperience: {hero.sexperience} ({hero.min_sexperience})"
                        else:
                            text "{b}Sexperience:{/b} [hero.sexperience]" alt ""
                            $ character_self_voicing += f". Sexperience: {hero.sexperience}"

                        if hero.children:
                            text "{b}Children:{/b} [hero.children]" alt ""
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
                            text "{b}Job (night):{/b} [job_night]" alt ""
                        $ character_self_voicing += f". Job (night): {job_night}"
                        text "{b}Job (day):{/b} [job_day]" alt ""
                        $ character_self_voicing += f". Job (day): {job_day}"

                        if hero.is_female:
                            text "{b}Sex:{/b} Female" alt ""
                            if hero.is_visibly_pregnant or [guy for guy in Guy.all() if guy.flags.toldpreg]:
                                text "{b}Fertility:{/b} Pregnant" alt ""
                                $ character_self_voicing += f". Fertility: Pregnant"
                            else:
                                text "{b}Fertility:{/b} [hero.fertility]%" alt ""
                                $ character_self_voicing += f". Fertility: {hero.fertility}%"
                        else:
                            text "{b}Sex:{/b} Male" alt ""

                        button:
                            style "empty"
                            action NullAction()
                            keyboard_focus False
                            alt character_self_voicing
                    vbox:
                        yalign 1.0
                        text " "
                        textbutton "Back" action [SetScreenVariable("selected_char", None), SetScreenVariable("smartphone_screen", "home")] default_focus check_controller()

            elif smartphone_screen == "calendar":
                $ hero_agenda = hero.calendar.get_agenda()
                background "gui/phone/phone_bg_bar.png"
                label "Appointments" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (1, 85)
                    maximum (290, 370)
                    hbox:
                        viewport id "calendar":
                            draggable True
                            mousewheel True
                            xysize (270, 370)
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
                                        text _lssb_ui_resize(entry.name, 350, 19) xpos 18 alt ""
                                        null height 2
                                        add "gui/phone/phone_divider.png" xpos 5
                                    button:
                                        style "empty"
                                        action NullAction()
                                        keyboard_focus False
                                        alt f'{entry.name}: {find_full_day_name(entry.day)} {entry.hour}'
                        use scrollbar_phone("calendar")
                    textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 375 default_focus check_controller()
            elif smartphone_screen == "services":
                python:
                    cleaningservices_status = f'{"✔" if game.flags.cleaningservices else "❌"}'
                    notexting_status = f'{"✔" if game.flags.noTexting else "❌"}'
                    reminders_status = f'{"✔" if game.flags.reminders else "❌"}'
                background "gui/phone/phone_bg_bar.png"
                label "Services" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (1, 85)
                    xysize (290, 370)
                    vbox spacing 5:
                        hbox:
                            spacing 0
                            frame:
                                style "empty"
                                xysize (240, 40)
                                label _lssb_ui_resize(" Cleaning ($100/week)", 240) align (0.0, 0.5) alt ""
                                button:
                                    style "empty"
                                    action ToggleVariable("game.flags.cleaningservices", True, False)
                                    alt f'Cleaning ($100/week): {"On" if game.flags.cleaningservices else "Off"}'
                            textbutton cleaningservices_status align (1.0, 0.5) style "story_type_button" action ToggleVariable("game.flags.cleaningservices", True, False) alt f'Cleaning ($100/week): {"On" if game.flags.cleaningservices else "Off"}'

                        hbox:
                            spacing 0
                            frame:
                                style "empty"
                                xysize (240, 40)
                                label _lssb_ui_resize(" Block text messages", 240) align (0.0, 0.5) alt ""
                                button:
                                    style "empty"
                                    action ToggleVariable("game.flags.noTexting", True, False)
                                    alt f'Block text messages: {"On" if game.flags.noTexting else "Off"}'
                            textbutton notexting_status align (1.0, 0.5) style "story_type_button" action ToggleVariable("game.flags.noTexting", True, False) alt f'Block text messages: {"On" if game.flags.noTexting else "Off"}'
                        hbox:
                            spacing 0
                            frame:
                                style "empty"
                                xysize (240, 40)
                                label _lssb_ui_resize(" Reminder notifications", 240) align (0.0, 0.5) alt ""
                                button:
                                    style "empty"
                                    action ToggleVariable("game.flags.reminders", True, False)
                                    alt f'Reminder notifications: {"On" if game.flags.reminders else "Off"}'
                            textbutton reminders_status align (1.0, 0.5) style "story_type_button" action ToggleVariable("game.flags.reminders", True, False) alt f'Reminder notifications: {"On" if game.flags.reminders else "Off"}'

                        text ""
                        if game.flags.hirePI:
                            textbutton _lssb_ui_resize("Hire an Investigator", 270) action [ToggleScreen("smartphone"), Call("call_hire_PI")]
                        if not game.flags.houseowned:
                            textbutton _lssb_ui_resize("Buy the house", 270) action [ToggleScreen("smartphone"), Call("call_buy_house")]
                        else:
                            textbutton _lssb_ui_resize("House rent", 270) action [ToggleScreen("smartphone"), Call("call_house_rules")]
                        if game.flags.debt > 0:
                            textbutton _lssb_ui_resize("Repayment plan", 270) action SetScreenVariable("smartphone_screen", "debt")
                    textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 375 default_focus check_controller()

            elif smartphone_screen == "debt":
                python:
                    debt_owed = int(game.flags.debt)
                    debt_installment = game.get_debt_installment()
                    debt_ceiling = game.get_debt_installment_ceiling()
                    debt_fee = int(game.DEBT_FEE * 100)
                    debt_settlement = game.get_debt_settlement()
                background "gui/phone/phone_bg_bar.png"
                label "Repayment plan" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (1, 85)
                    xysize (290, 370)
                    vbox spacing 5:
                        text " Owed: [debt_owed]{image=gui/icons/icon_money.png}" alt f"Owed: {debt_owed}"
                        text " A [debt_fee]% fee is taken out of every payment." size 16 alt f"A {debt_fee}% fee is taken out of every payment."
                        null height 10
                        hbox:
                            spacing 0
                            frame:
                                style "empty"
                                xysize (140, 40)
                                label _lssb_ui_resize(" Weekly payment", 140) align (0.0, 0.5) alt ""
                            textbutton "-" align (0.5, 0.5) style "story_type_button" sensitive debt_installment > game.DEBT_PAYMENT_MIN action Function(game.change_debt_installment, -100) alt f"Lower the weekly payment, currently {debt_installment}"
                            frame:
                                style "empty"
                                xysize (70, 40)
                                text f"{debt_installment}" align (0.5, 0.5) alt ""
                            textbutton "+" align (0.5, 0.5) style "story_type_button" sensitive debt_installment < debt_ceiling action Function(game.change_debt_installment, 100) alt f"Raise the weekly payment, currently {debt_installment}"
                        null height 10
                        textbutton _lssb_ui_resize(f"Pay it all off", 270) sensitive hero.money >= debt_settlement action [Function(game.settle_debt), SetScreenVariable("smartphone_screen", "services")] alt f"Pay it all off, {debt_settlement}"
                    textbutton "Back" action SetScreenVariable("smartphone_screen", "services") ypos 375 default_focus check_controller()

            elif smartphone_screen == "contacts":
                background "gui/phone/phone_bg_bar.png"
                label "Contacts" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (1, 85)
                    maximum (290, 370)
                    hbox:
                        viewport id "contacts":
                            draggable True
                            mousewheel True
                            maximum (270, 370)
                            has vbox spacing 5
                            for i in hero_contacts:
                                use contact_name_line(i, True)
                            null height 2
                        use scrollbar_phone("contacts")
                    textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 375 default_focus check_controller()
            elif not selected_char:
                background "gui/phone/phone_bg_bar.png"
                label "Contacts" pos (26, 30)
                frame:
                    style "invisible_frame"
                    pos (1, 85)
                    maximum (290, 370)
                    hbox:
                        viewport id "contacts":
                            draggable True
                            mousewheel True
                            maximum (270, 370)
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
                    textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 375 default_focus check_controller()

            else:
                $ info_self_voicing = f"{selected_char.name} . age: {selected_char.age + selected_char.flags.age_increase}"
                background "gui/phone/phone_bg_bar.png"
                $ charname_ui = f"{selected_char.name.upper()} {selected_char.family_name.upper()}"[0:13]
                label charname_ui pos (26, 30)
                text f"{selected_char.age + selected_char.flags.age_increase}" pos (248, 38) alt ""
                if smartphone_screen != "job_change":
                    text _lssb_ui_status(selected_char) pos (30, 70) alt ""
                    $ info_self_voicing += f". Status: {selected_char.status}"

                if smartphone_screen == "contact_hub":
                    if smartphone_screen not in ["manage", "job_change"]:
                        add f"{selected_char.id} smartphone" pos (100, 85)
                        if selected_char.flags.pill and (selected_char.sub >= 75 or selected_char.love >= 150) and selected_char.sexperience > 1:
                            add "gui/icons/icon_pill_small.png" pos (250, 75)
                            $ info_self_voicing += ". Take contraceptives pill"
                        if selected_char.flags.birthdayknown:
                            hbox:
                                spacing 4
                                pos (30, 85)
                                label "Birthday:" text_size 21 align (0.5, 0.5)
                                text _lssb_ui_birthday(selected_char) align (0.5, 0.6) alt ""
                            $ info_self_voicing += f". Birthday: {selected_char.birthday_display_name}"
                    vbox:
                        yanchor "bottom"
                        ypos 500
                        spacing 4
                        vbox:
                            spacing 3
                            xpos 6
                            box_reverse True
                            frame:
                                style "invisible_frame"
                                maximum (290, 370)
                                vbox:
                                    xpos 10
                                    yalign 1.0
                                    $ traits = ", ".join([_lssb_ui_translate(t.replace("_", " ").capitalize()) for t in sorted(selected_char.traits.known)])
                                    if len(traits) > 0:
                                        vbox:
                                            xpos 10
                                            xsize 220
                                            spacing -7
                                            label "Traits" text_size 21
                                            text traits alt ""
                                            $ info_self_voicing += f". Traits: {traits}"
                                    null height 10
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
                                                    xysize (220, 28)
                                                    bar value n range 100 left_bar "gui/phone/bar_full.png" right_bar "gui/phone/bar_empty.png" ymaximum 21
                                                    bar value m range mr left_bar "gui/phone/bar_thru.png" right_bar "gui/phone/bar_locked.png" ymaximum 21
                                                    text "[n]%" align (0.5, 0.5) size 16 alt ""
                                                    $ info_self_voicing += f". {replace_tags_alt(attr.get_icon())}: {n}% {' is Lock' if attr.is_max else ''}"
                                                    if attr.is_max and n < 100:
                                                        add "gui/icons/icon_lock.png" align (0.87, 0.5)
                                button:
                                    style "empty"
                                    action NullAction()
                                    keyboard_focus False
                                    alt info_self_voicing
                        vbox:
                            spacing 3
                            xpos 6
                            $ hub_buttons = []
                            if selected_char not in Room.find(game.room).get_present_girls() and not selected_char.hidden:
                                if ((not Conditioned.done_today("smartphone_call_" + selected_char.id)
                                or not Conditioned.done_today("smartphone_booty_call_" + selected_char.id)
                                and Room.has_tag(game.room, 'home'))
                                and not bool(game.active_date)):
                                    textbutton "Call" action [SetScreenVariable("smartphone_screen", "call")] idle_background "gui/phone/empty_short_idle.png" hover_background "gui/phone/empty_short_hover.png" insensitive_background "gui/phone/empty_short_insensitive.png" xminimum 275
                                if (((not Conditioned.done_today(f"smartphone_send_flirty_text_{selected_char.id}") and hero.charm >= 15
                                or not Conditioned.done_today(f"smartphone_send_dirty_text_{selected_char.id}") and hero.charm >= 30
                                or not Conditioned.done_today(f"smartphone_send_friendly_text_{selected_char.id}")
                                and not bool(game.active_date)))):
                                    $ hub_buttons.append("text")
                            for i in hub_buttons:
                                textbutton i.capitalize() action [SetScreenVariable("smartphone_screen", i)]
                            if selected_char.flags.managecareer:
                                textbutton "Manage" action [SetScreenVariable("smartphone_screen", "manage")]
                            textbutton "Back" action [SetScreenVariable("selected_char", None), SetScreenVariable("smartphone_screen", "contacts")] default_focus check_controller()

                elif smartphone_screen == "call":
                    add f"{selected_char.id} smartphone" pos (100, 85)
                    vbox:
                        spacing 3
                        xpos 6
                        yalign 0.83
                        if selected_char not in Room.find(game.room).get_present_girls() and not selected_char.hidden:
                            if not Conditioned.done_today(f"smartphone_call_{selected_char.id}"):
                                textbutton "Call" action [ToggleScreen("smartphone"), Call("smartphone_call", selected_char)]
                            if (selected_char.id not in ["bree", "sasha", "minami"] or (selected_char.id in ("lexi", "samantha") and Person.find(selected_char.id).flags.schedule != "harem")) and not Conditioned.done_today(f"smartphone_booty_call_{selected_char.id}") and Room.has_tag(game.room, 'home') and game.room != "housemap" and hero.stamina:
                                textbutton "Booty call" action [ToggleScreen("smartphone"), Call("smartphone_booty_call", selected_char)]
                        textbutton "Back" action [SetScreenVariable("smartphone_screen", "contact_hub")] default_focus check_controller()

                elif smartphone_screen == "text":
                    add f"{selected_char.id} smartphone" pos (100, 85)
                    vbox:
                        spacing 3
                        xpos 6
                        yalign 0.85
                        if selected_char not in Room.find(game.room).get_present_girls() and not selected_char.hidden:
                            if not Conditioned.done_today(f"smartphone_send_flirty_text_{selected_char.id}") and hero.charm >= 15 and not selected_char.flags.noFlirtyText and selected_char.flags.kiss >= 1:
                                textbutton "Send sexy text" action [ToggleScreen("smartphone"), Call("smartphone_send_flirty_text", selected_char)]
                            if not Conditioned.done_today(f"smartphone_send_dirty_text_{selected_char.id}") and hero.charm >= 30 and not selected_char.flags.noDirtyText and selected_char.sexperience >= 1:
                                textbutton "Send dirty text" action [ToggleScreen("smartphone"), Call("smartphone_send_dirty_text", selected_char)]
                            if not Conditioned.done_today(f"smartphone_send_friendly_text_{selected_char.id}") and not selected_char.flags.noFriendlyText:
                                textbutton _lssb_ui_resize("Send friendly text", 270) action [ToggleScreen("smartphone"), Call("smartphone_send_friendly_text", selected_char)]
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
                        pos (26, 92)
                        maximum (260, 200)
                        has vbox
                        spacing 1
                        for m_line in m_lines:
                            text m_line size 17 xalign 0.0 alt ""
                    vbox:


                        spacing 3
                        xpos 6
                        yanchor "bottom"
                        ypos 500
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
                        pos (1, 85)
                        maximum (290, 370)
                        hbox:
                            viewport id "manage_act":
                                draggable True
                                mousewheel True
                                xmaximum 270
                                has vbox
                                spacing 3
                                xpos 6
                                textbutton text_tag_resize("Pitch her to a client (1h)", 270) sensitive a_can_pitch action [ToggleScreen("smartphone"), Call("smartphone_agent_pitch", selected_char)]
                                textbutton text_tag_resize(f"Book a portfolio shoot ({a_portfolio})", 270) sensitive a_can_portfolio action [ToggleScreen("smartphone"), Call("smartphone_agent_portfolio", selected_char)]
                                textbutton text_tag_resize("Negotiate her rate (1h)", 270) sensitive a_can_negotiate action [ToggleScreen("smartphone"), Call("smartphone_agent_negotiate", selected_char)]
                                textbutton text_tag_resize(a_coach_label, 270) action [ToggleScreen("smartphone"), Call("smartphone_agent_coach", selected_char)]
                                textbutton text_tag_resize("Front a campaign (1000 loan)", 270) sensitive a_can_campaign action [ToggleScreen("smartphone"), Call("smartphone_agent_campaign", selected_char)]
                                textbutton text_tag_resize("Set my cut", 270) action [ToggleScreen("smartphone"), Call("smartphone_agent_setcut", selected_char)]
                            use scrollbar_phone("manage_act")
                        textbutton "Back" action [SetScreenVariable("smartphone_screen", "manage")] ypos 370 default_focus check_controller()

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
                        pos (1, 85)
                        maximum (290, 370)
                        hbox:
                            viewport id "job_change":
                                draggable True
                                mousewheel True
                                xmaximum 270
                                has vbox
                                spacing 3
                                xpos 6
                                yalign 0.85
                                for job in jobs:
                                    python:
                                        j = JOBS[job]
                                        j_gain, j_days = j.daily_gain(selected_char)

                                        j_risk = j.readiness_label(selected_char).replace(" ", "\N{NO-BREAK SPACE}")
                                        j_line = f"{text_tag_resize(j.name, 225)}\n{{size=14}}{j.weekly_income(selected_char)}/wk · +{j_gain}/day · cap {j.career_max} · {{color={j.readiness_color(selected_char)}}}{j_risk}{{/color}}{{/size}}"
                                    if selected_char.flags.job == job:
                                        textbutton j_line style "smartphone_tall_button"
                                    else:
                                        textbutton j_line style "smartphone_tall_button" action [SetScreenVariable("smartphone_screen", "manage"), Call("smartphone_change_job", selected_char, job)]

                            use scrollbar_phone("job_change")
                        textbutton "Back" action [SetScreenVariable("smartphone_screen", "manage")] ypos 370 default_focus check_controller()

screen npc_info(girl, clear=False):
    variant "lssb_ui_ru_26_8_0d"
    vbox:
        if persistent.new_ui:
            at npc_info
        else:
            at npc_info_old_ui
        xsize 313
        ypos 150
        spacing 5
        frame:
            $ text_displayed = 0
            $ info_self_voicing = ""
            background "gui/npc_info_bg.png"
            xysize (313, 215)
            add f"gui/id_chibi/{girl.id}.png" ypos 10 xpos 15
            vbox:
                xsize 313
                hbox:
                    ypos 5
                    xalign 1.0
                    xysize (200, 120)
                    yfill True
                    xfill True
                    vbox:
                        if clear:
                            $ text_color = "#FFFFFF"
                        else:
                            $ text_color = gui.text_color
                        spacing 2
                        xfill True
                        text "{b}Name:{/b} [girl.name]" size 15 color text_color font "exo2_regular" alt ""
                        $ info_self_voicing += f"{girl.name}. "
                        $ text_displayed += 1
                        if girl.status:
                            text _lssb_ui_translate("{b}Status:{/b} ") + _lssb_ui_status(girl) size 15 color text_color font "exo2_regular" alt ""
                            $ info_self_voicing += f"Status: {girl.status}. "
                            $ text_displayed += 1
                        text "{b}Age:{/b} [girl.age + girl.flags.age_increase]" size 15 color text_color font "exo2_regular" alt ""
                        $ info_self_voicing += f"Age: {girl.age + girl.flags.age_increase}. "
                        $ text_displayed += 1
                        if girl.flags.birthdayknown:
                            text "{b}Birthday:{/b} [girl.birthday[0]!tc]  [girl.birthday[1]]" size 15 color text_color font "exo2_regular" alt ""
                            $ info_self_voicing += f"Birthday: {girl.birthday[0]} {girl.birthday[1]}. "
                            $ text_displayed += 1
                        if girl.is_female:
                            if (girl.sub >= 75 or girl.love >= 150) and girl.sexperience > 1:
                                if girl.flags.pill:
                                    text "{b}Birth control:{/b} Yes" size 15 color text_color font "exo2_regular" alt ""
                                    $ info_self_voicing += "Birth control: Yes. "
                                else:
                                    text "{b}Birth control:{/b} No" size 15 color text_color font "exo2_regular" alt ""
                                    $ info_self_voicing += "Birth control: No. "
                                $ text_displayed += 1
                            if hero.has_skill("fertility_assessment"):
                                if girl.is_visibly_pregnant or girl.flags.toldpreg:
                                    text "{b}Fertility:{/b} Pregnant" size 15 color text_color font "exo2_regular" alt ""
                                    $ info_self_voicing += f"Fertility: Pregnant. "
                                else:
                                    text "{b}Fertility:{/b} [girl.fertility]%" size 15 color text_color font "exo2_regular" alt ""
                                    $ info_self_voicing += f"Fertility: {girl.fertility}%. "
                                $ text_displayed += 1
                        if girl.sexperience >= 1:
                            text "{b}Sex count:{/b} [girl.sexperience]" color text_color size 15 font "exo2_regular" alt ""
                            $ info_self_voicing += f"Sex count: {girl.sexperience}. "
                            $ text_displayed += 1

                        if girl.flags.mikeBabies or girl.flags.otherBabies:
                            $ babies = girl.flags.mikeBabies + girl.flags.otherBabies
                            text "{b}Babies:{/b} [babies]" color text_color size 15 font "exo2_regular" alt ""
                            $ info_self_voicing += f"Babies: {babies}. "
                            $ text_displayed += 1
                        $ job = girl.flags.job
                        if job:
                            text _lssb_ui_translate("{b}Job:{/b} ") + _lssb_ui_translate(JOBS[job].name) size 15 color text_color font "exo2_regular" alt ""
                            $ info_self_voicing += f"Job: {JOBS[job].name}. "
                            $ text_displayed += 1
                if girl.traits.known:
                    vbox:
                        if text_displayed >= 7:
                            ypos 11 + 20 * (text_displayed - 7)
                        xpos 10
                        xsize 303
                        xfill True
                        python:
                            traits = ""
                            line_limit = 39
                            entries = remains = 0
                            for trait in girl.traits.known:
                                trait = _lssb_ui_translate(trait.replace("_", " ").capitalize()) + ", "
                                if (len(traits) - entries) + len(trait) > (line_limit * (entries + 1)) - remains: 
                                    traits += "\n" 
                                    entries += 1 
                                    remains += (line_limit * entries) - (len(traits) - entries)
                                traits += trait
                            traits = traits[:-2] 
                        text "{b}Traits{/b}" size 15 color text_color font "exo2_regular" alt ""
                        text traits size 15 color text_color font "exo2_regular" alt ""
                        $ info_self_voicing += f"Traits: {traits}, "
            button:
                style "empty"
                action NullAction()
                keyboard_focus False
                alt info_self_voicing

        for attr in girl.get_attributes():
            if attr.visible():
                $ attr_bar_ui = attr.for_ui()
                fixed:
                    xysize (313, 31)
                    bar:
                        value attr_bar_ui['vbar']['value']
                        range attr_bar_ui['vbar']['range']
                        left_bar "gui/bar_full_big.png"
                        right_bar "gui/bar_empty_big.png"
                    bar:
                        value attr_bar_ui['lbar']['value']
                        range attr_bar_ui['lbar']['range']
                        left_bar f"gui/bar_{attr_bar_ui['lbar']['left']}_big.png"
                        right_bar f"gui/bar_{attr_bar_ui['lbar']['right']}_big.png"
                    add attr_bar_ui['icon'] align (0.25, 0.5)
                    text attr_bar_ui['text'] align (0.5, 0.5) size 23 color "#ffffff" font "exo2_regular" alt ""
                    if attr_bar_ui['lock']:
                        add "gui/icons/icon_lock.png" align (0.87, 0.5)
                    button:
                        style "empty"
                        action NullAction()
                        keyboard_focus False
                        alt replace_tags_alt(f"{attr_bar_ui['icon']} {attr_bar_ui['text']} {' is Lock' if attr_bar_ui['lock'] else ''}")

        if game.active_date.on_date(girl.id):
            hbox spacing 5 yalign 0.0:
                $ score = game.active_date.score
                if score > 100:
                    $ score = 100
                if score < -100:
                    $ score = -100
                fixed:
                    xysize (313, 31)
                    bar value score range 100 left_bar "gui/bar_full_big.png" right_bar "gui/bar_empty_big.png"
                    hbox spacing 10 xalign 0.5:
                        add "gui/icons/icon_dating.png" yalign 1.0
                        text str(score) + "%" yalign 0.5 size 23 color "#ffffff" font "exo2_regular" alt ""

screen old_ui_helper(helper):
    variant "lssb_ui_ru_26_8_0d"

    if helper:
        $ helper_name, helper_type = helper
        if helper_type == "activity" and game.room == "map":
            vbox:
                align (0.5, 0.17)
                text helper_name size 23 font "exo2_regular" color "#fff" outlines [(1, "#0099ff", 0, 0)] xalign 0.5
        else:
            hbox:
                xalign 0.5
                if helper_type in ["talk", "activity"]:
                    text helper_name size 23 font "exo2_regular" color "#FFFFFF" outlines [(1, "#0099ff", 0, 0)] xalign 0.5 alt ""
                elif helper_type == "room":
                    text "Go to [helper_name!t]" size 23 font "exo2_regular" color "#FFFFFF" outlines [(1, "#0099ff", 0, 0)] xalign 0.5

screen tooltip():
    variant "lssb_ui_ru_26_8_0d"
    $ tooltip = GetTooltip()
    $ keep_at_it = isinstance(tooltip, tuple) and len(tooltip) == 2 and tooltip[0] == "keep_at_it"
    if keep_at_it:
        $ tooltip = tooltip[1]
    if tooltip:
        if renpy.get_screen(["inventory"]):
            $ in_inventory = True
        else:
            $ in_inventory = False
        nearrect:
            at FadeInTransform
            focus "tooltip"
            style_prefix "tooltips"
            if isinstance(tooltip, Room):
                preferred_side "top"
                frame:
                    xpos 50
                    xanchor 0.5
                    style "invisible_frame"
                    text "Go to [tooltip.display_name!t]" size 23 font "exo2_regular" color "#fff" outlines [(1, "#0099ff", 0, 0)] xalign 0.5
            elif isinstance(tooltip, (tuple, list)):
                preferred_side "right"
                xpos 30
                frame:
                    ypos 30
                    yanchor 0.5
                    style "overlay_ui_frame"
                    has vbox
                    align (0.5, 0.5)
                    spacing 5
                    text " ".join(_lssb_ui_translate(part) for part in tooltip) substitute False yalign 0.5
            elif isinstance(tooltip, str):
                preferred_side "right"
                xpos 30
                frame:
                    ypos 30
                    yanchor 0.5
                    style "overlay_ui_frame"
                    has vbox
                    align (0.5, 0.5)
                    spacing 5
                    text _lssb_ui_translate(tooltip) substitute False yalign 0.5
            else:
                preferred_side "right"
                if isinstance(tooltip, ItemBase):
                    xpos 30
                else:
                    xpos 10
                frame:
                    ypos 30
                    yanchor 0.5
                    style "overlay_ui_frame"
                    has vbox
                    align (0.5, 0.5)
                    spacing 5
                    $ name = tooltip.display_name if not isinstance(tooltip, Person) else "Talk to [tooltip.name]"
                    $ name = tooltip.loop_display_name if keep_at_it and isinstance(tooltip, BaseActivity) else name
                    text name size 23 font "exo2_regular" color "#fff" outlines [(1, "#0099ff", 0, 0)] xalign 0.5
                    if not isinstance(tooltip, Person) and tooltip.get_tooltip():
                        text _lssb_ui_translate(tooltip.get_tooltip(in_inventory)) substitute False yalign 0.5

screen tooltip_old_ui():

    variant "lssb_ui_ru_26_8_0d"

    $ tooltip = GetTooltip()

    if isinstance(tooltip, tuple) and len(tooltip) == 2 and tooltip[0] == "keep_at_it":

        $ tooltip = tooltip[1]

    if tooltip:

        if renpy.get_screen(["inventory"]):

            $ in_inventory = True

        else:

            $ in_inventory = False

        if isinstance(tooltip, BaseActivity):

            $ tooltip = tooltip.get_tooltip()

            if tooltip:

                if game.room == "map":

                    hbox:

                        xalign 0.5

                        ypos 25

                        text " ".join(_lssb_ui_translate(part) for part in tooltip) color "#FFFFFF" alt ""

                else:

                    hbox:

                        align (0.5, 0.88)

                        text " ".join(_lssb_ui_translate(part) for part in tooltip) color "#FFFFFF" alt ""

        elif isinstance(tooltip, ItemBase):

            $ tooltip = tooltip.get_tooltip(in_inventory)

            if tooltip:

                nearrect:

                    focus "tooltip"

                    style_prefix "tooltips"

                    has frame

                    yanchor 0

                    xalign 0.5

                    xpadding 20

                    text _lssb_ui_translate(tooltip) substitute False yalign 0.05

        elif isinstance(tooltip, (tuple, list)):

            hbox:

                xalign 0.5

                ypos 615

                text " ".join(_lssb_ui_translate(part) for part in tooltip) substitute False color "#FFFFFF"


screen shopping(items=[], clerk=None):
    variant "lssb_ui_ru_26_8_0d"
    style_prefix "shopping"
    modal True
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Return("exit")
    button pos (0, 0) xysize (1280, 720) action Return("exit")
    on "show" action [Hide("quick_menu"), Hide("say")]
    if clerk:
        if persistent.new_ui:
            add clerk align (0.7, 1.0)
        else:
            add clerk align (0.25, 1.0)
    vbox:
        if persistent.new_ui:
            xalign 0.2
        else:
            xalign 0.75
        ypos 100
        spacing 10
        xsize 315
        frame:
            ysize 435
            background "gui/inv/inventory_box.png"
            label Room.find(game.room).display_name alt ""
            viewport id "inventory_vp":
                style_prefix "shopping_items"
                xfill True
                pos (10, 55)
                ysize 352
                draggable True
                mousewheel True
                has vbox
                for i, (item_name, item_id, item_price, item_tooltip) in enumerate(sorted(items, key=lambda x: x[0])):
                    hbox:
                        xsize 0.93
                        button sensitive item_price <= hero.money action Return((item_id, item_price)) default_focus (1 if i == 0 and check_controller() else 0):
                            xfill True
                            text _lssb_ui_resize(item_name, 270) alt ""
                            hbox:
                                xalign 1.0
                                text "[item_price] " alt ""
                                add hero.money.icon yalign 0.5
                            tooltip ItemBase.find(item_id)
                            alt f"{item_name}. money cost: {item_price}. " + replace_tags_alt(" ".join(item_tooltip))
            vbar value YScrollValue("inventory_vp") left_bar "gui/inv/vertical_idle_bar.png" thumb "gui/inv/vertical_idle_thumb.png" right_bar "gui/inv/vertical_idle_bar.png" xmaximum 11 ymaximum 370 xalign 1.0 ypos 50 unscrollable "hide" alt "scroll "
        fixed:
            ysize 29
            imagebutton auto "gui/button_%s.png" action Return("exit") alt "Exit"
            text "Exit" color "#ffffff" font "palanquin_bold" xalign 0.5 alt ""

    if persistent.new_ui:
        use tooltip
    else:
        use tooltip_old_ui

screen inventory():
    variant "lssb_ui_ru_26_8_0d"
    style_prefix "inventory"
    modal True
    predict False
    on "show" action [Hide("quick_menu"), Hide("say"), Function(hide_people)]
    if persistent.new_ui:
        add hero.layered_image() align (0.7, 1.0)
    else:
        add hero.layered_image() align (0.25, 1.0)
    vbox:
        if persistent.new_ui:
            xalign 0.2
        else:
            xalign 0.75
        ypos 100
        spacing 10
        xsize 315
        frame:
            ysize 88
            background "gui/inv/equipment_box.png"
            vbox spacing -9:
                label "Clothes:" text_size 20 alt ""
                label "Accessory:" text_size 20 alt ""
            vbox spacing 6:
                pos (145, 10)
                $ clothes, accessory = hero.equipment_for_ui
                text "[clothes!ti]" size 19 alt ""
                text "[accessory!ti]" size 19 alt ""
        frame:
            ysize 435
            background "gui/inv/inventory_box.png"
            label "Inventory" alt ""
            hbox:
                ypos 52
                textbutton "🗑️":
                    text_size 18
                    xpos 8
                    action ToggleVariable("discard_mode")
                    style ("filter_title_select" if discard_mode else "filter_title")
                hbox:
                    spacing 1
                    xpos 54
                    text "Filter: " yalign 0.5 alt ""

                    $ filters = {
                        "gift": ("🎁", "gift", Gift),
                        "equip": ("👔", "equip", Equip),
                        "cons": ("🫙", "consumable", Consumable),
                        "othe": ("📦", "other", Item)
                    }
                    for filter_name, (icon, alt_text, _) in filters.items():
                        textbutton icon:
                            if store.inventory_filter == filter_name:
                                style "filter_title_select"
                                action SetVariable("inventory_filter", None)
                                alt "filter {} selected".format(alt_text)
                            else:
                                style "filter_title"
                                action SetVariable("inventory_filter", filter_name)
                                alt "filter {}".format(alt_text)
            if hero.inventory:
                viewport id "inventory_vp":
                    style_prefix "inventory_items"
                    xfill True
                    pos (10, 90)
                    ysize 324
                    draggable True
                    mousewheel True
                    $ cls = filters.get(store.inventory_filter, (None, None, ItemBase))[2]
                    $ items = cls.filtered_sort(filter=lambda x: x.name in hero.inventory, key=lambda x: x.display_name)
                    vbox:
                        for item in items:
                            if discard_mode and item.one_only:
                                continue
                            $ t = _lssb_ui_translate(item.display_name)
                            $ n = hero.has_item(item.name)
                            if n > 1:
                                $ t += " ({})".format(n)
                            $ is_valid_equip = (isinstance(item, Equip) and game.room in ["bedroom1", "bedroom4"])
                            $ is_valid_consum = (isinstance(item, Consumable) and not game.flags[item.name] and item.test())
                            $ is_sensitive = is_valid_equip or is_valid_consum
                            hbox:
                                if discard_mode:
                                    button:
                                        yalign 0.5
                                        text "❌" align (0.0, 0.5) style "inventory_items_text_icon" alt "" size 12
                                        action Function(hero.lose_item, item)
                                frame:
                                    xysize (0.93, 26)
                                    style "invisible_frame"
                                    button:
                                        if discard_mode:
                                            action NullAction()
                                            sensitive False
                                        else:
                                            action Return(item)
                                            sensitive is_sensitive
                                        xfill True
                                        yfill True
                                        yalign 0.5
                                        hbox:
                                            xfill True
                                            yalign 0.5
                                            text _lssb_ui_resize(t, (275 if discard_mode else 295), style.inventory_items_text.size):
                                                align (0.0, 0.5)
                                                alt t + ". " + replace_tags_alt(" ".join(item.get_tooltip(True)))
                                            text item.icon align (1.0, 0.5) style "inventory_items_text_icon" alt ""
                                        tooltip item
                                    if not is_sensitive:
                                        $ insensitive_tooltip = ""
                                        if not is_valid_equip and isinstance(item, Equip):
                                            $ insensitive_tooltip += _lssb_ui_translate("{color=#ddddddcc}Can only be equipped in bedroom{/color}")
                                        elif not is_valid_consum and isinstance(item, Consumable):
                                            $ insensitive_tooltip += _lssb_ui_translate("{color=#ddddddcc}Need to wait a ")
                                            if (item.frequency_limit):
                                                $ insensitive_tooltip += _lssb_ui_translate(item.frequency_limit)
                                            else:
                                                $ insensitive_tooltip += _lssb_ui_translate("bit")
                                            $ insensitive_tooltip += _lssb_ui_translate(" between use{/color}")
                                        elif isinstance(item, Gift):
                                            $ insensitive_tooltip += _lssb_ui_translate("{color=#ddddddcc}A gift for someone{/color}")

                                        button:
                                            style "invisible_button"
                                            action NullAction()
                                            xfill True
                                            yfill True
                                            yalign 0.5
                                            tooltip insensitive_tooltip
                                            keyboard_focus False
                                            alt t + " not usable now. " + replace_tags_alt(" ".join(insensitive_tooltip))

                vbar value YScrollValue("inventory_vp") left_bar "gui/inv/vertical_idle_bar.png" thumb "gui/inv/vertical_idle_thumb.png" right_bar "gui/inv/vertical_idle_bar.png" xmaximum 11 ymaximum 324 xalign 1.0 ypos 90 unscrollable "hide" alt "scroll "
        fixed:
            ysize 29
            imagebutton auto "gui/button_%s.png" action [SetVariable("inventory_filter", None), SetVariable("discard_mode", False), Return("exit")] keysym "game_menu" alt "Exit"
            text "Exit" color "#ffffff" font "palanquin_bold" xalign 0.5 alt ""

    if persistent.new_ui:
        use tooltip
    else:
        use tooltip_old_ui

screen choose_gift(exc=None):
    variant "lssb_ui_ru_26_8_0d"
    style_prefix "inventory"
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Return("exit")
    button pos (0, 0) xsize 1280 ysize 720 action Return("exit")
    on "show" action [Hide("quick_menu"), Hide("say")]
    vbox:
        xalign 0.75
        ypos 100
        spacing 10
        xsize 315
        frame:
            ysize 88
            background "gui/inv/equipment_box.png"
            vbox spacing -9:
                label "Clothes:" text_size 20 alt ""
                label "Accessory:" text_size 20 alt ""
            vbox spacing 6:
                pos (145, 10)
                $ clothes, accessory = hero.equipment_for_ui
                text "[clothes!ti]" size 19 alt ""
                text "[accessory!ti]" size 19 alt ""
        frame:
            ysize 435
            background "gui/inv/inventory_box.png"
            label "Gift" alt ""
            if hero.inventory:
                viewport id "inventory_vp":
                    style_prefix "inventory_items"
                    xfill True
                    pos (10, 55)
                    ysize 352
                    draggable True
                    mousewheel True
                    has vbox
                    for item in Gift.filtered_sort(
                            filter=lambda x: x.name in hero.inventory,
                            key=lambda x: x.display_name,
                        ):
                        $ t = item.display_name
                        $ n = hero.has_item(item.name)
                        if n > 1:
                            $ t += " ({})".format(n)
                        hbox:
                            xsize 0.93
                            button action Return(item):
                                xfill True
                                yalign 0.5
                                has hbox
                                xfill True
                                yalign 0.5
                                text t yalign 0.5
                                text item.icon align (1.0, 0.5) style "inventory_items_text_icon"
                vbar value YScrollValue("inventory_vp") left_bar "gui/inv/vertical_idle_bar.png" thumb "gui/inv/vertical_idle_thumb.png" right_bar "gui/inv/vertical_idle_bar.png" xmaximum 11 ymaximum 370 xalign 1.0 ypos 50 unscrollable "hide" alt "scroll "
        fixed:
            xysize (315, 29)
            imagebutton auto "gui/button_%s.png" action Return("exit")
            text "Exit" color "#ffffff" font "palanquin_bold" xalign 0.5

screen get_birthday_screen():
    variant "lssb_ui_ru_26_8_0d"
    style_prefix "setup"
    add gui.game_menu_background

    vbox:
        yalign 0.1
        label "‍🎂" style "setup_title" alt ""
        label "CHOOSE YOUR BIRTHDAY" style "setup_title" alt ""
        text "What is your birthday?" alt f"What is your birthday? Currently month: {birthday_month} and day: {str(birthday_day)}"
    vbox:
        xsize 420
        yalign 0.75
        spacing 15
        hbox:
            label _lssb_ui_translate("Month: ") + _lssb_ui_translate(birthday_month.title()) alt ""
            label _lssb_ui_translate("Day: ") + str(birthday_day) alt ""
        grid 2 2:
            textbutton "Spring" action SetVariable("birthday_month","spring") alt "Set month to spring" tooltip ""
            textbutton "Fall" action SetVariable("birthday_month","fall") alt "Set month to fall" tooltip ""
            textbutton "Summer" action SetVariable("birthday_month","summer") alt "Set month to summer" tooltip ""
            textbutton "Winter" action SetVariable("birthday_month","winter") alt "Set month to winter" tooltip ""
        grid 6 6:
            style_prefix "setup_round"
            for i in range(1, 32):
                textbutton str(i) action SetVariable("birthday_day", i) alt "Set day to {}".format(i) tooltip ""
    hbox:
        yalign 1.0
        textbutton _("BACK") action Rollback() tooltip "" style "game_menu_return_button"
        textbutton _("CONTINUE") action Return tooltip "" style "game_menu_return_button"

screen get_start_date_screen():
    variant "lssb_ui_ru_26_8_0d"
    style_prefix "setup"
    add gui.game_menu_background

    vbox:
        yalign 0.1
        label "‍🚩" style "setup_title" alt ""
        label "CHOOSE YOUR STARTING DAY" style "setup_title" alt ""
        text "When do you want the game to start?" alt f"When do you want the game to start? Currently month: {starting_month} and day: {starting_day}"
    vbox:
        xsize 420
        yalign 0.75
        spacing 15
        hbox:
            label _lssb_ui_translate("Month: ") + _lssb_ui_translate(starting_month.title()) alt ""
            label _lssb_ui_translate("Day: ") + str(starting_day) alt ""

        grid 2 2:
            textbutton "Spring" action SetVariable("starting_month", "spring") alt "Set month to spring" tooltip ""
            textbutton "Fall" action SetVariable("starting_month", "fall") alt "Set month to fall" tooltip ""
            textbutton "Summer" action SetVariable("starting_month", "summer") alt "Set month to summer" tooltip ""
            textbutton "Winter" action SetVariable("starting_month", "winter") alt "Set month to winter" tooltip ""
        grid 6 6:
            style_prefix "setup_round"
            for i in range(1, 32):
                textbutton str(i) action SetVariable("starting_day", i) alt "Set day to {}".format(i) tooltip ""
    hbox:
        yalign 1.0
        textbutton _("BACK") action Rollback() tooltip "" style "game_menu_return_button"
        textbutton _("DONE") action Return tooltip "" style "game_menu_return_button"

screen story_tracker():

    variant "lssb_ui_ru_26_8_0d"

    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Hide("story_tracker")

    on "show" action Hide("smartphone")

    default tracker_type = StoryStatus.ACTIVE

    default tracker_story = None

    default tracker_filter = "all"

    default enable_spoilers = False

    default spoilers_hints = None

    default spoilers_height = 120

    default spoilers_width = 120

    $ participants, stories, tracker_story = storytracker.for_ui(tracker_filter, tracker_type, tracker_story)

    $ generic_stories = {k:v for k,v in stories.items() if v._type == "generic"}

    $ harems_stories = {k:v for k,v in stories.items() if v._type == "harem"}

    $ npc_stories = {k:v for k,v in stories.items() if v._type == "npc"}

    $ cupid_stories = {k:v for k,v in stories.items() if v._type == "cupid"}

    $ filters = {"all": "All", "harem": "Harems", "generic": "Generic"}

    $ filters.update(participants)

    style_prefix "story"

    vbox:

        xysize (1230, 600)

        pos (25, 110)

        frame:

            xysize (1230, 600)

            xpadding 5

            frame:

                style_prefix "story_title"

                pos -20,-20

                label "STORY TRACKER"

            vbox:

                frame style "invisible_frame":

                    xysize (1200, 47)

                    align (0.5, 0.5)

                    style_prefix "story_type"

                    textbutton "Filter: [filters[tracker_filter]!t]":

                        align (0.5, 0.5)

                        action CaptureFocus("filter_dropdown")

                    hbox:

                        spacing 4

                        align (0.99, 0.5)

                        textbutton _("Spoilers") selected enable_spoilers tooltip "Enable/Disable tooltip for the story steps.\nClick on the step with a 👁️ to see the hints." action ToggleLocalVariable("enable_spoilers", true_value=True, false_value=False)

                        textbutton _("Active") tooltip "Show the ongoing step." action [SensitiveIf(tracker_type != StoryStatus.ACTIVE), SetScreenVariable("tracker_type", StoryStatus.ACTIVE)]

                        textbutton _("Completed") tooltip "Show the completed step." action [SensitiveIf(tracker_type != StoryStatus.COMPLETED), SetScreenVariable("tracker_type", StoryStatus.COMPLETED)]

                frame:

                    xysize (1230, 15)

                    xpos -4

                    background Line("#006284", (0, 0), (1230, 0), 5)

                hbox:

                    viewport id "story_stories":

                        if tracker_filter == True:

                            xpos -600

                        xysize (280, 505)

                        draggable True

                        mousewheel True

                        vbox spacing 1:

                            if generic_stories:

                                textbutton "Generic"

                                for key, story in generic_stories.items():

                                    button:

                                        hbox:

                                            if story.complete and story.status_icon != "None":

                                                add "gui/icons/icon_[story.status_icon].png" xysize (25, 25) yalign 0.5

                                            else:

                                                null width 30

                                            text _lssb_ui_resize(story.name, 270)

                                        action [SelectedIf(tracker_story == key), SetScreenVariable("tracker_story", key)]

                            if npc_stories:

                                textbutton "Npc"

                                for key, story in npc_stories.items():

                                    button:

                                        hbox:

                                            if story.complete and story.status_icon != "None":

                                                add "gui/icons/icon_[story.status_icon].png" xysize (25, 25) yalign 0.5

                                            else:

                                                null width 30

                                            text _lssb_ui_resize(story.name, 270)

                                        action [SelectedIf(tracker_story == key), SetScreenVariable("tracker_story", key)]

                            if cupid_stories:

                                textbutton "Cupid"

                                for key, story in cupid_stories.items():

                                    button:

                                        hbox:

                                            if story.complete and story.status_icon != "None":

                                                add "gui/icons/icon_[story.status_icon].png" xysize (25, 25) yalign 0.5

                                            else:

                                                null width 30

                                            text text_tag_resize(story.name, 270)

                                        action [SelectedIf(tracker_story == key), SetScreenVariable("tracker_story", key)]

                            if harems_stories:

                                textbutton "Harems"

                                for key, story in harems_stories.items():

                                    button:

                                        hbox:

                                            if story.complete and story.status_icon != "None":

                                                add "gui/icons/icon_[story.status_icon].png" xysize (25, 25) yalign 0.5

                                            else:

                                                null width 30

                                            text _lssb_ui_resize(story.name, 270)

                                        action [SelectedIf(tracker_story == key), SetScreenVariable("tracker_story", key)]

                            null height 2

                    vbar value YScrollValue("story_stories") xmaximum 11 unscrollable "hide" alt "scroll "

                    viewport id "story_description_text":

                        draggable True

                        mousewheel True

                        xsize 890

                        has vbox

                        style_prefix "story_description"

                        if not tracker_story in stories:

                            text "There are no stories to show"

                        else:

                            $ current_story = stories[tracker_story]

                            $ extra_data = None

                            if enable_spoilers and current_story.extra_data:

                                $ extra_data = [f"{k.capitalize()}: {safe_eval(v)}\n" for k,v in current_story.extra_data.items()]

                            hbox:

                                style_prefix "story_title"

                                spacing 10

                                textbutton current_story.name:

                                    alt current_story.name

                                    if extra_data:

                                        action [CaptureFocus("spoilers"), SetScreenVariable("spoilers_hints", extra_data)]

                                    else:

                                        tooltip ""

                                        action NullAction

                                if hasattr(current_story, 'wiki_link') and current_story.wiki_link:

                                    textbutton "{size=25}🔗{/size}":

                                        action OpenURL(current_story.wiki_link)

                            null height 10

                            text current_story.desc alt ""

                            if tracker_type == StoryStatus.COMPLETED:

                                null height 10

                                text "Outcome" alt "" style_prefix "story_title"

                                null height 10

                                text current_story[current_story.outcome].description alt ""

                            null height 20

                            for step in current_story.steps.values():

                                if not step.inactive and not step.hide:

                                    $ step_self_voicing = ""

                                    $ desc = step.desc if not step.optional else f"OPTIONAL: {step.desc}"

                                    $ hints = None

                                    if enable_spoilers and ((step.active and tracker_type == StoryStatus.ACTIVE) or config.developer) and hasattr(step, 'related_event') and step.related_event:

                                        if BaseEvent.find(step.related_event):

                                            $ hints = BaseEvent.find(step.related_event).examine_ui()

                                        elif BaseActivity.find(step.related_event):

                                            $ hints = BaseActivity.find(step.related_event).examine_ui()

                                        elif TalkSubject.find(step.related_event):

                                            $ hints = TalkSubject.find(step.related_event).examine_ui()

                                        if hints:

                                            $ desc = f"👁️ {desc}"

                                    hbox:

                                        fixed:

                                            style_prefix "story_description_icon"

                                            if step.percentage and step.active:

                                                bar value step.percentage_for_ui range 100 ysize 32 xsize 95

                                                text f"{step.percentage_for_ui}%" alt ""

                                                $ step_self_voicing = f"active: {step.percentage_for_ui}% {desc}"

                                            elif step.status_icon != "None":

                                                text "{image=gui/icons/icon_[step.status_icon].png}" alt ""

                                                $ step_self_voicing = f"{story_step_alt(step.status_icon)}: {desc}"

                                            else:

                                                null height 25

                                        textbutton desc:

                                            if hints:

                                                action [CaptureFocus("spoilers"), SetScreenVariable("spoilers_hints", hints)]

                                            else:

                                                action NullAction

                                                tooltip ""

                                            alt step_self_voicing

                        null height 20

                    vbar value YScrollValue("story_description_text") unscrollable "hide" alt "scroll "

    if GetFocusRect("filter_dropdown"):

        dismiss action ClearFocus("filter_dropdown")

        nearrect:

            focus "filter_dropdown"

            style_prefix "story_select"

            has frame

            align (0.5, 0.5)

            modal True

            xysize (200, 300)

            frame style "invisible_frame":

                align (0.5, 0.5)

                xmaximum 180

                ymaximum 280

                viewport id "filter_drop":

                    draggable True

                    mousewheel True

                    has vbox

                    for filterid, filtername in filters.items():

                        textbutton filtername:

                            action [SetScreenVariable("tracker_filter", filterid), ClearFocus("filter_dropdown")]

                            xanchor 5

                vbar value YScrollValue("filter_drop") left_bar "gui/inv/vertical_idle_bar_small.png" thumb "gui/inv/vertical_idle_thumb.png" right_bar "gui/inv/vertical_idle_bar_small.png" align (0.97, 0.5) ysize 250 thumb_offset 10 top_gutter 10.5 bottom_gutter 10.5 unscrollable "hide" alt "scroll "

    $ tooltip = GetTooltip()

    if tooltip:

        nearrect:

            focus "tooltip"

            preferred_side "right"

            style_prefix "tooltips"

            has frame

            align (0.5, 0.4)

            ymaximum 650

            xpadding 20

            text _lssb_ui_translate(tooltip) substitute False yalign 0.05 alt ""

    if GetFocusRect("spoilers"):

        dismiss action [ClearFocus("spoilers"), SetScreenVariable("spoilers_hints", None)]

        if spoilers_hints:

            $ spoilers_width = int(max([get_string_size_in_pixel(s, style.tooltips_text.font, style.item_frame_message_text.size)[0] for s in spoilers_hints])) + 1

            $ spoilers_height = len(spoilers_hints) * 25

            nearrect:

                rect (450, 320, 25, 25)

                preferred_side "right"

                style_prefix "tooltips"

                has frame

                modal True

                xmaximum 800

                if spoilers_height < 625:

                    align (0.5, 0.5)

                    xsize spoilers_width + 30

                    vbox:

                        xmaximum 780

                        for spoiler in spoilers_hints:

                            text spoiler substitute False align (0.0, 0.05) alt ""

                else:

                    align (0.5, 0.4)

                    xsize spoilers_width + 35

                    ysize 625

                    viewport id "spoilers_vp":

                        draggable True

                        mousewheel True

                        scrollbars "vertical"

                        vscrollbar_base_bar Frame("gui/inv/vertical_idle_bar_long.png")

                        vscrollbar_thumb "gui/inv/vertical_idle_thumb.png"

                        has vbox

                        xmaximum 780

                        for spoiler in spoilers_hints:

                            text spoiler substitute True align (0.0, 0.05) alt ""


screen cheats_attr_change(owner):
    variant "lssb_ui_ru_26_8_0d"
    use cheats_viewport("characters"):
        vbox:
            if isinstance(owner, Hero):
                $ tgt = hero
                $ tgt_type = "hero"
                $ room_key = game.room
            else:
                $ tgt = Person.find(owner)
                $ tgt_type = "npc"
                $ room_key = tgt.room
            text tgt.name size 30 style "cheats_display_text" yalign 0
            $ room = Room.find(room_key).display_name if Room.find(room_key) is not None else room_key.capitalize()
            text "Location: [room!t]" style "cheats_display_text" yalign 0
            null height 10
            textbutton "Learn All Traits" action [Function(cheat_traits, tgt)] sensitive cheat_has_traits(tgt) style "cheats_button" yalign 0
            if tgt_type == "hero":
                if tgt.is_male:
                    if game.flags.nopreg:
                        textbutton "MC: Infertile" action [Function(cheat_nopreg, False)] style "cheats_button"
                    else:
                        textbutton "MC: Fertile" action [Function(cheat_nopreg, True)] style "cheats_button"

                if tgt.is_female:
                    if tgt.pregnant:
                        textbutton "Stop MC pregnancy" action [Function(cheat_pregnancy, tgt, False)] selected tgt.pregnant style "cheats_button"
                    else:
                        textbutton "Make MC pregnant" action [Function(cheat_pregnancy, tgt, True)] style "cheats_button"

                    if tgt.is_collared:
                        textbutton "Remove MC collar" action [SetVariable("hero.flags.collared", False)] selected tgt.is_collared style "cheats_button"
                    else:
                        textbutton "Add MC collar" action [SetVariable("hero.flags.collared", True)] style "cheats_button"

                    if tgt.flags.pubes:
                        textbutton "Remove MC pubes" action [SetVariable("hero.flags.pubes", False)] selected tgt.flags.pubes style "cheats_button" yalign 0
                    else:
                        textbutton "Add MC pubes" action [SetVariable("hero.flags.pubes", True)] style "cheats_button" yalign 0

                    textbutton "Switch MC haircut" action [ToggleVariable("hero.flags.haircut", True, False)] style "cheats_button" yalign 0
            else:
                if tgt.is_female:
                    if tgt.pregnant:
                        textbutton "Stop her pregnancy" action [Function(cheat_pregnancy, tgt, False)] style "cheats_button" yalign 0
                    else:
                        textbutton "Make her pregnant" action [Function(cheat_pregnancy, tgt, True)] style "cheats_button" yalign 0
            if tgt.id == "sasha":
                if tgt.flags.boobjob:
                    textbutton "Switch to small breasts" action [SetVariable(f"{tgt.id}.flags.boobjob", False)] style "cheats_button" yalign 0
                else:
                    textbutton "Switch to big breasts" action [SetVariable(f"{tgt.id}.flags.boobjob", True)] style "cheats_button" yalign 0

            textbutton "Wear all piercings" action [Function(cheat_piercings, tgt)] selected cheat_has_piercings(tgt) style "cheats_button" yalign 0
            null height 10
            $ attrs = sorted(cheat_get_attributes(owner), key=lambda x: x.name)
            $ cnt = len(attrs)
            grid 1 cnt:
                for attr in attrs:
                    hbox:
                        spacing 0
                        ysize 25
                        fixed:
                            xsize 160
                            $ npc_attr = attr.name.split("'s ")
                            if len(npc_attr) > 1:
                                text attr.name.split("'s ")[1].capitalize() style "cheats_button_text"
                            else:
                                text attr.name style "cheats_button_text"
                        textbutton "-" action [Function(cheat_attribute, attr, -10)] sensitive not attr.is_min xsize 40 text_size 30 style "cheats_button" text_xalign 0.5 text_yalign 0.63
                        textbutton "+" action [Function(cheat_attribute, attr, 10)] sensitive cheat_can_raise_attribute(attr) xsize 40 text_size 30 style "cheats_button" text_xalign 0.5 text_yalign 0.63

screen preferences():
    variant "lssb_ui_ru_26_8_0d"
    tag menu
    style_prefix "lspref"
    add gui.game_menu_background
    text "OPTIONS" xalign 0.5 ypos 42 font "palanquin_bold" size 48 color "#62ACD1" outlines [(3,"#000000")]
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action [Hide("preferences"), Return()]
    zorder 50

    frame:
        style "invisible_frame"
        minimum 1100,500
        maximum 1100,500
        ypos 150
        xalign 0.5
        viewport id "prefs":
            draggable True
            mousewheel True
            has vbox
            spacing 40
            vbox:
                spacing 20
                use text_tooltip(_lssb_ui_resize(_("Global Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Force update check"), 230, 30), _("Force the check for new version"), "lspref_label_text")
                        textbutton _("Force update") action [SetVariable("persistent._update_last_checked", {}), SetVariable("persistent._update_version", {})]
                    if renpy.android:
                        if config.basedir.endswith('base'):

                            vbox:
                                xysize (450, 60)
                                use text_tooltip(_lssb_ui_resize(_("Downloader:"), 450, 30), "", "lspref_label_text_title")
                                use text_tooltip(_lssb_ui_resize(_("Force downloader startup"), 450, 30), _("Force launch downloader instead of the game"), "lspref_label_text")
                                textbutton _lssb_ui_resize(_("Startup downloader"), 450) selected os.environ.get("USE_DOWNLOADER") action Function(search_in_path)
                        vbox:
                            xysize (300, 60)
                            use text_tooltip(_lssb_ui_resize(_("DLCs:"), 300, 30), "", "lspref_label_text_title")
                            use text_tooltip(_lssb_ui_resize(_("DLC Location"), 300, 30), _("Relocate your DLC file for the game to correctly load it (restart the game after locating the file)"), "lspref_label_text")
                            textbutton _lssb_ui_resize(_("Import DLC file"), 300) action Function(move_rpa)
            vbox:
                spacing 20
                use text_tooltip(_lssb_ui_resize(_("Video Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    if renpy.variant("pc"):
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(_lssb_ui_resize(_("Screen Display"), 230, 30), _("Change the game's window display"), "lspref_label_text")
                            textbutton _("Window") action Preference("display", "window")
                            textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Powersave"), 230, 30), _("Turn on, save power and reduce heat by updating the screen less often.\nTurn off for smoother visuals but higher power use."), "lspref_label_text")
                        textbutton _("Enable") action Preference("gl powersave", True)
                        textbutton _("Disable") action Preference("gl powersave", False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize("New UI", 230, 30), _("Enable new UI"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'new_ui', True)
                        textbutton _("Off") action SetField(persistent, 'new_ui', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_("X-Ray"), _("Allow to see through body during some scenes"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'xray', True)
                        textbutton _("Off") action SetField(persistent, 'xray', False)
                    if renpy.has_live2d() and any(dlc in DLCS for dlc in ('lively', 'fafow', 'fafwm')):
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(_lssb_ui_resize(_("Animations"), 230, 30), _("Enable/Disable sprites animations"), "lspref_label_text")
                            textbutton _("On") action SetField(persistent, 'live2d_on', True)
                            textbutton _("Off") action SetField(persistent, 'live2d_on', False)
                    if 'lively' in DLCS:
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(_lssb_ui_resize(_("Lively backgrounds"), 230, 30), _("Enable/Disable sprites in backgrounds"), "lspref_label_text")
                            textbutton _("On") action SetField(persistent, 'lively_bg', True)
                            textbutton _("Off") action SetField(persistent, 'lively_bg', False)
            vbox:
                spacing 20
                use text_tooltip(_lssb_ui_resize(_("Gameplay Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Tutorial"), 230, 30), _("Enable/Disable the tutorial at the start of a new game"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'skip_tutorial', False)
                        textbutton _("Skip") action SetField(persistent, 'skip_tutorial', True)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Difficulty"), 230, 30), _("Change the game difficulty"), "lspref_label_text")
                        textbutton _("Easy") action SetField(persistent, 'difficulty', -1)
                        textbutton _("Normal") action SetField(persistent, 'difficulty', 0)
                        textbutton _("Difficult") action SetField(persistent, 'difficulty', 1)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Random Schedule"), 230, 30), _("Allow non-player characters to choose among several locations during this routine"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'schedule_randomness', True)
                        textbutton _("Off") action SetField(persistent, 'schedule_randomness', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Random Needs"), 225, 30), _("The need's cost can fluctuate when performing actions"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'needs_randomness', True)
                        textbutton _("Off") action SetField(persistent, 'needs_randomness', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Shuffle Choices"), 225, 30), _("Modify the order of the selections in nearly all of the menu choices"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'choices_shuffle', True)
                        textbutton _("Off") action SetField(persistent, 'choices_shuffle', False)

                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Notifications pop-up"), 230, 30), _("Enable/Disable the notification pop-up"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'notifications', True)
                        textbutton _("Hide") action SetField(persistent, 'notifications', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Close-up pop-ups"), 230, 30), _("Show/Hide the close-up inserts during sex scenes"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'hide_sex_inserts', False)
                        textbutton _("Hide") action SetField(persistent, 'hide_sex_inserts', True)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Pregnancy duration"), 230, 30), _("Change the pregnancy duration to suit your preference"), "lspref_label_text")
                        textbutton _("Endless") action SetField(persistent, 'pregnancy_end', False)
                        textbutton _("Immersive") action SetField(persistent, 'pregnancy_end', True)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Pregnancy pop-up"), 230, 30), _("Enable/Disable pregnancy pop-up"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'pregnancy_notification', True)
                        textbutton _("Hide") action SetField(persistent, 'pregnancy_notification', False)
                    if persistent.start_plus:
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(_lssb_ui_resize(_("Reset NG+"), 230, 30), _("Clear NG+ saved statistics"), "lspref_label_text")
                            textbutton _("Clear stats") action Confirm("You're going to clear NG+ statistics.", Function(game.clear_new_game_plus))
                    if Achievement.total_unlocked:
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(_lssb_ui_resize(_("Reset Achievements"), 230, 30), _("Clear all unlocked achievements"), "lspref_label_text")
                            textbutton _("Clear achievements") action Confirm("You're going to clear achievements.", Function(Achievement.reset))
                    if check_controller():
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(_lssb_ui_resize(_("Frame Selector"), 230, 30), _("Allow to see selection with a framed border"), "lspref_label_text")
                            textbutton _("On") action SetField(persistent, 'selector', True)
                            textbutton _("Off") action SetField(persistent, 'selector', False)
            vbox:
                spacing 20
                use text_tooltip(_lssb_ui_resize(_("Dialogue Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Text Speed"), 343, 30), _("Controls the rate at which text displays.\nThe further to the right this slider is, the faster the text will display.\nAll the way to the right causes text to be shown instantly."), "lspref_label_text")
                        bar value Preference("text speed")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Auto forward Time"), 343, 30), _("Controls automatic advance.\nThe further to the left this slider is, the shorter the amount of time before the game advances.\nAll the way to the right means text will never auto-forward."), "lspref_label_text")
                        bar value Preference("auto-forward time")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Rollback Side"), 230, 30), _("Enable a side of the screen to causes rollback"), "lspref_label_text")
                        textbutton _("Disable") action Preference("rollback side", "disable")
                        textbutton _("Left") action Preference("rollback side", "left")
                        textbutton _("Right") action Preference("rollback side", "right")
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Skip"), 230, 30), _("Allow the game to skipping parts, like texts or transitions"), "lspref_label_text")
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")
                        textbutton _("Transitions") action Preference("transitions", "toggle")
            vbox:
                spacing 20
                use text_tooltip(_lssb_ui_resize(_("Audio Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Music Volume"), 343, 30), _("Controls the volume of the music.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("music volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Sound Volume"), 343, 30), _("Controls the volume of the sounds.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("sound volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Voice Volume"), 343, 30), _("Controls the volume of the voices.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("voice volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Ambience Volume"), 343, 30), _("Controls the volume of the sound ambience.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("ambience volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Sex Sounds Volume"), 343, 30), _("Controls the volume of the sex sounds.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("sexsfx volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Moans Volume"), 343, 30), _("Controls the volume of the moans.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("moans volume")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Mute audio"), 230, 30), _("Enable/Disable game audio"), "lspref_label_text")
                        textbutton _("Mute all") action Preference("all mute", "toggle") alt f"Mute all is {'On' if persistent.mute_characters else 'Off'}."
                        textbutton _("Mute alarm clock") selected persistent.mute_alarm_clock action ToggleField(persistent, 'mute_alarm_clock', True, False) alt f"Alarm clock sound is {'On' if not persistent.mute_alarm_clock else 'Off'}."
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Mute voice"), 230, 30), _("Enable/Disable character voice"), "lspref_label_text")
                        textbutton _("Mute Bree") action [ToggleVoiceMute("bree")] alt f"Mute Bree is {'On' if 'bree' in persistent._voice_mute else 'Off'}."
                        textbutton _("Mute Mike") action [ToggleVoiceMute("mike")] alt f"Mute Mike is {'On' if 'mike' in persistent._voice_mute else 'Off'}."
                        textbutton _("Mute all characters") selected persistent.mute_characters action Function(toggle_mute_all_characters) alt f"Mute all characters is {'On' if persistent.mute_characters else 'Off'}."
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Self-voicing"), 230, 30), _("Self-voicing setting"), "lspref_label_text")
                        textbutton _("Override voice") selected persistent.tts_override action Function(toggle_tts_override_voice_channel) alt f"Self-voicing override voice is {'On' if persistent.tts_override else 'Off'}."
        vbar:
            value YScrollValue("prefs")
            left_bar "gui/inv/vertical_idle_bar.png"
            right_bar "gui/inv/vertical_idle_bar.png"
            thumb "gui/inv/vertical_idle_thumb.png"
            thumb_offset 63
            left_gutter 63
            right_gutter 63
            maximum 11,359
            xpos 1100
            yalign 0.5
    button style "return_arrow_button" action [Hide("preferences"),Return()] tooltip "" default_focus check_controller()

    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            style_prefix "tooltips"

            has frame
            yanchor 0
            xalign 0.5
            xpadding 20
            text _lssb_ui_translate(tooltip) substitute False yalign 0.05

screen file_slots(title):
    variant "lssb_ui_ru_26_8_0d"
    zorder 50 tag menu


    if renpy.get_screen('game_save'):
        add gui.game_menu_background
        text "SAVE" xalign 0.5 ypos 42 font "palanquin_bold" size 48 color "#62ACD1" outlines [(3,"#000000")]
    else:
        add gui.game_menu_background
        text "LOAD" xalign 0.5 ypos 42 font "palanquin_bold" size 48 color "#62ACD1" outlines [(3,"#000000")]


    $ positions = [(133, 143), (498, 143), (850, 143), (133, 377), (498, 377), (850, 377)]


    for i, pos in enumerate(positions, start=1):
        button style "slot_save_load_button" pos pos default_focus (1 if i == 0 and check_controller() else 0):
            if renpy.get_screen('game_save'):
                action [SetVariable('save_name', FileSaveName(i)), ShowMenu('save_name_dialogue', i)]
            else:
                action FileLoad(i)
            use load_save_slot(number=i)

    use access_slots()

screen help():
    variant "lssb_ui_ru_26_8_0d"
    tag menu
    add gui.game_menu_background
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action [Hide("help"), Return()]
    if check_controller():
        text "ГЕЙМПАД" xalign 0.5 ypos 70 font "palanquin_bold" size 32 color "#ffffff"
        vbox:
            pos (180, 150)
            spacing 22
            for key_name, description in [
                ("Правый триггер / A", "Продолжить диалог, выбрать элемент"),
                ("Левый триггер / LB", "Вернуться к предыдущему тексту"),
                ("RB", "Перейти к следующему тексту"),
                ("Крестовина / стики", "Перемещаться по интерфейсу"),
                ("Start / Guide / B", "Открыть игровое меню"),
                ("Y", "Скрыть интерфейс")]:
                hbox:
                    spacing 30
                    text key_name xsize 300 min_width 300 font "palanquin_bold" size 22 color "#ffffff"
                    text description xsize 500 font "exo2_regular" size 22 color "#ffffff"
    else:
        text "КЛАВИАТУРА" pos (100, 90) font "palanquin_bold" size 30 color "#ffffff"
        text "МЫШЬ" pos (775, 90) font "palanquin_bold" size 30 color "#ffffff"
        vbox:
            pos (45, 155)
            spacing 2
            for key_name, description in [
                ("Enter", "Продолжить диалог, выбрать элемент"),
                ("Пробел", "Продолжить диалог без выбора ответа"),
                ("Стрелки", "Перемещаться по интерфейсу"),
                ("Esc", "Открыть игровое меню"),
                ("Ctrl", "Удерживать для пропуска текста"),
                ("Tab", "Включить или выключить пропуск"),
                ("Page Up", "Вернуться к предыдущему тексту"),
                ("Page Down", "Перейти к следующему тексту"),
                ("H", "Скрыть интерфейс"),
                ("S", "Сделать снимок экрана"),
                ("V", "Включить или выключить чтение вслух")]:
                hbox:
                    ysize 45
                    spacing 18
                    text key_name xsize 145 min_width 145 textalign 1.0 font "palanquin_bold" size 20 color "#ffffff"
                    text description xsize 400 font "exo2_regular" size 20 color "#ffffff"
        vbox:
            pos (695, 155)
            spacing 18
            for key_name, description in [
                ("Левая кнопка", "Продолжить диалог, выбрать элемент"),
                ("Колёсико", "Скрыть интерфейс"),
                ("Правая кнопка", "Открыть игровое меню"),
                ("Колесо вверх", "Вернуться к предыдущему тексту"),
                ("Колесо вниз", "Перейти к следующему тексту")]:
                hbox:
                    ysize 70
                    spacing 18
                    text key_name xsize 155 min_width 155 textalign 1.0 font "palanquin_bold" size 20 color "#ffffff"
                    text description xsize 330 font "exo2_regular" size 20 color "#ffffff"
    button style "return_arrow_button" action [Hide("help"),Return()] tooltip ""

