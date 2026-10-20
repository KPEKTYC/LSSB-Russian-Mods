# Display-only translation of activity cards, legacy captions and notifications.
init 1006 python:
    import builtins as _lssb_activity_builtins
    import re as _lssb_activity_re
    _lssb_activity_strings = {'Treat your injuries': 'Обработать раны', 'Report the rape': 'Сообщить об изнасиловании', 'Go confront the coach': 'Выяснить отношения с тренером', 'Go talk to the coach': 'Поговорить с тренером', 'A night at the movies with Alexis': 'Вечер в кино с Алексис', 'Glory-hole booth with Alexis': 'Кабинка глорихола с Алексис', 'Ask for a job': 'Спросить о работе', 'Attend mass': 'Посетить мессу', "Go to Ayesha's show": 'Пойти на выступление Айеши', 'Shop': 'За покупками', 'Battle of the bands': 'Битва музыкальных групп', 'Surf in the sunset': 'Заняться сёрфингом на закате', 'Sasha won a contest': 'Саша выиграла конкурс', 'Bible study': 'Изучать Библию', 'Place spy camera': 'Установить скрытую камеру', 'Boardroom Meeting': 'Совещание руководства', 'Buy a round': 'Угостить всех выпивкой', 'Buy some illegal stuff': 'Купить запрещённые вещества', 'Buy a lottery ticket': 'Купить лотерейный билет', 'Buy a membership': 'Купить абонемент', 'Call someone in': 'Позвать кого-нибудь', 'Call Kylie': 'Позвонить Кайли', 'Go back undercover': 'Вернуться к работе под прикрытием', 'Manage Office': 'Управлять офисом', "Place spy camera in Dwayne's office": 'Установить камеру в кабинете Дуэйна', 'Cheats': 'Читы', 'Visit Cherie': 'Навестить Шери', 'Clean my bedroom': 'Убраться в своей спальне', 'Clean': 'Убраться', 'Vacuum': 'Пропылесосить', 'Clean the pool': 'Почистить бассейн', 'Take a coffee break': 'Сделать перерыв на кофе', 'Have a pastry': 'Съесть пирожное', 'Buy popcorn': 'Купить попкорн', 'Caress her boobs': 'Поласкать её грудь', 'Put your hand inside': 'Просунуть руку под одежду', 'Make a sand castle': 'Построить замок из песка', 'Chat on the couch': 'Поболтать на диване', 'Watch the clouds': 'Посмотреть на облака', 'Have a coffee': 'Выпить кофе', 'Eat a burger': 'Съесть бургер', 'Eat': 'Поесть', 'Run together': 'Побегать вместе', 'Go shopping': 'Пройтись по магазинам', 'Touch [date_girl.possessive_adjective] hand': 'Коснуться руки', 'Hold [date_girl.possessive_adjective] hand': 'Взять за руку', 'Dip in the hot tub': 'Расслабиться в джакузи', 'Ice skate': 'Покататься на коньках', 'Have an ice cream': 'Съесть мороженое', 'Go karting': 'Покататься на картинге', 'Make a snowman': 'Слепить снеговика', 'Order for [date_girl.personal_pronoun]': 'Сделать заказ за партнёра', 'Pay for both of you': 'Заплатить за двоих', 'Take a pic together': 'Сфотографироваться вместе', 'Have a picnic': 'Устроить пикник', 'Visit the piercing shop': 'Зайти в салон пирсинга', 'Play at the arcade': 'Поиграть на автоматах', 'Play in the sea': 'Порезвиться в море', 'Play boardgame': 'Сыграть в настольную игру', 'Play console': 'Поиграть на приставке', 'Play darts': 'Сыграть в дартс', 'Play guitar': 'Поиграть на гитаре', 'Play in the pool': 'Порезвиться в бассейне', 'Ask for sunscreen': 'Попросить нанести крем от загара', 'Apply sunscreen': 'Нанести крем от загара', 'Play pool': 'Сыграть в бильярд', 'Hand between [date_girl.possessive_adjective] legs': 'Положить руку между ног', 'Finger her': 'Поласкать её пальцами', 'Hand on leg': 'Положить руку на ногу', 'Read poetry': 'Почитать стихи', 'Make some snacks': 'Приготовить закуски', 'Have a snowball fight': 'Поиграть в снежки', 'Go to the spa': 'Сходить в спа', 'Steal shit': 'Стащить что-нибудь', 'Go for a swim': 'Поплавать', 'Swim with [date_girl.possessive_adjective] in the pool': 'Поплавать вместе в бассейне', 'Swim together in the sea': 'Поплавать вместе в море', 'Waterslide': 'Прокатиться с водной горки', 'Play some beach volley': 'Поиграть в пляжный волейбол', 'Take her for a walk': 'Пойти с ней на прогулку', 'Watch a movie': 'Посмотреть фильм', 'Watch the movie': 'Посмотреть фильм', 'Watch TV': 'Посмотреть телевизор', 'Do the dishes': 'Помыть посуду', 'Do some push-ups': 'Поотжиматься', 'Order a drink': 'Заказать напиток', 'Drink coffee': 'Выпить кофе', 'Buy a coffee': 'Купить кофе', 'Order a drink and watch the show': 'Заказать напиток и посмотреть шоу', "Dump Aletta's gun": 'Избавиться от пистолета Алетты', "Dump Dwayne's corpse": 'Избавиться от тела Дуэйна', 'Eat a hot dog': 'Съесть хот-дог', 'Eat a Ramen': 'Поесть рамен', 'Eat a snack': 'Перекусить', 'Date next step': 'Продолжить свидание', 'Feed the cat': 'Покормить кота', 'Feed the dog': 'Покормить собаку', 'Find 4 Leaf Clover': 'Найти четырёхлистный клевер', 'Have a meal': 'Поесть', 'Get a haircut': 'Подстричься', 'Get a lap dance': 'Заказать приватный танец', 'Play a gig': 'Выступить с концертом', 'Go to the appointment': 'Пойти на встречу', 'Go on a date': 'Пойти на свидание', "Hack Aletta's computer": 'Взломать компьютер Алетты', 'Fuck Hanna on the front porch': 'Заняться сексом с Ханной на крыльце', "Wait for Harmony's dance": 'Дождаться танца Хармони', 'Go on a hike': 'Сходить в поход', 'Dip in the hot tub alone': 'Расслабиться в джакузи в одиночестве', 'Check spy camera': 'Проверить скрытую камеру', 'Interact': 'Взаимодействовать', 'Open inventory': 'Открыть инвентарь', 'Hire a private investigator': 'Нанять частного детектива', 'Drive a kart': 'Покататься на карте', 'Knock (Bathroom)': 'Постучать в ванную', 'Knock ([bree.name])': 'Постучать: [bree.name]', 'Knock (Sasha)': 'Постучать к Саше', 'Knock (Minami)': 'Постучать к Минами', 'Find and confront Kylie': 'Найти Кайли и выяснить отношения', 'Report Kylie': 'Заявить на Кайли', "Dump Danny's corpse": 'Избавиться от тела Дэнни', 'Look for the dream girl': 'Найти девушку из сна', 'Look for Lexi': 'Найти Лекси', 'Order something': 'Сделать заказ', 'Manage Team': 'Управлять командой', 'Masturbate': 'Мастурбировать', 'Mod Manager': 'Менеджер модов', 'Pass One Day': 'Пропустить день', 'Mow the lawn': 'Подстричь газон', 'Party': 'Устроить вечеринку', 'Pet the cat': 'Погладить кота', 'Pet the dog': 'Погладить собаку', 'Play a game': 'Поиграть на автомате', 'Play with [bree.name]': 'Поиграть вместе: [bree.name]', 'Play with the girls': 'Поиграть с девушками', 'Play with Minami': 'Поиграть с Минами', 'Play with Sasha': 'Поиграть с Сашей', 'Play video games': 'Поиграть в видеоигры', 'Play video games with [bree.name]': 'Поиграть в видеоигры: [bree.name]', 'Sunbath': 'Позагарать', 'Practice': 'Репетировать', 'Practice speech': 'Потренировать речь', 'Quit your day job': 'Уволиться с дневной работы', 'Quit your night job': 'Уволиться с ночной работы', 'APEX procedure': 'Процедура APEX', 'Read': 'Почитать', 'Look at the hot tub': 'Осмотреть джакузи', 'Go for a run': 'Выйти на пробежку', 'Get scavenger hunt clue': 'Получить подсказку для квеста', 'Guess scavenger hunt': 'Разгадать загадку квеста', 'Go to map': 'Открыть карту', 'Set Alarm': 'Поставить будильник', 'Pay off the manager': 'Заплатить управляющему', 'Shovel the snow': 'Расчистить снег', 'Sleep': 'Поспать', 'Study': 'Поучиться', 'Sweep the leaves': 'Убрать опавшие листья', 'Swim': 'Поплавать', 'Take a bath': 'Принять ванну', 'Take a shower': 'Принять душ', 'Take a nap': 'Вздремнуть', 'Think': 'Поразмыслить', 'Light training': 'Лёгкая тренировка', 'Train': 'Потренироваться', 'Heavy training': 'Интенсивная тренировка', 'Wait': 'Подождать', 'Wake_up': 'Проснуться', 'Watch TV with [bree.name]': 'Посмотреть телевизор: [bree.name]', 'Watch TV with everyone': 'Посмотреть телевизор вместе со всеми', 'Watch TV with [mike.name]': 'Посмотреть телевизор: [mike.name]', 'Watch TV with Minami': 'Посмотреть телевизор с Минами', 'Watch TV with Samantha': 'Посмотреть телевизор с Самантой', 'Watch TV with Sasha': 'Посмотреть телевизор с Сашей', 'Work': 'Поработать', 'Call Jeff the accountant': 'Позвонить бухгалтеру Джеффу', 'Work hard': 'Усердно поработать', 'Fuck': 'Заняться сексом', 'Use the remote vibrator': 'Включить вибратор с пульта', 'Apologize for breaking up': 'Извиниться за расставание', 'Ask for a second chance': 'Попросить второй шанс', 'Ask on a date': 'Пригласить на свидание', 'Ask birthday': 'Узнать день рождения', 'Ask number': 'Попросить номер телефона', 'About your belly': 'Поговорить о животике', 'Break up with her': 'Расстаться с ней', 'Break up with him': 'Расстаться с ним', 'Propose to Kylie and Camila': 'Сделать предложение Кайли и Камиле', 'Visit Kylie': 'Навестить Кайли', 'Cancel': 'Отмена', 'Cancel date': 'Отменить свидание', 'Cancel engagement': 'Расторгнуть помолвку', 'Invite to movie': 'Пригласить в кино', 'Command': 'Дать указание', 'Have her dance with a girl': 'Предложить ей танец с девушкой', 'Ask [date_girl.possessive_adjective] to dance on stage': 'Предложить танец на сцене', 'Ask to dance': 'Пригласить потанцевать', 'Friendzone her': 'Предложить ей остаться друзьями', 'Friendzone him': 'Предложить ему остаться друзьями', 'Conjugal visit': 'Супружеское свидание', 'Offer a gift': 'Сделать подарок', 'Go steady': 'Предложить встречаться', 'Cop a feel': 'Полапать', 'Use hypnosis': 'Применить гипноз', 'Invite to a race': 'Пригласить на гонку', 'Kiss': 'Поцеловать', 'Offer a massage': 'Предложить массаж', 'Practice dating with Minami': 'Потренироваться в свиданиях с Минами', 'Girl Mod Menu': 'Меню мода: персонаж', 'Offer a drink': 'Предложить выпить', 'Pet her head': 'Погладить её по голове', 'Fuck Morgan and Kleio': 'Заняться сексом с Морган и Клео', 'Play a game together': 'Поиграть вместе', 'Propose': 'Сделать предложение', 'Go shopping together': 'Пройтись по магазинам вместе', 'Slap ass': 'Шлёпнуть по попе', 'Study together': 'Поучиться вместе', 'Compliment': 'Сделать комплимент', 'Talk': 'Поговорить', 'Go on a date with Kylie and Ayesha': 'Пойти на свидание с Кайли и Айешой', 'Aquarium date with Kylie and Ayesha': 'Свидание с Кайли и Айешой в океанариуме', 'Home date with Kylie and Ayesha': 'Домашнее свидание с Кайли и Айешой', 'Meet Kylie and Ayesha at home': 'Встретиться дома с Кайли и Айешой', 'Test his DNA': 'Проверить его ДНК', 'Tickle [active_girl.personal_pronoun]': 'Пощекотать', 'Train together': 'Потренироваться вместе', 'Work together': 'Поработать вместе', 'You have a date!': 'У вас свидание!', 'You have an appointment.': 'У вас назначена встреча.', '{size=20}You have a date!{/size}': '{size=20}У вас свидание!{/size}', '{size=20}You have an appointment.{/size}': '{size=20}У вас назначена встреча.{/size}'}
    _lssb_activity_variant = "lssb_activities_ru_26_8_0d"
    _lssb_activity_previous_translate = _lssb_ui_translate
    _lssb_activity_time_pattern = _lssb_activity_re.compile(
        r"(\{image=gui/icons/icon_clock(?:@\d+)?\.png\}\s*[+-]?[0-9]+(?:[.,][0-9]+)?\s*)h\b")

    def _lssb_activity_text(value):
        if isinstance(value, (_lssb_activity_builtins.list, _lssb_activity_builtins.tuple)):
            return [_lssb_activity_text(part) for part in value]
        if not isinstance(value, str):
            return value
        text = _lssb_activity_previous_translate(value)
        if renpy.game.preferences.language != "russian":
            return text
        text = _lssb_activity_strings.get(value, text)
        return _lssb_activity_time_pattern.sub(lambda match: match.group(1).rstrip()+" ч", text)

    def _lssb_activity_enter_ru():
        if True and _lssb_activity_variant not in config.variants:
            config.variants.insert(0, _lssb_activity_variant)

    def _lssb_activity_leave_ru():
        if _lssb_activity_variant in config.variants:
            config.variants.remove(_lssb_activity_variant)

    if True:
        _lssb_ui_translate = _lssb_activity_text
        config.language_callbacks["russian"].append(_lssb_activity_enter_ru)
        for _lssb_language in set(renpy.known_languages()) | {None}:
            if _lssb_language != "russian":
                config.language_callbacks[_lssb_language].append(_lssb_activity_leave_ru)

