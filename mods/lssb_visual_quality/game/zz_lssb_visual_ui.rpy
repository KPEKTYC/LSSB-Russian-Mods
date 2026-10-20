# Additive visual interface for Love & Sex: Second Base 26.8.0d.
# All positions and interaction directives come from the installed version.
init 1000 python:
    _lssb_visual_ui_variant = "lssb_visual_ui_26_8_0d"
    _lssb_visual_ui_ru_labels = {'Home': 'Дом', 'Mall': 'Торговый центр', 'Street': 'Улица', 'Club': 'Клуб', 'Gym': 'Спортзал', 'Waterpark': 'Аквапарк', 'City': 'Город', 'Office': 'Офис', 'Aquarium': 'Океанариум', 'University': 'Университет', 'Park': 'Парк', 'Dark alley': 'Тёмный переулок', 'Car workshop': 'Автомастерская', 'Beach': 'Пляж', 'Cemetery': 'Кладбище', 'Church': 'Церковь', 'Movie theater': 'Кинотеатр', 'Forest': 'Лес', 'Gym reception': 'Вход в спортзал', 'Hospital': 'Больница', 'Karting track': 'Картодром', 'Maid Cafe': 'Мейд-кафе', 'Mansion': 'Особняк', 'Night Club': 'Ночной клуб', 'Photo Studio': 'Фотостудия', 'Police Station': 'Полиция', 'Pub': 'Паб', 'Rooftop': 'Крыша', 'Sex shop': 'Секс-шоп', 'Strip club': 'Стрип-клуб', 'Recording Studio': 'Студия звукозаписи', 'Trailer Park': 'Трейлерный парк', 'Uptown': 'Верхний город', 'Front Porch': 'Крыльцо', 'Reading room': 'Библиотека', 'Living Room': 'Гостиная', 'Hallway': 'Коридор', 'Bathroom': 'Ванная', 'Kitchen': 'Кухня', 'Pool': 'Бассейн', 'Attic': 'Чердак', 'My Bedroom': 'Моя спальня', "Sasha's Bedroom": 'Спальня Саши', "Minami's Bedroom": 'Спальня Минами', "[bree.name]'s Bedroom": 'Спальня [bree.name]', "Audrey's home": 'Дом Одри', "Palla's home": 'Дом Паллы', 'First\nFloor': 'Первый\nэтаж', 'Second\nFloor': 'Второй\nэтаж', 'Amusement park': 'Парк аттракционов', 'Amusement Park': 'Парк аттракционов', 'Amusement': 'Парк аттракционов', "Amy's home": 'Дом Эми', "Amy's Home": 'Дом Эми', 'Amyhome': 'Дом Эми', 'Golf course': 'Поле для гольфа', 'Golf Course': 'Поле для гольфа', 'Golf': 'Гольф', "Kat's home": 'Дом Кэт', "Kat's Home": 'Дом Кэт', 'Kathome': 'Дом Кэт', 'Restaurant': 'Ресторан', 'Shooting range': 'Тир', 'Shooting Range': 'Тир', 'Shootingrange': 'Тир', "Victor's safehouse": 'Убежище Виктора', "Victor's Safehouse": 'Убежище Виктора', 'Victorsafehouse': 'Убежище Виктора', 'Zoo': 'Зоопарк', 'Bedroom4': 'Спальня 4', 'Bedroom6': 'Спальня 6', "Mike's Bedroom": 'Спальня Майка', "Mike's bedroom": 'Спальня Майка'}
    _lssb_visual_ui_label_offsets = {
        "sexshop": (-14, False),
        "photostudio": (14, False),
        "trailer": (-42, False),
        "beach": (0, True),
    }

    def _lssb_visual_ui_translate(value):
        translated = renpy.translation.translate_string(value)
        # The achievement also uses "Beach"; its title is not a place caption.
        if (renpy.game.preferences.language == "russian" and value == "Beach"
                and translated == "Любовь к пляжу"):
            return "Пляж"
        if translated == value and renpy.game.preferences.language == "russian":
            return _lssb_visual_ui_ru_labels.get(value, value)
        return translated

    class _LssbVisualLabelBackground(renpy.Displayable):
        # Render a single SVG at the final caption dimensions. Slicing an SVG
        # Frame produces independently pixel-aligned pieces on the GL renderer.
        def render(self, width, height, st, at):
            width, height = max(1, int(width)), max(1, int(height))
            key = (width, height)
            if getattr(self, "_panel_size", None) != key:
                svg = ('<svg xmlns="http://www.w3.org/2000/svg" '
                       'width="%d" height="%d" viewBox="0 0 %d %d">'
                       '<rect x=".5" y=".5" width="%d" height="%d" rx="5.5" '
                       'fill="#104968" fill-opacity=".94" stroke="#a7e3f6" '
                       'stroke-opacity=".82"/></svg>') % (
                           width * 4, height * 4, width, height, width - 1, height - 1)
                self._panel_image = renpy.display.im.Data(
                    svg.encode("utf-8"), "lssb_label.svg", oversample=4)
                self._panel_size = key
            return renpy.render(self._panel_image, width, height, st, at)

    if True and _lssb_visual_ui_variant not in config.variants:
        config.variants.insert(0, _lssb_visual_ui_variant)

