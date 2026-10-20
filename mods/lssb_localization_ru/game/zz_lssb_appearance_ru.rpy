# Russian appearance controls. Native conditions, state values and actions are retained.
init 1011 python in lssb_appearance:
    import renpy as engine
    from store import renpy, config
    _constant = True
    version = "1.3.1"
    variant = "lssb_appearance_ru_26_8_0d"
    strings = {'Casual outfit': 'Повседневный наряд', 'Casual': 'Обычный наряд', 'Pure casual': 'Скромный наряд', 'Innocent casual': 'Невинный наряд', 'Date outfit': 'Наряд для свидания', 'Date': 'Обычный наряд', 'Sexy date': 'Сексуальный наряд', 'Slutty date': 'Откровенный наряд', 'Pure date': 'Скромный наряд', 'Swimsuit outfit': 'Купальник', 'Swimsuit': 'Обычный купальник', 'Sexy swimsuit': 'Сексуальный купальник', 'Slutty swimsuit': 'Откровенный купальник', 'Underwear outfit': 'Нижнее бельё', 'Underwear': 'Обычное бельё', 'Sexy underwear': 'Сексуальное бельё', 'Collar': 'Ошейник', 'Wear your collar': 'Надеть ошейник', 'Remove your collar': 'Снять ошейник', 'Piercings': 'Пирсинг', 'Pubes': 'Волосы на лобке', 'Shave your pussy': 'Побрить лобок', 'Stop shaving': 'Не бриться', 'Armpits': 'Подмышки', 'Shave your armpits': 'Побрить подмышки', 'Haircut': 'Причёска', 'Untie your hair': 'Распустить волосы', 'Tie your hair': 'Собрать волосы', 'Grow your hair': 'Отрастить волосы', 'Cut your hair': 'Подстричься', 'Dye your hair': 'Покрасить волосы', 'Undye your hair': 'Вернуть естественный цвет', 'Makeup': 'Макияж', 'Wear makeup': 'Нанести макияж', 'Remove makeup': 'Снять макияж', 'Clothes policy': 'Одежда дома', 'Clothed': 'В одежде', 'Topless': 'Без верха', 'Naked': 'Без одежды', 'Uniform policy': 'Как носить форму', 'Fully clothed': 'Полная форма', 'Work uniform': 'Рабочая форма', 'Casual uniform': 'Обычная форма', 'Sexy uniform': 'Сексуальная форма', 'Stripper outfit': 'Наряд для стриптиза', 'Stripper': 'Обычный наряд', 'Exit': 'Выход'}
    piercings = {'ears': 'Уши', 'nose': 'Нос', 'navel': 'Пупок', 'tongue': 'Язык', 'lips': 'Губы', 'eyebrow': 'Бровь', 'nipples': 'Соски', 'clit': 'Клитор', 'dick': 'Пенис'}

    def text(value):
        if engine.game.preferences.language == "russian":
            return strings.get(value, engine.translation.translate_string(value))
        return value

    def piercing(value):
        return piercings.get(value, value.capitalize()) if engine.game.preferences.language == "russian" else value.capitalize()

    class Panel(renpy.Displayable):
        def __init__(self, fill="#51aece", edge="#087797", opacity="0.90"):
            super(Panel, self).__init__()
            self.fill, self.edge, self.opacity = fill, edge, opacity

        def render(self, width, height, st, at):
            width, height = max(4, int(width)), max(4, int(height))
            if getattr(self, "_size", None) != (width, height):
                svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">'
                    '<rect x="1.25" y="1.25" width="%s" height="%s" rx="14" fill="%s" fill-opacity="%s" '
                    'stroke="%s" stroke-width="2.5"/></svg>') % (
                        width*4, height*4, width, height, width-2.5, height-2.5,
                        self.fill, self.opacity, self.edge)
                self._image = engine.display.im.Data(svg.encode("utf-8"), "lssb_appearance_panel.svg", oversample=4, mipmap=True)
                self._size = (width, height)
            return renpy.render(self._image, width, height, st, at)

    panel = Panel()
    idle = Panel("#51aece", "#087797", "0.94")
    hover = Panel("#72c7e5", "#f1fbff", "1.0")
    selected = Panel("#65badb", "#e8f8ff", "1.0")

    def enter():
        if False:
            return
        if variant not in config.variants:
            config.variants.insert(0, variant)
        # Native string lookup also covers the salon's dynamically formatted cost labels.
        translations = engine.game.script.translator.strings["russian"].translations
        for key, value in piercings.items():
            translations[key] = value
            translations[key.capitalize()] = value
            if key not in engine.store.Piercings.all_piercings:
                continue
            cost = engine.store.Piercings.all_piercings[key]
            suffix = " (" + str(cost) + "{image=gui/icons/icon_money.png})"
            translations[key.capitalize()+suffix] = value+suffix

    def leave():
        if variant in config.variants:
            config.variants.remove(variant)

    if True:
        config.language_callbacks["russian"].append(enter)
        for language in set(renpy.known_languages()) | {None}:
            if language != "russian":
                config.language_callbacks[language].append(leave)

