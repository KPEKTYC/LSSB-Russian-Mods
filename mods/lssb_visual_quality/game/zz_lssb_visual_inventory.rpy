# Crisp inventory panels and bounded text. Item data and actions stay native.
init 1007 python:
    _lssb_inventory_variant = "lssb_inventory_26_8_0d"

    def _lssb_inventory_text(value):
        if hasattr(store, "_lssb_ui_translate"):
            return _lssb_ui_translate(value)
        return renpy.translation.translate_string(value)

    _lssb_inventory_measure_cache = {}

    def _lssb_inventory_equipment_layout():
        clothes, accessory = hero.equipment_for_ui
        heights = []
        for value in (clothes, accessory):
            text = renpy.substitute(_lssb_inventory_text(value or "None"))
            if text not in _lssb_inventory_measure_cache:
                probe = Text(text, substitute=False, style="inventory_text", size=19, xsize=208, layout="tex")
                _lssb_inventory_measure_cache[text] = max(50, int(renpy.render(probe,208,720,0.,0.).get_size()[1]))
            heights.append(_lssb_inventory_measure_cache[text])
        return clothes, accessory, heights[0], heights[1], 32 + sum(heights)

    class _LssbInventoryPanel(renpy.Displayable):
        def __init__(self, fill="#48a9c8", edge="#087a98", opacity=".82"):
            super(_LssbInventoryPanel, self).__init__()
            self.fill, self.edge, self.opacity = fill, edge, opacity

        def render(self, width, height, st, at):
            width, height = max(4, int(width)), max(4, int(height))
            if getattr(self, "_size", None) != (width, height):
                # One complete shape, rasterized at 4x density. No stretched
                # bitmap corners and no separate Frame slices at fractional DPI.
                svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">'
                    '<rect x="1.25" y="1.25" width="%s" height="%s" rx="14" fill="%s" fill-opacity="%s" '
                    'stroke="%s" stroke-width="2.5"/></svg>') % (
                        width*4, height*4, width, height, width-2.5, height-2.5,
                        self.fill, self.opacity, self.edge)
                self._image = renpy.display.im.Data(svg.encode("utf-8"), "lssb_inventory_panel.svg", oversample=4, mipmap=True)
                self._size = (width, height)
            return renpy.render(self._image, width, height, st, at)

    def _lssb_inventory_activate():
        _lssb_inventory_measure_cache.clear()
        if True:
            if _lssb_inventory_variant in config.variants:
                config.variants.remove(_lssb_inventory_variant)
            config.variants.insert(0, _lssb_inventory_variant)

    for _lssb_inventory_language in set(renpy.known_languages()) | {None, "russian"}:
        config.language_callbacks[_lssb_inventory_language].append(_lssb_inventory_activate)
    _lssb_inventory_activate()

style lssb_inventory_row_button is inventory_items_button:
    padding (0, 4)
    ysize None
    yminimum 32

style lssb_inventory_row_text is inventory_items_text:
    size 19
    # TeX wrapping accounts for the final glyph at the column boundary.
    # Greedy wrapping in the bundled engine can overshoot it by a few pixels.
    layout "tex"