style lssb_visual_ui_frame is overlay_ui_frame:
    background Frame("lssb_visual_quality/ui/panel.svg", gui.overlay_ui_frame_borders, tile=gui.frame_tile)

style lssb_visual_map_label is text:
    font "exo2_bold"
    size 15
    color "#ffffff"
    outlines []
    text_align 0.5
    line_spacing -1
    layout "greedy"

screen _lssb_visual_map_label(label, x, y, location_id=None):
    # Only the caption is bounded; the location button and character icons retain
    # their exact original coordinates, geometry and hit area.
    $ label_dx, label_below = _lssb_visual_ui_label_offsets.get(location_id, (0, False))
    $ label_x = x + label_dx
    $ label_width = max(36, min(150, int(2 * min(label_x, config.screen_width - label_x)) - 12))
    frame:
        background _LssbVisualLabelBackground()
        padding (6, 2)
        xpos label_x
        ypos (y + 24 if label_below else y - 22)
        xanchor 0.5
        yanchor (0.0 if label_below else 1.0)
        xmaximum label_width
        text _lssb_visual_ui_translate(label) style "lssb_visual_map_label" xmaximum (label_width - 12) alt ""

screen map(locations):
    variant "lssb_visual_ui_26_8_0d"
    if not (renpy.get_screen("smartphone") or renpy.get_screen("story_tracker")):
        default destination = ""
        fixed:
            at master_bleed
            add "bg map"
            for location in locations:

                if location.id == "mall1":
                    $ location = Room.find("mallmap")
                if location.id == "gym":
                    $ location = Room.find("gymreception")
                $ x, y = map_location_positions[location.id]
                $ npcs = location.get_present_npcs_ids_by_tag()[:6]
                $ self_voicing_location = f"{location.display_name}; {'; '.join(npcs)}"
                imagebutton auto "lssb_visual_quality/ui/map_hex_%s.svg" xpos x ypos y xanchor 0.5 yanchor 0.5 alt self_voicing_location:
                    action [Function(location.travel_to), SetVariable("game.room", location.id), Return()]
                    hovered SetScreenVariable("destination", location)
                    unhovered SetScreenVariable("destination", "")
                for n_index, npc in enumerate(npcs):
                    $ x_g = x
                    $ y_g = y
                    if n_index == 1:
                        $ y_g += 35
                    elif n_index:
                        if n_index in [2, 4]:
                            $ x_g += 29
                        else:
                            $ x_g = x - 29
                        if n_index in [2, 3]:
                            $ y_g += 19
                        else:
                            $ y_g = y - 19
                    fixed:
                        xpos x_g
                        ypos y_g
                        xsize 25
                        ysize 25
                        xanchor 0.5
                        yanchor 0.5
                        add "gui/icons/icon_bg_small.png"
                        add f"notify {npc}"
                if location.id == "housemap":
                    $ location_name = "Home"
                elif location.id == "mallmap":
                    $ location_name = "Mall"
                elif location.id == "street":
                    $ location_name = "Street"
                elif location.id == "nightclub":
                    $ location_name = "Club"
                elif location.id == "gymreception":
                    $ location_name = "Gym"
                elif location.id == "waterpark":
                    $ location_name = "Waterpark"
                else:
                    $ location_name = location.display_name
                use _lssb_visual_map_label(location_name, x, y, location.id)

        if persistent.new_ui:
            use actions([(a, a.icon, a.display_name) for a in Activity.valid_activities()])
            use tooltip
        use ui_destination_helper(destination, location)