style lssb_appearance_label is appearance_label
style lssb_appearance_label_text is appearance_label_text:
    size 28
    xsize 322
    layout "tex"

style lssb_appearance_items_vbox:
    spacing 6

style lssb_appearance_items_button is appearance_items_button:
    background lssb_appearance.idle
    idle_background lssb_appearance.idle
    hover_background lssb_appearance.hover
    selected_background lssb_appearance.selected
    selected_hover_background lssb_appearance.hover
    xsize 322
    ysize None
    yminimum 42
    padding (18, 7)

style lssb_appearance_items_button_text is appearance_items_button_text:
    xpos 0
    ypos 0
    xanchor 0
    yanchor 0
    xsize 286
    size 21
    layout "tex"
    color "#ffffff"

style lssb_appearance_submenu_items_vbox:
    xpos 16
    xsize 306
    spacing 6

style lssb_appearance_submenu_items_button is lssb_appearance_items_button:
    xsize 306

style lssb_appearance_submenu_items_button_text is lssb_appearance_items_button_text:
    xsize 270

style lssb_appearance_exit is lssb_appearance_items_button:
    xsize 360
    ysize 44
    padding (12, 0)

style lssb_appearance_exit_text is lssb_appearance_items_button_text:
    xsize None
    font "palanquin_bold"
    size 24
    align (0.5, 0.5)
    textalign 0.5