screen inventory():
    variant "lssb_inventory_26_8_0d"
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
        id "lssb_inventory_window"
        ypos 80
        spacing 10
        xsize 360
        $ clothes, accessory, clothes_height, accessory_height, equipment_height = _lssb_inventory_equipment_layout()
        $ inventory_panel_height = 532 - equipment_height
        frame:
            id "lssb_inventory_equipment_panel"
            xysize (360, equipment_height)
            padding (0, 0)
            background _LssbInventoryPanel()
            vbox:
                pos (16, 12)
                xsize 328
                spacing 8
                fixed:
                    xysize (328, clothes_height)
                    text _lssb_inventory_text("Clothes:") id "lssb_inventory_clothes_label" xsize 112 size 18 font "exo2_bold" color "#ffffff"
                    text _lssb_inventory_text(clothes or "None") id "lssb_inventory_clothes_value" xpos 120 xsize 208 size 19 layout "tex" color "#ffffff"
                fixed:
                    xysize (328, accessory_height)
                    text _lssb_inventory_text("Accessory:") id "lssb_inventory_accessory_label" xsize 112 size 18 font "exo2_bold" color "#ffffff"
                    text _lssb_inventory_text(accessory or "None") id "lssb_inventory_accessory_value" xpos 120 xsize 208 size 19 layout "tex" color "#ffffff"
        frame:
            id "lssb_inventory_list_panel"
            xysize (360, inventory_panel_height)
            padding (0, 0)
            background _LssbInventoryPanel()
            text _lssb_inventory_text("Inventory") id "lssb_inventory_title" pos (16, 10) size 27 font "exo2_bold" color "#ffffff" xmaximum 328
            add Solid("#c9f0fa99") id "lssb_inventory_separator" pos (16, 102) xysize (328, 1)
            hbox:
                pos (16, 56)
                spacing 8
                textbutton "🗑️":
                    text_size 18
                    xysize (30, 34)
                    action ToggleVariable("discard_mode")
                    style ("filter_title_select" if discard_mode else "filter_title")
                hbox:
                    spacing 4
                    text _lssb_inventory_text("Filter: ") size 17 yalign 0.5 alt ""

                    $ filters = {
                        "gift": ("🎁", "gift", Gift),
                        "equip": ("👔", "equip", Equip),
                        "cons": ("🫙", "consumable", Consumable),
                        "othe": ("📦", "other", Item)
                    }
                    for filter_name, (icon, alt_text, _) in filters.items():
                        textbutton icon:
                            xysize (30, 34)
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
                    xsize 312
                    pos (16, 114)
                    ysize (inventory_panel_height - 130)
                    draggable True
                    mousewheel True
                    $ cls = filters.get(store.inventory_filter, (None, None, ItemBase))[2]
                    $ items = cls.filtered_sort(filter=lambda x: x.name in hero.inventory, key=lambda x: x.display_name)
                    vbox:
                        for item in items:
                            if discard_mode and item.one_only:
                                continue
                            $ t = _lssb_inventory_text(item.display_name)
                            $ n = hero.has_item(item.name)
                            if n > 1:
                                $ t += " ({})".format(n)
                            $ is_valid_equip = (isinstance(item, Equip) and game.room in ["bedroom1", "bedroom4"])
                            $ is_valid_consum = (isinstance(item, Consumable) and not game.flags[item.name] and item.test())
                            $ is_sensitive = is_valid_equip or is_valid_consum
                            hbox:
                                xsize 312
                                spacing 6
                                if discard_mode:
                                    button:
                                        xysize (22, 32)
                                        yalign 0.5
                                        text "❌" align (0.0, 0.5) style "inventory_items_text_icon" alt "" size 12
                                        action Function(hero.lose_item, item)
                                frame:
                                    xsize (284 if discard_mode else 312)
                                    ysize None
                                    padding (0, 0)
                                    style "invisible_frame"
                                    has fixed
                                    fit_first "height"
                                    button:
                                        id ("lssb_inventory_item_" + item.id)
                                        style "lssb_inventory_row_button"
                                        if discard_mode:
                                            action NullAction()
                                            sensitive False
                                        else:
                                            action Return(item)
                                            sensitive is_sensitive
                                        xfill True
                                        yalign 0.5
                                        fixed:
                                            fit_first "height"
                                            xsize (284 if discard_mode else 312)
                                            text t id ("lssb_inventory_name_" + item.id) xsize (248 if discard_mode else 276) style "lssb_inventory_row_text":
                                                align (0.0, 0.5)
                                                alt t + ". " + replace_tags_alt(" ".join(item.get_tooltip(True)))
                                            text item.icon id ("lssb_inventory_icon_" + item.id) align (1.0, 0.5) style "inventory_items_text_icon" alt ""
                                        tooltip item
                                    if not is_sensitive:
                                        $ insensitive_tooltip = ""
                                        if not is_valid_equip and isinstance(item, Equip):
                                            $ insensitive_tooltip += _lssb_inventory_text("{color=#ddddddcc}Can only be equipped in bedroom{/color}")
                                        elif not is_valid_consum and isinstance(item, Consumable):
                                            $ insensitive_tooltip += _lssb_inventory_text("{color=#ddddddcc}Need to wait a ")
                                            if (item.frequency_limit):
                                                $ insensitive_tooltip += _lssb_inventory_text(item.frequency_limit)
                                            else:
                                                $ insensitive_tooltip += _lssb_inventory_text("bit")
                                            $ insensitive_tooltip += _lssb_inventory_text(" between use{/color}")
                                        elif isinstance(item, Gift):
                                            $ insensitive_tooltip += _lssb_inventory_text("{color=#ddddddcc}A gift for someone{/color}")

                                        button:
                                            style "invisible_button"
                                            action NullAction()
                                            xfill True
                                            yfill True
                                            yalign 0.5
                                            tooltip insensitive_tooltip
                                            keyboard_focus False
                                            alt t + " not usable now. " + replace_tags_alt(" ".join(insensitive_tooltip))

                vbar value YScrollValue("inventory_vp") left_bar "gui/inv/vertical_idle_bar.png" thumb "gui/inv/vertical_idle_thumb.png" right_bar "gui/inv/vertical_idle_bar.png" xmaximum 12 ymaximum (inventory_panel_height - 130) xpos 332 ypos 114 unscrollable "hide" alt "scroll "
        fixed:
            xysize (360, 48)
            imagebutton id "lssb_inventory_exit_button" xysize (360, 48) idle _LssbInventoryPanel() hover _LssbInventoryPanel("#66c1db", "#daf5ff", ".94") action [SetVariable("inventory_filter", None), SetVariable("discard_mode", False), Return("exit")] keysym "game_menu" alt "Exit"
            text _lssb_inventory_text("Exit") id "lssb_inventory_exit_text" color "#ffffff" font "exo2_bold" size 23 align (0.5, 0.5) yoffset -3 alt ""

    if persistent.new_ui:
        use tooltip
    else:
        use tooltip_old_ui