screen housemap(locations):
    variant "lssb_visual_ui_26_8_0d"
    if not (renpy.get_screen("smartphone") or renpy.get_screen("story_tracker")):
        default destination = ""
        fixed:
            at master_bleed
            if house_floor != 0:
                add "bg housemap first"
                imagebutton auto "gui/down_%s.png" action SetVariable("house_floor",0) xpos 250 ypos 530 xanchor 0.5 yanchor 0.5 alt "go to home first floor"
                text _lssb_visual_ui_translate("First\nFloor") font "exo2_bold" outlines [(1, "#083449")] color "#ffffff" xpos 250 ypos 610 xanchor 0.5 yanchor 0.5 alt ""
            else:
                imagebutton auto "gui/up_%s.png" action SetVariable("house_floor",1) xpos 250 ypos 530 xanchor 0.5 yanchor 0.5 alt "go to home second floor"
                text _lssb_visual_ui_translate("Second\nFloor") font "exo2_bold" outlines [(1, "#083449")] color "#ffffff" xpos 250 ypos 610 xanchor 0.5 yanchor 0.5 alt ""
            imagebutton auto "gui/map/city_%s.png" action SetVariable("game.room", "map"), Return() xpos 1000 ypos 530 xanchor 0.5 yanchor 0.5 alt "go to city"
            text _lssb_visual_ui_translate("City") font "exo2_bold" outlines [(1, "#083449")] color "#ffffff" xpos 1000 ypos 610 xanchor 0.5 yanchor 0.5 alt ""
            for location in [l for l in locations if l.id in housemap_location_positions[house_floor]]:
                $ x, y = housemap_location_positions[house_floor][location.id]
                $ npcs = location.get_present_npcs_ids()[:6]
                $ self_voicing_location = f"{location.display_name}; {'; '.join(npcs)}"
                imagebutton auto "lssb_visual_quality/ui/map_hex_%s.svg" xpos x ypos y xanchor 0.5 yanchor 0.5 alt self_voicing_location:
                    action SetVariable("game.room",location.id), Return()
                    hovered SetScreenVariable("destination", location)
                    unhovered SetScreenVariable("destination", "")
                for n_index, npc in enumerate(npcs):
                    $ x_g = x
                    $ y_g = y
                    if n_index == 1:
                        $ y_g += 35
                    elif n_index:
                        if n_index in [2, 4]:
                            $ x_g += 29
                        else:
                            $ x_g = x - 29
                        if n_index in [2, 3]:
                            $ y_g += 19
                        else:
                            $ y_g = y - 19
                    fixed:
                        xpos x_g
                        ypos y_g
                        xsize 25
                        ysize 25
                        xanchor 0.5
                        yanchor 0.5
                        add "gui/icons/icon_bg_small.png"
                        add f"notify {npc}"
                $ location_name = location.display_name
                use _lssb_visual_map_label(location_name, x, y, location.id)
        if persistent.new_ui:
            use actions([(a, a.icon, a.display_name) for a in Activity.valid_activities()])
            use tooltip
        else:
            use ui_destination_helper(destination, location)