screen appearance(npc=None):
    variant "lssb_appearance_ru_26_8_0d"
    style_prefix "lssb_appearance"

    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Return()

    on "show" action [Hide("smartphone"), Hide("story_tracker"), Function(hide_people)]
    on "hide" action Function(show_people)

    default submenu = None
    default shown_npc = npc
    default shown_attributes = set()
    default refresh = False

    $ pierced_piercings = [v for _, v in shown_npc.piercings.items() if v.pierced]

    frame:
        background None
        if not shown_attributes:
            $ shown_attributes = {shown_npc.get_clothes()}
        $ shown_attributes.update({pi.location for pi in pierced_piercings if pi.worn})
        $ display_shown = " ".join(shown_attributes)
        add "[shown_npc.id] ['anim' if npc.id in anim_tag and persistent.live2d_on else ''] [display_shown]" xalign 0.25

    vbox:
        xalign 0.75
        ypos 100
        spacing 10
        xsize 360
        frame:
            ysize 435
            background lssb_appearance.panel
            padding (0, 0)
            add Solid("#d6f4ff99") xpos 18 ypos 46 xysize (324, 2)
            label "[npc.name]" xpos 18 ypos 5
            viewport id "inventory_vp":
                style_prefix "lssb_appearance_items"
                xsize 322
                xpos 18
                ypos 55
                ysize 352
                draggable True
                mousewheel True
                has vbox

                vbox:
                    xfill True
                    textbutton lssb_appearance.text('Casual outfit'):
                        action [
                                ToggleScreenVariable("submenu", "casual", None),
                                SetScreenVariable("shown_attributes", {"casual"})
                                ]
                        hovered If(not submenu, SetScreenVariable("shown_attributes", {"casual"}))
                if shown_npc.flags.giftpure_casual and (shown_npc.id != "reona" or shown_npc.purity >= 50) or shown_npc.flags.giftinnocent_casual:
                    if submenu == "casual":
                        vbox:
                            style_prefix "lssb_appearance_submenu_items"
                            xfill True
                            textbutton lssb_appearance.text('Casual'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.purecasual", False),
                                        SetField(shown_npc, "flags.innocentcasual", False),
                                        SetScreenVariable("shown_attributes", {"casual"})
                                        ]
                                selected not(shown_npc.flags.purecasual or shown_npc.flags.innocentcasual)
                                hovered [
                                        SetScreenVariable("shown_attributes", {"casual"})
                                        ]
                            if shown_npc.flags.giftpure_casual and (shown_npc.id != "reona" or shown_npc.purity >= 50):
                                textbutton lssb_appearance.text('Pure casual'):
                                    xpos 0
                                    action [
                                            SetField(shown_npc, "flags.purecasual", True),
                                            SetField(shown_npc, "flags.innocentcasual", False),
                                            SetScreenVariable("shown_attributes", {"casual"})
                                            ]
                                    selected shown_npc.flags.purecasual
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"purecasual"})
                                            ]
                            if shown_npc.flags.giftinnocent_casual:
                                textbutton lssb_appearance.text('Innocent casual'):
                                    xpos 0
                                    action [
                                            SetField(shown_npc, "flags.purecasual", False),
                                            SetField(shown_npc, "flags.innocentcasual", True),
                                            SetScreenVariable("shown_attributes", {"casual"})
                                            ]
                                    selected shown_npc.flags.innocentcasual
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"innocentcasual"})
                                            ]


                if (shown_npc.flags.giftsexy_dress and (shown_npc.id != "reona" or shown_npc.purity < 20)) or (shown_npc.flags.giftslutty_dress and (shown_npc.id != "reona" or shown_npc.purity < 10)) or (shown_npc.flags.giftpure_date and (shown_npc.id != "reona" or shown_npc.purity >= 60)):
                    vbox:
                        xfill True
                        textbutton lssb_appearance.text('Date outfit'):
                            action [
                                    ToggleScreenVariable("submenu", "date", None),
                                    SetScreenVariable("shown_attributes", {"date"})
                                    ]
                            hovered If(not submenu, SetScreenVariable("shown_attributes", {"date"}))
                    if submenu == "date":
                        vbox:
                            style_prefix "lssb_appearance_submenu_items"
                            xfill True
                            textbutton lssb_appearance.text('Date'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.sexydate", False),
                                        SetField(shown_npc, "flags.sluttydate", False),
                                        SetField(shown_npc, "flags.puredate", False),
                                        SetScreenVariable("shown_attributes", {"casual_date"})
                                        ]
                                selected not(shown_npc.flags.sexydate or shown_npc.flags.sluttydate or shown_npc.flags.puredate)
                                hovered [
                                        SetScreenVariable("shown_attributes", {"casual_date"})
                                        ]
                            if shown_npc.flags.giftsexy_dress and (shown_npc.id != "reona" or shown_npc.purity < 20):
                                textbutton lssb_appearance.text('Sexy date'):
                                    xpos 0
                                    action [
                                            SetField(shown_npc, "flags.sexydate", True),
                                            SetField(shown_npc, "flags.sluttydate", False),
                                            SetField(shown_npc, "flags.puredate", False),
                                            SetScreenVariable("shown_attributes", {"date"})
                                            ]
                                    selected shown_npc.flags.sexydate
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"sexydate"})
                                            ]
                            if shown_npc.flags.giftslutty_dress and (shown_npc.id != "reona" or shown_npc.purity < 10):
                                textbutton lssb_appearance.text('Slutty date'):
                                    xpos 0
                                    action [
                                            SetField(shown_npc, "flags.sexydate", False),
                                            SetField(shown_npc, "flags.sluttydate", True),
                                            SetField(shown_npc, "flags.puredate", False),
                                            SetScreenVariable("shown_attributes", {"date"})
                                            ]
                                    selected shown_npc.flags.sluttydate
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"sluttydate"})
                                            ]
                            if shown_npc.flags.giftpure_date and (shown_npc.id != "reona" or shown_npc.purity >= 60):
                                textbutton lssb_appearance.text('Pure date'):
                                    xpos 0
                                    action [
                                            SetField(shown_npc, "flags.sexydate", False),
                                            SetField(shown_npc, "flags.sluttydate", False),
                                            SetField(shown_npc, "flags.puredate", True),
                                            SetScreenVariable("shown_attributes", {"date"})
                                            ]
                                    selected shown_npc.flags.puredate
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"puredate"})
                                            ]


                if shown_npc.flags.giftsexy_swimsuit or shown_npc.flags.giftslutty_swimsuit:
                    vbox:
                        xfill True
                        textbutton lssb_appearance.text('Swimsuit outfit'):
                            action [
                                    ToggleScreenVariable("submenu", "swimsuit", None),
                                    SetScreenVariable("shown_attributes", {"swimsuit"})
                                    ]
                            hovered If(not submenu, SetScreenVariable("shown_attributes", {"swimsuit"}))
                    if submenu == "swimsuit":
                        vbox:
                            style_prefix "lssb_appearance_submenu_items"
                            xfill True
                            textbutton lssb_appearance.text('Swimsuit'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.sexyswimsuit", False),
                                        SetField(shown_npc, "flags.sluttyswimsuit", False),
                                        SetScreenVariable("shown_attributes", {"casual_swimsuit"})
                                        ]
                                selected not(shown_npc.flags.sexyswimsuit or shown_npc.flags.sluttyswimsuit)
                                hovered [
                                        SetScreenVariable("shown_attributes", {"casual_swimsuit"})
                                        ]
                            if shown_npc.flags.giftsexy_swimsuit:
                                textbutton lssb_appearance.text('Sexy swimsuit'):
                                    xpos 0
                                    action [
                                            SetField(shown_npc, "flags.sexyswimsuit", True),
                                            SetField(shown_npc, "flags.sluttyswimsuit", False),
                                            SetScreenVariable("shown_attributes", {"swimsuit"})
                                            ]
                                    selected shown_npc.flags.sexyswimsuit
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"sexyswimsuit"})
                                            ]
                            if shown_npc.flags.giftslutty_swimsuit:
                                textbutton lssb_appearance.text('Slutty swimsuit'):
                                    xpos 0
                                    action [
                                            SetField(shown_npc, "flags.sexyswimsuit", False),
                                            SetField(shown_npc, "flags.sluttyswimsuit", True),
                                            SetScreenVariable("shown_attributes", {"swimsuit"})
                                            ]
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"sluttyswimsuit"})
                                            ]
                                    selected shown_npc.flags.sluttyswimsuit


                if shown_npc.flags.giftlingerie and shown_npc.id in SEXY_UNDERWEAR_NPCS and (shown_npc.id != "reona" or (shown_npc.purity < 20 and shown_npc.sub >= 50)):
                    vbox:
                        xfill True
                        textbutton lssb_appearance.text('Underwear outfit'):
                            action [
                                    ToggleScreenVariable("submenu", "underwear", None),
                                    SetScreenVariable("shown_attributes", {"underwear"})
                                    ]
                            hovered If(not submenu, SetScreenVariable("shown_attributes", {"underwear"}))
                    if submenu == "underwear":
                        vbox:
                            style_prefix "lssb_appearance_submenu_items"
                            xfill True
                            textbutton lssb_appearance.text('Underwear'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.sexyunderwear", False),
                                        SetScreenVariable("shown_attributes", {"casual_underwear"})
                                        ]
                                selected not shown_npc.flags.sexyunderwear
                                hovered [
                                        SetScreenVariable("shown_attributes", {"casual_underwear"})
                                        ]
                            if shown_npc.flags.giftlingerie and shown_npc.id in SEXY_UNDERWEAR_NPCS and (shown_npc.id != "reona" or (shown_npc.purity < 20 and shown_npc.sub >= 50)):
                                textbutton lssb_appearance.text('Sexy underwear'):
                                    xpos 0
                                    action [
                                            SetField(shown_npc, "flags.sexyunderwear", True),
                                            SetScreenVariable("shown_attributes", {"underwear"})
                                            ]
                                    selected shown_npc.flags.sexyunderwear
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"sexyunderwear"})
                                            ]


                if shown_npc.flags.giftslave_collar:
                    vbox:
                        xfill True
                        textbutton lssb_appearance.text('Collar'):
                            action [
                                    ToggleScreenVariable("submenu", "collar", None)
                                    ]
                    if submenu == "collar":
                        vbox:
                            style_prefix "lssb_appearance_submenu_items"
                            xfill True
                            textbutton lssb_appearance.text('Wear your collar'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.collared", True),
                                        SetScreenVariable("shown_attributes", {})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"collar"})
                                        ]
                                selected shown_npc.flags.collared
                            textbutton lssb_appearance.text('Remove your collar'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.collared", False),
                                        SetScreenVariable("shown_attributes", {})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"-collar"})
                                        ]
                                selected not shown_npc.flags.collared


                if pierced_piercings:
                    vbox:
                        xfill True
                        textbutton lssb_appearance.text('Piercings'):
                            action [
                                    ToggleScreenVariable("submenu", "piercings", None),
                                    SetScreenVariable("shown_attributes", {"naked"})
                                    ]
                            hovered If(not submenu, SetScreenVariable("shown_attributes", {"naked"}.union({pi.location for pi in pierced_piercings if pi.worn})))
                    if submenu == "piercings":
                        vbox:
                            style_prefix "lssb_appearance_submenu_items"
                            xfill True
                            for piercing in pierced_piercings:
                                textbutton lssb_appearance.piercing(piercing.location):
                                    selected piercing.worn
                                    xpos 0
                                    action [
                                            ToggleField(shown_npc.piercings, f"{piercing.location}.worn", True, False),
                                            ToggleSetMembership(shown_attributes, piercing.location)
                                            ]


                if shown_npc.is_female and shown_npc.sub >= 75:
                    vbox:
                        xfill True
                        textbutton lssb_appearance.text('Pubes'):
                            action [
                                    ToggleScreenVariable("submenu", "pubes", None),
                                    SetScreenVariable("shown_attributes", {"naked"})
                                    ]
                            hovered If(not submenu, SetScreenVariable("shown_attributes", {"naked", "pubes" if shown_npc.flags.pubes else ""}))
                    if submenu == "pubes":
                        vbox:
                            style_prefix "lssb_appearance_submenu_items"
                            xfill True
                            textbutton lssb_appearance.text('Shave your pussy'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.pubes", False),
                                        SetScreenVariable("shown_attributes", {"naked"})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"naked", "-pubes"})
                                        ]
                                selected not shown_npc.flags.pubes
                            textbutton lssb_appearance.text('Stop shaving'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.pubes", True),
                                        SetScreenVariable("shown_attributes", {"naked"})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"naked", "pubes"})
                                        ]
                                selected shown_npc.flags.pubes


                if shown_npc.id in ["hanna"] and shown_npc.is_female and shown_npc.sub >= 50:
                    vbox:
                        xfill True
                        textbutton lssb_appearance.text('Armpits'):
                            action [
                                    ToggleScreenVariable("submenu", "armpits", None),
                                    SetScreenVariable("shown_attributes", {"naked"})
                                    ]
                    if submenu == "armpits":
                        vbox:
                            style_prefix "lssb_appearance_submenu_items"
                            xfill True
                            textbutton lssb_appearance.text('Shave your armpits'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.armpits", False),
                                        SetScreenVariable("shown_attributes", {})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"-armpits"})
                                        ]
                                selected not shown_npc.flags.armpits
                            textbutton lssb_appearance.text('Stop shaving'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.armpits", True),
                                        SetScreenVariable("shown_attributes", {})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"armpits"})
                                        ]
                                selected shown_npc.flags.armpits


                if shown_npc.id in ["aletta", "camila", "kleio", "minami", "sasha", "reona", "cherie", "claire", "kiara"] and shown_npc.sub >= 25 and not shown_npc.flags.haircutDelay:
                    if shown_npc.id == "aletta" and ("aletta_event_03b" in DONE or "aletta_event_05b" in DONE) and shown_npc.sub >= 50:
                        $ text_do = "Untie your hair"
                        $ text_undo = "Tie your hair"
                    elif shown_npc.id == "camila" and "camila_event_06" in DONE:
                        $ text_do = "Tie your hair"
                        $ text_undo = "Untie your hair"
                    elif shown_npc.id == "kleio" and "kleio_twintails_02" in DONE and shown_npc.sub >= 35:
                        $ text_do = "Grow your hair"
                        $ text_undo = "Cut your hair"
                    elif shown_npc.id == "minami" and "minami_likes_blondes" in DONE:
                        $ text_do = "Dye your hair"
                        $ text_undo = "Undye your hair"
                    elif shown_npc.id == "sasha" and "sasha_likes_blondes_2" in DONE:
                        $ text_do = "Dye your hair"
                        $ text_undo = "Undye your hair"
                    elif shown_npc.id == "reona" and shown_npc.purity >= 50:
                        $ text_do = "Undye your hair"
                        $ text_undo = "Dye your hair"
                    elif shown_npc.id == "cherie":
                        $ text_do = "Tie your hair"
                        $ text_undo = "Untie your hair"
                    elif shown_npc.id == "claire":
                        $ text_do = "Untie your hair"
                        $ text_undo = "Tie your hair"
                    elif shown_npc.id == "kiara":
                        $ text_do = "Tie your hair"
                        $ text_undo = "Untie your hair"
                    else:
                        $ text_do = None
                        $ text_undo = None

                    if text_do:
                        vbox:
                            xfill True
                            textbutton lssb_appearance.text('Haircut'):
                                action [
                                        ToggleScreenVariable("submenu", "haircut", None)
                                        ]
                            if submenu == "haircut":
                                vbox:
                                    style_prefix "lssb_appearance_submenu_items"
                                    xfill True
                                    textbutton lssb_appearance.text(text_do):
                                        xpos 0
                                        action [
                                                SetField(shown_npc, "flags.haircut", True),
                                                SetScreenVariable("shown_attributes", {})
                                                ]
                                        hovered [
                                                SetScreenVariable("shown_attributes", {"haircut"})
                                                ]
                                        selected shown_npc.flags.haircut
                                    textbutton lssb_appearance.text(text_undo):
                                        xpos 0
                                        action [
                                                SetField(shown_npc, "flags.haircut", False),
                                                SetScreenVariable("shown_attributes", {})
                                                ]
                                        hovered [
                                                SetScreenVariable("shown_attributes", {"nohaircut"})
                                                ]
                                        selected not shown_npc.flags.haircut


                if shown_npc.id in ["morgan"] and shown_npc.male < 40:
                    vbox:
                        xfill True
                        textbutton lssb_appearance.text('Makeup'):
                            action [
                                    ToggleScreenVariable("submenu", "makeup", None),
                                    ]

                    if submenu == "makeup":
                        vbox:
                            style_prefix "lssb_appearance_submenu_items"
                            xfill True
                            textbutton lssb_appearance.text('Wear makeup'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.nomakeup", False),
                                        SetScreenVariable("shown_attributes", {})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"makeup"})
                                        ]
                                selected not shown_npc.flags.nomakeup
                            textbutton lssb_appearance.text('Remove makeup'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.nomakeup", True),
                                        SetScreenVariable("shown_attributes", {})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"-makeup"})
                                        ]
                                selected shown_npc.flags.nomakeup


                if shown_npc.id in ["bree", "lexi", "minami", "samantha", "sasha"] and shown_npc.sub >= 90:
                    vbox:
                        xfill True
                        label "At home:"
                        textbutton lssb_appearance.text('Clothes policy'):
                            action [
                                    ToggleScreenVariable("submenu", "home_policy", None),
                                    SetScreenVariable("shown_attributes", {"casual"}),
                                    ]
                            hovered [
                                    If(not submenu, SetScreenVariable("shown_attributes", {"casual", "topless" if shown_npc.flags.topless else "", "naked" if shown_npc.flags.naked else ""})),
                                    ]
                    if submenu == "home_policy":
                        vbox:
                            style_prefix "lssb_appearance_submenu_items"
                            xfill True
                            textbutton lssb_appearance.text('Clothed'):
                                xpos 0
                                action [
                                            SetField(shown_npc, "flags.topless", False),
                                            SetField(shown_npc, "flags.naked", False),
                                            SetScreenVariable("shown_attributes", {"casual"})
                                            ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"casual", "-topless", "-naked"})
                                        ]
                                selected not (shown_npc.flags.topless or shown_npc.flags.naked)
                            textbutton lssb_appearance.text('Topless'):
                                xpos 0
                                action [
                                            SetField(shown_npc, "flags.topless", True),
                                            SetField(shown_npc, "flags.naked", False),
                                            SetScreenVariable("shown_attributes", {"casual", "topless"})
                                            ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"casual", "topless"})
                                        ]
                                selected shown_npc.flags.topless
                            textbutton lssb_appearance.text('Naked'):
                                xpos 0
                                action [
                                            SetField(shown_npc, "flags.topless", False),
                                            SetField(shown_npc, "flags.naked", True),
                                            SetScreenVariable("shown_attributes", {"casual", "naked"})
                                            ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"casual", "naked"})
                                        ]
                                selected shown_npc.flags.naked



                if shown_npc.id == "cassidy" and shown_npc.status in ["pet", "sex slave"]:
                    vbox:
                        xfill True
                        label "At work:"
                    vbox:
                        xfill True
                        textbutton lssb_appearance.text('Uniform policy'):
                            action [
                                    ToggleScreenVariable("submenu", "work_policy", None),
                                    SetScreenVariable("shown_attributes", {"work"}),
                                    ]
                            hovered [
                                    If(not submenu, SetScreenVariable("shown_attributes", {"work"})),
                                    ]
                    if submenu == "work_policy":
                        vbox:
                            xfill True
                            style_prefix "lssb_appearance_submenu_items"
                            textbutton lssb_appearance.text('Fully clothed'):
                                xpos 0
                                action [
                                            SetField(shown_npc, "flags.topless", False),
                                            SetScreenVariable("shown_attributes", {"work"})
                                            ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"work", "-topless"})
                                        ]
                                selected not (shown_npc.flags.topless or shown_npc.flags.naked)
                            textbutton lssb_appearance.text('Topless'):
                                xpos 0
                                action [
                                            SetField(shown_npc, "flags.topless", True),
                                            SetScreenVariable("shown_attributes", {"work", "topless"})
                                            ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"work", "topless"})
                                        ]
                                selected shown_npc.flags.topless



                if shown_npc.id == "cherie" and game.flags.isceo and shown_npc.sub >= 90:
                    vbox:
                        xfill True
                        label "At work:"
                    vbox:
                        xfill True
                        textbutton lssb_appearance.text('Uniform policy'):
                            action [
                                    ToggleScreenVariable("submenu", "work_policy", None),
                                    SetScreenVariable("shown_attributes", {"work"}),
                                    ]
                            hovered [
                                    If(not submenu, SetScreenVariable("shown_attributes", {"work", "naked" if shown_npc.flags.naked else ""})),
                                    ]
                    if submenu == "work_policy":
                        vbox:
                            xfill True
                            style_prefix "lssb_appearance_submenu_items"
                            textbutton lssb_appearance.text('Fully clothed'):
                                xpos 0
                                action [
                                            SetField(shown_npc, "flags.naked", False),
                                            SetScreenVariable("shown_attributes", {"work"})
                                            ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"work", "-naked"})
                                        ]
                                selected not shown_npc.flags.naked
                            textbutton lssb_appearance.text('Naked'):
                                xpos 0
                                action [
                                            SetField(shown_npc, "flags.naked", True),
                                            SetScreenVariable("shown_attributes", {"work", "naked"})
                                            ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"work", "naked"})
                                        ]
                                selected shown_npc.flags.naked

                if shown_npc.id in ["aletta", "audrey", "lavish", "shiori"] and game.flags.isceo and shown_npc.sub >= 50:
                    vbox:
                        xfill True
                        label "At work:"

                    if shown_npc.sub >= 90:
                        vbox:
                            xfill True
                            textbutton lssb_appearance.text('Uniform policy'):
                                action [
                                        ToggleScreenVariable("submenu", "work_policy", None),
                                        SetScreenVariable("shown_attributes", {"work"}),
                                        ]
                                hovered [
                                        If(not submenu, SetScreenVariable("shown_attributes", {"work", "topless" if shown_npc.flags.topless else ""})),
                                        ]
                        if submenu == "work_policy":
                            vbox:
                                xfill True
                                style_prefix "lssb_appearance_submenu_items"
                                textbutton lssb_appearance.text('Fully clothed'):
                                    xpos 0
                                    action [
                                                SetField(shown_npc, "flags.topless", False),
                                                SetScreenVariable("shown_attributes", {"work"}),
                                                ]
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"work", "-topless"})
                                            ]
                                    selected not shown_npc.flags.topless
                                textbutton lssb_appearance.text('Topless'):
                                    xpos 0
                                    action [
                                                SetField(shown_npc, "flags.topless", True),
                                                SetScreenVariable("shown_attributes", {"work", "topless"})
                                                ]
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"work", "topless"})
                                            ]
                                    selected shown_npc.flags.topless

                    vbox:
                        xfill True
                        textbutton lssb_appearance.text('Work uniform'):
                            action [
                                    ToggleScreenVariable("submenu", "work", None),
                                    SetScreenVariable("shown_attributes", {"work"}),
                                    ]
                            hovered [
                                    If(not submenu, SetScreenVariable("shown_attributes", {"work", "topless" if shown_npc.flags.topless else ""})),
                                    ]
                    if submenu == "work":
                        vbox:
                            style_prefix "lssb_appearance_submenu_items"
                            xfill True
                            textbutton lssb_appearance.text('Casual uniform'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.sexywork", False),
                                        SetScreenVariable("shown_attributes", {"work", "topless" if shown_npc.flags.topless else ""}),
                                        ]
                                selected not shown_npc.flags.sexywork
                                hovered [
                                        SetScreenVariable("shown_attributes", {"work", "topless" if shown_npc.flags.topless else ""}),
                                        ]
                            textbutton lssb_appearance.text('Sexy uniform'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.sexywork", True),
                                        SetScreenVariable("shown_attributes", {"sexywork", "topless" if shown_npc.flags.topless else ""}),
                                        ]
                                selected shown_npc.flags.sexywork
                                hovered [
                                        SetScreenVariable("shown_attributes", {"sexywork", "topless" if shown_npc.flags.topless else ""}),
                                        ]

                if shown_npc.id in ["bree", "hanna", "harmony", "lexi", "reona", "shiori"] and (shown_npc.flags.schedule == "stripclub" or shown_npc.flags.work_stripclub) and ((shown_npc.flags.giftsexy_dress and (shown_npc.id != "reona" or shown_npc.purity < 20)) or (shown_npc.flags.giftslutty_dress and (shown_npc.id != "reona" or shown_npc.purity < 10))):
                    vbox:
                        xfill True
                        label "At the stripclub:"

                    vbox:
                        xfill True
                        textbutton lssb_appearance.text('Stripper outfit'):
                            action [
                                    ToggleScreenVariable("submenu", "stripclub", None),
                                    SetScreenVariable("shown_attributes", {shown_npc.flags.stripper_outfit if shown_npc.flags.stripper_outfit else "stripper"}),
                                    ]
                            hovered [
                                    If(not submenu, SetScreenVariable("shown_attributes", {shown_npc.flags.stripper_outfit if shown_npc.flags.stripper_outfit else "stripper"})),
                                    ]
                    if submenu == "stripclub":
                        vbox:
                            style_prefix "lssb_appearance_submenu_items"
                            xfill True
                            textbutton lssb_appearance.text('Stripper'):
                                xpos 0
                                action [
                                        SetField(shown_npc, "flags.stripper_outfit", "stripper"),
                                        SetScreenVariable("shown_attributes", {"stripper",}),
                                        ]
                                selected shown_npc.flags.stripper_outfit == "stripper" or not shown_npc.flags.stripper_outfit
                                hovered [
                                        SetScreenVariable("shown_attributes", {"stripper"}),
                                        ]
                            if shown_npc.flags.giftsexy_dress and (shown_npc.id != "reona" or shown_npc.purity < 20):
                                textbutton lssb_appearance.text('Sexy date'):
                                    xpos 0
                                    action [
                                            SetField(shown_npc, "flags.stripper_outfit", "sexydate"),
                                            SetScreenVariable("shown_attributes", {"sexydate"}),
                                            ]
                                    selected shown_npc.flags.stripper_outfit == "sexydate"
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"sexydate"}),
                                            ]
                            if shown_npc.flags.giftslutty_dress and (shown_npc.id != "reona" or shown_npc.purity < 10):
                                textbutton lssb_appearance.text('Slutty date'):
                                    xpos 0
                                    action [
                                            SetField(shown_npc, "flags.stripper_outfit", "sluttydate"),
                                            SetScreenVariable("shown_attributes", {"sluttydate"}),
                                            ]
                                    selected shown_npc.flags.stripper_outfit == "sluttydate"
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"sluttydate"}),
                                            ]

            vbar value YScrollValue("inventory_vp") left_bar "gui/inv/vertical_idle_bar.png" thumb "gui/inv/vertical_idle_thumb.png" right_bar "gui/inv/vertical_idle_bar.png" xmaximum 8 ymaximum 352 xpos 346 ypos 55 unscrollable "hide"

        textbutton lssb_appearance.text("Exit"):
            id "lssb_appearance_exit"
            style "lssb_appearance_exit"
            action [SetScreenVariable("shown_attributes", {shown_npc.get_clothes()}), Function(hero.cancel_activity), Return()]

        if config.developer:
            vbox:
                text "[shown_npc.id] [display_shown]" color "#ff0000"
                text "[submenu]" color "#ff0000"