screen tooltip():
    variant "lssb_activities_ru_26_8_0d"
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
            elif isinstance(tooltip, BaseActivity):
                preferred_side "right"
                xpos 10
                frame:
                    id "lssb_activity_card"
                    ypos 30
                    yanchor 0.5
                    style "overlay_ui_frame"
                    has vbox
                    align (0.5, 0.5)
                    spacing 5
                    text _lssb_ui_translate(tooltip.loop_display_name if keep_at_it else tooltip.display_name) id "lssb_activity_title" size 23 font "exo2_regular" color "#fff" outlines [(1, "#0099ff", 0, 0)] xalign 0.5 text_align 0.5 xmaximum 500 layout "greedy"
                    if tooltip.get_tooltip():
                        text " ".join(_lssb_ui_translate(tooltip.get_tooltip(in_inventory))) id "lssb_activity_effects" substitute False xalign 0.5 text_align 0.5 xmaximum 500 layout "greedy"
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
                    text _lssb_ui_translate(name) size 23 font "exo2_regular" color "#fff" outlines [(1, "#0099ff", 0, 0)] xalign 0.5
                    if not isinstance(tooltip, Person) and tooltip.get_tooltip():
                        text _lssb_ui_translate(tooltip.get_tooltip(in_inventory)) substitute False yalign 0.5