screen choose_gift(exc=None):
    variant "lssb_inventory_26_8_0d"
    style_prefix "inventory"
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Return("exit")
    button pos (0, 0) xsize 1280 ysize 720 action Return("exit")
    on "show" action [Hide("quick_menu"), Hide("say")]
    vbox:
        xalign 0.75
        id "lssb_inventory_window"
        ypos 80
        spacing 10
        xsize 360
        $ clothes, accessory, clothes_height, accessory_height, equipment_height = _lssb_inventory_equipment_layout()
        $ inventory_panel_height = 532 - equipment_height
        frame:
            id "lssb_inventory_equipment_panel"
            xysize (360, equipment_height)
            padding (0, 0)
            background _LssbInventoryPanel()
            vbox:
                pos (16, 12)
                xsize 328
                spacing 8
                fixed:
                    xysize (328, clothes_height)
                    text _lssb_inventory_text("Clothes:") id "lssb_inventory_clothes_label" xsize 112 size 18 font "exo2_bold" color "#ffffff"
                    text _lssb_inventory_text(clothes or "None") id "lssb_inventory_clothes_value" xpos 120 xsize 208 size 19 layout "tex" color "#ffffff"
                fixed:
                    xysize (328, accessory_height)
                    text _lssb_inventory_text("Accessory:") id "lssb_inventory_accessory_label" xsize 112 size 18 font "exo2_bold" color "#ffffff"
                    text _lssb_inventory_text(accessory or "None") id "lssb_inventory_accessory_value" xpos 120 xsize 208 size 19 layout "tex" color "#ffffff"
        frame:
            id "lssb_inventory_list_panel"
            xysize (360, inventory_panel_height)
            padding (0, 0)
            background _LssbInventoryPanel()
            text _lssb_inventory_text("Gift") id "lssb_inventory_title" pos (16, 10) size 27 font "exo2_bold" color "#ffffff" xmaximum 328
            add Solid("#c9f0fa99") id "lssb_inventory_separator" pos (16, 56) xysize (328, 1)
            if hero.inventory:
                viewport id "inventory_vp":
                    style_prefix "inventory_items"
                    xsize 312
                    pos (16, 70)
                    ysize (inventory_panel_height - 86)
                    draggable True
                    mousewheel True
                    has vbox
                    for item in Gift.filtered_sort(
                            filter=lambda x: x.name in hero.inventory,
                            key=lambda x: x.display_name,
                        ):
                        $ t = _lssb_inventory_text(item.display_name)
                        $ n = hero.has_item(item.name)
                        if n > 1:
                            $ t += " ({})".format(n)
                        hbox:
                            xsize 312
                            button action Return(item):
                                id ("lssb_inventory_item_" + item.id)
                                style "lssb_inventory_row_button"
                                xsize 312
                                has fixed
                                fit_first "height"
                                xsize 312
                                text t id ("lssb_inventory_name_" + item.id) xsize 276 style "lssb_inventory_row_text" yalign 0.5
                                text item.icon id ("lssb_inventory_icon_" + item.id) align (1.0, 0.5) style "inventory_items_text_icon"
                vbar value YScrollValue("inventory_vp") left_bar "gui/inv/vertical_idle_bar.png" thumb "gui/inv/vertical_idle_thumb.png" right_bar "gui/inv/vertical_idle_bar.png" xmaximum 12 ymaximum (inventory_panel_height - 86) xpos 332 ypos 70 unscrollable "hide" alt "scroll "
        fixed:
            xysize (360, 48)
            imagebutton id "lssb_inventory_exit_button" xysize (360, 48) idle _LssbInventoryPanel() hover _LssbInventoryPanel("#66c1db", "#daf5ff", ".94") action Return("exit")
            text _lssb_inventory_text("Exit") id "lssb_inventory_exit_text" color "#ffffff" font "exo2_bold" size 23 align (0.5, 0.5) yoffset -3