screen ui_destination_helper(destination, location):
    variant "lssb_visual_ui_26_8_0d"
    if destination:
        if destination.id == "map":
            $ destination_name = "City"
        elif destination.id == "housemap":
            $ destination_name = "Home"
        elif destination.id == "mallmap":
            $ destination_name = "Mall"
        elif destination.id == "street":
            $ destination_name = "Street"
        elif destination.id == "nightclub":
            $ destination_name = "Club"
        elif destination.id == "gymreception":
            $ destination_name = "Gym"
        elif destination.id == "waterpark":
            $ destination_name = "Waterpark"
        else:
            $ destination_name = destination.display_name
        vbox:
            if renpy.get_screen("housemap") or (renpy.get_screen("map") and persistent.new_ui):
                align (0.5, 0.1)
            else:
                align (0.5, 0.2)
            spacing 20
            text _lssb_visual_ui_translate(destination_name) font "exo2_bold" outlines [(1, "#083449")] color "#ffffff" size 40 xalign 0.5 alt ""
            hbox:
                xalign 0.5
                box_justify True
                spacing 5
                if renpy.get_screen("housemap"):
                    $ present_people = destination.get_present_npcs_ids()
                else:
                    $ present_people = destination.get_present_npcs_ids_by_tag()

                for p in present_people:
                    add Composite(
                        (50, 50),
                        (0, 0), Transform("gui/phone/ico_phone_idle.png", zoom=0.8),
                        (7, 7), f"gui/action_icons/button_{p}.png"
                        ):
                        at Position(anchor=(0.5, 0.5))