screen tooltip_old_ui():

    variant "lssb_activities_ru_26_8_0d"

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

            $ tooltip = _lssb_ui_translate(tooltip.get_tooltip(in_inventory))

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


screen old_ui_helper(helper):
    variant "lssb_activities_ru_26_8_0d"

    if helper:
        $ helper_name, helper_type = helper
        if helper_type == "activity" and game.room == "map":
            vbox:
                align (0.5, 0.17)
                text _lssb_ui_translate(helper_name) size 23 xmaximum 800 text_align 0.5 layout "greedy" font "exo2_regular" color "#fff" outlines [(1, "#0099ff", 0, 0)] xalign 0.5
        else:
            hbox:
                xalign 0.5
                if helper_type in ["talk", "activity"]:
                    text _lssb_ui_translate(helper_name) size 23 xmaximum 800 text_align 0.5 layout "greedy" font "exo2_regular" color "#FFFFFF" outlines [(1, "#0099ff", 0, 0)] xalign 0.5 alt ""
                elif helper_type == "room":
                    text "Go to [helper_name!t]" size 23 font "exo2_regular" color "#FFFFFF" outlines [(1, "#0099ff", 0, 0)] xalign 0.5



screen actions(activities, helper=False):
    variant "lssb_activities_ru_26_8_0d"

    if persistent.new_ui:
        if not renpy.get_screen(["smartphone", "story_tracker", "smartphone_choice"]):
            frame:
                at show_actions
                style "invisible_frame"
                yalign 0.6
                has hbox
                spacing 5
                if len(activities) > 8:
                    $ div = ceil(len(activities)/8)
                else:
                    $ div = 1
                for i in range(div):
                    vbox:
                        spacing 5
                        align (0.5, 0.5)
                        for (action_object, action_icon, action_display_name) in activities[i*ceil(len(activities)/div):(i+1)*ceil(len(activities)/div)]:
                            fixed:
                                fit_first True
                                imagebutton:
                                    auto f"button_{action_icon} %s"
                                    focus_mask True
                                    action [Return(action_object)]
                                    tooltip action_object
                                    alt _lssb_ui_translate(action_display_name)
                                use keep_at_it_button(action_object)

    else:
        frame:
            style "invisible_frame"
            if len(activities) > 10:
                add "gui/actions_box_big.png" xalign 0.5 ypos 520
                $ div = int(ceil(len(activities) / 10))
            else:
                add "gui/actions_box.png" xalign 0.5 ypos 570
                $ div = 1
            xsize 0.65
            xalign 0.5
            vbox:
                xalign 0.5
                ypos 605
                yanchor 1.0
                use old_ui_helper(helper)

                for i in range(div):
                    hbox:
                        xalign 0.5
                        spacing 5
                        for (action_object, action_icon, action_display_name) in activities[i*ceil(len(activities)/div):(i+1)*ceil(len(activities)/div)]:
                            fixed:
                                fit_first True
                                imagebutton:
                                    auto f"button_{action_icon} %s"
                                    focus_mask True
                                    hovered SetScreenVariable("helper", (action_display_name, "activity"))
                                    unhovered SetScreenVariable("helper", False)
                                    action [SetScreenVariable("helper", False), Return(action_object)]
                                    tooltip action_object
                                    alt _lssb_ui_translate(action_display_name)
                                use keep_at_it_button(action_object)

screen notification_popup(notif, pos):
    variant "lssb_activities_ru_26_8_0d"
    frame at notification_popout():
        xalign 1.0
        ypos 120 + (pos * 55)
        background "gui/notification_box.png"
        xminimum 100
        ysize 50
        xpadding 10
        text _lssb_ui_translate(notif[0]) yalign 0.5 style "ui_text" alt ""
    timer 4.0 action [Hide()]

