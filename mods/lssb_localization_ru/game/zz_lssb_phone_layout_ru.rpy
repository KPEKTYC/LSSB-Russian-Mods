# Display-only call screens. Native caller keys still select the portraits.
# Capture contracts before Ren'Py prepares and caches the screen trees.
init 971 python:
    _lssb_phone_expected = {
        "smartphone_choice": "ceceda6585a52b4ff7b02b7ccf845a7d1874d0eb306871b7a0e11cfc8f69c9c2",
        "smartphone_calling": "2563d0b361016c46cf70911a13df68626cafb982875d311f00891818493fa24e",
    }
    for _lssb_phone_screen, _lssb_phone_hash in _lssb_phone_expected.items():
        _lssb_phone_native = renpy.display.screen.screens.get((_lssb_phone_screen, None))
        try:
            _lssb_phone_actual = lssb_compat._module.fingerprint(_lssb_phone_native.function) if _lssb_phone_native else None
        except Exception:
            _lssb_phone_actual = None
        if _lssb_phone_actual != _lssb_phone_hash or (config.screen_width, config.screen_height) != (1280, 720):
            renpy.display.screen.screens.pop((_lssb_phone_screen, "lssb_ui_ru_26_8_0d"), None)
            lssb_compat.disabled[_lssb_phone_screen] = "экран игры изменён"

init 1003 python:
    def _lssb_phone_name(value):
        special = {"UNKNOWN": "Неизвестный номер", "Unknown": "Неизвестный номер",
                   "Investigator": "Следователь", "Office": "Офис", "Landlord": "Арендодатель",
                   "Jack": "Джек", "Ryan": "Райан"}
        return special.get(value, _lssb_story_text(value))

screen smartphone_choice(girl="UNKNOWN", info="", show_mc=True, accept_only=False):
    variant "lssb_ui_ru_26_8_0d"
    predict False
    on "show" action Hide("say")
    if show_mc:
        add hero.layered_image() align (0.3, 1.0)
    style_prefix "smartphone"

    frame:
        align (0.75, 0.7)
        xysize (313, 573)
        background "gui/phone/phone_bg_home.png"
        $ girlname = girl.lower()
        $ self_voicing_name = "Звонок от: " + _lssb_phone_name(girl)
        frame:
            style "empty"
            if girlname and renpy.has_image(f"{girlname} smartphone"):
                add "[girlname]_smartphone" align (0.5, 0.15)
            else:
                add "gui/phone/unknown_smartphone.png" alpha 0.25 align (0.5, 0.15)
            button:
                style "empty"
                action NullAction()
                keyboard_focus False
                alt self_voicing_name

        vbox:
            xalign 0.5
            xsize 265
            yalign 0.85
            text _lssb_ui_translate(info) xsize 265 textalign 0.5
            label _lssb_phone_name(girl) xalign 0.5 text_xmaximum 265 text_textalign 0.5
            hbox:
                xalign 0.5
                spacing 15
                vbox:
                    xsize 125
                    imagebutton auto "gui/phone/ico_pickup_%s.png" action Return(True) xalign 0.5 alt "Ответить"
                    text "Ответить" xalign 0.5 xmaximum 125 textalign 0.5 alt ""
                if not accept_only:
                    vbox:
                        xsize 125
                        imagebutton auto "gui/phone/ico_dontpickup_%s.png" action Return(False) xalign 0.5 alt "Отклонить"
                        text "Отклонить" xalign 0.5 xmaximum 125 textalign 0.5 alt ""

screen smartphone_calling(npc="Unknown"):
    variant "lssb_ui_ru_26_8_0d"
    predict False
    on "show" action Hide("say")
    style_prefix "smartphone"

    frame:
        align (0.25, 0.3)
        xysize (245, 450)
        background Frame("gui/phone/phone_bg_home.png")
        $ npcname = npc.lower()
        $ self_voicing_name = "Вызов: " + _lssb_phone_name(npc)
        vbox:
            xalign 0.5
            xsize 207
            ysize 0.70
            vbox:
                xysize (0.65, 0.65)
                ypos 0.15
                if npcname and renpy.has_image(f"{npcname} smartphone"):
                    add Frame(f"{npcname}_smartphone")
                else:
                    add Frame("gui/phone/unknown_smartphone.png") alpha 0.25
            vbox:
                xalign 0.5
                xsize 207
                ypos 0.15
                label _lssb_phone_name(npc) xalign 0.5 text_xmaximum 207 text_textalign 0.5
                add "gui/phone/ico_calling_idle.png" alt "Calling" xalign 0.5
                text "Calling" alt "" xalign 0.5