screen overlay_ui():

    variant "lssb_visual_ui_26_8_0d"

    default helper = False

    if helper:

        $ helper_name, helper_type = helper

    zorder 1

    use button_screen

    default self_voicing_date = f"{game.calendar.hour_of_day}:00\n{game.calendar.day_of_week_name} {game.calendar.day_of_season} {game.calendar.season_name}"

    if not HIDE_UI:

        if persistent.notifications == True and NOTIFICATIONS and game.room not in ["map", "housemap", "mallmap"]:

            $ display_notifications()

        hbox xalign 0.5 ypos 10 spacing 10:

            frame:

                xysize (80, 80)

                style "invisible_frame"

                has imagebutton auto "lssb_visual_quality/ui/smart_%s.svg"

                align (0.5, 0.5)

                if renpy.get_screen(["room", "smartphone", "map", "housemap", "mallmap"]):

                    action ToggleScreen("smartphone")

                else:

                    sensitive False

                alt "smartphone"

            hbox spacing 10:

                python:

                    is_sick = game.flags.sick

                    is_injured = game.flags.injured

                vbox:

                    xsize 218

                    spacing 5

                    box_justify True

                    vbox:

                        spacing 0

                        frame:

                            xfill True

                            ysize 47

                            padding (14, 9)

                            if game.calendar.is_day:

                                background "lssb_visual_quality/ui/date_day.svg"

                            else:

                                background "lssb_visual_quality/ui/date_night.svg"

                            python:

                                hour = f"{game.calendar.hour_of_day}:00"

                                day = game.calendar.day_of_week_short_name.capitalize()

                                date = str(game.calendar.day_of_season)

                                icon = f"gui/icons/icon_{game.calendar.season_name}.png"

                            hbox:

                                align (1.0, 0.5)

                                spacing 5

                                style_prefix "ui"

                                text hour alt ""

                                text day alt ""

                                text date alt ""

                                add icon

                            button:

                                style "empty"

                                action NullAction()

                                keyboard_focus False

                                alt self_voicing_date

                        if game.flags.alarm_clock and game.room == "bedroom1":

                            frame:

                                xfill True

                                ysize 40

                                yoffset -5

                                padding (19, 10)

                                background "gui/alarm_box.png"

                                hbox spacing 10 align (0.5, 0.5):

                                    add "gui/icons/icon_hour.png" yalign 0.5

                                    text "[game.flags.alarm_time]:00" alt "" size 22 color "#006284"

                                button:

                                    style "empty"

                                    action NullAction()

                                    keyboard_focus False

                                    alt "Sickness for [game.timers.sick] day"

                    if not renpy.get_screen(["smartphone", "story_tracker", "smartphone_choice", "inventory", "shopping"]):

                        if is_sick:

                            textbutton "[game.timers.sick] ['day' if game.timers.sick == 1 else 'days']":

                                text_style "ui_text"

                                text_xalign 0.5

                                xfill True

                                padding (0, 0)

                                background "gui/physicalstates_icons/physicalstate_sickness.png"

                                sensitive None

                                action NullAction()

                                keyboard_focus False

                                alt "Sickness for [game.timers.sick] day"

                        if is_injured:

                            textbutton "[game.timers.injured] ['day' if game.timers.injured == 1 else 'days']":

                                text_style "ui_text"

                                text_xalign 0.5

                                xfill True

                                padding (0, 0)

                                background "gui/physicalstates_icons/physicalstate_bleed.png"

                                sensitive None

                                action NullAction()

                                keyboard_focus False

                                alt "Injured for [game.timers.injured] day"

                if game.room != "map" or persistent.new_ui:

                    frame xysize (297, 47) style "lssb_visual_ui_frame":

                        has hbox align (0.5, 0.5) spacing 5

                        for need in sorted(hero.get_needs(), key=lambda x: x.name):

                            frame xysize (64, 40):

                                style "empty"

                                yalign 0.5

                                hbox spacing 3:

                                    yalign 0.5

                                    fixed xysize (32, 32):

                                        add need.icon align (0.5, 0.5)

                                    if need < 1:

                                        label str(need) alt "" xsize 30 text_style "ui_text_error"

                                    elif need < 3:

                                        label str(need) alt "" xsize 30 text_style "ui_text_warning"

                                    else:

                                        label str(need) alt "" xsize 30 text_style "ui_text"

                                button:

                                    style "empty"

                                    action NullAction()

                                    keyboard_focus False

                                    alt need.name + str(need)

                    frame xysize (297, 47) style "lssb_visual_ui_frame":

                        has hbox align (0.5, 0.5) spacing 9

                        for attr in sorted(hero.get_attributes(), key=lambda x: x.name):

                            if attr.name != "Morality":

                                frame xysize (77, 40):

                                    style "empty"

                                    yalign 0.5

                                    fixed xysize (32, 32):

                                        yalign 0.5

                                        xpos 0

                                        add attr.get_icon() align (0.5, 0.5)

                                    if attr.is_at_maximum_cap:

                                        text "{size=*1.5}∞{/size}" alt "" xpos 39 yalign 0.5 style "ui_text"

                                    else:

                                        text str(attr.val) alt "" xpos 39 yalign 0.5 style "ui_text"

                                    button:

                                        style "empty"

                                        action NullAction()

                                        keyboard_focus False

                                        alt attr.name + str(attr)

                    fixed xysize (150, 90):

                        frame xysize (150, 47) style "lssb_visual_ui_frame":

                            add hero.money.icon yalign 0.5

                            $ money = str(hero.money)

                            label money alt "" align (1.0, 0.5) text_style "ui_text"

                            button:

                                style "empty"

                                action NullAction()

                                keyboard_focus False

                                alt "money" + money

                        if (

                        game.active_date or

                        (game.room in ["studio"] and game.flags.bandpractice) or

                        (Room.has_tag(game.room, 'home') and game.flags.chores < 100 and not game.flags.cleaningservices) or

                        (Room.has_tag(game.room, 'work') and (game.flags.worksatisfaction or game.flags.underinvestigation)) or

                        (game.room == 'bedroom1' and game.flags.alarm_clock)

                        ) and IN_EVENT_WITH != "tuto":

                            fixed xysize (218, 31) align (1.0, 1.0):

                                default self_voicing_progressbar = ""

                                if game.active_date:

                                    $ self_voicing_progressbar = "date: " + str(game.active_date.score) + "%"

                                    use percentile(game.active_date.score, "gui/icons/icon_dating.png", lower_bound=-100)

                                elif game.room in ["studio"] and game.flags.bandpractice:

                                    $ self_voicing_progressbar = "rehearsal: " + str(game.flags.bandpractice) + "%"

                                    use percentile(game.flags.bandpractice, "gui/icons/icon_guitar.png")

                                elif Room.has_tag(game.room, 'home') and game.flags.chores < 100 and not game.flags.cleaningservices:

                                    $ self_voicing_progressbar = "chores: " + str(game.flags.chores) + "%"

                                    use percentile(game.flags.chores, "gui/icons/icon_chores.png")

                                elif Room.has_tag(game.room, 'work') and game.flags.underinvestigation:

                                    $ self_voicing_progressbar = "investigation" + str(game.flags.workinvestigation) + "%"

                                    use percentile(game.flags.workinvestigation, "gui/icons/icon_investigation.png")

                                elif Room.has_tag(game.room, 'hospital') and game.flags.angelainvestigation and not game.flags.angela_test_results:

                                    $ self_voicing_progressbar = "investigation" + str(game.flags.angelainvestigation) + "%"

                                    use percentile(game.flags.angelainvestigation, "gui/icons/icon_investigation.png")

                                elif Room.has_tag(game.room, 'work') and game.flags.worksatisfaction and not game.flags.capped_promotion:

                                    $ val = game.flags.worksatisfaction if not game.flags.promoted else game.flags.worksatisfaction * 100 // game.get_promotion_cost()

                                    $ self_voicing_progressbar = "career: " + str(val) + "%"

                                    use percentile(val, "gui/icons/icon_career.png")

                                elif Room.has_tag(game.room, 'work') and game.flags.capped_promotion:

                                    bar value StaticValue(100/100.) style "overlay_ui_bar"

                                    hbox spacing 10 xalign 0.5:

                                        add "gui/icons/icon_career.png" yalign 0.5

                                        text "Max" alt "" yalign 0.5 style "ui_text"

                                    $ self_voicing_progressbar = "career: " + "Max"

                                button:

                                    style "empty"

                                    action NullAction()

                                    keyboard_focus False

                                    alt self_voicing_progressbar

                else:

                    frame:

                        style "invisible_frame"

                        xysize (536, 47)

                        if not IN_EVENT_WITH and not IN_ACTIVITY_WITH:

                            $ valid_activities = [(valid_activity, valid_activity.icon, valid_activity.display_name) for valid_activity in Activity.valid_activities()]

                            frame:

                                background Frame("gui/actions_box.png", Borders(10, 10, 10, 10)) xalign 0.5

                                xysize (450, 70)

                            hbox:

                                xalign 0.5

                                ypos 40

                                vbox:

                                    hbox spacing 5:

                                        for (action_object, action_icon, action_display_name) in valid_activities:

                                            fixed:

                                                fit_first True

                                                imagebutton:

                                                    auto f"button_{action_icon} %s"

                                                    focus_mask True

                                                    hovered SetScreenVariable("helper", (action_display_name, "activity"))

                                                    unhovered SetScreenVariable("helper", False)

                                                    action [SetScreenVariable("helper", False), Return(action_object)]

                                                    tooltip action_object

                                                    alt action_display_name

                                                use keep_at_it_button(action_object)

                    frame:

                        style "invisible_frame"

                        xysize (218, 47)

                frame:

                    xysize (80, 80)

                    style "invisible_frame"

                    imagebutton auto "lssb_visual_quality/ui/story_%s.svg":

                        align (0.5, 0.5)

                        if renpy.get_screen(["room", "story_tracker", "map", "housemap"]):

                            action ToggleScreen("story_tracker")

                        else:

                            sensitive False

                        alt "story tracker"

                    if IN_EVENT_WITH:

                        text "❗" align (0.5, 0.5) size 30 color "#96AEBE" outlines [(2, "#fff", 0, 0) ] alt ""

                        $ path_icon = "gui/action_icons/button_" + IN_EVENT_WITH + ".png"

                        if renpy.exists(path_icon):

                            add "gui/phone/ico_phone_insensitive.png" align (0.5, 0.5)

                            add path_icon align (0.5, 0.5)

        if not persistent.new_ui:

            use tooltip_old_ui


