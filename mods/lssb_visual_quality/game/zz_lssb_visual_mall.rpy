# Mall map extension. All gameplay actions remain those of the native screen.
init 1004 python:
    if renpy.has_image("mallmap", exact=True):
        _lssb_visual_ui_ru_labels.update({'Mall Southside': 'Южное крыло', 'Mall Northside': 'Северное крыло', 'Arcade': 'Игровые автоматы', 'Electronic Store': 'Электроника', 'Coffee Shop': 'Кофейня', 'Jewelry Store': 'Ювелирный магазин', 'Clothes Shop': 'Магазин одежды', 'Drug Store': 'Аптека', 'Bakery': 'Пекарня', 'Book Store': 'Книжный магазин', 'Flower Shop': 'Цветочный магазин', 'Tattoo Shop': 'Тату-салон', 'Tattoo Parlor': 'Тату-салон', 'Tattooshop': 'Тату-салон'})
        # Replace the leaf image. The native layeredimage and its name are retained.
        renpy.image("mallmap", Image("lssb_visual_quality/maps/mallmap.webp", oversample=4, mipmap=True))

screen mallmap(locations):
    variant "lssb_visual_ui_26_8_0d"
    if not (renpy.get_screen("smartphone") or renpy.get_screen("story_tracker")):
        default destination = ""
        fixed:
            at master_bleed
            add "bg mallmap"
            imagebutton auto "gui/map/city_%s.png" action SetVariable("game.room", "map"), Return() xpos 1100 ypos 600 xanchor 0.5 yanchor 0.5 alt _lssb_visual_ui_translate("City")
            text _lssb_visual_ui_translate("City") font "exo2_bold" size 26 outlines [(1, "#083449")] color "#ffffff" xpos 1100 ypos 680 xanchor 0.5 yanchor 0.5 alt ""
            for location in [l for l in locations if l.id in mallmap_location_positions]:
                $ x, y = mallmap_location_positions[location.id]
                $ girls = location.get_present_girls_ids()
                $ glist = ""
                for index, girl in enumerate(girls[:6]):
                    $ glist += f"; {girl}"
                $ self_voicing_location = _lssb_visual_ui_translate(location.display_name) + "; " + glist
                imagebutton auto "lssb_visual_quality/ui/map_hex_%s.svg" xpos x ypos y xanchor 0.5 yanchor 0.5 alt self_voicing_location:
                    action [SetVariable("game.room", location.id), Return()]
                    hovered SetScreenVariable("destination", location)
                    unhovered SetScreenVariable("destination", "")
                for index, g in enumerate(girls[:6]):
                    $ x_g = x
                    $ y_g = y
                    if index == 1:
                        $ y_g += 35
                    elif index:
                        if index in [2, 4]:
                            $ x_g += 29
                        else:
                            $ x_g = x - 29
                        if index in [2, 3]:
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
                        add "notify " + g
                if location.id == "mall1":
                    $ location_name = "Mall Southside"
                elif location.id == "mall2":
                    $ location_name = "Mall Northside"
                else:
                    $ location_name = location.display_name
                use _lssb_visual_map_label(location_name, x, y, location.id)
        if destination:
            if destination.id == "mall1":
                $ destination_name = "Mall"
            else:
                $ destination_name = destination.display_name
            vbox:
                align (0.5, 0.1)
                spacing 20
                text _lssb_visual_ui_translate(destination_name) font "exo2_bold" outlines [(1, "#083449")] color "#ffffff" size 32 xalign 0.5 xmaximum 780 text_align 0.5
                hbox:
                    xalign 0.5
                    box_justify True
                    spacing 5
                    for p in destination.get_present_girls_ids():
                        add Composite(
                            (50, 50),
                            (0, 0), Transform("gui/phone/ico_phone_idle.png", zoom=0.8),
                            (7, 7), f"gui/action_icons/button_{p}.png"
                            ):
                            at Position(anchor=(0.5, 0.5))

