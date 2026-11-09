# LSSB Russian base translation. Maintained as part of the standalone localization.
# Original game archives are not modified.

# Preserve the game's typography while supplying Russian glyphs when a font lacks them.
translate russian python hide:
    import renpy.text.font as _lssb_base_font

    _lssb_base_font_attributes = (
        "text_font",
        "name_text_font",
        "interface_text_font",
        "button_text_font",
        "choice_button_text_font",
    )
    _lssb_base_seen_aliases = set()
    for _lssb_base_attribute in _lssb_base_font_attributes:
        _lssb_base_configured = getattr(gui, _lssb_base_attribute, None)
        _lssb_base_alias = None
        if (
            isinstance(_lssb_base_configured, str)
            and _lssb_base_configured in config.font_name_map
        ):
            _lssb_base_alias = _lssb_base_configured
            if _lssb_base_alias in _lssb_base_seen_aliases:
                continue
            _lssb_base_seen_aliases.add(_lssb_base_alias)
            _lssb_base_source = config.font_name_map[_lssb_base_alias]
        else:
            _lssb_base_source = _lssb_base_configured

        _lssb_base_alias_chain = set()
        while (
            isinstance(_lssb_base_source, str)
            and _lssb_base_source in config.font_name_map
            and _lssb_base_source not in _lssb_base_alias_chain
        ):
            _lssb_base_alias_chain.add(_lssb_base_source)
            _lssb_base_source = config.font_name_map[_lssb_base_source]

        if (
            not isinstance(_lssb_base_source, (str, _lssb_base_font.FontGroup))
            or getattr(
                _lssb_base_source,
                "_lssb_cyrillic_fallback",
                False,
            )
        ):
            continue
        if (
            isinstance(_lssb_base_source, _lssb_base_font.FontGroup)
            and None not in _lssb_base_source.map
        ):
            continue

        _lssb_base_description = "{} {} {}".format(
            _lssb_base_attribute, _lssb_base_configured, _lssb_base_source
        ).casefold()
        _lssb_base_is_bold = any(
            _lssb_base_weight in _lssb_base_description
            for _lssb_base_weight in (
                "bold", "black", "heavy", "semibold", "demibold"
            )
        )
        _lssb_base_fallback = (
            "DejaVuSans-Bold.ttf" if _lssb_base_is_bold else "DejaVuSans.ttf"
        )
        _lssb_base_group = _lssb_base_font.FontGroup()
        _lssb_base_group.add(_lssb_base_fallback, 0x0400, 0x052F)
        _lssb_base_group.add(_lssb_base_fallback, 0x20BD, 0x20BD)
        _lssb_base_group.add(_lssb_base_fallback, 0x2116, 0x2116)
        _lssb_base_group.add(_lssb_base_source, None, None)
        _lssb_base_group._lssb_cyrillic_fallback = True
        if _lssb_base_alias is not None:
            config.font_name_map[_lssb_base_alias] = _lssb_base_group
        else:
            setattr(gui, _lssb_base_attribute, _lssb_base_group)

translate russian about_photostudio_ed8648aa:

    "В городе открылась фотостудия. Возможно, здесь получится найти работу."

translate russian aletta_audrey_lavish_male_ending_5929f2ae:

    aletta.say "Да."

translate russian aletta_audrey_lavish_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian aletta_audrey_lavish_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian aletta_audrey_lavish_propose_male_1c0d45e8:

    mike.say "Ну..."

translate russian aletta_audrey_lavish_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian aletta_audrey_lavish_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian aletta_audrey_lavish_shiori_male_ending_5929f2ae:

    aletta.say "Да."

translate russian aletta_audrey_lavish_shiori_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian aletta_audrey_lavish_shiori_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian aletta_audrey_lavish_shiori_propose_male_1c0d45e8:

    mike.say "Ну..."

translate russian aletta_audrey_lavish_shiori_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian aletta_audrey_lavish_shiori_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian aletta_audrey_male_ending_5929f2ae:

    aletta.say "Да."

translate russian aletta_audrey_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian aletta_audrey_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian aletta_audrey_propose_male_1c0d45e8:

    mike.say "Ну..."

translate russian aletta_audrey_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian aletta_audrey_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian aletta_audrey_shiori_male_ending_5929f2ae:

    aletta.say "Да."

translate russian aletta_audrey_shiori_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian aletta_audrey_shiori_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian aletta_audrey_shiori_propose_male_1c0d45e8:

    mike.say "Ну..."

translate russian aletta_audrey_shiori_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian aletta_audrey_shiori_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian aletta_chat_about_cherie_07767eec:

    aletta.say "Как прошла встреча с мамой Кэссиди?"

translate russian aletta_lavish_male_ending_5929f2ae:

    aletta.say "Да."

translate russian aletta_lavish_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian aletta_lavish_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian aletta_lavish_propose_male_1c0d45e8:

    mike.say "Ну..."

translate russian aletta_lavish_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian aletta_lavish_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian aletta_lavish_shiori_male_ending_5929f2ae:

    aletta.say "Да."

translate russian aletta_lavish_shiori_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian aletta_lavish_shiori_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian aletta_lavish_shiori_propose_male_1c0d45e8:

    mike.say "Ну..."

translate russian aletta_lavish_shiori_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian aletta_lavish_shiori_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian aletta_shiori_male_ending_5929f2ae:

    aletta.say "Да."

translate russian aletta_shiori_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian aletta_shiori_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian aletta_shiori_propose_male_1c0d45e8:

    mike.say "Ну..."

translate russian aletta_shiori_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian aletta_shiori_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian amy_teaser_009bac59:

    shawn.say "Да ладно тебе, чувак! Я тебя понимаю!"

translate russian amy_teaser_020f72f9:

    "Я просто оказался в торговом центре и убиваю время, поэтому зашёл в магазин электроники."

translate russian amy_teaser_0755084c:

    "Шон сейчас выглядит довольно незрело."

translate russian amy_teaser_07f307e8:

    "Я продолжаю наблюдать за ней, стараясь выглядеть так, будто просто осматриваю товары."

translate russian amy_teaser_0a6f5feb:

    amy.say "Интересно, ещё в чём ты хорош?"

translate russian amy_teaser_0a6f5feb_1:

    amy.say "Интересно, ещё в чём ты хорош?"

translate russian amy_teaser_0a987852:

    "Шон снова кивает и уходит, оставляя меня одного."

translate russian amy_teaser_0de97bf1:

    "Шон отмахивается от моих опасений, качая головой."

translate russian amy_teaser_0fc9189b:

    "А потом я качаю головой, пытаясь сосредоточиться на Эми."

translate russian amy_teaser_120ebbf1:

    shawn.say "Не мог не заметить, как ты только что смотрел на Эми."

translate russian amy_teaser_15b34775:

    amy.say "Но Шон следит за мной, как ястреб!"

translate russian amy_teaser_15b34775_1:

    amy.say "Но Шон следит за мной, как ястреб!"

translate russian amy_teaser_17ccc806:

    "Мы обмениваемся прощальными словами."

translate russian amy_teaser_17ccc806_1:

    "Мы обмениваемся прощальными словами."

translate russian amy_teaser_19742a2a:

    "Я хмурюсь и бросаю взгляд в сторону того парня, который здесь постоянно работает."

translate russian amy_teaser_1a4d674f:

    "С этими словами он разворачивается и уходит обратно в магазин."

translate russian amy_teaser_1a4d674f_1:

    "С этими словами он разворачивается и уходит обратно в магазин."

translate russian amy_teaser_1b45fad9:

    amy.say "Он просто работает здесь уже очень давно."

translate russian amy_teaser_1b45fad9_1:

    amy.say "Он просто работает здесь уже очень давно."

translate russian amy_teaser_203dde6b:

    mike.say "Шон, успокойся, ради бога!"

translate russian amy_teaser_20598d93:

    mike.say "Правда?!"

translate russian amy_teaser_20598d93_1:

    mike.say "Ты это сделала?!"

translate russian amy_teaser_22687fbe:

    "Это новый сотрудник, а именно — сотрудница."

translate russian amy_teaser_237b3018:

    "Я слышу, как глотаю, и внимательнее рассматриваю её."

translate russian amy_teaser_237b3018_1:

    "Я слышу, как глотаю, и внимательнее рассматриваю её."

translate russian amy_teaser_240ecda5:

    mike.say "Меня зовут [hero.name]."

translate russian amy_teaser_240ecda5_1:

    mike.say "Я [hero.name]."

translate russian amy_teaser_248b058e:

    "Просто так подойти к той же девушке и заговорить с ней."

translate russian amy_teaser_2561339c:

    "Но когда она звучит с её улыбающихся губ, это похоже на слова ангела!"

translate russian amy_teaser_2561339c_1:

    "Но когда она звучит с её улыбающихся губ, это похоже на слова ангела!"

translate russian amy_teaser_25c76b4f:

    "И ещё лучше — она явно готтка, несмотря на свою униформу!"

translate russian amy_teaser_260eb311:

    mike.say "Как скажешь, Шон."

translate russian amy_teaser_267fd3fa:

    "Что Шон вообще думает?"

translate russian amy_teaser_26a8174d:

    "Эми кивает и улыбается, затем отворачивается, чтобы вернуться к работе."

translate russian amy_teaser_26a8174d_1:

    "Эми кивает и улыбается, затем отворачивается, чтобы вернуться к работе."

translate russian amy_teaser_28a42efe:

    "Эми кивает и дарит мне очень милую улыбку."

translate russian amy_teaser_28a42efe_1:

    "Эми кивает и дарит мне очень милую улыбку."

translate russian amy_teaser_2fd679e3:

    amy.say "Ты такой смешной и милый."

translate russian amy_teaser_2fd679e3_1:

    amy.say "Ты такой смешной и милый."

translate russian amy_teaser_30e74fc5:

    mike.say "Эм..."

translate russian amy_teaser_30e74fc5_1:

    mike.say "Эм..."

translate russian amy_teaser_336b8db7:

    mike.say "Что я сделал, чтобы ты так разозлился?"

translate russian amy_teaser_33956670:

    "Я невольно подпрыгиваю от неожиданности, когда Шон появляется рядом со мной."

translate russian amy_teaser_3939e466:

    mike.say "Он тебе доставляет неприятности?"

translate russian amy_teaser_3a5ff38f:

    "Он не может просто решить, что Эми принадлежит ему."

translate russian amy_teaser_3b024a4f:

    "Но в конце концов он уходит, чтобы заняться чем-то другим."

translate russian amy_teaser_3b0d38f2:

    shawn.say "Не притворяйся невинным со мной, [hero.name]."

translate russian amy_teaser_3f7255f6:

    mike.say "Я просто посмотрю кое-что, ладно?"

translate russian amy_teaser_415d58d6:

    "И он мрачно кивает головой."

translate russian amy_teaser_415d58d6_1:

    "И он мрачно кивает головой."

translate russian amy_teaser_42710614:

    amy.say "Он просто любит притворяться моим начальником."

translate russian amy_teaser_42af4db2:

    amy.say "На самом деле, я рада, что ты подошёл сюда."

translate russian amy_teaser_42af4db2_1:

    amy.say "На самом деле, я рада, что ты подошёл сюда."

translate russian amy_teaser_437b237a:

    shawn.say "Привет, [hero.name]!"

translate russian amy_teaser_4472d14a:

    "Теперь девушка одна, всё ещё раскладывает товары на полках."

translate russian amy_teaser_44c02808:

    mike.say "Да нет, Эми..."

translate russian amy_teaser_44c02808_1:

    mike.say "Да нет, Эми..."

translate russian amy_teaser_4525eb81:

    shawn.say "Это значит война!"

translate russian amy_teaser_46e014e8:

    amy.say "Но если тебе не нужна моя помощь, мне нужно возвращаться к работе!"

translate russian amy_teaser_46e014e8_1:

    amy.say "Но если тебе не нужна моя помощь, мне нужно возвращаться к работе!"

translate russian amy_teaser_49007bbc:

    "Girl" "Могу ли я вам чем-нибудь помочь сегодня?"

translate russian amy_teaser_4b110996:

    mike.say "Тебе твой начальник доставляет неприятности?"

translate russian amy_teaser_4bf68e95:

    "Глаза Шона сужаются, когда он злобно смотрит на меня."

translate russian amy_teaser_4bf68e95_1:

    "Глаза Шона сужаются, когда он злобно смотрит на меня."

translate russian amy_teaser_7ebf664b:

    mike.say "О... хорошо... извини!"

translate russian amy_teaser_7ebf664b_1:

    mike.say "О... хорошо... извини!"

translate russian amy_teaser_4ffe147a:

    "В конце концов, я просто сдаюсь и ухожу, чувствуя себя совершенно подавленным."

translate russian amy_teaser_4ffe147a_1:

    "В конце концов, я просто сдаюсь и ухожу, чувствуя себя совершенно подавленным."

translate russian amy_teaser_50c0e39b:

    mike.say "Потому что я знаю этого парня, и он может быть настоящим засранцем!"

translate russian amy_teaser_51f9ba9e:

    mike.say "А не для того, чтобы устраивать выяснение отношений из-за какой-то девчонки!"

translate russian amy_teaser_52c65242:

    mike.say "Что?!"

translate russian amy_teaser_554b29d8:

    "Всё, что мне остаётся, это уйти, чувствуя себя совершенно подавленным."

translate russian amy_teaser_55d50cf2:

    "Либо она показывает другому покупателю, где найти то, что он хочет."

translate russian amy_teaser_55d50cf2_1:

    "Либо она показывает другому покупателю, где найти то, что он хочет."

translate russian amy_teaser_55e1add1:

    shawn.say "Видел что-нибудь, что тебе понравилось?"

translate russian amy_teaser_5632f576:

    shawn.say "Чушь — я видел, как ты обменивался номерами!"

translate russian amy_teaser_5a6c4ddf:

    shawn.say "Она только пару дней назад начала работать."

translate russian amy_teaser_5e557cd6:

    amy.say "Ой, [hero.name]!"

translate russian amy_teaser_5e557cd6_1:

    amy.say "Ой, [hero.name]!"

translate russian amy_teaser_5ebee31e:

    "На звук моего голоса девушка поднимает голову от того, что она делала."

translate russian amy_teaser_5f2dc4d4:

    amy.say "В любом случае, забудь о нём."

translate russian amy_teaser_5f2dc4d4_1:

    amy.say "В любом случае, забудь о нём."

translate russian amy_teaser_8dc4ebf0:

    mike.say "Я просто... я просто пойду куда-нибудь ещё?"

translate russian amy_teaser_8dc4ebf0_1:

    mike.say "Я просто... я просто пойду куда-нибудь ещё?"

translate russian amy_teaser_61d85a6e:

    amy.say "Я хотела поговорить с тобой..."

translate russian amy_teaser_61d85a6e_1:

    amy.say "Я хотела поговорить с тобой..."

translate russian amy_teaser_6332429b:

    amy.say "Ой, он не такой уж плохой."

translate russian amy_teaser_63a145fd:

    amy.say "Так что он, наверное, считает, что у него есть право командовать!"

translate russian amy_teaser_63a145fd_1:

    amy.say "Так что он, наверное, считает, что у него есть право командовать!"

translate russian amy_teaser_64805695:

    "И этот звук — восхитительно вызывающий."

translate russian amy_teaser_64805695_1:

    "И этот звук — восхитительно вызывающий."

translate russian amy_teaser_6658acb2:

    mike.say "Да ладно, Шон, да что ты..."

translate russian amy_teaser_665db557:

    "То есть, он просто не может решить, что Эми принадлежит ему."

translate russian amy_teaser_68bca6d6:

    "Шон кивает, поворачиваясь, чтобы тоже посмотреть на Эми."

translate russian amy_teaser_692d84eb:

    "И я более чем готов сражаться за неё сам!"

translate russian amy_teaser_6cee9fe2:

    "И всё, что я могу сделать, это уйти, чувствуя себя совершенно подавленным."

translate russian amy_teaser_6ec422ae:

    shawn.say "Тебе лучше отступить, потому что я обратил на неё внимание первым!"

translate russian amy_teaser_700f54ac:

    mike.say "Вот так..."

translate russian amy_teaser_710f1617:

    "И она соответственно меняет тон, её улыбка становится более искренней."

translate russian amy_teaser_710f1617_1:

    "И она соответственно меняет тон, её улыбка становится более искренней."

translate russian amy_teaser_71de399f:

    "Я не знаю, сдержу ли я своё обещание ему или нет."

translate russian amy_teaser_728cfbd2:

    shawn.say "У неё ещё период испытания."

translate russian amy_teaser_74143306:

    "Но я обязательно буду следить за Эми."

translate russian amy_teaser_3b484601:

    mike.say "Ты...?"

translate russian amy_teaser_3b484601_1:

    mike.say "А... ты кто?"

translate russian amy_teaser_7a513575:

    "Потому что вблизи она выглядит ещё более сексуально, чем издалека!"

translate russian amy_teaser_7a513575_1:

    "Потому что вблизи она выглядит ещё более сексуально, чем издалека!"

translate russian amy_teaser_7b61f6d7:

    mike.say "Чёрт, Шон — ты меня напугал до смерти!"

translate russian amy_teaser_7e645ada:

    mike.say "Может быть, если мы когда-нибудь встретимся, ты это узнаешь?"

translate russian amy_teaser_7e645ada_1:

    mike.say "Может быть, если мы когда-нибудь встретимся, ты это узнаешь?"

translate russian amy_teaser_7f857ba8:

    "И он посмотрел мне прямо в глаза."

translate russian amy_teaser_8663f7d0:

    "И кажется, он довольно доволен тем, как все это для меня сложилось."

translate russian amy_teaser_87bf1a46:

    "Но я не хочу, чтобы она видела, как я с ним спорю."

translate russian amy_teaser_8a1ed3e8:

    shawn.say "И, благодаря моему обучению, у неё всё получится."

translate russian amy_teaser_8b4dbb30:

    amy.say "Правда?"

translate russian amy_teaser_8b4dbb30_1:

    amy.say "Правда?"

translate russian amy_teaser_8b740d9a:

    "Это был бы идеальный шанс подойти к ней и представиться."

translate russian amy_teaser_8cbb2d92:

    "Girl" "Привет!"

translate russian amy_teaser_8dce6ec1:

    amy.say "Тебе нужна какая-нибудь помощь сегодня?"

translate russian amy_teaser_8e66b9bf:

    "Шон скрестил руки на бёдрах."

translate russian amy_teaser_8f531c09:

    shawn.say "Эй, парень!"

translate russian amy_teaser_9070d91a:

    mike.say "Я здесь, чтобы посмотреть на то, что ты продаёшь."

translate russian amy_teaser_90f07af8:

    amy.say "Добро пожаловать в магазин."

translate russian amy_teaser_916090fd:

    "Я делаю паузу, чтобы взглянуть на её бейджик."

translate russian amy_teaser_94c16ea5:

    shawn.say "Если ты так хочешь."

translate russian amy_teaser_95abdf8a:

    mike.say "Эми — это не предмет, который можно просто забрать себе!"

translate russian amy_teaser_95f6a3b3:

    shawn.say "И я не хочу, чтобы ты все испортила мне!"

translate russian amy_teaser_9768fe54:

    "Всё, что я могу сделать, это покачать головой и уйти."

translate russian amy_teaser_9768fe54_1:

    "Всё, что я могу сделать, это покачать головой и уйти."

translate russian amy_teaser_98607517:

    "Я думал, мы продвигаемся вперёд, но она просто прервала меня!"

translate russian amy_teaser_98607517_1:

    "Я думал, мы продвигаемся вперёд, но она просто прервала меня!"

translate russian amy_teaser_9a2a95ba:

    amy.say "Я только что увидела, как ты вошёл, и хотела поздороваться."

translate russian amy_teaser_9a2a95ba_1:

    amy.say "Я только что увидела, как ты вошёл, и хотела поздороваться."

translate russian amy_teaser_9db90706:

    "Но даже сейчас я уверен, что Эми того стоит."

translate russian amy_teaser_9dd6ea43:

    "Просто неспешно пройти по тому же ряду, что и Эми, и завести разговор."

translate russian amy_teaser_9df19043:

    "Но каждый раз, когда я поднимаю глаза, она кажется занятой чем-то другим."

translate russian amy_teaser_9df19043_1:

    "Но каждый раз, когда я поднимаю глаза, она кажется занятой чем-то другим."

translate russian amy_teaser_a1e5114e:

    "И он выглядит очень злым на меня."

translate russian amy_teaser_a2d74b00:

    "Что также делает её ещё милее!"

translate russian amy_teaser_a2d74b00_1:

    "Что также делает её ещё милее!"

translate russian amy_teaser_a4931bbb:

    "Когда я выхожу из магазина, я вижу, как Шон наблюдает за мной."

translate russian amy_teaser_a4a1f375:

    "Я тороплюсь туда, стараясь казаться максимально спокойным."

translate russian amy_teaser_a4a1f375_1:

    "Я тороплюсь туда, стараясь казаться максимально спокойным."

translate russian amy_teaser_a523218c:

    amy.say "Привет!"

translate russian amy_teaser_a56e4692:

    "Либо Шон стоит рядом с ней, пока она работает."

translate russian amy_teaser_a84d6fcd:

    "Он, должно быть, заметил меня, когда я зашёл, и тихонько подобрался ко мне."

translate russian amy_teaser_aa874548:

    "Особенно после того, как я заполучил номер телефона этой горячей девчонки!"

translate russian amy_teaser_ac1a7054:

    "Шон прав, мне не нужно портить ему ничего."

translate russian amy_teaser_ae7aee4e:

    mike.say "Я просто разговаривал с ней, это все!"

translate russian amy_teaser_b2ab948a:

    "Или же один из сотрудников мужского пола постоянно стоит рядом с ней, пока она работает."

translate russian amy_teaser_b445bbe8:

    "Наверное, он её обучает работе в магазине."

translate russian amy_teaser_b5c442b8:

    "Я делаю шаг назад от Шона."

translate russian amy_teaser_b7701f95:

    "А все это время я рассматривал эту симпатичную девушку."

translate russian amy_teaser_beab5b59:

    "Затем я выхожу из этого места, чувствуя себя так, будто лечу над землёй."

translate russian amy_teaser_c1e5f61f:

    "Но кому какое дело до того, что он думает."

translate russian amy_teaser_c3875b80:

    "Этот странный парень, который здесь работает, некоторое время разговаривает с ней."

translate russian amy_teaser_c72c28c5:

    amy.say "Ой, он не мой начальник."

translate russian amy_teaser_c83a991c:

    "И стараюсь не пялиться на её грудь!"

translate russian amy_teaser_c916c646:

    "Я закатываю глаза, понимая, насколько же этот Шон — пустозвон."

translate russian amy_teaser_c92f9dde:

    "Girl" "Добро пожаловать в магазин."

translate russian amy_teaser_c9bcee82:

    shawn.say "Но она очень быстро учится."

translate russian amy_teaser_cfa0f62e:

    shawn.say "Что ты себе позволяешь?!"

translate russian amy_teaser_d0de7cd6:

    "Эми немного наклоняется ближе."

translate russian amy_teaser_d0de7cd6_1:

    "Эми немного наклоняется ближе."

translate russian amy_teaser_d137dbb6:

    "А потом я выхожу из этого места, чувствуя себя так, будто лечу над землёй."

translate russian amy_teaser_d164890a:

    "Но прежде чем я успеваю выйти в дверь, Шон снова появляется."

translate russian amy_teaser_d179aca4:

    "И сегодня это тоже так, если не считать того, что моё внимание привлекла не новая техника."

translate russian amy_teaser_d1d4d5e9:

    "Я, должно быть, слышал эту заученную фразу уже сотню раз."

translate russian amy_teaser_d1d4d5e9_1:

    "Я, должно быть, слышал эту заученную фразу уже сотню раз."

translate russian amy_teaser_d32d8f7a:

    "То, как внезапно Эми меняет тему разговора, меня удивляет."

translate russian amy_teaser_d32d8f7a_1:

    "То, как внезапно Эми меняет тему разговора, меня удивляет."

translate russian amy_teaser_d3dac635:

    "Кажется, Эми понимает, что я не пришёл сюда за покупками."

translate russian amy_teaser_d3dac635_1:

    "Кажется, Эми понимает, что я не пришёл сюда за покупками."

translate russian amy_teaser_d589358f:

    amy.say "Очень приятно познакомиться, [hero.name]."

translate russian amy_teaser_d589358f_1:

    amy.say "Очень приятно познакомиться, [hero.name]."

translate russian amy_teaser_d6457806:

    mike.say "Да нет..."

translate russian amy_teaser_d71a0f39:

    shawn.say "Ты должна это иметь в виду, [hero.name]."

translate russian amy_teaser_d72f51b4:

    "Он подступает ко мне вплотную, и я даже не понимаю, почему."

translate russian amy_teaser_da1e074b:

    "Мой коллега-мужчина сверлит меня взглядом, когда я ухожу."

translate russian amy_teaser_da2b631c:

    "Несколько раз я пытаюсь набраться смелости и подойти туда."

translate russian amy_teaser_da2b631c_1:

    "Несколько раз я пытаюсь набраться смелости и подойти туда."

translate russian amy_teaser_da706b36:

    "Обычно всегда есть что-нибудь новенькое и блестящее, на что можно посмотреть."

translate russian amy_teaser_daefd739:

    "Скорее всего, он сам это сделает."

translate russian amy_teaser_dc975c7d:

    "Я не искал ничего конкретного, но здесь довольно приятно проводить время."

translate russian amy_teaser_dcdc00da:

    mike.say "Я не знаю, Эми."

translate russian amy_teaser_dcdc00da_1:

    mike.say "Я не знаю, Эми."

translate russian amy_teaser_dd9ecfd5:

    mike.say "Я просто хотел поздороваться и представиться."

translate russian amy_teaser_dd9ecfd5_1:

    mike.say "Я просто хотел поздороваться и представиться."

translate russian amy_teaser_df6ed4af:

    mike.say "Привет..."

translate russian amy_teaser_df6ed4af_1:

    mike.say "Привет..."

translate russian amy_teaser_e03a0a8b:

    "Я стараюсь выглядеть непринуждённо, пока жду, когда Шон уйдёт."

translate russian amy_teaser_e0a33d3e:

    amy.say "Возможно, [hero.name], так и сделаем!"

translate russian amy_teaser_e0a33d3e_1:

    amy.say "Возможно, [hero.name], так и сделаем!"

translate russian amy_teaser_e3d3715f:

    mike.say "Давай, вырастешь, Шон."

translate russian amy_teaser_ea5f1075:

    "Эми снова хихикает, ей забавно видеть, как я попался."

translate russian amy_teaser_ea5f1075_1:

    "Эми снова хихикает, ей забавно видеть, как я попался."

translate russian amy_teaser_eb0ce906:

    shawn.say "Хорошо, [hero.name]."

translate russian amy_teaser_ecdda39a:

    mike.say "Так что если ты хочешь её, тебе придётся бороться за неё!"

translate russian amy_teaser_eed609d8:

    shawn.say "Потому что у меня хорошее предчувствие насчёт Эми и меня."

translate russian amy_teaser_f1d8a63c:

    mike.say "Эм..."

translate russian amy_teaser_f1d8a63c_1:

    mike.say "Эм..."

translate russian amy_teaser_f1d8a63c_2:

    mike.say "Эм..."

translate russian amy_teaser_f21ce084:

    shawn.say "Я видел, как ты ухаживал за Эми только что!"

translate russian amy_teaser_f2b83e16:

    mike.say "Она просто невероятная, Шон!"

translate russian amy_teaser_f4549cbb:

    amy.say "Да, потому что это означало, что мне не нужно было подходить к тебе."

translate russian amy_teaser_f4549cbb_1:

    amy.say "Да, потому что это означало, что мне не нужно было подходить к тебе."

translate russian amy_teaser_f4e8eaf9:

    "Эми смеётся над этим."

translate russian amy_teaser_f4e8eaf9_1:

    "Эми смеётся над этим."

translate russian amy_teaser_f64e3ea9:

    "Затем он кивает в сторону новой девушки, которая занята тем, что раскладывает товары на полках."

translate russian amy_teaser_kiss_011d0c21:

    mike.say "Привет, Эми!"

translate russian amy_teaser_kiss_04554633:

    amy.say "Реальная... кровь?!"

translate russian amy_teaser_kiss_098ddef0:

    "И часть меня просто хочет пятиться назад и уйти отсюда."

translate russian amy_teaser_kiss_0ada2d04:

    "И, делая это, она видит меня, стоящего позади неё."

translate russian amy_teaser_kiss_0c596ed9:

    "Тогда я смогу наконец спросить её, что вообще происходит между нами."

translate russian amy_teaser_kiss_0f976421:

    "Это всё равно, что тебя перенесло из самой неловкой ситуации, которую только можно представить."

translate russian amy_teaser_kiss_10bb44c7:

    "И он совсем не выглядит довольным мной!"

translate russian amy_teaser_kiss_11ea1e4b:

    amy.say "Обещаю, этого больше не повторится."

translate russian amy_teaser_kiss_1ac00e5d:

    "Она бросает вызывающий взгляд на Шона."

translate russian amy_teaser_kiss_1d4a9b21:

    "Я чувствую, как напрягаются мышцы моего лица, когда я улыбаюсь им."

translate russian amy_teaser_kiss_20aa4842:

    amy.say "Я же уже сказала, что извинилась, Шон!"

translate russian amy_teaser_kiss_23f4c761:

    "Если бы она предложила себя, я бы занялся с ней прямо сейчас!"

translate russian amy_teaser_kiss_2ceca909:

    "И ты оказываешься в месте абсолютного наслаждения!"

translate russian amy_teaser_kiss_35f03eab:

    "Что очень неприятно, потому что это означает, что я стою здесь с неловким эрекцией."

translate russian amy_teaser_kiss_38cb918e:

    "Но затем Эми прекращает поцелуй."

translate russian amy_teaser_kiss_3908d5c8:

    mike.say "Ты не занята сейчас?"

translate russian amy_teaser_kiss_3c375110:

    "Теперь, когда её нет рядом, Шон подходит ко мне."

translate russian amy_teaser_kiss_3d148637:

    "Но похоже, она уже ушла в заднюю часть магазина."

translate russian amy_teaser_kiss_40c2f88c:

    "Внезапно они оба молча смотрят на меня."

translate russian amy_teaser_kiss_425899b1:

    "А затем она уверенно подходит к тому месту, где я стою."

translate russian amy_teaser_kiss_429ba3a7:

    "Я забываю, где мы находимся и кто сейчас на нас смотрит."

translate russian amy_teaser_kiss_433f28db:

    "Я вижу, как выражение её лица становится решительным."

translate russian amy_teaser_kiss_45baacdd:

    shawn.say "Она даже со мной не ведёт себя так!"

translate russian amy_teaser_kiss_46114186:

    shawn.say "Ты не мог бы объяснить мне, что это было?"

translate russian amy_teaser_kiss_46ac1bee:

    mike.say "Я собирался спросить тебя об этом же!"

translate russian amy_teaser_kiss_4a0408b3:

    "Она удивлена, но легко рывком тянет меня вперёд."

translate russian amy_teaser_kiss_4cf775c5:

    mike.say "Что?"

translate russian amy_teaser_kiss_57e0d348:

    amy.say "Фу!"

translate russian amy_teaser_kiss_5953048d:

    "Но эта улыбка тут же сменяется растерянным и разочарованным выражением, когда я слышу и вижу, что происходит внутри."

translate russian amy_teaser_kiss_5e773823:

    "Эми тоже без колебаний прижимается ко мне."

translate russian amy_teaser_kiss_60edea6b:

    "Я прохожу мимо магазина электроники, где работают Шон и Эми, поэтому я делаю крюк, чтобы зайти."

translate russian amy_teaser_kiss_6386d373:

    "В этот момент я совершенно ошеломлён и не могу пошевелиться."

translate russian amy_teaser_kiss_65dd98e6:

    "Оправившись от неожиданного поцелуя Эми, я извиняюсь и ухожу."

translate russian amy_teaser_kiss_66d4b5da:

    shawn.say "Может быть, попробуешь хоть раз послушать меня, а?"

translate russian amy_teaser_kiss_68b79a4d:

    "Раньше у меня даже была возможность пообщаться с Шоном."

translate russian amy_teaser_kiss_6a7b4991:

    "Всегда полезно посмотреть, что у них есть в продаже и какие новинки."

translate russian amy_teaser_kiss_6abbd721:

    "Я зашёл внутрь с глупой улыбкой на лице, предвкушая встречу с ней."

translate russian amy_teaser_kiss_764c311c:

    "Эми буквально засовывает свой язык мне в рот."

translate russian amy_teaser_kiss_7f3529e5:

    "Ну, когда я говорю «целоваться», я имею в виду не просто лёгкий поцелуй."

translate russian amy_teaser_kiss_7f454da4:

    mike.say "Она обычно так себя ведёт с клиентами?"

translate russian amy_teaser_kiss_7f98d569:

    "Кажется, Эми первой приходит в себя."

translate russian amy_teaser_kiss_82148ff6:

    shawn.say "Да сколько же можно?!"

translate russian amy_teaser_kiss_830de6a4:

    "Неважно, насколько странно это будет выглядеть сейчас."

translate russian amy_teaser_kiss_8550155f:

    "И вот, меня резко возвращают в реальность."

translate russian amy_teaser_kiss_8f83df7b:

    "Клянусь, если бы она положила руку мне под штаны, я бы не смог её остановить."

translate russian amy_teaser_kiss_99b4437e:

    "Затем он исследует там, как змея, ищущая добычу!"

translate russian amy_teaser_kiss_9b6bf034:

    "И я вижу, как Шон смотрит на меня с другой стороны магазина."

translate russian amy_teaser_kiss_9dd1d99b:

    "Я открываю рот, чтобы что-то сказать."

translate russian amy_teaser_kiss_9f97cbfc:

    shawn.say "Может быть, попробуй запомнить что-нибудь в своей пустой голове?"

translate russian amy_teaser_kiss_a36c8ef6:

    "У меня такое ощущение, что после того, что произошло, я не самый любимый человек для Шоу."

translate russian amy_teaser_kiss_a8c17a2e:

    "Я смотрю на Эми, надеясь, что она придёт мне на помощь."

translate russian amy_teaser_kiss_ad9e7b30:

    amy.say "Я не обязана стоять здесь и выслушивать это от тебя!"

translate russian amy_teaser_kiss_b78d906a:

    shawn.say "Жаль..."

translate russian amy_teaser_kiss_b7b38692:

    "Может быть, мне стоит поговорить с ней наедине, чтобы Шон не подслушивал?"

translate russian amy_teaser_kiss_bdd170a6:

    amy.say "Чего ты ещё хочешь?"

translate russian amy_teaser_kiss_c3ad8fda:

    "К тому же, мне нужно понять, почему Эми поступила именно так."

translate russian amy_teaser_kiss_d47f8b71:

    "Этот жест позволяет Шону тоже увидеть меня, прерывая его следующий ответ."

translate russian amy_teaser_kiss_d4c5ef5a:

    mike.say "Привет, Шон!"

translate russian amy_teaser_kiss_de1ad19c:

    amy.say "Можешь засунуть..."

translate russian amy_teaser_kiss_e04a41cb:

    "И я чувствую себя довольно неловко."

translate russian amy_teaser_kiss_e813d541:

    "И ощущение её тела, соприкасающегося с моим, мгновенно приводит меня в возбуждение."

translate russian amy_teaser_kiss_f1d8a63c:

    mike.say "Эм..."

translate russian amy_teaser_kiss_f225405c:

    "Но именно в этот момент Эми тянется вверх и хватает меня за переднюю часть рубашки."

translate russian amy_teaser_kiss_fbcd5cb5:

    "И тут она целует меня прямо в губы."

translate russian amy_teaser_kiss_fe9dbd2f:

    "Я начинаю отвечать на поцелуй с растущим энтузиазмом."

translate russian amy_teaser_sex_00f5667b:

    shawn.say "ЭЙ, ЭМИ!"

translate russian amy_teaser_sex_01948a37:

    "Но она же никогда конкретно не говорила, где именно ей это нужно, правда?"

translate russian amy_teaser_sex_02896bf8:

    amy.say "Никто не сможет войти, а Шон будет слишком занят, чтобы нам мешать."

translate russian amy_teaser_sex_032627f1:

    "И я никогда не думал, что буду трахать Эми вот так!"

translate russian amy_teaser_sex_032627f1_1:

    "И я никогда не думал, что буду трахать Эми вот так!"

translate russian amy_teaser_sex_033a8fbc:

    mike.say "Но в целом он хороший парень!"

translate russian amy_teaser_sex_1e8e033a:

    "Ладно, ладно... давайте будем честными."

translate russian amy_teaser_sex_05c4cf67:

    "Направив свой член выше её влагалища, я целился в её аккуратную попку."

translate russian amy_teaser_sex_065cb505:

    mike.say "Ты тоже отлично выглядишь!"

translate russian amy_teaser_sex_076d611c:

    "И её юбка тоже опасно задирается!"

translate russian amy_teaser_sex_ab4f14b5:

    mike.say "Эм... нет, вроде бы ничего."

translate russian amy_teaser_sex_0b243712:

    shawn.say "Ладно, чувак..."

translate russian amy_teaser_sex_0ddf52c6:

    "Того же самого эффекта, который она сейчас оказывает на меня!"

translate russian amy_teaser_sex_0ecfb6b0:

    amy.say "Вещи, которые находятся в самой дальней части корзины."

translate russian amy_teaser_sex_0f6c7f5c:

    "Она почти мурлычет от этого ощущения, сильнее прижимая свою задницу ко мне."

translate russian amy_teaser_sex_0fadda20:

    amy.say "Что..."

translate russian amy_teaser_sex_11265af5:

    "И я не хочу останавливаться, чтобы разобраться с ним."

translate russian amy_teaser_sex_11265af5_1:

    "И я не хочу останавливаться, чтобы разобраться с ним."

translate russian amy_teaser_sex_1347deec:

    "Ну, мне, например!"

translate russian amy_teaser_sex_1347deec_1:

    "Ну, мне, например!"

translate russian amy_teaser_sex_160450cc:

    mike.say "Просто присматривался, да?"

translate russian amy_teaser_sex_1623b5d1:

    "Поэтому я киваю в знак согласия и усилию свои усилия."

translate russian amy_teaser_sex_1623b5d1_1:

    "Поэтому я киваю в знак согласия и усилию свои усилия."

translate russian amy_teaser_sex_16ddc4e0:

    "Шон закатывает глаза и поворачивается, чтобы уйти в заднюю часть помещения."

translate russian amy_teaser_sex_174a3f3a:

    "И в то же время я на грани из-за того, что знаю, нас наблюдают."

translate russian amy_teaser_sex_174a3f3a_1:

    "И в то же время я на грани из-за того, что знаю, нас наблюдают."

translate russian amy_teaser_sex_180377c9:

    amy.say "Фу..."

translate russian amy_teaser_sex_1887500e:

    "Потому что иначе я уверен, что Эми уже сейчас бы упала на пол без сознания!"

translate russian amy_teaser_sex_1887500e_1:

    "Потому что иначе я уверен, что Эми уже сейчас бы упала на пол без сознания!"

translate russian amy_teaser_sex_1887500e_2:

    "Потому что иначе я уверен, что Эми уже сейчас бы упала на пол без сознания!"

translate russian amy_teaser_sex_1887500e_3:

    "Потому что иначе я уверен, что Эми уже сейчас бы упала на пол без сознания!"

translate russian amy_teaser_sex_18dff2b9:

    "На самом деле, я почти поднимаю её над землёй!"

translate russian amy_teaser_sex_18dff2b9_1:

    "На самом деле, я почти поднимаю её над землёй!"

translate russian amy_teaser_sex_19335038:

    amy.say "Я обещаю, [hero.name]."

translate russian amy_teaser_sex_19f1dc5a:

    "Я быстро хватаю Эми за бедра, крепко сжимая их."

translate russian amy_teaser_sex_1b358b79:

    mike.say "Понимаю, как это может быть неловко!"

translate russian amy_teaser_sex_1be057af:

    "И она наверняка выставит свою задницу в мою сторону, когда так делает."

translate russian amy_teaser_sex_1bf7e73d:

    "Просто я проходил мимо магазина электроники, где работает мой друг Шон."

translate russian amy_teaser_sex_1d261ad2:

    amy.say "О том, как я получаю оральный секс в магазине от покупателя."

translate russian amy_teaser_sex_1d8c8722:

    "И я это действительно имею в виду."

translate russian amy_teaser_sex_1f75d3f2:

    mike.say "Правда?"

translate russian amy_teaser_sex_1fe949dc:

    "В конце концов, я немного разочарован, когда все заканчивается."

translate russian amy_teaser_sex_20ba89c1:

    "Ничто не может помешать мне получить то, что я хочу."

translate russian amy_teaser_sex_212c2118:

    "Пока Эми задаёт вопрос, я уже расстёгиваю свою молнию."

translate russian amy_teaser_sex_21abdeb8:

    amy.say "Поэтому мне приходится тянуться, вот так..."

translate russian amy_teaser_sex_21ae5bf2:

    "Эми пищит, когда я одним плавным движением вытаскиваю свой член из её влагалища."

translate russian amy_teaser_sex_2381f05a:

    "И тут я вижу что-то в дверном проёме, ведущем в заднюю комнату."

translate russian amy_teaser_sex_2381f05a_1:

    "И тут я вижу что-то в дверном проёме, ведущем в заднюю комнату."

translate russian amy_teaser_sex_27b826a4:

    amy.say "Он достаёт свой член."

translate russian amy_teaser_sex_27d49f37:

    "Почувствовав, что мне нужно срочно уйти, я засовываю свой член обратно в собственные штаны."

translate russian amy_teaser_sex_282c3cdc:

    amy.say "Ты же не умеешь принимать комплименты?"

translate russian amy_teaser_sex_299a30f9:

    amy.say "Я справлюсь с [hero.name] сама!"

translate russian amy_teaser_sex_2c5d83f4:

    "А затем она начинает стонать, когда я извергаю сперму на её задницу."

translate russian amy_teaser_sex_2cd56263:

    amy.say "О боже..."

translate russian amy_teaser_sex_2cd56263_1:

    amy.say "О боже..."

translate russian amy_teaser_sex_2dfb22e9:

    "Пытаясь придумать что-нибудь, чтобы продлить удовольствие, я оглядываю магазин."

translate russian amy_teaser_sex_2dfb22e9_1:

    "Пытаясь придумать что-нибудь, чтобы продлить удовольствие, я оглядываю магазин."

translate russian amy_teaser_sex_2f69f71d:

    "Она уже стоит на носочках."

translate russian amy_teaser_sex_316aac5d:

    mike.say "Потому что я ЧУДНО хочу воспользоваться твоим предложением!"

translate russian amy_teaser_sex_32e3c620:

    mike.say "На самом деле, ты у меня в мыслях с тех пор, как я тебя впервые увидел!"

translate russian amy_teaser_sex_3546f4dd:

    amy.say "Можешь угадать, что он сделает дальше?"

translate russian amy_teaser_sex_36e8ff68:

    amy.say "Ты тоже!"

translate russian amy_teaser_sex_3700f9c4:

    "Не поймите меня неправильно, Шон — довольно хороший парень."

translate russian amy_teaser_sex_390cca9d:

    "А затем она начинает стонать, пока я извергаю сперму на её ягодицы."

translate russian amy_teaser_sex_3976ead9:

    "Шон кивает, всё ещё выглядя довольно взволнованным."

translate russian amy_teaser_sex_3b810c39:

    amy.say "У меня есть одна фантазия, [hero.name]..."

translate russian amy_teaser_sex_3bc720d9:

    amy.say "Я закрыла ставни, прежде чем пришла сюда."

translate russian amy_teaser_sex_3d41c85b:

    "Я бросаю взгляд на Эми, понимая, что она, должно быть, спланировала это с самого начала."

translate russian amy_teaser_sex_403b8058:

    "Ничто из этого меня не останавливает, и медленно мой член начинает проникать в Эми."

translate russian amy_teaser_sex_412a7243:

    mike.say "Ну, он иногда бывает немного... педантичным."

translate russian amy_teaser_sex_433fc528:

    shawn.say "Извини, я спешу, нужно кое-что закончить в задней части магазина!"

translate russian amy_teaser_sex_437b237a:

    shawn.say "Привет, [hero.name]!"

translate russian amy_teaser_sex_43d5b967:

    "И я изо всех сил пытаюсь привлечь внимание Шона, пока он зовёт её."

translate russian amy_teaser_sex_450dcfdc:

    "Она пытается вовлечь меня в это, заставить меня участвовать в ролевой игре!"

translate russian amy_teaser_sex_45b0de75:

    "Поэтому я решаю заглянуть и посмотреть, как сегодня дела у Шона."

translate russian amy_teaser_sex_46550ff1:

    "Я думаю, у меня есть не больше нескольких секунд, чтобы решить, что будет дальше..."

translate russian amy_teaser_sex_46550ff1_1:

    "Я думаю, у меня есть не больше нескольких секунд, чтобы решить, что будет дальше..."

translate russian amy_teaser_sex_46a00bc3:

    amy.say "Он поднимает мою юбку!"

translate russian amy_teaser_sex_46f9c3c2:

    "Эми подносит руку к виску, изображая жест телефонного звонка."

translate russian amy_teaser_sex_47340aca:

    amy.say "Привет, [hero.name]!"

translate russian amy_teaser_sex_47a8d18d:

    "Но сейчас у меня уже глубоко член внутри неё."

translate russian amy_teaser_sex_47a8d18d_1:

    "Но сейчас у меня уже глубоко член внутри неё."

translate russian amy_teaser_sex_49445dd2:

    "Эми начинает пищать, когда я проникаю в неё настолько глубоко, насколько это возможно."

translate russian amy_teaser_sex_49445dd2_1:

    "Эми начинает пищать, когда я проникаю в неё настолько глубоко, насколько это возможно."

translate russian amy_teaser_sex_4a86e050:

    "Эми наполовину открывает ставни и почти выталкивает меня из магазина."

translate russian amy_teaser_sex_4b69013a:

    "Я не могу сказать, что мне нравится идея того, что Шон наблюдает за тем, как я трахаюсь с Эми!"

translate russian amy_teaser_sex_4b69013a_1:

    "Я не могу сказать, что мне нравится идея того, что Шон наблюдает за тем, как я трахаюсь с Эми!"

translate russian amy_teaser_sex_43deda51:

    amy.say "Понимаешь... у меня есть другой парень, который мне нравится!"

translate russian amy_teaser_sex_4ee4a7b3:

    "Вдруг меня озаряет, что делает Эми."

translate russian amy_teaser_sex_4ef29c01:

    "Потому что я уверен, что это положит конец тому, чем мы занимаемся прямо сейчас."

translate russian amy_teaser_sex_4ef29c01_1:

    "Потому что я уверен, что это положит конец тому, чем мы занимаемся прямо сейчас."

translate russian amy_teaser_sex_4f0f441c:

    "Одновременно она тянется и нежно гладит мою щёку."

translate russian amy_teaser_sex_50b6584c:

    "Эми поворачивается и наклоняется над корзиной перед собой."

translate russian amy_teaser_sex_50d7dd17:

    "Эми бросает взгляд на дверь в служебный кабинет, словно боится, что Шон снова появится."

translate russian amy_teaser_sex_50fdd82d:

    amy.say "В любом случае, ты гораздо веселее, чем Шон сейчас!"

translate russian amy_teaser_sex_5442fe5d:

    shawn.say "О..."

translate russian amy_teaser_sex_55185f12:

    "Она поворачивается к Шону и отмахивается от него рукой."

translate russian amy_teaser_sex_5658ac30:

    "Кажется, она слышит звук, и снова хихикает."

translate russian amy_teaser_sex_56d7c8b8:

    amy.say "ЧТО?"

translate russian amy_teaser_sex_599fba12:

    amy.say "Позвони мне, хорошо?"

translate russian amy_teaser_sex_59b11375:

    "Она выглядит довольной тем, что я признался ей в своих чувствах."

translate russian amy_teaser_sex_59c1cec5:

    shawn.say "Что бы ты ни говорила, Эми..."

translate russian amy_teaser_sex_e5a3f069:

    mike.say "Ты серьёзно, Эми?"

translate russian amy_teaser_sex_5b58d1ac:

    "Там очень тесно, и её мышцы постоянно сжимают меня, пытаясь не пустить меня внутрь."

translate russian amy_teaser_sex_5c816265:

    "Но, делая это, она кричит мне вслед."

translate russian amy_teaser_sex_5c8d820b:

    amy.say "Рада снова тебя видеть!"

translate russian amy_teaser_sex_37c2a191:

    mike.say "Шон...смотрит!"

translate russian amy_teaser_sex_37c2a191_1:

    mike.say "Шон... смотрит!"

translate russian amy_teaser_sex_5d645fa9:

    "Она не просто показывает мне свою фантазию."

translate russian amy_teaser_sex_5fa3e7cf:

    amy.say "Чёрт..."

translate russian amy_teaser_sex_61fcd316:

    "Она стонет и выдыхает, когда он входит внутрь, явно наслаждаясь каждым моментом."

translate russian amy_teaser_sex_61fcd316_1:

    "Она стонет и выдыхает, когда он входит внутрь, явно наслаждаясь каждым моментом."

translate russian amy_teaser_sex_671b914f:

    "Эми немного продвинулась вперёд, но она всё равно хихикает и кивает."

translate russian amy_teaser_sex_6832f70c:

    "Уже почти закрытие магазина, а обычно в это время здесь довольно тихо."

translate russian amy_teaser_sex_68c0f290:

    "Я всё ещё чувствую, что нас могут поймать в любой момент."

translate russian amy_teaser_sex_6add1126:

    "Я оглядываюсь, пытаясь найти Шона среди полок."

translate russian amy_teaser_sex_6b319ac8:

    amy.say "Дело не в этом, [hero.name]."

translate russian amy_teaser_sex_6c823ff5:

    mike.say "Ты хочешь заняться этим?"

translate russian amy_teaser_sex_6d596abe:

    "Но когда он не появляется даже при упоминании его имени, она, кажется, успокаивается."

translate russian amy_teaser_sex_6f147f2f:

    mike.say "Здесь и сейчас?!"

translate russian amy_teaser_sex_70028224:

    amy.say "Да, [hero.name], именно так!"

translate russian amy_teaser_sex_700f54ac:

    mike.say "Вот так..."

translate russian amy_teaser_sex_70d96dbf:

    mike.say "Я не могу тебе отказать, Эми."

translate russian amy_teaser_sex_7142b9f1:

    "Затем ставни снова захлопываются, и я остаюсь один снаружи магазина."

translate russian amy_teaser_sex_7531810b:

    "Но потом я снова смотрю на неё, и я знаю, каким будет мой ответ."

translate russian amy_teaser_sex_78aa6762:

    "Но также потому, что у меня есть сюрприз для неё."

translate russian amy_teaser_sex_79dd7541:

    "Кажется, Эми начала возбуждаться почти с того момента, как увидела меня!"

translate russian amy_teaser_sex_7d9e2dba:

    amy.say "Конечно, [hero.name]!"

translate russian amy_teaser_sex_7e4809bd:

    mike.say "Что, если кто-то нас увидит?"

translate russian amy_teaser_sex_7e996cff:

    amy.say "И он намного привлекательнее Шона..."

translate russian amy_teaser_sex_809dab97:

    amy.say "Не волнуйся, [hero.name]."

translate russian amy_teaser_sex_81cd0d4b:

    amy.say "МНЕ это нужно..."

translate russian amy_teaser_sex_81cd0d4b_1:

    amy.say "Мне это НУЖНО..."

translate russian amy_teaser_sex_82255768:

    "И дать Эми именно то, чего она хочет!"

translate russian amy_teaser_sex_83e8558b:

    "И это потому, что там уже все скользкое и влажное."

translate russian amy_teaser_sex_83fd9fdf:

    "Её синие волосы покачиваются вверх и вниз, когда она проходит небольшое расстояние до того места, где я стою."

translate russian amy_teaser_sex_85e7f352:

    "И мой член становится твёрдым, как камень, только при мысли о том, чтобы заняться с ней."

translate russian amy_teaser_sex_86730e8e:

    shawn.say "Ты сможешь присмотреть за [hero.name]?"

translate russian amy_teaser_sex_87fe0fdf:

    "Затем я отвечаю на поцелуй с такой же страстью, какую Эми способна выдержать."

translate russian amy_teaser_sex_88c66995:

    "Но вскоре я забываю о нём и начинаю думать об Эми."

translate russian amy_teaser_sex_88e7af72:

    "Едва отдышавшись, Эми начинает стягивать свои трусики."

translate russian amy_teaser_sex_89a89fcb:

    mike.say "Ты уверена, Эми?"

translate russian amy_teaser_sex_8df1d2c9:

    "Ему не требуется много усилий, чтобы мой член начал проникать в Эми."

translate russian amy_teaser_sex_8e1dff0f:

    "И её язык проникает в мой рот ещё до того, как я успеваю понять, что происходит!"

translate russian amy_teaser_sex_8f56215c:

    amy.say "Тогда ты знаешь, что делает этот извращенец?"

translate russian amy_teaser_sex_93e8bd5b:

    amy.say "Да, это именно так!"

translate russian amy_teaser_sex_940d6101:

    amy.say "А потом он засовывает его мне!"

translate russian amy_teaser_sex_954ac9fe:

    amy.say "Ой..."

translate russian amy_teaser_sex_9638e62e:

    mike.say "Эми..."

translate russian amy_teaser_sex_9638e62e_1:

    mike.say "Эми..."

translate russian amy_teaser_sex_9699f4f2:

    "Я наблюдаю, как Эми тянется к задней части корзины."

translate russian amy_teaser_sex_45b4d646:

    mike.say "О... ты действительно так думаешь?"

translate russian amy_teaser_sex_9b1fffcf:

    "Я отвожу взгляд от Эми на мгновение, поворачивая голову в сторону задней части магазина."

translate russian amy_teaser_sex_9b975450:

    "И я думаю о том, что, чёрт возьми, мог подумать об этом Шон."

translate russian amy_teaser_sex_9c75c525:

    amy.say "Ни за что, [hero.name]!"

translate russian amy_teaser_sex_a0754296:

    "Я вижу, как его голова мелькает по одному из проходов на высокой скорости."

translate russian amy_teaser_sex_a127f6ca:

    "Затем она начинает стонать, когда я наконец теряю контроль и извергаю сперму."

translate russian amy_teaser_sex_a127f6ca_1:

    "Затем она начинает стонать, когда я наконец теряю контроль и извергаю сперму."

translate russian amy_teaser_sex_a1321d11:

    "Я опускаю взгляд на себя, и меня это немного удивляет."

translate russian amy_teaser_sex_a19c62e3:

    amy.say "Но знаешь что — я хочу большего!"

translate russian amy_teaser_sex_a36fcece:

    "Эми улыбается мне, крутя свои синие волосы одной рукой."

translate russian amy_teaser_sex_a4bb270c:

    "Но озорная улыбка на лице Эми компенсирует это разочарование."

translate russian amy_teaser_sex_a543b956:

    "Мои глаза расширяются, когда Эми наклоняется вперёд и прижимает свои губы к моим."

translate russian amy_teaser_sex_a55cf6cd:

    amy.say "Иди-ка ты, Шон."

translate russian amy_teaser_sex_a6ac5dec:

    mike.say "Что, если Шон нас поймает?"

translate russian amy_teaser_sex_a716ca17:

    amy.say "Кому какое дело?"

translate russian amy_teaser_sex_a716ca17_1:

    amy.say "Кому какое дело?"

translate russian amy_teaser_sex_a9eec336:

    amy.say "Этот парень постоянно просит меня доставать вещи."

translate russian amy_teaser_sex_ab9ab91b:

    "Она так хорошо ощущается вокруг моего члена, я хочу, чтобы это продолжалось дольше."

translate russian amy_teaser_sex_ab9ab91b_1:

    "Она так хорошо ощущается вокруг моего члена, я хочу, чтобы это продолжалось дольше."

translate russian amy_teaser_sex_acaaeb2f:

    amy.say "ЧЕМ ЗАНИМАЕШЬСЯ, ШОН?"

translate russian amy_teaser_sex_af9935bf:

    "Но это не совсем неожиданно, и я быстро прихожу в себя."

translate russian amy_teaser_sex_b1158528:

    amy.say "Вот это уже лучше!"

translate russian amy_teaser_sex_b1158528_1:

    amy.say "Вот это уже лучше!"

translate russian amy_teaser_sex_b20d313a:

    "Эми кивает и тихонько хихикает."

translate russian amy_teaser_sex_b2331f88:

    "И Эми, кажется, сразу же оценила работу, которую я проделал."

translate russian amy_teaser_sex_b2331f88_1:

    "И Эми, кажется, сразу же оценила работу, которую я проделал."

translate russian amy_teaser_sex_b2afc985:

    amy.say "Ммм..."

translate russian amy_teaser_sex_b2afc985_1:

    amy.say "Ммм..."

translate russian amy_teaser_sex_b2afc985_2:

    amy.say "Ммм..."

translate russian amy_teaser_sex_b2e83d33:

    shawn.say "Мне нужно отойти в подсобку."

translate russian amy_teaser_sex_b3cd1441:

    "Зайдя в магазин, я сразу вижу, что я единственный потенциальный покупатель."

translate russian amy_teaser_sex_b443c437:

    "К этому моменту Эми уже сильно меня возбудила, как ты, наверное, можешь себе представить."

translate russian amy_teaser_sex_b748e488:

    amy.say "Шон — довольно спокойный начальник, ты знаешь?"

translate russian amy_teaser_sex_bcc13120:

    shawn.say "Слушай, просто позови Эми, если тебе что-нибудь понадобится, хорошо?"

translate russian amy_teaser_sex_bf1c3825:

    "Интересно, сколько мне нужно подождать, прежде чем позвонить ей."

translate russian amy_teaser_sex_bfc4474f:

    "Она опирается о корзину, полную игр со скидкой."

translate russian amy_teaser_sex_c161531e:

    "Я чуть не подпрыгиваю от одного упоминания имени её коллеги."

translate russian amy_teaser_sex_c196902b:

    "Но когда я наконец его замечаю, это лишь мимолётный взгляд."

translate russian amy_teaser_sex_c2db1c31:

    amy.say "Что ты делаешь..."

translate russian amy_teaser_sex_c3532fe6:

    "Улыбка Эми говорит мне всё, что мне нужно знать."

translate russian amy_teaser_sex_c665391c:

    mike.say "Очень рад тебя видеть, Эми!"

translate russian amy_teaser_sex_c6c9bbb5:

    "Как только мы остаёмся одни, я чувствую волну облегчения."

translate russian amy_teaser_sex_c6f3b014:

    amy.say "О да..."

translate russian amy_teaser_sex_c6f3b014_1:

    amy.say "О, да..."

translate russian amy_teaser_sex_c7311c11:

    "И хорошо, что она наклонилась над корзиной, пока все это происходит."

translate russian amy_teaser_sex_c7311c11_1:

    "И хорошо, что она наклонилась над корзиной, пока все это происходит."

translate russian amy_teaser_sex_c7311c11_2:

    "И хорошо, что она наклонилась над корзиной, пока все это происходит."

translate russian amy_teaser_sex_c7311c11_3:

    "И хорошо, что она наклонилась над корзиной, пока все это происходит."

translate russian amy_teaser_sex_c74f34be:

    "Я давил изо всех сил, насколько позволяло, погружая головку своего члена в отверстие Эми."

translate russian amy_teaser_sex_c87c882d:

    "Эми качает головой, отвергая мои доводы в пользу Шона."

translate russian amy_teaser_sex_c8fb5fd4:

    amy.say "Ах, пошли его, [hero.name]!"

translate russian amy_teaser_sex_c8fb5fd4_1:

    amy.say "Ах, пошли его, [hero.name]!"

translate russian amy_teaser_sex_c9c55fa5:

    "Корзина гремит под Эми, пока я яростно двигаюсь в ней."

translate russian amy_teaser_sex_c9c55fa5_1:

    "Корзина гремит под Эми, пока я яростно двигаюсь в ней."

translate russian amy_teaser_sex_ca22bd67:

    amy.say "Я так долго этого ждала!"

translate russian amy_teaser_sex_e3a6be64:

    amy.say "Ты представляешь, я наклоняюсь вперёд... вот так."

translate russian amy_teaser_sex_ccc2305e:

    "Я пожимаю плечами, чувствуя себя немного неловко."

translate russian amy_teaser_sex_ccf146b9:

    "И её голова наклонена ко мне."

translate russian amy_teaser_sex_ceb53051:

    "Я киваю и улыбаюсь, с нетерпением ожидая близости с Эми."

translate russian amy_teaser_sex_cf01586a:

    "Я ни в чём не стесняюсь, позволяя ей получить всё, что я могу дать."

translate russian amy_teaser_sex_cf01586a_1:

    "Я ни в чём не стесняюсь, позволяя ей получить всё, что я могу дать."

translate russian amy_teaser_sex_d35dc4d2:

    "А именно — я начинаю кончить!"

translate russian amy_teaser_sex_d35dc4d2_1:

    "А именно — я начинаю кончить!"

translate russian amy_teaser_sex_d3c25749:

    "Белые полосы спермы покрывают её бледную кожу и впитываются в её юбку."

translate russian amy_teaser_sex_d3c25749_1:

    "Белые полосы спермы покрывают её бледную кожу и впитываются в её юбку."

translate russian amy_teaser_sex_d3d17437:

    "Я киваю головой, даже пока вставляю пальцы в резинку трусиков Эми."

translate russian amy_teaser_sex_d3e4797a:

    "Поэтому я не теряю времени и сразу перехожу к делу."

translate russian amy_teaser_sex_d4c5ef5a:

    mike.say "Эй, Шон!"

translate russian amy_teaser_sex_d77cea10:

    "И её смех становится ещё более восторженным, когда я поднимаю её юбку."

translate russian amy_teaser_sex_d7bb15ab:

    "Эми стонет, когда я одним плавным движением вытаскиваю свой член из её ануса."

translate russian amy_teaser_sex_da1de010:

    mike.say "Он слишком тебя заставляет работать или что-то в этом роде?"

translate russian amy_teaser_sex_dc3747c3:

    "Именно сочетание этих двух факторов, как мне кажется, и стало причиной того, что произошло дальше."

translate russian amy_teaser_sex_dc3747c3_1:

    "Именно сочетание этих двух факторов, как мне кажется, и стало причиной того, что произошло дальше."

translate russian amy_teaser_sex_dd07420e:

    "Но он не оказывает на меня такого же эффекта, как Эми."

translate russian amy_teaser_sex_dd3a8364:

    amy.say "Ты хорошо выглядишь, то есть..."

translate russian amy_teaser_sex_deaa474f:

    "Примерно в этот момент я понимаю, что Эми гладит меня ниже пояса."

translate russian amy_teaser_sex_df6be74b:

    "Я подхожу к ней сзади и прижимаю свой член к её ягодицам."

translate russian amy_teaser_sex_e0b709ed:

    amy.say "О, блин, [hero.name]..."

translate russian amy_teaser_sex_e0b709ed_1:

    amy.say "О, блин, [hero.name]..."

translate russian amy_teaser_sex_e24ae26a:

    "Я уже набираю скорость, двигаясь вперёд и назад внутри неё."

translate russian amy_teaser_sex_e24ae26a_1:

    "Я уже набираю скорость, двигаясь вперёд и назад внутри неё."

translate russian amy_teaser_sex_e341d7ff:

    amy.say "Это было очень весело, [hero.name]!"

translate russian amy_teaser_sex_e38bd009:

    "И теперь она кажется ещё более решительной, чтобы и она добилась своего со мной!"

translate russian amy_teaser_sex_e41395a3:

    "И мне приходится помахать рукой, чтобы убедиться, что он меня заметил."

translate russian amy_teaser_sex_e4305593:

    "Я пожимаю плечами и поворачиваюсь, чтобы уйти."

translate russian amy_teaser_sex_e53a0c6b:

    shawn.say "Тебе что-то нужно?"

translate russian amy_teaser_sex_e5ce134b:

    "Почему бы ей иначе закрыть жалюзи и так резко выпроводить Шона?"

translate russian amy_teaser_sex_e7d05b3f:

    amy.say "Будет только ты и я — будем веселиться!"

translate russian amy_teaser_sex_e84ffc6f:

    mike.say "Что?"

translate russian amy_teaser_sex_e885e53b:

    "Затем она торопит меня к двери, постоянно оглядываясь через плечо."

translate russian amy_teaser_sex_e9c93109:

    amy.say "А потом этот мерзавец стягивает мои трусики, ты можешь себе представить?!"

translate russian amy_teaser_sex_ea93bf03:

    "Прежде чем я успеваю возразить, я вижу, как появляется верх головы Эми."

translate russian amy_teaser_sex_eb66b802:

    "Я так взволнован возможностью заняться с Эми таким образом."

translate russian amy_teaser_sex_eb66b802_1:

    "Я так взволнован возможностью заняться с Эми таким образом."

translate russian amy_teaser_sex_eca5679d:

    "Эми кивает и хихикает, явно довольная тем, что заманила меня в свою ловушку."

translate russian amy_teaser_sex_ed36ab64:

    "Я оглядываюсь вокруг в магазине."

translate russian amy_teaser_sex_1f9a5897:

    amy.say "Просто... у меня такое ощущение, что он хочет от меня большего!"

translate russian amy_teaser_sex_ee796b93:

    amy.say "А мне он просто неинтересен, да?"

translate russian amy_teaser_sex_f11c6403:

    mike.say "Ты уверена, что Шон — не подходящий кандидат для отношений?"

translate russian amy_teaser_sex_f1d8a63c:

    mike.say "Эм..."

translate russian amy_teaser_sex_f1d8a63c_1:

    mike.say "Эм..."

translate russian amy_teaser_sex_f1d8a63c_2:

    mike.say "Эм..."

translate russian amy_teaser_sex_f53daee5:

    "Я как-то надеялся, что Эми будет рядом, когда я решил зайти в этот магазин."

translate russian amy_teaser_sex_f60f8207:

    "Голова моего члена скользит по губам её влагалища."

translate russian amy_teaser_sex_f955f24c:

    "И затем я опускаю их вниз, обнажая бледные щечки её ягодиц."

translate russian amy_teaser_sex_fc71b18a:

    amy.say "Я никогда не думала, что ты будешь таким БОЛЬШИМ!"

translate russian amy_teaser_sex_fc71b18a_1:

    amy.say "Я никогда не думала, что ты будешь таким БОЛЬШИМ!"

translate russian amy_teaser_sex_fec0c84c:

    "Она конкретно трёт мой член через штаны!"

translate russian amy_teaser_sex_fec2a8ab:

    amy.say "Спасибо, [hero.name]!"

translate russian angela_afterblow_bruce_call_000ea0ce:

    breesdad "Да ладно тебе, ни за что!"

translate russian angela_afterblow_bruce_call_07d17da3:

    breesdad "Она только и хотела, чтобы я рассказал ей информацию о [bree.name]!"

translate russian angela_afterblow_bruce_call_0e3bf868:

    "Я слышу, как Брюс смеётся на другом конце линии."

translate russian angela_afterblow_bruce_call_109eface:

    "Во второй раз я удивляюсь тому, что говорит Брюс."

translate russian angela_afterblow_bruce_call_128f80cd:

    mike.say "Я видел, как ты был там с моей мамой!"

translate russian angela_afterblow_bruce_call_15321788:

    "Я пытаюсь игнорировать угрожающий тон голоса, который использует Брюс."

translate russian angela_afterblow_bruce_call_27e41cc0:

    breesdad "Что тебе нужно?"

translate russian angela_afterblow_bruce_call_29421a35:

    breesdad "[hero.name] кто?"

translate russian angela_afterblow_bruce_call_2d4583a7:

    breesdad "Я не узнаю этот номер!"

translate russian angela_afterblow_bruce_call_34fe0985:

    mike.say "Привет, Брюс — это [hero.name]."

translate russian angela_afterblow_bruce_call_37e9c219:

    breesdad "Но она продолжала спрашивать!"

translate russian angela_afterblow_bruce_call_470a9236:

    "И с этими словами он завершает звонок."

translate russian angela_afterblow_bruce_call_4d1906b8:

    breesdad "Да, я ходил на свидание с твоей мамой."

translate russian angela_afterblow_bruce_call_503145f3:

    "И это меня сбивает с толку."

translate russian angela_afterblow_bruce_call_553ec2ee:

    breesdad "В любом случае, она была плохой компанией."

translate russian angela_afterblow_bruce_call_5d49cfa8:

    "И у меня уже достаточно информации, чтобы мои мысли завертелись от возможностей."

translate russian angela_afterblow_bruce_call_6262c021:

    breesdad "Особенно после того, что твоя сумасшедшая мать со мной сделала!"

translate russian angela_afterblow_bruce_call_6bc85d69:

    breesdad "Я не знаю никакого чертового [hero.name]!"

translate russian angela_afterblow_bruce_call_6fc80885:

    "Почему моя мама могла пойти за спиной моего отца, а потом выбросить Брюса на следующий день?"

translate russian angela_afterblow_bruce_call_71c0e28e:

    breesdad "Ты оба можете держаться от меня подальше!"

translate russian angela_afterblow_bruce_call_77cbfb63:

    "Телефон несколько раз звонит, а потом он отвечает."

translate russian angela_afterblow_bruce_call_7ae80ddc:

    "И, к сожалению, Брюс тоже это слышит."

translate russian angela_afterblow_bruce_call_29a59224:

    mike.say "Ага, да...спасибо, Брюс."

translate russian angela_afterblow_bruce_call_81a9f94e:

    "И ещё есть вопрос о том, как она расспрашивала этого парня о [bree.name]."

translate russian angela_afterblow_bruce_call_81f7aca7:

    "Она осознала, что совершила ошибку, и почувствовала угрызения совести?"

translate russian angela_afterblow_bruce_call_82c25ed0:

    mike.say "Она спрашивала у тебя про [bree.name]?"

translate russian angela_afterblow_bruce_call_86ffb563:

    mike.say "Моя мама не сумасшедшая!"

translate russian angela_afterblow_bruce_call_87567724:

    breesdad "Ладно, приятель, я буду честен с тобой."

translate russian angela_afterblow_bruce_call_89a65dbd:

    "В итоге у меня теперь ещё больше вопросов, чем было раньше!"

translate russian angela_afterblow_bruce_call_92caf287:

    breesdad "Кто, чёрт возьми, мне звонит?"

translate russian angela_afterblow_bruce_call_9883aeec:

    "Я заканчиваю разговор, так как Брюс больше ничего не предлагает."

translate russian angela_afterblow_bruce_call_98d5309c:

    breesdad "Ну а почему бы и нет?"

translate russian angela_afterblow_bruce_call_9e5aac25:

    breesdad "Похоже, ты знаешь только часть правды!"

translate russian angela_afterblow_bruce_call_a3187c1f:

    "Прежде чем я успеваю сказать хоть слово, Брюс перебивает меня."

translate russian angela_afterblow_bruce_call_b40a650e:

    breesdad "Не знаю, сопляк!"

translate russian angela_afterblow_bruce_call_b544b0b1:

    breesdad "И теперь, когда я об этом подумал — кто дал тебе мой чёртов номер?"

translate russian angela_afterblow_bruce_call_b5f1cffb:

    "Я не могу сдержать вздох облегчения, услышав эту новость."

translate russian angela_afterblow_bruce_call_be1e1baa:

    breesdad "Но она разорвала отношения на следующий день — бросила меня через текстовое сообщение!"

translate russian angela_afterblow_bruce_call_c3bba402:

    breesdad "Она очень привлекательная!"

translate russian angela_afterblow_bruce_call_c9982741:

    mike.say "Я — сожитель [bree.name], помнишь?"

translate russian angela_afterblow_bruce_call_ca8540bc:

    breesdad "Ты совсем обнаглел, парень, названивая мне."

translate russian angela_afterblow_bruce_call_caef364f:

    breesdad "Да-да, смейся, сопляк."

translate russian angela_afterblow_bruce_call_ce9be00c:

    "Почему ей так интересно, станет ли одна из моих соседок хорошей женой?"

translate russian angela_afterblow_bruce_call_cec314e1:

    mike.say "Я видел тебя в ресторане на днях, Брюс."

translate russian angela_afterblow_bruce_call_cfb2df40:

    breesdad "Как будто моя маленькая девочка могла бы подойти для такого неудачника, как ты!"

translate russian angela_afterblow_bruce_call_d1663f37:

    breesdad "Я и так натерпелся от твоей сумасшедшей мамы."

translate russian angela_afterblow_bruce_call_e364a874:

    breesdad "А, ЭТОТ [hero.name]!"

translate russian angela_afterblow_bruce_call_ec7ebdd9:

    "Это был не тот ответ, который я ожидал."

translate russian angela_afterblow_bruce_call_eceb28af:

    breesdad "Она сказала что-то вроде того, что ей нужно узнать, подходишь ли ты ей как 'жена'!"

translate russian angela_afterblow_bruce_call_f4574d51:

    mike.say "Зачем ей это?"

translate russian angela_afterblow_bruce_call_f7001728:

    "И вместо этого я сосредотачиваюсь на настоящей причине моего звонка ему."

translate russian angela_afterblow_bruce_call_f934f74a:

    "Как только я остался один, я звоню."

translate russian angela_afterblow_bruce_call_6c2acc3a:

    mike.say "Ч-что ты имеешь в виду?"

translate russian angela_afterblow_call_061614d8:

    "И, возможно, достаточно времени, чтобы она подумала, что ей всё сошло с рук."

translate russian angela_afterblow_call_669e9c7a:

    mike.say "Ну... была одна вещь, мам."

translate russian angela_afterblow_call_1116852e:

    "На другом конце линии повисает пауза."

translate russian angela_afterblow_call_34112b9e:

    mike.say "То есть, ты ужинала с кем-то!"

translate russian angela_afterblow_call_345531a1:

    mike.say "Если это твоя версия, то я тебе верю."

translate russian angela_afterblow_call_4776769c:

    angela.say "Ой, нет, это не могла быть я, дорогой."

translate russian angela_afterblow_call_4d698837:

    "Объяснения моей мамы не убедили меня."

translate russian angela_afterblow_call_50859c2f:

    angela.say "Привет, дорогой!"

translate russian angela_afterblow_call_548052a7:

    angela.say "Тебе что-то нужно?"

translate russian angela_afterblow_call_54f1eba4:

    "Но теперь у меня больше вопросов, чем когда я только начал погружаться в эту историю!"

translate russian angela_afterblow_call_5580220f:

    mike.say "Я же не говорил, что это был ресторан!"

translate russian angela_afterblow_call_5f5f1447:

    mike.say "Я не думал, что это могла быть ты."

translate russian angela_afterblow_call_6122594f:

    "Поэтому я сразу же задаю вопрос."

translate russian angela_afterblow_call_705fb129:

    mike.say "Хорошо, мам."

translate russian angela_afterblow_call_62cc1a5b:

    angela.say "О... просто так, дорогой."

translate russian angela_afterblow_call_78f2187e:

    angela.say "В любом случае, это не имеет большого значения, правда?"

translate russian angela_afterblow_call_85bbf1f9:

    "Но когда она наконец заговорила, я был очень удивлён."

translate russian angela_afterblow_call_89fb0610:

    "Поэтому, пока что, я решил притвориться, что верю ей."

translate russian angela_afterblow_call_8b226521:

    mike.say "Мы могли быть в кафе, у ларька с хот-догами, даже перекусывать бургером в пабе."

translate russian angela_afterblow_call_903e0598:

    angela.say "Потому что я уже сказала тебе, что меня там не было."

translate russian angela_afterblow_call_91f1a53c:

    "Я заканчиваю разговор и не могу удержаться от того, чтобы покачать головой в замешательстве."

translate russian angela_afterblow_call_9500f2a9:

    mike.say "Привет, мам..."

translate russian angela_afterblow_call_95bfe2db:

    mike.say "И я тебя там увидел — ты была с кем-то..."

translate russian angela_afterblow_call_98c65439:

    "Нет смысла ходить вокруг да около."

translate russian angela_afterblow_call_a342e22a:

    "Как обычно, ей не требуется много времени, чтобы ответить, когда я звоню."

translate russian angela_afterblow_call_a5e7c6b1:

    mike.say "Конечно, мам."

translate russian angela_afterblow_call_aa3845d2:

    "Я почти слышу, как в голове моей мамы что-то происходит."

translate russian angela_afterblow_call_b113d59a:

    angela.say "Ты можешь звонить мне в любое время, помни об этом!"

translate russian angela_afterblow_call_b69e086e:

    "Либо Брюс получал оральный секс от своей давно потерянной сестры-близнеца."

translate russian angela_afterblow_call_bbc4f282:

    angela.say "Это просто такая фраза — понимаешь?"

translate russian angela_afterblow_call_bd3c4753:

    mike.say "Почему ты вообще упомянула ресторан?"

translate russian angela_afterblow_call_c201a06f:

    angela.say "Я там не была, где бы это ни было, хорошо?"

translate russian angela_afterblow_call_c525ac3c:

    "То есть, не сразу после того, как мы вышли из ресторана, где видели её."

translate russian angela_afterblow_call_cc04e281:

    "Я не жду слишком долго, прежде чем беру телефон и звоню маме."

translate russian angela_afterblow_call_cee48c5a:

    mike.say "Я ужинал в ресторане на днях."

translate russian angela_afterblow_call_d4cb416c:

    "Просто достаточно времени, чтобы прийти в себя и понять, что я хочу у неё спросить."

translate russian angela_afterblow_call_d9856168:

    "Этот звонок должен был прояснить для меня ситуацию, объяснить, что происходит."

translate russian angela_afterblow_call_da194e56:

    "Но если она этого не признает, что я могу сделать?"

translate russian angela_afterblow_call_dea8953f:

    "Я делаю глубокий вдох, готовясь к тому, что будет дальше."

translate russian angela_afterblow_call_dee6f586:

    angela.say "Я была здесь, дома, с твоим отцом."

translate russian angela_afterblow_call_e2b030ac:

    angela.say "Как приятно, что ты позвонил."

translate russian angela_afterblow_call_e84ffc6f:

    mike.say "Что?"

translate russian angela_afterblow_call_eb42d52d:

    "Я не хочу выходить и обвинять её в измене и лжи."

translate russian angela_afterblow_call_f38cf864:

    angela.say "Я ни в одном ресторане не была."

translate russian angela_afterblow_call_f7393625:

    "Или она просто неистово врёт, пытаясь скрыть свои действия."

translate russian angela_afterblow_call_f91aa6de:

    mike.say "Но я просто хотел убедиться."

translate russian angela_afterblow_call_fb1bb1c4:

    angela.say "Или ты просто хотел поговорить со своей мамой?"

translate russian angela_afterblow_call_fb346ca2:

    angela.say "Конечно, дорогой."

translate russian angela_afterblow_dad_call_02c40ef6:

    mike.say "Это совсем не так, честно говоря."

translate russian angela_afterblow_dad_call_06143e61:

    "Dad" "Давай же, [hero.name], выкладывай."

translate russian angela_afterblow_dad_call_08bf155b:

    mike.say "Что ты имеешь в виду, что ты уже все знаешь?!"

translate russian angela_afterblow_dad_call_0c8f2a7a:

    "Dad" "Ты обычно звонишь мне только тогда, когда тебе что-то нужно!"

translate russian angela_afterblow_dad_call_0d503636:

    "Dad" "Ну что ж, это другое дело, сынок."

translate russian angela_afterblow_dad_call_0edc4ce4:

    "Dad" "Мы вместе уже давно, и иногда случаются ошибки."

translate russian angela_afterblow_dad_call_11bb0d26:

    "И я представляю, как он качает головой."

translate russian angela_afterblow_dad_call_1253ac6b:

    "И кажется, мой отец воспринимает это как подтверждение своих подозрений."

translate russian angela_afterblow_dad_call_179d3a3a:

    "Я слышу, как мой отец вздыхает на другом конце линии."

translate russian angela_afterblow_dad_call_1a573d51:

    "Dad" "Хорошо, сынок, хорошо!"

translate russian angela_afterblow_dad_call_6b2513a7:

    mike.say "И мама тоже была там... с другим мужчиной!"

translate russian angela_afterblow_dad_call_21be2ad4:

    "Я не могу удержаться от нервного смеха."

translate russian angela_afterblow_dad_call_23a97a55:

    "Dad" "Я все это знаю."

translate russian angela_afterblow_dad_call_29834e55:

    "Dad" "И мы тоже любим друг друга."

translate russian angela_afterblow_dad_call_2c8e3584:

    "Dad" "Просто помни, что мама и я любим тебя."

translate russian angela_afterblow_dad_call_2d58a3be:

    "Это как закрыть глаза, ожидая, что тебе дадут пощёчину."

translate russian angela_afterblow_dad_call_368305b4:

    "Я стараюсь отогнать эти мысли, надеясь, что я ошибаюсь и он прав."

translate russian angela_afterblow_dad_call_39b0e029:

    "У меня нет ни малейшего представления о том, как он отреагирует на эту новость."

translate russian angela_afterblow_dad_call_39db924f:

    "И когда он заговорил, его голос стал более серьёзным."

translate russian angela_afterblow_dad_call_47d84b93:

    mike.say "Они вместе зашли в ванную комнату, и..."

translate russian angela_afterblow_dad_call_4c7f8e66:

    mike.say "Нет, пап..."

translate russian angela_afterblow_dad_call_504d21b7:

    "Dad" "Я всегда буду рядом, чтобы помочь своему единственному сыну!"

translate russian angela_afterblow_dad_call_5aa6e49f:

    "Dad" "Твоя мама извинилась, и мы стараемся разобраться с этим."

translate russian angela_afterblow_dad_call_5b5e170f:

    mike.say "Если ты так говоришь, пап."

translate russian angela_afterblow_dad_call_5bebc7d0:

    "А потом экспериментально снова открыть их, когда удара не происходит."

translate russian angela_afterblow_dad_call_5f3b87dc:

    "Dad" "Ну, не стоит."

translate russian angela_afterblow_dad_call_61cbfff9:

    mike.say "У меня есть кое-что сказать тебе, кое-что, что тебе нужно знать."

translate russian angela_afterblow_dad_call_6940b22b:

    "Dad" "Что послужило причиной этой чести?"

translate russian angela_afterblow_dad_call_69ab713c:

    "Dad" "Я уже знаю все подробности!"

translate russian angela_afterblow_dad_call_7fe7bdfe:

    "Я заканчиваю разговор с папой, стараясь звучать уверенно."

translate russian angela_afterblow_dad_call_8522fcc2:

    "Я не хочу этого делать, но я не вижу, как можно избежать этого."

translate russian angela_afterblow_dad_call_866d2e29:

    mike.say "Привет, пап!"

translate russian angela_afterblow_dad_call_96377496:

    mike.say "Но, пап..."

translate russian angela_afterblow_dad_call_98a0be6a:

    "Dad" "Ха-ха, я знал!"

translate russian angela_afterblow_dad_call_99cf347b:

    "Я слышу, как отец снова вздыхает."

translate russian angela_afterblow_dad_call_6c928997:

    mike.say "Я... я был в ресторане на днях, отец."

translate russian angela_afterblow_dad_call_bd4939f7:

    "Dad" "Да, сынок..."

translate russian angela_afterblow_dad_call_bd8dd8ed:

    "Вот почему я звоню своему отцу после того, как видел маму и Брюса в ресторане."

translate russian angela_afterblow_dad_call_c052e392:

    "Но он имеет право знать, что происходит за его спиной."

translate russian angela_afterblow_dad_call_cf3a99fc:

    "Dad" "Она призналась, и я её простил."

translate russian angela_afterblow_dad_call_d0eb3d4b:

    "На мгновение я просто не могу осознать то, что он только что сказал."

translate russian angela_afterblow_dad_call_d2e81e3b:

    mike.say "Я просто волновался, вот и все."

translate russian angela_afterblow_dad_call_d55396fa:

    "Dad" "Твоя мама уже рассказала мне об этом, сынок."

translate russian angela_afterblow_dad_call_d75a572b:

    "Dad" "Слушай, сынок, это не так уж и серьёзно."

translate russian angela_afterblow_dad_call_ddf68483:

    "Что странно, потому что я ожидал, что он разозлится в любой момент."

translate russian angela_afterblow_dad_call_e745c8a4:

    "Dad" "Что ты хочешь мне сказать?"

translate russian angela_afterblow_dad_call_e84ffc6f:

    mike.say "Что?"

translate russian angela_afterblow_dad_call_e9e05252:

    "Но что-то всё равно продолжает тревожить меня."

translate russian angela_afterblow_dad_call_ea2583c2:

    "На самом деле, это тон, который я хорошо помню с тех пор, как был ребёнком!"

translate russian angela_afterblow_dad_call_ee60becc:

    "Dad" "Никто не идеален, но наши отношения сильнее этого, хорошо?"

translate russian angela_afterblow_dad_call_f03eca55:

    "Мой отец на мгновение замолкает."

translate russian angela_afterblow_dad_call_f1d8a63c:

    mike.say "Эм..."

translate russian angela_afterblow_dad_call_f7703fbc:

    "Dad" "Здравствуй, сынок!"

translate russian angela_afterblow_dad_call_fb9bf7d6:

    mike.say "Она была на свидании с отцом моего соседа!"

translate russian angela_bj_bruce_00c0a806:

    mike.say "Если один парень пойдёт в туалет для женщин, это будет подозрительно."

translate russian angela_bj_bruce_05e13b1a:

    "Она повернула голову в мою сторону, выглядя растерянной."

translate russian angela_bj_bruce_0686bb2b:

    "Но теперь мы оба больше заинтересованы в Брюсе и моей маме."

translate russian angela_bj_bruce_086fe9d5:

    "И, к счастью для нас, Брюс и моя мама сейчас очень отвлечены!"

translate russian angela_bj_bruce_0b356088:

    "Она уже наполовину встала со своего места, когда это сказала."

translate russian angela_bj_bruce_0ff02064:

    mike.say "Слушай, давай просто понаблюдаем за ними, посмотрим, что произойдёт."

translate russian angela_bj_bruce_13220f91:

    mike.say "Они могут там делать что угодно."

translate russian angela_bj_bruce_19b23bde:

    minami.say "Это мама — и она с каким-то парнем, который не папа!"

translate russian angela_bj_bruce_212ae386:

    bree.say "Ты...ты имеешь в виду...?"

translate russian angela_bj_bruce_212ae386_1:

    bree.say "Ты не имеешь в виду..."

translate russian angela_bj_bruce_2208b1d2:

    "Её глаза расширяются от удивления, когда я это говорю."

translate russian angela_bj_bruce_2208b1d2_1:

    "Её глаза расширяются от удивления, когда я это говорю."

translate russian angela_bj_bruce_22bc74dc:

    bree.say "Что она делает на свидании с моим отцом?!"

translate russian angela_bj_bruce_22bdbf18:

    "Когда мы внутри, я замечаю, что только одна кабинка занята."

translate russian angela_bj_bruce_257ed31b:

    "И она поднимает меню, чтобы закрыть лицо."

translate russian angela_bj_bruce_27f85bce:

    "Не стоит паниковать, похоже, она просто идёт в туалет."

translate russian angela_bj_bruce_29a54305:

    mike.say "Откуда я должен знать?"

translate russian angela_bj_bruce_2ba01c05:

    bree.say "«Я ужасно голодна, [hero.name]»."

translate russian angela_bj_bruce_2bb23d9b:

    "Я вижу этот столик и двух людей, которые за ним сидят."

translate russian angela_bj_bruce_30b26409:

    "И я тоже не могу не удивиться."

translate russian angela_bj_bruce_30ba9581:

    mike.say "Это же моя мама!"

translate russian angela_bj_bruce_33c44e7f:

    bree.say "Там — в углу."

translate russian angela_bj_bruce_346463c5:

    "Моя мама стоит перед ним на коленях."

translate russian angela_bj_bruce_347b9976:

    "Почти не задумываясь, я закрываю рот [bree.name] рукой."

translate russian angela_bj_bruce_35887351:

    "Но я протянул руку и положил её на её запястье."

translate russian angela_bj_bruce_393ca63c:

    "Но, может быть, есть совершенно безобидное объяснение."

translate russian angela_bj_bruce_3b56c5cc:

    minami.say "Что он делает на свидании с нашей мамой?!"

translate russian angela_bj_bruce_3e43cc45:

    "Я качаю головой, пытаясь понять, что я вижу."

translate russian angela_bj_bruce_400faa34:

    mike.say "Может быть, они просто старые друзья, и никто из нас об этом не знает."

translate russian angela_bj_bruce_42bbca92:

    minami.say "Хм!"

translate russian angela_bj_bruce_45fd148c:

    "Я поднимаю голову и вижу, что Брюс тоже встаёт со своего места."

translate russian angela_bj_bruce_47889e37:

    minami.say "Нам нужно за ними следить!"

translate russian angela_bj_bruce_481b4411:

    "И она прямо сейчас делает ему довольно интенсивный оральный секс!"

translate russian angela_bj_bruce_52c0775d:

    "Но когда он подходит к двери мужского туалета, он меняет направление."

translate russian angela_bj_bruce_52f2e92d:

    minami.say "Там, в углу."

translate russian angela_bj_bruce_549bb96e:

    "Как только они ушли, мы наклоняемся друг к другу над столом."

translate russian angela_bj_bruce_5a5f1352:

    bree.say "Хм!"

translate russian angela_bj_bruce_5c041074:

    "И как только он уходит, они наклоняются ближе друг к другу, держатся за руки и улыбаются друг другу."

translate russian angela_bj_bruce_5feee5e1:

    "Но ни один из нас не может удержаться от того, чтобы украдкой поглядывать в сторону моей мамы и Брюса."

translate russian angela_bj_bruce_63f1c8bf:

    bree.say "Нам нужно за ними следить!"

translate russian angela_bj_bruce_6400f0b5:

    "Мы заказываем еду и стараемся вести себя естественно."

translate russian angela_bj_bruce_64eed76f:

    "Они просят счёт и довольно быстро уходят."

translate russian angela_bj_bruce_650c6219:

    "Мы стараемся вернуться к нашей еде."

translate russian angela_bj_bruce_67c80c59:

    mike.say "Постой..."

translate russian angela_bj_bruce_68c4b6f4:

    bree.say "Ну же, [hero.name]."

translate russian angela_bj_bruce_694e0180:

    "Мы киваем друг другу, заключая сделку."

translate russian angela_bj_bruce_6be11f89:

    "Но я не могу не гадать, что именно мы собираемся узнать."

translate russian angela_bj_bruce_6e154b71:

    mike.say "Ладно, ладно..."

translate russian angela_bj_bruce_6ee95723:

    minami.say "Похоже, отцу [bree.name] тоже пора в туалет!"

translate russian angela_bj_bruce_6f050f83:

    "Затем он зажигает свечу и наливает им каждому бокал вина."

translate russian angela_bj_bruce_6f5a8f5e:

    "Практически одновременно с тем, как дверь закрывается за Брюсом, я встаю."

translate russian angela_bj_bruce_6f8316ce:

    "[bree.name] серьёзно нахмурилась и кивнула."

translate russian angela_bj_bruce_6ff60c93:

    "Я иду первой, стараясь проскользнуть внутрь как можно тише."

translate russian angela_bj_bruce_7122e9f9:

    minami.say "Мама никогда бы..."

translate russian angela_bj_bruce_7122e9f9_1:

    minami.say "Мама бы никогда..."

translate russian angela_bj_bruce_71551e81:

    bree.say "Как они вообще могли встретиться?"

translate russian angela_bj_bruce_7181587d:

    "Затем она снова спряталась за своим меню."

translate russian angela_bj_bruce_71d177a5:

    "[bree.name] встаёт с места и идёт за мной в дамскую комнату."

translate russian angela_bj_bruce_72517e2b:

    "Стараясь не издать ни звука, мы возвращаемся к нашему столику."

translate russian angela_bj_bruce_77a65b9e:

    mike.say "Конечно, я хочу пойти за ними!"

translate russian angela_bj_bruce_813f4f3e:

    mike.say "Значит, они ДЕЙСТВИТЕЛЬНО на свидании!"

translate russian angela_bj_bruce_8183d84c:

    bree.say "Кажется, моему папе тоже нужно в туалет!"

translate russian angela_bj_bruce_86a9cfa0:

    mike.say "Я имею в виду, это может быть деловая встреча."

translate russian angela_bj_bruce_8a6606bb:

    "Минами кивает и изо всех сил пытается выглядеть серьёзной."

translate russian angela_bj_bruce_8b644f5e:

    mike.say "Нам нужно разобраться в этом, да?"

translate russian angela_bj_bruce_8ecdcd2c:

    "[bree.name] садится и с энтузиазмом берет меню у официанта."

translate russian angela_bj_bruce_91866a6d:

    "Но я сразу вижу, что она всё ещё взволнована."

translate russian angela_bj_bruce_920e7962:

    mike.say "А?!"

translate russian angela_bj_bruce_9599a7a7:

    bree.say "Это мой папа!"

translate russian angela_bj_bruce_99cf2fcb:

    "Некоторое время нам удаётся следовать плану."

translate russian angela_bj_bruce_9bac4cb6:

    "Я вижу, как он незаметно для всех проникает в женский туалет!"

translate russian angela_bj_bruce_a4099f45:

    minami.say "Но зачем, [hero.name]?"

translate russian angela_bj_bruce_a450a7c3:

    "Почти не задумываясь, я закрываю рот Минами рукой."

translate russian angela_bj_bruce_a4bc1cf1:

    mike.say "Это же не так, что у мужского туалета очередь!"

translate russian angela_bj_bruce_a55fb44d:

    mike.say "Давай — чего ты ждёшь?"

translate russian angela_bj_bruce_a9867758:

    "Как будто отвечая на мой вопрос, официант подходит к их столику."

translate russian angela_bj_bruce_b2fd8892:

    "Мы вместе крадёмся к соседней кабинке и встаём возле унитаза."

translate russian angela_bj_bruce_b3ca36e3:

    "Минами радостно позволяет официанту отодвинуть её стул и берет меню."

translate russian angela_bj_bruce_b7353732:

    minami.say "О нет — это значит, что мама и папа разводятся?!"

translate russian angela_bj_bruce_b859efe2:

    "Похоже, у них пропал аппетит, или, может быть, они насытились."

translate russian angela_bj_bruce_be9eab97:

    mike.say "Ну, это же не так, что мужской туалет сломан!"

translate russian angela_bj_bruce_c060ede2:

    "Через некоторое время Брюс выходит из женской уборной и возвращается на своё место."

translate russian angela_bj_bruce_c2a80f99:

    mike.say "А если туда пойдут двое, это будет выглядеть так, будто мы устраиваем там оргию!"

translate russian angela_bj_bruce_c45435f8:

    mike.say "Это отец [bree.name]!"

translate russian angela_bj_bruce_c76bb041:

    bree.say "Мне кажется, я могу съесть лошадь!"

translate russian angela_bj_bruce_c8e08457:

    "Моя мама появляется через несколько минут, выглядя немного растрёпанной."

translate russian angela_bj_bruce_cc0cb61c:

    minami.say "Ох..."

translate russian angela_bj_bruce_cf2c994e:

    "Я знаю, что должен вести себя так же сдержанно, как она сейчас."

translate russian angela_bj_bruce_d092e13e:

    "Конечно, это выглядит довольно подозрительно с того места, где мы сидим."

translate russian angela_bj_bruce_d1e4d9cc:

    "Брюс стоит там, штаны опущены до щиколоток."

translate russian angela_bj_bruce_d310ebeb:

    "Минами встаёт с места и идёт за мной в дамскую комнату."

translate russian angela_bj_bruce_b326bed5:

    minami.say "Т...ты хочешь пойти за ними?!"

translate russian angela_bj_bruce_d66a0ec8:

    "Оттуда у нас открывается отличный вид на занятую кабинку."

translate russian angela_bj_bruce_d6796a40:

    "В результате она успевает лишь издать несколько приглушённых звуков испуга."

translate russian angela_bj_bruce_d8de3117:

    "Кажется, все идёт хорошо, нас проводят к нашему столику в ресторане."

translate russian angela_bj_bruce_df886bc4:

    mike.say "Что случилось?"

translate russian angela_bj_bruce_df961a4f:

    mike.say "Почему же он туда пошёл?!"

translate russian angela_bj_bruce_df961a4f_1:

    mike.say "Почему он вообще туда пошёл?!?"

translate russian angela_bj_bruce_e9f4a726:

    "Но потом я вижу, как её глаза расширяются от удивления."

translate russian angela_bj_bruce_ed1c03c0:

    "Но вы знаете, как это бывает — стоит мне услышать эти слова, моя голова поворачивается."

translate russian angela_bj_bruce_eee30080:

    "Ничего особенного не происходит, пока моя мама не встаёт со своего места и не уходит."

translate russian angela_bj_bruce_f62e86a5:

    mike.say "Мы не можем за ними следить."

translate russian angela_bj_bruce_f6a94b29:

    "И мы видим картину, которая навсегда останется в моей памяти."

translate russian angela_bj_bruce_f9b47dc1:

    bree.say "Согласна."

translate russian angela_bj_bruce_fc0aaa3b:

    "Все это время я молюсь, чтобы нас никто не видел."

translate russian angela_bj_bruce_fc801987:

    minami.say "Фу!"

translate russian angela_bj_bruce_fc801987_1:

    minami.say "Фу!"

translate russian angela_bj_bruce_fd481a97:

    bree.say "Но зачем, [hero.name]?"

translate russian angela_bj_bruce_c1aa49b3:

    mike.say "Мы...мы же не знаем, что они на свидании, верно?"

translate russian angela_bj_bruce_7e30b67a:

    bree.say "Т...ты хочешь пойти за ними?!"

translate russian anna_bree_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian anna_bree_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian anna_bree_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian anna_bree_propose_male_8fb73da4:

    mike.say "Я..."

translate russian anna_bree_propose_male_8fb73da4_1:

    mike.say "Я..."

translate russian anna_bree_propose_male_8fb73da4_2:

    mike.say "Я..."

translate russian anna_concert_naked_30e74fc5:

    mike.say "Эм..."

translate russian anna_concert_naked_6757cf6b:

    mike.say "Ну..."

translate russian anna_concert_naked_8fb73da4:

    mike.say "Я..."

translate russian anna_concert_naked_f1d8a63c:

    mike.say "Эм..."

translate russian anna_kleio_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian anna_kleio_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian anna_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian apologize_39807de4:

    active_girl.say "Ладно, но больше никогда так не делай."

translate russian apply_sunscreen_e2544685:

    "Я наношу солнцезащитный крем на [active_girl.name]."

translate russian arcade_competition_25b667a7:

    "Мне не хочется участвовать."

translate russian arcade_competition_5bcf2974:

    "Я проиграл."

translate russian arcade_competition_d69e06be:

    "Участие стоит 25{image=gui/icons/icon_money.png}."

translate russian arcade_competition_daa884aa:

    "Я победил! Приз составил [money]{image=gui/icons/icon_money.png}."

translate russian arcade_competition_f1b92c55:

    "У меня нет денег на участие."

translate russian arcade_competition_f3c0809c:

    "Здесь проходит турнир по видеоиграм."

translate russian ask_birthday_914b3cf4:

    active_girl.say "Мой день рождения — [active_girl.birthday[1]] [active_girl.birthday[0]]."

translate russian ask_birthday_9562be10:

    active_girl.say "Ты собираешься подарить мне подарок?"

translate russian ask_birthday_a1061e73:

    active_girl.say "Не думаю, что это тебя касается."

translate russian ask_bree_about_sam_08a9b882:

    "Я не могу поверить своим ушам."

translate russian ask_bruce_number_1632f4d2:

    bree.say "Ты уверен, что хочешь это сделать, [hero.name]?"

translate russian ask_bruce_number_188f8b53:

    "Но потом она пожимает плечами и качает головой."

translate russian ask_bruce_number_188f8b53_1:

    "Но потом она пожимает плечами и качает головой."

translate russian ask_bruce_number_1a2e7984:

    "Кажется, [bree.name] собирается отказать."

translate russian ask_bruce_number_1a2e7984_1:

    "Кажется, [bree.name] собирается отказать."

translate russian ask_bruce_number_24278a5b:

    bree.say "А?"

translate russian ask_bruce_number_25167fd4:

    bree.say "Вот, держи..."

translate russian ask_bruce_number_25167fd4_1:

    bree.say "Вот, держи..."

translate russian ask_bruce_number_33e520c2:

    "Я решил, что лучше сразу спросить."

translate russian ask_bruce_number_3ae736fa:

    bree.say "Я так не думаю, [hero.name]."

translate russian ask_bruce_number_4281d0d5:

    "[bree.name] хмурится на меня, приподнимая одну бровь."

translate russian ask_bruce_number_4281d0d5_1:

    "[bree.name] хмурится на меня, приподнимая одну бровь."

translate russian ask_bruce_number_4b485cdf:

    bree.say "Что случилось, [hero.name]?"

translate russian ask_bruce_number_53655b02:

    "Конечно, я могу позвонить своей маме и расспросить её о том, что я видел в ресторане на прошлой неделе."

translate russian ask_bruce_number_644e20bf:

    bree.say "Разве не мне следовало бы это сделать?"

translate russian ask_bruce_number_66c3ca4e:

    "Затем она качает головой."

translate russian ask_bruce_number_910f93bf:

    bree.say "Я не думала, что вы так хорошо ладите!"

translate russian ask_bruce_number_910f93bf_1:

    bree.say "Я не думала, что вы так хорошо ладите!"

translate russian ask_bruce_number_ae08b529:

    mike.say "Могу ли я узнать номер телефона твоего отца?"

translate russian ask_bruce_number_b92df2dc:

    "Поэтому я думаю, лучше просто прямо спросить."

translate russian ask_bruce_number_bc733938:

    "[bree.name] немного подумала об этом."

translate russian ask_bruce_number_c2291acd:

    bree.say "Ты хочешь позвонить ему из-за того, что мы видели?"

translate russian ask_bruce_number_c289f097:

    bree.say "Зачем тебе это?"

translate russian ask_bruce_number_d5ad4dea:

    bree.say "Что бы ты ни говорил, [hero.name]."

translate russian ask_bruce_number_d5ad4dea_1:

    bree.say "Что бы ты ни говорил, [hero.name]."

translate russian ask_bruce_number_dc695aec:

    "Она выглядит не очень убеждённой."

translate russian ask_bruce_number_e6d12cf1:

    "Но, может быть, человеку, которому мне действительно стоит позвонить по этому поводу, — это сам отец [bree.name]?"

translate russian ask_bruce_number_e8df7633:

    mike.say "Это все просто мужские штучки, притворяемся, что не любим друг друга!"

translate russian ask_bruce_number_e8df7633_1:

    mike.say "Это все просто мужские штучки, когда притворяются, что друг друга не любят!"

translate russian ask_bruce_number_eb8514ef:

    "Единственная проблема в том, что у меня, очевидно, нет номера телефона Брюса."

translate russian ask_bruce_number_f31548b3:

    "В конце концов, возможно, мне стоит услышать обе стороны истории, прежде чем я решу, кто виноват."

translate russian ask_bruce_number_fd120d22:

    "И единственный человек, у которого я могу его попросить — это [bree.name]."

translate russian ask_for_a_job_day_e739f25e:

    "Shop owner" "Конечно, работа твоя."

translate russian ask_for_a_job_e739f25e:

    "Shop owner" "Конечно, работа твоя."

translate russian ask_for_a_job_night_e739f25e:

    "Shop owner" "Конечно, работа твоя."

translate russian ask_minami_about_lexi_1c0d45e8:

    mike.say "Ну..."

translate russian ask_minami_about_lexi_52c65242:

    mike.say "Что?!"

translate russian ask_number_402c069b:

    active_girl.say "Не думаю."

translate russian ask_number_b568c047:

    active_girl.say "Конечно."

translate russian ask_out_dialogues_1_male_f8354afa:

    mike.say "Конечно."

translate russian ask_sam_about_lexi_1c0d45e8:

    mike.say "Ну..."

translate russian ask_sasha_about_lexi_1c0d45e8:

    mike.say "Ну..."

translate russian ask_sasha_about_sam_4dda1c6b:

    mike.say "Что..."

translate russian attend_mass_d08a0551:

    "Я посещаю богослужение."

translate russian audrey_cassidy_palla_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian audrey_cassidy_palla_propose_male_be946dca:

    mike.say "Эм... да..."

translate russian audrey_cassidy_palla_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian audrey_cassidy_palla_propose_male_30e74fc5_1:

    mike.say "Эм..."

translate russian audrey_cassidy_palla_propose_male_30e74fc5_2:

    mike.say "Эм..."

translate russian audrey_cassidy_palla_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian audrey_cassidy_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian audrey_cassidy_propose_male_3f8382ca:

    mike.say "Ого..."

translate russian audrey_lavish_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian audrey_lavish_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian audrey_lavish_propose_male_1c0d45e8:

    mike.say "Ну..."

translate russian audrey_lavish_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian audrey_lavish_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian audrey_lavish_shiori_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian audrey_lavish_shiori_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian audrey_lavish_shiori_propose_male_1c0d45e8:

    mike.say "Ну..."

translate russian audrey_lavish_shiori_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian audrey_lavish_shiori_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian audrey_palla_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian audrey_palla_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian audrey_palla_propose_male_86d07102:

    mike.say "А..."

translate russian audrey_sasha_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian audrey_sasha_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian audrey_sasha_male_ending_da0db528:

    "Priest" "Может, начнём?"

translate russian audrey_sasha_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian audrey_sasha_propose_male_78820f82:

    mike.say "Фух..."

translate russian audrey_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian audrey_sasha_propose_male_8fb73da4:

    mike.say "Я..."

translate russian audrey_shiori_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian audrey_shiori_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian audrey_shiori_propose_male_1c0d45e8:

    mike.say "Ну..."

translate russian audrey_shiori_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian audrey_shiori_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian ayesha_emma_event_01_52c65242:

    mike.say "Что?!"

translate russian ayesha_emma_event_01_e1d914e5:

    mike.say "Хм..."

translate russian ayesha_hanna_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian ayesha_hanna_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian ayesha_hanna_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian ayesha_hanna_propose_male_86d07102:

    mike.say "А..."

translate russian ayesha_hanna_propose_male_f2c5197f:

    "Но затем качает головой."

translate russian ayesha_hanna_propose_male_f2c5197f_1:

    "Но затем качает головой."

translate russian ayesha_hanna_showdown_1ccab2e1:

    mike.say "Хм..."

translate russian ayesha_hanna_showdown_30e74fc5:

    mike.say "Эм..."

translate russian ayesha_hanna_showdown_4dda1c6b:

    mike.say "Что..."

translate russian ayesha_hanna_showdown_6e154b71:

    mike.say "Ладно, ладно..."

translate russian ayesha_hanna_showdown_881a82dd:

    "Я открываю рот, чтобы возразить."

translate russian ayesha_hanna_showdown_89d2bf47:

    mike.say "Нужно..."

translate russian ayesha_kylie_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian ayesha_kylie_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian bathroom_broken_c0a68a21:

    "Это ванная на первом этаже, но она уже целую вечность не работает..."

translate russian bathroom_broken_db29d36f:

    "Мне нужно 5000{image=gui/icons/icon_money.png}, чтобы её починить."

translate russian battle_of_the_bands_lose_30e74fc5:

    mike.say "Эм..."

translate russian battle_of_the_bands_round_one_52c65242:

    mike.say "Что?!"

translate russian battle_of_the_bands_win_nightclub_ec4150dc:

    mike.say "Какого..."

translate russian battle_of_the_bands_win_restaurant_3e00ed72:

    sasha.say "Кхм..."

translate russian beach_graduation_05febc09:

    "Я ведь плачу ему за это дерьмо, значит, он должен быть со мной помягче, верно?"

translate russian beach_graduation_0fa5f3c0:

    "Когда я прихожу на пляж и начинаю искать Мастера, голова уже полна догадок о том, какое унизительное задание он приготовил сегодня."

translate russian beach_graduation_132f639a:

    master.say "Никакие изощрённые боевые искусства не помогут против хорошего, сильного удара по яйцам."

translate russian beach_graduation_1736dfa3:

    mike.say "Да, Мастер. Спасибо."

translate russian beach_graduation_1810b3a4:

    "Мне остаётся лишь лежать, схватившись за пах, и стараться не блевануть."

translate russian beach_graduation_2053b5c5:

    master.say "Прощай и удачи, мой ученик!"

translate russian beach_graduation_28f4548a:

    "Что позволяет ему аккуратно врезать мне ногой прямо в пах."

translate russian beach_graduation_2a1a8c79:

    "О боже, да он и правда выглядит серьёзным!"

translate russian beach_graduation_bb082ab2:

    mike.say "Ты... ты только что пнул меня по яйцам... что это вообще за боевое искусство?!"

translate russian beach_graduation_418a95b5:

    "Облизнув губы и стиснув зубы, я пытаюсь повторить его стойку."

translate russian beach_graduation_4e2a3c32:

    master.say "Это последний урок, которому я тебя научу, мой мальчик."

translate russian beach_graduation_541eeafc:

    "Мастер издаёт какой-то боевой вопль и бросается на меня с той неестественной скоростью и ловкостью, которую иногда демонстрирует."

translate russian beach_graduation_57035e34:

    mike.say "Начнём, Мастер?"

translate russian beach_graduation_5c61255d:

    "С этими словами он уходит, посмеиваясь надо мной во всех возможных смыслах."

translate russian beach_graduation_70ca4401:

    master.say "Так что я досрочно выпускаю тебя. Думаю, я научил тебя всему необходимому... наверное."

translate russian beach_graduation_72302a7e:

    "Гораздо сильнее меня озадачивает то, что он просто стоит на месте, не подзывая меня и не предлагая очередное орудие ежедневной пытки."

translate russian beach_graduation_755798f5:

    "Он коротко кивает."

translate russian beach_graduation_76250943:

    "Мне остаётся лишь пожать плечами и принять его слова."

translate russian beach_graduation_77f276a4:

    "Но когда я нахожу его стоящим на песке с руками за спиной и широкой улыбкой при виде меня, возникает ощущение, что тут что-то не так."

translate russian beach_graduation_7c0b3a33:

    "Мастер несколько мгновений кивает, а затем внезапно принимает стойку, подозрительно похожую на те, что используют герои фильмов о боевых искусствах."

translate russian beach_graduation_7fcb4648:

    master.say "Вообще-то я мог бы научить тебя ещё многому, но возникло одно дело, которым мне нужно заняться."

translate russian beach_graduation_82dc2e59:

    "Ну да, ведь эти сто долларов буквально прожигают дыру в моём кармане!"

translate russian beach_graduation_b72c0985:

    master.say "Я научил тебя всему, чему мог... точнее, всему, чему мне не лень было тебя учить."

translate russian beach_graduation_9973accc:

    "Дело не в самой улыбке. Он наверняка доволен собой, ведь уже положил в карман пару сотен моих долларов за свои сомнительные уроки."

translate russian beach_graduation_9a85d7bc:

    "Мастер посмеивается и одобрительно кивает."

translate russian beach_graduation_111330f8:

    mike.say "Эм, Мастер... что вы делаете?"

translate russian beach_graduation_a4dae91c:

    "Хотя я рад, что он больше не будет опустошать мой банковский счёт, окончательность его слов всё равно застаёт меня врасплох."

translate russian beach_graduation_add014ff:

    mike.say "Я готов к сегодняшнему уроку!"

translate russian beach_graduation_b1b7eceb:

    "Мастер улыбается, глядя сверху, пока я корчусь от боли."

translate russian beach_graduation_b5b7dbae:

    "Честно говоря, мне не кажется, что я многому научился на его уроках, и уж точно недостаточно, чтобы они так внезапно закончились."

translate russian beach_graduation_b7fb8489:

    master.say "Теперь твоя подготовка завершена, ученик. Пришло время показать, чему ты научился!"

translate russian beach_graduation_c03c629c:

    mike.say "Правда, Мастер?"

translate russian beach_graduation_c4d9cd71:

    "Я мгновенно валюсь на песок и сворачиваюсь клубком, изо всех сил стараясь не блевануть."

translate russian beach_graduation_cfd2d6ae:

    master.say "Когда я сказал, что уроков больше не будет, я солгал."

translate russian beach_graduation_d87ad941:

    master.say "Меня радует твой энтузиазм, мой мальчик."

translate russian beach_graduation_dc60b9dc:

    "Я едва успеваю заметить его кулак, летящий слева, и уклониться..."

translate russian beach_graduation_e06b438c:

    "Он серьёзно?"

translate russian beach_graduation_f456529d:

    master.say "Но сегодня урока не будет. Как и завтра, и послезавтра."

translate russian bear_attack_male_087df9a0:

    "Он несётся прямо на меня с широко раскрытой пастью."

translate russian bear_attack_male_10a1ae12:

    "Страх не парализует меня, но я впадаю в панику, и ноги превращаются в ватные макаронины."

translate russian bear_attack_male_1797dd99:

    "Надо мной нависает силуэт медведя, а его челюсти смыкаются быстрее, чем я мог представить для существа такого размера."

translate russian bear_attack_male_4e2ace22:

    "Я изо всех сил пытаюсь бежать быстрее, но всё происходит слишком стремительно."

translate russian bear_attack_male_666d5639:

    "Боли нет, но лишь потому, что у меня не остаётся времени осознать происходящее."

translate russian bear_attack_male_af510cfe:

    "Всё вокруг смешивается: зелёная трава и красный цвет, исходящий уже не из разинутой пасти медведя."

translate russian bear_attack_male_bee05298:

    "А затем остаётся лишь тьма..."

translate russian bear_attack_male_c31f5069:

    "Из-за двух острых как бритва когтей, летящих к моему лицу, на меня смотрят сияющие красные глаза."

translate russian bear_attack_male_f0692734:

    "Это медведь. Огромный, уродливый и словно выползший из кошмарного фильма."

translate russian bear_attack_male_f4cfc9ec:

    "Я оглядываюсь через плечо, уже готовый сдаться и сделать вид, будто ничего не понимаю."

translate russian bear_attack_male_fbb6cbe6:

    "И тут вижу нечто, из-за чего мгновенно загрязняю чистый лесной воздух."

translate russian bear_chan_pet_02116fd6:

    "Более того, с каждой секундой он движется всё быстрее."

translate russian bear_chan_pet_07d06fe3:

    "Это может быть только медведь!"

translate russian bear_chan_pet_09bf8005:

    "Теперь я хочу лишь добраться до безопасной машины."

translate russian bear_chan_pet_0c3bb65c:

    "Это немного странно, ведь я думал, что он уже давно учуял мой запах."

translate russian bear_chan_pet_0df8fe92:

    "Я уже почти наложил в штаны от страха!"

translate russian bear_chan_pet_8ce9081a:

    mike.say "К-кто здесь?"

translate russian bear_chan_pet_1182a2e6:

    "И я уверен, что только что уничтожил последнюю возможность выбраться отсюда живым."

translate russian bear_chan_pet_118f130a:

    "Какого чёрта здесь нет сигнала на телефоне?"

translate russian bear_chan_pet_11d734c1:

    "За мгновение до того, как развернуться и побежать, я понимаю, почему мои угрозы совершенно не подействовали."

translate russian bear_chan_pet_159890d7:

    "И как можно осторожнее глажу его по макушке."

translate russian bear_chan_pet_1b4e31f9:

    "Почему бы не съездить в лес и хорошенько там прогуляться?"

translate russian bear_chan_pet_1ed9557c:

    mike.say "Хотите, чтобы вас здесь пристрелили?"

translate russian bear_chan_pet_22dd5be2:

    "А затем ещё больше трескающихся веток, гораздо больше."

translate russian bear_chan_pet_268fec84:

    "Но теперь та же тишина и пустота начинают действовать мне на нервы."

translate russian bear_chan_pet_929cec4a:

    mike.say "Х-хороший мишка..."

translate russian bear_chan_pet_2a9f1604:

    "Остаётся надеяться, что тот, кто там прячется, хотя бы задумается над такой возможностью."

translate russian bear_chan_pet_2c48da1c:

    "Он безучастно смотрит на меня, словно увидел впервые."

translate russian bear_chan_pet_3061c8ad:

    "Во всяком случае, пока он немного не отступает и снова не начинает пристально на меня смотреть."

translate russian bear_chan_pet_31993d6d:

    "Но сегодня был один из тех дней, понимаете?"

translate russian bear_chan_pet_377f8a96:

    "А убедившись, что он ушёл, со всех ног бросаюсь обратно."

translate russian bear_chan_pet_3998d5a1:

    mike.say "Молодец..."

translate russian bear_chan_pet_3cff9194:

    "Вот и всё, я умру здесь, в лесу."

translate russian bear_chan_pet_3fdf6a1f:

    "Медведь останавливается примерно в дюжине футов от меня."

translate russian bear_chan_pet_40d96294:

    "Да кого я вообще пытаюсь обмануть?"

translate russian bear_chan_pet_43eabe53:

    "Хотя, похоже, нет: я слышу, как он подходит всё ближе."

translate russian bear_chan_pet_49fd6e97:

    "Из кустов доносится лишь новое шуршание."

translate russian bear_chan_pet_4a882b55:

    "Не придумав ничего лучше, я протягиваю руку."

translate russian bear_chan_pet_51535980:

    "Ах да, и ещё сменить штаны..."

translate russian bear_chan_pet_53d28b22:

    "Все обычные назойливые туристы и собачники уже давно разошлись по домам."

translate russian bear_chan_pet_5a09e118:

    "Если мне не хватило ума взять фонарик, неужели я додумался бы прихватить настоящий пистолет?"

translate russian bear_chan_pet_5a0c24f2:

    "Обычно мне и в голову не пришло бы идти в лес после наступления темноты."

translate russian bear_chan_pet_65b24f11:

    "И всё потому, что мне захотелось прогуляться вечером."

translate russian bear_chan_pet_67bc637d:

    "Он недалеко от моего дома, а в такое время там наверняка тихо."

translate russian bear_chan_pet_69ada0e9:

    "Теперь медведь словно чего-то ждёт."

translate russian bear_chan_pet_6b093aa0:

    "А значит, я могу спокойно наслаждаться этим местом в полном одиночестве."

translate russian bear_chan_pet_6bb9ebdd:

    "После этого смогу уехать домой и никогда больше сюда не возвращаться."

translate russian bear_chan_pet_700f54ac:

    mike.say "Вот так..."

translate russian bear_chan_pet_798d3250:

    mike.say "Как я и говорил, хороший мишка..."

translate russian bear_chan_pet_80d1a035:

    "Сначала кажется, будто ко мне приближается кусок самой темноты."

translate russian bear_chan_pet_9be17d00:

    mike.say "Спасибо, что не съел меня!"

translate russian bear_chan_pet_9ed67d93:

    "Он обнюхивает меня, словно собака в поисках лакомства."

translate russian bear_chan_pet_a223994a:

    "Какого чёрта я не взял с собой фонарик?"

translate russian bear_chan_pet_a6671ce7:

    "Услышав мой голос, медведь начинает приближаться."

translate russian bear_chan_pet_af9b4a71:

    "Я крепко зажмуриваюсь и напрягаю каждую мышцу, готовясь умереть."

translate russian bear_chan_pet_c18e0acf:

    "Я продолжаю стоять неподвижно, пока он не скрывается среди деревьев."

translate russian bear_chan_pet_c4418012:

    "Вот так я и оказался на безлюдной лесной тропе уже после захода солнца."

translate russian bear_chan_pet_c49c0028:

    "Но затем он приобретает очертания огромного, массивного зверя."

translate russian bear_chan_pet_c8241446:

    "Мне действительно кажется, что на много миль вокруг нет ни одного человека."

translate russian bear_chan_pet_cba43e75:

    "На мой вопрос никто не отвечает."

translate russian bear_chan_pet_ce91e4ea:

    "Приоткрыв один глаз, я вижу, как медведь тычется в меня мордой."

translate russian bear_chan_pet_cf2eaf59:

    "Но достаточно хруста одной ветки, чтобы моё настроение полностью изменилось."

translate russian bear_chan_pet_d0ac7154:

    "Когда просто необходимо как-нибудь расслабиться."

translate russian bear_chan_pet_d237dbd3:

    "И в тот же миг вся атмосфера леса словно преображается."

translate russian bear_chan_pet_dc19fb49:

    "Поначалу мне даже хочется похвалить себя за такую замечательную идею."

translate russian bear_chan_pet_ddf2e3b0:

    "И какого чёрта я вообще сюда припёрся?!"

translate russian bear_chan_pet_5f9b4d9d:

    mike.say "Я... я вооружён..."

translate russian bear_chan_pet_e04af2d4:

    "Но тут слышу фырканье и тяжёлое сопение."

translate russian bear_chan_pet_e0655884:

    "Разумеется, никакого оружия у меня нет."

translate russian bear_chan_pet_e3c03080:

    "Я поворачиваю голову в сторону звука."

translate russian bear_chan_pet_e748d11b:

    "В передачах о природе постоянно рассказывают, насколько остры чувства у животных."

translate russian bear_chan_pet_e7523ea5:

    "В лесу так тихо и умиротворённо."

translate russian bear_chan_pet_ea3863ce:

    "И пока я размышлял, чем заняться, мне внезапно пришла эта мысль."

translate russian bear_chan_pet_edb46f45:

    "Но этот зверь смотрит на меня так, будто я застал его за тем, как он справляет нужду!"

translate russian bear_chan_pet_edbda7c4:

    "Остановившись на тропе, я всматриваюсь в деревья и подлесок."

translate russian bear_chan_pet_eed5b9ec:

    "Одновременно к моему лицу прикасается что-то холодное и мокрое."

translate russian bear_chan_pet_f1d8a63c:

    mike.say "Эм..."

translate russian bear_chan_pet_f2c9b996:

    "Прежде неподвижность вокруг дарила мне приятное чувство уединения."

translate russian bear_chan_pet_f4350b24:

    "Медведь снова фыркает, а затем разворачивается."

translate russian bear_chan_pet_f956fde0:

    "И что, по его мнению, я должен сделать?"

translate russian bear_chan_pet_fb51065a:

    "Теперь я открываю оба глаза, но продолжаю стоять неподвижно и позволяю ему делать что угодно."

translate russian bear_shark_ending_061b5703:

    "Я оседлал самого страшного высшего хищника на планете."

translate russian bear_shark_ending_0834bbc2:

    "И у меня вдруг появилась уверенность, чтобы с ними разговаривать."

translate russian bear_shark_ending_09063636:

    "После этого всё лишь продолжало набирать обороты."

translate russian bear_shark_ending_09ff8559:

    mike.say "Знаешь, это чистая правда, подруга!"

translate russian bear_shark_ending_10bb7749:

    "Она из тех, кто одним своим присутствием всегда склоняет чашу весов в твою пользу."

translate russian bear_shark_ending_238416e1:

    "Но именно в этот момент я чувствую, как меня обхватывает пара сильных рук."

translate russian bear_shark_ending_247f60e7:

    "Настолько, что я всерьёз рискую потерять хватку и свалиться с акулы."

translate russian bear_shark_ending_24ab1613:

    "Раньше мне казалось, что моя жизнь совершенно серая и скучная, будто со мной никогда не происходит ничего интересного."

translate russian bear_shark_ending_297018a3:

    "Bear Chan" "АААРРРГХ!"

translate russian bear_shark_ending_311ffe66:

    "Что бы ни ждало нас за горизонтом, уверен, там будет не менее безумно."

translate russian bear_shark_ending_31ccb076:

    "И когда я говорю «сильных», я не преувеличиваю. Они безумно сильные!"

translate russian bear_shark_ending_334494f3:

    "И мчусь на этой чёртовой твари к горизонту, прямо в закат."

translate russian bear_shark_ending_3b723f0f:

    mike.say "Не знаю, что бы я без тебя делал."

translate russian bear_shark_ending_402e1561:

    "Иногда я даже набирался смелости пригласить её на свидание."

translate russian bear_shark_ending_45b96788:

    "До второй базы я уже добрался."

translate russian bear_shark_ending_4efd3d10:

    "И я знаю, что всё, чему научился по пути, подготовило меня к любому испытанию."

translate russian bear_shark_ending_4f3b402d:

    mike.say "Я только что чуть не свалился!"

translate russian bear_shark_ending_58399aa4:

    "К тому же покрыты шерстью и заканчиваются лапами с когтями больше моей головы."

translate russian bear_shark_ending_5a4578e6:

    "Как только её огромная лапа шлёпает по моей ладони, я начинаю кивать."

translate russian bear_shark_ending_5c967ca9:

    "И не успевал опомниться, как уже заводил разговор и шутил с ней."

translate russian bear_shark_ending_62d30ae9:

    "Но потом всё вдруг начало меняться."

translate russian bear_shark_ending_6664eda0:

    "Моя жизнь становилась всё безумнее и интереснее."

translate russian bear_shark_ending_6fab7153:

    "Я невольно киваю, когда Медведица-тян даёт понять, что именно думает."

translate russian bear_shark_ending_70e61bb7:

    "Наверное, именно поэтому я сейчас сижу верхом на спине взрослой акулы."

translate russian bear_shark_ending_766bba21:

    "А пока я просто откинусь назад."

translate russian bear_shark_ending_78820f82:

    mike.say "Фух..."

translate russian bear_shark_ending_79370ad1:

    "Работа была скучной, друзья были сборищем законченных задротов, а личная жизнь умерла, не успев начаться."

translate russian bear_shark_ending_7c86fb79:

    "И буду смотреть, как солнце садится за далёкий горизонт."

translate russian bear_shark_ending_8905528b:

    "В такие моменты мне обычно хочется ущипнуть себя."

translate russian bear_shark_ending_897541cd:

    "Но в этом и есть одно из преимуществ компании Медведицы-тян."

translate russian bear_shark_ending_8acda997:

    mike.say "Как всегда."

translate russian bear_shark_ending_90facb1c:

    "Bear Chan" "УУУРРРГХ!"

translate russian bear_shark_ending_964d8a66:

    "Понятия не имею, куда направляется эта чёртова акула."

translate russian bear_shark_ending_98517e4f:

    mike.say "Спасибо, Медведица-тян..."

translate russian bear_shark_ending_9a9f7a98:

    "И какого чёрта мне вообще переживать из-за такой мелочи?"

translate russian bear_shark_ending_a3633153:

    "Кажется, это началось примерно тогда, когда Сэм и Райан съезжали."

translate russian bear_shark_ending_a3bd4093:

    "Чёрт, бывало даже, что девушка соглашалась!"

translate russian bear_shark_ending_ab18cd9c:

    "И, если уж на то пошло, как мы вообще собираемся с неё слезать."

translate russian bear_shark_ending_b1c48c69:

    "Пока что это была самая безумная поездка, какую только можно представить, и я отлично провёл время."

translate russian bear_shark_ending_b5f05b0a:

    "Моя жизнь становилась безумнее настолько постепенно, что порой я этого даже не замечаю."

translate russian bear_shark_ending_b68ec0fa:

    "Я уже расслабляюсь и откидываюсь на своего товарища по поездке на акуле."

translate russian bear_shark_ending_b76cb0d0:

    "И когда такое случается, мне хочется остановиться и осмыслить происходящее."

translate russian bear_shark_ending_bb5a8324:

    "И, как всегда, я очень ценю, что она совершенно ничего не скрывает."

translate russian bear_shark_ending_c0bb44f8:

    "А когда [bree.name] и Саша окончательно заселились, перемены уже точно были в самом разгаре."

translate russian bear_shark_ending_c6d8b31b:

    "Просто чтобы убедиться, что я не сплю и всё это не сон."

translate russian bear_shark_ending_ca1bf213:

    "Я постоянно знакомился с новыми людьми, причём чертовски привлекательными!"

translate russian bear_shark_ending_cab92652:

    "Например, я замечал новую девушку на работе или в одном из местных магазинов."

translate russian bear_shark_ending_d2c12baf:

    "Bear Chan" "РУУУРРРГХ!"

translate russian bear_shark_ending_d931dd1e:

    "Но ощущение было такое, словно какая-то внешняя сила внезапно начала вмешиваться в мою жизнь."

translate russian bear_shark_ending_df503850:

    "Значит, впереди как минимум ещё две, верно?"

translate russian bear_shark_ending_e1834ff5:

    "Поэтому я поднимаю руку и запрокидываю ладонь назад через плечо."

translate russian bear_shark_ending_eb7974f0:

    "Расслаблюсь в компании своей верной косолапой подруги."

translate russian bear_shark_ending_ed69c807:

    mike.say "Мы с тобой против всего мира."

translate russian bear_shark_ending_f0c2920f:

    "Я знаю, что она без труда удержит мой вес."

translate russian bear_shark_ending_f3d899eb:

    "Я не знаю, как это объяснить, не прозвучав при этом сумасшедшим."

translate russian bear_shark_ending_f8d44501:

    "Руками я крепко держусь за плавник посреди её спины."

translate russian bible_study_430c530b:

    "Я изучаю Библию в церкви..."

translate russian bird_attack_male_167e154f:

    mike.say "Что я тебе вообще сделал?!"

translate russian bird_attack_male_2a29418a:

    "Но перед этим обнаруживаю, что она ещё и успела нагадить мне на голову!"

translate russian bird_attack_male_34384545:

    "Но это всё же лучше, чем если бы то же самое досталось моему лицу."

translate russian bird_attack_male_3b401c39:

    "Я отчаянно размахиваю руками, пытаясь отбиться от нападающей."

translate russian bird_attack_male_6c8c441d:

    "А может, она заметила добычу попроще, которая имела неосторожность есть мороженое."

translate russian bird_attack_male_73131dbd:

    mike.say "Отвали, злобная пернатая тварь!"

translate russian bird_attack_male_753bf396:

    "И в награду она царапает и клюёт мои пальцы."

translate russian bird_attack_male_8027a658:

    "Чайка снова издаёт мерзкий вопль и внезапно улетает."

translate russian bird_attack_male_825a4bb4:

    "Я просто прогуливаюсь по пляжу, никого не трогаю, когда это случается."

translate russian bird_attack_male_9569d98d:

    "А потом понимаю, что на меня напала чёртова чайка!"

translate russian bird_attack_male_977e1695:

    "Должно быть, защищаясь, я всё-таки нанёс ей хотя бы один серьёзный удар."

translate russian bird_attack_male_993b9b95:

    "Как бы там ни было, я спешу уйти, пока она не решила вернуться."

translate russian bird_attack_male_a6705d7e:

    "Сначала я слышу лишь хлопанье крыльев и отвратительное карканье."

translate russian bird_attack_male_d5979dca:

    mike.say "А-а-а!"

translate russian bird_attack_male_d7c529ae:

    "На меня с ясного голубого неба пикирует какое-то существо."

translate russian bitchy_harem_foursome_437a01ea:

    mike.say "Ох, чёрт..."

translate russian bitchy_harem_foursome_437a01ea_1:

    mike.say "Ох, чёрт..."

translate russian bitchy_harem_foursome_appointment_intro_200eb25b:

    mike.say "Эй!"

translate russian bitchy_harem_foursome_ask_cassidy_1c0d45e8:

    mike.say "Ну..."

translate russian bitchy_harem_foursome_ask_cassidy_6757cf6b:

    mike.say "Ну..."

translate russian bitchy_harem_foursome_nightclub_intro_64949c1d:

    mike.say "Эм, да..."

translate russian bitchy_harem_foursome_request_700f54ac:

    mike.say "Вот так..."

translate russian bitchy_harem_foursome_request_b199b4a5:

    mike.say "Нет..."

translate russian bitchy_harem_foursome_request_f1d8a63c:

    mike.say "Эм..."

translate russian bj3_porn_03e902cf:

    "Обе наклоняются надо мной через диван, строя мне томные глазки."

translate russian bj3_porn_056650a5:

    "Девушки улыбаются мне снизу вверх, томно хлопая полуприкрытыми глазами."

translate russian bj3_porn_22b0f3f2:

    "Они снова облизывают мой член, проходясь по головке и самому кончику."

translate russian bj3_porn_259cadf0:

    "Я больше не могу сдерживаться и со стоном кончаю, выплёскиваясь на них."

translate russian bj3_porn_28f4b064:

    "Обе мои соседки разделись и смотрят на меня сверху вниз с улыбками, полными похоти и вполне ясных намерений."

translate russian bj3_porn_31ae29e6:

    bree_sasha "Эй, [hero.name]."

translate russian bj3_porn_550fb010:

    bree.say "Расслабься, но не слишком!"

translate russian bj3_porn_5a4581b8:

    "Когда они забираются на диван, Саша слева от меня, а [bree.name] справа, их тихий шёпот нежно касается моих ушей."

translate russian bj3_porn_72b19974:

    "Она протягивает палец [bree.name], а та обхватывает губами мой член и довольно стонет, наслаждаясь вкусом."

translate russian bj3_porn_78678f63:

    "Вместе они обхватывают мой член пальцами и высовывают языки, проводя ими вдоль всей длины."

translate russian bj3_porn_846e0342:

    "Когда я снова смотрю на них, [bree.name] и Саша уже стоят по обе стороны дивана."

translate russian bj3_porn_8f602fc3:

    mike.say "И?"

translate russian bj3_porn_9c55c374:

    mike.say "О... ого..."

translate russian bj3_porn_9cfa9c30:

    "Их языки соприкасаются, и обе смотрят на меня снизу вверх, обмениваясь смешком, прежде чем обхватить губами головку."

translate russian bj3_porn_a7d46405:

    bree.say "Перейдём к делу?"

translate russian bj3_porn_aa492e5e:

    "Они кивают друг другу."

translate russian bj3_porn_aca0951c:

    "Я думаю об этом, пока возбуждение от их действий волнами проходит по всему телу."

translate russian bj3_porn_af107b7a:

    "Саша проводит пальцем по лицу, собирая каплю моей спермы."

translate russian bj3_porn_b2745158:

    bree.say "Полностью согласна."

translate russian bj3_porn_be52683a:

    "Возбуждение охватывает всех..."

translate russian bj3_porn_c436957b:

    "Что я сделал, чтобы заслужить лучших соседок в мире?"

translate russian bj3_porn_c4a44cd8:

    "Саша цепляет пальцами бретельки лифчика и спускает их с плеч."

translate russian bj3_porn_c5b28849:

    sasha.say "Просто смотреть скучно."

translate russian bj3_porn_c9b38abb:

    sasha.say "Надеюсь, тебе нравится вид."

translate russian bj3_porn_ca622ff0:

    "Я ненадолго задумываюсь."

translate russian bj3_porn_dcc1e2e0:

    "Две лучшие соседки в мире целуются, зажав между собой мой член; их языки танцуют по моей коже, а руки синхронно дрочат мне."

translate russian bj3_porn_e1152ec2:

    bree.say "Ну что же!"

translate russian bj3_porn_e44a4af2:

    "Мы смотрим порно..."

translate russian bj3_porn_e53f5eb8:

    "Сперма брызгает им на лица, щедро покрывая их."

translate russian bj3_porn_e872aeb6:

    sasha.say "Давайте немного развлечёмся..."

translate russian bj3_porn_ea3b8162:

    "Я обнимаю их обеих и провожу пальцами по их гладкой коже."

translate russian bj3_porn_ea91a808:

    "Вскоре они прижимаются ко мне своими тёплыми телами, устраиваясь между моих разведённых ног."

translate russian bj3_porn_ec2b08ef:

    "Говорит [bree.name], стягивая с себя трусики."

translate russian bj3_porn_ee543538:

    sasha.say "Наслаждайся этим видом..."

translate russian bj3_porn_f8f2c254:

    "Она игриво отбрасывает их ногой."

translate russian bj_birthday_03e902cf:

    "Обе наклоняются надо мной через диван, строя мне томные глазки."

translate russian bj_birthday_056650a5:

    "Девушки улыбаются мне снизу вверх, томно хлопая полуприкрытыми глазами."

translate russian bj_birthday_22b0f3f2:

    "Они снова облизывают мой член, проходясь по головке и самому кончику."

translate russian bj_birthday_259cadf0:

    "Я больше не могу сдерживаться и со стоном кончаю, выплёскиваясь на них."

translate russian bj_birthday_846e0342:

    "Когда я снова смотрю на них, [bree.name] и Саша уже стоят по обе стороны дивана."

translate russian bj_birthday_9c55c374:

    mike.say "О... ого..."

translate russian bj_birthday_9cfa9c30:

    "Их языки соприкасаются, и обе смотрят на меня снизу вверх, обмениваясь смешком, прежде чем обхватить губами головку."

translate russian bj_birthday_a7d46405:

    bree.say "Перейдём к делу?"

translate russian bj_birthday_aa492e5e:

    "Они кивают друг другу."

translate russian bj_birthday_aca0951c:

    "Я думаю об этом, пока возбуждение от их действий волнами проходит по всему телу."

translate russian bj_birthday_af107b7a:

    "Саша проводит пальцем по лицу, собирая каплю моей спермы."

translate russian bj_birthday_c436957b:

    "Что я сделал, чтобы заслужить лучших соседок в мире?"

translate russian bj_birthday_ca622ff0:

    "Я ненадолго задумываюсь."

translate russian bj_birthday_dcc1e2e0:

    "Две лучшие соседки в мире целуются, зажав между собой мой член; их языки танцуют по моей коже, а руки синхронно дрочат мне."

translate russian bj_birthday_ea3b8162:

    "Я обнимаю их обеих и провожу пальцами по их гладкой коже."

translate russian blissard_meeting_spy_camera_c15880ae:

    "Мне требуется некоторое время, чтобы найти для камеры удачное место, откуда видна вся комната, а саму её почти невозможно заметить, если специально не искать."

translate russian book_signing_5b0149e1:

    "Здесь проходит автограф-сессия любимого писателя [bree.name]."

translate russian book_signing_6d952841:

    "Это не стоит моего времени."

translate russian book_signing_8048cbe0:

    "Уверен, она будет в восторге."

translate russian book_signing_88139e08:

    "Жаль, у меня не хватает денег."

translate russian book_signing_cf5b2070:

    "Может, стоит купить его новую книгу и попросить подписать её."

translate russian bree_caught_peeping_male_09ea7414:

    bree.say "Я тебе не верю, [hero.name]."

translate russian bree_caught_peeping_male_16bef269:

    "Что вовсе не воспользуюсь возможностью заглянуть внутрь."

translate russian bree_caught_peeping_male_23f278bf:

    "Услышав голос [bree.name], я резко оборачиваюсь."

translate russian bree_caught_peeping_male_abc2228f:

    bree.say "О... МОЙ... БОГ..."

translate russian bree_caught_peeping_male_39b1ff36:

    "Я быстро бросаю взгляд и вижу, что именно это и произошло."

translate russian bree_caught_peeping_male_44dc77da:

    "Я снова и снова убеждаю себя, что лишь собираюсь закрыть дверь."

translate russian bree_caught_peeping_male_46ed1dde:

    bree.say "[hero.name]!"

translate russian bree_caught_peeping_male_56f3725d:

    "Я спокойно прохожу мимо ванной, никого не трогая, когда слышу это."

translate russian bree_caught_peeping_male_5ac4ee55:

    "[bree.name] качает головой, отметая моё объяснение."

translate russian bree_caught_peeping_male_5f03a12b:

    "С этими словами [bree.name] сердито уходит."

translate russian bree_caught_peeping_male_7356db01:

    "Меня невольно тянет к проёму."

translate russian bree_caught_peeping_male_7b151b21:

    mike.say "Вдруг кто-то случайно оставил душ включённым? Клянусь!"

translate russian bree_caught_peeping_male_7fc84c38:

    bree.say "С каких пор, чтобы закрыть дверь, нужно сначала заглянуть внутрь?"

translate russian bree_caught_peeping_male_927c2602:

    "В голове уже роится целая буря оправданий."

translate russian bree_caught_peeping_male_9bf96648:

    mike.say "Я просто хотел закрыть дверь, вот и всё!"

translate russian bree_caught_peeping_male_9c63c87a:

    mike.say "Нет-нет-нет..."

translate russian bree_caught_peeping_male_a1b0e38c:

    "А я остаюсь один и чувствую себя жалким извращенцем, которым она теперь меня считает."

translate russian bree_caught_peeping_male_a5ff6cb7:

    "Шум льющейся воды, будто кто-то включил душ и сразу залез под него."

translate russian bree_caught_peeping_male_ac2f2847:

    "Но настолько громко он бывает только тогда, когда находишься по другую сторону двери."

translate russian bree_caught_peeping_male_ae392724:

    mike.say "Я лишь проверял, есть ли там кто-нибудь."

translate russian bree_caught_peeping_male_b1d01af4:

    "Или если дверь ванной оставили открытой..."

translate russian bree_caught_peeping_male_cd148aa9:

    bree.say "Ты собирался подсматривать, извращенец!"

translate russian bree_caught_peeping_male_d8d9f903:

    bree.say "И ещё установлю на дверь ванной замок!"

translate russian bree_caught_peeping_male_db40b114:

    bree.say "Ты действительно..."

translate russian bree_caught_peeping_male_e20421a8:

    "Но я всего лишь человек, и любопытство берёт верх."

translate russian bree_caught_peeping_male_e8ea5834:

    "Кто бы ни был внутри, он забыл закрыть за собой дверь."

translate russian bree_caught_peeping_male_edd6fc0b:

    "Я берусь за ручку и наклоняю голову к щели в двери..."

translate russian bree_caught_peeping_male_ee480ba1:

    "Конечно, ничего необычного в этом нет, я постоянно слышу такой звук."

translate russian bree_kat_threesome_6e154b71:

    mike.say "Ладно, ладно..."

translate russian bree_kat_threesome_920e7962:

    mike.say "А?!"

translate russian bree_kat_threesome_d977d523:

    bree.say "Угх..."

translate russian bree_kat_threesome_e1d914e5:

    mike.say "Хм..."

translate russian bree_kat_threesome_e1d914e5_1:

    mike.say "Хм..."

translate russian bree_kat_threesome_edbaad66:

    "Что тут сказать?"

translate russian bree_lexi_minami_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian bree_lexi_minami_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian bree_lexi_minami_samantha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian bree_lexi_minami_samantha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian bree_lexi_minami_samantha_sasha_male_ending_41ef0227:

    minami.say "Угх..."

translate russian bree_lexi_minami_samantha_sasha_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian bree_lexi_minami_samantha_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian bree_lexi_minami_samantha_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian bree_lexi_minami_sasha_male_ending_41ef0227:

    minami.say "Угх..."

translate russian bree_lexi_minami_sasha_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian bree_lexi_minami_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian bree_lexi_minami_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian bree_lexi_pregnant_showdown_30e74fc5:

    mike.say "Эм..."

translate russian bree_lexi_pregnant_showdown_6e154b71:

    mike.say "Ладно, ладно..."

translate russian bree_lexi_pregnant_showdown_d977d523:

    bree.say "Угх..."

translate russian bree_lexi_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian bree_lexi_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian bree_lexi_samantha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian bree_lexi_samantha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian bree_lexi_samantha_sasha_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian bree_lexi_samantha_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian bree_lexi_samantha_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian bree_lexi_sasha_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian bree_lexi_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian bree_lexi_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian bree_lexi_threesome_breefuck_db9b2219:

    bree.say "Ого..."

translate russian bree_lexi_threesome_intro_0457e272:

    mike.say "Я не знаю..."

translate russian bree_lexi_threesome_intro_200eb25b:

    mike.say "Эй!"

translate russian bree_lexi_threesome_intro_f1d8a63c:

    mike.say "Эм..."

translate russian bree_lexi_threesome_intro_f1d8a63c_1:

    mike.say "Эм..."

translate russian bree_lexi_threesome_lexifuck_c68cc434:

    mike.say "Ох, чёрт..."

translate russian bree_lexi_threesome_lexifuck_c68cc434_1:

    mike.say "Ох, чёрт..."

translate russian bree_minami_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian bree_minami_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian bree_minami_samantha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian bree_minami_samantha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian bree_minami_samantha_sasha_male_ending_24278a5b:

    bree.say "А?"

translate russian bree_minami_samantha_sasha_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian bree_minami_samantha_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian bree_minami_samantha_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian bree_minami_sasha_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian bree_minami_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian bree_minami_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian bree_minami_sasha_transition_bj_foursome_24278a5b:

    bree.say "А?"

translate russian bree_minami_threesome_437a01ea:

    mike.say "Ох, чёрт..."

translate russian bree_minami_threesome_437a01ea_1:

    mike.say "Ох, чёрт..."

translate russian bree_minami_threesome_intro_f1d8a63c:

    mike.say "Эм..."

translate russian bree_request_24278a5b:

    bree.say "А?"

translate russian bree_samantha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian bree_samantha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian bree_samantha_sasha_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian bree_samantha_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian bree_samantha_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian bree_sasha_alternative_creation_087ff008:

    mike.say "Подожди..."

translate russian bree_sasha_alternative_creation_202024be:

    bree.say "Эм..."

translate russian bree_sasha_alternative_creation_30e74fc5:

    mike.say "Эм..."

translate russian bree_sasha_alternative_creation_6757cf6b:

    mike.say "Ну..."

translate russian bree_sasha_alternative_creation_67d5b96e:

    mike.say "Угх..."

translate russian bree_sasha_alternative_creation_78820f82:

    mike.say "Фух..."

translate russian bree_sasha_alternative_creation_8fb73da4:

    mike.say "Я..."

translate russian bree_sasha_alternative_creation_a1c6a138:

    mike.say "Что думаешь?"

translate russian bree_sasha_alternative_creation_c155a10d:

    mike.say "Эй..."

translate russian bree_sasha_alternative_creation_db9b2219:

    bree.say "Ого..."

translate russian bree_sasha_alternative_creation_e1d914e5:

    mike.say "Хм..."

translate russian bree_sasha_alternative_creation_ec4150dc:

    mike.say "Какого..."

translate russian bree_sasha_alternative_creation_f1d8a63c:

    mike.say "Эм..."

translate russian bree_sasha_alternative_creation_f1d8a63c_1:

    mike.say "Эм..."

translate russian bree_sasha_pet_request_75d236b4:

    "Мне остаётся лишь пожать плечами и покачать головой."

translate russian bree_sasha_pet_request_89d2bf47:

    mike.say "Нужно..."

translate russian bree_sasha_pet_request_e84ffc6f:

    mike.say "Что?"

translate russian bree_sasha_pet_request_f1d8a63c:

    mike.say "Эм..."

translate russian bree_sasha_request_1c0d45e8:

    mike.say "Ну..."

translate russian bree_sasha_showdown_8fb73da4:

    mike.say "Я..."

translate russian bree_sasha_showdown_a2dd5d3e:

    mike.say "Не знаю, о чём я думал."

translate russian buy_lottery_ticket_118f74fe:

    "Я проиграл..."

translate russian buy_lottery_ticket_94fd90f7:

    "Я покупаю несколько лотерейных билетов."

translate russian buy_lottery_ticket_9c069fda:

    "Я выиграл [w]{image=gui/icons/icon_money.png}!"

translate russian call_in_home_0248c4fd:

    samantha.say "Да, [hero.name]?"

translate russian call_in_home_1c3d9bfb:

    mike.say "Минами, можешь подойти сюда?"

translate russian call_in_home_338fccbe:

    mike.say "Саша, можешь подойти сюда?"

translate russian call_in_home_510625bf:

    bree.say "Да, [hero.name]?"

translate russian call_in_home_72dbb9e6:

    sasha.say "Да, [hero.name]?"

translate russian call_in_home_9932e9f6:

    lexi.say "Да, [hero.name]?"

translate russian call_in_home_a05ec51c:

    mike.say "[bree.name], можешь подойти сюда?"

translate russian call_in_home_c91d59df:

    mike.say "Лекси, можешь подойти сюда?"

translate russian camila_kylie_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian camila_lexi_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian camila_lexi_propose_male_4df698bd:

    lexi.say "ЭЙ!"

translate russian camila_lexi_propose_male_4df698bd_1:

    lexi.say "ЭЙ!"

translate russian camila_lexi_propose_male_4df698bd_2:

    lexi.say "ЭЙ!"

translate russian camila_lexi_propose_male_52c65242:

    mike.say "Что?!"

translate russian camila_lexi_propose_male_78820f82:

    mike.say "Фух..."

translate russian camila_lexi_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian camila_lexi_threesome_30e74fc5:

    mike.say "Эм..."

translate russian camila_lexi_threesome_6757cf6b:

    mike.say "Ну..."

translate russian camila_lexi_threesome_fuck_3f8382ca:

    mike.say "Ого..."

translate russian camila_lexi_threesome_fuck_ef8c2b21:

    "Я даже не останавливаюсь, чтобы подумать, что делаю."

translate russian cancel_date_internal_5e81b5fb:

    active_girl.say "Хорошо, не переживай."

translate russian cancel_halloween_invite_5e81b5fb:

    active_girl.say "Хорошо, не переживай."

translate russian cassidy_audrey_showdown_8fb73da4:

    mike.say "Я..."

translate russian cassidy_audrey_showdown_f1d8a63c:

    mike.say "Эм..."

translate russian cassidy_palla_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian cassidy_palla_propose_male_30e74fc5_1:

    mike.say "Эм..."

translate russian cassidy_palla_propose_male_30e74fc5_2:

    mike.say "Эм..."

translate russian cassidy_palla_propose_male_30e74fc5_3:

    mike.say "Эм..."

translate russian cassidy_palla_propose_male_30e74fc5_4:

    mike.say "Эм..."

translate russian cassidy_palla_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian cassidy_palla_showdown_1c0d45e8:

    mike.say "Ну..."

translate russian caught_peeping_dialogues_1_male_2c108356:

    mike.say "Я просто..."

translate russian caught_peeping_dialogues_1_male_5cd3bcf5:

    mike.say "Просто проверял..."

translate russian caught_peeping_dialogues_1_male_24f7a903:

    mike.say "П... привет, [caught_girl]!"

translate russian caught_peeping_dialogues_1_male_f1d8a63c:

    mike.say "Эм..."

translate russian cemetery_threesome_1c0d45e8:

    mike.say "Ну..."

translate russian cemetery_threesome_30e74fc5:

    mike.say "Эм..."

translate russian cemetery_threesome_6757cf6b:

    mike.say "Ну..."

translate russian cemetery_threesome_f1d8a63c:

    mike.say "Эм..."

translate russian check_condom_usage_bf1ba27d:

    "Прежде чем продолжить, я беру презерватив с прикроватного столика."

translate russian choose_dog_f1d8a63c:

    mike.say "Эм..."

translate russian cinema_with_231de2c9:

    active_girl.say "Прости, мне сейчас не хочется."

translate russian cinema_with_b778778c:

    active_girl.say "Конечно, почему бы и нет?"

translate russian cinema_with_e97a6db0:

    "Я смотрю фильм вместе с [active_girl.name]."

translate russian clean_my_bedroom_ce54d8db:

    "Я убираюсь в своей спальне."

translate russian clean_the_livingroom_1ec9848a:

    "Я убираюсь в гостиной."

translate russian clean_the_pool_7a7c9fb9:

    "Я чищу бассейн."

translate russian clean_the_secondfloor_5ce15463:

    "Я мою пол."

translate russian cleaning_attic_016cd095:

    "Значит, остаётся только чердак, если, конечно, не поставить для Минами палатку в саду."

translate russian cleaning_attic_018df7b5:

    "Или позвонить Сэм и рассказать, что я нашёл?"

translate russian cleaning_attic_08ed94e5:

    "Но значительная часть меня с радостью просто выбросила бы всё это в мусор и забыла."

translate russian cleaning_attic_09622a18:

    "Откуда, чёрт возьми, всё это взялось?"

translate russian cleaning_attic_0b51c278:

    "И тут я понимаю, что совершенно не представляю, что лежит внутри этих коробок."

translate russian cleaning_attic_11c4428f:

    "Позвонить ему и потребовать объяснений?"

translate russian cleaning_attic_189c61a1:

    "Поэтому я не обращаю на неё внимания и разрезаю скотч, которым заклеена коробка."

translate russian cleaning_attic_191ff460:

    "Остаётся надеяться, что этого достаточно, чтобы стереть воспоминание о моей находке."

translate russian cleaning_attic_1d1b456f:

    "Поэтому я поднимаюсь на чердак, думая, что там потребуется лишь хорошая уборка."

translate russian cleaning_attic_1e0e6d81:

    "Но точно не думал, что она будет доверху забита фотографиями."

translate russian cleaning_attic_1ecf2537:

    "В конце концов я решаю лишь одно: решить я ничего не могу."

translate russian cleaning_attic_228ba475:

    "Но мысль о том, что Минами будет спать там, где хранилась эта жуткая коллекция, всё равно не даёт мне покоя."

translate russian cleaning_attic_2a509b86:

    "Ну, я ведь сам сказал, что это должно стать моим наказанием."

translate russian cleaning_attic_2b6072bf:

    "Ещё раз взглянув на почерк на коробке, я внезапно вспоминаю, где видел его раньше."

translate russian cleaning_attic_2eb1e6e9:

    "Наконец, содрогнувшись и чувствуя себя грязным, я бросаю фотографии обратно в коробку."

translate russian cleaning_attic_30471380:

    "Комната выглядит точно так же, как и в прошлый раз."

translate russian cleaning_attic_35d1cde5:

    "Чтобы отправить всё на переработку, сначала нужно понять, с чем я имею дело."

translate russian cleaning_attic_3a64362f:

    "Сначала характер находки меня удивляет, но не пугает."

translate russian cleaning_attic_3bc0cd4f:

    "Поспешно убирая чердак, как и собирался, я пытаюсь забыть о находке."

translate russian cleaning_attic_3db311c7:

    "Когда я заканчиваю отмывать и вычищать всё вокруг, чердак выглядит совершенно иначе."

translate russian cleaning_attic_3e8a4124:

    "С каждым следующим кадром на ней становится всё меньше одежды, пока она не остаётся полностью обнажённой."

translate russian cleaning_attic_421f1525:

    "Она не может спать в моей комнате, и я точно не могу просить [bree.name] или Сашу делить с ней свою."

translate russian cleaning_attic_4292a058:

    "Даже если в контейнеры всё не поместится, можно вызвать соответствующую службу, чтобы они всё забрали."

translate russian cleaning_attic_45f55c7e:

    "Заинтригованный находкой, я наугад беру одну связку и подношу её к свету."

translate russian cleaning_attic_486cb91f:

    "Единственная настоящая проблема с идеей поселить Минами на чердаке в том, что его придётся расчистить."

translate russian cleaning_attic_5af6d167:

    "Первая мысль: просто выбросить всё это вместе с мусором."

translate russian cleaning_attic_5bbbb71b:

    "Теперь, когда переезд Минами ко мне должен стать реальностью, нужно найти место, где её поселить."

translate russian cleaning_attic_5cb781e0:

    "С этой мыслью я сваливаю в одну кучу все принесённые сюда чистящие средства и щётки."

translate russian cleaning_attic_600e4d9c:

    "На всех снимках одна и та же девушка, которая, похоже, вовсе не против того, что её фотографируют."

translate russian cleaning_attic_64b9e292:

    "На каждой из них девушка запечатлена в компрометирующей ситуации, и ни одна, похоже, не знает, что её фотографируют."

translate russian cleaning_attic_64e17520:

    "Все они аккуратно перевязаны бечёвкой и уложены стопками до самого верха."

translate russian cleaning_attic_673da223:

    "Хотя решить, что теперь делать, уборка мне всё равно никак не поможет..."

translate russian cleaning_attic_82a576cf:

    "Логичнее всего было бы не делать ни того ни другого, а обратиться в полицию."

translate russian cleaning_attic_8450c63f:

    "Но стоит мне войти и включить свет, как сердце уходит в пятки."

translate russian cleaning_attic_86fa7455:

    "Я помню только пыльную комнату, которую нам обещали привести в порядок до нашего заселения."

translate russian cleaning_attic_8b0b000c:

    "Я вижу Сэм, раздевающуюся в какой-то незнакомой мне ванной."

translate russian cleaning_attic_8d071e4a:

    "И снова заниматься этим придётся мне, ведь в конечном счёте она переезжает сюда почти целиком по моей вине."

translate russian cleaning_attic_902be422:

    "Почерк кажется смутно знакомым, но сама надпись мне ни о чём не говорит."

translate russian cleaning_attic_90388fb7:

    "Я понимаю, что должен немедленно перестать листать снимки."

translate russian cleaning_attic_90e7e635:

    "В конце концов, похоже, я просто наткнулся на чью-то забытую коллекцию порно."

translate russian cleaning_attic_98e0ab85:

    "Поэтому собираю все коробки и прячу их в шкафу в коридоре, завалив уже лежащим там хламом."

translate russian cleaning_attic_9a323863:

    "Я мучительно вздыхаю, прекрасно понимая, насколько сложнее теперь будет работа."

translate russian cleaning_attic_a17131cb:

    "Если не считать груды картонных коробок посреди пола."

translate russian cleaning_attic_a5163aa8:

    "Постепенно всё это начинает больше походить на фотоколлекцию сталкера, чем на обычный запас материала для дрочки."

translate russian cleaning_attic_b0346465:

    "Я мог бы поселить её на одном из диванов в гостиной, но в долгосрочной перспективе это не выход."

translate russian cleaning_attic_b2e79a42:

    "Когда глаза привыкают, увиденное оказывается настолько неожиданным, что я едва не роняю фотографии."

translate russian cleaning_attic_b3057de7:

    "Но когда я наугад беру ещё несколько связок, начинает вырисовываться закономерность."

translate russian cleaning_attic_c359ce7f:

    "На клапанах коробки что-то написано, но разобрать надпись трудно."

translate russian cleaning_attic_c4d20345:

    "Там лежат целые связки снимков: полароидные карточки и обычные отпечатки."

translate russian cleaning_attic_c6a94178:

    "Я беру канцелярский нож из кучи инструментов и подхожу к ближайшей стопке."

translate russian cleaning_attic_c830490a:

    "Настоящий ужас и осознание того, на что именно я наткнулся, приходят мгновение спустя."

translate russian cleaning_attic_cfec7eab:

    "На верхнем снимке девушка в нижнем белье лежит на кровати."

translate russian cleaning_attic_d105c364:

    "А затем осматриваю груды коробок, пытаясь понять, с чего начать."

translate russian cleaning_attic_d4fc0f3a:

    "Заинтересовавшись, я перелистываю остальные фотографии, и изображение оживает, словно в книжке с анимацией."

translate russian cleaning_attic_da1f6b0e:

    "Но этого точно не будет: я ведь знаю, что она каким-нибудь образом добьётся, чтобы в палатке жил именно я!"

translate russian cleaning_attic_eae0eeb5:

    "Поэтому я смиряюсь с предстоящей работой и стараюсь воспринимать её как наказание за то, что навязал Минами всем нам."

translate russian cleaning_attic_eb284979:

    "Несколько мгновений я совершенно не понимаю, что делать дальше."

translate russian cleaning_attic_ee3f80fe:

    "Но болезненное, мрачное любопытство заставляет меня смотреть дальше, пока она заходит в душ и моется."

translate russian cleaning_attic_f0b56a4f:

    "Наверное, не стоит жаловаться. Лучше засучить рукава и покончить с этим."

translate russian cleaning_attic_f19479f5:

    "Правда, на чердаке я не был ещё с тех пор, как переехал сюда вместе с Сэмом и Райаном."

translate russian cleaning_attic_f239ac20:

    "Да и тогда агент лишь показал нам помещение, после чего мы сразу пошли дальше."

translate russian cleaning_attic_f3d2f1dc:

    "Это происходит, когда на одной из фотографий я узнаю девушку, которую слишком хорошо знаю."

translate russian cleaning_attic_fa5aff33:

    "Возможно, это дата или адрес, нацарапанные перманентным маркером."

translate russian cleaning_attic_fcbe5c43:

    "В крайнем случае я могу сам загрузить коробки в машину и отвезти их в центр переработки."

translate russian cleaning_attic_fd2b31bb:

    "Это почерк Райана, без всяких сомнений."

translate russian cleaning_attic_feae9a3f:

    "Честно говоря, я понятия не имею, что ожидал найти в первой коробке."

translate russian coffee_break_6c866f70:

    "Я делаю перерыв на кофе..."

translate russian common_cancel_propose_4227f65a:

    bree.say "Мне... Мне просто нужно больше времени..."

translate russian common_cancel_propose_613584bc:

    bree.say "Чтобы разобраться в себе, понимаешь?"

translate russian common_cancel_propose_81713309:

    bree.say "Думаю, нам не стоит жениться прямо сейчас..."

translate russian common_cancel_propose_b35e42c7:

    mike.say "Думаю, нам не стоит жениться прямо сейчас..."

translate russian common_cancel_propose_ed3f5e58:

    mike.say "Чтобы разобраться в себе, понимаешь?"

translate russian common_cancel_propose_f4e3c87b:

    mike.say "Мне... Мне просто нужно больше времени..."

translate russian common_propose_1fc5f118:

    "Мне стоит попробовать ещё раз позже."

translate russian common_propose_6fdc31e6:

    "Попробую ещё раз позже."

translate russian cooking_skill_book_446dcead:

    "Я уже знаю о готовке всё необходимое."

translate russian cooking_skill_book_a014f450:

    "Я учусь готовить. ([skill]%%)"

translate russian criminal_harem_blowjob_67d5b96e:

    mike.say "Угх..."

translate russian criminal_harem_event_01_b199b4a5:

    mike.say "Нет..."

translate russian criminal_harem_event_01_f1d8a63c:

    mike.say "Эм..."

translate russian criminal_harem_event_02_881a82dd:

    "Я открываю рот, чтобы возразить."

translate russian criminal_harem_event_03_30e74fc5:

    mike.say "Эм..."

translate russian criminal_harem_event_03_437a01ea:

    mike.say "Ох, чёрт..."

translate russian criminal_harem_event_03_67d5b96e:

    mike.say "Угх..."

translate russian criminal_harem_event_03_86d07102:

    mike.say "А..."

translate russian criminal_harem_event_03_a5dcc328:

    mike.say "Ай!"

translate russian criminal_harem_event_03_de2ad759:

    mike.say "Что ты..."

translate russian criminal_harem_event_03_f1d8a63c:

    mike.say "Эм..."

translate russian criminal_harem_event_04_1c0d45e8:

    mike.say "Ну..."

translate russian criminal_harem_event_04_30e74fc5:

    mike.say "Эм..."

translate russian criminal_harem_event_04_30e74fc5_1:

    mike.say "Эм..."

translate russian criminal_harem_event_04_3ba2622c:

    "Ну вот, опять!"

translate russian criminal_harem_event_04_401e336e:

    "Я не могу удержаться от улыбки."

translate russian criminal_harem_event_04_4dda1c6b:

    mike.say "Что..."

translate russian criminal_harem_event_04_6757cf6b:

    mike.say "Ну..."

translate russian criminal_harem_event_04_6e154b71:

    mike.say "Ладно, ладно..."

translate russian criminal_harem_fuck_date_30e74fc5:

    mike.say "Эм..."

translate russian criminal_harem_fuck_date_3f8382ca:

    mike.say "Ого..."

translate russian criminal_harem_fuck_date_6757cf6b:

    mike.say "Ну..."

translate russian criminal_harem_fuck_date_9c63c87a:

    mike.say "Нет-нет-нет..."

translate russian dance_girl_2117ea02:

    "[active_girl.name] танцует с симпатичной девушкой."

translate russian dance_girl_402c069b:

    active_girl.say "Не думаю."

translate russian dance_girl_b778778c:

    active_girl.say "Конечно, почему бы и нет?"

translate russian dance_girl_f6741a64:

    mike.say "[active_girl.name], тебе стоит потанцевать с той симпатичной девушкой."

translate russian dance_with_0399574d:

    active_girl.say "Прости, мне не хочется танцевать."

translate russian dance_with_8bfee4ec:

    "Я танцую с [active_girl.name]."

translate russian dance_with_b778778c:

    active_girl.say "Конечно, почему бы и нет?"

translate russian date_buy_a_round_61abc83e:

    active_girl.say "Ты серьёзно?!"

translate russian date_buy_a_round_fb20fd2c:

    "Я хочу угостить пивом весь паб."

translate russian date_her_internal_c64d5e82:

    active_girl.say "Прости, [hero.name], но я не воспринимаю тебя в таком смысле."

translate russian date_her_internal_e2f9481e:

    active_girl.say "Конечно, может быть весело. Когда ты хочешь пойти?"

translate russian date_hot_tub_home_0a0f6ae6:

    "Мы приятно расслабляемся в джакузи."

translate russian date_kart_24e2a451:

    "Я участвую в гонке с [active_girl.name]."

translate russian date_play_arcade_118f74fe:

    "Я проиграл..."

translate russian date_stripclub_dance_on_stage_b778778c:

    active_girl.say "Конечно, почему бы и нет?"

translate russian dna_test_0c6ea6b9:

    "Я незаметно беру образец ДНК у [active_girl.name]."

translate russian dna_test_91b464b7:

    "[active_girl.name] — не отец моего ребёнка..."

translate russian dna_test_c0fa61bb:

    "[active_girl.name] — отец моего ребёнка..."

translate russian do_the_dishes_6875f4c5:

    "Я мою посуду."

translate russian dog_attack_male_222a5594:

    "Обернувшись, я успеваю увидеть лишь размытое пятно лохматой шерсти, несущееся прямо на меня."

translate russian dog_attack_male_30098413:

    "Ещё один взмах, и собака улетает на несколько футов в сторону."

translate russian dog_attack_male_34d3fc9f:

    "К счастью, собака, похоже, вцепилась в основном в штанину, а не в саму ногу."

translate russian dog_attack_male_567012b4:

    "Примерно после полудюжины хороших встрясок я слышу, как рвутся брюки."

translate russian dog_attack_male_7a612c40:

    mike.say "Ой... привет, мальчик!"

translate russian dog_attack_male_5f3c3146:

    "Я даже не останавливаюсь, чтобы посмотреть, куда приземлилась собака."

translate russian dog_attack_male_62b6249d:

    "Я протягиваю руку приближающейся собаке, но её это, похоже, не интересует."

translate russian dog_attack_male_8f21ab8e:

    "Не успеваю я опомниться, как чёртова псина уже грызёт мою ногу!"

translate russian dog_attack_male_a3eed444:

    mike.say "Отцепись от меня, блохастая мелкая тварь!"

translate russian dog_attack_male_a7753c7b:

    "Позади внезапно раздаются лай и цокот когтей по асфальту."

translate russian dog_attack_male_aec6bbe0:

    "Я просто иду по улице, никого не трогаю, когда это происходит."

translate russian dog_attack_male_e497299a:

    "Просто бегу, пока не убеждаюсь, что она больше меня не преследует."

translate russian dog_attack_male_e86a7271:

    mike.say "А-а-аргх!"

translate russian dog_attack_male_edc0b486:

    "Но она упрямо держится, пока я размахиваю ногой из стороны в сторону, пытаясь её стряхнуть."

translate russian dog_attack_male_f3764d14:

    "Я не упускаю шанс и, едва освободившись, тут же бросаюсь бежать."

translate russian dog_attack_male_f7173f55:

    "Вместо этого она скалит зубы и бросается мне на лодыжку."

translate russian dog_shit_bc42788c:

    "Я наступаю в собачье дерьмо..."

translate russian drink_beer_ea9ff812:

    "Буль-буль...\nБуль..."

translate russian drink_coffee_800a0453:

    "Я пью кофе..."

translate russian drink_poledance_02b43b5d:

    "Я смотрю шоу с танцем на шесте."

translate russian drink_poledance_39d36b9b:

    "Я наслаждаюсь особым представлением."

translate russian drink_tea_448d749a:

    "Я пью чай..."

translate russian drink_tea_cured_448d749a:

    "Я пью чай..."

translate russian eat_a_burger_78905beb:

    "Хрум, хрум...\nХрум..."

translate russian eat_a_ramen_3a016881:

    "Хлюп, хлюп...\nХлюп..."

translate russian eat_a_snack_374c9bb7:

    "Я перекусываю."

translate russian emma_samantha_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian emma_samantha_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian emma_samantha_male_ending_da0db528:

    "Priest" "Может, начнём?"

translate russian emma_samantha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian emma_samantha_propose_male_8fb73da4:

    mike.say "Я..."

translate russian emma_samantha_showdown_200eb25b:

    mike.say "Эй!"

translate russian emma_samantha_showdown_f1d8a63c:

    mike.say "Эм..."

translate russian emma_samantha_threesome_intro_30e74fc5:

    mike.say "Эм..."

translate russian emma_samantha_threesome_intro_3f8382ca:

    mike.say "Ого..."

translate russian emma_samantha_threesome_intro_3f8382ca_1:

    mike.say "Ого..."

translate russian fertility_skill_book_8db3f2d0:

    "Я уже знаю о фертильности всё необходимое."

translate russian fertility_skill_book_988606d8:

    "Я читаю в книге о фертильности и о том, как её распознать. ([skill]%%)"

translate russian find_clover_6c1ba575:

    "Сегодня ничего. Попробую снова завтра."

translate russian find_clover_d770ab93:

    "Да! Нашёл!"

translate russian find_clover_efdf8dfc:

    "Я ищу четырёхлистный клевер, чтобы улучшить свою удачу."

translate russian fivesome_breeminamisamsasha_200eb25b:

    mike.say "Эй!"

translate russian found_money_375b8a22:

    "Я нашёл на тротуаре [amount]{image=gui/icons/icon_money.png}!"

translate russian foursome_breesamsasha_e6dcc559:

    mike.say "Ух... ух..."

translate russian foursome_breesamsasha_c633af0c:

    mike.say "Ты в порядке?"

translate russian foursome_office_aletta_50433017:

    aletta.say "Конечно люблю, [hero.name]."

translate russian gaming_harem_event_03_fuck_24278a5b:

    bree.say "А?"

translate russian gaming_harem_event_03_fuck_30e74fc5:

    mike.say "Эм..."

translate russian gaming_harem_threesome_fuck_f1d8a63c:

    mike.say "Эм..."

translate russian gaming_harem_threesome_fuck_f1d8a63c_1:

    mike.say "Эм..."

translate russian generic_get_out_19d7fc07:

    "[verb] без одежды..."

translate russian generic_get_out_7bb7e497:

    "[verb] в нижнем белье [third_person]..."

translate russian generic_get_out_ae349af3:

    "[verb], прикрывшись лишь [towel]..."

translate russian generic_get_out_b0f27b6b:

    "Из-за двери доносится голос."

translate russian generic_get_out_d998d858:

    "[verb] в разной степени раздетости..."

translate russian generic_get_out_dialogues_1_male_f8354afa:

    mike.say "Конечно."

translate russian generic_get_out_dialogues_2_male_eceeeb6e:

    mike.say "Прости, [name], я не знал, что ты здесь."

translate russian generic_meal_1877194a:

    "Мы вместе приятно ужинаем."

translate russian gianna_coffeshop_tea_022b27ce:

    "И к тому же совершенно мне незнакомый."

translate russian gianna_coffeshop_tea_0457e272:

    mike.say "Я не знаю..."

translate russian gianna_coffeshop_tea_04e7b2a3:

    "Gianna" "У нас есть «Английский завтрак», «Эрл Грей», дарджилинг, ассам, сэнтя, «Русский караван», «Леди Грей» и цейлонский!"

translate russian gianna_coffeshop_tea_06fd37e9:

    "Когда изо дня в день ходишь в одну и ту же кофейню, то со временем начинаешь делать всё на автопилоте."

translate russian gianna_coffeshop_tea_0b299a9e:

    "Но никто не выскакивает с признанием, поэтому я прихожу в себя и пытаюсь ответить."

translate russian gianna_coffeshop_tea_0c9d2ad2:

    mike.say "Мне просто нужен чай со вкусом чая!"

translate russian gianna_coffeshop_tea_0df9d40c:

    mike.say "Я хочу чай."

translate russian gianna_coffeshop_tea_135c1150:

    "Иногда за всё время, проведённое там, можно даже ни разу не оторваться от телефона."

translate russian gianna_coffeshop_tea_172d8d31:

    "Остаётся лишь надеяться, что, когда я наконец туда зайду, внутри не окажется никого из тех, кто только что всё это видел."

translate russian gianna_coffeshop_tea_18e006a4:

    "Gianna" "Чай?!"

translate russian gianna_coffeshop_tea_1c307442:

    bree.say "Я бы хотел попробовать чай."

translate russian gianna_coffeshop_tea_1ca42557:

    "Не знаю, то ли я уже перебрал с кофеином."

translate russian gianna_coffeshop_tea_1ca8f0f3:

    "Просто я почти ничего в этом не понимаю."

translate russian gianna_coffeshop_tea_1e964a2b:

    "Gianna" "Хм..."

translate russian gianna_coffeshop_tea_1fd71f0c:

    "Разумеется, всё это время я внимательно разглядываю новую бариста."

translate russian gianna_coffeshop_tea_202024be:

    bree.say "Эм..."

translate russian gianna_coffeshop_tea_20c00d7f:

    "Столько настойчивых вопросов подряд здорово сбивают меня с толку."

translate russian gianna_coffeshop_tea_25e364a3:

    "Но понимаю, что она ждёт от меня ответа."

translate russian gianna_coffeshop_tea_2ea5c6c2:

    bree.say "Я..."

translate russian gianna_coffeshop_tea_2ea5c6c2_1:

    bree.say "Я..."

translate russian gianna_coffeshop_tea_2ea5c6c2_2:

    bree.say "Я..."

translate russian gianna_coffeshop_tea_30e74fc5:

    mike.say "Эм..."

translate russian gianna_coffeshop_tea_31d728e4:

    "Gianna" "Вы действительно хотите чай?"

translate russian gianna_coffeshop_tea_33bbfc1c:

    mike.say "Привет..."

translate russian gianna_coffeshop_tea_eb02b834:

    "Gianna" "Например... чёрный или зелёный?"

translate russian gianna_coffeshop_tea_3b84d620:

    "Её голос сладкий и звонкий, словно колокольчик."

translate russian gianna_coffeshop_tea_3f0a860b:

    "Или хотя бы ответить на один из вопросов."

translate russian gianna_coffeshop_tea_3f8382ca:

    mike.say "Ого..."

translate russian gianna_coffeshop_tea_40ee58e7:

    "Сейчас она, должно быть, считает меня самым тупым парнем на свете!"

translate russian gianna_coffeshop_tea_460e8f70:

    "Но важнее всего то, что говорящая не знает мой обычный заказ."

translate russian gianna_coffeshop_tea_51675402:

    "Gianna" "Может, масала-чай или бабл-ти?"

translate russian gianna_coffeshop_tea_531bb867:

    "Gianna" "Какой ИМЕННО чай, глупенький!"

translate russian gianna_coffeshop_tea_55e4dd91:

    "Но что тут может быть сложного?"

translate russian gianna_coffeshop_tea_6005cfff:

    "Я знаю, что в меню кофейни много разных сортов, потому что видел их."

translate russian gianna_coffeshop_tea_60f53030:

    mike.say "Я бы хотел попробовать чай."

translate russian gianna_coffeshop_tea_662116b9:

    "Gianna" "Или, может, какую-нибудь смесь?"

translate russian gianna_coffeshop_tea_679c727a:

    bree.say "Разве я уже не сказал, что хочу чай?"

translate russian gianna_coffeshop_tea_67dbea69:

    "Похоже, мой выбор напитка сегодня не единственная приятная новинка!"

translate russian gianna_coffeshop_tea_6a0e713b:

    bree.say "Джанна..."

translate russian gianna_coffeshop_tea_6ef0a634:

    "Gianna" "Фух..."

translate russian gianna_coffeshop_tea_72e5e859:

    "Может, и не завтра, но когда-нибудь точно, ведь я серьёзно подсел на хороший кофе."

translate russian gianna_coffeshop_tea_7788dff2:

    "Gianna" "Да!"

translate russian gianna_coffeshop_tea_79b8d610:

    "Длинные каштановые волосы, собранные в два хвостика, светло-зелёные глаза и внушительная фигура под фартуком."

translate russian gianna_coffeshop_tea_7aeb9a17:

    "Gianna" "Кажется, это всё!"

translate russian gianna_coffeshop_tea_7c8615ee:

    "Gianna" "Что вам приготовить сегодня?"

translate russian gianna_coffeshop_tea_8049e112:

    bree.say "Нет, я совершенно серьёзно..."

translate russian gianna_coffeshop_tea_83ea5222:

    "Я не останавливаюсь и не оглядываюсь, пока не оказываюсь в нескольких кварталах от кофейни."

translate russian gianna_coffeshop_tea_87419d37:

    "Я на мгновение задерживаю взгляд на бейджике девушки."

translate russian gianna_coffeshop_tea_8bd68613:

    "Значит, она здесь новенькая, и пора произвести хорошее первое впечатление!"

translate russian gianna_coffeshop_tea_8fb73da4:

    mike.say "Я..."

translate russian gianna_coffeshop_tea_8fb73da4_1:

    mike.say "Я..."

translate russian gianna_coffeshop_tea_8fb73da4_2:

    mike.say "Я..."

translate russian gianna_coffeshop_tea_936bb66e:

    "Gianna" "Тогда можете выбрать чай с корой ивы, белым пионом, куркумой, шалфеем, шиповником, хвоей, перечной мятой, петрушкой, крапивой, мятой, календулой, солодкой, жасмином, жимолостью, гибискусом, имбирём, фенхелем, корицей, ромашкой или гречихой..."

translate russian gianna_coffeshop_tea_9e7c0a6b:

    bree.say "Привет..."

translate russian gianna_coffeshop_tea_a1391c04:

    "Я могу лишь стоять и изумлённо смотреть на Джанну."

translate russian gianna_coffeshop_tea_a2771924:

    "Gianna" "Вы уверены, что имели в виду не кофе?"

translate russian gianna_coffeshop_tea_a652e098:

    "Gianna" "Возможно, вам больше нравятся определённые вкусы?"

translate russian gianna_coffeshop_tea_a730718c:

    bree.say "Я не знаю..."

translate russian gianna_coffeshop_tea_a8ca1efd:

    "И вот ты уже выходишь с кофе в руке, сведя общение с людьми к абсолютному минимуму."

translate russian gianna_coffeshop_tea_aca7ab37:

    bree.say "Это напитки или названия мест?"

translate russian gianna_coffeshop_tea_af9588bf:

    "Но сегодня всё иначе: мне захотелось чего-нибудь нового."

translate russian gianna_coffeshop_tea_afcd3bcc:

    "После всех перечисленных Джанной сортов и вкусов это наверняка прозвучало ужасно глупо."

translate russian gianna_coffeshop_tea_b2d7aadd:

    "И должен признать, увиденное впечатляет меня сильнее, чем я ожидал."

translate russian gianna_coffeshop_tea_b32e0cdc:

    mike.say "Джанна..."

translate russian gianna_coffeshop_tea_b445769a:

    "Бариста тебя узнаёт, готовит обычный заказ, а ты прикладываешь карту или телефон."

translate russian gianna_coffeshop_tea_b8ed6c29:

    "И только тогда понимаю, что рано или поздно мне всё равно придётся туда вернуться."

translate russian gianna_coffeshop_tea_c08c1d0f:

    "Джанна радостно хлопает в ладоши."

translate russian gianna_coffeshop_tea_c1400bec:

    mike.say "Нет, я совершенно серьёзно..."

translate russian gianna_coffeshop_tea_c4e8c4d7:

    bree.say "Мне просто нужен чай со вкусом чая!"

translate russian gianna_coffeshop_tea_c4ef1b97:

    "Gianna" "Или даже копчёный?"

translate russian gianna_coffeshop_tea_c829c178:

    "Gianna" "Привет..."

translate russian gianna_coffeshop_tea_d04d4e6c:

    "Единственное, что приходит мне в голову, это развернуться и выбежать прямо за дверь."

translate russian gianna_coffeshop_tea_d14c8cc6:

    "Настолько, что я отступаю на шаг и оглядываюсь, проверяя, не разыгрывают ли меня."

translate russian gianna_coffeshop_tea_d18c1c45:

    bree.say "Я хочу чай."

translate russian gianna_coffeshop_tea_c522a084:

    "Gianna" "Так... что вам приготовить?"

translate russian gianna_coffeshop_tea_d57e9418:

    "Gianna" "Я ОБОЖАЮ чай, но все заказывают только кофе."

translate russian gianna_coffeshop_tea_d8799d7e:

    "Gianna" "Вы только что сделали мой день!"

translate russian gianna_coffeshop_tea_db3fbb30:

    "То ли просто мечтаю о другом напитке, который не даст мне уснуть прямо за рабочим столом."

translate russian gianna_coffeshop_tea_db9b2219:

    bree.say "Ого..."

translate russian gianna_coffeshop_tea_dbcc8bd5:

    mike.say "Разве я уже не сказал, что хочу чай?"

translate russian gianna_coffeshop_tea_de9fb209:

    "Его ведь просто наливают в чашку, как кофе, верно?"

translate russian gianna_coffeshop_tea_dfc2d3c2:

    "И под этим давлением мой мозг будто полностью отключается."

translate russian gianna_coffeshop_tea_e1721ad2:

    "Какой бы ни была причина этого внезапного предательства кофе, я хочу попробовать чай."

translate russian gianna_coffeshop_tea_f8334765:

    "Gianna" "По крайней мере, так было до вашего прихода!"

translate russian gianna_coffeshop_tea_f9eb11d8:

    mike.say "Это напитки или названия мест?"

translate russian gianna_coffeshop_tea_febe16a0:

    "Обычно любого из этих обстоятельств хватило бы, чтобы я поднял взгляд и обратил внимание."

translate russian gig_b3fab84d:

    "На выступлении мы заработали [money_produced]{image=gui/icons/icon_money.png}!"

translate russian gig_d6894531:

    "Я забираю свою долю, примерно [hero_share]{image=gui/icons/icon_money.png}."

translate russian give_a_gift_3b6be9cb:

    active_girl.say "Нет, спасибо."

translate russian give_a_gift_736a6223:

    active_girl.say "Зачем мне вторая?"

translate russian give_a_gift_ab412b1c:

    "Не думаю, что мне стоит дарить это [active_girl.personal_pronoun]... По крайней мере, пока..."

translate russian give_a_gift_d38ab07e:

    active_girl.say "У меня уже есть такая вещь."

translate russian give_a_gift_reaction_07f96c45:

    "Похоже, подарок оставил [active_girl.name] равнодушной."

translate russian give_a_gift_reaction_92df63c3:

    "Похоже, подарок понравился [active_girl.name]."

translate russian give_a_gift_reaction_e417cbc7:

    "Похоже, подарок не понравился [active_girl.name]."

translate russian give_phone_number_dialogues_1_male_f8354afa:

    mike.say "Конечно."

translate russian go_steady_8f5f1cd6:

    active_girl.say "Нет, спасибо..."

translate russian go_steady_96a996b9:

    active_girl.say "Конечно, я этого хочу!"

translate russian goodevil_harem_event_01_1c0d45e8:

    mike.say "Ну..."

translate russian goodevil_harem_event_01_200eb25b:

    mike.say "Эй!"

translate russian goodevil_harem_event_01_30e74fc5:

    mike.say "Эм..."

translate russian goodevil_harem_event_01_6757cf6b:

    mike.say "Ну..."

translate russian goodevil_harem_event_01_67d5b96e:

    mike.say "Угх..."

translate russian goodevil_harem_event_01_67d5b96e_1:

    mike.say "Угх..."

translate russian goodevil_harem_event_01_6e154b71:

    mike.say "Ладно, ладно..."

translate russian goodevil_harem_event_01_786aeaf8:

    mike.say "Ого!"

translate russian goodevil_harem_event_01_86d07102:

    mike.say "А..."

translate russian goodevil_harem_event_02_4df698bd:

    lexi.say "ЭЙ!"

translate russian goodevil_harem_event_02_6757cf6b:

    mike.say "Ну..."

translate russian goodevil_harem_event_02_6e154b71:

    mike.say "Ладно, ладно..."

translate russian goodevil_harem_event_02_ee1a096f:

    mike.say "Ни за что!"

translate russian goodevil_harem_event_02_ee1a096f_1:

    mike.say "Ни за что!"

translate russian goodevil_threesome_30e74fc5:

    mike.say "Эм..."

translate russian goodevil_threesome_cumshare_1ccab2e1:

    mike.say "Хм..."

translate russian goodevil_threesome_cumshare_de2ad759:

    mike.say "Что ты..."

translate russian goodevil_threesome_e84ffc6f:

    mike.say "Что?"

translate russian goodevil_threesome_fuck_harmony_4dda1c6b:

    mike.say "Что..."

translate russian goodevil_threesome_fuck_harmony_4dda1c6b_1:

    mike.say "Что..."

translate russian goodevil_threesome_mikebedroom_double_oral_finish_1ccab2e1:

    mike.say "Хм..."

translate russian goodevil_threesome_mikebedroom_double_oral_finish_de2ad759:

    mike.say "Что ты..."

translate russian grope_738d3ca8:

    "Похоже, ей это не нравится..."

translate russian grope_bf431e08:

    "Похоже, ей это нравится!"

translate russian grope_c90a624b:

    "Я хватаю [active_girl.name] за грудь."

translate russian guitar_skill_book_7862365e:

    "Я упражняюсь в игре на гитаре. ([skill]%%)"

translate russian guitar_skill_book_88ba00b5:

    "Я уже знаю об игре на гитаре всё необходимое."

translate russian gym_need_membership_1d38c428:

    "Для доступа в это помещение мне нужен абонемент."

translate russian gym_out_4a3d612d:

    "Чтобы приходить сюда, мне нужно купить спортивную одежду."

translate russian hack_computer_04c246a3:

    "Стоит мне подумать, что я наконец-то к чему-то подобрался, как зацепки заканчиваются. Всё выглядит так, будто кто-то специально добавил эти операции в мою бухгалтерию."

translate russian hack_computer_135c0d1e:

    "И теперь у меня есть доказательства."

translate russian hack_computer_1f62b217:

    "После ещё одного часа проверки операций след приводит к нескольким внешним счетам дочерней компании. Завтра придётся изучить её подробнее."

translate russian hack_computer_22a7efa6:

    "Я сажусь за компьютер Алетты и вхожу в систему. Поначалу я понятия не имею, что искать, поэтому начинаю просматривать все папки, связанные с бухгалтерией."

translate russian hack_computer_26e8085a:

    "Прошло немало времени, и мне следовало бы помнить все эти цифры, но я их не помню. Я отмечаю несколько операций и записываю, какие из них нужно проверить завтра."

translate russian hack_computer_3f9da6ee:

    "Я собираю воедино всё, что уже выяснил, и трижды перепроверяю бухгалтерские данные."

translate russian hack_computer_5403241c:

    "Я продолжаю с того места, где остановился, и глубже изучаю систему, проверяя собственные счета расходов за последние несколько лет."

translate russian hack_computer_9632f7ca:

    "Генеральный директор этой компании присваивает деньги, а меня сделал козлом отпущения."

translate russian hack_computer_b2536afe:

    "Около часа я изучаю счета, но информации так много, что ничего действительно полезного мне найти не удаётся."

translate russian hack_computer_b858d68f:

    "Я глубже изучаю дочернюю компанию, но постоянно упираюсь в тупики, похожие на ложные следы: офшорные счета и фирмы без единого сотрудника."

translate russian hack_computer_c5802c0d:

    "Но я не могу понять кто, а единственное доказательство состоит в том, что я их не помню. Никто этому не поверит."

translate russian hack_computer_e7a00abb:

    "Выясняется, что компания, которую я обнаружил в прошлый раз, была создана из офиса Дуэйна, но в документах это намеренно скрыто за расплывчатыми формулировками. Неужели настоящий вор Дуэйн? Увы, доказательств у меня нет."

translate russian hack_computer_ecbd2d6d:

    "Придётся попробовать снова завтра."

translate russian hack_computer_eece1fb2:

    "Я целый час изучаю отмеченные операции. Я уверен, что не совершал их, но всё ещё не могу понять, откуда они взялись. Завтра проверю ещё раз."

translate russian hack_computer_f70a102b:

    "Отбросив ложные следы, я больше не сомневаюсь: фиктивные операции создал сам Дуэйн."

translate russian haircut_07964778:

    "Нужно лишь подровнять кончики."

translate russian haircut_0a934246:

    "Мне нравится мой естественный цвет."

translate russian haircut_4e633e47:

    "Мне нужны перемены. Я покрашу волосы."

translate russian haircut_68d4f997:

    "Стало немного лучше, но жизнь это не изменило."

translate russian haircut_7d1d87ef:

    "Так мне уже гораздо лучше."

translate russian haircut_a20cefa7:

    "..."

translate russian haircut_c838c46d:

    "Я стригусь."

translate russian haircut_ead7c143:

    "Я стригусь и крашу волосы."

translate russian haircut_eee2c9b8:

    "Хотя не думаю, что небольшая стрижка сильно повлияет на мою харизму..."

translate russian halloween_invite_8669f130:

    mike.say "У тебя уже есть планы на Хэллоуин?"

translate russian halloween_invite_86d07102:

    mike.say "А..."

translate russian harmony_lexi_showdown_200eb25b:

    mike.say "Эй!"

translate russian harmony_lexi_showdown_200eb25b_1:

    mike.say "Эй!"

translate russian harmony_lexi_showdown_30e74fc5:

    mike.say "Эм..."

translate russian harmony_lexi_showdown_67d5b96e:

    mike.say "Угх..."

translate russian harmony_lexi_showdown_6e154b71:

    mike.say "Ладно, ладно..."

translate russian harmony_poledance_08f4f128:

    "Но потом она тянется руками к шесту."

translate russian harmony_poledance_0c306736:

    "Не знаю, репетировала ли Хармони этот номер заранее."

translate russian harmony_poledance_19fee952:

    "К этому моменту на Хармони остаются только лифчик и трусики."

translate russian harmony_poledance_2ff5a466:

    "Под громкую музыку Хармони уверенно выходит на середину сцены."

translate russian harmony_poledance_3efbd03b:

    "Не знаю, напоминает ли это мне грудное вскармливание из младенчества."

translate russian harmony_poledance_46c21809:

    "Все следят за каждым движением и почти умоляют о продолжении!"

translate russian harmony_poledance_4a96bb6c:

    "Хармони изгибается и поворачивается, понемногу спуская платье с плеч."

translate russian harmony_poledance_4f1378df:

    "Будто заранее понимают, что сейчас произойдёт нечто необычное."

translate russian harmony_poledance_5d92d111:

    "Она держится так, словно владеет этим местом, как королева на приёме."

translate russian harmony_poledance_60071870:

    "Когда она наконец поворачивается спиной и расстёгивает лифчик, зал взрывается."

translate russian harmony_poledance_688012c3:

    "Но на сцене всё это почему-то кажется совершенно новым."

translate russian harmony_poledance_73e1e5ee:

    "Хармони прикрывает грудь обеими руками, а затем снова поворачивается лицом."

translate russian harmony_poledance_852f43be:

    "Хармони снова начинает двигаться, заставляя её покачиваться из стороны в сторону."

translate russian harmony_poledance_85312732:

    "На мгновение я думаю, что она на этом остановится."

translate russian harmony_poledance_8b6ac53f:

    "Зрители сразу замечают что-то особенное в её улыбке."

translate russian harmony_poledance_8c4a3b59:

    "Возможно, вся история с тем, что она затащила меня сюда, была подстроена."

translate russian harmony_poledance_8e0116a2:

    "Когда мы встретились раньше вечером, я уже удивился тому, как мало на ней одежды."

translate russian harmony_poledance_935c1de5:

    "Но теперь она каким-то образом превращает её снятие в целое представление!"

translate russian harmony_poledance_98bc31d0:

    "Как бы то ни было, на сцене она зажигает, а я становлюсь твёрже с каждой секундой."

translate russian harmony_poledance_b00a4ff8:

    "И с первого же движения Хармони не разочаровывает."

translate russian harmony_poledance_b0c3310a:

    "Движение гипнотизирует, от него невозможно отвести взгляд."

translate russian harmony_poledance_c0566788:

    "Не могу поверить, как легко она дразнит публику."

translate russian harmony_poledance_c94964ff:

    "Она обвивается вокруг шеста на сцене."

translate russian harmony_poledance_ca5000f6:

    "Или меня просто соблазняет самая идеальная пара грудей, какую можно представить!"

translate russian harmony_poledance_cff6fe54:

    "Ведь я уже не раз видел Хармони голой."

translate russian harmony_poledance_d3e93a37:

    "Но может быть, всё происходит спонтанно и у неё просто природный талант."

translate russian harmony_poledance_d85ed547:

    "Странно, но я заворожён не меньше всех остальных."

translate russian harmony_poledance_e4ec192c:

    "С каждым движением зрителям открывается всё больше её обнажённой кожи."

translate russian harmony_poledance_e8e381ac:

    "И чем больше вижу, тем сильнее хочу увидеть остальное."

translate russian harmony_poledance_f683afb5:

    "И её тяжёлая округлая грудь освобождается."

translate russian harmony_poledance_ffdd9b42:

    "Я так же, как остальные, напрягаюсь, стараясь увидеть как можно больше."

translate russian heart_attack_02ec9de9:

    "Например, на том, что в постели я сейчас просто творю чудеса."

translate russian heart_attack_08f6aa78:

    "Я не понимаю, принадлежат ли слышимые мною приглушённые звуки голосам этих людей." with dissolve

translate russian heart_attack_0db00d3f:

    "Ничего серьёзного, просто лёгкий спазм, хотя он и заставляет меня немного встревожиться."

translate russian heart_attack_160c36ab:

    "Или это где-то вдали воет сирена скорой помощи."

translate russian heart_attack_271d8366:

    "Почти такая же широкая, как у девушек, с которыми я сплю!"

translate russian heart_attack_29248ee0:

    "Хотя, возможно, это просто пятна перед глазами."

translate russian heart_attack_2951d303:

    "В кистях появляется покалывание, а голова начинает кружиться."

translate russian heart_attack_30b67470:

    "Серьёзно, своими подвигами под одеялом я буквально сражаю женщин наповал!"

translate russian heart_attack_38c2b3e1:

    "Кажется, надо мной стоят какие-то люди."

translate russian heart_attack_438d9f26:

    "Но разве так будет не всегда?"

translate russian heart_attack_56a674d0:

    "Зрение мутнеет, а по краям всё начинает темнеть."

translate russian heart_attack_64a53be7:

    "Да-да, я знаю, о чём вы подумали."

translate russian heart_attack_69025f54:

    "А теперь осталась лишь тьма..." with dissolve

translate russian heart_attack_720d91fe:

    "Я знаю лишь одно: всё вокруг постепенно погружается во тьму." with dissolve

translate russian heart_attack_78d909f8:

    "И продолжаю уверенно шагать по улице, стараясь выбросить это из головы."

translate russian heart_attack_7a72de52:

    "Конечно, кое-что в моей жизни могло бы складываться и получше."

translate russian heart_attack_86044a55:

    "Затем колени подгибаются, и я падаю на землю."

translate russian heart_attack_8ce322b1:

    "Но зачем довольствоваться посредственным результатом, когда можно добиться гораздо большего?"

translate russian heart_attack_93788837:

    "Будто такие штуки нужны только старикам, у которых уже не встаёт."

translate russian heart_attack_af3026fc:

    "И всё благодаря одной маленькой синей таблетке."

translate russian heart_attack_bea69099:

    "Вместо того чтобы думать о подобных неприятностях, я сосредоточиваюсь на хорошем."

translate russian heart_attack_c251deef:

    "Сегодня я иду по улице в редком состоянии почти полного счастья."

translate russian heart_attack_c591e8c4:

    "И я ничего не могу с этим сделать."

translate russian heart_attack_d45d7f95:

    "Вы бы видели, какая широкая улыбка появляется у меня на лице."

translate russian heart_attack_e595c84c:

    "Я не могу пошевелиться, а сердце будто вот-вот взорвётся у меня в груди."

translate russian heart_attack_ef6272a0:

    "И на этот раз боль гораздо сильнее, её уже невозможно игнорировать."

translate russian heart_attack_fed9fcf2:

    "Я решаю, что такое иногда просто случается."

translate russian home_harem_bree_lexi_beach_date_1c0d45e8:

    mike.say "Ну..."

translate russian home_harem_bree_lexi_beach_date_24278a5b:

    bree.say "А?"

translate russian home_harem_bree_lexi_beach_date_6e154b71:

    mike.say "Ладно, ладно..."

translate russian home_harem_bree_lexi_beach_date_94966ff5:

    bree.say "Эй!"

translate russian home_harem_bree_lexi_beach_date_d977d523:

    bree.say "Угх..."

translate russian home_harem_bree_lexi_beach_date_f1d8a63c:

    mike.say "Эм..."

translate russian home_harem_bree_lexi_beach_fuck_200eb25b:

    mike.say "Эй!"

translate russian home_harem_bree_lexi_beach_fuck_24278a5b:

    bree.say "А?"

translate russian home_harem_bree_lexi_beach_fuck_437a01ea:

    mike.say "Ох, чёрт..."

translate russian home_harem_bree_lexi_beach_fuck_437a01ea_1:

    mike.say "Ох, чёрт..."

translate russian home_harem_bree_sasha_beach_date_33a63351:

    bree.say "Ох, [hero.name]!"

translate russian home_harem_bree_sasha_beach_date_59628124:

    mike.say "Неважно."

translate russian home_harem_bree_sasha_beach_fuck_202024be:

    bree.say "Эм..."

translate russian home_harem_bree_sasha_beach_fuck_e84ffc6f:

    mike.say "Что?"

translate russian home_harem_confession_to_sam_1c0d45e8:

    mike.say "Ну..."

translate russian home_harem_confession_to_sam_881a82dd:

    "Я открываю рот, чтобы возразить."

translate russian home_harem_lexi_minami_samantha_beach_date_30e74fc5:

    mike.say "Эм..."

translate russian home_harem_lexi_minami_samantha_beach_date_3f8382ca:

    mike.say "Ого..."

translate russian home_harem_lexi_minami_samantha_beach_date_4dda1c6b:

    mike.say "Что..."

translate russian home_harem_lexi_minami_samantha_beach_date_6e154b71:

    mike.say "Ладно, ладно..."

translate russian home_harem_lexi_minami_samantha_beach_fuck_intro_200eb25b:

    mike.say "Эй!"

translate russian home_harem_lexi_minami_samantha_beach_fuck_intro_30e74fc5:

    mike.say "Эм..."

translate russian home_harem_lexi_minami_samantha_beach_fuck_intro_3f8382ca:

    mike.say "Ого..."

translate russian home_harem_samantha_sasha_beach_date_b199b4a5:

    mike.say "Нет..."

translate russian home_harem_samantha_sasha_beach_date_e1d914e5:

    mike.say "Хм..."

translate russian home_harem_samantha_sasha_beach_fuck_1a3f4f16:

    mike.say "Д... да..."

translate russian home_harem_sixsome_satisfied_sex_ending_c633af0c:

    mike.say "Ты в порядке?"

translate russian hot_tub_0a0f6ae6:

    "Мы приятно расслабляемся в джакузи."

translate russian hot_tub_alone_0db88be6:

    "Я погружаюсь в джакузи."

translate russian hotdog_374c9bb7:

    "Я перекусываю."

translate russian house_place_spy_camera_11810b75:

    "Да, на бумаге задача кажется не самой сложной, но я специалист по компьютерам, а не мастер на все руки, понятно?"

translate russian house_place_spy_camera_525ee70b:

    "Место для камеры получилось удачным: она охватывает весь передний двор, а заметить её почти невозможно, если специально не искать."

translate russian house_place_spy_camera_58661ffd:

    "Когда с этим было покончено, мне понадобилось всего несколько минут, чтобы вывести изображение с камеры на ноутбук и телефон."

translate russian house_place_spy_camera_70c32ea0:

    "Честно говоря, я не помню, возникла ли идея купить камеру и установить её у крыльца из-за Кайли."

translate russian house_place_spy_camera_9810a003:

    "Наверное, уже сам факт того, что я всё закончил, помог мне почувствовать себя гораздо спокойнее."

translate russian house_place_spy_camera_ba55c45e:

    "Или я и раньше подумывал об этом, а история с ней лишь заставила меня наконец действовать."

translate russian house_place_spy_camera_d4c417aa:

    "Как бы то ни было, я раздобыл камеру и потратил несколько мучительных часов, пытаясь незаметно установить её у входа."

translate russian house_remove_spy_camera_087526b3:

    "Единственный признак жизни на записи — кто-то, выгуливающий собаку посреди ночи."

translate russian house_remove_spy_camera_289ce3cc:

    "Запись заканчивается, и теперь я в полной мере понимаю значение слова «скука»."

translate russian house_remove_spy_camera_6a594caa:

    "Как только у меня появляется свободная минута, я открываю запись за прошлую ночь."

translate russian house_remove_spy_camera_7613200f:

    "Поначалу, сколько я ни просматриваю её, ничего, что могло бы объяснить эту загадку, не нахожу."

translate russian house_remove_spy_camera_93dcb426:

    "Странно, конечно, но ничего незаконного или антиобщественного в этом нет."

translate russian hypnosis_action_0801bba7:

    active_girl.say "Мне нужно стать более распутной, чтобы угодить Господу..."

translate russian hypnosis_action_1417ec23:

    mike.say "Думаю, тебе стоит стать более неуравновешенной."

translate russian hypnosis_action_1f7ebad5:

    mike.say "Думаю, тебе стоит быть более мужественной."

translate russian hypnosis_action_202c0f32:

    active_girl.say "Мне стоит быть более женственной..."

translate russian hypnosis_action_24d76322:

    active_girl.say "Мне стоит быть более властной..."

translate russian hypnosis_action_2547b47c:

    "Я начинаю гипнотизировать [active_girl.name]..."

translate russian hypnosis_action_2c856244:

    mike.say "Думаю, тебе стоит меньше любить девушек."

translate russian hypnosis_action_40845f56:

    active_girl.say "Мне нужно быть хорошей девочкой..."

translate russian hypnosis_action_44477f2c:

    active_girl.say "Мне стоит стать более неуравновешенной."

translate russian hypnosis_action_460400d8:

    active_girl.say "Девушки такие сексуальные и милые..."

translate russian hypnosis_action_629a1049:

    mike.say "Слушай меня, [active_girl.name]."

translate russian hypnosis_action_6824362b:

    active_girl.say "Мне стоит быть более мужественной..."

translate russian hypnosis_action_7bed30f1:

    active_girl.say "В конце концов, девушки не такие уж сексуальные..."

translate russian hypnosis_action_84c7438f:

    mike.say "Думаю, тебе стоит быть более женственной."

translate russian hypnosis_action_8d76ab40:

    active_girl.say "Мне нужно быть более распутной..."

translate russian hypnosis_action_919ca7c4:

    mike.say "...Ничего..."

translate russian hypnosis_action_919e7336:

    mike.say "Думаю, тебе стоит быть более невинной."

translate russian hypnosis_action_94d2586e:

    mike.say "Думаю, Бог хочет, чтобы ты стала более распутной."

translate russian hypnosis_action_a4eee12a:

    mike.say "Думаю, тебе стоит быть более властной."

translate russian hypnosis_action_b6e432d6:

    active_girl.say "Мне стоит стать более уравновешенной."

translate russian hypnosis_action_c1386e0b:

    mike.say "Думаю, тебе стоит больше любить девушек."

translate russian hypnosis_action_cb6714c7:

    active_girl.say "Мне стоит быть более покорной..."

translate russian hypnosis_action_d17ca080:

    mike.say "Думаю, тебе стоит быть более покорной."

translate russian hypnosis_action_d2dc9751:

    active_girl.say "Какого хрена ты делаешь?"

translate russian hypnosis_action_ee1f2270:

    mike.say "Думаю, тебе стоит быть более распутной."

translate russian hypnosis_action_f51c56e9:

    mike.say "Думаю, тебе стоит стать более уравновешенной."

translate russian hypnosis_arrested_01d704e4:

    "Michaels" "А ты сиди смирно, сынок."

translate russian hypnosis_arrested_021e017c:

    "Прекрасно, теперь ко мне на улице пристаёт какой-то извращенец!"

translate russian hypnosis_arrested_0af582f3:

    "Michaels" "Положи эту штуку и спокойно пойдём со мной, сынок!"

translate russian hypnosis_arrested_121d4528:

    "Michaels" "Фух..."

translate russian hypnosis_arrested_1326f6a8:

    "Michaels" "Видите ли, я ищу парня, который ходит по городу и гипнотизирует людей."

translate russian hypnosis_arrested_13ee464e:

    "Какой бы вопрос ни возник, в конце концов все начинают соглашаться со мной!"

translate russian hypnosis_arrested_16cb9974:

    "Он старше меня, но жилистый и крепкий."

translate russian hypnosis_arrested_1e7a069d:

    "Книга о гипнозе лежит у меня в кармане, и я вытаскиваю её."

translate russian hypnosis_arrested_2338436e:

    "Он машет мне рукой, словно хочет о чём-то спросить."

translate russian hypnosis_arrested_2956f60c:

    mike.say "О нет!"

translate russian hypnosis_arrested_2c6239fd:

    "А затем, словно этого мало, садится на меня и вызывает подкрепление."

translate russian hypnosis_arrested_2c67bb77:

    "Michaels" "Скоро за тобой приедут."

translate russian hypnosis_arrested_32a233b1:

    "Поэтому пытается успокоить ситуацию."

translate russian hypnosis_arrested_343146c3:

    "Michaels" "И мне нужно посадить его за решётку, чтобы это прекратилось."

translate russian hypnosis_arrested_358d9b9d:

    "Michaels" "А вы очень похожи на молодого человека, которого я сейчас разыскиваю!"

translate russian hypnosis_arrested_362c0355:

    "Детектив, должно быть, думает, что я тянусь за оружием."

translate russian hypnosis_arrested_48ed01de:

    "Но тут уже удивляюсь я: он достаёт полицейский жетон."

translate russian hypnosis_arrested_5112778d:

    "Вот почему сейчас я уверенно шагаю по улице, чувствуя себя королём мира."

translate russian hypnosis_arrested_51af659d:

    "Качаю головой и выставляю перед собой руки, пытаясь удержать его на расстоянии."

translate russian hypnosis_arrested_5465ac9f:

    "Надо бы найти время, написать отцу и поблагодарить его за присланную книгу."

translate russian hypnosis_arrested_587855c6:

    "Но я замечаю, что одновременно он качает головой."

translate russian hypnosis_arrested_62160ba2:

    "Детектив Майклс делает шаг вперёд, по-прежнему улыбаясь мне."

translate russian hypnosis_arrested_654f7c2a:

    "Я инстинктивно начинаю пятиться."

translate russian hypnosis_arrested_694dc984:

    mike.say "Прости, приятель, но бродягам я денег не подаю!"

translate russian hypnosis_arrested_72636e60:

    "Но затем усмехается и качает головой."

translate russian hypnosis_arrested_77579305:

    "Michaels" "Это я!"

translate russian hypnosis_arrested_80fd285c:

    "Но затем видит, что у меня всего лишь книга, и смеётся."

translate russian hypnosis_arrested_836131e8:

    "Знакомство с основами гипноза стало для меня настоящим откровением."

translate russian hypnosis_arrested_86d07102:

    mike.say "А..."

translate russian hypnosis_arrested_8726fc9d:

    "И вскоре я чувствую, как он надевает на меня наручники."

translate russian hypnosis_arrested_8dab4b77:

    "Michaels" "Нет, так не пойдёт!"

translate russian hypnosis_arrested_94a0356f:

    "Inspector" "Простите, сэр..."

translate russian hypnosis_arrested_abb11bdb:

    "Inspector" "Эм..."

translate russian hypnosis_arrested_ae75600a:

    mike.say "Иначе я и вас загипнотизирую!"

translate russian hypnosis_arrested_b277f574:

    "Я останавливаюсь и оборачиваюсь, замечая неряшливого мужчину средних лет."

translate russian hypnosis_arrested_b8533ad1:

    "Мужчина выглядит немного удивлённым моим ответом."

translate russian hypnosis_arrested_b8d7913c:

    "Inspector" "Детектив Майклс..."

translate russian hypnosis_arrested_bbfc3298:

    "Inspector" "Нет, сэр, нет..."

translate russian hypnosis_arrested_beae7373:

    "Inspector" "Ваша мелочь мне не нужна."

translate russian hypnosis_arrested_c84d4319:

    "Говоря это, он начинает шарить под пальто."

translate russian hypnosis_arrested_e06b179d:

    "Michaels" "Точнее говоря, он гипнотизирует молодых женщин по всему городу."

translate russian hypnosis_arrested_e84ffc6f:

    mike.say "Что?"

translate russian hypnosis_arrested_ea2a984d:

    "Michaels" "А потом ты сможешь как следует отдохнуть в уютной маленькой камере!"

translate russian hypnosis_arrested_ee1a096f:

    mike.say "Ни за что!"

translate russian hypnosis_arrested_f0c6be92:

    "Мы с детективом средних лет начинаем бороться, катаясь по земле."

translate russian hypnosis_arrested_fc44699d:

    "Я бы даже сказал, что оно изменило мою жизнь, причём к лучшему!"

translate russian hypnosis_arrested_fd74c5d7:

    mike.say "Не подходите!"

translate russian hypnosis_arrested_fe8911ec:

    "Дальнейшее трудно назвать самым достойным моментом моей жизни."

translate russian hypnosis_package_1a4d9146:

    "И зачем, чёрт возьми, кто-то прислал мне это?"

translate russian hypnosis_package_32e9d253:

    "Но сегодня я как раз прохожу через прихожую, когда это происходит, и смотрю в сторону двери."

translate russian hypnosis_package_362fe411:

    "Мне даже не нужно читать подпись внизу, чтобы понять, что записка от отца."

translate russian hypnosis_package_4880db2e:

    "«Эта книга изменила мою жизнь. Уверен, она изменит и твою»."

translate russian hypnosis_package_48b2fb3a:

    "Зато на титульном листе написано: «Техники гипноза и месмеризма: полное руководство»."

translate russian hypnosis_package_6000c90e:

    "Но выглядит она довольно старой: кожаный переплёт заметно потрёпан временем."

translate russian hypnosis_package_6b83af6e:

    "Скорее всего, это книга для Саши или очередная безделушка, которые [bree.name] постоянно заказывает."

translate russian hypnosis_package_900b7e27:

    "На обложке книги нет названия."

translate russian hypnosis_package_9c422580:

    "Пока я листаю книгу, из неё выпадает записка и падает на пол."

translate russian hypnosis_package_a25138f4:

    "Отчасти моё любопытство вызвано тем, что среди писем я замечаю посылку."

translate russian hypnosis_package_b072328d:

    "Хм, всё-таки это книга."

translate russian hypnosis_package_bc2b3e79:

    "Но с каких пор он вообще интересуется гипнозом?"

translate russian hypnosis_package_ccfb1c7a:

    "Я подхожу, поднимаю её с коврика и гадаю, кому она может быть адресована."

translate russian hypnosis_package_cf7c88f2:

    "Но, взяв посылку, я с удивлением вижу, что она адресована мне!"

translate russian hypnosis_package_d2eeadda:

    "Я перелистываю пожелтевшие страницы и не замечаю ни пропавших, ни повреждённых."

translate russian hypnosis_package_db473a5e:

    "Обычно я не обращаю внимания на звук открывающейся почтовой щели и падающих на пол писем."

translate russian hypnosis_package_dee4f970:

    "Заинтригованный, я разрываю упаковку, чтобы посмотреть, что внутри."

translate russian hypnosis_package_ecf2608a:

    "А надпись на корешке выцвела настолько, что её уже невозможно разобрать."

translate russian hypnosis_package_f4039624:

    "Я наклоняюсь, чтобы поднять её, и почерк кажется мне знакомым."

translate russian hypnosis_package_f9b09fe0:

    "И всё же кто-то явно хорошо о ней заботился."

translate russian hypnosis_skill_book_2d1ea041:

    "Странно, но само изучение гипноза словно вводит в гипноз!"

translate russian hypnosis_skill_book_35bfd86f:

    "Но вскоре я уже читаю целые отрывки и по-настоящему увлекаюсь."

translate russian hypnosis_skill_book_38fe0259:

    "Я читаю в книге о гипнозе. ([skill]%%)"

translate russian hypnosis_skill_book_845185f7:

    "Я уже знаю о гипнозе всё, что мне нужно."

translate russian hypnosis_skill_book_f2243537:

    "Хм... Интересно, пробовал ли кто-нибудь использовать гипноз, чтобы знакомиться с девушками?"

translate russian hypnosis_skill_book_a04931a8:

    "Кажется, немного попрактиковавшись, я и сам смогу повторить кое-что из этого."

translate russian hypnosis_skill_book_d789833a:

    "Сначала я обращаю внимание только на то, что меня заинтересовало, например на любопытные схемы."

translate russian hypnosis_skill_book_e725d39a:

    "Заинтересовавшись, я начинаю понемногу читать книгу."

translate russian hypnosis_talk_84d7ab11:

    mike.say "Ты не против, если я с помощью гипноза немного изменю твоё поведение?"

translate russian hypnosis_talk_c5fe738d:

    mike.say "Эй, [active_girl.name], я хочу кое-что спросить..."

translate russian hypnosis_talk_cb439b46:

    active_girl.say "Ни за что!"

translate russian hypnosis_talk_e23253ba:

    active_girl.say "Конечно!"

translate russian introduce_sam_to_girls_1c0d45e8:

    mike.say "Ну..."

translate russian introduce_sam_to_girls_c0a1a7c9:

    mike.say "Заходи."

translate russian investigation_hire_pi_089a3222:

    "Кем этот тип меня считает?"

translate russian investigation_hire_pi_0aa52177:

    "Да, это один из тех случаев, когда жизнь вручает тебе лимоны."

translate russian investigation_hire_pi_0f430fe5:

    "Investigator" "Посмотрите и скажите, как вам."

translate russian investigation_hire_pi_1116852e:

    "На другом конце линии повисает пауза."

translate russian investigation_hire_pi_12a4e872:

    "Потому что снова оказался там же, откуда начал."

translate russian investigation_hire_pi_1a26cd68:

    "Investigator" "Вы их прочитаете, подпишете в нужном месте, а дальше оставите всё мне."

translate russian investigation_hire_pi_1df9158c:

    mike.say "И я совершенно невиновен!"

translate russian investigation_hire_pi_2059ebdd:

    mike.say "Но мне действительно нужна ваша помощь."

translate russian investigation_hire_pi_2262774c:

    "Я ставлю детектива на удержание, открываю сообщение и читаю."

translate russian investigation_hire_pi_25728e4b:

    "Голос на другом конце линии звучит серьёзно."

translate russian investigation_hire_pi_2610745c:

    "Investigator" "И посмотрите на это с другой стороны..."

translate russian investigation_hire_pi_289dadb9:

    "Investigator" "Если вы невиновны, работодатель будет обязан выплатить компенсацию."

translate russian investigation_hire_pi_2b2f0c8b:

    "Или то, что теперь я сижу без дела и могу лишь мрачно размышлять об этом."

translate russian investigation_hire_pi_2e3d9692:

    "И я слышу тяжёлый вздох собеседника."

translate russian investigation_hire_pi_32d3c411:

    "На мгновение мне кажется, что я ошибся номером."

translate russian investigation_hire_pi_3bafdd8f:

    mike.say "Меня обвиняют в краже денег у компании."

translate russian investigation_hire_pi_3c995d39:

    "Investigator" "Что ж, меня это, честно говоря, не касается, сэр."

translate russian investigation_hire_pi_41436be1:

    "Вместо того чтобы обидеться или разозлиться, детектив снова усмехается."

translate russian investigation_hire_pi_41fedb42:

    "Осознание того, что кто-то специально подставил меня за растрату."

translate russian investigation_hire_pi_43a80c2a:

    "Но останавливаюсь и задумываюсь об альтернативе."

translate russian investigation_hire_pi_44617681:

    "Я завершаю звонок, прежде чем скажу что-нибудь, о чём потом пожалею."

translate russian investigation_hire_pi_470a9236:

    "И с этими словами он завершает звонок."

translate russian investigation_hire_pi_49f66a1d:

    "Investigator" "Тогда, возможно, смогли бы позволить себе мои услуги!"

translate russian investigation_hire_pi_525e88dd:

    "На другом конце линии детектив усмехается."

translate russian investigation_hire_pi_53717e83:

    mike.say "У меня нет таких денег, просто валяющихся без дела!"

translate russian investigation_hire_pi_572b4916:

    "Investigator" "Сейчас пришлю вам сообщение с расценками."

translate russian investigation_hire_pi_58318cfa:

    "Investigator" "В любом случае вы можете позволить себе заплатить мне, чтобы я спас вашу задницу!"

translate russian investigation_hire_pi_5b00276c:

    "Кто бы это ни был, он, вероятно, уже думает, что это розыгрыш!"

translate russian investigation_hire_pi_5c026c96:

    "Но и подстава за растрату тоже."

translate russian investigation_hire_pi_5d08267a:

    mike.say "Вы недёшево берёте, мистер Пауэрс."

translate russian investigation_hire_pi_672f4aaf:

    "Прочитанная сумма словно бьёт меня под дых."

translate russian investigation_hire_pi_684e9f63:

    "Я уже собираюсь сказать детективу, куда он может засунуть свои услуги."

translate russian investigation_hire_pi_692df27e:

    "Investigator" "Ну, очень жаль, правда?"

translate russian investigation_hire_pi_abacec75:

    mike.say "О... точно!"

translate russian investigation_hire_pi_6fa17470:

    "Может, в такой ситуации не стоит переживать из-за цены?"

translate russian investigation_hire_pi_7653783b:

    "И уже через час у меня есть номер частного детектива, работающего прямо здесь, в городе."

translate russian investigation_hire_pi_7842248b:

    "Но всё же кажется, что я сделал положительный шаг."

translate russian investigation_hire_pi_7d8472d8:

    "Что меня успокаивает."

translate russian investigation_hire_pi_87f5a5a5:

    "Но в его словах есть смысл."

translate russian investigation_hire_pi_889802a8:

    mike.say "Упс..."

translate russian investigation_hire_pi_9270b0be:

    mike.say "Так что я вас нанимаю."

translate russian investigation_hire_pi_940d884c:

    "Но затем я понимаю, что ещё не сказал ни слова."

translate russian investigation_hire_pi_9737a379:

    "Если включится голосовая почта, по крайней мере смогу сказать, что попытался, верно?"

translate russian investigation_hire_pi_98732c28:

    mike.say "У меня проблемы на работе."

translate russian investigation_hire_pi_998bd07d:

    "Через мгновение телефон вибрирует, сообщая о новом сообщении."

translate russian investigation_hire_pi_9a803552:

    "Каким-то миллионером?!"

translate russian investigation_hire_pi_9aacf4c6:

    "Нужно лишь немного покопаться в интернете и сделать несколько запросов."

translate russian investigation_hire_pi_a7e0022e:

    "Investigator" "Это Джейк Пауэрс, частный детектив."

translate russian investigation_hire_pi_acb1e4dc:

    "Наём частного детектива всегда кажется чем-то из кино."

translate russian investigation_hire_pi_adc8012b:

    "Не знаю, что хуже всего в отстранении от работы."

translate russian investigation_hire_pi_ae27628d:

    "Investigator" "Алло?"

translate russian investigation_hire_pi_aeefdf45:

    "Остаётся надеяться, что этот парень действительно так хорош, как пишут в отзывах на его сайте!"

translate russian investigation_hire_pi_b15a114f:

    mike.say "Это частный сыщик?"

translate russian investigation_hire_pi_b92ce7db:

    "Я не чувствую, что с плеч свалился весь груз мира."

translate russian investigation_hire_pi_b9e0fb5f:

    "И как только вижу указанные цифры, мои глаза расширяются!"

translate russian investigation_hire_pi_b9ed6262:

    "Раздаётся несколько гудков, и я уже начинаю думать, что никто не ответит."

translate russian investigation_hire_pi_ba9e8b70:

    "Так, может, пора начать делать из них лимонад?"

translate russian investigation_hire_pi_baa48d44:

    "Investigator" "Хорошо, я свяжусь с вами."

translate russian investigation_hire_pi_bc249e75:

    "Возможно, всё это свободное время стоит использовать, чтобы дать отпор?"

translate russian investigation_hire_pi_bc5f81ca:

    "А затем раздражённо вздыхаю."

translate russian investigation_hire_pi_bdc63c99:

    "Investigator" "А если виновны, у вас уже есть куча грязных денег."

translate russian investigation_hire_pi_c9d60f60:

    mike.say "Нет, не о паре."

translate russian investigation_hire_pi_ca402494:

    "Investigator" "Так чем я могу вам помочь?"

translate russian investigation_hire_pi_d0a73e52:

    mike.say "И что теперь?"

translate russian investigation_hire_pi_d125cb8c:

    "Снова наступает короткая пауза."

translate russian investigation_hire_pi_d267715e:

    "Investigator" "И не называйте меня «частным членом», ладно?"

translate russian investigation_hire_pi_d7f66c9e:

    "Investigator" "Меня волнует только то, сможете ли вы оплатить мои услуги!"

translate russian investigation_hire_pi_d89e25b3:

    mike.say "Простите, мистер Пауэрс."

translate russian investigation_hire_pi_dab96c3d:

    "Но, возможно, я смотрю на ситуацию не с той стороны."

translate russian investigation_hire_pi_dbe5aec3:

    "Investigator" "В нашей профессии эта шутка очень быстро надоедает."

translate russian investigation_hire_pi_de081ba0:

    mike.say "Вы с ума сошли?"

translate russian investigation_hire_pi_de7aaa41:

    "Investigator" "Без проблем."

translate russian investigation_hire_pi_e029f549:

    "Я бы, конечно, выразился иначе."

translate russian investigation_hire_pi_e1207f89:

    "Я снимаю детектива с удержания и высказываю ему всё, что думаю."

translate russian investigation_hire_pi_e4bf5318:

    "Investigator" "Поверьте, вы получаете ровно то, за что платите!"

translate russian investigation_hire_pi_e4cdbe0b:

    mike.say "Для начала неплохо."

translate russian investigation_hire_pi_ee59108e:

    "Мне непривычно заниматься подобными вещами, поэтому перед звонком я колеблюсь."

translate russian investigation_hire_pi_f2f30017:

    "Investigator" "Теперь я пришлю вам документы."

translate russian investigation_hire_pi_f3c26b43:

    "Investigator" "Дайте угадаю: речь не о паре долларов тут и там?"

translate russian investigation_hire_pi_f4b6c206:

    mike.say "Речь идёт о серьёзной сумме."

translate russian investigation_hire_pi_f508571b:

    "Investigator" "Кто это?"

translate russian investigation_hire_pi_f8445efd:

    mike.say "Это..."

translate russian investigation_hire_pi_f8f0995e:

    "Investigator" "Вот если бы вы действительно украли деньги..."

translate russian investigation_hire_pi_fab6288c:

    "Investigator" "Как вам такой план?"

translate russian investigation_hire_pi_fd64e926:

    "Поэтому я отбрасываю сомнения и набираю номер."

translate russian investigation_hire_pi_fedf3148:

    "Но когда детектив заговорил вновь, его голос уже звучит спокойнее и профессиональнее."

translate russian investigation_skill_book_07acdbe1:

    "{i}«Разум начнёт играть с ними злую шутку: каждому будет казаться, что остальные его сдадут».{/i}"

translate russian investigation_skill_book_112c284a:

    "Я читаю в книге советы по ведению расследований. ([skill]%%)"

translate russian investigation_skill_book_16892be8:

    "Я уже знаю о расследованиях всё необходимое."

translate russian investigation_skill_book_1ffaac2a:

    "Хотя полиции было бы гораздо сложнее, если бы они могли безоговорочно доверять друг другу."

translate russian investigation_skill_book_29fadc95:

    "{i}«Получить сведения от подозреваемых проще, если надолго изолировать их друг от друга».{/i}"

translate russian investigation_skill_book_2dc88b4f:

    "{i}«Такое бывает редко, но дело может оказаться особенно сложным, если мы начинаем доверять тому, кому не следовало бы».{/i}"

translate russian investigation_skill_book_2f0f9599:

    "В этом есть смысл."

translate russian investigation_skill_book_3c4484d5:

    "{i}«Обнаружив труп, первым делом нужно тщательно осмотреть всё вокруг и найти орудие убийства».{/i}"

translate russian investigation_skill_book_50d2ae90:

    "Неудивительно, что люди хотят выбраться из такой ситуации, даже если ради этого приходится подставить сообщника."

translate russian investigation_skill_book_52cb6e70:

    "{i}«Запах выдал его в тот день, когда он плохо закрыл банку».{/i}"

translate russian investigation_skill_book_69bd2b78:

    "Невозможно найти такую маленькую вещь, как нож или пистолет, в лесу или в море."

translate russian investigation_skill_book_6a55f93c:

    "{i}«К счастью, этот психопат повсюду таскал рюкзак с банкой, в которой хранились большие пальцы ног его жертв».{/i}"

translate russian investigation_skill_book_6b6464c3:

    "Какого хрена вообще носить с собой такое?!"

translate russian investigation_skill_book_6bf3bd0f:

    "Пф-ф, будто я в это поверю!"

translate russian investigation_skill_book_74063518:

    "Мы и правда живём в больном мире..."

translate russian investigation_skill_book_76292a20:

    "Кажется, именно он снял «Криминальное чтиво»."

translate russian investigation_skill_book_850fde31:

    "{i}«Неважно, насколько велика территория: рано или поздно его найдут».{/i}"

translate russian investigation_skill_book_8cec5f48:

    "Это был какой-то старый режиссёр, помешанный на ступнях!"

translate russian investigation_skill_book_c1a62ec0:

    "{i}«Но он так активно помогал следствию, что мы невольно перестали его подозревать».{/i}"

translate russian investigation_skill_book_d47e4157:

    "{i}«Однажды у нас был парень, который, как и остальные, проходил подозреваемым...»{/i}"

translate russian investigation_skill_book_df6b72e5:

    "{i}«Когда все подозреваемые рассказывают одну и ту же версию, отделить правду от лжи помогает сложная полицейская работа».{/i}"

translate russian investigation_skill_book_e40f1f0c:

    "{i}«После этого достаточно немного надавить, чтобы в их рассказах появились первые несостыковки».{/i}"

translate russian investigation_skill_book_f31f93d0:

    "Погодите... я помню это дело!"

translate russian jealous_arrangement_889802a8:

    mike.say "Упс..."

translate russian jealous_threesome_920e7962:

    mike.say "А?!"

translate russian jealous_threesome_f1d8a63c:

    mike.say "Эм..."

translate russian jeff_in_the_pub_028e4ebc:

    "Но пока у меня есть лишь слова одного робкого бухгалтера."

translate russian jeff_in_the_pub_061af114:

    "Любой намёк на то, что он заметил моё предыдущее оскорбление, исчезает без следа."

translate russian jeff_in_the_pub_070fc915:

    "Мне нужны веские доказательства."

translate russian jeff_in_the_pub_08872e46:

    "Возможно, стоит изучить эту зацепку..."

translate russian jeff_in_the_pub_0941d826:

    "Но вижу, что это работает: Джефф покорно сдаётся."

translate russian jeff_in_the_pub_0a62f9d8:

    "Jeff" "Отстой, что они так с тобой поступают, [hero.name]."

translate russian jeff_in_the_pub_0bb0ce93:

    "Внутри не слишком людно, поэтому пробиваться к стойке не приходится."

translate russian jeff_in_the_pub_0bbbcfe5:

    mike.say "Говори конкретнее."

translate russian jeff_in_the_pub_0e4592e1:

    "Половина посетителей паба поворачивается в мою сторону."

translate russian jeff_in_the_pub_10d0616b:

    "Jeff" "Всегда оказываюсь там, когда такое случается!"

translate russian jeff_in_the_pub_120be04f:

    mike.say "Слушай, может, я угощу тебя ещё одной?"

translate russian jeff_in_the_pub_13e80e31:

    mike.say "Гораздо лучше скрыто, чем у большинства!"

translate russian jeff_in_the_pub_14463054:

    "С этими словами он залпом допивает свой напиток."

translate russian jeff_in_the_pub_17677020:

    "Jeff" "Ладно, [hero.name]..."

translate russian jeff_in_the_pub_18231b88:

    "А затем поворачивается, чтобы уйти..."

translate russian jeff_in_the_pub_19c94055:

    "Поначалу меньше всего мне хотелось выходить и встречаться с внешним миром."

translate russian jeff_in_the_pub_19da41b9:

    "И с размаху бью кулаком по стойке."

translate russian jeff_in_the_pub_1b5c41fa:

    "Jeff" "Большие начальники приказывают совершить что-то незаконное, и выбора у нас нет!"

translate russian jeff_in_the_pub_1bdf70a8:

    "Jeff" "Это всё конфиденциально!"

translate russian jeff_in_the_pub_2125592e:

    "Джефф не выложил всё начистоту."

translate russian jeff_in_the_pub_22234c02:

    "Всё это время я думаю, как лучше завести разговор об обвинениях против меня."

translate russian jeff_in_the_pub_23ff542e:

    "Услышав голос Джеффа, я удивлённо оборачиваюсь к нему."

translate russian jeff_in_the_pub_25129cdc:

    "Но достаточно крепче сжать пальцы, чтобы он передумал."

translate russian jeff_in_the_pub_2522743b:

    "Jeff" "Да, я на самой передовой."

translate russian jeff_in_the_pub_25310799:

    "Jeff" "Мне нужно идти..."

translate russian jeff_in_the_pub_ba8b637b:

    "Jeff" "Ну... вслух об этом никто не говорит."

translate russian jeff_in_the_pub_39dc687b:

    "Внезапно до Джеффа доходит, что он сболтнул лишнее."

translate russian jeff_in_the_pub_3b4ccd99:

    "Но, привлекая внимание бармена и заказывая выпивку, я замечаю знакомое лицо."

translate russian jeff_in_the_pub_3c0c60d3:

    "Jeff" "Полагаю, во мне скрыто немало неожиданного!"

translate russian jeff_in_the_pub_3d4e26d1:

    "Мысли уже лихорадочно крутятся вокруг того, что к делу причастен Дуэйн."

translate russian jeff_in_the_pub_3db6a641:

    "Поэтому неудивительно, что он спешит ко мне, даже зная, что я отстранён."

translate russian jeff_in_the_pub_3dd5560c:

    mike.say "Привет, Джефф!"

translate russian jeff_in_the_pub_41325f8b:

    "Меньше всего сейчас нужно ещё и обвинение в нападении!"

translate russian jeff_in_the_pub_443ef2fd:

    "Когда ещё бухгалтеру удаётся собрать вокруг себя слушателей?"

translate russian jeff_in_the_pub_448e1c92:

    "Jeff" "Погоди-ка..."

translate russian jeff_in_the_pub_44f96725:

    "Но, возможно, встреча не была совершенно бесполезной."

translate russian jeff_in_the_pub_3f17b2b4:

    "Jeff" "Л... ладно... ладно..."

translate russian jeff_in_the_pub_45a714ba:

    "Jeff" "Но когда мой начальник сказал, что мы расследуем тебя..."

translate russian jeff_in_the_pub_47ce5fd7:

    "Jeff" "Точно не знаю."

translate russian jeff_in_the_pub_49c602ae:

    "Теперь он уже не притворяется, и нервозность становится очевидной!"

translate russian jeff_in_the_pub_4de6a4c0:

    "Услышав это, я не могу сдержать эмоций."

translate russian jeff_in_the_pub_4ec9f437:

    "Каждый раз, когда я видел Джеффа и общался с ним, он был неловким и нервным."

translate russian jeff_in_the_pub_52273058:

    "С этими словами он поспешно убегает через весь паб."

translate russian jeff_in_the_pub_525bdf17:

    "Jeff" "Я останусь, [hero.name]."

translate russian jeff_in_the_pub_53d4e6a8:

    "Он смотрит сначала на мою руку, затем на меня."

translate russian jeff_in_the_pub_5408c8b4:

    "Но вон там определённо сидит Джефф из бухгалтерии."

translate russian jeff_in_the_pub_55954f9e:

    "Звучит жестоко, но он почти карикатурный бухгалтер."

translate russian jeff_in_the_pub_5bf2b52e:

    mike.say "Ничего, совсем ничего..."

translate russian jeff_in_the_pub_5d239141:

    "Я думаю попытаться его остановить."

translate russian jeff_in_the_pub_5dd65597:

    mike.say "Такое уже случалось раньше?"

translate russian jeff_in_the_pub_5ec7708d:

    "Я привлекаю внимание Джеффа и машу ему, приглашая присоединиться ко мне у стойки."

translate russian jeff_in_the_pub_6304dd0c:

    "Я почти не замечаю, что Джефф ушёл."

translate russian jeff_in_the_pub_65b70baf:

    "Я вижу, что он подумывает позвать на помощь."

translate russian jeff_in_the_pub_699e1359:

    "Он явно рад меня видеть и охотно принимает оказываемое ему внимание."

translate russian jeff_in_the_pub_6cd8d781:

    "Понятно, что ему ужасно нравится возможность поговорить об этом."

translate russian jeff_in_the_pub_6fa5dc50:

    "Jeff" "Да, да..."

translate russian jeff_in_the_pub_c1e1f04d:

    "Jeff" "Ну... кажется, за минуту до этого я слышал, как он разговаривал с Дуэйном!"

translate russian jeff_in_the_pub_71de33ad:

    "Я долго вздыхаю и качаю головой."

translate russian jeff_in_the_pub_73d6687d:

    "Любой другой коллега сейчас относился бы ко мне как к прокажённому!"

translate russian jeff_in_the_pub_77277b8b:

    "Но затем отбрасываю эту мысль и просто смотрю, как он уходит."

translate russian jeff_in_the_pub_7894b0cc:

    mike.say "И часто?"

translate russian jeff_in_the_pub_f25705c6:

    "Jeff" "Э... эй..."

translate russian jeff_in_the_pub_7ee18fe5:

    mike.say "А, да, это..."

translate russian jeff_in_the_pub_8014e5e5:

    "Хотя, признаться, понятия не имею, была ли это вообще шутка."

translate russian jeff_in_the_pub_0d7376ba:

    "Jeff" "Ну... эта растрата и всё такое."

translate russian jeff_in_the_pub_814fcc30:

    "Не успев подумать, я выбрасываю руку вперёд."

translate russian jeff_in_the_pub_8410ea0c:

    "Но затем Джефф сам открывает рот и выпаливает всё напрямую."

translate russian jeff_in_the_pub_84582d45:

    "Jeff" "Уже недолго!"

translate russian jeff_in_the_pub_8af24f5b:

    "Я моргаю, а затем качаю головой."

translate russian jeff_in_the_pub_90d00a9b:

    "Jeff" "А, да, [hero.name]."

translate russian jeff_in_the_pub_91ae929e:

    "С улыбкой я отпускаю запястье Джеффа."

translate russian jeff_in_the_pub_920e7962:

    mike.say "А?!"

translate russian jeff_in_the_pub_93c1bcb2:

    "И в этот момент мне приходит идея."

translate russian jeff_in_the_pub_97faf632:

    "Jeff" "Мне ещё одну такую же."

translate russian jeff_in_the_pub_9868b71e:

    "Jeff" "Ну..."

translate russian jeff_in_the_pub_9a876083:

    "И поэтому снова и снова прокручиваю в голове одно и то же, постепенно сходя с ума."

translate russian jeff_in_the_pub_9ce48bc4:

    "Джефф кивает, теперь уже охотно готовый всё выложить после моей угрозы."

translate russian jeff_in_the_pub_9d2a5e17:

    "Но я уже чувствую, что теряю рассудок, поэтому заставляю себя выйти из дома."

translate russian jeff_in_the_pub_9dac9464:

    "Джефф кивает, стараясь придать себе философский вид."

translate russian jeff_in_the_pub_9dca569e:

    mike.say "Ты собирался рассказать, часто ли такое происходит, верно?"

translate russian jeff_in_the_pub_a0295e8e:

    mike.say "Никогда бы не подумал, что встречу тебя здесь!"

translate russian jeff_in_the_pub_a24d3424:

    "Я наклоняюсь ближе и смотрю Джеффу прямо в глаза."

translate russian jeff_in_the_pub_a3a2b98c:

    mike.say "Слишком много расплывчатой херни, Джефф."

translate russian jeff_in_the_pub_a4f07215:

    mike.say "Дуэйн..."

translate russian jeff_in_the_pub_a5c6de54:

    "Я нарочито смеюсь над словами Джеффа."

translate russian jeff_in_the_pub_ab61a196:

    "Jeff" "О, спасибо, [hero.name]!"

translate russian jeff_in_the_pub_adc1f1ce:

    "Jeff" "И это означает, что нам нужно смотреть в другую сторону."

translate russian jeff_in_the_pub_ae4293cf:

    "Jeff" "Я не говорил, что это он!"

translate russian jeff_in_the_pub_b1871a8b:

    "Можно ещё угостить его выпивкой в надежде развязать язык!"

translate russian jeff_in_the_pub_b19e3eaa:

    "Стараюсь выглядеть так, будто совершенно не хочу это обсуждать."

translate russian jeff_in_the_pub_953c79f7:

    "Jeff" "Эм... нет... я..."

translate russian jeff_in_the_pub_b40fe001:

    "Или хотя бы что-нибудь, чем можно шантажом заставить Дуэйна прекратить расследование!"

translate russian jeff_in_the_pub_b4380161:

    "За время работы на нынешней должности я пару раз разговаривал с Джеффом."

translate russian jeff_in_the_pub_b61ec302:

    "Наверное, временно утопить печаль в алкоголе не самая плохая идея."

translate russian jeff_in_the_pub_b63b03ad:

    "Сейчас я чувствую себя школьным хулиганом и стыжусь того, что прибегаю к грубой силе."

translate russian jeff_in_the_pub_b7205425:

    mike.say "А, точно, вспомнил!"

translate russian jeff_in_the_pub_b8b9bae5:

    "При упоминании бесплатной выпивки Джефф моментально меняет тон."

translate russian jeff_in_the_pub_bd7dbe1e:

    "Jeff" "Только не делай мне больно, хорошо?"

translate russian jeff_in_the_pub_bdfa7802:

    "Однако всё же проговорился, что это не единичный случай."

translate russian jeff_in_the_pub_c1d82f44:

    "Jeff" "Иногда нам велят делать то, что, как мы понимаем, нарушает правила."

translate russian jeff_in_the_pub_c3558668:

    "Для большего эффекта даже разглаживаю его рукав."

translate russian jeff_in_the_pub_c4886eee:

    "Нужно упомянуть их как бы невзначай, зайти с другой стороны."

translate russian jeff_in_the_pub_c51dc2ac:

    "Jeff" "Хм..."

translate russian jeff_in_the_pub_c5a6b5fc:

    mike.say "Так на чём мы остановились?"

translate russian jeff_in_the_pub_c6089ba9:

    "У меня и без того достаточно проблем."

translate russian jeff_in_the_pub_d19de0f8:

    "Может, получится вытянуть из него внутреннюю информацию?"

translate russian jeff_in_the_pub_d40193b2:

    "Я киваю бармену и оплачиваю Джеффу следующий напиток."

translate russian jeff_in_the_pub_58de625d:

    "Jeff" "Но иногда мы получаем приказы... сверху."

translate russian jeff_in_the_pub_d49caa03:

    "Мне нужно отвлечься от расследования и от того, что меня, как я знаю, подставили."

translate russian jeff_in_the_pub_d63e1307:

    mike.say "Надо было сразу понять, что это он!"

translate russian jeff_in_the_pub_d889d51e:

    mike.say "Куда ты собрался, Джефф?"

translate russian jeff_in_the_pub_daef4335:

    "А Джефф от испуга едва не обделывается."

translate russian jeff_in_the_pub_ddbbff09:

    "Я хватаю Джеффа за запястье и не даю ему уйти."

translate russian jeff_in_the_pub_e0bef632:

    mike.say "Что ты имеешь в виду, Джефф?"

translate russian jeff_in_the_pub_e33f9c48:

    "Он действительно сказал то, что мне послышалось?"

translate russian jeff_in_the_pub_e62d367e:

    "Я понятия не имею, куда иду, пока не поднимаю взгляд и не обнаруживаю себя у «Винчестера»."

translate russian jeff_in_the_pub_e870f8e3:

    mike.say "А в моём случае, Джефф?"

translate russian jeff_in_the_pub_edbb788c:

    "Мало кто с работы пьёт здесь, ведь паб находится почти в пригороде."

translate russian jeff_in_the_pub_ededba72:

    "Что странно, ведь раньше я ни о чём подобном не слышал."

translate russian jeff_in_the_pub_f35e08b6:

    mike.say "Мы ещё не закончили нашу маленькую беседу!"

translate russian jeff_in_the_pub_f4422187:

    "Оглянувшись, я пожимаю плечами и решаю зайти выпить."

translate russian jeff_in_the_pub_f58e377e:

    "Он наверняка знает что-нибудь о том компромате, который компания собрала на меня."

translate russian jeff_in_the_pub_f6af96bc:

    "Jeff" "Что это значит?"

translate russian jeff_in_the_pub_f8f8e65f:

    mike.say "Ты всё ещё здесь?"

translate russian jeff_in_the_pub_f928f78e:

    mike.say "Наверное, ты знаешь об этом всё, да?"

translate russian jeff_in_the_pub_faa0bd93:

    "Недостаточно, чтобы считать его другом, но вполне достаточно, чтобы поздороваться."

translate russian jeff_in_the_pub_fae370a5:

    "Похоже, ради желаемого он не гнушается нарушать правила."

translate russian jeff_in_the_pub_fd7888fa:

    mike.say "О каком большом начальнике идёт речь?"

translate russian jeff_in_the_pub_ff3880b0:

    "После отстранения от работы я почти всё время торчу дома."

translate russian kart_with_231de2c9:

    active_girl.say "Прости, мне сейчас не хочется."

translate russian kart_with_24e2a451:

    "Я участвую в гонке с [active_girl.name]."

translate russian kart_with_b778778c:

    active_girl.say "Конечно, почему бы и нет?"

translate russian karting_solo_5d9524ae:

    "Я отлично провожу время, гоняя по трассе!"

translate russian kiara_special_coffee_0304d9b3:

    "Что довольно трудно, потому что почти всё в ней имеет явный сексуальный подтекст."

translate russian kiara_special_coffee_08fdc6df:

    kiara.say "Я точно знаю, что тебе нужно. Идём со мной в подсобку."

translate russian kiara_special_coffee_09378a6d:

    mike.say "Выбирать значит отказываться, как говорится."

translate russian kiara_special_coffee_15392d4f:

    "Я замечаю разочарование в глазах Киары."

translate russian kiara_special_coffee_1551449f:

    kiara.say "Эти брюки ТАК тебя обтягивают."

translate russian kiara_special_coffee_165931aa:

    "Но я вынужден подавлять это желание, боясь выдать нас."

translate russian kiara_special_coffee_18ff4194:

    mike.say "Мне тоже приятно видеть себя... то есть тебя..."

translate russian kiara_special_coffee_24557062:

    "А то, что она делает это в таком месте... Что, если кто-нибудь откроет дверь?"

translate russian kiara_special_coffee_2c7edecc:

    "Но каждый раз они удаляются."

translate russian kiara_special_coffee_2ca6dc4f:

    kiara.say "Ты уже сделал заказ?"

translate russian kiara_special_coffee_30ef6280:

    kiara.say "Надеюсь, тебе понравилось это особое угощение."

translate russian kiara_special_coffee_342b110f:

    kiara.say "М-м-м..."

translate russian kiara_special_coffee_442254bc:

    "К этому моменту она уже расстегнула мою ширинку."

translate russian kiara_special_coffee_45394c92:

    "И она именно это и делает."

translate russian kiara_special_coffee_4993ac3c:

    kiara.say "Как же я рада снова тебя видеть."

translate russian kiara_special_coffee_5420c2fa:

    "Какова бы ни была причина, Киара принимает это совершенно спокойно."

translate russian kiara_special_coffee_5499545d:

    "Я заказываю кофе и тоже ухожу."

translate russian kiara_special_coffee_5769dbd3:

    "После этого я поспешно выхожу из кафе, уже пытаясь привести мысли в порядок."

translate russian kiara_special_coffee_5c042ee9:

    kiara.say "Может, ещё как-нибудь увидимся."

translate russian kiara_special_coffee_6f149b06:

    kiara.say "А, [hero.name]."

translate russian kiara_special_coffee_71730a5d:

    "И она уходит."

translate russian kiara_special_coffee_7b1f4fb7:

    "Она потрясающая женщина с телом, за которое можно умереть."

translate russian kiara_special_coffee_7bbdab80:

    "Киара начинает с поцелуев головки моего члена."

translate russian kiara_special_coffee_7cf3eedf:

    kiara.say "Но я поняла, что хочу попробовать это, в тот же миг, когда увидела."

translate russian kiara_special_coffee_7de47b03:

    "А затем начинает медленно брать его в рот, дюйм за дюймом."

translate russian kiara_special_coffee_8371d11e:

    mike.say "В общем, привет!"

translate russian kiara_special_coffee_9748f8bb:

    kiara.say "Взять его в рот — только об этом я и могла думать!"

translate russian kiara_special_coffee_9ac0e650:

    kiara.say "Я вижу каждую мелочь, [hero.name]."

translate russian kiara_special_coffee_9bd052dd:

    "В глазах Киары вспыхивает огонёк."

translate russian kiara_special_coffee_9c953ce9:

    "Я смотрю, как она невозмутимо встаёт и убирает мой член обратно в брюки."

translate russian kiara_special_coffee_a6f0d63d:

    "Дверь едва успевает закрыться, а Киара уже стоит передо мной на коленях и тянется к ширинке."

translate russian kiara_special_coffee_ab2de3dd:

    "Она не торопится и всё время смотрит на меня снизу вверх."

translate russian kiara_special_coffee_aefce0ce:

    kiara.say "Очень жаль. Тогда приятного кофе."

translate russian kiara_special_coffee_1a3f4f16:

    mike.say "Д... да..."

translate russian kiara_special_coffee_b28f1508:

    mike.say "Скажем так, ты меня более чем заинтриговала. Идём."

translate russian kiara_special_coffee_b4acb381:

    mike.say "Ещё нет. Мне здесь всё нравится."

translate russian kiara_special_coffee_b5044ffe:

    "Одного ощущения опасности более чем достаточно, чтобы мой член стал твёрдым как камень."

translate russian kiara_special_coffee_b7a4932e:

    "Она хороша, но страх быть пойманными делает ощущения гораздо ярче."

translate russian kiara_special_coffee_c3fd6adf:

    kiara.say "Будто ты всё это время специально меня дразнил!"

translate russian kiara_special_coffee_c48c069c:

    "Несколько раз я слышу голоса, приближающиеся к двери."

translate russian kiara_special_coffee_d32cb272:

    "Киара запрокидывает голову и искренне, от души смеётся над моим сбивчивым ответом."

translate russian kiara_special_coffee_d3bdb1a8:

    "Она едва вздрагивает, когда я кончаю ей в рот."

translate russian kiara_special_coffee_dc2e2367:

    "Каждую секунду, пока мой член у неё во рту, мне хочется застонать и закричать."

translate russian kiara_special_coffee_e100c543:

    "Я улыбаюсь Киаре, изо всех сил стараясь не подать ей неверный сигнал."

translate russian kiara_special_coffee_e333985e:

    "Возможно, именно облегчение заставляет меня кончить уже через секунду."

translate russian kiara_special_coffee_f1458534:

    "Я стою, погружённый в свои мысли, и пытаюсь решить, что заказать сегодня."

translate russian kiara_special_coffee_f4d648a6:

    "Когда Киара наконец заглатывает мой член на всю длину, я уже почти не дышу."

translate russian kiara_special_coffee_f6eb1f7d:

    "И её пальцы проникают внутрь..."

translate russian kiara_special_coffee_f9c5b437:

    "Я бы солгал, сказав, что ещё не возбуждён."

translate russian kiara_special_coffee_fec235f1:

    mike.say "Спасибо, но, пожалуй, я возьму старый добрый чёрный кофе."

translate russian kiss_her_122e26d7:

    "Глядя на неё, я вижу, как в её выражении смешались удивление и удовольствие."

translate russian kiss_her_355250eb:

    "Спустя, казалось бы, целую вечность мы отстраняемся друг от друга, тяжело дыша..."

translate russian kiss_her_3f2a3fdd:

    active_girl.say "Больше никогда так не делай."

translate russian kiss_her_75778827:

    "Когда наши губы соприкасаются, по моей спине пробегает дрожь..."

translate russian kiss_her_784c782d:

    "[active_girl.name] страстно целует меня."

translate russian kiss_her_8e94ad91:

    active_girl.say "Такое чувство, будто я слишком долго ждала этого поцелуя.\nНадеюсь, он будет не последним."

translate russian kiss_her_988307f7:

    "[active_girl.name] нежно целует меня."

translate russian kiss_her_c3c7c04c:

    "Сказав это, она разворачивается и уходит."

translate russian kiss_her_c84672aa:

    "Пьянящий аромат цветов и вкус черники придают нашему первому поцелую особое ощущение..."

translate russian kiss_her_cec36c11:

    "[active_girl.name] отталкивает меня."

translate russian kiss_her_d9e138e1:

    "[active_girl.name] обхватывает меня за шею и запускает свой влажный язык мне в рот."

translate russian kleio_morgan_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian kleio_morgan_propose_male_be946dca:

    mike.say "Эм... да..."

translate russian kleio_sasha_propose_male_1c0d45e8:

    mike.say "Ну..."

translate russian kleio_sasha_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian kleio_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian kleio_sasha_propose_male_c155a10d:

    mike.say "Эй..."

translate russian kleio_sasha_propose_male_f1d8a63c:

    mike.say "Эм..."

translate russian knock_bathroom_102d055b:

    "Я вижу, как Лекси и Саша вместе принимают ванну..."

translate russian knock_bathroom_26cb21fe:

    "Я вижу, как Саманта и Минами вместе принимают ванну..."

translate russian knock_bathroom_38a7c703:

    "Я вижу, как Саманта и Минами вместе принимают душ..."

translate russian knock_bathroom_4b3ea422:

    "Я вижу, как [mike.name] и Саша вместе принимают ванну..."

translate russian knock_bathroom_4bfbc7d4:

    "Я вижу, как Саманта и Саша вместе принимают ванну..."

translate russian knock_bathroom_5b3fcc70:

    "Я вижу, как [mike.name] принимает ванну..."

translate russian knock_bathroom_62ce154d:

    "Я вижу, как Лекси и Минами вместе принимают ванну..."

translate russian knock_bathroom_7e37afd9:

    "Я вижу, как [bree.name] и Минами вместе принимают ванну..."

translate russian knock_bathroom_894c5f1a:

    "Какие же они милые!"

translate russian knock_bathroom_894c5f1a_1:

    "Какие же они милые!"

translate russian knock_bathroom_894c5f1a_2:

    "Какие же они милые!"

translate russian knock_bathroom_894c5f1a_3:

    "Какие же они милые!"

translate russian knock_bathroom_894c5f1a_4:

    "Какие же они милые!"

translate russian knock_bathroom_894c5f1a_5:

    "Какие же они милые!"

translate russian knock_bathroom_894c5f1a_6:

    "Какие же они милые!"

translate russian knock_bathroom_894c5f1a_7:

    "Какие же они милые!"

translate russian knock_bathroom_894c5f1a_8:

    "Какие же они милые!"

translate russian knock_bathroom_894c5f1a_9:

    "Какие же они милые!"

translate russian knock_bathroom_b7795948:

    "Я вижу, как [bree.name] и Саша вместе принимают ванну..."

translate russian knock_bathroom_ba10adc5:

    "Она такая красивая."

translate russian knock_bathroom_cd78d140:

    "Я вижу, как [girl.name] принимает душ..."

translate russian knock_bathroom_f06d96f4:

    "Я вижу, как Лекси и Саша вместе принимают душ..."

translate russian knock_bathroom_f261106f:

    "Какой же он милый!"

translate russian knock_bathroom_ff2116f9:

    "Я вижу, как Лекси и Минами вместе принимают душ..."

translate russian lapdance_dca65c35:

    "Мне танцуют приватный танец..."

translate russian lavish_shiori_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian lavish_shiori_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian lavish_shiori_propose_male_1c0d45e8:

    mike.say "Ну..."

translate russian lavish_shiori_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian lavish_shiori_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian lexi_caught_peeping_male_01bb63a2:

    lexi.say "И что же тут у нас?"

translate russian lexi_caught_peeping_male_042c3eac:

    lexi.say "Будешь пускать слюни в щель двери каждый раз, когда я принимаю душ?"

translate russian lexi_caught_peeping_male_1472d5cb:

    lexi.say "И тогда посмотрим, понравится ли им жить с подглядывающим извращенцем!"

translate russian lexi_caught_peeping_male_31fe67e9:

    "Я перебираю в голове все эти отговорки и оправдания."

translate russian lexi_caught_peeping_male_375084ef:

    "Я всего лишь быстро загляну внутрь."

translate russian lexi_caught_peeping_male_42088b24:

    "Поэтому сам не замечаю, как крадусь к двери ванной."

translate russian lexi_caught_peeping_male_48dae388:

    lexi.say "А когда я хожу по-маленькому или по-большому?"

translate russian lexi_caught_peeping_male_4eea4c79:

    "Она стоит всего в нескольких футах от меня."

translate russian lexi_caught_peeping_male_504a8e2b:

    lexi.say "И что?"

translate russian lexi_caught_peeping_male_51c6cda0:

    "Одна из девушек могла оставить душ включённым и уйти за какой-нибудь вещью."

translate russian lexi_caught_peeping_male_57e3efb6:

    mike.say "Как дела, Лекси!"

translate russian lexi_caught_peeping_male_5bc84c43:

    lexi.say "Послушай, [hero.name], в этот раз я закрою глаза, хорошо?"

translate russian lexi_caught_peeping_male_5edd3c68:

    "Но насколько я помню, к таким я не отношусь!"

translate russian lexi_caught_peeping_male_6270e0db:

    "Лекси обрывает меня, прежде чем я успеваю придумать оправдание."

translate russian lexi_caught_peeping_male_683b3ff6:

    mike.say "Обычно я такими вещами не занимаюсь."

translate russian lexi_caught_peeping_male_6b04d1aa:

    lexi.say "За этим тоже собираешься наблюдать?"

translate russian lexi_caught_peeping_male_6cced978:

    lexi.say "Но если снова поймаю, расскажу остальным девушкам."

translate russian lexi_caught_peeping_male_7219a247:

    "И на её лице играет насмешливая улыбка."

translate russian lexi_caught_peeping_male_752d5d05:

    "Да-да, знаю. Следовало просто пожать плечами и пройти дальше."

translate russian lexi_caught_peeping_male_78ff7265:

    lexi.say "Ну-ну-ну..."

translate russian lexi_caught_peeping_male_86c9e633:

    "Услышав голос Лекси, я подскакиваю и едва не отшатываюсь от двери ванной."

translate russian lexi_caught_peeping_male_89cbd87f:

    "Именно так поступил бы в этой ситуации зрелый, уравновешенный взрослый."

translate russian lexi_caught_peeping_male_904a4db5:

    lexi.say "Крался как мерзкий маленький извращенец со стояком!"

translate russian lexi_caught_peeping_male_9bf0ae0b:

    "С их помощью заглушаю совесть, наклоняясь к щели в двери."

translate russian lexi_caught_peeping_male_9eca68af:

    "Поэтому слышу и шум льющейся внутри воды."

translate russian lexi_caught_peeping_male_a4c0ea65:

    "К тому же внутри вообще может никого не быть."

translate russian lexi_caught_peeping_male_988f9956:

    mike.say "Ч... что..."

translate russian lexi_caught_peeping_male_cb0c733e:

    mike.say "Да ладно тебе, Лекси!"

translate russian lexi_caught_peeping_male_d7f8f2fb:

    lexi.say "Ты ведь подсматривал за тем, кто там принимает душ, верно?"

translate russian lexi_caught_peeping_male_e078aa2b:

    lexi.say "Ты извращенец только по особым случаям?"

translate russian lexi_caught_peeping_male_ff9c4c30:

    mike.say "Я... я просто..."

translate russian lexi_caught_peeping_male_e8ca341b:

    "С этими словами Лекси уверенно уходит."

translate russian lexi_caught_peeping_male_eaa853d8:

    "Но если совесть не смогла меня остановить, то следующий звук точно сможет..."

translate russian lexi_caught_peeping_male_f1ca9f69:

    lexi.say "Это часть сделки за то, что ты разрешил мне здесь пожить, [hero.name]?"

translate russian lexi_caught_peeping_male_f583ef3d:

    "Я ведь не собираюсь снимать происходящее на телефон или делать что-нибудь настолько мерзкое."

translate russian lexi_caught_peeping_male_f8892766:

    "Проходя мимо, я замечаю, что дверь ванной оставили открытой."

translate russian lexi_caught_peeping_male_ff41fe01:

    "Она качает головой, отметая мои попытки прикинуться невиновным."

translate russian lexi_event_01_59cbd0df:

    thug_say "Простите, сэр, я вас не узнал."

translate russian lexi_minami_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian lexi_minami_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian lexi_minami_samantha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian lexi_minami_samantha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian lexi_minami_samantha_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian lexi_minami_samantha_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian lexi_minami_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian lexi_minami_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian lexi_moving_in_be946dca:

    mike.say "Эм... да..."

translate russian lexi_moving_in_30e74fc5:

    mike.say "Эм..."

translate russian lexi_moving_in_a2dd5d3e:

    mike.say "Не знаю, о чём я думал."

translate russian lexi_moving_in_f1d8a63c:

    mike.say "Эм..."

translate russian lexi_samantha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian lexi_samantha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian lexi_samantha_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian lexi_samantha_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian lexi_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian lexi_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian lexi_sasha_threesome_intro_200eb25b:

    mike.say "Эй!"

translate russian lexi_sasha_threesome_intro_200eb25b_1:

    mike.say "Эй!"

translate russian lexi_sasha_threesome_intro_4dda1c6b:

    mike.say "Что..."

translate russian lexi_sasha_threesome_intro_4dda1c6b_1:

    mike.say "Что..."

translate russian livingroom_masturbate_male_ca2fbdc8:

    "М-м-м, как же приятно."

translate russian livingroom_masturbate_male_eac2e61d:

    "Я решаю немного развлечься в одиночестве."

translate russian maidcafe_order_147f6b0a:

    mike.say "Мне, пожалуйста, кофе."

translate russian maidcafe_order_151a34ab:

    bree.say "Вот, держи, [hero.name]!"

translate russian maidcafe_order_44d7ea9c:

    bree.say "Как пожелаешь, [hero.name]."

translate russian maidcafe_order_5aca3d8a:

    mike.say "Мне, пожалуйста, мокко."

translate russian maidcafe_order_94a1df80:

    bree.say "Принесу в мгновение ока."

translate russian maidcafe_order_c27b5894:

    bree.say "Что тебе принести, [hero.name]?"

translate russian maidcafe_order_db9e8e50:

    mike.say "Мне, пожалуйста, какао."

translate russian maidcafe_order_eee62860:

    bree.say "Сейчас будет."

translate russian maidcafe_welcome_7a9e41c5:

    bree.say "Добро пожаловать, [hero.name]."

translate russian male_intro_7646cc1e:

    mike.say "Взаимно."

translate russian male_intro_7bc80586:

    mike.say "Алло?"

translate russian massage_152fa069:

    "Я делаю массаж [active_girl.name]."

translate russian massage_skill_book_1ef0ee66:

    "Я уже знаю о массаже всё необходимое."

translate russian massage_skill_book_7fa9a00c:

    "Я читаю в книге о массаже. ([skill]%%)"

translate russian meet_d2966bf5:

    "Я встречаю на улице [interact_girl.name]."

translate russian meet_ede278fe:

    interact_girl.say "До встречи, [hero.name]."

translate russian meet_the_master_male_000fa685:

    "Пока я отплёвываюсь и кашляю с полным ртом песка, сидящие ближе всего девушки не могут удержаться от смеха при виде моего несчастья."

translate russian meet_the_master_male_0e4834c6:

    "Старик отмахивается от моего объяснения."

translate russian meet_the_master_male_0f09ef8c:

    "Разумеется, из-за прекрасной погоды к моему приходу здесь уже полно людей, и мне приходится пробираться хотя бы на сотню футов ближе к воде."

translate russian meet_the_master_male_0f7bfc7c:

    mike.say "А не сидящими в пляжных дюнах, где можно глазеть на полуобнажённых девушек и спокойно дрочить, оставаясь незамеченным!"

translate russian meet_the_master_male_12fc191f:

    "Old pervert" "Именно так. Я видел, как те накачанные хулиганы сбили тебя с ног и швырнули задницей в песок."

translate russian meet_the_master_male_2144e675:

    mike.say "Я уже ходил на занятия по самообороне в спортзале..."

translate russian meet_the_master_male_24108975:

    "Но когда я подхожу к дюнам на краю пляжа, слышу, как кто-то зовёт меня."

translate russian meet_the_master_male_24e4114f:

    master.say "Встреть меня здесь, когда будешь готов, мой мальчик, и мы начнём!"

translate russian meet_the_master_male_25417e82:

    master.say "Больше никто никогда не пнёт тебе песок в лицо!"

translate russian meet_the_master_male_2551b8b3:

    "Старик хохочет и качает головой в ответ на мои слова."

translate russian meet_the_master_male_25a79970:

    "Он снова заставляет меня замолчать взмахом руки."

translate russian meet_the_master_male_2a7651db:

    "Стоит мне приблизиться на несколько шагов, как старик выскакивает из дюн и начинает разглядывать меня с головы до ног."

translate russian meet_the_master_male_2b29a167:

    master.say "Но не беспокойся о деньгах. Есть вещи важнее таких мелочных материальных забот."

translate russian meet_the_master_male_2ccb0e0e:

    "В сущности, никто не виноват. Я просто отступаю в сторону, пропуская двух настоящих качков, наступаю на что-то и растягиваюсь лицом в песке."

translate russian meet_the_master_male_39b2398a:

    master.say "Не глупи, мой мальчик. Такая возможность выпадает раз в жизни!"

translate russian meet_the_master_male_3a5641c5:

    "С этими словами он разворачивается и снова исчезает среди дюн."

translate russian meet_the_master_male_41e7de19:

    "Старик выглядит искренне ошеломлённым, вероятно, потому что привык, что доверчивые идиоты ведутся на его речи."

translate russian meet_the_master_male_4515949b:

    "Old pervert" "Да, я тебя зову, парень. Иди сюда!"

translate russian meet_the_master_male_49680255:

    "Он делает паузу, слегка покашливает и продолжает."

translate russian meet_the_master_male_4fbe4f43:

    mike.say "Вообще-то я вроде как сам упал..."

translate russian meet_the_master_male_56529444:

    "Часть меня сомневается в его словах, но разве фильмы не полны мастеров боевых искусств, которые ведут совершенно обычную и скучную жизнь?"

translate russian meet_the_master_male_5b1d09d5:

    "Обычно я не провожу много свободного времени на пляже, но сегодня погода настолько хороша, что я не смог устоять."

translate russian meet_the_master_male_5b6ea45b:

    mike.say "Вообще-то я и сам посмеялся вместе с ними..."

translate russian meet_the_master_male_60c5df85:

    master.say "Всего за весьма разумную плату в сто долларов за урок..."

translate russian meet_the_master_male_67b0df06:

    "Я всё ещё слышу его протесты, когда огибаю изгиб пляжа и оставляю его позади."

translate russian meet_the_master_male_68c52402:

    "Old pervert" "Я говорю о древних боевых искусствах, сынок!"

translate russian meet_the_master_male_6bba887c:

    "Заинтересовавшись тем, что хочет сказать странный старик, я подхожу к нему."

translate russian meet_the_master_male_6c6fbc02:

    "По моим собственным оценкам, всё идёт довольно неплохо, пока судьба не решает унизить меня перед всей пляжной толпой."

translate russian meet_the_master_male_6ec3ecb9:

    "Сначала я смотрю по сторонам, убеждаясь, что рядом больше никого нет, а затем указываю на себя."

translate russian meet_the_master_male_6eec2b13:

    "Я отвечаю на это заявление самой убедительной улыбкой, на какую способен, хотя она всё равно выходит довольно нервной."

translate russian meet_the_master_male_6e3fff70:

    "Old pervert" "Пс-с... эй, ты!"

translate russian meet_the_master_male_83058973:

    "Глядя ему вслед, я невольно думаю, во что же ввязался."

translate russian meet_the_master_male_880219c4:

    "Эй, я их понимаю. Наверное, это и правда выглядело забавно, даже если произошло со мной."

translate russian meet_the_master_male_96481f21:

    mike.say "Простите, но мне всегда казалось, что мастеров боевых искусств находят в солидных додзё."

translate russian meet_the_master_male_99b55995:

    "Old pervert" "Я видел, что там произошло, сынок. Я наблюдал за всем!"

translate russian meet_the_master_male_a2e6ab72:

    "Old pervert" "Меня называют «Мастером». Тебе нужно учиться, а я могу тебя обучить!"

translate russian meet_the_master_male_11511c22:

    mike.say "Ладно, отлично... когда начинаем?"

translate russian meet_the_master_male_a833d52a:

    "Поднявшись и отряхнув столько песка, сколько могу, я замечаю, что одновременно они сочувственно пожимают плечами."

translate russian meet_the_master_male_acdd04b4:

    "Посмеиваясь над наглостью этого типа, я стараюсь переключиться на отдых, ради которого сюда и пришёл."

translate russian meet_the_master_male_aedfd4a1:

    "Большую часть времени я верчусь из стороны в сторону: сначала уклоняюсь от человека, идущего навстречу, а через мгновение уже обхожу другого с противоположной стороны."

translate russian meet_the_master_male_b0bda423:

    "В смысле, тот Мияги ведь был сантехником, разве нет?"

translate russian meet_the_master_male_b4509ee5:

    master.say "Когда я закончу с тобой, твои разум и тело будут отточены и превращены в смертоносное оружие!"

translate russian meet_the_master_male_b471b67d:

    "Old pervert" "Я видел и тех девушек, которые над тобой смеялись!"

translate russian meet_the_master_male_b4a6b961:

    mike.say "Ладно, «Мастер», или как там вас называют. Я дам вам шанс."

translate russian meet_the_master_male_b55702c3:

    "Я пожимаю плечами в ответ и снова иду дальше, стараясь забыть о случившемся и просто продолжить свой день на пляже."

translate russian meet_the_master_male_b768060d:

    "Я качаю головой, поражаясь его настойчивости, но всё равно начинаю уходить."

translate russian meet_the_master_male_b8818427:

    "На нём солнцезащитные очки и пляжная одежда, а выделяются лишь длинная белая бородка и усы."

translate russian meet_the_master_male_bd555a1a:

    "Но без предупреждения он тыкает костлявым пальцем мне в грудь."

translate russian meet_the_master_male_c191b7b7:

    "Old pervert" "Тебе, мой мальчик, нужен тот, кто научит тебя защищаться!"

translate russian meet_the_master_male_eed89f6a:

    "Old pervert" "Тех, в бикини с завязками и огромными... солнцезащитными очками, сидевших на красных полотенцах!"

translate russian meet_the_master_male_c9f6625f:

    "Я останавливаюсь и осматриваю ближайшие дюны, и в награду вижу лысого старика, пристально смотрящего на меня из-за них."

translate russian meet_the_master_male_d77444d4:

    "На морщинистом лице старика расплывается улыбка."

translate russian meet_the_master_male_d77606aa:

    mike.say "Лучше бы так и было, потому что если всё это окажется полной чушью, я потребую вернуть деньги!"

translate russian meet_the_master_male_d8ca67de:

    "Old pervert" "Хватит искать оправдания, сынок!"

translate russian meet_the_master_male_d8cecf73:

    master.say "Ах, поверь мне, сынок. Ты не пожалеешь!"

translate russian meet_the_master_male_dd9b4a98:

    "Возможно, сразу отметать заявления старика было бы большой ошибкой."

translate russian meet_the_master_male_df49a68a:

    "Большинство людей просто приходят на пляж отдохнуть, но мне, как всегда, везёт собрать вокруг себя всех психов в радиусе двух миль."

translate russian meet_the_master_male_e4a56751:

    "Качки даже не замечают моего падения, и один из них случайно пинает мне в лицо песок, проходя мимо."

translate russian meet_the_master_male_f5d4b0c6:

    master.say "Вот это правильно, мальчик. Я научу тебя постоять за себя, как сейчас!"

translate russian meet_the_master_male_f61aaa0c:

    "Я уже собираюсь спросить, что именно он имеет в виду и почему вообще прятался в дюнах."

translate russian meet_the_master_male_f9355867:

    "Я искоса смотрю на него, всё ещё не готовый полностью довериться."

translate russian meet_the_master_male_fdfef269:

    mike.say "Сто долларов за урок? Да это грабёж среди бела дня, старый ты хрыч!"

translate russian mike_tv_c12dec03:

    mike.say "Прости, сейчас у меня нет времени."

translate russian minami_caught_peeping_male_095d0a22:

    mike.say "Ничего подобного, Минами!"

translate russian minami_caught_peeping_male_0ca4ff1b:

    "Шум работающего душа слышен с самого конца коридора."

translate russian minami_caught_peeping_male_1fd47256:

    "Я отпрыгиваю от двери гораздо быстрее, чем подошёл к ней."

translate russian minami_caught_peeping_male_25f3a52c:

    minami.say "Ты огромный извращенец!"

translate russian minami_caught_peeping_male_264b0705:

    "С этими словами Минами качает головой и сердито уходит."

translate russian minami_caught_peeping_male_26b5a8e7:

    "Или если кто-то оставил дверь открытой..."

translate russian minami_caught_peeping_male_2c108356:

    mike.say "Я просто..."

translate russian minami_caught_peeping_male_44db1aae:

    "Я понимаю, что следует просто не обращать внимания и идти дальше..."

translate russian minami_caught_peeping_male_532350f0:

    "Совсем не потому, что хочу поизвращаться и увидеть одну из девушек в душе."

translate russian minami_caught_peeping_male_66976450:

    "Подойдя ближе, я вижу, что именно это кто-то и сделал."

translate russian minami_caught_peeping_male_7217142f:

    "Она качает головой и наступает на меня."

translate russian minami_caught_peeping_male_775054d4:

    "Я наклоняюсь ближе, закрываю один глаз и прижимаю другой к щели..."

translate russian minami_caught_peeping_male_79ef1a38:

    "Поэтому как можно тише спешу к двери ванной."

translate russian minami_caught_peeping_male_7a022a09:

    mike.say "Я тебя не заметил."

translate russian minami_caught_peeping_male_8de0f0c3:

    "И не могу не задуматься: не прозвучала ли в конце лёгкая ревность?"

translate russian minami_caught_peeping_male_a3725b41:

    "Услышав мой тон, Минами мрачнеет ещё сильнее."

translate russian minami_caught_peeping_male_ace31b87:

    mike.say "Я просто проверял, не оставил ли кто-нибудь душ включённым!"

translate russian minami_caught_peeping_male_b00f89a1:

    mike.say "Ты меня до смерти напугала!"

translate russian minami_caught_peeping_male_bc025491:

    "Что немного странно, ведь обычно его можно услышать лишь рядом с дверью."

translate russian minami_caught_peeping_male_bc353abc:

    minami.say "Ты подглядывал через дверь ванной!"

translate russian minami_caught_peeping_male_b07ba964:

    mike.say "М... Минами..."

translate russian minami_caught_peeping_male_c0d68adc:

    "Она скрестила руки на груди, а лицо мрачнее тучи."

translate russian minami_caught_peeping_male_c5a335f8:

    "Но я ведь не каменный, правда?"

translate russian minami_caught_peeping_male_c73c2074:

    minami.say "Какого чёрта ты делаешь?!"

translate russian minami_caught_peeping_male_d10dd90a:

    minami.say "Я видела, что ты делал."

translate russian minami_caught_peeping_male_d422a79c:

    "А затем резко оборачиваюсь и вижу позади Минами."

translate russian minami_caught_peeping_male_dc861f60:

    "Я всего лишь быстро загляну, и больше ничего."

translate russian minami_caught_peeping_male_e5627129:

    "А я остаюсь один, размышляя о том, что только что сделал."

translate russian minami_caught_peeping_male_e9fa8855:

    "Дверь приоткрыта совсем немного, щель шириной не больше дюйма."

translate russian minami_caught_peeping_male_f58dee9d:

    "Причём исключительно ради удовлетворения любопытства."

translate russian minami_crash_threesome_52c65242:

    mike.say "Что?!"

translate russian minami_samantha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian minami_samantha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian minami_samantha_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian minami_samantha_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian minami_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian minami_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian minami_sasha_threesome_f1d8a63c:

    mike.say "Эм..."

translate russian minami_sasha_threesome_intro_200eb25b:

    mike.say "Эй!"

translate russian minami_sasha_threesome_intro_ee1a096f:

    mike.say "Ни за что!"

translate russian morgan_kleio_event_03_alternate_1c0d45e8:

    mike.say "Ну..."

translate russian morgan_kleio_event_05_200eb25b:

    mike.say "Эй!"

translate russian movie_reactions_17a00328:

    "Похоже, [who] почти не обращает внимания на фильм."

translate russian movie_reactions_21f99641:

    "Похоже, [who] получают огромное удовольствие."

translate russian movie_reactions_26bb41fd:

    "Похоже, [who] получает огромное удовольствие."

translate russian movie_reactions_2827e1bb:

    "Похоже, [who] скорее напугана, чем развлекается."

translate russian movie_reactions_3491154f:

    "Похоже, [who] нравится происходящее."

translate russian movie_reactions_38c352cb:

    "Похоже, увиденное сильно возбуждает [who]."

translate russian movie_reactions_3d306c21:

    "Похоже, никто особенно не следит за происходящим на экране."

translate russian movie_reactions_415590d5:

    "Похоже, [who] нравится происходящее."

translate russian movie_reactions_4c3cc48b:

    "Похоже, [who] почти не обращают внимания на фильм."

translate russian movie_reactions_57c8224c:

    "[who], похоже, не могут оторвать взгляд."

translate russian movie_reactions_5947852a:

    "[who] прямо сияет."

translate russian movie_reactions_5b0ad8ba:

    "[who], похоже, не может оторвать взгляд."

translate russian movie_reactions_7090c108:

    "Похоже, [who] ужасно скучно."

translate russian movie_reactions_74020c9e:

    "Похоже, [who] ужасно скучно."

translate russian movie_reactions_a7425c7f:

    "Похоже, [who] нравится происходящее."

translate russian movie_reactions_b5fd3a1b:

    "Похоже, [who] скорее напуганы, чем развлекаются."

translate russian movie_reactions_bdb914c6:

    "Похоже, всем ужасно скучно."

translate russian movie_reactions_d07d83bb:

    "Похоже, увиденное сильно возбуждает [who]."

translate russian movie_reactions_e5bdc813:

    "[who] прямо сияют."

translate russian movie_reactions_e64f52d7:

    "Похоже, всем весело."

translate russian movie_reactions_f6062c89:

    "Похоже, [who] получает огромное удовольствие."

translate russian mow_the_lawn_ba1a72de:

    "Я стригу газон."

translate russian naked_gig_3f8382ca:

    mike.say "Ого..."

translate russian naked_gig_4dda1c6b:

    mike.say "Что..."

translate russian naked_gig_86d07102:

    mike.say "А..."

translate russian naked_gig_de2ad759:

    mike.say "Что ты..."

translate russian name_cat_e1d914e5:

    mike.say "Хм..."

translate russian name_cat_e1d914e5_1:

    mike.say "Хм..."

translate russian name_cat_e1d914e5_2:

    mike.say "Хм..."

translate russian name_cat_e84ffc6f:

    mike.say "Что?"

translate russian nightclub_party_d9aaad99:

    "[s]"

translate russian nodate_halloween_dance_f1d8a63c:

    mike.say "Эм..."

translate russian offer_a_drink_2a4779d6:

    active_girl.say "Я не могу пить, пока беременна!"

translate russian offer_a_drink_487e80f4:

    active_girl.say "О чём ты вообще думаешь?!"

translate russian offer_a_drink_61abc83e:

    active_girl.say "Ты серьёзно?!"

translate russian offer_a_drink_e23253ba:

    active_girl.say "Конечно!"

translate russian offer_a_drink_ed7e0069:

    active_girl.say "Прости, мне не хочется пить."

translate russian office_aletta_audrey_lavish_shiori_01_30e74fc5:

    mike.say "Эм..."

translate russian office_aletta_audrey_lavish_shiori_01_7879598f:

    mike.say "Привет, Алетта."

translate russian office_aletta_audrey_lavish_shiori_01_f1d8a63c:

    mike.say "Эм..."

translate russian office_aletta_audrey_lavish_shiori_showdown_3de183af:

    "Алетта качает головой."

translate russian office_aletta_audrey_lavish_shiori_showdown_c8dafa44:

    mike.say "Эм, Алетта..."

translate russian office_aletta_audrey_lavish_shiori_showdown_cb97ef18:

    aletta.say "Кхм..."

translate russian office_aletta_audrey_lavish_shiori_showdown_d752f321:

    aletta.say "Спасибо, [hero.name]."

translate russian office_aletta_audrey_lavish_shiori_showdown_d9dbfc7d:

    aletta.say "Хорошо, [hero.name]."

translate russian office_aletta_lavish_showdown_6e154b71:

    mike.say "Ладно, ладно..."

translate russian office_aletta_lavish_showdown_f1d8a63c:

    mike.say "Эм..."

translate russian office_aletta_shiori_showdown_30e74fc5:

    mike.say "Эм..."

translate russian office_audrey_lavish_shiori_showdown_6e154b71:

    mike.say "Ладно, ладно..."

translate russian office_audrey_lavish_showdown_f1d8a63c:

    mike.say "Эм..."

translate russian office_audrey_shiori_02_1ccab2e1:

    mike.say "Хм..."

translate russian office_audrey_shiori_02_86d07102:

    mike.say "А..."

translate russian office_audrey_shiori_02_9c63c87a:

    mike.say "Нет-нет-нет..."

translate russian office_audrey_shiori_showdown_087ff008:

    mike.say "Подожди..."

translate russian office_christmas_antics_a34b5d12:

    aletta.say "Хм..."

translate russian office_christmas_antics_a34b5d12_1:

    aletta.say "Хм..."

translate russian office_christmas_antics_a34b5d12_2:

    aletta.say "Хм..."

translate russian office_christmas_antics_a34b5d12_3:

    aletta.say "Хм..."

translate russian office_christmas_antics_a34b5d12_4:

    aletta.say "Хм..."

translate russian office_christmas_antics_b42793c9:

    aletta.say "О нет!"

translate russian office_christmas_antics_bb8b8e9b:

    aletta.say "О чём ты говоришь?"

translate russian office_christmas_arrival_a34b5d12:

    aletta.say "Хм..."

translate russian office_christmas_arrival_a34b5d12_1:

    aletta.say "Хм..."

translate russian office_christmas_arrival_f1d8a63c:

    mike.say "Эм..."

translate russian office_christmas_arrival_fb8993dd:

    mike.say "Ох..."

translate russian office_christmas_dancing_82a73e37:

    shiori.say "П... правда?!"

translate russian office_christmas_dancing_bcdcbc34:

    mike.say "Эй, Алетта..."

translate russian office_christmas_dancing_c155a10d:

    mike.say "Эй..."

translate russian office_christmas_dwayne_antics_7a022a09:

    mike.say "Я тебя не заметил."

translate russian office_christmas_dwayne_sex_437a01ea:

    mike.say "Ох, чёрт..."

translate russian office_christmas_dwayne_sex_437a01ea_1:

    mike.say "Ох, чёрт..."

translate russian office_christmas_intro_1c0d45e8:

    mike.say "Ну..."

translate russian office_christmas_intro_cb97ef18:

    aletta.say "Кхм..."

translate russian office_christmas_mistletoe_kiss_1c0d45e8:

    mike.say "Ну..."

translate russian office_christmas_mistletoe_kiss_8fb73da4:

    mike.say "Я..."

translate russian office_christmas_mistletoe_kiss_938f1047:

    aletta.say "О, понятно!"

translate russian office_christmas_mistletoe_kiss_d6be390c:

    mike.say "Эм, Алетта..."

translate russian office_christmas_sex_3f8382ca:

    mike.say "Ого..."

translate russian office_christmas_sex_3f8382ca_1:

    mike.say "Ого..."

translate russian office_christmas_sex_6153f545:

    aletta.say "О боже..."

translate russian office_christmas_sex_726262ee:

    aletta.say "Ой..."

translate russian office_christmas_sex_e314c139:

    aletta.say "М-м-м..."

translate russian office_christmas_sex_e84ffc6f:

    mike.say "Что?"

translate russian office_christmas_sex_e84ffc6f_1:

    mike.say "Что?"

translate russian office_event_01_86d07102:

    mike.say "А..."

translate russian office_event_01_da127422:

    mike.say "Что я могу для тебя сделать?"

translate russian office_fivesome_alettafuck_audrey_lavish_shiori_0b789f36:

    aletta.say "Ох, чёрт..."

translate russian office_fivesome_alettafuck_audrey_lavish_shiori_0b789f36_1:

    aletta.say "Ох, чёрт..."

translate russian office_fivesome_alettafuck_audrey_lavish_shiori_80c6e9a4:

    aletta.say "[hero.name]..."

translate russian office_fivesome_alettafuck_audrey_lavish_shiori_ce565589:

    aletta.say "Ах..."

translate russian office_fivesome_lavishfuck_aletta_audrey_shiori_3f8382ca:

    mike.say "Ого..."

translate russian office_fivesome_lavishfuck_aletta_audrey_shiori_a34b5d12:

    aletta.say "Хм..."

translate russian office_harem_pimping_aletta_567a9f21:

    mike.say "Нет, Алетта."

translate russian office_harem_pimping_aletta_a34b5d12:

    aletta.say "Хм..."

translate russian office_harem_pimping_audrey_4c843a4b:

    mike.say "Нет!"

translate russian office_harem_pimping_lavish_aadca25d:

    "Была не была..."

translate russian office_lavish_shiori_showdown_f1d8a63c:

    mike.say "Эм..."

translate russian office_party_6a20a80d:

    "Я качаю головой."

translate russian office_party_94004a03:

    "А."

translate russian office_party_94004a03_1:

    "А."

translate russian office_threesome_lavishfuck_audrey_64a53be7:

    "Да-да, я знаю, о чём вы подумали."

translate russian office_threesome_shiorifuck_lavish_6f8c017a:

    "Но затем мне в голову приходит одна мысль."

translate russian palla_audrey_date_areyoumad_0457e272:

    mike.say "Я не знаю..."

translate russian palla_sasha_male_ending_4dda1c6b:

    mike.say "Что..."

translate russian palla_sasha_male_ending_81a70b3a:

    "Priest" "Дорогие собравшиеся..."

translate russian palla_sasha_male_ending_86d07102:

    mike.say "А..."

translate russian palla_sasha_male_ending_b6b86ea1:

    "Priest" "Кхм..."

translate russian palla_sasha_male_ending_da0db528:

    "Priest" "Может, начнём?"

translate russian palla_sasha_propose_male_30e74fc5:

    mike.say "Эм..."

translate russian palla_sasha_propose_male_30e74fc5_1:

    mike.say "Эм..."

translate russian palla_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian park_thug_attack_0cbf2167:

    thug_say "Ты об этом пожалеешь, пидор."

translate russian park_thug_attack_1f9bf496:

    thug_say "Я ещё отомщу!"

translate russian park_thug_attack_2775cd36:

    thug_say "Эй, ты!"

translate russian park_thug_attack_29914f52:

    "Я отдаю бандиту деньги."

translate russian park_thug_attack_370be80f:

    "Бандит избивает меня, забирает деньги и оставляет лежать на земле."

translate russian park_thug_attack_3aca338d:

    thug_say "Ну, это мы ещё посмотрим."

translate russian park_thug_attack_5728ccd7:

    thug_say "В следующий раз отдавай по-хорошему."

translate russian park_thug_attack_59cbd0df:

    thug_say "Простите, сэр, я вас не узнал."

translate russian park_thug_attack_6ee4730e:

    mike.say "Тебе лучше уйти. Я занимаюсь макраме."

translate russian park_thug_attack_873f733b:

    mike.say "Ни за что. Иди на хуй."

translate russian park_thug_attack_90d4199d:

    "Ночью в парке и правда жутковато..."

translate russian park_thug_attack_99372e63:

    "Я жестоко надираю ему задницу."

translate russian park_thug_attack_ae141266:

    thug_say "Да, ты! Гони деньги!"

translate russian park_thug_attack_ae18099a:

    thug_say "Умница."

translate russian park_thug_attack_c41dddb8:

    "Он разворачивается и убегает, словно за ним гонится сам дьявол."

translate russian park_thug_attack_c41dddb8_1:

    "Он разворачивается и убегает, словно за ним гонится сам дьявол."

translate russian park_thug_attack_d87d7e27:

    thug_say "О, это ты..."

translate russian park_thug_attack_e89b580d:

    thug_say "Ладно, ладно, ладно..."

translate russian park_thug_attack_fd4dd062:

    thug_say "Это какое-то уберизраильское боевое искусство?"

translate russian pet_17f520e0:

    "Я глажу [active_girl.name] по голове."

translate russian pixie_second_threesome_437a01ea:

    mike.say "Ох, чёрт..."

translate russian pixie_second_threesome_437a01ea_1:

    mike.say "Ох, чёрт..."

translate russian pixie_second_threesome_86d07102:

    mike.say "А..."

translate russian pixie_second_threesome_f1d8a63c:

    mike.say "Эм..."

translate russian play_a_videogame_118f74fe:

    "Я проиграл..."

translate russian play_a_videogame_42b9e48c:

    "Я решаю сыграть в автомат с клешнёй."

translate russian play_a_videogame_65d065db:

    "Я выиграл милую плюшевую игрушку!"

translate russian play_in_the_pool_with_everyone_af646cd0:

    "Я играю с девушками в бассейне."

translate russian play_videogames_e766fa23:

    "Я немного играю в видеоигры."

translate russian play_videogames_lexi_sleep_005fd160:

    "Я ждал, пока все разойдутся спать, прислушиваясь к звуку закрывающихся дверей."

translate russian play_videogames_lexi_sleep_00e29b97:

    "Ну конечно, как я мог забыть?"

translate russian play_videogames_lexi_sleep_02e0df32:

    lexi.say "Я пыталась поспать!"

translate russian play_videogames_lexi_sleep_092af0b0:

    "По её позе видно, что она уже приготовилась к ссоре."

translate russian play_videogames_lexi_sleep_09f1f327:

    "И как только раздаётся последний щелчок, я выхожу из своей комнаты и направляюсь в гостиную."

translate russian play_videogames_lexi_sleep_0b13b056:

    lexi.say "Ты действительно хороший друг."

translate russian play_videogames_lexi_sleep_0e3031cd:

    lexi.say "Ургх..."

translate russian play_videogames_lexi_sleep_0e4f54d9:

    mike.say "Чёрт, какой же я плохой друг!"

translate russian play_videogames_lexi_sleep_15c0b304:

    "Лекси кивает и снова устраивается на диване."

translate russian play_videogames_lexi_sleep_d039ad12:

    mike.say "Эм... куда ты собралась, Лекси?"

translate russian play_videogames_lexi_sleep_22b02086:

    "Тогда я хотя бы сначала побью рекорд [bree.name]..."

translate russian play_videogames_lexi_sleep_237b215f:

    "Я бросаюсь к пульту, чтобы убавить громкость прежде, чем меня обнаружат."

translate russian play_videogames_lexi_sleep_23fb32fe:

    "И в той ситуации, в которой она сейчас оказалась, тоже нет её вины."

translate russian play_videogames_lexi_sleep_30e74fc5:

    mike.say "Эм..."

translate russian play_videogames_lexi_sleep_32f796f3:

    lexi.say "Ладно, забудь, [hero.name]."

translate russian play_videogames_lexi_sleep_36ee6ed0:

    "Она сгребает одеяла в охапку и оглядывается по сторонам."

translate russian play_videogames_lexi_sleep_3746ac2b:

    "Что же я за друг такой?"

translate russian play_videogames_lexi_sleep_390e76e0:

    lexi.say "Раз уж ты предпочитаешь торчать здесь, а не спать в ней!"

translate russian play_videogames_lexi_sleep_393d3d8c:

    mike.say "Думаю, нам обоим пора заканчивать на сегодня, ладно?"

translate russian play_videogames_lexi_sleep_a520d208:

    mike.say "Это... в общем, это может подождать до завтра."

translate russian play_videogames_lexi_sleep_44c7cc12:

    "Она трёт глаза тыльной стороной ладони."

translate russian play_videogames_lexi_sleep_4df0fb82:

    "С этими словами она уходит, оставляя меня одного в гостиной."

translate russian play_videogames_lexi_sleep_502e71b6:

    "Я резко поворачиваю голову, пытаясь понять, откуда доносятся ворчание и стоны."

translate russian play_videogames_lexi_sleep_50edbfad:

    "У меня включён телевизор, а на экране запущена игра с Zbox."

translate russian play_videogames_lexi_sleep_51368501:

    "В тишине дома этот шум звучит как взрыв."

translate russian play_videogames_lexi_sleep_582d81bb:

    lexi.say "Посреди ночи здесь можно играть и в более интересные игры."

translate russian play_videogames_lexi_sleep_5e40a6bc:

    lexi.say "Вот умеешь ты дать девушке почувствовать, что ей здесь рады!"

translate russian play_videogames_lexi_sleep_5ee86732:

    "Лекси садится и постепенно приходит в себя."

translate russian play_videogames_lexi_sleep_621c4d1d:

    "Но прежде чем я дохожу до двери, она ловит мой взгляд."

translate russian play_videogames_lexi_sleep_640f67cf:

    "Но явно не ожидала, что я отступлю и извинюсь."

translate russian play_videogames_lexi_sleep_18e65b32:

    mike.say "Я... пытался побить рекорд [bree.name]."

translate russian play_videogames_lexi_sleep_6c16078c:

    "Я ещё покажу [bree.name], как побить мой рекорд, а затем всю ночь буду тыкать её в это носом!"

translate russian play_videogames_lexi_sleep_6c92bf96:

    "Она смотрит на время и тут же окончательно просыпается."

translate russian play_videogames_lexi_sleep_6e440ef0:

    lexi.say "Гр-р-р..."

translate russian play_videogames_lexi_sleep_71a79a39:

    lexi.say "И чтобы ты знал..."

translate russian play_videogames_lexi_sleep_71bcc6ad:

    "Похоже, сегодня мне придётся спать на диване."

translate russian play_videogames_lexi_sleep_7268a654:

    lexi.say "Да что ты вообще знаешь о жизни на улице, а?"

translate russian play_videogames_lexi_sleep_773af269:

    "Словно подчёркивая свои слова, Лекси вскакивает с дивана."

translate russian play_videogames_lexi_sleep_7b52fb14:

    mike.say "До утра ещё рановато!"

translate russian play_videogames_lexi_sleep_7c70a141:

    lexi.say "[hero.name]?"

translate russian play_videogames_lexi_sleep_7f5d2f58:

    "Лекси целую минуту молча смотрит на меня."

translate russian play_videogames_lexi_sleep_8195d462:

    "После того как её трейлер сгорел, она всё ещё спит на диване!"

translate russian play_videogames_lexi_sleep_8c264c65:

    "Сам я сижу на полу с геймпадом в руках."

translate russian play_videogames_lexi_sleep_8d7bc945:

    mike.say "Всяко лучше, чем спать на улице!"

translate russian play_videogames_lexi_sleep_8ddcc8b9:

    lexi.say "Ой, даже не знаю, [hero.name]."

translate russian play_videogames_lexi_sleep_8f2f66cb:

    lexi.say "Готова поспорить, сейчас в доме пустует одна кровать."

translate russian play_videogames_lexi_sleep_903b4c93:

    "Лекси морщится и сонно смотрит на меня."

translate russian play_videogames_lexi_sleep_917fbf7c:

    "Её волосы растрёпаны, и, похоже, во сне у неё даже текли слюни."

translate russian play_videogames_lexi_sleep_94750899:

    lexi.say "Какого..."

translate russian play_videogames_lexi_sleep_9d2f6018:

    "Ну и неловко получилось..."

translate russian play_videogames_lexi_sleep_a2403718:

    mike.say "И как-то забыл, что ты здесь спишь!"

translate russian play_videogames_lexi_sleep_a2c69c85:

    lexi.say "Уже утро?"

translate russian play_videogames_lexi_sleep_a3d24ad8:

    "Мне остаётся лишь вздохнуть и покачать головой."

translate russian play_videogames_lexi_sleep_a50c8259:

    lexi.say "Я проспала?"

translate russian play_videogames_lexi_sleep_a68b3fac:

    "По её виду понятно, что она пытается сообразить, что происходит."

translate russian play_videogames_lexi_sleep_a71e77df:

    "Признавшись в этом, Лекси слегка краснеет."

translate russian play_videogames_lexi_sleep_a87375c7:

    "Она права. Какого чёрта я вообще творю?"

translate russian play_videogames_lexi_sleep_a95e5bfe:

    lexi.say "И запомни, [hero.name]..."

translate russian play_videogames_lexi_sleep_aaf779af:

    lexi.say "Да уж, [hero.name]!"

translate russian play_videogames_lexi_sleep_ad554e03:

    mike.say "Мне следовало помнить, что ты здесь."

translate russian play_videogames_lexi_sleep_b1879d74:

    "Какого чёрта она вообще нарушает мою домашнюю идиллию?"

translate russian play_videogames_lexi_sleep_b36fcd47:

    lexi.say "Просто я становлюсь раздражительной, когда меня будят, вот и всё!"

translate russian play_videogames_lexi_sleep_be6de3e8:

    mike.say "Нет, Лекси."

translate russian play_videogames_lexi_sleep_c25eec9e:

    lexi.say "Всё зависит от того, с кем ты играешь!"

translate russian play_videogames_lexi_sleep_c2a0f2e0:

    "Даже если начну всё отрицать, Лекси и так прекрасно видит правду!"

translate russian play_videogames_lexi_sleep_c2e45830:

    "Но ещё до того, как я нажимаю кнопку, другой звук даёт понять, что уже слишком поздно!"

translate russian play_videogames_lexi_sleep_c6852a9f:

    lexi.say "Один из лучших, какие у меня когда-либо были!"

translate russian play_videogames_lexi_sleep_c845f60a:

    lexi.say "Что ты вообще здесь делаешь?"

translate russian play_videogames_lexi_sleep_cabd56c1:

    mike.say "Эй, Лекс!"

translate russian play_videogames_lexi_sleep_ce029010:

    mike.say "Здесь ведь больше негде спать!"

translate russian play_videogames_lexi_sleep_d13d52ca:

    "Но всё равно чувствую, как начинаю выходить из себя."

translate russian play_videogames_lexi_sleep_d2f09e87:

    mike.say "Знаешь, Лекси, могла бы быть хоть немного благодарнее."

translate russian play_videogames_lexi_sleep_d92a914f:

    "Лишь когда вместе с приставкой оживает телевизор, я понимаю, что кое-что забыл."

translate russian play_videogames_lexi_sleep_da0d03f2:

    "Когда [bree.name] играет на Zbox, она любит выкручивать громкость на полную!"

translate russian play_videogames_lexi_sleep_deb8bc7c:

    "Она расслабляется и слегка качает головой."

translate russian play_videogames_lexi_sleep_e957a7e8:

    "Особенно после всего, через что Лекси недавно пришлось пройти."

translate russian play_videogames_lexi_sleep_e958dd42:

    "Я понимаю, что Лекси, скорее всего, просто раздражена из-за того, что её разбудили."

translate russian play_videogames_lexi_sleep_f3d5de2b:

    mike.say "Прости, Лекси."

translate russian play_videogames_lexi_sleep_f465eab9:

    "Лекси отвечает мне злобным взглядом."

translate russian play_videogames_lexi_sleep_f5b1a9dc:

    mike.say "Ну разбудил я тебя, и что с того?"

translate russian play_videogames_lexi_sleep_f63e54fe:

    lexi.say "По крайней мере, там мне не пришлось бы терпеть твоё дерьмо!"

translate russian play_videogames_lexi_sleep_f6a825d3:

    lexi.say "Ничего себе, [hero.name]. Просто слов нет."

translate russian play_videogames_lexi_sleep_fbd8f879:

    "И тогда впервые замечаю Лекси, всё ещё закутанную в гнездо из одеял."

translate russian play_videogames_lexi_sleep_fe7d478e:

    "Я тоже отвожу взгляд, тронутый её искренностью."

translate russian play_videogames_lexi_sleep_ff7370e2:

    mike.say "Я всё-таки приютил тебя, когда тебе негде было жить."

translate russian play_videogames_lexi_sleep_fff70ef8:

    "Мне требуется всего несколько секунд, чтобы включить Zbox и схватить геймпад."

translate russian play_videogames_with_bree_23c02f97:

    "И побеждаю!"

translate russian play_videogames_with_bree_9785b0de:

    "Я немного играю в видеоигры вместе с [bree.name]."

translate russian play_videogames_with_bree_c3b02779:

    "И проигрываю..."

translate russian play_with_231de2c9:

    active_girl.say "Прости, мне сейчас не хочется."

translate russian play_with_b778778c:

    active_girl.say "Конечно, почему бы и нет?"

translate russian play_with_bree_02d764b1:

    mike.say "Было весело."

translate russian play_with_bree_16742d44:

    bree.say "Не переживай, в следующий раз точно меня обыграешь!"

translate russian play_with_bree_35c90c19:

    "Я довольно легко её обыгрываю."

translate russian play_with_bree_4cb1b83e:

    mike.say "Нет, прости."

translate russian play_with_bree_6fd64c7b:

    bree.say "Хочешь сыграть против меня?"

translate russian play_with_bree_9f11c32b:

    bree.say "Да, нам обязательно нужно как-нибудь прийти сюда снова!"

translate russian play_with_bree_cc26b258:

    mike.say "Я проиграл."

translate russian play_with_bree_db2ac7b6:

    "[bree.name] бросает на меня вызывающий взгляд."

translate russian play_with_bree_e977a8c4:

    bree.say "Тогда в другой раз."

translate russian play_with_bree_f8354afa:

    mike.say "Конечно."

translate russian play_with_dd025e89:

    "Я играю вместе с [active_girl.name]."

translate russian polygamy_news_114a8036:

    "У меня есть отвратительная привычка: вечером после работы я прихожу домой, валюсь на диван и включаю орущий телевизор."

translate russian polygamy_news_141b39b6:

    "Стоит им прозвучать, и я, словно собака Павлова при звоне колокольчика, тут же выпрямляюсь и начинаю внимательно слушать."

translate russian polygamy_news_18b3404d:

    "Shady guy" "Критики прозвали его «Законом о двоежёнстве» из-за наиболее далеко идущих последствий, и ожидалось, что на сегодняшнем заседании его наконец отклонят."

translate russian polygamy_news_23ded5ac:

    "Сегодня вечером произошло первое, а не второе."

translate russian polygamy_news_26ae5171:

    "Но ведь тогда, если предложить такое двум или нескольким представительницам противоположного пола, они уже не обязательно тут же влепят тебе пощёчину?"

translate russian polygamy_news_2aeb2d3a:

    "Shady guy" "...сегодня в нижней палате состоялось второе чтение скандального «Законопроекта о реформе брака и социальных институтов»."

translate russian polygamy_news_324e3629:

    "Shady guy" "Однако неожиданно его поддержали депутаты, которые прежде воздерживались, и законопроект с небольшим перевесом был принят."

translate russian polygamy_news_36fa8b03:

    "Когда-то я, возможно, действительно садился посмотреть что-то конкретное, но теперь телевизор служит скорее фоновым шумом для чувств."

translate russian polygamy_news_3fdfd078:

    "Как бы рассеянно я ни смотрел телевизор, некоторые слова и выражения всегда пробиваются сквозь туман и доходят до моего сознания."

translate russian polygamy_news_4b088457:

    "Поначалу к этой идее, вероятно, начнут склоняться лишь самые непредубеждённые девушки."

translate russian polygamy_news_534e3574:

    "Часто я даже не знаю, что именно смотрю, если только что-то действительно примечательное не привлечёт моё внимание или кто-нибудь не войдёт и не накричит на меня."

translate russian polygamy_news_60fd56e1:

    "Shady guy" "Его противники назвали этот шаг доказательством масштабного заговора, направленного на подрыв..."

translate russian polygamy_news_75b52cb5:

    "Ведущая продолжила разбирать эту тему, но к тому моменту я уже давно перестал её слушать."

translate russian polygamy_news_9eb5d754:

    "И в каком-то смысле я был даже рад, что, услышав сказанное, оказался в комнате один."

translate russian polygamy_news_a1e565ca:

    "Схватив пульт, я отматываю запись примерно на тридцать секунд, чтобы услышать начало сюжета."

translate russian polygamy_news_a74eed77:

    "Но постоянно возмущённые правые консерваторы слишком боялись, что их назовут гомофобами, чтобы выступать против основных положений законопроекта."

translate russian polygamy_news_ab680ed4:

    "Кто-то другой, наверное, задумался бы о более широких социальных последствиях такого изменения закона."

translate russian polygamy_news_b96c3260:

    "А, точно. Тот самый законопроект, который проходил через парламент и где-то содержал пункт о многожёнстве."

translate russian polygamy_news_bfa430fc:

    "Это действительно происходило, и вскоре закон позволит любому желающему состоять в браке сразу с несколькими людьми."

translate russian polygamy_news_ca0f5266:

    "Но мне первым делом пришло в голову, что если многожёнство станет нормой, то и отношения между более чем двумя людьми тоже будут восприниматься нормально."

translate russian polygamy_news_ce36c2ad:

    "Я немного читал о нём в интернете. Предполагалось, что он уравняет права в браке и гражданских союзах для всех, независимо от ориентации."

translate russian polygamy_news_d2006b9c:

    "Я тут же заинтересованно поднимаю взгляд и понимаю, что смотрю новости."

translate russian polygamy_news_d86be79f:

    "Пункт о многожёнстве, вероятно, был наименее важной частью всего документа."

translate russian polygamy_news_f3b8f8ea:

    "Поэтому они ухватились за многожёнство как за обходной способ выступить против него и прозвали документ «Законом о двоежёнстве»."

translate russian polygamy_news_fa9c0b18:

    "В данном случае таким словом оказалось «многожёнство»."

translate russian pool_tan_fbc96115:

    "Я дремлю на солнце."

translate russian practice_band_e0e9b040:

    "Мы тренируемся вместе."

translate russian quit_a_job_day_3a9dfd8f:

    "Shop owner" "Какая жалость..."

translate russian quit_a_job_night_3a9dfd8f:

    "Shop owner" "Какая жалость..."

translate russian reona_teaser_03fb2db8:

    "Girl" "Я тебе покажу."

translate russian reona_teaser_0463ff8c:

    "Я иду по коридору, почти не глядя по сторонам."

translate russian reona_teaser_067dad0d:

    "Зачем? Я делал что-то глупое? У меня что-то застряло в зубах?"

translate russian reona_teaser_0af2e66e:

    "Сердце начинает сильнее колотиться в груди. Я больше ничего не говорю, когда она достаёт из декольте сложенный листок и прижимает его плоской ладонью к моей груди."

translate russian reona_teaser_0edfc7f3:

    bree.say "Никто не знает, что с ней произошло. Раньше она была милой и тихой, а теперь стала совершенно бесстыжей шлюхой."

translate russian reona_teaser_1173f947:

    mike.say "Я запомню."

translate russian reona_teaser_12b635bf:

    "Я не до конца уверен, хочу ли держаться от неё подальше."

translate russian reona_teaser_14eca4d6:

    "Она делает ещё крошечный шаг вперёд, но я до болезненности осознаю, насколько мало места между нами, особенно когда она снова подносит членоледенец к языку и соблазнительно проводит им по его центру."

translate russian reona_teaser_18ed24c4:

    "Girl" "В чём проблема? Не встаёт? Обещаю, я могу с этим помочь."

translate russian reona_teaser_197aacd0:

    "Юбка настолько короткая, что едва начинает прикрывать изгибы бёдер. Мой взгляд задерживается на её краю, под которым трусики, наверное, скрыты от меня лишь одной тончайшей ниточкой ткани."

translate russian reona_teaser_200eb25b:

    mike.say "Эй!"

translate russian reona_teaser_23ef0d49:

    "Я замечаю группу людей, занявших слишком много места и слишком громко разговаривающих, лишь когда один из них слишком широко взмахивает рукой и едва не задевает меня по лицу."

translate russian reona_teaser_23fc2f20:

    "Её дерзость на мгновение лишает меня дара речи. Я переминаюсь с ноги на ногу и засовываю руки в карманы, понимая, что, вероятно, скоро придётся кое-что поправить."

translate russian reona_teaser_26cd4086:

    "Теперь виноват ещё и я."

translate russian reona_teaser_28e089b7:

    "Даже задним числом это осознание заставляет что-то внутри меня шевельнуться."

translate russian reona_teaser_2defa4ef:

    "Её голос одновременно мягкий, томный и сладкий. От осознания, что всё её внимание принадлежит мне, внутри становится странно приятно."

translate russian reona_teaser_331100b5:

    "Girl" "Давай покажем друг другу, на что способны..."

translate russian reona_teaser_3b5b0449:

    "Они не замечают меня даже после крика, и мне самому приходится резко уворачиваться, чтобы не получить сломанный нос. Я оступаюсь и врезаюсь в кого-то другого."

translate russian reona_teaser_3ca6b858:

    mike.say "Эти идиоты чуть меня не ударили, я не хотел..."

translate russian reona_teaser_3e98bb5d:

    "В уголке её губ появляется кокетливая улыбка. Она снова вводит головку леденца между губ и на мгновение проводит языком вдоль стержня, прежде чем продолжить."

translate russian reona_teaser_3fb7f4d9:

    bree.say "Держись от неё подальше, хорошо? Здесь все знают, какая она."

translate russian reona_teaser_40c7d4c3:

    "Я всё ещё не уверен, что она серьёзно, а не просто издевается, но внезапно ясно понимаю, что ответил совсем не так, как следовало."

translate russian reona_teaser_4272a234:

    "Она подмигивает."

translate russian reona_teaser_4392abcd:

    bree.say "Я просто о тебе беспокоюсь."

translate russian reona_teaser_460a8409:

    "Она делает маленький шаг вперёд, но я остро ощущаю, как сокращается расстояние между нами. Её сексуальная аура почти душит меня прямо посреди людного места."

translate russian reona_teaser_483f2b6c:

    "Кажется, я ещё никогда не встречал девушку, о которой точно знал бы, что она настолько сильно хочет меня просто ради удовольствия. От одной этой мысли я схожу с ума."

translate russian reona_teaser_4aaf47ec:

    "В её открытом, наглом желании моего члена и во взгляде, который говорил, что она предпочла бы прямо здесь, в коридоре, встать на колени и отсосать мне, а не ограничиваться леденцом, было что-то почти гипнотическое."

translate russian reona_teaser_4e3c3f25:

    "Girl" "Я таких за милю чую."

translate russian reona_teaser_0f120951:

    "Она потрясающая, хотя выглядит почти карикатурой на ту модную субкультуру, о которой я слышал... гангуро или гяру?"

translate russian reona_teaser_50d85cc7:

    "На ней яркие и, откровенно говоря, безвкусные аксессуары, сильно осветлённые волосы и густой тёмный макияж, подчёркивающий симпатичные черты."

translate russian reona_teaser_514fbf32:

    "Я оглядываю коридор в поисках людей, которые сейчас хихикают надо мной. Такие девушки не существуют за пределами дешёвого порно и влажных снов, правда?"

translate russian reona_teaser_557a59b9:

    mike.say "Ты не ошиблась. Где ты научилась такому таланту?"

translate russian reona_teaser_5739d1e8:

    "Но [bree.name], похоже, искренне переживает, и я вижу тревогу в её больших карих глазах."

translate russian reona_teaser_5bd0bc14:

    "Girl" "Я видела, как ты шёл сюда. Я всё заметила."

translate russian reona_teaser_5dd6f8cc:

    "Girl" "Хочешь сказать, что я ошиблась?"

translate russian reona_teaser_5f05ef36:

    bree.say "Я видела, как ты разговаривал с той девушкой..."

translate russian reona_teaser_5f2e468e:

    "[bree.name] слегка надувает губы, но, похоже, принимает мой ответ таким, какой он есть."

translate russian reona_teaser_6bc773d2:

    "При ходьбе её бёдра восхитительно покачиваются, а нижняя половина ягодиц остаётся открытой и подпрыгивает. Я прекрасно понимаю, что это сделано намеренно."

translate russian reona_teaser_733798c6:

    "На ней написано «РЕОНА», рядом нарисованы маленькие сердечко и звезда, а ниже указан номер телефона."

translate russian reona_teaser_76e97f58:

    "В нижнем углу нарисован маленький член, кончающий на эмодзи-язык."

translate russian reona_teaser_7aa01703:

    "Мне не нужно было это объяснять: Реона сама дала понять всё более чем ясно."

translate russian reona_teaser_7b290f60:

    "Girl" "Скажем так, благодаря практике."

translate russian reona_teaser_837b9cfa:

    bree.say "Вообще-то мне нужно ещё зайти к одному преподавателю, но позже обязательно увидимся!"

translate russian reona_teaser_8cef2bef:

    "Girl" "Угу. Ты похож на парня, который умеет как следует развлечь девушку."

translate russian reona_teaser_8dc1664f:

    "Я машу ей вслед. Она разворачивается и убегает, а я остаюсь один посреди коридора, вздыхаю и ещё минуту осмысливаю произошедшее, прежде чем идти дальше."

translate russian reona_teaser_94966ff5:

    bree.say "Эй!"

translate russian reona_teaser_95f77634:

    "Она мурлычет, подмигивает, запускает руку в декольте и вытаскивает сложенный листок, вкладывая его мне в ладонь, прежде чем я успеваю отреагировать."

translate russian reona_teaser_9838f4f8:

    "Не слишком тонко, зато она точно позаботилась, чтобы, снова увидев записку, я не забыл, кто такая Реона."

translate russian reona_teaser_9afeaf9a:

    "Я опускаю взгляд на бумажку и с любопытством разворачиваю её. Даже отсюда чувствуется нанесённый на неё аромат духов."

translate russian reona_teaser_9de9d374:

    "Girl" "М-м-м."

translate russian reona_teaser_a4a42fdc:

    "Прекрасно."

translate russian reona_teaser_a7b5a85a:

    "Девушка скрещивает руки под великолепной грудью и обиженно надувает блестящие губы."

translate russian reona_teaser_ad16738f:

    "Она совершенно бесстыдно сосёт леденец в форме члена и смотрит на меня большими оленьими глазами."

translate russian reona_teaser_b0bb7401:

    "Girl" "Слишком быстро кончаешь?"

translate russian reona_teaser_bf1d1769:

    mike.say "Это какой-то розыгрыш?"

translate russian reona_teaser_bf485ced:

    mike.say "Смотрела на меня?"

translate russian reona_teaser_c06dcd96:

    "...Правда?"

translate russian reona_teaser_c46a2204:

    "Наверное, именно эту мягкую, упругую и блаженно приятную плоть я почувствовал, когда столкнулся с ней."

translate russian reona_teaser_c71f6fd6:

    "Я понимаю, что и она способна отлично меня развлечь, и пульс беспомощно ускоряется."

translate russian reona_teaser_c8d30aaf:

    "Не стану отрицать."

translate russian reona_teaser_c9d81a2f:

    mike.say "Я... прости."

translate russian reona_teaser_cd412cda:

    "Мой взгляд поднимается по обнажённой безупречной загорелой коже живота к щедрому декольте, почти бьющему меня в лицо благодаря, должно быть, самому мощному пуш-апу."

translate russian reona_teaser_cd4a2bc4:

    "Girl" "Я знаю."

translate russian reona_teaser_d143e4cd:

    "Она выставляет бедро в сторону, открывая ещё полдюйма кожи, и мой взгляд беспомощно опускается к её ногам."

translate russian reona_teaser_d172813e:

    "Girl" "Привет."

translate russian reona_teaser_d2531846:

    "Я оборачиваюсь и вижу, как она бежит ко мне по коридору, нахмурив брови."

translate russian reona_teaser_e199e35c:

    "Продолжая, она глубоко и хорошо обсасывает конфету, затем с громким чмоком вытаскивает её и облизывает верхнюю губу."

translate russian reona_teaser_e3620283:

    "Голос [bree.name] резко вырывает меня из мечтательного состояния, пока я улыбаюсь, глядя на номер телефона и предаваясь фантазиям."

translate russian reona_teaser_e3eadce5:

    "Girl" "Мы всегда можем просто повторить."

translate russian reona_teaser_eb3d03ca:

    "Выбора мне не оставляют, и я беру бумажку, а затем поднимаю взгляд и смотрю, как она разворачивается и уходит, оставляя меня слегка опьянённым этой встречей."

translate russian reona_teaser_eee8c5e6:

    "Я улыбаюсь ей более ободряюще. Она полностью расслабляется и слегка улыбается в ответ, хотя брови всё ещё немного нахмурены."

translate russian reona_teaser_f000a8a9:

    "Она звучит немного расстроенно."

translate russian reona_teaser_f261fa4a:

    "Girl" "Как-нибудь позвони мне."

translate russian reona_teaser_f4387aa1:

    "Свободной рукой девушка касается верхней пуговицы рубашки, едва удерживающей рвущуюся наружу грудь, и начинает намеренно играть с ней, слегка оттягивая ткань, чтобы открыть мне более глубокий вид в декольте."

translate russian reona_teaser_f702762b:

    "Она снова берёт леденец в рот, несколько раз двигает им между сжатыми губами, а затем вытаскивает с громким удовлетворённым хлопком."

translate russian reona_teaser_fb301810:

    "Я прочищаю горло, чтобы справиться с заиканием, и продолжаю."

translate russian reona_teaser_ff499c67:

    "Я поворачиваюсь, чтобы извиниться перед миниатюрной девушкой, которую едва не сбил, и замираю, поражённый её видом."

translate russian repair_hot_tub_b0a17b71:

    "Джакузи сломано. Мне нужно 5000{image=gui/icons/icon_money.png}, чтобы его починить."

translate russian run_activity_05873090:

    "Девушки не сводят с меня глаз, пока я бегу."

translate russian run_activity_80d4cba3:

    "Они не сводят с меня глаз, пока я бегу."

translate russian run_activity_af593116:

    "[successes[0].name] не сводит с меня глаз, пока я бегу."

translate russian run_activity_f2a4b7cb:

    "[successes[0].name] не сводит с меня глаз, пока я бегу."

translate russian run_forest_05873090:

    "Девушки не сводят с меня глаз, пока я бегу."

translate russian run_forest_80d4cba3:

    "Они не сводят с меня глаз, пока я бегу."

translate russian run_forest_af593116:

    "[successes[0].name] не сводит с меня глаз, пока я бегу."

translate russian run_forest_f2a4b7cb:

    "[successes[0].name] не сводит с меня глаз, пока я бегу."

translate russian samantha_caught_peeping_male_0471e944:

    "Но Сэм обрывает меня, прежде чем я успеваю сказать хоть слово."

translate russian samantha_caught_peeping_male_0e1e0f9f:

    samantha.say "Господи, ты занимался этим и раньше, когда я здесь жила?"

translate russian samantha_caught_peeping_male_176e31a7:

    "Но от двери ванной точно отпрыгиваю."

translate russian samantha_caught_peeping_male_188ead88:

    "Значит, если я слышу его здесь, возможно только одно: кто-то оставил дверь открытой."

translate russian samantha_caught_peeping_male_2e8c46b4:

    mike.say "Ч... чтобы проверить, свободна ли ванная!"

translate russian samantha_caught_peeping_male_1f170698:

    samantha.say "Но мы оба понимаем, что ты только что делал."

translate russian samantha_caught_peeping_male_211669b1:

    "Но я всего лишь человек. Разве один быстрый взгляд кому-нибудь навредит?"

translate russian samantha_caught_peeping_male_26fde33a:

    samantha.say "Тогда почему бы просто не постучать?"

translate russian samantha_caught_peeping_male_2c108356:

    mike.say "Я просто..."

translate russian samantha_caught_peeping_male_2eedcbcd:

    samantha.say "Что ты делаешь?!"

translate russian samantha_caught_peeping_male_3183ad24:

    "Или осознание, что я её разочаровал."

translate russian samantha_caught_peeping_male_4d6562fe:

    samantha.say "ЭЙ!"

translate russian samantha_caught_peeping_male_5cd3bcf5:

    mike.say "Просто проверял..."

translate russian samantha_caught_peeping_male_6b7519c5:

    samantha.say "Вообще-то я не хочу знать."

translate russian samantha_caught_peeping_male_6d84835d:

    samantha.say "Может, тогда я ещё смогу верить, что ты не законченный мерзавец!"

translate russian samantha_caught_peeping_male_7d1d546c:

    "Я молча киваю и смотрю, как Сэм уходит."

translate russian samantha_caught_peeping_male_8282fe9c:

    "Сэм вздыхает и закатывает глаза."

translate russian samantha_caught_peeping_male_8520d4c9:

    "Услышав голос Сэм, я едва не выпрыгиваю из собственной кожи."

translate russian samantha_caught_peeping_male_864de253:

    "Он ещё пригодится, когда вечером я останусь один!"

translate russian samantha_caught_peeping_male_9249bd35:

    "Подняв взгляд, я вижу, что она явно недовольна."

translate russian samantha_caught_peeping_male_94f54213:

    "Мне не нужно наблюдать долго."

translate russian samantha_caught_peeping_male_a3b93aad:

    samantha.say "Да неужели?"

translate russian samantha_caught_peeping_male_a7f3d13a:

    "Одновременно наклоняюсь вперёд и прикладываю глаз к щели."

translate russian samantha_caught_peeping_male_b77ae0d7:

    "Сэм смотрит на меня так, словно я заявил, что у меня две головы."

translate russian samantha_caught_peeping_male_c2b5a993:

    "Достаточно заглянуть на несколько секунд и сохранить хороший образ в памяти."

translate russian samantha_caught_peeping_male_cd7e4f57:

    "Я просто прохожу мимо ванной, когда слышу шум льющейся внутри воды."

translate russian samantha_caught_peeping_male_ce9303be:

    "Я понимаю, что не должен этого делать, что следует просто идти дальше и обо всём забыть."

translate russian samantha_caught_peeping_male_d0899de9:

    "Я как можно тише подкрадываюсь к двери ванной."

translate russian samantha_caught_peeping_male_d8e9b636:

    "Никому больше знать не обязательно..."

translate russian samantha_caught_peeping_male_dc66db81:

    "Я открываю рот, пытаясь объясниться."

translate russian samantha_caught_peeping_male_df5fb05b:

    "Не знаю, что хуже: чувство вины из-за того, что меня поймали."

translate russian samantha_caught_peeping_male_dfd99d19:

    "Ничего странного, кроме того, что закрытая дверь обычно не пропускает этот звук наружу."

translate russian samantha_caught_peeping_male_ebe0e572:

    samantha.say "Просто пообещай, что перестанешь, хорошо?"

translate russian samantha_caught_peeping_male_f0a0bd54:

    mike.say "Наверное, мне следовало самому до этого додуматься!"

translate russian samantha_caught_peeping_male_f1d8a63c:

    mike.say "Эм..."

translate russian samantha_caught_peeping_male_f6fbbbee:

    samantha.say "Хорошая попытка, [hero.name]."

translate russian samantha_event_01_889802a8:

    mike.say "Упс..."

translate russian samantha_request_30e74fc5:

    mike.say "Эм..."

translate russian samantha_request_f1d8a63c:

    mike.say "Эм..."

translate russian samantha_sasha_pregnant_showdown_8fb73da4:

    mike.say "Я..."

translate russian samantha_sasha_pregnant_showdown_e84ffc6f:

    mike.say "Что?"

translate russian samantha_sasha_propose_male_6757cf6b:

    mike.say "Ну..."

translate russian samantha_sasha_propose_male_8069cfae:

    mike.say "Ты выйдешь за меня?"

translate russian samantha_sharing_bed_0b60d8ce:

    mike.say "П... правда?"

translate russian samantha_sharing_bed_30e74fc5:

    mike.say "Эм..."

translate russian samantha_sharing_bed_3f8382ca:

    mike.say "Ого..."

translate russian samantha_sharing_bed_67d5b96e:

    mike.say "Угх..."

translate russian samantha_sharing_bed_f1d8a63c:

    mike.say "Эм..."

translate russian samantha_sharing_bed_f1d8a63c_1:

    mike.say "Эм..."

translate russian sasha_caught_peeping_male_0919776c:

    "Сейчас ей совсем не весело."

translate russian sasha_caught_peeping_male_0eb1c940:

    sasha.say "И напомни, у нас есть правило насчёт подглядывания?"

translate russian sasha_caught_peeping_male_0fe81f15:

    "Саша качает головой и горько усмехается."

translate russian sasha_caught_peeping_male_107a898b:

    "С этими словами Саша сердито уходит."

translate russian sasha_caught_peeping_male_1ec39d52:

    "Саша стоит там, уперев сжатые кулаки в бёдра."

translate russian sasha_caught_peeping_male_26009b0f:

    "Обычно я такими вещами не занимаюсь, но перед соблазном не устоял."

translate russian sasha_caught_peeping_male_27050310:

    sasha.say "А я знаю, [hero.name]."

translate russian sasha_caught_peeping_male_2abbc6a1:

    sasha.say "Не строй из себя невинного, [hero.name]."

translate russian sasha_caught_peeping_male_30e74fc5:

    mike.say "Эм..."

translate russian sasha_caught_peeping_male_36d7fcbb:

    "Не обычный непроизвольный кашель."

translate russian sasha_caught_peeping_male_3f8168c8:

    "Я подкрадываюсь ближе и наклоняюсь, чтобы быстро заглянуть, всего на секунду, клянусь!"

translate russian sasha_caught_peeping_male_48f1df89:

    "Проходя мимо, я вижу, что дверь ванной приоткрыта, и слышу шум льющейся внутри воды."

translate russian sasha_caught_peeping_male_4e3b5e04:

    sasha.say "И с этого момента я буду за тобой следить."

translate russian sasha_caught_peeping_male_5a61fd3d:

    sasha.say "Потому что такое правило НЕ ДОЛЖНО быть нужно, [hero.name]."

translate russian sasha_caught_peeping_male_7d04244f:

    "Я медленно оборачиваюсь, уже чувствуя, как внутри всё скручивается."

translate russian sasha_caught_peeping_male_88953f1b:

    sasha.say "Я прекрасно представляю, что творилось у тебя в голове!"

translate russian sasha_caught_peeping_male_8be1659c:

    sasha.say "И знаешь, ПОЧЕМУ?"

translate russian sasha_caught_peeping_male_ebc6caad:

    mike.say "Н... нет."

translate russian sasha_caught_peeping_male_9244ddd9:

    mike.say "Д... да, Саша... ты права."

translate russian sasha_caught_peeping_male_a2dd5d3e:

    mike.say "Не знаю, о чём я думал."

translate russian sasha_caught_peeping_male_a4ade6b9:

    "Более того, она выглядит так, будто собирается меня убить!"

translate russian sasha_caught_peeping_male_abd2d484:

    "И именно в этот момент кто-то позади демонстративно прочищает горло."

translate russian sasha_caught_peeping_male_b591f303:

    sasha.say "Потому что нормальные люди не ходят и не подглядывают за соседями!"

translate russian sasha_caught_peeping_male_ce1a8154:

    "Я уже чувствую, как щёки горят от стыда."

translate russian sasha_caught_peeping_male_d44d7292:

    mike.say "Привет, Саша!"

translate russian sasha_caught_peeping_male_d8c0294d:

    "Такого вопроса я не ожидал."

translate russian sasha_caught_peeping_male_dc54c359:

    mike.say "Нет, Саша, кажется, нет."

translate russian sasha_caught_peeping_male_ebef79ff:

    "А намеренный, которым дают понять, что тебя застукали!"

translate russian sasha_caught_peeping_male_ec347765:

    "В итоге опускаю взгляд к ногам, боясь встретиться с Сашей глазами."

translate russian sasha_caught_peeping_male_f1d8a63c:

    mike.say "Эм..."

translate russian sasha_caught_peeping_male_f5dab866:

    "И он скорее сбивает меня с толку."

translate russian sasha_caught_peeping_male_ffae3bac:

    sasha.say "И какого чёрта ты, по-твоему, делаешь?"

translate russian sasha_concert_naked_30e74fc5:

    mike.say "Эм..."

translate russian sasha_concert_naked_8fb73da4:

    mike.say "Я..."

translate russian sasha_kitchen_bree_0351800a:

    bree.say "Я тоже."

translate russian sasha_kitchen_bree_05aea1ac:

    "Саша и [bree.name] беседуют на кухне."

translate russian sasha_kitchen_bree_1369b0a6:

    bree.say "Ага, здесь дёшево и уютно."

translate russian sasha_kitchen_bree_2032768d:

    sasha.say "Я бы не возражала поделиться им..."

translate russian sasha_kitchen_bree_2032768d_1:

    sasha.say "Я бы не возражала поделиться им..."

translate russian sasha_kitchen_bree_283b6a75:

    sasha.say "Если место занято мной, больше там никому не поместиться."

translate russian sasha_kitchen_bree_2b6ceda4:

    sasha.say "Как же здорово, что я нашла это место."

translate russian sasha_kitchen_bree_3d9b789d:

    bree.say "Ещё посмотрим..."

translate russian sasha_kitchen_bree_3fae6693:

    "Они просто болтают о всяких девчачьих вещах."

translate russian sasha_kitchen_bree_409a2cb2:

    sasha.say "Удачи тебе с этим."

translate russian sasha_kitchen_bree_5053e720:

    bree.say "Тебе определённо стоит попробовать."

translate russian sasha_kitchen_bree_54e7e8f7:

    bree.say "Да, я бы не отказалась от него кусочек."

translate russian sasha_kitchen_bree_6d30b063:

    bree.say "Я видела, как ты смотришь на [hero.name]."

translate russian sasha_kitchen_bree_6d30b063_1:

    bree.say "Я видела, как ты смотришь на [hero.name]."

translate russian sasha_kitchen_bree_6d30b063_2:

    bree.say "Я видела, как ты смотришь на [hero.name]."

translate russian sasha_kitchen_bree_6d30b063_3:

    bree.say "Я видела, как ты смотришь на [hero.name]."

translate russian sasha_kitchen_bree_6fadeb6d:

    bree.say "Похоже, теперь мы соперницы."

translate russian sasha_kitchen_bree_7eaf9918:

    sasha.say "И сосед довольно симпатичный."

translate russian sasha_kitchen_bree_81652d8b:

    sasha.say "Я подумываю сделать [hero.name] своей личной секс-игрушкой."

translate russian sasha_kitchen_bree_8353bc98:

    bree.say "Только через мой труп."

translate russian sasha_kitchen_bree_87d21a72:

    sasha.say "Ты ничем не лучше."

translate russian sasha_kitchen_bree_87d21a72_1:

    sasha.say "Ты ничем не лучше."

translate russian sasha_kitchen_bree_b98d5813:

    sasha.say "Только не обижайся, когда застанешь меня с ним в постели..."

translate russian sasha_kitchen_bree_c252bc47:

    bree.say "Где есть место для одной, найдётся место и для двоих..."

translate russian sasha_kitchen_bree_cbe060b6:

    sasha.say "Следи за своей диетой."

translate russian sasha_kitchen_bree_e26964b9:

    bree.say "Тогда и узнаем, что произойдёт."

translate russian sasha_kitchen_bree_f3c2f3b3:

    bree.say "Я подумываю подкатить к [hero.name]."

translate russian sasha_livingroom_bree_82fe55f5:

    "Саша и [bree.name] беседуют на диване."

translate russian sasha_livingroom_bree_83b79c1d:

    "После моего вмешательства они прекращают спор."

translate russian sasha_livingroom_bree_91079b0f:

    "Я ненадолго присоединяюсь к ним."

translate russian sasha_livingroom_bree_b250e3cb:

    "Саша и [bree.name] о чём-то спорят."

translate russian sasha_request_c9ec908a:

    "Я снова киваю."

translate russian sasha_threesome_confrontation_c2d7cc03:

    "Мой рот двигается, но слов не выходит."

translate russian science_project_01_f1d8a63c:

    mike.say "Эм..."

translate russian science_project_03_30e74fc5:

    mike.say "Эм..."

translate russian science_project_03_30e74fc5_1:

    mike.say "Эм..."

translate russian science_project_03_6e154b71:

    mike.say "Ладно, ладно..."

translate russian science_project_03_80d3a831:

    mike.say "Прости!"

translate russian science_project_03_80d3a831_1:

    mike.say "Прости!"

translate russian science_project_03_80d3a831_2:

    mike.say "Прости!"

translate russian science_project_03_86d07102:

    mike.say "А..."

translate russian science_project_03_86d07102_1:

    mike.say "А..."

translate russian science_project_03_86d07102_2:

    mike.say "А..."

translate russian science_project_03_8fb73da4:

    mike.say "Я..."

translate russian science_project_03_8fb73da4_1:

    mike.say "Я..."

translate russian science_project_03_8fb73da4_2:

    mike.say "Я..."

translate russian science_project_03_de2ad759:

    mike.say "Что ты..."

translate russian science_project_04_e84ffc6f:

    mike.say "Что?"

translate russian scottie_greet_dialogues_male_6810e1f5:

    mike.say "Привет."

translate russian sexual_tension_bree_sam_200eb25b:

    mike.say "Эй!"

translate russian sexual_tension_sam_lexi_4cf775c5:

    mike.say "Что?"

translate russian sexual_tension_sam_minami_30e74fc5:

    mike.say "Эм..."

translate russian sexual_tension_sam_minami_f1d8a63c:

    mike.say "Эм..."

translate russian shark_attack_male_0110d469:

    "Срабатывает инстинкт: я начинаю грести руками и работать ногами."

translate russian shark_attack_male_028aada7:

    "Я лишь вполуха слушаю шум, доносящийся с берега."

translate russian shark_attack_male_028c42b5:

    "Вот, должно быть, что каждый день чувствовали такие парни, как Дуэйн."

translate russian shark_attack_male_087df9a0:

    "И она несётся прямо на меня с широко раскрытой пастью."

translate russian shark_attack_male_08e4c38f:

    "Над зияющей красной глоткой и рядами зазубренных, острых как бритва зубов на меня смотрят маленькие чёрные глаза."

translate russian shark_attack_male_0a6a9c08:

    "Обожаю, когда поход на пляж складывается настолько удачно."

translate russian shark_attack_male_0ee0f7e3:

    "Я стону и качаю головой: сейчас у меня совершенно нет ни времени, ни терпения выслушивать нотации от какой-то статистки из «Спасателей Малибу»."

translate russian shark_attack_male_19b53d85:

    "Наверное, из-за паники я беспомощно барахтаюсь, а не плыву."

translate russian shark_attack_male_1aaa509a:

    "Но почему-то вместо ускорения я, кажется, только замедляюсь."

translate russian shark_attack_male_282a3461:

    "Оглянувшись через плечо, я вижу спасательницу, которая словно в замедленной съёмке бежит ко мне по пляжу."

translate russian shark_attack_male_292a3e6a:

    "Я довольно хорошо плаваю, поэтому успеваю отплыть далеко ещё до того, как спасательница добегает до кромки воды."

translate russian shark_attack_male_2a197435:

    "Ну да, я и сам понимаю, что великолепно выгляжу, рассекая воду."

translate russian shark_attack_male_2e7cf637:

    "Сохраняя невозмутимый вид, я иду дальше, а волны начинают омывать мои ступни и щиколотки."

translate russian shark_attack_male_2f85f8b8:

    "Bather" "Это что..."

translate russian shark_attack_male_33b53cbe:

    "Когда вода поднимается выше колен, я начинаю готовиться к тому, чтобы поплыть."

translate russian shark_attack_male_35836e42:

    "Но к тому моменту уже поздно: я погружаюсь в океан пустоты."

translate russian shark_attack_male_35902697:

    "А заодно пасть с несколькими рядами острых как бритва зубов!"

translate russian shark_attack_male_360c25d6:

    "Теперь её голос заглушают ещё и волны, а я нарочно не оглядываюсь, продолжая плыть дальше."

translate russian shark_attack_male_3fcafcba:

    "И даже мне кажется, что это уже немного чересчур!"

translate russian shark_attack_male_46cd0f79:

    "Теперь мне приходится уже брести по воде, а не просто идти, поэтому я замедляюсь."

translate russian shark_attack_male_48639df7:

    "Крики отдыхающих на пляже с каждой секундой становятся всё тише."

translate russian shark_attack_male_4b7f5098:

    "Я изо всех сил стараюсь двигаться быстрее, но всё происходит слишком стремительно."

translate russian shark_attack_male_4b8feebf:

    "Правда, есть одна небольшая проблема."

translate russian shark_attack_male_4d1d737b:

    "Я довольно сильный пловец, поэтому без колебаний отплываю чуть дальше."

translate russian shark_attack_male_4e5edd94:

    "Я почти дохожу до места, где волны разбиваются о песок, когда слышу какой-то далёкий приглушённый крик."

translate russian shark_attack_male_55dc8bf4:

    "Bather" "АКУЛА!"

translate russian shark_attack_male_6228821e:

    "Простите, парни, я не виноват, что ваши девушки хотят урвать кусочек такого красавчика!"

translate russian shark_attack_male_62e4121f:

    "А значит, заодно я получаю ещё и бесплатную тренировку!"

translate russian shark_attack_male_63e738e1:

    "Но стоит мне это сделать, как я вижу торчащий из воды акулий плавник."

translate russian shark_attack_male_64c5ebc2:

    "Я ведь не могу весь день ходить по пляжу туда-сюда."

translate russian shark_attack_male_6616a488:

    "Потом всегда можно притвориться, будто я ничего не понял, и сказать, что она была слишком далеко и я не расслышал её."

translate russian shark_attack_male_666d5639:

    "Боли нет, но лишь потому, что у меня не остаётся времени осознать происходящее."

translate russian shark_attack_male_6857c2fa:

    "Как только ноги полностью скрываются под водой, я наклоняюсь вперёд и вытягиваю руки."

translate russian shark_attack_male_6a736424:

    "Я понимаю, что плавание станет идеальным решением."

translate russian shark_attack_male_732a3935:

    "Я уже чувствую, как напряжённо работают мышцы, пока я рассекаю воду."

translate russian shark_attack_male_741d92ae:

    "Надо мной нависает силуэт акулы, и её челюсти смыкаются быстрее, чем я мог представить для существа такого размера."

translate russian shark_attack_male_7ac488ac:

    "Все мои чувства разом захлёстывает такая буря ощущений, что всё сливается в мутное пятно."

translate russian shark_attack_male_7d23f515:

    "Bather" "Боже мой!"

translate russian shark_attack_male_7e1b5172:

    "Всего через пару шагов вода уже доходит до середины икр и продолжает подниматься."

translate russian shark_attack_male_80acfaca:

    "Что весьма некстати, ведь у акулы таких проблем нет."

translate russian shark_attack_male_860f0b00:

    "И тут мой взгляд падает на сверкающую морскую гладь."

translate russian shark_attack_male_8b02d9ed:

    "Я изо всех сил пытаюсь плыть к берегу как можно быстрее."

translate russian shark_attack_male_8b8e6e36:

    "Похоже, позади меня что-то огромное рассекает воду и стремительно нагоняет."

translate russian shark_attack_male_8bd497d1:

    "Пожалуй, единственная милость судьбы в том, что всё происходит чертовски быстро."

translate russian shark_attack_male_8f947e15:

    "Быстро прикинув, насколько она дальше от меня, чем море, я понимаю, что окажусь в воде задолго до того, как она подбежит."

translate russian shark_attack_male_931e894a:

    "После этого я уже не плыву, меня просто тащит сквозь воду."

translate russian shark_attack_male_93e46bc5:

    "Всё потому, что их девушки откровенно разглядывают меня прямо у них на глазах!"

translate russian shark_attack_male_94a2f3e8:

    "Оглядываясь вокруг, я пытаюсь придумать решение."

translate russian shark_attack_male_9ae164f0:

    "Всё вокруг бурлит: белая пена и красный цвет, который исходит уже не только из раскрытой пасти акулы."

translate russian shark_attack_male_9c7e5b9d:

    "Я прогуливаюсь по этому песку в своих лучших плавках и выгляжу превосходно."

translate russian shark_attack_male_a10e56ac:

    "Люди не только смогут продолжать смотреть на меня."

translate russian shark_attack_male_a1215901:

    "И вот я уже без всяких усилий плыву сквозь прохладную воду."

translate russian shark_attack_male_a12781a6:

    "Страх не парализует меня, но я впадаю в панику, и мои гребки превращаются в жалкое плавание по-собачьи."

translate russian shark_attack_male_a6edefcb:

    "Приняв решение, я пробегаю последние пару шагов по мелководью и ныряю, как только становится достаточно глубоко."

translate russian shark_attack_male_ad629f94:

    "Они ещё и смогут разглядеть моё тело, пока я плыву!"

translate russian shark_attack_male_ae032135:

    "В океан, из которого уже не вернуться."

translate russian shark_attack_male_aef2c233:

    "Но пока это продолжается, я выжму из каждой секунды всё возможное."

translate russian shark_attack_male_b0379a80:

    "Но вскоре я различаю новый звук, достаточно громкий, чтобы пробиться даже сквозь шум волн."

translate russian shark_attack_male_b40bada7:

    "Это акула. Огромная, уродливая и словно выползшая из кошмарного фильма."

translate russian shark_attack_male_b8da4362:

    "Не теряя времени, я поворачиваю к воде и захожу на мелководье."

translate russian shark_attack_male_bc350fc1:

    "Я поворачиваю голову, не желая верить собственным ушам."

translate russian shark_attack_male_bc45c37e:

    "Но люди на берегу уже начинают кричать и вопить."

translate russian shark_attack_male_bee05298:

    "А затем остаётся лишь тьма..."

translate russian shark_attack_male_c3561fdc:

    "Высоко в чистом голубом небе сияет солнце, заливая жаром золотой песок."

translate russian shark_attack_male_c459a082:

    "А я просто прохожу мимо с широкой улыбкой на лице."

translate russian shark_attack_male_ca84b0b1:

    "Мне нужно оставаться на виду у всех на пляже и при этом продолжать двигаться."

translate russian shark_attack_male_cbb3b92c:

    "И тут вижу нечто, из-за чего мгновенно загрязняю тот небольшой участок моря, где сейчас нахожусь."

translate russian shark_attack_male_cf944f6a:

    "Услышав изумлённые возгласы людей, я не могу удержаться от смешка."

translate russian shark_attack_male_d46ab8e3:

    "Остаётся лишь оттолкнуться, и я чувствую, как вода удерживает меня на поверхности."

translate russian shark_attack_male_d87623f5:

    "Несколько парней уже заметно закипают от злости."

translate russian shark_attack_male_daf184f1:

    "И не верьте мне на слово, достаточно посмотреть, сколько восхищённых взглядов я ловлю."

translate russian shark_attack_male_de71a83c:

    "И да, я понимаю, что это не будет длиться вечно."

translate russian shark_attack_male_e1b836b1:

    "Ещё мгновение, и глубина уже позволяет мне оторвать ноги от дна."

translate russian shark_attack_male_e26aa804:

    "Bather" "Там акула!"

translate russian shark_attack_male_e733a113:

    "Bather" "Да, это он!"

translate russian shark_attack_male_e9e7c8e8:

    "Решив, что это, скорее всего, другие спасатели на гидроциклах или небольшой лодке, я понимаю, что игра окончена."

translate russian shark_attack_male_f0149c2f:

    "Я не успеваю даже почувствовать боль, как её челюсти смыкаются на мне."

translate russian shark_attack_male_f01578be:

    "Поэтому, когда вокруг темнеет, сначала мне кажется, что это лишь очередная часть всеобщей путаницы."

translate russian shark_attack_male_f4cfc9ec:

    "Я оглядываюсь через плечо, готовый сдаться и прикинуться, будто ничего не знал."

translate russian shark_attack_male_fa6d9b9d:

    "Если продолжу, все поймут, что я просто красуюсь, и тогда всему конец."

translate russian shark_attack_male_fb1c213d:

    "Лишь когда ни одно из чувств не возвращается, я начинаю подозревать, что что-то не так."

translate russian shark_attack_male_fb49751b:

    "Вот, должно быть, что каждый день чувствуют такие парни, как Дуэйн."

translate russian shark_attack_male_fcb2b13b:

    "Bather" "Все из воды!"

translate russian shark_chan_pet_0110d469:

    "Срабатывает инстинкт: я начинаю грести руками и работать ногами."

translate russian shark_chan_pet_028aada7:

    "Я лишь вполуха слушаю шум и суматоху на берегу."

translate russian shark_chan_pet_028c42b5:

    "Ух ты, наверное, именно так каждый день своей жизни чувствовали себя парни вроде Дуэйна."

translate russian shark_chan_pet_0a6a9c08:

    "Обожаю, когда поездка на пляж складывается так удачно."

translate russian shark_chan_pet_146c8b15:

    "Но вместо этого чувствую, как что-то трётся о мою ладонь."

translate russian shark_chan_pet_17369123:

    "Наверняка некоторые гадают, какого чёрта я творю."

translate russian shark_chan_pet_183a44d2:

    "Но акула следует за мной до самого берега, приставая, словно назойливая собака."

translate russian shark_chan_pet_2553b530:

    "Но вряд ли мне удалось бы уплыть от акулы, даже если бы я попытался."

translate russian shark_chan_pet_2a197435:

    "Ну да, понимаю, что выгляжу эффектно, рассекая воду."

translate russian shark_chan_pet_2e6ef046:

    "Что там говорилось в «Как приручить свою акулу» о подобных ситуациях?"

translate russian shark_chan_pet_2e7cf637:

    "Сохраняя невозмутимый вид, я иду дальше, пока волны плещутся у ступней и щиколоток."

translate russian shark_chan_pet_2f85f8b8:

    "Bather" "Это что..."

translate russian shark_chan_pet_33b53cbe:

    "Когда вода поднимается выше колен, я начинаю готовиться плыть."

translate russian shark_chan_pet_35902697:

    "А заодно пасть с несколькими рядами острых как бритва зубов!"

translate russian shark_chan_pet_3a61ded1:

    "Когда я выхожу на пляж, все снова смотрят на меня."

translate russian shark_chan_pet_3fcafcba:

    "И даже мне кажется, что это уже немного чересчур!"

translate russian shark_chan_pet_41594c5e:

    "Хотя я их не виню, потому что чувствую то же самое."

translate russian shark_chan_pet_46cd0f79:

    "Теперь мне приходится уже брести по воде, а не просто идти, поэтому темп замедляется."

translate russian shark_chan_pet_47c535b3:

    "Что-то очень большое, с кожей, похожей на чёртову наждачную бумагу!"

translate russian shark_chan_pet_49d4b676:

    "На пляже всё ещё кричат."

translate russian shark_chan_pet_4b8feebf:

    "Хотя здесь есть небольшая проблема."

translate russian shark_chan_pet_4d1d737b:

    "Я довольно сильный пловец, поэтому не боюсь отплыть немного подальше."

translate russian shark_chan_pet_55dc8bf4:

    "Bather" "АКУЛА!"

translate russian shark_chan_pet_569d7d84:

    "Так что остаётся лишь надеяться, что это сработает."

translate russian shark_chan_pet_591e86b4:

    "Они ещё и смогут любоваться моим телом, пока я плаваю!"

translate russian shark_chan_pet_622182b7:

    "Прямо передо мной в воде неподвижно висит акула."

translate russian shark_chan_pet_6228821e:

    "Простите, парни, не моя вина, что ваши девушки хотят откусить кусочек этого красавчика!"

translate russian shark_chan_pet_62e4121f:

    "Получается, вдобавок я ещё и бесплатно тренируюсь!"

translate russian shark_chan_pet_63e738e1:

    "Но стоит мне это сделать, как я вижу торчащий из воды акулий плавник."

translate russian shark_chan_pet_64c5ebc2:

    "Я ведь не могу весь день ходить по пляжу туда-сюда."

translate russian shark_chan_pet_6857c2fa:

    "Как только ноги полностью скрываются под водой, я наклоняюсь вперёд и вытягиваю руки."

translate russian shark_chan_pet_69bebbc7:

    "В конце концов мне удаётся выбраться обратно на берег, на безопасную сушу."

translate russian shark_chan_pet_6a736424:

    "Я понимаю, что плавание идеально решает проблему."

translate russian shark_chan_pet_732a3935:

    "Я уже чувствую, как мышцы напрягаются, пока я рассекаю воду."

translate russian shark_chan_pet_7419d217:

    "От этого она, кажется, становится ещё дружелюбнее."

translate russian shark_chan_pet_77c07f5c:

    "Не раздумывая, я начинаю гладить и похлопывать акулу по носу."

translate russian shark_chan_pet_7d23f515:

    "Bather" "Боже мой!"

translate russian shark_chan_pet_7e1b5172:

    "Через каких-то пару шагов вода уже доходит до середины икр и продолжает подниматься."

translate russian shark_chan_pet_860f0b00:

    "И тут мой взгляд падает на мерцающую морскую воду."

translate russian shark_chan_pet_8e0bb229:

    "Поморщившись и зажмурившись, я выставляю перед собой руку."

translate russian shark_chan_pet_918d9b62:

    "Пока акула несётся на меня, я принимаю нужную позу."

translate russian shark_chan_pet_93e46bc5:

    "Ведь их девушки разглядывают меня прямо у них на глазах!"

translate russian shark_chan_pet_94a2f3e8:

    "Оглядываясь по сторонам, я пытаюсь придумать решение."

translate russian shark_chan_pet_95022b1e:

    "Ага, кажется, всё зависит от того, как именно расположиться в воде."

translate russian shark_chan_pet_9988a071:

    "Честно говоря, я ожидаю открыть глаза и увидеть вместо неё окровавленный обрубок."

translate russian shark_chan_pet_9c7e5b9d:

    "По этому песку я иду в своих лучших плавках и выгляжу просто великолепно."

translate russian shark_chan_pet_9f03b78f:

    "И трётся мордой о мою руку, словно пёс, отчаянно требующий внимания!"

translate russian shark_chan_pet_a10e56ac:

    "Люди не только смогут меня видеть."

translate russian shark_chan_pet_a1215901:

    "И вот я уже без труда плыву сквозь прохладную воду."

translate russian shark_chan_pet_a5dae41c:

    "Но тут вспоминаю, что недавно прочитал книгу, которая может мне помочь."

translate russian shark_chan_pet_aef2c233:

    "Но я собираюсь наслаждаться каждой секундой, пока это продолжается."

translate russian shark_chan_pet_b8da4362:

    "Не теряя времени, я поворачиваюсь к морю и захожу на мелководье."

translate russian shark_chan_pet_bc350fc1:

    "Я поворачиваю голову, не желая верить собственным ушам."

translate russian shark_chan_pet_bc45c37e:

    "Но люди на берегу уже начинают кричать и вопить."

translate russian shark_chan_pet_bd995f5e:

    "Только теперь уже скорее от полного изумления и недоверия."

translate russian shark_chan_pet_c3561fdc:

    "Солнце высоко в чистом голубом небе и палит золотистый песок."

translate russian shark_chan_pet_c459a082:

    "А я лишь прохожу мимо с широченной ухмылкой на лице."

translate russian shark_chan_pet_ca84b0b1:

    "Мне нужно оставаться у всех на виду и при этом продолжать двигаться."

translate russian shark_chan_pet_cf944f6a:

    "И невольно усмехаюсь, слыша изумлённые возгласы."

translate russian shark_chan_pet_d46ab8e3:

    "Остаётся лишь оттолкнуться, и я чувствую, как вода поддерживает моё тело."

translate russian shark_chan_pet_d87623f5:

    "Не один парень сейчас буквально кипит от злости."

translate russian shark_chan_pet_daf184f1:

    "И не верьте мне на слово, взгляните, сколько восхищённых взглядов я ловлю."

translate russian shark_chan_pet_de71a83c:

    "И да, я понимаю, что это не будет длиться вечно."

translate russian shark_chan_pet_e1b836b1:

    "Ещё мгновение, и становится достаточно глубоко, чтобы оторвать ноги от дна."

translate russian shark_chan_pet_e26aa804:

    "Bather" "Там акула!"

translate russian shark_chan_pet_e733a113:

    "Bather" "Да, точно!"

translate russian shark_chan_pet_ebac4027:

    "Открыв сначала один глаз, а затем другой, я не могу поверить увиденному."

translate russian shark_chan_pet_f5481a10:

    "Я уже собираюсь в отчаянии плыть к берегу."

translate russian shark_chan_pet_fa6d9b9d:

    "Если продолжу, все поймут, что я просто красуюсь, и волшебство закончится."

translate russian shark_chan_pet_fb49751b:

    "Ух ты, наверное, именно так каждый день своей жизни чувствуют себя парни вроде Дуэйна."

translate russian shark_chan_pet_fcb2b13b:

    "Bather" "Все из воды!"

translate russian shibari_skill_book_2a6a27cf:

    "Я изучаю сибари. ([skill]%%)"

translate russian shibari_skill_book_48bc7f16:

    "Я уже знаю о сибари всё необходимое."

translate russian shiori_teaser_1168b1f5:

    "Она закончила свою речь, и теперь говорить должен я."

translate russian shiori_teaser_1341f718:

    mike.say "Боюсь, я не смогу предложить вам эту должность."

translate russian shiori_teaser_14640f74:

    "Можете назвать меня сексистом, но внешне они тоже все были болезненно обычными."

translate russian shiori_teaser_15e7e805:

    shiori.say "Я допустила ошибку?"

translate russian shiori_teaser_18cabe6b:

    shiori.say "А вы, должно быть, мистер [hero.family_name]."

translate russian shiori_teaser_1a9ed2c9:

    "И не могу избавиться от мысли, что только что упустил нечто особенное."

translate russian shiori_teaser_1e217fd0:

    "Через мгновение она уже на ногах и почти выбегает из кабинета."

translate russian shiori_teaser_1fa42bf2:

    "Похоже, она действительно рада, что ей дали шанс."

translate russian shiori_teaser_214c3c61:

    "Но голос настолько тихий и робкий, что я качаю головой, уже заранее списывая её со счетов."

translate russian shiori_teaser_24dc2d8e:

    "Она краснеет и скромно отводит взгляд, отчего выглядит обезоруживающе."

translate russian shiori_teaser_286dd121:

    mike.say "Спасибо, что пришли."

translate russian shiori_teaser_2ff9d612:

    shiori.say "Я тоже так думаю, мистер [hero.family_name]. Не могу дождаться, когда вы дадите мне работу!"

translate russian shiori_teaser_7ada205f:

    mike.say "П... правда, Сиори?"

translate russian shiori_teaser_30a380f2:

    "Она слегка кланяется в пояс."

translate russian shiori_teaser_39efe7e2:

    "Всё стремительно катится к провалу."

translate russian shiori_teaser_44e6c414:

    shiori.say "Но если я окажусь под руководством правильного мужчины, вы не поверите, на что я способна..."

translate russian shiori_teaser_82a73e37:

    shiori.say "П... правда?!"

translate russian shiori_teaser_48df5fd9:

    shiori.say "Мне говорили, что я очень гибкая."

translate russian shiori_teaser_4a29fbe7:

    "И это оказывает весьма заметный эффект на её грудь."

translate russian shiori_teaser_4e3520ce:

    shiori.say "А, что-то не так, мистер [hero.family_name]?"

translate russian shiori_teaser_4e43f120:

    mike.say "Да, входите!"

translate russian shiori_teaser_4f528617:

    "Чёрт, точно. Я же провожу собеседование на новую должность секретаря."

translate russian shiori_teaser_1c48a590:

    mike.say "Присаживайтесь и расскажите о себе... Сиори."

translate russian shiori_teaser_5ceb2426:

    "После третьей кандидатки я сбился со счёта."

translate russian shiori_teaser_5ed93259:

    "Несмотря на мою неуклюжую болтовню, Сиори, похоже, не замечает сексуального напряжения, которое я чувствую."

translate russian shiori_teaser_5ff6aec2:

    mike.say "Потому что, думаю, ты идеально подходишь для этой работы."

translate russian shiori_teaser_60bc0d80:

    shiori.say "Это было ОЧЕНЬ короткое собеседование, мистер [hero.family_name]!"

translate russian shiori_teaser_620dd134:

    shiori.say "Если вы меня наймёте, я смогу называть вас так постоянно, мистер [hero.family_name]!"

translate russian shiori_teaser_669bf373:

    "И вдобавок, возможно, с самой огромной грудью, которую я когда-либо видел!"

translate russian shiori_teaser_6a420307:

    "Пунктуальные, эффективные, профессиональные и раздражающе бодрые."

translate russian shiori_teaser_6a755d56:

    "Я смотрю, как при ходьбе покачиваются её бёдра и подпрыгивает грудь."

translate russian shiori_teaser_6ac95c5c:

    shiori.say "Вы можете поставить меня практически в любую позу... то есть на любую должность."

translate russian shiori_teaser_6d44702a:

    "Я качаю головой и пожимаю плечами, стараясь выглядеть как можно непринуждённее."

translate russian shiori_teaser_a03b8833:

    mike.say "Эм... что ж, Сиори."

translate russian shiori_teaser_72581720:

    "Сиори смотрит на меня широко раскрытыми от удивления огромными глазами."

translate russian shiori_teaser_76482472:

    "А улыбка, которой она отвечает, услышав его..."

translate russian shiori_teaser_767f5941:

    "Она улыбается, и улыбка выглядит искренней."

translate russian shiori_teaser_76d0fe59:

    "Придя в себя, я понимаю, что совершенно не знаю, о чём только что говорили."

translate russian shiori_teaser_785992a7:

    mike.say "Ничего страшного, Сиори."

translate russian shiori_teaser_c6a6d16a:

    shiori.say "Я... я должна быть честна, мистер [hero.family_name]."

translate russian shiori_teaser_7a8a2d72:

    "Shiori" "Я по поводу должности секретаря."

translate russian shiori_teaser_7fefd4bc:

    "Нет, нужно сосредоточиться и вести себя профессионально!"

translate russian shiori_teaser_80670830:

    mike.say "Оставьте всё мне, и примерно через неделю вы получите ответ."

translate russian shiori_teaser_80eea4ff:

    "Я чувствую, как начинаю оттягивать воротник."

translate russian shiori_teaser_830bb7b6:

    "При каждом шаге её бёдра покачиваются, а грудь подпрыгивает."

translate russian shiori_teaser_849d306f:

    "Слово «должность» мгновенно вызывает в голове образ, достойный подростка."

translate russian shiori_teaser_87fce5e4:

    "Кого-то искреннего, от кого не несёт притворством?"

translate russian shiori_teaser_67a077cd:

    mike.say "Мне... мне просто нравится, когда вы называете меня «мистер [hero.family_name]», вот и всё."

translate russian shiori_teaser_8a14d1fc:

    "Он резко контрастирует с монотонным голосом, который едва не усыпил меня."

translate russian shiori_teaser_8b3432aa:

    "Сиори подскакивает, словно игрушка из коробки."

translate russian shiori_teaser_7cde3ee6:

    "Shiori" "О... боже..."

translate russian shiori_teaser_911fd142:

    "Неужели так сложно найти настоящего живого человека?"

translate russian shiori_teaser_92adedd1:

    "Почти всё, что она говорит, звучит как двусмысленность."

translate russian shiori_teaser_938af83b:

    shiori.say "Тогда увидимся утром, мистер [hero.family_name]. Я приду пораньше!"

translate russian shiori_teaser_93e5ee08:

    "И от этого кажется ещё милее..."

translate russian shiori_teaser_943773c3:

    mike.say "Наверное, я просто перепутал время!"

translate russian shiori_teaser_94ead517:

    "Но, думаю, мы оба уже понимаем, что работу она не получит."

translate russian shiori_teaser_a411bf2c:

    mike.say "А... з... забудьте, что я только что сказал."

translate russian shiori_teaser_986180c9:

    "Shiori" "Меня зовут Сиори."

translate russian shiori_teaser_497a2892:

    mike.say "ДА... то есть да, это я."

translate russian shiori_teaser_9a8e4d1b:

    "Стук в дверь кабинета резко прекращает моё саможаление."

translate russian shiori_teaser_9efb4cbe:

    "Внезапный кашель по другую сторону стола возвращает меня к реальности."

translate russian shiori_teaser_a0ffc87b:

    shiori.say "У меня не самое впечатляющее резюме."

translate russian shiori_teaser_a47ae597:

    "Она кивает слишком поспешно, чтобы это выглядело искренне."

translate russian shiori_teaser_a4b9abc9:

    "Я откидываюсь в кресле и со стоном смотрю на гору заявлений на столе."

translate russian shiori_teaser_189f692f:

    "Я... я должен сохранять ясную голову и вести себя профессионально!"

translate russian shiori_teaser_a698d113:

    mike.say "Просто у меня хорошее предчувствие насчёт тебя, Сиори, понимаешь?"

translate russian shiori_teaser_a7aa9271:

    "Я едва удерживаюсь от смешка."

translate russian shiori_teaser_ade83dcd:

    "Начав паниковать, я вижу лишь один надёжный способ выбраться из этой ситуации."

translate russian shiori_teaser_af6c1f5d:

    "Миниатюрная девушка азиатского происхождения с большими глазами и чёрными волосами."

translate russian shiori_teaser_b06e4d3a:

    mike.say "Я вижу, что всё может прекрасно сложиться: я сверху, а ты..."

translate russian shiori_teaser_b29eadc0:

    "Её имя так приятно звучит, когда я произношу его вслух."

translate russian shiori_teaser_eebb16f1:

    mike.say "Т... тогда привыкай выполнять каждое моё распоряжение, Сиори."

translate russian shiori_teaser_b77e2918:

    "Мне остаётся лишь улыбнуться девушке, которая теперь смотрит на меня в ожидании ответа."

translate russian shiori_teaser_b99f61df:

    "И теперь все они начинают сливаться в одну!"

translate russian shiori_teaser_bbdc3e72:

    mike.say "Простите, вам придётся вернуться завтра..."

translate russian shiori_teaser_bf2c5bc9:

    mike.say "Нет, Сиори, всё в порядке."

translate russian shiori_teaser_c2ff8d05:

    "Я провожаю Сиори взглядом, пока она выходит из кабинета."

translate russian shiori_teaser_c3526e3e:

    "По сути, бесконечная вереница клонов, говорящих мне именно то, что, по их мнению, я хочу услышать."

translate russian shiori_teaser_c4fb12b5:

    "И тут я впервые поднимаю взгляд и вижу её."

translate russian shiori_teaser_c739ef8a:

    mike.say "Ого, вот это презентация!"

translate russian shiori_teaser_ca6a7201:

    "Я понимаю, что во время её поклона не смог удержаться и заглянул ей в декольте."

translate russian shiori_teaser_ca8f8648:

    "И я понимаю, что буду думать о ней до самой нашей встречи завтра утром."

translate russian shiori_teaser_cc11ec25:

    "Это ощущается почти как физический удар."

translate russian shiori_teaser_80c38427:

    shiori.say "О... я... я и не знала!"

translate russian shiori_teaser_cea143f8:

    "Тут я замечаю, что она слегка покраснела."

translate russian shiori_teaser_d020e8b6:

    shiori.say "Когда я приступаю?"

translate russian shiori_teaser_3e637329:

    mike.say "Т... то есть ты подо мной... работаешь под моим руководством!"

translate russian shiori_teaser_d264bafe:

    "Вот чёрт, она думает, что я над ней смеюсь!"

translate russian shiori_teaser_d2c98c5e:

    "Да, каждая была довольно симпатичной, но я не смог бы опознать ни одну из них в полицейской линейке."

translate russian shiori_teaser_d5c7c1c9:

    "Я отрываю взгляд от груди Сиори и указываю на стул."

translate russian shiori_teaser_d66cbda7:

    "Даже если бы от этого зависела моя жизнь..."

translate russian shiori_teaser_d8a366ac:

    "Мы обмениваемся натянутыми профессиональными улыбками."

translate russian shiori_teaser_a6292516:

    "Shiori" "Это... это сюда?"

translate russian shiori_teaser_db2c772c:

    "Сиори начинает ёрзать на стуле и избегать зрительного контакта."

translate russian shiori_teaser_e95f4ecc:

    shiori.say "Конечно, мистер [hero.family_name]!"

translate russian shiori_teaser_fa96398b:

    "Она... она со мной флиртует?!"

translate russian shiori_teaser_eb16b816:

    mike.say "Как можно скорее. Как насчёт завтрашнего утра?"

translate russian shiori_teaser_ee43ba3f:

    "Я устало стону и провожу ладонями по лицу."

translate russian shiori_teaser_fab6fc20:

    shiori.say "О да, мистер [hero.family_name]."

translate russian shop_with_231de2c9:

    active_girl.say "Прости, мне сейчас не хочется."

translate russian shop_with_b778778c:

    active_girl.say "Конечно, почему бы и нет?"

translate russian shop_with_d9e44614:

    "Я отправляюсь за покупками вместе с [active_girl.name]."

translate russian shovel_snow_53482e14:

    "Я убираю снег лопатой."

translate russian slap_238098d7:

    "Я шлёпаю [active_girl.name] по заднице."

translate russian slap_9d67642c:

    active_girl.say "Что ты делаешь?"

translate russian slap_a48b1c01:

    "Она улыбается и краснеет..."

translate russian sleep_3e989193:

    "Я чувствую, что полностью отдохнул."

translate russian sleep_5294248b:

    "Звонит будильник."

translate russian sleep_c80b71e7:

    "Хр-р-р...{w=1}{nw}"

translate russian sleep_dream_9cb8de10:

    "Мне приснился приятный сон."

translate russian sleep_nightmare_666f0c94:

    "Какой ужасный кошмар..."

translate russian sm_skill_book_3845b9f6:

    "Я уже знаю о садомазохизме всё необходимое."

translate russian sm_skill_book_d4f7f47d:

    "Я изучаю БДСМ. ([skill]%%)"

translate russian smartphone_booty_call_3512255f:

    "Нет ответа."

translate russian smartphone_booty_call_6fd260f5:

    smartphone_girl.say "Да ни за что!"

translate russian smartphone_booty_call_aa988b41:

    "Я звоню [girl.name]."

translate russian smartphone_booty_call_fcb7922a:

    smartphone_girl.say "Конечно."

translate russian smartphone_call_039ece2a:

    kylie.say "Сплю у себя в кровати. А где мне ещё быть?"

translate russian smartphone_call_0aa0f7a9:

    smartphone_girl.say "Я в лесу."

translate russian smartphone_call_0cf3ff17:

    smartphone_girl.say "Да?"

translate russian smartphone_call_111b9b1d:

    smartphone_girl.say "Я в лаунж-баре."

translate russian smartphone_call_11c39609:

    "[girl.subject_pronoun.capitalize()] не берёт трубку."

translate russian smartphone_call_212d56e1:

    smartphone_girl.say "Я в аквапарке."

translate russian smartphone_call_21a51aa3:

    smartphone_girl.say "Я в панк-баре в центре города."

translate russian smartphone_call_221c30c1:

    smartphone_girl.say "Я на картодроме."

translate russian smartphone_call_2972a05c:

    smartphone_girl.say "Я в спортзале."

translate russian smartphone_call_30b88485:

    smartphone_girl.say "Я в больнице."

translate russian smartphone_call_3313a28a:

    smartphone_girl.say "Я в кафе с горничными."

translate russian smartphone_call_3512255f:

    "Нет ответа."

translate russian smartphone_call_3c08c8ef:

    smartphone_girl.say "Я в секс-шопе."

translate russian smartphone_call_3f3b91f1:

    smartphone_girl.say "Я в ресторане."

translate russian smartphone_call_470054b3:

    smartphone_girl.say "Я в кинотеатре."

translate russian smartphone_call_56151f07:

    kylie.say "Кто вообще стал бы так делать..."

translate russian smartphone_call_59685141:

    smartphone_girl.say "Даже не надейся. Это ты приезжай ко мне, а не я к тебе!"

translate russian smartphone_call_5dc94626:

    smartphone_girl.say "Я в ночном клубе."

translate russian smartphone_call_6322bdd8:

    smartphone_girl.say "Я дома."

translate russian smartphone_call_64526f24:

    kylie.say "Шучу!"

translate russian smartphone_call_81bb2dd3:

    smartphone_girl.say "Я в парке аттракционов."

translate russian smartphone_call_82f5b49d:

    smartphone_girl.say "Я в парке."

translate russian smartphone_call_83b5f4ba:

    smartphone_girl.say "Уверена, тебя это совершенно не касается."

translate russian smartphone_call_8621df7e:

    smartphone_girl.say "Я в океанариуме."

translate russian smartphone_call_862a9db2:

    smartphone_girl.say "Прости, но я сейчас работаю..."

translate russian smartphone_call_885ab4e0:

    smartphone_girl.say "Кажется, я немного заблудилась."

translate russian smartphone_call_977998bf:

    smartphone_girl.say "Я в стриптиз-клубе."

translate russian smartphone_call_9ba56aa2:

    smartphone_girl.say "Ладно! Уже иду."

translate russian smartphone_call_aa28b85f:

    smartphone_girl.say "Попробуй угадать."

translate russian smartphone_call_aa988b41:

    "Я звоню [girl.name]."

translate russian smartphone_call_b979dcbe:

    smartphone_girl.say "Я на пляже."

translate russian smartphone_call_ba3e7a5e:

    smartphone_girl.say "Я в торговом центре."

translate russian smartphone_call_c709b85e:

    smartphone_girl.say "Я в церкви."

translate russian smartphone_call_cb5db8c9:

    smartphone_girl.say "Я в пабе."

translate russian smartphone_call_d12ff108:

    smartphone_girl.say "Я на работе."

translate russian smartphone_call_d14da8d7:

    kylie.say "Смотрю на тебя из окна..."

translate russian smartphone_call_d25423ea:

    kylie.say "Я точно не стою перед твоим домом."

translate russian smartphone_call_dc7eb02e:

    smartphone_girl.say "Я на кладбище."

translate russian smartphone_call_e6f0cdad:

    smartphone_girl.say "Я в городе."

translate russian smartphone_call_eec3dff4:

    smartphone_girl.say "Я репетирую в студии."

translate russian smartphone_call_f69dd73c:

    smartphone_girl.say "Я отправилась в небольшую поездку."

translate russian smartphone_call_f77621d4:

    smartphone_girl.say "Я на железнодорожном вокзале."

translate russian smartphone_call_f98518ee:

    smartphone_girl.say "Я в гараже."

translate russian smartphone_call_fab94e0e:

    smartphone_girl.say "Я в университете."

translate russian smartphone_call_fd0509e5:

    smartphone_girl.say "Я в полицейском участке."

translate russian smartphone_send_dirty_text_40f1ad8b:

    "Я отправляю [girl.name] сообщение."

translate russian smartphone_send_dirty_text_574e3ae4:

    "Она не отвечает..."

translate russian smartphone_send_dirty_text_a20cefa7:

    "..."

translate russian smartphone_send_flirty_text_40f1ad8b:

    "Я отправляю [girl.name] сообщение."

translate russian smartphone_send_flirty_text_92c30ed9:

    "[girl.subject_pronoun.capitalize()] не отвечает..."

translate russian smartphone_send_flirty_text_a20cefa7:

    "..."

translate russian smartphone_send_friendly_text_40f1ad8b:

    "Я отправляю [girl.name] сообщение."

translate russian smartphone_send_friendly_text_92c30ed9:

    "[girl.subject_pronoun.capitalize()] не отвечает..."

translate russian smartphone_send_friendly_text_a20cefa7:

    "..."

translate russian sporty_blowjob_sex_f1d8a63c:

    mike.say "Эм..."

translate russian sporty_harem_event_02_30e74fc5:

    mike.say "Эм..."

translate russian study_classroom_d9aaad99:

    "[s]"

translate russian study_with_0236a9f7:

    active_girl.say "Вообще-то да!"

translate russian study_with_1375bfe9:

    active_girl.say "У меня всё хорошо."

translate russian study_with_a4a96ac0:

    "Я помогаю [active_girl.name] с учёбой."

translate russian study_with_dialogues_1_male_3851180b:

    mike.say "[active_girl.name], тебе помочь?"

translate russian sweep_leaves_81d61e3c:

    "Я подметаю листья."

translate russian swim_609f90e1:

    "Девушки не могут отвести от меня глаз, пока я плаваю."

translate russian swim_8772f875:

    "[successes[0].name] не может отвести от меня глаз, пока я плаваю."

translate russian swim_b35e886c:

    "[successes[0].name] не может отвести от меня глаз, пока я плаваю."

translate russian swim_de25d256:

    "Они не могут отвести от меня глаз, пока я плаваю."

translate russian take_a_bath_69911ecb:

    "Мы приятно и спокойно проводим время в ванной."

translate russian take_a_shower_gym_3d83271a:

    "Я принимаю душ..."

translate russian takeanappark_57fefccf:

    "Я дремлю на скамейке."

translate russian talk_d59fd609:

    "Нам не о чём говорить."

translate russian taming_bondage_ayesha_fuck_c68cc434:

    mike.say "Ох, чёрт..."

translate russian taming_event_03_a_1c0d45e8:

    mike.say "Ну..."

translate russian taming_event_03_a_1c0d45e8_1:

    mike.say "Ну..."

translate russian taming_event_03_a_1c0d45e8_2:

    mike.say "Ну..."

translate russian taming_event_03_a_1c0d45e8_3:

    mike.say "Ну..."

translate russian taming_event_03_a_1c0d45e8_4:

    mike.say "Ну..."

translate russian taming_event_03_a_1c0d45e8_5:

    mike.say "Ну..."

translate russian taming_event_03_a_3ba2622c:

    "Ну вот, опять!"

translate russian taming_event_03_a_6757cf6b:

    mike.say "Ну..."

translate russian taming_event_03_b_be946dca:

    mike.say "Эм... да..."

translate russian taming_event_03_b_1c0d45e8:

    mike.say "Ну..."

translate russian taming_event_03_b_1c0d45e8_1:

    mike.say "Ну..."

translate russian taming_event_03_b_1c0d45e8_2:

    mike.say "Ну..."

translate russian taming_event_03_b_1c0d45e8_3:

    mike.say "Ну..."

translate russian taming_event_03_b_6757cf6b:

    mike.say "Ну..."

translate russian taming_event_03_b_6757cf6b_1:

    mike.say "Ну..."

translate russian taming_event_03_b_6e154b71:

    mike.say "Ладно, ладно..."

translate russian taming_event_03_b_f1d8a63c:

    mike.say "Эм..."

translate russian taming_event_03_c_1c0d45e8:

    mike.say "Ну..."

translate russian taming_event_03_c_3ba2622c:

    "Ну вот, опять!"

translate russian taming_event_03_c_3f8382ca:

    mike.say "Ого..."

translate russian taming_event_03_c_6757cf6b:

    mike.say "Ну..."

translate russian taming_event_03_c_700f54ac:

    mike.say "Вот так..."

translate russian taming_event_03_c_89d2bf47:

    mike.say "Нужно..."

translate russian taming_event_03_c_8fb73da4:

    mike.say "Я..."

translate russian taming_event_04_a63dbdf0:

    "Она смеётся и качает головой."

translate russian taming_event_05_200eb25b:

    mike.say "Эй!"

translate russian taming_event_05_8fb73da4:

    mike.say "Я..."

translate russian taming_event_05_8fb73da4_1:

    mike.say "Я..."

translate russian taming_event_05_d0d5644c:

    "Ого..."

translate russian taming_event_05_d0d5644c_1:

    "Ого..."

translate russian taming_event_2_1ccab2e1:

    mike.say "Хм..."

translate russian taming_event_2_1ccab2e1_1:

    mike.say "Хм..."

translate russian taming_threesome_fuck_200eb25b:

    mike.say "Эй!"

translate russian taming_threesome_fuck_c155a10d:

    mike.say "Эй..."

translate russian taming_threesome_kylie_fuck_437a01ea:

    mike.say "Ох, чёрт..."

translate russian taming_threesome_kylie_fuck_c68cc434:

    mike.say "Ох, чёрт..."

translate russian thinkpark_1e7be2f5:

    "Я немного размышляю о жизни, Вселенной и всём остальном..."

translate russian tickle_7f4a1b6a:

    "Я щекочу [active_girl.name]."

translate russian train_beach_01613e63:

    "Не успеваю я ответить какой-нибудь подобающей колкостью, как снова вскрикиваю: очередной краб вцепился мне в палец."

translate russian train_beach_0653ef22:

    mike.say "Я вижу лишь пару крабов, Мастер."

translate russian train_beach_09c4b758:

    master.say "Для начала самое важное!"

translate russian train_beach_0b3a1cec:

    "Именно этим я оправдываю то, что от неожиданного голоса Мастера подпрыгиваю и визжу как маленькая девочка."

translate russian train_beach_0cad6ba0:

    master.say "Поэтому именно они станут самым сложным испытанием!"

translate russian train_beach_0d1fced7:

    "Большинство тех, кого мне всё же удаётся поймать, умудряются ущипнуть меня за палец и вылетают из воды, когда я вскрикиваю от боли."

translate russian train_beach_0dfcc48f:

    "Ту, где затравленный парень учится сокрушительному удару ногой, балансируя на такой же свае?"

translate russian train_beach_0e82f257:

    "Он машет мне рукой, и я направляюсь к нему, ускоряя шаг, когда понимаю, что он торопит меня."

translate russian train_beach_106c5b7d:

    "Я прищуриваюсь, подозревая, что здесь куда больше похоти, чем скрытности."

translate russian train_beach_13d33a86:

    master.say "А вот и ты, мой ученик!"

translate russian train_beach_148727a4:

    "Несмотря на все мои возражения, Мастер заставляет меня замолчать и продолжает настаивать."

translate russian train_beach_1540d53c:

    master.say "Теперь залезай в яму."

translate russian train_beach_15f54d13:

    master.say "Теперь, когда начнётся прилив, ты научишься быть таким же стойким, как само море!"

translate russian train_beach_17fb651c:

    "Мастер замечает мой энтузиазм и одобрительно кивает."

translate russian train_beach_217decfe:

    master.say "А теперь делай, что тебе велено!"

translate russian train_beach_25579b92:

    "Лишь когда я наконец встаю и разминаю затёкшую спину, чувство достижения исчезает."

translate russian train_beach_27dd7709:

    master.say "В яму. ЖИВО!"

translate russian train_beach_2f34d93b:

    master.say "Прекрасно. Теперь врата духовного храма открыты!"

translate russian train_beach_31026257:

    master.say "Во времена самураев эти легендарные японские воины с той же целью занимались составлением цветочных композиций."

translate russian train_beach_36367efd:

    "Желая получить хоть что-то за свои деньги, я выполняю приказ."

translate russian train_beach_367a7390:

    master.say "Что ж, думаю, урок усвоен превосходно!"

translate russian train_beach_36eacda1:

    master.say "Сегодняшний урок будет посвящён скрытности и уклонению."

translate russian train_beach_3aed8bc5:

    master.say "Снимай обувь и забирайся наверх. Живо!"

translate russian train_beach_4e9c4ee4:

    mike.say "Кх... гх... помогите!"

translate russian train_beach_3c32c553:

    "И тут я вижу Мастера с ведром, в которое он складывает крабов, снимая их с камней."

translate russian train_beach_3ca4ff43:

    "Освободив их, я наконец вытаскиваю себя из песка, продолжая кашлять и тяжело дышать."

translate russian train_beach_3ddd78b3:

    "Если я вернусь после этого задания и меня не арестуют за подглядывание, клянусь заодно проверить слух самого Мастера."

translate russian train_beach_40353860:

    "Почувствовав деньги на ладони, Мастер радостно хихикает и кивает."

translate russian train_beach_40cfbe5c:

    master.say "Для этого возьми фотоаппарат и незаметно сфотографируй ничего не подозревающих отдыхающих на пляже."

translate russian train_beach_46f04876:

    "Он указывает на песок у своих ног, явно ожидая, что я буквально выкопаю описанную им яму."

translate russian train_beach_480428e2:

    master.say "Краб, мальчик, является совершеннейшим природным подобием воина в доспехах!"

translate russian train_beach_48c1d755:

    "Клянусь, ещё мгновение назад, когда я отвернулся, вокруг не было ни души, насколько хватало глаз."

translate russian train_beach_4b19abf9:

    "Я выжидающе смотрю на него, надеясь узнать хотя бы тему сегодняшнего урока или причину, по которой рядом с ним стоят ведёрко и лопатка."

translate russian train_beach_4c880332:

    mike.say "Ничего особенного..."

translate russian train_beach_4da2fb01:

    "Я нахожу Мастера сидящим на песке со скрещёнными ногами, словно он ждал моего прихода."

translate russian train_beach_4ef53dd3:

    "Он с улыбкой наблюдает, как застал меня врасплох, явно довольный тем, что добился такой реакции."

translate russian train_beach_5254f346:

    "Мастер ухмыляется и протягивает мне руку с ведёрком и лопаткой."

translate russian train_beach_55804728:

    "Взрослый мужик строит замки из песка по приказу безумного старого хрыча!"

translate russian train_beach_55aaccbb:

    master.say "Постарайся сделать как можно больше удачных снимков молодых девушек в бикини."

translate russian train_beach_598d7667:

    "Он уходит, продолжая посмеиваться, а мне приходится на четвереньках ползти обратно к машине и проклинать его последними словами."

translate russian train_beach_5d95cecb:

    "Как только я заканчиваю, он костлявым пальцем указывает на дно ямы."

translate russian train_beach_5fd4671d:

    master.say "Составлять цветочные композиции или строить замки из песка, никакой разницы."

translate russian train_beach_619769fd:

    "Неизвестно откуда он достаёт лопату и протягивает её мне."

translate russian train_beach_61a7e994:

    "Он молча протягивает руку и ждёт, пока я не достаю пачку купюр и не кладу её ему на ладонь."

translate russian train_beach_69d8d893:

    "А именно попытаюсь незаметно подкрасться и раскроить ему череп его же фотоаппаратом."

translate russian train_beach_6a2a1d53:

    master.say "Доброе утро, мой мальчик."

translate russian train_beach_6b75c95b:

    "При нём нет ничего, кроме яркого детского ведёрка и лопатки, какие обычно берут с собой на пляж."

translate russian train_beach_6d1513b1:

    "Первые несколько волн не доходят до моего рта, поэтому я всё ещё могу звать на помощь."

translate russian train_beach_6d6d00cf:

    "Испытав внезапный прилив восторга, навеянного в основном старыми фильмами восьмидесятых, я спешу выполнить его приказ."

translate russian train_beach_6e3d8612:

    "Бормоча себе под нос что-то о мошенниках и похотливых старых извращенцах, я уползаю прочь через дюны."

translate russian train_beach_6fb1014e:

    "Мастер указывает на каменную лужу, и через несколько мгновений я уже шарю руками в воде."

translate russian train_beach_70e42e91:

    mike.say "К чёрту твоё «терпи»! Вытащи меня отсюда, безумный старый ублюдок!"

translate russian train_beach_72d6e512:

    "Он садится на корточки, поднимает руки в воздух и начинает семенить влево и вправо по краю каменной лужи."

translate russian train_beach_72fcbb23:

    "Вот это мне уже знакомо. Все ведь видели знаменитую сцену из фильма, верно?"

translate russian train_beach_73062221:

    "От внезапного крика я подпрыгиваю и поспешно забираюсь внутрь."

translate russian train_beach_7544edab:

    master.say "Краб движется хитро и быстро, а крепости его доспехов не уступает мощь щёлкающих клешней!"

translate russian train_beach_776c21b3:

    "Заметив мой нахмуренный взгляд, он лишь пожимает плечами и ухмыляется."

translate russian train_beach_7a2d69a5:

    "Не знаю, осознал ли Мастер всю серьёзность ситуации или просто увидел, как очередные сто долларов ускользают под воду."

translate russian train_beach_7a595f31:

    "Внезапно он останавливается и полностью сосредоточивается на одной из них, хотя для меня она почти ничем не отличается от предыдущих."

translate russian train_beach_7a797d80:

    master.say "Именно поэтому, мой мальчик, ты будешь строить замки из песка!"

translate russian train_beach_7c693626:

    "Я оглядываю пляж и не вижу вокруг ничего, кроме песка и моря."

translate russian train_beach_7d4f426f:

    "Несколько секунд я смотрю на него, проверяя, не ослышался ли."

translate russian train_beach_80fa3f7c:

    "Все мои первые попытки без исключения рассыпаются, за что Мастер безжалостно ругает мои старания."

translate russian train_beach_82004ae9:

    master.say "Чтобы понять его способ сражения, ты должен вступить с ним в бой и взять в плен. Ты должен поймать его!"

translate russian train_beach_8409c5a4:

    "Следующие волны оказываются выше и почти заливают мне рот солёной водой, пока я кричу Мастеру, чтобы он помог."

translate russian train_beach_86e1a7c9:

    mike.say "Мне следует искать отдыхающих какого-то определённого типа?"

translate russian train_beach_8a25133f:

    master.say "Помимо того что краб является природным воплощением воина в доспехах, он ещё и очень вкусен в супе или рагу!"

translate russian train_beach_8a643e82:

    "Но он поднимает руку и заставляет меня замолчать ещё до того, как я успеваю произнести хоть слово."

translate russian train_beach_93415893:

    master.say "Дух сильнее тела. Терпи!"

translate russian train_beach_9372ae09:

    "Я обречённо вздыхаю и достаю свёрток купюр, чтобы заплатить за сегодняшний урок."

translate russian train_beach_93e3b838:

    mike.say "Вытащите меня отсюда!"

translate russian train_beach_9944d763:

    "Быстро осмотрев ближайшие из них, я замечаю лицо Мастера, выглядывающее между двумя пучками высокой травы."

translate russian train_beach_9c097224:

    "У меня недостаточно денег на урок Мастера."

translate russian train_beach_6f7b0811:

    mike.say "Эм... вы уверены?"

translate russian train_beach_a33d9d67:

    "С неохотой я отдаю очередную порцию честно заработанных денег и наблюдаю, как они навсегда исчезают в кармане его рубашки."

translate russian train_beach_a3f2941d:

    "Осторожно пробираясь по неровной поверхности, он проводит меня мимо примерно дюжины каменных луж, заглядывая в каждую по пути."

translate russian train_beach_a5c2819d:

    "Я уже несколько раз прохожу пляж из конца в конец, прежде чем наконец слышу, как кто-то шипящим шёпотом зовёт меня из дюн."

translate russian train_beach_a94a3ed0:

    "Мастер тут же подбегает, с готовностью протягивая перед собой ведро."

translate russian train_beach_ac362909:

    "С неохотой я отдаю деньги за урок и наблюдаю, как его улыбка становится ещё шире."

translate russian train_beach_aef765a9:

    master.say "Вглядись в глубину этой каменной лужи, мой мальчик. Скажи, что ты видишь."

translate russian train_beach_af78e7ef:

    master.say "Научно доказано, что женщины в возрасте от восемнадцати до двадцати пяти лет обладают самым острым слухом среди всех людей."

translate russian train_beach_b131a5c1:

    "Я уже вижу, как прилив быстро приближается, пока я беспомощно застрял под песком."

translate russian train_beach_b260c7e0:

    master.say "Сегодня мы поработаем над твоим равновесием."

translate russian train_beach_b39c04dc:

    master.say "Сегодня ты узнаешь всё о выносливости и терпении."

translate russian train_beach_b7045fb8:

    "Я качаю головой, наблюдая, как он прячет мои деньги, и снова думаю, не совершил ли огромную ошибку, доверившись этому старому козлу."

translate russian train_beach_b735b8af:

    "Мастер, похоже, не замечает очевидной ловушки и серьёзно кивает."

translate russian train_beach_b7f11866:

    "Мне становится интересно, куда приземляются эти несчастные ракообразные, и я останавливаюсь, чтобы оглядеться."

translate russian train_beach_b94c14ac:

    "Теперь я замечаю постоянный поток сёрферов, бегунов и людей с собаками, которые проходят мимо и почти не скрывают своего веселья."

translate russian train_beach_ba277c5a:

    "В этот момент мне стоит огромных усилий не схватить лопату и не огреть его по голове."

translate russian train_beach_bb932d0c:

    master.say "Сегодняшний урок научит тебя понимать мир в целом, сосредоточившись на мельчайших деталях!"

translate russian train_beach_be37b50c:

    "Я закатываю глаза, достаю смятую пачку купюр и кладу плату за урок в его нетерпеливую руку."

translate russian train_beach_bfcc0ee5:

    "Лишь забравшись наверх, я замечаю, насколько грубая и занозистая древесина окажется под моими босыми ногами."

translate russian train_beach_c22151d8:

    "Но когда он начинает щёлкать большими и указательными пальцами, я понимаю, что он изображает краба."

translate russian train_beach_c3e76cc1:

    "Я пытаюсь возразить, но он останавливает меня поднятой рукой, и я замолкаю, пока он закапывает меня по самую шею."

translate russian train_beach_c48733e3:

    "На мгновение я всерьёз думаю, что он окончательно поддался старческому слабоумию."

translate russian train_beach_c84b2cc0:

    mike.say "Но здесь нет никаких цветов!"

translate russian train_beach_c8596d4d:

    master.say "Твоя задача будет заключаться в том, чтобы повторить мифические навыки ниндзя."

translate russian train_beach_c9a3547f:

    master.say "Ничего особенного, ничего особенного!"

translate russian train_beach_cbb8c4c1:

    "Старик поднимает на меня взгляд с широкой ухмылкой, затем раскрывает ладонь и указывает на неё указательным пальцем другой руки."

translate russian train_beach_cffd72b9:

    "Мастер встречает меня на пляже, а затем жестом велит следовать за ним и направляется к более каменистой его части."

translate russian train_beach_d03fa93b:

    "Недовольно ворча, я начинаю наполнять ведёрко песком и переворачивать его на землю."

translate russian train_beach_d4eb9dec:

    "Я киваю, показывая, что всё понял, и начинаю копать так быстро, как могу."

translate russian train_beach_d50c648c:

    master.say "Для начала выкопай яму прямо здесь, глубиной в пять футов!"

translate russian train_beach_d605a3b8:

    mike.say "Постойте... что?!"

translate russian train_beach_d90f8802:

    mike.say "А-а-а!"

translate russian train_beach_ddc52164:

    master.say "Если кто-то велит тебе сделать глупость, не делай её!"

translate russian train_beach_ddde9877:

    "Я падаю со сваи, катаюсь по песку и вою от боли, а Мастер уже во второй раз смеётся надо мной."

translate russian train_beach_dfcb3d98:

    "Он одаривает меня своей привычной ухмылкой, качает головой и протягивает руку."

translate russian train_beach_e3428ba9:

    "Спрятав деньги где-то в складках своей одежды, Мастер одним проворным движением вскакивает на ноги."

translate russian train_beach_e51880c9:

    master.say "Поздравляю, мальчик. Ты усвоил ИСТИННУЮ тему сегодняшнего урока."

translate russian train_beach_e54bfa62:

    "Мне удаётся поймать его взгляд, и я киваю в сторону так заинтересовавшей его лужи, надеясь понять причину."

translate russian train_beach_e67d6bf5:

    "Как бы то ни было, он подбегает и начинает откапывать мои руки."

translate russian train_beach_e7c9d241:

    "Затем следует уже знакомый жест: он протягивает руку за деньгами, без которых отказывается продолжать."

translate russian train_beach_ed21940d:

    "Когда мне наконец начинает казаться, что я освоился, Мастер хвалит меня весьма скупо, но всё же выглядит довольным тем, как быстро я продвинулся."

translate russian train_beach_edf78848:

    "Оказавшись среди дюн и присев рядом, я открываю рот, чтобы спросить, почему мы здесь прячемся."

translate russian train_beach_ee74be7d:

    "По самым честным подсчётам, мне удаётся продержаться там секунд пять или шесть, прежде чем боль становится невыносимой."

translate russian train_beach_eeda0d44:

    "Подходя к Мастеру, я вижу, что он уже стоит на пляже спиной ко мне и смотрит на море."

translate russian train_beach_f08f9001:

    master.say "Доброе утро, мой юный ученик."

translate russian train_beach_f2105f01:

    "Дело идёт лучше, когда я нахожу слой влажного песка, и следующая серия замков уже почти полностью держит форму."

translate russian train_beach_f48e5f8d:

    "Не оборачиваясь, он протягивает руку и нетерпеливо потирает пальцы."

translate russian train_beach_f54f3f03:

    "Как только я оказываюсь в яме и смотрю на него снизу вверх, Мастер хватает лопату и начинает засыпать песок обратно."

translate russian train_beach_f68f9b7a:

    "Он наклоняется к траве у своих ног и достаёт фотоаппарат, который, по всей видимости, всё это время лежал там."

translate russian train_beach_f933be99:

    master.say "Если ты действительно веришь, что способен выстоять, значит, выстоишь!"

translate russian train_beach_fd8dbc67:

    "Мой ответ заставляет Мастера возмущённо запыхтеть."

translate russian train_beach_fd9707da:

    master.say "Никаких вопросов. Делай, что я сказал!"

translate russian train_beach_fde03e8f:

    "Он поворачивается и указывает на несколько свай, уходящих вдоль пляжа в море."

translate russian train_beach_fe0c3877:

    "Но крабы проворны и находятся в родной стихии, поэтому без труда ускользают от моих неуклюжих попыток их схватить."

translate russian train_with_13746bde:

    "Я тренируюсь вместе с [active_girl.name]."

translate russian train_with_58b5672a:

    active_girl.say "Почему бы и нет."

translate russian train_with_a6f73338:

    active_girl.say "Прости, мне не хочется тренироваться вместе с тобой."

translate russian training_5d603a7e:

    "[successes[0].name] не сводит с меня глаз, пока я тренируюсь."

translate russian training_6f6884e6:

    "Девушки не сводят с меня глаз, пока я тренируюсь."

translate russian training_aeea7ea9:

    "[successes[0].name] не сводит с меня глаз, пока я тренируюсь."

translate russian training_b3c4f533:

    "Они не сводят с меня глаз, пока я тренируюсь."

translate russian training_e61eae8a:

    "Я некоторое время тренируюсь в спортзале."

translate russian training_hard_3ed4d569:

    "Я заставляю себя выдержать тяжёлую тренировку в спортзале."

translate russian training_hard_5d603a7e:

    "[successes[0].name] не сводит с меня глаз, пока я тренируюсь."

translate russian training_hard_6f6884e6:

    "Девушки не сводят с меня глаз, пока я тренируюсь."

translate russian training_hard_aeea7ea9:

    "[successes[0].name] не сводит с меня глаз, пока я тренируюсь."

translate russian training_hard_b3c4f533:

    "Они не сводят с меня глаз, пока я тренируюсь."

translate russian tv_bj_bree_samantha_sasha_2c108356:

    mike.say "Я просто..."

translate russian tv_bj_bree_samantha_sasha_30e74fc5:

    mike.say "Эм..."

translate russian tv_bj_bree_samantha_sasha_30e74fc5_1:

    mike.say "Эм..."

translate russian tv_bj_bree_samantha_sasha_30e74fc5_2:

    mike.say "Эм..."

translate russian tv_bj_bree_samantha_sasha_5d1a8c04:

    "Какого чёрта?"

translate russian tv_bj_bree_samantha_sasha_86d07102:

    mike.say "А..."

translate russian vacuum_bree_sleep_male_03e18915:

    bree.say "Извинения приняты, [hero.name]."

translate russian vacuum_bree_sleep_male_042e6061:

    "Однако кто-то, похоже, думает иначе..."

translate russian vacuum_bree_sleep_male_08b0129a:

    mike.say "Мне стоило сделать это раньше."

translate russian vacuum_bree_sleep_male_0e65b319:

    "Что-нибудь, объясняющее, почему я вынужден заниматься этим именно сейчас."

translate russian vacuum_bree_sleep_male_11857438:

    "Но долго продолжать эту борьбу она не может."

translate russian vacuum_bree_sleep_male_12accaec:

    mike.say "Увидимся утром."

translate russian vacuum_bree_sleep_male_132ba5bd:

    "А затем пытаюсь спрятать её за спиной, будто это каким-то образом поможет."

translate russian vacuum_bree_sleep_male_193fd1fb:

    bree.say "Пожалуй, я ведь тоже играла."

translate russian vacuum_bree_sleep_male_1cd260db:

    bree.say "То есть это МОЯ вина?!"

translate russian vacuum_bree_sleep_male_1f95ec5b:

    "Я смотрю, как [bree.name] скрывается в комнате, и думаю, действительно ли она это сделает!"

translate russian vacuum_bree_sleep_male_21bc88d4:

    "И это, очевидно, исключительно моя собственная глупость!"

translate russian vacuum_bree_sleep_male_2874c012:

    "А я остаюсь один в коридоре, всё ещё сжимая насадку пылесоса."

translate russian vacuum_bree_sleep_male_2b81ebe5:

    bree.say "Если до утра я снова услышу эту штуку, то засуну её туда, куда не светит солнце!"

translate russian vacuum_bree_sleep_male_2c25f14f:

    bree.say "Ты не застал меня бодрствующей, [hero.name]."

translate russian vacuum_bree_sleep_male_2d8a157c:

    bree.say "Ты меня разбудил!"

translate russian vacuum_bree_sleep_male_3336a823:

    "Я смотрю на насадку пылесоса в своей руке."

translate russian vacuum_bree_sleep_male_338a872c:

    bree.say "И помню, что просила тебя продолжить, когда ты хотел закончить!"

translate russian vacuum_bree_sleep_male_3397ce3c:

    mike.say "Прости, что разбудил тебя."

translate russian vacuum_bree_sleep_male_33a63351:

    bree.say "Ох, [hero.name]!"

translate russian vacuum_bree_sleep_male_3664d70f:

    "Почему-то мне кажется, что именно такого объяснения она не хотела услышать."

translate russian vacuum_bree_sleep_male_392ba348:

    "Но вспоминаю лишь то, что несколько часов играл на Zbox."

translate russian vacuum_bree_sleep_male_3cdb5b9b:

    "Мне кажется, я буквально вижу, как на лбу [bree.name] начинают вздуваться вены."

translate russian vacuum_bree_sleep_male_3e8af435:

    "Её глаз дёргается, пока она пытается не потерять самообладание."

translate russian vacuum_bree_sleep_male_3ec103ef:

    "Я киваю, отвечая на улыбку [bree.name]."

translate russian vacuum_bree_sleep_male_40c4ddf5:

    "Поэтому беру пылесос и приступаю к порученной мне изнурительной задаче."

translate russian vacuum_bree_sleep_male_42faa52b:

    bree.say "Что ты делаешь?!"

translate russian vacuum_bree_sleep_male_45ad7da1:

    bree.say "Ты эгоистичный придурок!"

translate russian vacuum_bree_sleep_male_46ed1dde:

    bree.say "[hero.name]!"

translate russian vacuum_bree_sleep_male_492e8f15:

    bree.say "Я больше не могу продолжать этот разговор."

translate russian vacuum_bree_sleep_male_49e6df14:

    "[bree.name] разворачивается и возвращается в свою спальню."

translate russian vacuum_bree_sleep_male_4cc3bbb2:

    "[bree.name] в полном раздражении вскидывает руки."

translate russian vacuum_bree_sleep_male_52b1459f:

    "Эй, погодите-ка. С чего [bree.name] вообще решила читать мне такую лекцию?"

translate russian vacuum_bree_sleep_male_5ebcefb2:

    "[bree.name] кивает и поворачивается к своей двери."

translate russian vacuum_bree_sleep_male_6039831b:

    "Но главное ведь, что работа вообще будет сделана, верно?"

translate russian vacuum_bree_sleep_male_609a2648:

    "Я беспомощно пожимаю плечами."

translate russian vacuum_bree_sleep_male_68427d82:

    "Я чувствую, как кто-то хлопает меня по спине."

translate russian vacuum_bree_sleep_male_707ad5b9:

    bree.say "Просто закончи утром, хорошо?"

translate russian vacuum_bree_sleep_male_714e4328:

    mike.say "Не думал, что встречу тебя бодрствующей в такой час!"

translate russian vacuum_bree_sleep_male_773fed17:

    "Она в пижаме, а волосы торчат во все стороны."

translate russian vacuum_bree_sleep_male_77ae7c31:

    "Я выключаю пылесос, чтобы лучше её слышать."

translate russian vacuum_bree_sleep_male_79365a51:

    bree.say "Это самое жалкое оправдание из всех, что я слышала!"

translate russian vacuum_bree_sleep_male_7d60371c:

    "Да, я занимаюсь этим уже глубокой ночью, прямо перед сном."

translate russian vacuum_bree_sleep_male_7ec3f1f6:

    mike.say "Но вместо этого я играл на Zbox."

translate russian vacuum_bree_sleep_male_87578d0a:

    "Они с Сашей постоянно твердят, что я должен честно выполнять свою часть работы по дому."

translate russian vacuum_bree_sleep_male_8da27cef:

    "Я прокручиваю в голове события последних нескольких часов."

translate russian vacuum_bree_sleep_male_9157dd8e:

    "А теперь, когда я именно это и пытаюсь сделать, мне ещё и достаётся!"

translate russian vacuum_bree_sleep_male_916d537f:

    mike.say "Да неужели?"

translate russian vacuum_bree_sleep_male_9501845c:

    "Но всё равно явно старается говорить спокойно."

translate russian vacuum_bree_sleep_male_959fe92c:

    bree.say "И ещё, [hero.name]?"

translate russian vacuum_bree_sleep_male_96491050:

    "Глаза [bree.name] широко раскрываются, а рот приоткрывается."

translate russian vacuum_bree_sleep_male_9fa0a2c2:

    bree.say "Неужели нельзя было сделать это ДО того, как я легла спать?!"

translate russian vacuum_bree_sleep_male_a0ce3a07:

    bree.say "Может, оставишь пылесос до утра?"

translate russian vacuum_bree_sleep_male_a2576cbb:

    mike.say "Иначе пришлось бы пожертвовать игровым временем!"

translate russian vacuum_bree_sleep_male_a63145a9:

    bree.say "Никто не заставлял тебя всю ночь играть на Zbox."

translate russian vacuum_bree_sleep_male_ab6abb2f:

    "Я вижу, что на этой неделе по графику должен пылесосить дом."

translate russian vacuum_bree_sleep_male_ab7dc52c:

    bree.say "А если Саша начнёт ругаться, я скажу, что сама тебя отпустила."

translate russian vacuum_bree_sleep_male_b492b7f5:

    "Закатывая глаза, она слабо улыбается."

translate russian vacuum_bree_sleep_male_bc46d057:

    "А я отступаю на шаг, опасаясь, что она и правда меня ударит."

translate russian vacuum_bree_sleep_male_bd44cc41:

    "Выражение лица [bree.name] смягчается."

translate russian vacuum_bree_sleep_male_bd4a586d:

    mike.say "Кажется, кто-то просил меня продолжить."

translate russian vacuum_bree_sleep_male_c03fd7d4:

    "И не поймите неправильно, я ненавижу домашние дела не меньше любого нормального человека."

translate russian vacuum_bree_sleep_male_d78b20bb:

    mike.say "Но я уже почти закончил."

translate russian vacuum_bree_sleep_male_d977d523:

    bree.say "Угх..."

translate russian vacuum_bree_sleep_male_d99206cd:

    bree.say "Мне нужно спать!"

translate russian vacuum_bree_sleep_male_de5a6402:

    "И резко оборачиваюсь, увидев в коридоре позади себя [bree.name]."

translate russian vacuum_bree_sleep_male_de6d65b2:

    "Но также хочу сохранить хорошие отношения с остальными и показать, что вношу свой вклад."

translate russian vacuum_bree_sleep_male_df7e0782:

    bree.say "ЧТО?"

translate russian vacuum_bree_sleep_male_e2aab607:

    mike.say "И прости, что веду себя как безответственный придурок."

translate russian vacuum_bree_sleep_male_eb8fb3d0:

    bree.say "Я ведь не выкручивала тебе руки!"

translate russian vacuum_bree_sleep_male_f0cc42a5:

    "Пытаюсь найти аргумент, которым можно ответить [bree.name]."

translate russian vacuum_bree_sleep_male_f8d186e8:

    "[bree.name] закатывает глаза."

translate russian vacuum_bree_sleep_male_fb4d74a5:

    mike.say "Осталось не больше получаса!"

translate russian vacuum_bree_sleep_male_fe35eb92:

    mike.say "Причём этот человек находится не за миллион миль отсюда!"

translate russian vacuum_lexi_sleep_05250971:

    "Значит, я могу спокойно закончить уборку, не мешая никому из жильцов."

translate russian vacuum_lexi_sleep_07e1b50b:

    "Лекси вздыхает и снова укладывается в своём гнезде из одеял."

translate russian vacuum_lexi_sleep_09c6b51e:

    mike.say "Вообще-то ты живёшь здесь бесплатно, Лекси."

translate russian vacuum_lexi_sleep_0a29f3a8:

    "Можно было бы ожидать от неё хоть немного благодарности."

translate russian vacuum_lexi_sleep_0ae0b804:

    lexi.say "Кто знает, может, мне удастся перебраться куда-нибудь получше?"

translate russian vacuum_lexi_sleep_0e3031cd:

    lexi.say "Угх..."

translate russian vacuum_lexi_sleep_107b5480:

    "Я понимаю, что уже поздновато пылесосить дом."

translate russian vacuum_lexi_sleep_1164a7f4:

    lexi.say "Но я правда благодарна, что ты позволил мне здесь остаться."

translate russian vacuum_lexi_sleep_135aa5f3:

    lexi.say "Или я не считаюсь?"

translate russian vacuum_lexi_sleep_14bdfda3:

    "Что сейчас вообще произошло?"

translate russian vacuum_lexi_sleep_14f53022:

    lexi.say "Я постараюсь, [hero.name]."

translate russian vacuum_lexi_sleep_1c9ea150:

    lexi.say "Похоже, ты хочешь что-то сказать, [hero.name]."

translate russian vacuum_lexi_sleep_1d24c6fb:

    lexi.say "А теперь я пойду спать в другое место."

translate russian vacuum_lexi_sleep_21856b59:

    "Выходя из гостиной, Лекси оглядывается через плечо."

translate russian vacuum_lexi_sleep_23d8ad14:

    mike.say "Не уверен, Лекси."

translate russian vacuum_lexi_sleep_243b07f6:

    lexi.say "Мне нужно выспаться ради красоты!"

translate russian vacuum_lexi_sleep_2668c2cd:

    "Что же я за друг такой?"

translate russian vacuum_lexi_sleep_26ac6a6a:

    "Ладно, она сама напросилась."

translate russian vacuum_lexi_sleep_286c46b9:

    "Из спутанной груды одеял высовывается сонная голова Лекси."

translate russian vacuum_lexi_sleep_2b83852e:

    lexi.say "А ты подумай о том, как жестоко со мной обошёлся."

translate russian vacuum_lexi_sleep_30e74fc5:

    mike.say "Эм..."

translate russian vacuum_lexi_sleep_31326715:

    "Она всё ещё закутана в одеяла."

translate russian vacuum_lexi_sleep_32e67f07:

    "И мне едва удаётся удержаться от того, чтобы согласиться с её последними словами."

translate russian vacuum_lexi_sleep_40c3fd89:

    lexi.say "Я сделаю вид, что ты этого не говорил, [hero.name]."

translate russian vacuum_lexi_sleep_47a55510:

    "Пока она спала, у неё ещё и слюна текла из уголка рта."

translate russian vacuum_lexi_sleep_4b37f175:

    mike.say "А теперь тебе лучше снова лечь спать."

translate russian vacuum_lexi_sleep_4de32809:

    lexi.say "Спокойной ночи, [hero.name]!"

translate russian vacuum_lexi_sleep_4df698bd:

    lexi.say "ЭЙ!"

translate russian vacuum_lexi_sleep_53a1555c:

    mike.say "Где ещё ты собираешься спать?"

translate russian vacuum_lexi_sleep_562db0e1:

    lexi.say "Какого чёрта ты делаешь?!"

translate russian vacuum_lexi_sleep_5a354c90:

    "Вот чёрт, теперь я вспомнил."

translate russian vacuum_lexi_sleep_5a7eccc4:

    mike.say "Но это меньшее, что я мог сделать."

translate russian vacuum_lexi_sleep_5b32153e:

    "Лекси качает головой, пытаясь прогнать остатки сна."

translate russian vacuum_lexi_sleep_63bd2dd8:

    "И вообще, с какой стати Лекси меня отчитывает?"

translate russian vacuum_lexi_sleep_649b44f1:

    lexi.say "Мне сейчас не до этого дерьма."

translate russian vacuum_lexi_sleep_658d5d58:

    "Едва я заканчиваю говорить, Лекси вскакивает с дивана."

translate russian vacuum_lexi_sleep_66d17530:

    lexi.say "Потому что ты мой друг и вообще хороший человек."

translate russian vacuum_lexi_sleep_6c8ce8b3:

    "К тому же никто не заметит, если я где-нибудь схалтурю!"

translate russian vacuum_lexi_sleep_72b93b73:

    "Но поскольку я хочу, чтобы мои яйца остались на месте, я держу своё мнение при себе."

translate russian vacuum_lexi_sleep_bde04bd9:

    mike.say "Н... но, Лекси..."

translate russian vacuum_lexi_sleep_7712b81c:

    "Как получилось, что я лишился собственной кровати и теперь сплю на диване?!"

translate russian vacuum_lexi_sleep_77c477d0:

    "Лекси приподнимает бровь и улыбается."

translate russian vacuum_lexi_sleep_7b02887b:

    "Но убрать нужно только на первом этаже, а все остальные уже легли спать."

translate russian vacuum_lexi_sleep_7df5cdfb:

    mike.say "Я просто забыл, что ты здесь, вот и всё."

translate russian vacuum_lexi_sleep_80ee69cf:

    mike.say "Я знаю, Лекси."

translate russian vacuum_lexi_sleep_862673ec:

    "Всё идёт по плану, пока я не добираюсь до гостиной."

translate russian vacuum_lexi_sleep_86ebe2ce:

    lexi.say "У вас здесь так принято, [hero.name]?"

translate russian vacuum_lexi_sleep_8a4712f2:

    mike.say "Тогда тем, кто действительно оплачивает счета, не пришлось бы заниматься этим так поздно!"

translate russian vacuum_lexi_sleep_c643ff9b:

    mike.say "С... спокойной ночи, Лекси!"

translate russian vacuum_lexi_sleep_8d531794:

    mike.say "И мы даже не ограничивали срок, на который ты можешь остаться."

translate russian vacuum_lexi_sleep_94f254fa:

    "Из-за этого она выглядит довольно нелепо."

translate russian vacuum_lexi_sleep_9ade25ae:

    lexi.say "Спокойной ночи. Надеюсь, утром тебе станет лучше!"

translate russian vacuum_lexi_sleep_9eac5ce7:

    "Погоди-ка..."

translate russian vacuum_lexi_sleep_a526a8b2:

    lexi.say "Наверное, для нас обоих эта ситуация довольно странная!"

translate russian vacuum_lexi_sleep_a68e0c80:

    "В последнее время Лекси пришлось пережить столько всего."

translate russian vacuum_lexi_sleep_a6d0a881:

    lexi.say "Но этот диван не очень-то подходит для сна."

translate russian vacuum_lexi_sleep_ac93d0f0:

    "Её глаза расширяются, а уголки губ опускаются."

translate russian vacuum_lexi_sleep_adf99059:

    lexi.say "Хм, а я-то думала, что ты просто решил мне помочь!"

translate russian vacuum_lexi_sleep_ae0ad182:

    "Но это не мешает ей размахивать пальцем у меня перед лицом."

translate russian vacuum_lexi_sleep_ae40a619:

    "Именно я приютил её, когда она потеряла всё!"

translate russian vacuum_lexi_sleep_b189dac8:

    "Наверное, днём одна из девушек соорудила из них себе гнездо."

translate russian vacuum_lexi_sleep_b1a827f2:

    mike.say "Может, тебе стоило бы хоть иногда помогать по дому."

translate russian vacuum_lexi_sleep_b5879bc3:

    "Сначала я принимаю лежащую на диване груду за беспорядочную кучу одеял."

translate russian vacuum_lexi_sleep_ba8b34ad:

    "Да и раньше её жизнь вовсе не была усыпана розами."

translate russian vacuum_lexi_sleep_bfd97468:

    "Но не успеваю закончить и четверть комнаты, как позади раздаётся крик."

translate russian vacuum_lexi_sleep_c06bcc18:

    "Слыша это, я невольно смотрю на растрёпанные волосы Лекси."

translate russian vacuum_lexi_sleep_c7e9c0bd:

    lexi.say "Ты заходишь с этой штукой в комнату к каждому?"

translate russian vacuum_lexi_sleep_d1e71a71:

    "К этому моменту Лекси уже окончательно просыпается."

translate russian vacuum_lexi_sleep_d1e71a71_1:

    "К этому моменту Лекси уже окончательно просыпается."

translate russian vacuum_lexi_sleep_d3ec7372:

    mike.say "Сейчас в доме нет свободных кроватей."

translate russian vacuum_lexi_sleep_d5aa54f4:

    "О чём я вообще думаю?"

translate russian vacuum_lexi_sleep_41f10d99:

    mike.say "Я... наверное, просто забыл, что ты здесь, Лекси."

translate russian vacuum_lexi_sleep_d73db748:

    mike.say "Я скажу, что имею в виду, Лекси."

translate russian vacuum_lexi_sleep_15dfb585:

    lexi.say "Эй... не вини себя так, [hero.name]."

translate russian vacuum_lexi_sleep_e223e258:

    lexi.say "А я не против спать вместе!"

translate russian vacuum_lexi_sleep_e23d1e8e:

    lexi.say "Я займу твою комнату, а ты можешь спать на диване."

translate russian vacuum_lexi_sleep_e4f790e9:

    "Прежде чем ответить, я делаю глубокий вдох."

translate russian vacuum_lexi_sleep_e9604e9a:

    "Но по её виду ясно, что внезапное пробуждение её совсем не обрадовало."

translate russian vacuum_lexi_sleep_eeaa1019:

    lexi.say "Так почему бы тебе не сказать это прямо?"

translate russian vacuum_lexi_sleep_eeebc039:

    "Я лишь пожимаю плечами и продолжаю пылесосить, ведь убирать их не моя забота."

translate russian vacuum_lexi_sleep_f1d8a63c:

    mike.say "Эм..."

translate russian vacuum_lexi_sleep_f2ea8dd8:

    "После того как её трейлер сгорел дотла, она всё ещё ночует на нашем диване!"

translate russian vacuum_lexi_sleep_f3d5de2b:

    mike.say "Прости, Лекси."

translate russian vacuum_lexi_sleep_f6dafadd:

    "Теперь она спит на моём диване, имея при себе лишь ту одежду, что на ней!"

translate russian vacuum_lexi_sleep_f769c717:

    "Я выключаю пылесос и оборачиваюсь."

translate russian vacuum_lexi_sleep_fb7ef491:

    "И моё извинение, похоже, немного её успокаивает."

translate russian vacuum_lexi_sleep_fc9fa3f4:

    mike.say "Закончу уборку утром."

translate russian vacuum_lexi_sleep_ff28d384:

    mike.say "Пылесошу, наверное."

translate russian vacuum_minami_sleep_male_01f55dd1:

    "Но, поднявшись, понимаю, что они принадлежат Минами."

translate russian vacuum_minami_sleep_male_05e2b65c:

    "Не помогает и то, что я откладывал всё до последней минуты."

translate russian vacuum_minami_sleep_male_0a364193:

    "Я поспешно выключаю пылесос, чтобы лучше расслышать её."

translate russian vacuum_minami_sleep_male_1658335d:

    minami.say "Что ты вообще делаешь?"

translate russian vacuum_minami_sleep_male_1bd6eaf3:

    "Возможно, маленькой принцессе пора привыкать к реальному миру."

translate russian vacuum_minami_sleep_male_1c36d550:

    minami.say "У меня с утра первое занятие."

translate russian vacuum_minami_sleep_male_26559043:

    minami.say "Может, утром я помогу тебе?"

translate russian vacuum_minami_sleep_male_292827b8:

    "В конце концов, я её старший брат."

translate russian vacuum_minami_sleep_male_29e4b364:

    minami.say "Посреди ночи, да ещё прямо у моей комнаты!"

translate russian vacuum_minami_sleep_male_30e74fc5:

    mike.say "Эм..."

translate russian vacuum_minami_sleep_male_3637ee37:

    "Если уж на то пошло, посуду она тоже никогда не моет."

translate russian vacuum_minami_sleep_male_3bfe6a21:

    "Я жду, пока она закроет дверь спальни, и лишь затем продолжаю уборку."

translate russian vacuum_minami_sleep_male_3c55ba3a:

    "Последнее я бы наверняка запомнил..."

translate russian vacuum_minami_sleep_male_413e3d9d:

    mike.say "Ты ведь понимаешь, что мы больше не дома, правда, Минами?"

translate russian vacuum_minami_sleep_male_41ef0227:

    minami.say "Угх..."

translate russian vacuum_minami_sleep_male_425031c2:

    "И вот я чищу ковры, хотя после тяжёлого рабочего дня мне следовало бы отдыхать."

translate russian vacuum_minami_sleep_male_4b41c534:

    minami.say "Я вижу, идиот."

translate russian vacuum_minami_sleep_male_50823e86:

    mike.say "Все выполняют свою часть домашних дел."

translate russian vacuum_minami_sleep_male_50ba314e:

    mike.say "Здесь нет мамы, которая будет за нами бегать."

translate russian vacuum_minami_sleep_male_5136fba4:

    mike.say "Прости, что разбудил. Это было эгоистично с моей стороны."

translate russian vacuum_minami_sleep_male_562d540a:

    mike.say "Наверное, будут, Минами."

translate russian vacuum_minami_sleep_male_5def2a08:

    "Я невольно пожимаю плечами и поднимаю насадку пылесоса."

translate russian vacuum_minami_sleep_male_626b3aef:

    "Минами имеет полное право злиться за то, что я её разбудил."

translate russian vacuum_minami_sleep_male_649ba0a4:

    mike.say "Но я сам виноват, что не сделал всё раньше."

translate russian vacuum_minami_sleep_male_67c34b74:

    "Минами кивает и поворачивается, чтобы уйти."

translate russian vacuum_minami_sleep_male_67dd8b9a:

    "Минами надувает губы, но всё же кивает."

translate russian vacuum_minami_sleep_male_684e3e2c:

    "И, мягко говоря, совсем не рада меня видеть."

translate russian vacuum_minami_sleep_male_703a25ea:

    minami.say "Если, конечно, нормально высплюсь..."

translate russian vacuum_minami_sleep_male_710e159b:

    mike.say "Тогда зачем ты спросила..."

translate russian vacuum_minami_sleep_male_730d8a1e:

    "Я ненавижу домашнюю работу. Это проклятие моей жизни, которого я всегда стараюсь избегать."

translate russian vacuum_minami_sleep_male_77fc8a6b:

    "Опустив голову, я сосредоточенно пытаюсь убрать особенно упрямый комок пуха."

translate russian vacuum_minami_sleep_male_7ccc0099:

    "Мне неловко, но ей придётся потерпеть."

translate russian vacuum_minami_sleep_male_7d8d9247:

    "Я улыбаюсь Минами, а она проскальзывает в комнату и закрывает дверь."

translate russian vacuum_minami_sleep_male_80b6715a:

    mike.say "Знаю, что это неприятно, Минами."

translate russian vacuum_minami_sleep_male_80c2740b:

    "Она стоит в пижаме, скрестив руки на груди."

translate russian vacuum_minami_sleep_male_89358669:

    "Минами выглядит немного удивлённой моей вспышкой."

translate russian vacuum_minami_sleep_male_905c51b5:

    "После этих слов я немного смягчаюсь."

translate russian vacuum_minami_sleep_male_906428ec:

    mike.say "Когда живёшь в общем доме, нужно выполнять свою часть работы."

translate russian vacuum_minami_sleep_male_92150b03:

    "Сначала я вижу перед собой только пару худеньких коленей."

translate russian vacuum_minami_sleep_male_924be914:

    mike.say "На сегодня закончу и продолжу утром."

translate russian vacuum_minami_sleep_male_94043a06:

    minami.say "Я не виновата, что мама любила меня баловать."

translate russian vacuum_minami_sleep_male_595622f8:

    minami.say "Я... я разозлилась, потому что мне нужно спать, ясно?"

translate russian vacuum_minami_sleep_male_9e177314:

    "Когда я признаю свою вину, выражение лица Минами смягчается."

translate russian vacuum_minami_sleep_male_a15cea5e:

    "Но в этот раз отвертеться было невозможно, [bree.name] и Саша ясно это дали понять."

translate russian vacuum_minami_sleep_male_a197aaa0:

    "Я ни разу не видел, чтобы Минами катала пылесос по дому."

translate russian vacuum_minami_sleep_male_a3156faf:

    "И уж точно не ползает на четвереньках, оттирая полы!"

translate russian vacuum_minami_sleep_male_a8a1a169:

    "Но затем останавливается и оглядывается через плечо."

translate russian vacuum_minami_sleep_male_ab97bef0:

    "В графике, который они, похоже, составили за моей спиной, указано, что пылесосить должен я."

translate russian vacuum_minami_sleep_male_abab76f7:

    mike.say "Обещаю постараться сделать побыстрее, хорошо?"

translate russian vacuum_minami_sleep_male_af2e6144:

    "Я должен помогать ей привыкнуть к жизни здесь."

translate russian vacuum_minami_sleep_male_af47a15b:

    mike.say "Ты права, Минами."

translate russian vacuum_minami_sleep_male_b037cab3:

    "Мне казалось, ответ вполне очевиден."

translate russian vacuum_minami_sleep_male_b13f991d:

    mike.say "И должен закончить всё сегодня."

translate russian vacuum_minami_sleep_male_b1694cdf:

    mike.say "Но я поздно вернулся с работы."

translate russian vacuum_minami_sleep_male_bb183d2b:

    "С какого чёрта она вообще разговаривает со мной таким тоном?"

translate russian vacuum_minami_sleep_male_bc22d835:

    minami.say "Но разве [bree.name] и Саша не будут ругаться?"

translate russian vacuum_minami_sleep_male_c3225339:

    mike.say "Пылесошу?"

translate russian vacuum_minami_sleep_male_cc7f2e9c:

    "Теперь уже поздно, а я не закончил даже половины!"

translate russian vacuum_minami_sleep_male_da9a14aa:

    "Мне остаётся лишь беспомощно пожать плечами."

translate russian vacuum_minami_sleep_male_dbbf1517:

    "Поэтому замечаю, что больше не один, лишь когда наконец поднимаю взгляд."

translate russian vacuum_minami_sleep_male_decca38f:

    "Она кивает, но не возвращается в комнату."

translate russian vacuum_minami_sleep_male_e61df9d6:

    "Но затем, похоже, снова берёт себя в руки."

translate russian vacuum_minami_sleep_male_ecdcaf47:

    minami.say "О, ха-ха, очень смешно!"

translate russian vacuum_minami_sleep_male_ed4f520e:

    "И уж точно не должен всё для неё усложнять."

translate russian vacuum_minami_sleep_male_f1d8a63c:

    mike.say "Эм..."

translate russian vacuum_minami_sleep_male_f331e0b4:

    "Наверное, было немного эгоистично откладывать всё до такого позднего часа."

translate russian vacuum_minami_sleep_male_fa96f099:

    "Минами ещё не привыкла жить вдали от дома."

translate russian vacuum_sasha_sleep_male_043aa18e:

    mike.say "Прости, Саша, я не понял!"

translate russian vacuum_sasha_sleep_male_04f60769:

    "Настроение Саши мгновенно меняется."

translate russian vacuum_sasha_sleep_male_0a7a1c47:

    sasha.say "Меня раздражает другое: почему ты делаешь это именно сейчас?"

translate russian vacuum_sasha_sleep_male_1254028b:

    "Уверен, Саша ругалась бы и в том случае, если бы я ничего не делал."

translate russian vacuum_sasha_sleep_male_1b597e36:

    "Саша качает головой, словно разговаривает с полным идиотом."

translate russian vacuum_sasha_sleep_male_1dfd5904:

    sasha.say "Благодарны, что мужчина в доме соизволил испачкать руки?!"

translate russian vacuum_sasha_sleep_male_2355985d:

    sasha.say "О, не переживай об этом, [hero.name]."

translate russian vacuum_sasha_sleep_male_30a87c3b:

    "Возможно, в будущем стоит заниматься такими делами до того, как включу Zbox..."

translate russian vacuum_sasha_sleep_male_337a6978:

    sasha.say "Но сейчас мне нужен только сон."

translate russian vacuum_sasha_sleep_male_33ac6a5c:

    sasha.say "Да, это я уже поняла, [hero.name]."

translate russian vacuum_sasha_sleep_male_36c9f745:

    "Но теперь в её глазах вспыхивают настоящее раздражение и возмущение."

translate russian vacuum_sasha_sleep_male_3767b6ea:

    sasha.say "А отсюда прозвучало именно так."

translate russian vacuum_sasha_sleep_male_37960672:

    mike.say "Саша, я не это имел в виду!"

translate russian vacuum_sasha_sleep_male_3e00ed72:

    sasha.say "Кхм..."

translate russian vacuum_sasha_sleep_male_3f6d0936:

    "И вспоминаю, что большую часть ночи потратил на Zbox."

translate russian vacuum_sasha_sleep_male_40a8dc43:

    sasha.say "Тогда тебе не пришлось бы пылесосить посреди ночи!"

translate russian vacuum_sasha_sleep_male_4362dbeb:

    "Я всего лишь стараюсь выполнить свою часть уборки!"

translate russian vacuum_sasha_sleep_male_45bea768:

    mike.say "Ты права, мне следовало сделать это несколько часов назад."

translate russian vacuum_sasha_sleep_male_48168299:

    "И смотрю, как Саша возвращается в комнату и закрывает дверь."

translate russian vacuum_sasha_sleep_male_49b1ae65:

    sasha.say "А именно о том, куда я сейчас засуну эту вилку!"

translate russian vacuum_sasha_sleep_male_5020b64c:

    "Саша моргает, словно не верит своим ушам."

translate russian vacuum_sasha_sleep_male_50c8d33d:

    "Улыбаясь, Саша передаёт мне вилку от пылесоса."

translate russian vacuum_sasha_sleep_male_e3e73b33:

    mike.say "Я... прости, Саша."

translate russian vacuum_sasha_sleep_male_529688f9:

    sasha.say "Наверное, сейчас я особенно раздражительная!"

translate russian vacuum_sasha_sleep_male_534477d3:

    sasha.say "Почему ты занимаешься этим, пока я пытаюсь спать?"

translate russian vacuum_sasha_sleep_male_5a7000b7:

    sasha.say "Возможно, я так и сделаю."

translate russian vacuum_sasha_sleep_male_5db74213:

    "Уже поздно, но если двигаться как обычно быстро, я окажусь в постели в рекордные сроки!"

translate russian vacuum_sasha_sleep_male_5fd223f3:

    "В графике уборки нет ни одного дела, которого я бы особенно ждал."

translate russian vacuum_sasha_sleep_male_60741a57:

    "И тут слышу, как кто-то позади меня кашляет."

translate russian vacuum_sasha_sleep_male_6171b0bc:

    sasha.say "Спасибо, [hero.name]."

translate russian vacuum_sasha_sleep_male_634ad1be:

    "А заодно замечаю, что она в пижаме."

translate russian vacuum_sasha_sleep_male_64b20d16:

    "И я понимаю, что только что серьёзно облажался!"

translate russian vacuum_sasha_sleep_male_661a1d07:

    "Я киваю, радуясь перемене её настроения."

translate russian vacuum_sasha_sleep_male_711b2c1f:

    "Я уже чувствую, как меня начинает охватывать чувство вины."

translate russian vacuum_sasha_sleep_male_7297ff90:

    "Ну разбудил я её случайно, и что?"

translate russian vacuum_sasha_sleep_male_73791711:

    "Господи, неужели мне здесь вообще нельзя спокойно жить?"

translate russian vacuum_sasha_sleep_male_7b93a5de:

    "Я едва не выпрыгиваю из собственной кожи, прежде чем понимаю, что это всего лишь Саша."

translate russian vacuum_sasha_sleep_male_7f8e6f08:

    sasha.say "И ты меня прости, что так вспылила."

translate russian vacuum_sasha_sleep_male_86d07102:

    mike.say "А..."

translate russian vacuum_sasha_sleep_male_95a9a8f5:

    "И через несколько секунд из меня льётся поток бессвязных оправданий."

translate russian vacuum_sasha_sleep_male_9ac4dd10:

    "Но когда приходит моя очередь пользоваться пылесосом, это хотя бы небольшое облегчение."

translate russian vacuum_sasha_sleep_male_9ae82089:

    "Будто она сама не любит включать тяжёлый металл на полной громкости, когда ей вздумается!"

translate russian vacuum_sasha_sleep_male_9f620037:

    "Это не совсем удар, но толчок достаточно сильный, чтобы я ахнул."

translate russian vacuum_sasha_sleep_male_9fb59e5d:

    sasha.say "Знаешь, может, если бы ты меньше времени проводил за Zbox..."

translate russian vacuum_sasha_sleep_male_a0f075d9:

    "Я встаю и наматываю шнур пылесоса на руку."

translate russian vacuum_sasha_sleep_male_a990adee:

    "С насадкой в одной руке и самим пылесосом, который я тащу за собой, можно быстро носиться туда-сюда."

translate russian vacuum_sasha_sleep_male_ac62671b:

    mike.say "Просто решил пропылесосить, понимаешь?"

translate russian vacuum_sasha_sleep_male_ad25a634:

    mike.say "Ничего страшного, Саша."

translate russian vacuum_sasha_sleep_male_ad668368:

    mike.say "Разве главное не то, что я вообще это делаю?"

translate russian vacuum_sasha_sleep_male_b199b4a5:

    mike.say "Нет..."

translate russian vacuum_sasha_sleep_male_b377ee3c:

    "Я уже собираюсь открыть рот и начать спорить с Сашей."

translate russian vacuum_sasha_sleep_male_b7a3fd73:

    sasha.say "А, вот как, значит?"

translate russian vacuum_sasha_sleep_male_bf285e89:

    "Но затем лучше разглядываю выражение её лица."

translate russian vacuum_sasha_sleep_male_e28c85c4:

    mike.say "О... привет, Саша."

translate russian vacuum_sasha_sleep_male_c030ae79:

    "Знаете, возможно, она права."

translate russian vacuum_sasha_sleep_male_c19115cb:

    "Подчёркивая свои слова, Саша тыкает вилкой мне в живот."

translate russian vacuum_sasha_sleep_male_c2746d37:

    "Но не успеваю пройти и половину коридора, как пылесос внезапно перестаёт работать."

translate russian vacuum_sasha_sleep_male_c63ec20c:

    mike.say "Просто скажи, если тебе что-нибудь понадобится."

translate russian vacuum_sasha_sleep_male_c7342867:

    sasha.say "И тебе стоит гораздо сильнее беспокоиться о другом."

translate russian vacuum_sasha_sleep_male_c8cdc9ab:

    "Я хватаюсь за вилку, а она поворачивается ко мне спиной и сердито уходит."

translate russian vacuum_sasha_sleep_male_c92076f4:

    "Она права, сейчас я веду себя как чертовски эгоистичный придурок."

translate russian vacuum_sasha_sleep_male_c9d6a45d:

    "Даже после стольких лет жизни с соседями я всё ещё умудряюсь облажаться."

translate russian vacuum_sasha_sleep_male_d5654db9:

    mike.say "Выполняю свою часть работы по поддержанию чистоты в доме!"

translate russian vacuum_sasha_sleep_male_d5a94df0:

    "Она зловеще смотрит на меня, раскачивая в воздухе вилку от пылесоса."

translate russian vacuum_sasha_sleep_male_d640ac3e:

    mike.say "Да ладно тебе, Саша."

translate russian vacuum_sasha_sleep_male_d72cc0ad:

    "С этой мыслью я стремительно прохожу комнаты и поднимаюсь наверх, чтобы закончить."

translate russian vacuum_sasha_sleep_male_d947840e:

    "Озадаченно я смотрю в насадку, пытаясь понять, не застряло ли там что-нибудь."

translate russian vacuum_sasha_sleep_male_ee1a4133:

    mike.say "Ты спала?"

translate russian vacuum_sasha_sleep_male_f83afa35:

    "Но затем замечаю усталость в её глазах."

translate russian vacuum_sasha_sleep_male_f91d1550:

    sasha.say "Мы, девушки, должны быть благодарны, что ты выполняешь свою часть?"

translate russian vacuum_sasha_sleep_male_fa774a0e:

    "Но затем её настроение смягчается, и она качает головой."

translate russian vacuum_sasha_sleep_male_fc9fa3f4:

    mike.say "Закончу уборку утром."

translate russian vacuum_sasha_sleep_male_fd5a876b:

    sasha.say "Благодаря тебе я уже не сплю."

translate russian vacuum_sasha_sleep_male_ff0ad9e2:

    "Может, действительно стоит закончить уборку утром..."

translate russian vacuum_sasha_sleep_male_ff37394c:

    "Раньше она просто злилась на меня."

translate russian wait_bored_ed524a6e:

    "Мне скучно..."

translate russian watch_movie_e9620d5b:

    "Я смотрю фильм."

translate russian watch_tv_with_1f9e733e:

    "Мы вместе смотрим порно."

translate russian watch_tv_with_3bfe9efe:

    "Мы смотрим новости."

translate russian watch_tv_with_422d977a:

    "Мы смотрим познавательный канал."

translate russian watch_tv_with_6b1c4b9f:

    "Мы смотрим показ мод."

translate russian watch_tv_with_6e58a236:

    "Мы смотрим романтическую комедию."

translate russian watch_tv_with_a072ee9d:

    "Мы смотрим [t]."

translate russian watch_tv_with_ce33ad85:

    "Мы смотрим концерт."

translate russian watch_tv_with_e9126fc0:

    "Мы смотрим забавный мультфильм."

translate russian watch_tv_with_ebde43ca:

    "Мы смотрим фильм ужасов под названием [t]."

translate russian watch_tv_with_f49e0e5c:

    "Мы смотрим научно-фантастический фильм."

translate russian wish_had_console_850f77dd:

    "Надо купить себе игровую приставку, смотреть телевизор скучно."

translate russian wish_had_fancy_clothes_a6d64235:

    "Я слышал, что где-то поблизости есть ночной клуб, но без приличной одежды меня туда не пустят."

translate russian wish_had_sport_clothes_35d204b9:

    "Я слышал, что где-то поблизости есть хороший спортзал, но без спортивной одежды меня туда не пустят."

translate russian wish_had_swimsuit_5b456668:

    "Вот бы у меня был купальник, тогда можно было бы нырнуть..."

translate russian work_b2b872b4:

    mike.say "Я немного работаю."

translate russian work_bakery_2f7d43a9:

    "Печь хлеб, делать бутерброды, продавать бутерброды. Скучно, зато счета оплачивает, верно?"

translate russian work_bookstore_1ca7141f:

    "Если я продам сто книг, то получу премию в один доллар!"

translate russian work_c8bd83aa:

    aletta.say "Думаешь, я не вижу, как ты отлыниваешь, [hero.name]?"

translate russian work_call_the_accountant_08c3c530:

    mike.say "Знаешь? Кто?!"

translate russian work_call_the_accountant_0a70d448:

    "Я кладу трубку. Остаётся лишь надеяться и молиться, что он достаточно помешает расследованию, чтобы оно хотя бы осталось без определённого результата."

translate russian work_call_the_accountant_0b94f2dc:

    "Jeff" "Я сейчас повешу трубку. До свидания, мистер [hero.family_name]."

translate russian work_call_the_accountant_0d28d21b:

    "Jeff" "Можете сделать со мной что угодно, но он способен на худшее. Я ничего не скажу."

translate russian work_call_the_accountant_10c12b2e:

    "Я беру телефон, чтобы позвонить бухгалтеру, но сначала перебираю в голове всё, что о нём знаю."

translate russian work_call_the_accountant_1115a729:

    "Jeff" "Ничего не обещаю, мистер [hero.family_name]. Но посмотрю, что можно сделать."

translate russian work_call_the_accountant_11e755f9:

    mike.say "Погоди, Джефф. Прежде чем ты это сделаешь, Кэссиди передаёт привет. Кстати, как мне связаться с твоей женой?"

translate russian work_call_the_accountant_143242f5:

    "Судя по голосу, Джефф старше, чем я думал. Ему как минимум пятьдесят, если только он не потратил слишком большую часть жизни на сигареты и выпивку."

translate russian work_call_the_accountant_15f45df3:

    "Jeff" "О боже, я не могу об этом говорить."

translate russian work_call_the_accountant_337681d0:

    "Jeff" "Мистер [hero.family_name], мы должны разговаривать с вами только в том случае, если у нас появятся вопросы. В настоящий момент вопросов к вам нет."

translate russian work_call_the_accountant_3bf4ad8e:

    "Jeff" "Послушайте, я сделаю что смогу. Подправлю некоторые цифры. Но слишком сильно вмешиваться нельзя. Он поймёт и сделает со мной то, что вам даже не по силам."

translate russian work_call_the_accountant_52d95e32:

    "Jeff" "Здравствуйте, это Джефф из бухгалтерии."

translate russian work_call_the_accountant_5c9e9787:

    mike.say "Мне нужно лишь, чтобы ты сбил расследование со следа. Я выясню, куда на самом деле ушли деньги, и ублюдок, который это сделал, заплатит."

translate russian work_call_the_accountant_5f0976d4:

    "Jeff" "Я уже знаю, кто это сделал, и вы не сможете заставить его заплатить."

translate russian work_call_the_accountant_62618517:

    "Jeff" "Пожалуйста, не делайте этого!"

translate russian work_call_the_accountant_67baa1e2:

    "Jeff" "Я... я... я не стану отвечать на эти вопросы."

translate russian work_call_the_accountant_732ea616:

    "Голос Джеффа срывается, и я слышу всхлип."

translate russian work_call_the_accountant_75721fd1:

    "Значит, лучше всего начать по-хорошему, а затем пригрозить рассказать его жене о любовнице. Это поставит его в тяжёлое положение."

translate russian work_call_the_accountant_7bcaff0c:

    mike.say "Лучше бы тебе это сделать. Лучше исправь всё для меня. Иначе..."

translate russian work_call_the_accountant_80ed6bb8:

    mike.say "Привет, Джефф! Меня зовут [heroname] [hero.family_name]. Думаю, ты понимаешь, о чём речь."

translate russian work_call_the_accountant_88771c06:

    "Jeff" "Я вам не верю."

translate russian work_call_the_accountant_895dc7e6:

    mike.say "О, я просто подумал, что твоей жене и любовнице найдётся о чём поговорить."

translate russian work_call_the_accountant_8c7a893e:

    "В начале разговора Джефф говорил уверенно, но теперь в его голосе слышится отчаяние. Кажется, он уже у меня на крючке, осталось лишь подтянуть леску."

translate russian work_call_the_accountant_91a805c6:

    mike.say "Тогда прекрати всё это!"

translate russian work_call_the_accountant_9beb37ca:

    mike.say "Послушай, Джефф. Я не могу объяснить яснее: если утону я, то утяну тебя за собой. Ты можешь это остановить."

translate russian work_call_the_accountant_9c41ba73:

    mike.say "Она уже угрожала рассказать Кэролайн. Ведь так зовут твою жену?"

translate russian work_call_the_accountant_9ddf0120:

    "Наступает пауза, и я слышу, как он сглатывает."

translate russian work_call_the_accountant_9df39617:

    "Я знаю, что у Кэссиди есть на него компромат."

translate russian work_call_the_accountant_a1294201:

    "Jeff" "НЕТ! Всё не так!"

translate russian work_call_the_accountant_a1fcdb93:

    "Jeff" "Пожалуйста, мистер [hero.family_name], она не позволяет мне остановиться. Это случилось всего один раз, но потом у неё появились фотографии, и она заставляет меня..."

translate russian work_call_the_accountant_a7bc53bf:

    "Снова наступает пауза, и я чувствую, как давление взлетает, пока жду, клюнет ли он на приманку."

translate russian work_call_the_accountant_aefabbce:

    mike.say "Джефф, слушай меня очень внимательно. Твоя потаскушка пытается пригвоздить мои яйца к стене и использует для этого тебя."

translate russian work_call_the_accountant_b1a8114d:

    mike.say "Хорошо, Джефф, не отвечай. Но что скажет Кэролайн? Ты ведь годишься Кэссиди в отцы?"

translate russian work_call_the_accountant_c836aa0d:

    mike.say "Уверен, прекрасно понимаешь, Джефф."

translate russian work_call_the_accountant_c837fde9:

    "Jeff" "Ч-ч-что вы хотите, чтобы я сделал?"

translate russian work_call_the_accountant_cd604f7b:

    mike.say "Не так? Тогда как?"

translate russian work_call_the_accountant_ce67a8dc:

    "Всё может стать ещё хуже, но я уже в отчаянии."

translate russian work_call_the_accountant_d03ffac2:

    "Jeff" "З-з-зачем вам связываться с моей женой?"

translate russian work_call_the_accountant_d09db9fb:

    mike.say "Тогда помоги мне остановить её. У меня кое-что на неё есть. С твоей помощью я смогу вытащить нас обоих."

translate russian work_call_the_accountant_d6ffb628:

    "Jeff" "Я... я не могу. Я не могу это остановить."

translate russian work_call_the_accountant_e09895c3:

    "По словам Кэссиди, именно он подстроил всю эту историю."

translate russian work_call_the_accountant_e103e495:

    mike.say "Чёрт возьми, Джефф! Не трусь сейчас. На кону твоя семья!"

translate russian work_call_the_accountant_ee967f26:

    "Jeff" "Это не ваше дело!"

translate russian work_call_the_accountant_f198283d:

    "Я глубоко вздыхаю и набираю его добавочный номер."

translate russian work_call_the_accountant_f59e0937:

    mike.say "Нет? Совсем никаких вопросов? Ты не хочешь спросить, куда делись деньги? Ах да, потому что ты и так знаешь."

translate russian work_call_the_accountant_f6601a80:

    "Jeff" "Я... пожалуйста!"

translate russian work_call_the_accountant_f6a2b706:

    "Jeff" "Вы можете отнять у меня семью, но он способен отнять всё. Абсолютно всё."

translate russian work_call_the_accountant_fb7f8bfb:

    "Jeff" "Не понимаю, о чём вы говорите."

translate russian work_call_the_accountant_fe2ad0b7:

    "И почти уверен, что он спит с Кэссиди."

translate russian work_call_the_accountant_fe568662:

    mike.say "Тебе и не нужно мне верить. Если не поможешь, тебе конец. В это ты веришь?"

translate russian work_coffeeshop_5664e56d:

    "Если я продам сто чашек кофе, то получу премию в один доллар!"

translate russian work_electronic_e49a92a8:

    "Вкалываешь или делаешь вид? Именно это спрашивают покупатели. Ответ всегда один: делаю вид."

translate russian work_f8276acc:

    "Никто не замечает, что я отлыниваю."

translate russian work_gym_1977a5b9:

    "Работать за стойкой спортзала далеко не так весело, как тренироваться в нём."

translate russian work_place_spy_camera_2_f14c3cea:

    "На это уходит немного времени, но я нахожу удачное место для камеры: оттуда виден весь офис, а заметить её почти невозможно, если специально не искать."

translate russian work_place_spy_camera_f14c3cea:

    "На это уходит немного времени, но я нахожу удачное место для камеры: оттуда виден весь офис, а заметить её почти невозможно, если специально не искать."

translate russian work_promoted_2_2aedf7a8:

    "Мне повысили зарплату!"

translate russian work_promoted_2_df00492b:

    "Я уже достиг высшего уровня своей некомпетентности."

translate russian work_promoted_2_f370533d:

    "На нынешней работе меня больше не повысят."

translate russian work_promoted_86cc6132:

    aletta.say "[hero.name], руководство решило повысить тебя."

translate russian work_promoted_98546bb3:

    aletta.say "Добро пожаловать в руководство. Отныне у тебя будет собственный кабинет."

translate russian work_promoted_9e2fe4f0:

    aletta.say "Не стоит. Вместе с повышением ты получишь больше обязанностей и от тебя будут ожидать большего."

translate russian work_promoted_ebaa6ab5:

    mike.say "Спасибо, я очень благодарен."

translate russian work_random_events_16af949e:

    mike.say "Эм... да. Одна сотрудница моей команды по имени Сиори довольно часто им пользуется."

translate russian work_random_events_049f3d57:

    "Можно, конечно, взбеситься, но это всего лишь дешёвый батончик, да и обед уже не так далеко."

translate russian work_random_events_12b5385d:

    "Shady guy" "Ур-р-гх... а ты пробовал выключить и снова включить его?"

translate russian work_random_events_09f3b438:

    "Но за это время я успел набить туда столько туалетной бумаги, что возникает мгновенный засор."

translate russian work_random_events_0b39c3db:

    "Вокруг люди всё ещё жалуются, а некоторые даже задыхаются и издают рвотные звуки."

translate russian work_random_events_0b8efdad:

    "Сняв трубку, я стискиваю зубы и готовлюсь услышать неприятный голос на другом конце линии."

translate russian work_random_events_0bff483e:

    "Мать пожимает плечами в ответ на мою странную вспышку и, к счастью, выбирает кого-то другого."

translate russian work_random_events_0cdb7acf:

    mike.say "Алло, это [hero.name]."

translate russian work_random_events_0e2ba8d0:

    "Отчаянно схватившись за остатки галстука, я упираюсь в шредер и тяну изо всех сил."

translate russian work_random_events_0ec24839:

    "Зато я замечаю, сколько заинтересованных взглядов со стороны других женщин в офисе приносит мне эта маленькая демонстрация отцовской заботы."

translate russian work_random_events_105d1d74:

    "Эта привычка осталась со студенческих времён, когда денег было так мало, что приходилось всерьёз рассчитывать, сколько туалетной бумаги я могу позволить себе купить на неделю."

translate russian work_random_events_11478e1b:

    "Shady guy" "Тогда попробуй. Это обычно решает процентов девяносто девять всех проблем, знаешь ли."

translate russian work_random_events_1288455d:

    mike.say "Конечно я это пробовал! За какого идиота ты меня принимаешь?"

translate russian work_random_events_141ec8f9:

    "Если только почти все остальные не ушли в отпуск, не взяли больничный или по какой-то другой причине не оказались на месте, когда это нужно сделать."

translate russian work_random_events_15be4a94:

    "Не знаю, почему меня так тянет признаться, что это сделал я."

translate russian work_random_events_15d00fdf:

    aletta.say "Я хочу, чтобы ты остался, пока не решишь проблему."

translate russian work_random_events_1707cf40:

    "Проблема лишь в том, что я слишком занят, чтобы отойти от стола и купить что-нибудь поесть."

translate russian work_random_events_183b83f2:

    "Это тоже вызывает странные взгляды, но всё же бесконечно лучше того, что было раньше."

translate russian work_random_events_7137b1dc:

    mike.say "О нет... нет-нет-нет... я бы боялся... уронить его... вот именно, я могу уронить твоего ребёнка!"

translate russian work_random_events_1cfa426f:

    mike.say "Хорошо, без проблем."

translate russian work_random_events_1cfa426f_1:

    mike.say "Хорошо, без проблем."

translate russian work_random_events_207e77f4:

    "Shady guy" "Эм, за такого, которому приходится звонить мне, чтобы починить то, с чем разобрался бы обычный дошкольник?"

translate russian work_random_events_21d9ea57:

    "Shady guy" "Да, это ИТ-отдел. Нам сообщили, что кто-то скачивал порно на компьютер в твоём кабинете."

translate russian work_random_events_21eee98f:

    "Возможно, на целлофане, в который завёрнут сэндвич, когда-то была записка с именем владельца."

translate russian work_random_events_01d70f78:

    "Shady guy" "Хм... ладно. Тогда предупреди её, что это могут поднять на следующей квартальной аттестации, хорошо?"

translate russian work_random_events_01d70f78_1:

    "Shady guy" "Хм... ладно. Тогда предупреди её, что это могут поднять на следующей квартальной аттестации, хорошо?"

translate russian work_random_events_22b695ef:

    "До моего этажа осталось всего несколько пролётов. Нужно лишь молчать."

translate russian work_random_events_23e0d0a7:

    "Обрезая остатки галстука, чтобы освободиться, я думаю, что всё равно никогда особенно его не любил."

translate russian work_random_events_28d5dde7:

    audrey.say "Я серьёзно облажалась."

translate russian work_random_events_2955257a:

    "Теперь она, похоже, решила усугубить причинённые неудобства и раздражение, явившись в офис, чтобы похвастаться конечным результатом своих усилий."

translate russian work_random_events_2a8547d3:

    "Хуже того, рядом сейчас нет никого, кого можно было бы попросить сбегать за обедом."

translate russian work_random_events_2c9b935e:

    "По-прежнему голодный и теперь ещё ужасно пристыженный, я спешу обратно к своему столу, а даже вой сигнализации не заглушает урчание в животе."

translate russian work_random_events_2f2ebe7a:

    "Но затем во мне наконец просыпается адреналин, и я каким-то образом нахожу силы дёрнуть так сильно, что слышу, как внутри аппарата что-то натягивается и ломается."

translate russian work_random_events_10e43bb1:

    mike.say "Ладно, спасибо... попробую и перезвоню, если не поможет."

translate russian work_random_events_2f7191e4:

    "Либо накануне я куда-нибудь выбирался и слишком сильно перебрал, либо мне пришлось не спать всю ночь, чтобы подготовить всё к самому совещанию."

translate russian work_random_events_30c41006:

    "О боже, почему это никак не закончится?"

translate russian work_random_events_31a3d261:

    audrey.say "Спасибо, ты меня спас."

translate russian work_random_events_31f75536:

    "Shady guy" "Здравствуйте, ИТ-отдел."

translate russian work_random_events_32ffd088:

    aletta.say "Разумеется, ты получишь премию."

translate russian work_random_events_32ffd088_1:

    aletta.say "Разумеется, ты получишь премию."

translate russian work_random_events_340b7bf4:

    "Глубоко вздохнув, я решаю потерпеть ещё немного."

translate russian work_random_events_34201f3f:

    "Когда вода начинает переливаться через край и растекаться по кафельному полу, я бегу с места преступления."

translate russian work_random_events_3b2c0952:

    aletta.say "[hero.name], мы должны закончить это к завтрашнему дню. Я хочу, чтобы ты задержался ещё на пару часов."

translate russian work_random_events_3ba2622c:

    "Ну вот, опять!"

translate russian work_random_events_3d991a39:

    "Обычно проблем нет, но сегодня утром я выполняю привычный ритуал и после необходимого смыва собираюсь уйти."

translate russian work_random_events_3db7b741:

    "Мне остаётся лишь украдкой вернуться к своему столу и надеяться, что никто не свяжет меня с чудовищем, которое сейчас затапливает туалет."

translate russian work_random_events_3e28fdf7:

    "Я нащупываю трубку и зажимаю её плечом у уха, продолжая печатать."

translate russian work_random_events_3e52eacb:

    "Люди закрывают носы и начинают недовольно ворчать и перешёптываться."

translate russian work_random_events_40451948:

    "Смутившись и слегка запаниковав, я поспешно набрасываю сверху пригоршни туалетной бумаги, чтобы скрыть улики, пока думаю, что делать."

translate russian work_random_events_40a659df:

    "В приступе вызванной голодом ярости я набрасываюсь на автомат, колочу кулаками по стеклу и пытаюсь вытрясти застрявший батончик."

translate russian work_random_events_42f36eea:

    "На следующем этаже люди выходят, одаривая меня суровыми и злобными взглядами."

translate russian work_random_events_434432b8:

    "Как бы то ни было, в день совещания я неизменно совершенно измотан и едва не засыпаю."

translate russian work_random_events_43bfffdc:

    "Но затем случайно оглядываюсь и замечаю, что смыв не справился."

translate russian work_random_events_465e9579:

    mike.say "Да, привет. Слушай, мой компьютер барахлит..."

translate russian work_random_events_4b1b1485:

    "Алетта подходит ко мне."

translate russian work_random_events_4c46c5a5:

    "Я сразу же бросаюсь в ближайший туалет, забегаю в кабинку и снимаю разные туфли."

translate russian work_random_events_4d410cf1:

    "Мало того что моей команде пришлось подменять сотрудницу другого отдела, пока она ушла в декрет, который, казалось, длился целое десятилетие."

translate russian work_random_events_4eb27b8e:

    "Он будто издевается надо мной!"

translate russian work_random_events_4f2cd574:

    mike.say "Ладно, давай сюда маленького засранца!"

translate russian work_random_events_4f3fa372:

    "Но тут что-то внезапно начинает тянуть меня вниз, к острым как бритва лезвиям."

translate russian work_random_events_52afc35c:

    "Сегодня идеальный пример: впереди лишь часы скучных презентаций и слайды с инфографикой, превращающие мозг в кашу."

translate russian work_random_events_5503efb1:

    "Я знаю, что бывает, когда нечто подобное не понимает намёка после первого смыва."

translate russian work_random_events_577b3c60:

    mike.say "Хорошо, без проблем, босс."

translate russian work_random_events_75223de0:

    mike.say "Эм... да... возможно, это был я."

translate russian work_random_events_5d693608:

    "Shady guy" "Успокойся, приятель. Пришлю кого-нибудь, как только у нас появится свободный человек..."

translate russian work_random_events_5e1289b7:

    "Нет, это уже вопрос личной гордости. Я не усну на глазах у этих людей!"

translate russian work_random_events_625ab6a4:

    mike.say "Простите, босс, у меня уже есть планы."

translate russian work_random_events_625ab6a4_1:

    mike.say "Простите, босс, у меня уже есть планы."

translate russian work_random_events_63211b7c:

    "Домашний, набитый начинкой, которой у меня дома никогда не бывает, он мгновенно вводит меня в искушение..."

translate russian work_random_events_64ab229a:

    "Я медленно кладу трубку и клянусь себе больше никогда не смотреть порно в офисе."

translate russian work_random_events_676a70dc:

    mike.say "Слушай сюда, переоценённый задрот. Просто пришли кого-нибудь починить мой чёртов компьютер, ясно?"

translate russian work_random_events_67811c61:

    "Кто будет выглядеть подозрительнее парня, который пять минут назад умирал от голода, а теперь утверждает, что уже не хочет есть?"

translate russian work_random_events_679a9011:

    "Мне стыдно это признавать, но я привык по утрам ждать прихода на работу, чтобы сходить в туалет по-большому, если понимаете, о чём я."

translate russian work_random_events_681967d9:

    "Одри подходит к моему столу с виноватым выражением лица."

translate russian work_random_events_6ab93d4c:

    "Я нажимаю кнопки какого-то энергетического батончика с мюсли, решив, что это не так стыдно, как шоколад или другая сладкая дрянь."

translate russian work_random_events_6d732cb1:

    "Я почти слышу, как его коллеги хихикают на заднем плане."

translate russian work_random_events_6e28f2f9:

    mike.say "Прости, Одри, у меня нет времени."

translate russian work_random_events_758ab415:

    "Но сегодня мне пришлось выбежать из дома без завтрака, а до обеда ещё несколько часов."

translate russian work_random_events_7627fafb:

    "Shady guy" "Слушай, приятель, моя работа — разбираться с фактами, а не с оттенками серого!"

translate russian work_random_events_77d04d42:

    "Но тут случается кошмар: батончик падает вперёд и застревает у стекла, всего в дюйме от моего лица."

translate russian work_random_events_78740727:

    "В отчаянии я спешу в комнату отдыха и начинаю рыться в холодильнике в поисках чего-нибудь съедобного."

translate russian work_random_events_7aeaf08f:

    mike.say "Ну... вообще-то нет, не пробовал."

translate russian work_random_events_7f5d2ccc:

    "Что плохого может случиться, если пару минут подержать ребёнка?"

translate russian work_random_events_83d6242e:

    "Дело не в том, что я боюсь остаться без возможности работать, а в том, что терпеть не могу звонить в ИТ-отдел и просить их всё починить."

translate russian work_random_events_83ecaa31:

    "По крайней мере, пока не придумаю, как делать это безнаказанно..."

translate russian work_random_events_843fb53d:

    "Мне кажется, будто все нарочно прижимаются ко мне. Дай они мне хоть немного места, я, возможно, сумел бы сдержаться."

translate russian work_random_events_8469bb28:

    "Я работаю ещё два часа."

translate russian work_random_events_8469bb28_1:

    "Я работаю ещё два часа."

translate russian work_random_events_85dbc615:

    "Я захожу в лифт, стараясь не обращать внимания на смех вокруг и сосредоточиться на предстоящем дне."

translate russian work_random_events_8698a00f:

    "Откладывать дальше бессмысленно, поэтому я хватаю столько, сколько могу унести, и направляюсь к шредеру."

translate russian work_random_events_888f79bc:

    "К счастью, он с хрустом останавливается, оставляя меня в живых, но теперь придётся объяснять, как я умудрился сломать дорогую офисную технику по собственной глупости."

translate russian work_random_events_89575b56:

    "Я успокаиваю дыхание и закусываю губу, сдерживаясь после его высокомерного ответа."

translate russian work_random_events_8cd2dad7:

    "Если бы я ходил и показывал людям то, что вышло из моего тела, ожидая похвалы, меня бы заперли и выбросили ключ!"

translate russian work_random_events_8cf87fa5:

    "Поэтому обычно не мне достаётся самая дерьмовая офисная работа вроде копирования и уничтожения документов."

translate russian work_random_events_8ed4acfd:

    "Чёрт, туда затянуло мой галстук! Почему я не мог подождать до дня свободной одежды?"

translate russian work_random_events_8fe20296:

    aletta.say "Ничего себе, как всегда впечатляет, [hero.name]!"

translate russian work_random_events_9006d843:

    "Я два часа пытаюсь исправить последствия ошибки Одри."

translate russian work_random_events_90b1d6df:

    "К счастью, мне удалось занять место, где меня почти никто не видит, и я уже чувствую, как голова начинает опускаться."

translate russian work_random_events_91ddb9eb:

    "Но что произойдёт, когда настоящий владелец обнаружит пропажу и начнёт искать свой сэндвич?"

translate russian work_random_events_97ef8e53:

    "Я засовываю первую пачку внутрь и запускаю аппарат."

translate russian work_random_events_9916d089:

    "Вот почему я оказываюсь в коридоре и отчаянно запихиваю купюры в торговый автомат, чтобы добыть хоть что-нибудь пожевать."

translate russian work_random_events_995571a2:

    mike.say "Я уже всё исправил, босс."

translate russian work_random_events_99cfcaad:

    "Теперь я заперт здесь плечом к плечу с более чем дюжиной людей, работающих в том же здании."

translate russian work_random_events_9b8e77cb:

    "И конечно же, как только её мочевой пузырь, который беременность, по-видимому, полностью уничтожила, требует внимания, она начинает искать, кому отдать ребёнка."

translate russian work_random_events_a0f336e1:

    "Поэтому я как можно быстрее и непринуждённее выскальзываю из туалета."

translate russian work_random_events_3a1bf7fb:

    mike.say "Эм... да. Одна сотрудница моей команды по имени Одри довольно часто им пользуется."

translate russian work_random_events_a434a29f:

    aletta.say "[hero.name], у нас чрезвычайная ситуация! Нужно как можно скорее исправить эту ошибку."

translate russian work_random_events_aafbad8d:

    "Я возвращаюсь к своему столу, смирившись с тем, что весь день проведу с голодными спазмами и урчащим животом."

translate russian work_random_events_accbce6a:

    aletta.say "Отличная работа, [hero.name], мы закончили как раз вовремя!"

translate russian work_random_events_accbce6a_1:

    aletta.say "Отличная работа, [hero.name], мы закончили как раз вовремя!"

translate russian work_random_events_af4601fa:

    "И тут замечаю рядом с молоком весьма аппетитный сэндвич."

translate russian work_random_events_af947072:

    "А, к чёрту. Мне самому ничего представлять не нужно, и меня никто не видит."

translate russian work_random_events_b1960c6a:

    "Похоже, кто-то оценил мои усилия, даже если не я сам."

translate russian work_random_events_b230bd33:

    "Клянусь, я понятия не имел, что это произойдёт, даже когда ждал лифт и заходил внутрь."

translate russian work_random_events_b2bce46a:

    "Малыш и так почти спит и лишь оглядывается да немного ёрзает, пока мать не возвращается и не забирает его."

translate russian work_random_events_b3aea5fe:

    "Вот дерьмо, у меня уже очко сжимается от страха!"

translate russian work_random_events_b40be999:

    "Внезапно срабатывает встроенная сигнализация, предназначенная как раз для защиты от подобных приступов первобытного насилия, и все на этаже поворачиваются ко мне."

translate russian work_random_events_34332603:

    mike.say "Это вышло случайно... я могу всё объяснить..."

translate russian work_random_events_b51138f3:

    "Надеясь выглядеть невиновным, я тоже присоединяюсь к ним, возможно, даже с излишним усердием."

translate russian work_random_events_b5dfb0c0:

    "Я ведь уже несколько недель не ел ни мексиканской, ни индийской еды!"

translate russian work_random_events_b5e068e1:

    "В итоге мне удаётся выдержать всё совещание, и в конце я даже получаю небольшие аплодисменты."

translate russian work_random_events_b74562ce:

    "Всё, это последняя капля!"

translate russian work_random_events_b90388f0:

    "А сейчас я здесь совершенно один, и мой стол выглядит так, словно я пытался построить крепость из стопок бумаг, которые давно следовало измельчить."

translate russian work_random_events_bb65c014:

    "Я опускаю взгляд и с ужасом вижу, что на мне разные туфли. Мало того, одна со шнурками, а другая вообще без них!"

translate russian work_random_events_bd40fe00:

    "Но я не вижу её ни на упаковке, ни даже на полке."

translate russian work_random_events_bd7cf22d:

    "Он что, действительно включил громкую связь, чтобы они всё слушали?"

translate russian work_random_events_3aafc20b:

    mike.say "Да... конечно."

translate russian work_random_events_beb03286:

    "Как только шум набирающегося бачка стихает, я снова яростно нажимаю на слив."

translate russian work_random_events_bf18f2b1:

    "Как мне теперь с этим жить?!"

translate russian work_random_events_bfc12017:

    "Shady guy" "Жди, что это всплывёт на следующей квартальной аттестации, ясно?"

translate russian work_random_events_c2c04cf3:

    "Повторение того же действия не поможет, и придётся принимать более радикальные меры."

translate russian work_random_events_c934f985:

    "Я мысленно умоляю её выбрать одну из женщин, которые стоят вокруг и умиляются, но она смотрит прямо на меня."

translate russian work_random_events_c96ade12:

    "Некоторые коллеги замечают происходящее, и мне не раз достаётся локтем под рёбра."

translate russian work_random_events_ca1697a5:

    "Последнее, что мне нужно даже в обычный рабочий день, — это чтобы компьютер начал барахлить."

translate russian work_random_events_ca8d4d25:

    "Я, конечно, не вхожу в совет директоров, но и не нахожусь на самом дне служебной иерархии."

translate russian work_random_events_cb4bb4bf:

    "Если я хочу не уснуть, придётся серьёзно постараться."

translate russian work_random_events_cb921393:

    mike.say "Прости, игрушка, у меня нет времени."

translate russian work_random_events_cea10cb8:

    "Так продолжается, пока мне не начинает казаться, будто кто-то зовёт меня по имени."

translate russian work_random_events_cec41ed0:

    "Внимание ко мне нарастает как снежный ком, пока все вокруг не начинают смотреть на мои ноги и сдерживать смех."

translate russian work_random_events_cf588e4b:

    "И почему пахнет горящей покрышкой?"

translate russian work_random_events_d1b30924:

    "Обычно я не перекусываю между приёмами пищи. Это плохая привычка, которая в долгосрочной перспективе серьёзно портит диету."

translate russian work_random_events_f4b18203:

    mike.say "Ч... что... какого... я не сплю... и штаны на мне!"

translate russian work_random_events_d2e07ae1:

    "Я тут же качаю головой и начинаю пятиться от протянутого младенца, словно у него чума."

translate russian work_random_events_d2e951a1:

    "Размахивая рукой в сторону стены, я успеваю щёлкнуть выключателем как раз в тот момент, когда меня начинает тянуть вниз."

translate russian work_random_events_d5630c89:

    "Шредер с хрустом останавливается, и я наконец облегчённо вздыхаю, потянувшись за лежащими рядом ножницами."

translate russian work_random_events_d670f55d:

    "Я съедаю его так быстро, что едва не зарабатываю несварение."

translate russian work_random_events_db33d045:

    "Всё равно потом чувствовал бы вину за этот перекус."

translate russian work_random_events_dd91add2:

    "Стараясь не обращать внимания на чувство вины, я хватаю сэндвич и крадучись возвращаюсь к своему столу."

translate russian work_random_events_684bf95b:

    mike.say "Я... простите..."

translate russian work_random_events_dec7e159:

    "Но между этажами раздаётся неизбежный звук, похожий на долгий предсмертный хрип воздушного шарика."

translate russian work_random_events_ded21a0e:

    "Я просыпаюсь и вижу, что вся комната с весёлым ужасом смотрит на меня, а люди изо всех сил стараются не рассмеяться."

translate russian work_random_events_e4c735ce:

    mike.say "Ничего себе, понятия не имею, о чём ты!"

translate russian work_random_events_e81b7bf9:

    "Я действительно хочу его съесть."

translate russian work_random_events_e82d9f04:

    "Некоторое время всё висит на волоске, а вращающиеся лезвия становятся всё ближе."

translate russian work_random_events_e9ae6b8a:

    "Я даже не пытаюсь бороться с сонливостью и вскоре проваливаюсь в туманный сон."

translate russian work_random_events_ecddefe3:

    "Алетта подходит к моему столу."

translate russian work_random_events_ed5d3a37:

    "Я сосредоточенно смотрю на экран компьютера, когда на столе звонит телефон."

translate russian work_random_events_ef734b2f:

    "А заниматься таким на работе я даже не собираюсь."

translate russian work_random_events_efaa2365:

    "Сначала всё кажется нормальным, но, пока я жду лифт в холле, проходящие мимо люди начинают смеяться и поглядывать вниз."

translate russian work_random_events_aa4ecafa:

    "Shady guy" "Правда?.. Тогда у кого-нибудь ещё есть доступ к твоему компьютеру?"

translate russian work_random_events_f5b59989:

    "Остаток дня я хожу туда-сюда в одних носках."

translate russian work_random_events_f5d33a5c:

    "Просто кажется, что в любую секунду кто-нибудь всё равно укажет на меня как на виновника."

translate russian work_random_events_f8007bd7:

    audrey.say "Я удалила все данные по этому проекту и не могу найти резервную копию. Поможешь мне?"

translate russian work_random_events_f8fd12ab:

    "Я изо всех сил стараюсь не заснуть, пару раз почти отключаюсь, но каждый раз резко прихожу в себя."

translate russian work_random_events_fa2b7889:

    "Я уже начинаю паниковать, но тут вспоминаю, что именно для таких случаев выключатель шредера расположен на уровне груди."

translate russian work_random_events_fca35779:

    "Живот урчит так сильно, что я совершенно не могу сосредоточиться ни на чём, хоть немного связанном с работой."

translate russian work_random_events_fcd8db33:

    "Уже почти обед, и я слышу, как желудок урчит в предвкушении."

translate russian work_random_events_fd43cdbd:

    "Не знаю, как так получается, но это случается каждый раз, когда приходится сидеть на совещании отдела."

translate russian work_random_events_fded749d:

    "Как только лифт достигает моего этажа, я вываливаюсь наружу и делаю глубокий, восхитительный вдох чистого воздуха."

translate russian work_random_events_fe7d8461:

    "Обычно я не одеваюсь в темноте, но сегодня проспал и так спешил выйти из дома, что именно так и поступил."

translate russian work_sexshop_f33ff241:

    "Скажу честно, мне нравится продавать дилдо."

translate russian work_with_3851180b:

    mike.say "[active_girl.name], тебе помочь?"

translate russian work_with_866f2d09:

    "Я помогаю [active_girl.name] с работой."

translate russian work_with_b778778c:

    active_girl.say "Конечно, почему бы и нет?"

translate russian work_with_f62eb64c:

    active_girl.say "Прости, мне не нужна твоя помощь."

translate russian workhard_0afe3bd4:

    "Я усердно работаю."

translate russian workhard_a8e420be:

    aletta.say "Что ты делаешь, [hero.name]? Ты допустил столько ошибок, что теперь нам придётся начинать всё сначала..."

translate russian workhard_ddb61f34:

    "Мне удаётся сделать вдвое больше работы!"

translate russian xmas_party_presents_86d07102:

    mike.say "А..."

translate russian xmas_party_presents_86d07102_1:

    mike.say "А..."

translate russian xmas_party_presents_86d07102_2:

    mike.say "А..."

translate russian xmas_party_presents_e980e5d7:

    mike.say "Это..."

translate russian xmas_party_presents_e980e5d7_1:

    mike.say "Это..."

translate russian xmas_party_pudding_200eb25b:

    mike.say "Эй!"

translate russian xmas_party_pudding_30e74fc5:

    mike.say "Эм..."

translate russian xmas_party_singing_67d5b96e:

    mike.say "Угх..."

translate russian xmas_party_snacks_f1d8a63c:

    mike.say "Эм..."

translate russian xmas_party_turkey_30e74fc5:

    mike.say "Эм..."

translate russian xmas_party_turkey_55e4dd91:

    "Но что тут может быть сложного?"

translate russian xmas_party_turkey_9efa96ce:

    mike.say "Что происходит?"

translate russian strings:

    old "\n[renpy.license!t]"
    new "[renpy.license!t]"

    old "\n{color=#fff}Copied to clipboard.{/color}"
    new "{color=#fff}Скопировано в буфер обмена.{/color}"

    old "    [s]"
    new "[s]"

    old " translates [tl.filename]:[tl.linenumber]"
    new "переводит [tl.filename]:[tl.linenumber]"

    old "!"
    new "!"

    old "\""
    new "\""

    old "#"
    new "#"

    old "$"
    new "$"

    old "%"
    new "%"

    old "%b %d, %H:%M"
    new "%d %b, %H:%M"

    old "&"
    new "&"

    old "("
    new "("

    old "(attributes)"
    new "(аттрибуты)"

    old "(channel)"
    new "(канал)"

    old "(clear retained bubbles)"
    new "(очистить сохранившиеся пузыри)"

    old "(filename)"
    new "(имя файла)"

    old "(hide)"
    new "(скрыть)"

    old "(statement)"
    new "(оператор)"

    old "(tag)"
    new "(тег)"

    old "(transform)"
    new "(трансформация)"

    old "(transition)"
    new "(переход)"

    old ")"
    new ")"

    old "*"
    new "*"

    old "+"
    new "+"

    old "+START+"
    new "+НАЧАТЬ+"

    old "-"
    new "-"

    old "."
    new "."

    old "... "
    new "..."

    old "/"
    new "/"

    old "0"
    new "0"

    old "1"
    new "1"

    old "1. "
    new "1."

    old "10%"
    new "10%"

    old "2"
    new "2"

    old "2. "
    new "2."

    old "25%"
    new "25%"

    old "3"
    new "3"

    old "3 guys and some rope"
    new "Трое парней и немного верёвки"

    old "3 years and 11 months actually. I'm a courier so time matters to me."
    new "Вообще-то три года и одиннадцать месяцев. Я курьер, поэтому время для меня важно"

    old "3. "
    new "3."

    old "30"
    new "30"

    old "4"
    new "4"

    old "4. "
    new "4."

    old "5"
    new "5"

    old "5. "
    new "5."

    old "6"
    new "6"

    old "6. "
    new "6."

    old "60"
    new "60"

    old "7"
    new "7"

    old "8"
    new "8"

    old "9"
    new "9"

    old ":"
    new ":"

    old ";"
    new ";"

    old "<"
    new "<"

    old "<<"
    new "<<"

    old "="
    new "="

    old ">"
    new ">"

    old "> "
    new ">"

    old ">>"
    new ">>"

    old "@"
    new "@"

    old "[[LIE] No"
    new "[[LIE] Нет"

    old "[accessory!i]"
    new "[accessory!i]"

    old "[attributes] "
    new "[attributes]"

    old "[audio!q]"
    new "[audio!q]"

    old "[authentication_status.get('authorization_token')]"
    new "[authentication_status.get('authorization_token')]"

    old "[authentication_status.get('portal_environment')]"
    new "[authentication_status.get('portal_environment')]"

    old "[authentication_status.get('provider')]"
    new "[authentication_status.get('provider')]"

    old "[authentication_status.get('valid')]"
    new "[authentication_status.get('valid')]"

    old "[behind]"
    new "[behind]"

    old "[bree.name]"
    new "[bree.name]"

    old "[bree.name] and Lexi team together"
    new "[bree.name] и Лекси объединяются"

    old "[channel] "
    new "[channel]"

    old "[clothes!i]"
    new "[clothes!i]"

    old "[config.name!t]"
    new "[config.name!t]"

    old "[config.version]"
    new "[config.version]"

    old "[expr!q]: "
    new "[expr!q]:"

    old "[filename]:[line]"
    new "[filename]:[line]"

    old "[fps:.1f] fps\n[cur_time:.3f] ms\n[max_time:.3f] ms max\n[renderer]"
    new "[fps:.1f] кадр/с\n[cur_time:.3f] мс\n[max_time:.3f] мс макс.\n[renderer]"

    old "[game.flags.alarm_time]:00"
    new "[game.flags.alarm_time]:00"

    old "[game.timers.injured] ['day' if game.timers.injured == 1 else 'days']"
    new "[game.timers.injured] ['day' if game.timers.injured == 1 else 'days']"

    old "[game.timers.sick] ['day' if game.timers.sick == 1 else 'days']"
    new "[game.timers.sick] ['day' if game.timers.sick == 1 else 'days']"

    old "[game_id]:"
    new "[game_id]:"

    old "[he.command!q]"
    new "[he.command!q]"

    old "[he.result!q]"
    new "[he.result!q]"

    old "[he.result]"
    new "[he.result]"

    old "[hero.name] should be in the photo too"
    new "[hero.name] тоже должен быть на фотографии"

    old "[hero.name] tells Harmony that he does not feel the same way"
    new "[hero.name] говорит Хармони, что не испытывает к ней того же"

    old "[i]: [name]"
    new "[i]: [name]"

    old "[image_tag!q]"
    new "[image_tag!q]"

    old "[item_price] "
    new "[item_price]"

    old "[kind] "
    new "[kind]"

    old "[line!q]"
    new "[line!q]"

    old "[line_pos]"
    new "[line_pos]"

    old "[line_text!q]"
    new "[line_text!q]"

    old "[message!q]"
    new "[message!q]"

    old "[mode]"
    new "[mode]"

    old "[n]%"
    new "[n]%"

    old "[new] [seen]/[total]"
    new "[new] [seen]/[total]"

    old "[npc.name]"
    new "[npc.name]"

    old "[page]"
    new "[page]"

    old "[piercing.location!cl]"
    new "[piercing.location!cl]"

    old "[prog]/100"
    new "[prog]/100"

    old "[prop!q]"
    new "[prop!q]"

    old "[renpy.game.exception_info]"
    new "[renpy.game.exception_info]"

    old "[save_name!q]"
    new "[save_name!q]"

    old "[shown_npc.id] [display_shown]"
    new "[shown_npc.id] [display_shown]"

    old "[state.kind] "
    new "[state.kind]"

    old "[submenu]"
    new "[submenu]"

    old "[tag] "
    new "[tag]"

    old "[transforms] "
    new "[transforms]"

    old "[transition]"
    new "[transition]"

    old "[u.debug_message!q]"
    new "[u.debug_message!q]"

    old "[u.download_done_mb]/[u.download_total_mb] MB"
    new "[u.download_done_mb]/[u.download_total_mb] МБ"

    old "[u.message!q]"
    new "[u.message!q]"

    old "[u.version] is available. Do you want to install it?"
    new "[u.version] доступна. Вы хотите её установить?"

    old "[val]%"
    new "[val]%"

    old "[value!q]"
    new "[value!q]"

    old "_"
    new "_"

    old "A"
    new "A"

    old "a"
    new "a"

    old "A coffee it is"
    new "Тогда кофе"

    old "A few"
    new "Несколько"

    old "A friend date, then"
    new "Тогда дружеское свидание"

    old "A little bit of both"
    new "И то и другое понемногу"

    old "A little pain is good for her"
    new "Немного боли пойдёт ей на пользу"

    old "A lot"
    new "Много"

    old "A mermaid for Ayesha and a mermaid for Kylie"
    new "Русалка для Айши и русалка для Кайли"

    old "A mermaid for Ayesha and a shark for Kylie"
    new "Русалка для Айши и акула для Кайли"

    old "A mermaid for Kylie and a whale for Ayesha"
    new "Русалка для Кайли и кит для Айши"

    old "A whale for Ayesha and a shark for Kylie"
    new "Кит для Айши и акула для Кайли"

    old "Abort"
    new "Прервать"

    old "ABOUT"
    new "ОБ ИГРЕ"

    old "About"
    new "Об игре"

    old "About birth control"
    new "О контрацепции"

    old "About locker room"
    new "О раздевалке"

    old "About treadmill"
    new "О беговой дорожке"

    old "About what we call each other"
    new "О том, как нам называть друг друга"

    old "About your body/appearance"
    new "О твоём теле и внешности"

    old "Absolutely"
    new "Безусловно"

    old "Accept"
    new "Согласиться"

    old "Accept invitation"
    new "Принять приглашение"

    old "Accept Samantha"
    new "Принять Саманту"

    old "Accept the drink"
    new "Принять напиток"

    old "Accesses the game menu."
    new "Открывает игровое меню"

    old "accessibility menu"
    new "меню специальных возможностей"

    old "Accessibility Menu. Use up and down arrows to navigate, and enter to activate buttons and bars."
    new "Меню специальных возможностей. Для навигации используйте стрелки вверх и вниз, а для активации кнопок и панелей - клавишу Enter."

    old "Accessory:"
    new "Аксессуар:"

    old "Accuse Aletta"
    new "Обвинить Алетту"

    old "Accuse Audrey"
    new "Обвинить Одри"

    old "Accuse Shiori"
    new "Обвинить Сиори"

    old "achievements"
    new "достижения"

    old "Action movie"
    new "Боевик"

    old "activate"
    new "элемент активирован"

    old "Active"
    new "Активные"

    old "Add"
    new "Добавить"

    old "Admire the view"
    new "Полюбоваться видом"

    old "Admit"
    new "Признать"

    old "Admit cheating"
    new "Признаться в измене"

    old "Admit guilt"
    new "Признать вину"

    old "Admit it"
    new "Признаться"

    old "Admit it looks inviting for an amorous liaison"
    new "Признать, что место подходит для романтической встречи"

    old "Admit that you were looking"
    new "Признаться, что ты смотрел"

    old "Admit to buying condoms"
    new "Признаться в покупке презервативов"

    old "Advances dialogue and\nactivates the interface."
    new "Продолжает диалог и\nактивирует интерфейс"

    old "Advances dialogue and activates the interface."
    new "Продолжает диалог и активирует интерфейс"

    old "Advances dialogue without selecting choices."
    new "Продолжает диалог, не выбирая варианты"

    old "Advocate innocence"
    new "Отстаивать невиновность"

    old "After Choices"
    new "После выборов"

    old "after choices"
    new "после выборов"

    old "Agree"
    new "Согласиться"

    old "Agree (-2000$)"
    new "Согласиться (-2000$)"

    old "Agree and compliment Kylie"
    new "Согласиться и сделать Кайли комплимент"

    old "Agree that Ayesha should have a termination"
    new "Согласиться, что Айше стоит прервать беременность"

    old "Agree that the verses have illuminated your own sins"
    new "Согласиться, что эти стихи раскрыли твои собственные грехи"

    old "Agree that things have changed for the worse"
    new "Согласиться, что всё изменилось к худшему"

    old "Agree to a conjugal visit"
    new "Согласиться на супружеское свидание"

    old "Agree to ask Cassidy"
    new "Согласиться спросить Кэссиди"

    old "Agree to getting hot-dogs"
    new "Согласиться на хот-доги"

    old "Agree to give Kylie a tour"
    new "Согласиться провести Кайли экскурсию"

    old "Agree to help"
    new "Согласиться помочь"

    old "Agree to help Camila undercover"
    new "Согласиться помочь Камиле под прикрытием"

    old "Agree to let Alexis cuddle"
    new "Разрешить Алексис обниматься"

    old "Agree to manage Ayesha"
    new "Согласиться быть менеджером Айши"

    old "Agree to meet Harmony's family"
    new "Согласиться встретиться с семьёй Хармони"

    old "Agree to play"
    new "Согласиться сыграть"

    old "Agree to split in half"
    new "Согласиться разделить пополам"

    old "Agree to the Maid Cafe"
    new "Согласиться на кафе с горничными"

    old "Agree with [bree.name]"
    new "Согласиться с [bree.name]"

    old "Agree with Alexis"
    new "Согласиться с Алексис"

    old "Agree with Anna"
    new "Согласиться с Анной"

    old "Agree with Kleio"
    new "Согласиться с Клео"

    old "Agree with Sasha"
    new "Согласиться с Сашей"

    old "Agree with Shiori"
    new "Согласиться с Сиори"

    old "Aletta"
    new "Aletta"

    old "Aletta should not wear her sexy uniform anymore"
    new "Алетта больше не должна носить сексуальную униформу"

    old "Aletta should put her bottom back on"
    new "Алетта должна снова надевать низ"

    old "Aletta should put her top back"
    new "Алетта должна снова надевать верх"

    old "Aletta should put her uniform back"
    new "Алетта должна снова надевать униформу"

    old "Aletta should remove her bottoms at work"
    new "Алетта должна снимать низ на работе"

    old "Aletta should remove her top at work"
    new "Алетта должна снимать верх на работе"

    old "Aletta should remove her uniform at work"
    new "Алетта должна снимать униформу на работе"

    old "Aletta should wear her sexy uniform"
    new "Алетта должна носить свою сексуальную униформу"

    old "Alexis should wear less clothes"
    new "Алексис должна надеть меньше одежды"

    old "Alice Taylor, LordTouchMe, Devilman1987, Abdul, lucas lofgren,"
    new "Alice Taylor, LordTouchMe, Devilman1987, Abdul, lucas lofgren,"

    old "Alkatraz, Kyle Weber, Frank Mecka, Tobi, Manuel Fernandez,"
    new "Alkatraz, Kyle Weber, Frank Mecka, Tobi, Manuel Fernandez,"

    old "ALL"
    new "ВСЕ"

    old "All characters depicted in this game are over the age of 18, maybe more."
    new "Все изображённые в игре персонажи старше 18 лет, возможно, намного."

    old "All right"
    new "Ладно"

    old "Allow [bree.name] to speak"
    new "Разрешить [bree.name] говорить"

    old "Allow Sasha to speak"
    new "Разрешить Саше говорить"

    old "Alright. I'll come over later today."
    new "Ладно. Я зайду сегодня позже"

    old "Am I being paid for this?"
    new "Мне за это заплатят?"

    old "An error has occurred:"
    new "Произошла ошибка:"

    old "An error is being simulated."
    new "Симулируется ошибка."

    old "An error occurred when trying to download game data:"
    new "При попытке загрузить данные игры произошла ошибка:"

    old "An exception has occurred."
    new "Произошло исключение."

    old "An HTTP error has occurred:"
    new "Произошла ошибка HTTP:"

    old "An unknown error occurred while connecting to the Ren'Py Sync server."
    new "При подключении к серверу Ren'Py Sync произошла неизвестная ошибка."

    old "Anal"
    new "Анал"

    old "Anal beads"
    new "Анальные шарики"

    old "And it didn't work"
    new "И это не сработало"

    old "Andrealphus"
    new "Andrealphus"

    old "Andrealphus, Lent1, Spirit Writer, BlissfulDarkness, Firesparq,"
    new "Andrealphus, Lent1, Spirit Writer, BlissfulDarkness, Firesparq,"

    old "AndrÃ© Nilsen, Valnik, NightFury95, Ruben, Cal,"
    new "AndrÃ© Nilsen, Valnik, NightFury95, Ruben, Cal,"

    old "Angel wings"
    new "Крылья ангела"

    old "AngstyExistence as Mike"
    new "AngstyExistence — Майк"

    old "Animals hate me"
    new "Животные меня ненавидят"

    old "ANIMATORS"
    new "АНИМАТОРЫ"

    old "Anime soundtracks"
    new "Саундтреки из аниме"

    old "AnimeIsMyWaifu, Rem Rem, Stéphane Pasquier, Ryan Samr,"
    new "AnimeIsMyWaifu, Rem Rem, Stéphane Pasquier, Ryan Samr,"

    old "Another time maybe, I don't feel like it"
    new "Может, в другой раз, сейчас не хочется"

    old "Answer jokingly"
    new "Ответить шуткой"

    old "Answer seriously"
    new "Ответить серьёзно"

    old "Anything for you, Sweetheart"
    new "Для тебя что угодно, милая"

    old "Anything you like"
    new "Что угодно"

    old "Anyway... follow her lead to please her"
    new "Всё равно... следовать её примеру, чтобы угодить ей"

    old "Apologise"
    new "Извиниться"

    old "Apologize"
    new "Извиниться"

    old "Apologize and ignore the cheating"
    new "Извиниться и проигнорировать измену"

    old "Apologize and ignore the flirting"
    new "Извиниться и проигнорировать флирт"

    old "Apologize for earlier"
    new "Извиниться за случившееся ранее"

    old "Applaud the topless sunbathers"
    new "Поддержать загорающих топлес"

    old "Apply sunscreen on all of them"
    new "Нанести солнцезащитный крем на всех"

    old "Apply sunscreen on Lexi"
    new "Нанести солнцезащитный крем на Лекси"

    old "Apply sunscreen on Minami"
    new "Нанести солнцезащитный крем на Минами"

    old "Apply sunscreen on Samantha"
    new "Нанести солнцезащитный крем на Саманту"

    old "Appointments"
    new "Встречи"

    old "Approach Aletta"
    new "Подойти к Алетте"

    old "Approach Audrey"
    new "Подойти к Одри"

    old "Approach Cassidy"
    new "Подойти к Кэссиди"

    old "Approach Cherie"
    new "Подойти к Шери"

    old "Approach her directly."
    new "Подойти к ней напрямую"

    old "Approach Lavish"
    new "Подойти к Лавиш"

    old "Approach Shiori"
    new "Подойти к Сиори"

    old "Archives"
    new "Архивы"

    old "Are you okay with this?"
    new "Тебя это устраивает?"

    old "Are you okay?"
    new "Ты в порядке?"

    old "Are you serious?"
    new "Ты серьёзно?"

    old "Are you sure you want to begin skipping?"
    new "Вы уверены, что хотите начать пропуск?"

    old "Are you sure you want to continue where you left off?"
    new "Вы уверены, что хотите продолжить с того места, на котором остановились?"

    old "Are you sure you want to delete this save?"
    new "Вы уверены, что хотите удалить это сохранение?"

    old "Are you sure you want to end the replay?"
    new "Вы уверены, что хотите завершить повтор?"

    old "Are you sure you want to overwrite your save?"
    new "Вы уверены, что хотите перезаписать ваше сохранение?"

    old "Are you sure you want to quit?"
    new "Вы уверены, что хотите выйти?"

    old "Are you sure you want to return to the main menu?\nThis will lose unsaved progress."
    new "Вы уверены, что хотите вернуться в главное меню?\nЭто приведёт к потере несохранённого прогресса."

    old "Are you sure you want to skip to the next choice?"
    new "Вы точно хотите пропустить всё до следующего выбора?"

    old "Are you sure you want to skip unseen dialogue to the next choice?"
    new "Вы уверены, что хотите пропустить непрочитанные диалоги до следующего выбора?"

    old "ARE YOU SURE?"
    new "ВЫ УВЕРЕНЫ?"

    old "Are you sure?"
    new "Вы уверены?"

    old "Arendall, Zula D. Varr, Russ, Dung O'Dea, Dylan Ahling,"
    new "Arendall, Zula D. Varr, Russ, Dung O'Dea, Dylan Ahling,"

    old "Argue"
    new "Спорить"

    old "Argue with the bouncer"
    new "Спорить с вышибалой"

    old "Armpits"
    new "Подмышки"

    old "ARROW KEYS"
    new "СТРЕЛКИ"

    old "Arrow Keys"
    new "Стрелки"

    old "As in this movie, \"The Mall Pig\""
    new "Как в фильме «Свинья из торгового центра»"

    old "As in this movie, \"Wetty Prouman\""
    new "Как в фильме «Ветти Прауман»"

    old "As you wish, but..."
    new "Как пожелаешь, но..."

    old "As you wish, my Princess!"
    new "Как пожелаешь, моя Принцесса!"

    old "Ask [bree.name] on a date"
    new "Пригласить [bree.name] на свидание"

    old "Ask [bree.name] to leave"
    new "Попросить [bree.name] уйти"

    old "Ask [date_girl.personal_pronoun] to suggest a dish"
    new "Попросить [date_girl.personal_pronoun] предложить блюдо"

    old "Ask about her food"
    new "Спросить о её еде"

    old "Ask about Ryan"
    new "Спросить о Райане"

    old "Ask about the coach being made to retire"
    new "Спросить, почему тренера заставили уйти на пенсию"

    old "Ask about the decoration"
    new "Спросить об украшениях"

    old "Ask about the food"
    new "Спросить о еде"

    old "Ask about their friendship"
    new "Спросить об их дружбе"

    old "Ask about university"
    new "Спросить об университете"

    old "Ask about work"
    new "Спросить о работе"

    old "Ask Alexis on a date"
    new "Пригласить Алексис на свидание"

    old "Ask Anna on a date"
    new "Пригласить Анну на свидание"

    old "Ask Anna's opinion"
    new "Спросить мнение Анны"

    old "Ask Audrey and Palla on a date"
    new "Пригласить Одри и Паллу на свидание"

    old "Ask Audrey and Sasha on a date"
    new "Пригласить Одри и Сашу на свидание"

    old "Ask Audrey on a date"
    new "Пригласить Одри на свидание"

    old "Ask Audrey, Cassidy and Palla on a date"
    new "Пригласить Одри, Кэссиди и Паллу на свидание"

    old "Ask Ayesha and Hanna on a date"
    new "Пригласить Айшу и Ханну на свидание"

    old "Ask Ayesha and Kylie on a date"
    new "Пригласить Айшу и Кайли на свидание"

    old "Ask Ayesha for a blowjob"
    new "Попросить Айшу сделать минет"

    old "Ask Ayesha on a date"
    new "Пригласить Айшу на свидание"

    old "Ask Camila on a date"
    new "Пригласить Камилу на свидание"

    old "Ask Cassidy on a date"
    new "Пригласить Кэссиди на свидание"

    old "Ask Cassidy, Audrey and Palla on a date"
    new "Пригласить Кэссиди, Одри и Паллу на свидание"

    old "Ask Emma and Samantha on a date"
    new "Пригласить Эмму и Саманту на свидание"

    old "Ask Emma on a date"
    new "Пригласить Эмму на свидание"

    old "Ask for a blowjob"
    new "Попросить минет"

    old "Ask for a doggy bag"
    new "Попросить упаковать еду с собой"

    old "Ask for a handjob"
    new "Попросить дрочку рукой"

    old "Ask for a promotion"
    new "Попросить повышение"

    old "Ask for a rimjob"
    new "Попросить римминг"

    old "Ask for a titjob"
    new "Попросить подрочить сиськами"

    old "Ask for money"
    new "Попросить денег"

    old "Ask for the window table"
    new "Попросить столик у окна"

    old "Ask Harmony on a date"
    new "Пригласить Хармони на свидание"

    old "Ask help from Lavish to light the fire"
    new "Попросить Лавиш помочь разжечь огонь"

    old "Ask her if she's gonna drink it at some point"
    new "Спросить, собирается ли она когда-нибудь это выпить"

    old "Ask her to help"
    new "Попросить её помочь"

    old "Ask her to take it out"
    new "Попросить её снять его"

    old "Ask her to wait"
    new "Попросить её подождать"

    old "Ask her what's wrong"
    new "Спросить, что случилось"

    old "Ask if she crashed the party"
    new "Спросить, пробралась ли она на вечеринку"

    old "Ask if she has an extra"
    new "Спросить, есть ли у неё лишняя"

    old "Ask if she's a new employee"
    new "Спросить, новая ли она сотрудница"

    old "Ask Kleio on a date"
    new "Пригласить Клео на свидание"

    old "Ask Kylie and Ayesha on a date"
    new "Пригласить Кайли и Айшу на свидание"

    old "Ask Kylie on a date"
    new "Пригласить Кайли на свидание"

    old "Ask Lexi on a date"
    new "Пригласить Лекси на свидание"

    old "Ask me out sometime"
    new "Как-нибудь пригласи меня на свидание"

    old "Ask Palla and Audrey on a date"
    new "Пригласить Паллу и Одри на свидание"

    old "Ask Palla on a date"
    new "Пригласить Паллу на свидание"

    old "Ask Palla, Cassidy and Audrey on a date"
    new "Пригласить Паллу, Кэссиди и Одри на свидание"

    old "Ask quietly for the waiter's attention"
    new "Тихо привлечь внимание официанта"

    old "Ask Ryan to help you next time."
    new "В следующий раз попроси Райана помочь"

    old "Ask Samantha and Emma on a date"
    new "Пригласить Саманту и Эмму на свидание"

    old "Ask Samantha on a date"
    new "Пригласить Саманту на свидание"

    old "Ask Sasha and Audrey on a date"
    new "Пригласить Сашу и Одри на свидание"

    old "Ask Sasha on a date"
    new "Пригласить Сашу на свидание"

    old "Ask Shiori to dance"
    new "Пригласить Сиори на танец"

    old "Ask to share [bree.name]'s bedroll"
    new "Попроситься разделить спальник [bree.name]"

    old "Ask to share Minami's bedroll"
    new "Попроситься разделить спальник Минами"

    old "Ask to share Sasha's bedroll"
    new "Попроситься разделить спальник Саши"

    old "Asshole..."
    new "Мудак..."

    old "at "
    new "в"

    old "At home:"
    new "Дома:"

    old "At the stripclub:"
    new "В стрип-клубе:"

    old "At work:"
    new "На работе:"

    old "Attack him"
    new "Напасть на него"

    old "Attempts a roll back to a prior time, allowing you to save or choose a different choice."
    new "Пытается вернуться к предыдущему моменту, чтобы вы могли сохранить игру или выбрать другой вариант."

    old "Attributes:"
    new "Аттрибуты:"

    old "Audio Filename:"
    new "Имя файла:"

    old "audio when minimized"
    new "звук при сворачивании окна"

    old "audio when unfocused"
    new "звук при потере фокуса"

    old "Audrey"
    new "Audrey"

    old "Audrey should not wear her sexy uniform anymore"
    new "Одри больше не должна носить сексуальную униформу"

    old "Audrey should put her bottom back on"
    new "Одри должна снова надевать низ"

    old "Audrey should put her top back"
    new "Одри должна снова надевать верх"

    old "Audrey should put her uniform back"
    new "Одри должна снова надевать униформу"

    old "Audrey should remove her bottoms at work"
    new "Одри должна снимать низ на работе"

    old "Audrey should remove her top at work"
    new "Одри должна снимать верх на работе"

    old "Audrey should remove her uniform at work"
    new "Одри должна снимать униформу на работе"

    old "Audrey should wear her sexy uniform"
    new "Одри должна носить свою сексуальную униформу"

    old "Auhiie, Alexa, Fabien L'hermitte, Peaches652, Ultra Violet,"
    new "Auhiie, Alexa, Fabien L'hermitte, Peaches652, Ultra Violet,"

    old "authentication_provider: [persistent.authentication_provider]"
    new "поставщик аутентификации: [persistent.authentication_provider]"

    old "authentication_token:"
    new "токен аутентификации:"

    old "authentication_token: [persistent.authentication_token]"
    new "токен аутентификации: [persistent.authentication_token]"

    old "Authorization summary"
    new "Сводка авторизации"

    old "Auto"
    new "Авто"

    old "Auto forward"
    new "Авточтение"

    old "auto voice: [_voice.auto_file!sq]"
    new "автоматическая озвучка: [_voice.auto_file!sq]"

    old "auto-forward"
    new "авточтение"

    old "auto-forward after click"
    new "продолжать авточтение после клика"

    old "auto-forward time"
    new "скорость авточтения"

    old "automatic move"
    new "автоматически передвигать мышь к кнопке"

    old "Automatic saves"
    new "Автосохранения"

    old "Automatically Choose"
    new "Выбрать автоматически"

    old "Aw, why not?"
    new "Ой, почему нет?"

    old "Axium, Thormakar, Tomcat2k, CouncilOfOne, Zach Johnson,"
    new "Axium, Thormakar, Tomcat2k, CouncilOfOne, Zach Johnson,"

    old "Ayesha fucks Kylie's ass"
    new "Айша трахает Кайли в задницу"

    old "Ayesha fucks Kylie's pussy"
    new "Айша трахает киску Кайли"

    old "Ayesha is a personal trainer"
    new "Айша — персональный тренер"

    old "Ayesha is a professional wrestler"
    new "Айша — профессиональная рестлерша"

    old "Ayesha needs to cool down"
    new "Айше нужно остыть"

    old "Ayesha pulls out"
    new "Айша вытаскивает"

    old "Ayesha stays inside"
    new "Айша остаётся внутри"

    old "Ayesha! Shut up!"
    new "Айша! Заткнись!"

    old "Ayesha, I'm disappointed"
    new "Айша, я разочарован"

    old "Ayesha, it's just a joke"
    new "Айша, это просто шутка"

    old "B"
    new "B"

    old "b"
    new "b"

    old "Back"
    new "Назад"

    old "BACK"
    new "НАЗАД"

    old "Back (B)"
    new "Назад (B)"

    old "Back away"
    new "Отойти"

    old "Back down"
    new "Отступить"

    old "Back Off"
    new "Отступить"

    old "Back off"
    new "Отступить"

    old "Back off (Never meet Amy again)"
    new "Отступить (больше никогда не встречаться с Эми)"

    old "Back up [bree.name]"
    new "Поддержать [bree.name]"

    old "Back up Jack"
    new "Поддержать Джека"

    old "Back up Kylie"
    new "Поддержать Кайли"

    old "Background"
    new "Фон"

    old "BACKGROUND ARTISTS"
    new "ХУДОЖНИКИ ФОНОВ"

    old "Bad idea"
    new "Плохая идея"

    old "Bail Kleio out"
    new "Внести залог за Клео"

    old "Bake Something"
    new "Что-нибудь испечь"

    old "bar"
    new ". Полоса настройки"

    old "Barge into the room"
    new "Ворваться в комнату"

    old "Be amused"
    new "Развеселиться"

    old "Be angry"
    new "Разозлиться"

    old "Be as vague as possible"
    new "Говорить как можно неопределённее"

    old "Be awkward"
    new "Повести себя неловко"

    old "Be bad"
    new "Повести себя плохо"

    old "Be cautious"
    new "Действовать осторожно"

    old "Be cool"
    new "Вести себя спокойно"

    old "Be disapproving"
    new "Выразить неодобрение"

    old "Be disgusted"
    new "Выразить отвращение"

    old "Be falsely enthusiastic"
    new "Изобразить энтузиазм"

    old "Be flattered"
    new "Польститься"

    old "Be gentle"
    new "Действовать нежно"

    old "Be good"
    new "Повести себя хорошо"

    old "Be honest with her"
    new "Быть с ней честным"

    old "Be honest; we can do better."
    new "Сказать честно: мы можем лучше"

    old "Be interested"
    new "Заинтересоваться"

    old "Be Intrigued"
    new "Заинтересоваться"

    old "Be jealous"
    new "Ревновать"

    old "Be mean"
    new "Повести себя грубо"

    old "Be more feminine"
    new "Стать женственнее"

    old "Be more innocent"
    new "Стать невиннее"

    old "Be more masculine"
    new "Стать мужественнее"

    old "Be more stable"
    new "Стать стабильнее"

    old "Be more unstable"
    new "Стать нестабильнее"

    old "Be negative"
    new "Отнестись отрицательно"

    old "Be nice"
    new "Повести себя мило"

    old "Be nice, take the bill"
    new "Повести себя мило и оплатить счёт"

    old "Be nicer"
    new "Повести себя добрее"

    old "Be offended"
    new "Оскорбиться"

    old "Be passive"
    new "Вести себя пассивно"

    old "Be patient"
    new "Будь терпеливой"

    old "Be positive"
    new "Отнестись положительно"

    old "Be rough with her"
    new "Действовать грубо"

    old "Be sluttier"
    new "Стать распутнее"

    old "Be sophisticated"
    new "Повести себя утончённо"

    old "Be supportive"
    new "Поддержать"

    old "Be surprised"
    new "Удивиться"

    old "Be transparent"
    new "Сказать прямо"

    old "Bea Draven"
    new "Bea Draven"

    old "Bear with it"
    new "Потерпеть"

    old "Beat the waiter"
    new "Избить официанта"

    old "Because you're being a bitch tonight"
    new "Потому что сегодня ты ведёшь себя как сучка"

    old "Beg her to abort"
    new "Умолять её сделать аборт"

    old "Beg she stay"
    new "Умолять её остаться"

    old "begin skipping"
    new "начать пропуск"

    old "behind "
    new "позади"

    old "Behind:"
    new "Позади:"

    old "Believe her"
    new "Поверить ей"

    old "Bench"
    new "Скамейка"

    old "Better find another place"
    new "Лучше найди другое место"

    old "Better not interfere"
    new "Лучше не вмешиваться"

    old "BFF!"
    new "Лучшие друзья!"

    old "Birthday"
    new "День рождения"

    old "Birthday:"
    new "День рождения:"

    old "Bitch"
    new "Сучка"

    old "Black"
    new "Чёрный"

    old "Blackmail Dwayne"
    new "Шантажировать Дуэйна"

    old "Blackspack, Evan Laforet, Hunter ingram, Phillip Razlow,"
    new "Blackspack, Evan Laforet, Hunter ingram, Phillip Razlow,"

    old "Blame Ayesha"
    new "Обвинить Айшу"

    old "Blame Kylie"
    new "Обвинить Кайли"

    old "Blame the long narrative from the game you were playing"
    new "Сослаться на длинный сюжет игры, в которую ты играл"

    old "Blaze Foley, AzazelTheCursed, apoctriforce, mc 14028,"
    new "Blaze Foley, AzazelTheCursed, apoctriforce, mc 14028,"

    old "Blindfold"
    new "Повязка на глаза"

    old "Blow her off"
    new "Отшить её"

    old "Blow it off"
    new "Не придавать значения"

    old "Blow the other girl off"
    new "Отшить другую девушку"

    old "Blowjob"
    new "Минет"

    old "Bob Jones, Schumacher0318, Scomf13, Greg Bloomberg,"
    new "Bob Jones, Schumacher0318, Scomf13, Greg Bloomberg,"

    old "Booty call"
    new "Вызов для секса"

    old "Both"
    new "И то и другое"

    old "Both in my arms, you on your knees"
    new "Обе в моих объятиях, а ты на коленях"

    old "BoubreRig"
    new "BoubreRig"

    old "Boyfriend/girlfriend"
    new "Парень и девушка"

    old "Boyfriend/girlfriend instead?"
    new "Может, лучше парень и девушка?"

    old "bradley, Reo44, itslydiabxtch, James Rabbit, Beau FastrÃ©,"
    new "bradley, Reo44, itslydiabxtch, James Rabbit, Beau FastrÃ©,"

    old "Bribe the bouncer"
    new "Подкупить вышибалу"

    old "Bribe the bouncer to get into the VIP section"
    new "Подкупить вышибалу, чтобы попасть в VIP-зону"

    old "Bring her to her knees"
    new "Поставить её на колени"

    old "Bron-vito, Mr.dragon, Astre, DMan4g00d, Losstinhere,"
    new "Bron-vito, Mr.dragon, Astre, DMan4g00d, Losstinhere,"

    old "Bruce (Bree's dad)"
    new "Брюс (отец Бри)"

    old "Bruce seems fine"
    new "Брюс вроде нормальный"

    old "Brush against her arm"
    new "Случайно коснуться её руки"

    old "Burgers"
    new "Бургеры"

    old "But Aletta is special"
    new "Но Алетта особенная"

    old "But you stayed!"
    new "Но ты осталась!"

    old "Butt plug"
    new "Анальная пробка"

    old "Buy everything she wants"
    new "Купить всё, что она захочет"

    old "Buy her plushies"
    new "Купить ей плюшевые игрушки"

    old "Buy it alone"
    new "Купить самостоятельно"

    old "Buy Morgan a bunch of flowers"
    new "Купить Морган букет цветов"

    old "Buy Morgan a cookie"
    new "Купить Морган печенье"

    old "Buy Sasha a drink"
    new "Купить Саше выпивку"

    old "Buy yourself something and not Shiori"
    new "Купить что-нибудь себе, но не Сиори"

    old "C"
    new "C"

    old "c"
    new "c"

    old "Cain"
    new "Cain"

    old "calendar"
    new "календарь"

    old "Calibrate"
    new "Калибровать"

    old "Calibrating [name] ([i]/[total])"
    new "Калибровка [name] ([i]/[total])"

    old "call"
    new "звонок"

    old "Call"
    new "Позвонить"

    old "Call a cab"
    new "Вызвать такси"

    old "Call Audrey only"
    new "Позвонить только Одри"

    old "Call Camila"
    new "Позвонить Камиле"

    old "Call for the manager"
    new "Позвать менеджера"

    old "Call her dirty"
    new "Назвать её грязной"

    old "Call her out"
    new "Высказать ей всё"

    old "Call it a night"
    new "Закончить вечер"

    old "Call Lavish and Shiori"
    new "Позвонить Лавиш и Сиори"

    old "Call Lavish only"
    new "Позвонить только Лавиш"

    old "Call me [[hero.name]"
    new "Называй меня [[hero.name]"

    old "Call me [hero.name]"
    new "Называй меня [hero.name]"

    old "Call me [heroname]"
    new "Называй меня [heroname]"

    old "Call me Baby"
    new "Называй меня Малышом"

    old "Call me Boi"
    new "Называй меня Боем"

    old "Call me Boo"
    new "Называй меня Любимым"

    old "Call me Boss"
    new "Называй меня Боссом"

    old "Call me Boss Buck"
    new "Называй меня Большим боссом"

    old "Call me Boy"
    new "Называй меня Мальчиком"

    old "Call me Boytoy"
    new "Называй меня Игрушкой"

    old "Call me Brah"
    new "Называй меня Бро"

    old "Call me Bro"
    new "Называй меня Бро"

    old "Call me Bro-bro"
    new "Называй меня Братишкой"

    old "Call me Chad"
    new "Называй меня Чадом"

    old "Call me Champ"
    new "Называй меня Чемпионом"

    old "Call me Chief"
    new "Называй меня Шефом"

    old "Call me Coach"
    new "Называй меня Тренером"

    old "Call me Cow-boy"
    new "Называй меня Ковбоем"

    old "Call me Cuck"
    new "Называй меня Куколдом"

    old "Call me Cutie"
    new "Называй меня Милашкой"

    old "Call me Daddy"
    new "Называй меня Папочкой"

    old "Call me Dark knight"
    new "Называй меня Тёмным рыцарем"

    old "Call me Dearest"
    new "Называй меня Дорогим"

    old "Call me Demon"
    new "Называй меня Демоном"

    old "Call me Dick"
    new "Называй меня Членом"

    old "Call me Dreamboat"
    new "Называй меня Красавчиком"

    old "Call me Dude"
    new "Называй меня Чуваком"

    old "Call me Dumbass"
    new "Называй меня Дебилом"

    old "Call me Fuck Face"
    new "Называй меня Ебальником"

    old "Call me Fuckface"
    new "Называй меня Ебальником"

    old "Call me Guapo"
    new "Называй меня Гуапо"

    old "Call me Hanata"
    new "Называй меня Ханатой"

    old "Call me Handsome"
    new "Называй меня Красавчиком"

    old "Call me Hermoso"
    new "Называй меня Эрмосо"

    old "Call me Hero"
    new "Называй меня Героем"

    old "Call me Honey"
    new "Называй меня Милым"

    old "Call me Hotshot"
    new "Называй меня Крутышом"

    old "Call me Husband"
    new "Называй меня Мужем"

    old "Call me Idiot"
    new "Называй меня Идиотом"

    old "Call me Koibito"
    new "Называй меня Койбито"

    old "Call me Little man"
    new "Называй меня Малышом"

    old "Call me Little one"
    new "Называй меня Малышом"

    old "Call me Lord"
    new "Называй меня Лордом"

    old "Call me Love"
    new "Называй меня Любимым"

    old "Call me Master"
    new "Называй меня Господином"

    old "Call me Mr.Boss sir"
    new "Называй меня Господином Боссом"

    old "Call me Muffin"
    new "Называй меня Кексиком"

    old "Call me My angel"
    new "Называй меня Моим ангелом"

    old "Call me My ball and chain"
    new "Называй меня Обузой"

    old "Call me My Big Bear"
    new "Называй меня Моим большим медведем"

    old "Call me My friend"
    new "Называй меня Другом"

    old "Call me My Heart"
    new "Называй меня Моим сердцем"

    old "Call me My King"
    new "Называй меня Моим королём"

    old "Call me My One and Only"
    new "Называй меня Единственным"

    old "Call me My Prince"
    new "Называй меня Моим принцем"

    old "Call me My rock"
    new "Называй меня Моей опорой"

    old "Call me Naughty boy"
    new "Называй меня Плохим мальчиком"

    old "Call me Nii-san"
    new "Называй меня Нии-саном"

    old "Call me Onii-chan"
    new "Называй меня Они-тяном"

    old "Call me Owner"
    new "Называй меня Хозяином"

    old "Call me Papi"
    new "Называй меня Папи"

    old "Call me Papi Chulo"
    new "Называй меня Папи Чуло"

    old "Call me Partner"
    new "Называй меня Партнёром"

    old "Call me Peasant"
    new "Называй меня Крестьянином"

    old "Call me Perv"
    new "Называй меня Извращенцем"

    old "Call me Playboy"
    new "Называй меня Плейбоем"

    old "Call me Player One"
    new "Называй меня Первым игроком"

    old "Call me Roomie"
    new "Называй меня Соседом"

    old "Call me Senpai"
    new "Называй меня Сэмпаем"

    old "Call me Servant"
    new "Называй меня Слугой"

    old "Call me Smooth rider"
    new "Называй меня Ловким наездником"

    old "Call me Stallion"
    new "Называй меня Жеребцом"

    old "Call me Stud"
    new "Называй меня Жеребцом"

    old "Call me Studmuffin"
    new "Называй меня Жеребчиком"

    old "Call me Sugar"
    new "Называй меня Сладким"

    old "Call me Superstar"
    new "Называй меня Суперзвездой"

    old "Call me Sweetheart"
    new "Называй меня Любимым"

    old "Call me Sweetie"
    new "Называй меня Милым"

    old "Call me Twink"
    new "Называй меня Твинком"

    old "Call me Wallet"
    new "Называй меня Кошельком"

    old "Call me Young man"
    new "Называй меня Молодым человеком"

    old "Call Shiori only"
    new "Позвонить только Сиори"

    old "Calling"
    new "Вызов"

    old "Calm Morgan down"
    new "Успокоить Морган"

    old "Camila will pay"
    new "Заплатит Камила"

    old "Camila, will you finish your plate?"
    new "Камила, ты доешь свою порцию?"

    old "Can I join you?"
    new "Можно к вам?"

    old "Cancel"
    new "Отмена"

    old "Caress her belly"
    new "Погладить её живот"

    old "Carry on regardless"
    new "Всё равно продолжить"

    old "Cars"
    new "Машины"

    old "Cassidy"
    new "Cassidy"

    old "Cassidy should put her bottom back on"
    new "Кэссиди должна снова надеть низ"

    old "Cassidy should put her outfit back"
    new "Кэссиди должна снова надеть наряд"

    old "Cassidy should put her top back"
    new "Кэссиди должна снова надеть верх"

    old "Cassidy should remove her bottoms"
    new "Кэссиди должна снять низ"

    old "Cassidy should remove her outfit"
    new "Кэссиди должна снять наряд"

    old "Cassidy should remove her top"
    new "Кэссиди должна снять верх"

    old "Casual"
    new "Повседневный"

    old "Casual outfit"
    new "Повседневный наряд"

    old "Casual uniform"
    new "Повседневная униформа"

    old "Celebrate"
    new "Отпраздновать"

    old "Change"
    new "Изменить"

    old "Change jobs"
    new "Сменить работу"

    old "Change render options"
    new "Изменить параметры рендеринга"

    old "Change subject"
    new "Сменить тему"

    old "Change the subject."
    new "Сменить тему"

    old "Change your mind"
    new "Передумать"

    old "CHANGELOG"
    new "ИСТОРИЯ ИЗМЕНЕНИЙ"

    old "Changes will take effect the next time this program is run."
    new "Изменения вступят в силу при следующем запуске программы."

    old "Channel:"
    new "Каналы:"

    old "character"
    new "персонаж"

    old "CHARACTER ARTISTS"
    new "ХУДОЖНИКИ ПЕРСОНАЖЕЙ"

    old "CharDucks, darkabyss987, Chad Dreaney, Benjamin Loke,"
    new "CharDucks, darkabyss987, Chad Dreaney, Benjamin Loke,"

    old "Chastise her"
    new "Отчитать её"

    old "Chastise Lexi"
    new "Отчитать Лекси"

    old "Chat with Aletta"
    new "Поговорить с Алеттой"

    old "Chat with Audrey"
    new "Поговорить с Одри"

    old "Chat with Lavish"
    new "Поговорить с Лавиш"

    old "Chat with Shiori"
    new "Поговорить с Сиори"

    old "Cheat"
    new "Читы"

    old "cheat is off"
    new "читы выключены"

    old "cheat is on"
    new "читы включены"

    old "CHEATS"
    new "ЧИТЫ"

    old "Check what's going on"
    new "Проверить, что происходит"

    old "Checking for updates."
    new "Проверка обновлений."

    old "Cherrywood"
    new "Cherrywood"

    old "CHIBI ARTIST"
    new "ХУДОЖНИК ЧИБИ"

    old "Choke her"
    new "Душить её"

    old "Choose [bree.name]"
    new "Выбрать [bree.name]"

    old "Choose [bree.name]'s sandwich"
    new "Выбрать сэндвич [bree.name]"

    old "Choose a different spot"
    new "Выбрать другое место"

    old "Choose a talk subject"
    new "Выбрать тему разговора"

    old "Choose Kleio"
    new "Выбрать Клео"

    old "Choose Lexi"
    new "Выбрать Лекси"

    old "Choose Minami"
    new "Выбрать Минами"

    old "Choose Morgan"
    new "Выбрать Морган"

    old "Choose Sam"
    new "Выбрать Сэм"

    old "Choose Samantha"
    new "Выбрать Саманту"

    old "Choose Sasha"
    new "Выбрать Сашу"

    old "Choose Sasha's wrap"
    new "Выбрать ролл Саши"

    old "Choose Sirens and Serenity"
    new "Выбрать «Сирены и безмятежность»"

    old "Choose Space Wars"
    new "Выбрать «Космические войны»"

    old "Choose the band"
    new "Выбрать группу"

    old "Choose the first one"
    new "Выбрать первый вариант"

    old "Choose the second one"
    new "Выбрать второй вариант"

    old "Choose the shade"
    new "Выбрать тень"

    old "Choose the sun"
    new "Выбрать солнце"

    old "Choose to fuck in Palla's room"
    new "Выбрать секс в комнате Паллы"

    old "Choose to fuck in Shawn's room"
    new "Выбрать секс в комнате Шона"

    old "Choose to fuck on the balcony"
    new "Выбрать секс на балконе"

    old "Choose to help [bree.name]"
    new "Выбрать помощь [bree.name]"

    old "Choose to help Sasha"
    new "Выбрать помощь Саше"

    old "CHOOSE YOUR BIRTHDAY"
    new "ВЫБЕРИТЕ ДЕНЬ РОЖДЕНИЯ"

    old "CHOOSE YOUR NAME"
    new "ВЫБЕРИТЕ ИМЯ"

    old "CHOOSE YOUR STARTING DAY"
    new "ВЫБЕРИТЕ НАЧАЛЬНЫЙ ДЕНЬ"

    old "Christian, melodygreek, Justin Hood, NullVoided, Brian Embry,"
    new "Christian, melodygreek, Justin Hood, NullVoided, Brian Embry,"

    old "Cinnamon Rolls"
    new "Булочки с корицей"

    old "Claim to have no money"
    new "Сказать, что денег нет"

    old "Claim to need the bathroom"
    new "Сказать, что нужно в туалет"

    old "Claim you used to be a sporting prodigy"
    new "Заявить, что раньше был спортивным вундеркиндом"

    old "Clean the pool"
    new "Почисти бассейн"

    old "Clean this room"
    new "Убери эту комнату"

    old "Clear achievements"
    new "Сбросить достижения"

    old "Clear stats"
    new "Сбросить характеристики"

    old "Click to continue"
    new "Нажмите, чтобы продолжить"

    old "Click to play the video."
    new "Кликните, чтобы воспроизвести видео."

    old "Click to set transform, right click to add to transform list."
    new "Щёлкните, чтобы установить трансформацию. Щёлкните правой кнопкой, чтобы добавить в список трансформаций."

    old "Click to set, right click to add to behind list."
    new "Щёлкните, чтобы установить. Щёлкните правой кнопкой, чтобы добавить в список позади."

    old "Click to set."
    new "Нажмите, чтобы установить."

    old "Click to toggle attribute, right click to toggle negative attribute."
    new "Щёлкните, чтобы переключить атрибут. Щёлкните правой кнопкой, чтобы переключить отрицательный атрибут."

    old "Clipboard"
    new "Из буфера обмена"

    old "clipboard voicing"
    new "синтез речи из буфера обмена"

    old "clipboard voicing disable"
    new "отключить озвучивание буфера обмена"

    old "clipboard voicing enable"
    new "включить озвучивание буфера обмена"

    old "Clipboard voicing enabled. "
    new "Озвучка буфера обмена включена."

    old "Clipboard voicing enabled. Press 'shift+C' to disable."
    new "Озвучка буфера обмена включена. Нажмите 'shift+C', чтобы отключить её."

    old "Close"
    new "Закрыть"

    old "Clothed"
    new "В одежде"

    old "Clothes policy"
    new "Правила одежды"

    old "Clothes:"
    new "Одежда:"

    old "Cobblestone"
    new "Брусчатка"

    old "Cocoa"
    new "Какао"

    old "Coffee"
    new "Кофе"

    old "colison, BrotherDom, Kyle, Louka, slimsam9999, Tomb,"
    new "colison, BrotherDom, Kyle, Louka, slimsam9999, Tomb,"

    old "Collar"
    new "Ошейник"

    old "Come here."
    new "Иди сюда"

    old "Comfort her"
    new "Утешить её"

    old "Comfy sits are better"
    new "Удобные сиденья лучше"

    old "Comics"
    new "Комиксы"

    old "Compensate"
    new "Компенсировать"

    old "Complain"
    new "Пожаловаться"

    old "Complain about the kids"
    new "Пожаловаться на детей"

    old "Complain about the music"
    new "Пожаловаться на музыку"

    old "Complain that the soup is cold"
    new "Пожаловаться, что суп холодный"

    old "Completed"
    new "Завершённые"

    old "Compliment"
    new "Сделать комплимент"

    old "Compliment her"
    new "Сделать ей комплимент"

    old "Compliment her beauty"
    new "Сделать комплимент её красоте"

    old "Compliment her looks"
    new "Сделать комплимент её внешности"

    old "Compliment her muscles"
    new "Сделать комплимент её мышцам"

    old "Compliment her outfit"
    new "Сделать комплимент её наряду"

    old "Compliment her work"
    new "Похвалить её работу"

    old "Compliment him"
    new "Сделать ему комплимент"

    old "Compliment Minami"
    new "Сделать Минами комплимент"

    old "Compliment the girls"
    new "Сделать девушкам комплимент"

    old "Computer"
    new "Компьютер"

    old "Confront Dwayne"
    new "Противостоять Дуэйну"

    old "Confront her"
    new "Противостоять ей"

    old "Consider it"
    new "Подумать об этом"

    old "Console"
    new "Консоль"

    old "Contacting App Store\nPlease Wait..."
    new "Связываюсь с App Store\nПожалуйста, подождите..."

    old "contacts"
    new "контакты"

    old "Contacts"
    new "Контакты"

    old "Continue"
    new "Продолжить"

    old "CONTINUE"
    new "ПРОДОЛЖИТЬ"

    old "Continue her training"
    new "Продолжить её тренировки"

    old "Continue the visit"
    new "Продолжить визит"

    old "Continue, Don't show warning again"
    new "Продолжить и больше не показывать предупреждение"

    old "Continue, Show this warning again"
    new "Продолжить и показать это предупреждение снова"

    old "Continues spanking Audrey"
    new "Продолжить шлёпать Одри"

    old "CONTROLS"
    new "УПРАВЛЕНИЕ"

    old "controls"
    new "управление"

    old "Cook something"
    new "Что-нибудь приготовить"

    old "Cooking"
    new "Кулинария"

    old "Copies the traceback.txt file to the clipboard as BBcode for forums like https://lemmasoft.renai.us/."
    new "Копирует содержимое файла traceback.txt в буфер обмена в формате BBCode для форумов, например https://lemmasoft.renai.us/."

    old "Copies the traceback.txt file to the clipboard as Markdown for Discord."
    new "Копирует содержимое файла traceback.txt в буфер обмена в формате Markdown для Discord."

    old "Copy BBCode"
    new "Копировать BBCode"

    old "Copy Markdown"
    new "Копировать Markdown"

    old "Correct Camila"
    new "Поправить Камилу"

    old "Correct Camila and Lexi"
    new "Поправить Камилу и Лекси"

    old "Correct Lexi"
    new "Поправить Лекси"

    old "Could not connect to the Ren'Py Sync server."
    new "Не удалось подключиться к серверу Ren'Py Sync."

    old "Could not download file list: "
    new "Не удалось загрузить список файлов:"

    old "Could not verify update signature."
    new "Не могу верифицировать подпись обновления."

    old "Cowgirl"
    new "Наездница"

    old "Create a personal moment"
    new "Создать личный момент"

    old "Create a romantic moment"
    new "Создать романтический момент"

    old "Criticise"
    new "Раскритиковать"

    old "Criticize"
    new "Раскритиковать"

    old "Criticize him"
    new "Раскритиковать его"

    old "CTRL"
    new "CTRL"

    old "Ctrl"
    new "Ctrl"

    old "Cum in [bree.name]'s ass"
    new "Кончить в задницу [bree.name]"

    old "Cum in [bree.name]'s mouth"
    new "Кончить в рот [bree.name]"

    old "Cum in [bree.name]'s pussy"
    new "Кончить в киску [bree.name]"

    old "Cum in Anna's ass"
    new "Кончить Анне в задницу"

    old "Cum in Anna's mouth"
    new "Кончить Анне в рот"

    old "Cum in Anna's pussy"
    new "Кончить Анне в киску"

    old "Cum in ass"
    new "Кончить в задницу"

    old "Cum in Audrey's mouth"
    new "Кончить Одри в рот"

    old "Cum in Ayesha's mouth"
    new "Кончить Айше в рот"

    old "Cum in Camila's mouth"
    new "Кончить Камиле в рот"

    old "Cum in Cassidy's mouth"
    new "Кончить Кэссиди в рот"

    old "Cum in Hanna's mouth"
    new "Кончить Ханне в рот"

    old "Cum in her ass"
    new "Кончить ей в задницу"

    old "Cum in her mouth"
    new "Кончить ей в рот"

    old "Cum in her mouth."
    new "Кончить ей в рот"

    old "Cum in Kleio's ass"
    new "Кончить Клео в задницу"

    old "Cum in Kleio's pussy"
    new "Кончить Клео в киску"

    old "Cum in Lexi's mouth"
    new "Кончить Лекси в рот"

    old "Cum in Minami's ass"
    new "Кончить в задницу Минами"

    old "Cum in Minami's pussy"
    new "Кончить в киску Минами"

    old "Cum in Palla's mouth"
    new "Кончить Палле в рот"

    old "Cum in pussy"
    new "Кончить в киску"

    old "Cum in Samantha's mouth"
    new "Кончить в рот Саманты"

    old "Cum in Sasha's ass"
    new "Кончить в задницу Саши"

    old "Cum in Sasha's mouth"
    new "Кончить в рот Саши"

    old "Cum in Sasha's pussy"
    new "Кончить в киску Саши"

    old "Cum inside"
    new "Кончить внутрь"

    old "Cum inside Anna's mouth"
    new "Кончить Анне в рот"

    old "Cum inside ass"
    new "Кончить в задницу"

    old "Cum inside Audrey's ass"
    new "Кончить внутрь задницы Одри"

    old "Cum inside Audrey's pussy"
    new "Кончить внутрь киски Одри"

    old "Cum inside her"
    new "Кончить внутрь неё"

    old "Cum inside Kleio's pussy"
    new "Кончить внутрь киски Клео"

    old "Cum inside Minami"
    new "Кончить внутрь Минами"

    old "Cum inside of Sasha's ass"
    new "Кончить внутрь задницы Саши"

    old "Cum inside of Sasha's pussy"
    new "Кончить внутрь киски Саши"

    old "Cum on [bree.name]'s ass"
    new "Кончить на задницу [bree.name]"

    old "Cum on Aletta"
    new "Кончить на Алетту"

    old "Cum on Anna's face"
    new "Кончить Анне на лицо"

    old "Cum on Audrey"
    new "Кончить на Одри"

    old "Cum on Audrey's face"
    new "Кончить Одри на лицо"

    old "Cum on both girls"
    new "Кончить на обеих девушек"

    old "Cum on Cassidy's face"
    new "Кончить Кэссиди на лицо"

    old "Cum on Harmony"
    new "Кончить на Хармони"

    old "Cum on her back"
    new "Кончить ей на спину"

    old "Cum on her breasts"
    new "Кончить ей на грудь"

    old "Cum on her face"
    new "Кончить ей на лицо"

    old "Cum on her face."
    new "Кончить ей на лицо"

    old "Cum on her tits"
    new "Кончить ей на сиськи"

    old "Cum on Lavish"
    new "Кончить на Лавиш"

    old "Cum on Lexi"
    new "Кончить на Лекси"

    old "Cum on Palla's face"
    new "Кончить Палле на лицо"

    old "Cum on Sasha's ass"
    new "Кончить на задницу Саши"

    old "Cum on Sasha's face"
    new "Кончить Саше на лицо"

    old "Cum on Shiori"
    new "Кончить на Сиори"

    old "Cum on their face"
    new "Кончить им на лицо"

    old "Cum on their faces"
    new "Кончить им на лица"

    old "Cum outside"
    new "Кончить снаружи"

    old "Cum over Lexi and Sasha's faces"
    new "Кончить на лица Лекси и Саши"

    old "Cum over Sasha and Audrey"
    new "Кончить на Сашу и Одри"

    old "Cunnilingus"
    new "Кунилингус"

    old "Customize director.audio_channels to add more channels."
    new "Измените director.audio_channels, чтобы добавить больше каналов."

    old "Customize director.transforms to add more transforms."
    new "Измените director.transforms, чтобы добавить больше трансформаций."

    old "Customize director.transitions to add more transitions."
    new "Измените director.transitions, чтобы добавить больше переходов."

    old "Cute"
    new "Мило"

    old "D"
    new "D"

    old "d"
    new "d"

    old "D-Pad, Sticks"
    new "Крестовина, стики"

    old "Dad"
    new "Папа"

    old "Dallas Runchel, huunam Lee, Kevin Tra, Nathaniel Thomas,"
    new "Dallas Runchel, huunam Lee, Kevin Tra, Nathaniel Thomas,"

    old "Damn that's hot"
    new "Чёрт, это горячо"

    old "Dance"
    new "Танцевать"

    old "Dance to the song"
    new "Танцевать под песню"

    old "Dance with [bree.name]"
    new "Танцевать с [bree.name]"

    old "Dance with Aletta"
    new "Танцевать с Алеттой"

    old "Dance with Audrey"
    new "Танцевать с Одри"

    old "Dance with Ayesha"
    new "Танцевать с Айшей"

    old "Dance with Cherie"
    new "Танцевать с Шери"

    old "Dance with Kylie"
    new "Танцевать с Кайли"

    old "Dance with Lavish"
    new "Танцевать с Лавиш"

    old "Dance with Lexi"
    new "Танцевать с Лекси"

    old "Dance with Minami"
    new "Танцевать с Минами"

    old "Dance with Samantha"
    new "Танцевать с Самантой"

    old "Dance with Sasha"
    new "Танцевать с Сашей"

    old "Dance with Shiori"
    new "Танцевать с Сиори"

    old "Dancing"
    new "Танцы"

    old "Daring swimsuit"
    new "Смелый купальник"

    old "Dark-Oshigan, Senturi and HXL"
    new "Dark-Oshigan, Senturi and HXL"

    old "Darren Curtis"
    new "Darren Curtis"

    old "Date"
    new "Для свидания"

    old "Date outfit"
    new "Наряд для свидания"

    old "David Aguiari, Soul, Smitty, Goeuriot, Merc#2077,"
    new "David Aguiari, Soul, Smitty, Goeuriot, Merc#2077,"

    old "David Washington, Dready, King leoric, Lucas, jason rodger,"
    new "David Washington, Dready, King leoric, Lucas, jason rodger,"

    old "deactivate"
    new "элемент деактивирован"

    old "Deal with her later"
    new "Разобраться с ней позже"

    old "Deal with it"
    new "Смириться"

    old "Debug"
    new "Отладка"

    old "debug voicing"
    new "режим дебага синтеза речи"

    old "debug voicing disable"
    new "отключить дебаг озвучивания"

    old "debug voicing enable"
    new "включить дебаг озвучивания"

    old "Decline"
    new "Отклонить"

    old "Decline invitation"
    new "Отклонить приглашение"

    old "decrease"
    new "меньше"

    old "Decrease girl attraction"
    new "Снизить влечение к девушкам"

    old "Default"
    new "По умолчанию"

    old "Defend [bree.name]"
    new "Защитить [bree.name]"

    old "Defend Aletta"
    new "Защитить Алетту"

    old "Defend Anna"
    new "Защитить Анну"

    old "Defend Audrey"
    new "Защитить Одри"

    old "Defend Ayesha"
    new "Защитить Айшу"

    old "Defend Ayesha and yourself"
    new "Защитить Айшу и себя"

    old "Defend Camila"
    new "Защитить Камилу"

    old "Defend Cassidy"
    new "Защитить Кэссиди"

    old "Defend Emma"
    new "Защитить Эмму"

    old "Defend Jack"
    new "Защитить Джека"

    old "Defend Jack and Scottie"
    new "Защитить Джека и Скотти"

    old "Defend Kleio"
    new "Защитить Клео"

    old "Defend Lavish"
    new "Защитить Лавиш"

    old "Defend Morgan"
    new "Защитить Морган"

    old "Defend Palla"
    new "Защитить Паллу"

    old "Defend Sasha"
    new "Защитить Сашу"

    old "Defend Scottie"
    new "Защитить Скотти"

    old "Defend Scottie and Jack"
    new "Защитить Скотти и Джека"

    old "Defend Shiori"
    new "Защитить Сиори"

    old "DejaVu Sans"
    new "DejaVu Sans"

    old "Delete slot [text]"
    new "Удалить слот [text]"

    old "Demand she stay"
    new "Потребовать, чтобы она осталась"

    old "Deny"
    new "Отрицать"

    old "Deny cheating"
    new "Отрицать измену"

    old "Deny everything"
    new "Всё отрицать"

    old "Deny her tonight"
    new "Сегодня ей отказать"

    old "Deny it"
    new "Отрицать"

    old "Deny responsibility"
    new "Отрицать ответственность"

    old "Depends"
    new "Зависит от ситуации"

    old "Describe Kylie as a cold-blooded killer"
    new "Описать Кайли как хладнокровную убийцу"

    old "Describe opposite of Palla"
    new "Описать полную противоположность Паллы"

    old "Describe Palla"
    new "Описать Паллу"

    old "DEVELOPERS"
    new "РАЗРАБОТЧИКИ"

    old "Did you just call me bitch?"
    new "Ты только что назвала меня сучкой?"

    old "Different country"
    new "Другая страна"

    old "Difficult"
    new "Сложно"

    old "Dildo"
    new "Дилдо"

    old "Disable"
    new "Отключить"

    old "Disagree"
    new "Не согласиться"

    old "Disagree with Alexis"
    new "Не согласиться с Алексис"

    old "Disagree, Ayesha shouldn't have a termination"
    new "Не согласиться: Айше не стоит прерывать беременность"

    old "Disapprove"
    new "Выразить неодобрение"

    old "Disapprove of the topless sunbathing"
    new "Осудить загорание топлес"

    old "Discipline her"
    new "Наказать её"

    old "Discourage Hanna from dancing"
    new "Отговорить Ханну от танцев"

    old "Discreet"
    new "Незаметный"

    old "Dismiss the guitarist as a jerk"
    new "Назвать гитариста придурком"

    old "Dismiss the pole as sexist"
    new "Назвать шест сексистским"

    old "display"
    new "режим экрана"

    old "Disrupted"
    new "Disrupted"

    old "Do I have to?"
    new "Я обязан?"

    old "Do it"
    new "Сделать это"

    old "Do it raw"
    new "Без презерватива"

    old "Do it, I won't"
    new "Делай, я не буду"

    old "Do not choke her"
    new "Не душить её"

    old "Do not choke Sasha"
    new "Не душить Сашу"

    old "Do not dance"
    new "Не танцевать"

    old "Do not let Shiori call the babysitter"
    new "Не позволять Сиори звонить няне"

    old "Do not offer her your coat"
    new "Не предлагать ей пальто"

    old "Do not stop Audrey"
    new "Не останавливать Одри"

    old "Do not use a condom"
    new "Не использовать презерватив"

    old "Do not use blindfold"
    new "Не использовать повязку на глаза"

    old "Do not use protection"
    new "Не использовать защиту"

    old "Do nothing"
    new "Ничего не делать"

    old "Do something for me"
    new "Сделай кое-что для меня"

    old "Do the dishes"
    new "Помой посуду"

    old "Do you trust the device the save was created on? You should only choose yes if you are the device's sole user."
    new "Доверяете ли вы устройству, на котором было создано сохранение? Вы должны выбрать \"Да\", только если вы являетесь единственным пользователем устройства."

    old "Do you want to have some sexy time?"
    new "Хочешь немного развлечься по-взрослому?"

    old "Does it matter?"
    new "Это имеет значение?"

    old "Does that make me gay?"
    new "Это делает меня геем?"

    old "Does your daddy know?"
    new "Твой папочка знает?"

    old "Doggy"
    new "По-собачьи"

    old "Doggy style"
    new "По-собачьи"

    old "Doing it right now"
    new "Уже делаю"

    old "Don't"
    new "Не надо"

    old "Don't apologize"
    new "Не извиняться"

    old "Don't ask for anything"
    new "Ничего не просить"

    old "Don't back off"
    new "Не отступать"

    old "Don't bail Kleio out"
    new "Не вносить залог за Клео"

    old "Don't believe her"
    new "Не верить ей"

    old "Don't bother with the dude (Never meet Scottie again)"
    new "Не связываться с этим чуваком (больше никогда не встречаться со Скотти)"

    old "Don't Care"
    new "Не обращать внимания"

    old "Don't cheat on me again"
    new "Больше мне не изменяй"

    old "Don't choke her"
    new "Не душить её"

    old "Don't cum"
    new "Не кончать"

    old "Don't cum in her mouth"
    new "Не кончать ей в рот"

    old "Don't do it"
    new "Не делай этого"

    old "Don't eat the sandwich"
    new "Не есть сэндвич"

    old "Don't feel her up"
    new "Не лапать её"

    old "Don't flirt with Amy (Never meet Amy again)"
    new "Не флиртовать с Эми (больше никогда не встречаться с Эми)"

    old "Don't flirt with her (Never meet Amy again)"
    new "Не флиртовать с ней (больше никогда не встречаться с Эми)"

    old "Don't follow her"
    new "Не следовать за ней"

    old "Don't follow her (Never meet Lexi again)"
    new "Не следовать за ней (больше никогда не встречаться с Лекси)"

    old "Don't follow them"
    new "Не следовать за ними"

    old "Don't get involved"
    new "Не вмешиваться"

    old "Don't give her a project"
    new "Не давать ей проект"

    old "Don't go"
    new "Не идти"

    old "Don't go over to Audrey"
    new "Не подходить к Одри"

    old "Don't Grind"
    new "Не тереться"

    old "Don't help her"
    new "Не помогать ей"

    old "Don't hesitate. Yes"
    new "Не сомневаться. Да"

    old "Don't hire him"
    new "Не нанимать его"

    old "Don't intervene"
    new "Не вмешиваться"

    old "Don't kiss her"
    new "Не целовать её"

    old "Don't laugh"
    new "Не смеяться"

    old "Don't let Audrey do whatever she wants"
    new "Не позволять Одри делать всё, что ей захочется"

    old "Don't let Harmony meet Angela"
    new "Не позволять Хармони встречаться с Анджелой"

    old "Don't let her"
    new "Не позволять ей"

    old "Don't let her bother you. Pitch something"
    new "Не позволять ей отвлекать. Предложить что-нибудь"

    old "Don't let her come in."
    new "Не впускать её"

    old "Don't look at the toys"
    new "Не смотреть на игрушки"

    old "Don't make a wish"
    new "Не загадывать желание"

    old "Don't mention the music"
    new "Не упоминать музыку"

    old "Don't open it"
    new "Не открывать"

    old "Don't Pay"
    new "Не платить"

    old "Don't pick a side"
    new "Не выбирать сторону"

    old "Don't play the guitar"
    new "Не играть на гитаре"

    old "Don't play too late."
    new "Не играй слишком долго"

    old "Don't push him"
    new "Не давить на него"

    old "Don't react"
    new "Не реагировать"

    old "Don't reassure Alexis"
    new "Не успокаивать Алексис"

    old "Don't resist"
    new "Не сопротивляться"

    old "Don't slide hand up"
    new "Не поднимать руку выше"

    old "Don't spank her"
    new "Не шлёпать её"

    old "Don't stop her"
    new "Не останавливать её"

    old "Don't use protection"
    new "Не использовать защиту"

    old "Don't use toys"
    new "Не использовать игрушки"

    old "Don't watch"
    new "Не смотреть"

    old "Don't watch the footage"
    new "Не смотреть запись"

    old "Don't worry"
    new "Не волнуйся"

    old "Don't worry about it."
    new "Не переживай об этом"

    old "Don't worry, I'll cover the difference."
    new "Не волнуйся, я покрою разницу"

    old "Don't worry, I'll protect you"
    new "Не волнуйся, я тебя защищу"

    old "Don't you think you need to be punished"
    new "Тебе не кажется, что тебя нужно наказать?"

    old "DONE"
    new "ГОТОВО"

    old "Done"
    new "Принять"

    old "DornVA as Angela"
    new "DornVA — Анджела"

    old "dotdotdot, Aphelion, Dr.Pancakes, CSP, nebs"
    new "dotdotdot, Aphelion, Dr.Pancakes, CSP, nebs"

    old "Double facial"
    new "Кончить на лица обеих"

    old "Doubt"
    new "Сомневаться"

    old "Downloading the game data."
    new "Загрузка данных игры."

    old "Downloading the updates."
    new "Загрузка обновлений."

    old "Dozens"
    new "Десятки"

    old "Drew Turner, Brandon Ferguson, Buttery Biscuit, Scottie,"
    new "Drew Turner, Brandon Ferguson, Buttery Biscuit, Scottie,"

    old "Drop it"
    new "Забыть об этом"

    old "Dump her ass"
    new "Бросить её"

    old "Dump Sasha"
    new "Бросить Сашу"

    old "dxxx, dosel, Lafenya Lou, Aeon, Archie themoon, Mike Johnson,"
    new "dxxx, dosel, Lafenya Lou, Aeon, Archie themoon, Mike Johnson,"

    old "Dye my hair in pink"
    new "Покрасить волосы в розовый"

    old "E"
    new "E"

    old "e"
    new "e"

    old "E-sports and speedrunning"
    new "Киберспорт и спидраны"

    old "Ease the tension"
    new "Разрядить обстановку"

    old "Easy"
    new "Легко"

    old "Eat her pussy"
    new "Вылизать её киску"

    old "Eat quickly"
    new "Есть быстро"

    old "Eat the sandwich"
    new "Съесть сэндвич"

    old "Eat the soup without complaint"
    new "Съесть суп без жалоб"

    old "Education"
    new "Педагогика"

    old "Either this project does not support updating, or the update status file was deleted."
    new "Или этот проект не поддерживает обновление, или файл статуса обновления был удалён."

    old "ElysianReign, Cosmic_SK, Chris, lee osterloh, Joe Kieler,"
    new "ElysianReign, Cosmic_SK, Chris, lee osterloh, Joe Kieler,"

    old "Emma, we can go to one of her shows"
    new "Эмма, мы можем сходить на одно из её шоу"

    old "Emma, you should try a wrestling class once"
    new "Эмма, тебе как-нибудь стоит попробовать занятие по рестлингу"

    old "emphasize audio"
    new "усилить громкость заранее заданных звуковых каналов за счёт приглушения остальных каналов"

    old "Enable"
    new "Включить"

    old "Enable (No Blocklist)"
    new "Включить (без списка блокировки)"

    old "Enable/Disable tooltip for the story steps.\nClick on the step with a 👁️ to see the hints."
    new "Включить или отключить подсказки для этапов сюжета.\nНажмите на этап со значком 👁️, чтобы увидеть подсказки."

    old "Enabled DLCS"
    new "Включённые DLC"

    old "Enabling cheats will disable the New Game+ and Achievements for this game's save.\n\nIf you want to unlock Achievements again, you need to start a new game and play without cheats."
    new "Включение читов отключит «Новую игру+» и достижения для этого сохранения.\n\nЧтобы снова получать достижения, начните новую игру и играйте без читов."

    old "Encourage Hanna to dance"
    new "Поддержать желание Ханны танцевать"

    old "Encourage her not to get inked"
    new "Убедить её не делать татуировку"

    old "Encourage her to get inked"
    new "Убедить её сделать татуировку"

    old "End Replay"
    new "Завершить повтор"

    old "Endless"
    new "Бесконечно"

    old "Enjoy the moment"
    new "Насладиться моментом"

    old "Enjoy the ride"
    new "Наслаждаться поездкой"

    old "Enough"
    new "Достаточно"

    old "Enough of her crap, I'm going home"
    new "Хватит с меня её чуши, я иду домой"

    old "ENTER"
    new "ENTER"

    old "Enter"
    new "Enter"

    old "Enter Sync ID"
    new "Введите Sync ID"

    old "Enter the booth with Alexis"
    new "Войти в кабинку вместе с Алексис"

    old "Entertaining."
    new "Забавно"

    old "Envy the guitarist his popularity"
    new "Позавидовать популярности гитариста"

    old "Equip a shield"
    new "Экипировать щит"

    old "ERROR!"
    new "ОШИБКА!"

    old "ESCAPE"
    new "ESCAPE"

    old "Escape"
    new "Escape"

    old "Escort Palla out"
    new "Проводить Паллу наружу"

    old "Exit"
    new "Выход"

    old "Explain yourself"
    new "Объясниться"

    old "Eyes up here."
    new "Глаза сюда"

    old "F"
    new "F"

    old "f"
    new "f"

    old "Facial"
    new "Кончить на лицо"

    old "Failed to save screenshot as %s."
    new "Не удалось сохранить скриншот как %s."

    old "Fall"
    new "Осень"

    old "Fantastic"
    new "Прекрасно"

    old "Fantasy"
    new "Фэнтези"

    old "Fat and ugly, indeed"
    new "Толстая и уродливая, и правда"

    old "Fawn over the kids"
    new "Умиляться детям"

    old "Feel her up"
    new "Полапать её"

    old "Femdom porn"
    new "Фемдом-порно"

    old "Feniks"
    new "Feniks"

    old "Fenpai, A.K.A wut, WilliamS, Sir. BYM, Sly, HalfFang,"
    new "Fenpai, A.K.A wut, WilliamS, Sir. BYM, Sly, HalfFang,"

    old "Fiction"
    new "Художественная литература"

    old "Fight"
    new "Драться"

    old "Fight bare handed"
    new "Драться голыми руками"

    old "File list digest does not match."
    new "Дайджест списка файлов не совпадает."

    old "File page [text]"
    new "Страница сохранений [text]"

    old "File page auto"
    new "Автосохранения"

    old "File page quick"
    new "Быстрые сохранения"

    old "Filter: "
    new "Фильтр:"

    old "Find a deeper spiritual meaning in the story"
    new "Найти в истории более глубокий духовный смысл"

    old "Find a diplomatic solution"
    new "Найти дипломатическое решение"

    old "Find an empty seat"
    new "Найти свободное место"

    old "Find fault with the moral of the story"
    new "Найти изъян в морали истории"

    old "Fine"
    new "Ладно"

    old "Fine, I'll meet you there"
    new "Ладно, я встречусь с тобой там"

    old "Fine, Let's Go"
    new "Ладно, пошли"

    old "Fine, you win"
    new "Ладно, ты победила"

    old "Fine... I won't meet Thyra"
    new "Ладно... я не буду встречаться с Тирой"

    old "Finely balanced, as all things should be"
    new "Идеально сбалансировано, как и должно быть"

    old "Finger [bree.name]'s ass"
    new "Ласкать задницу [bree.name] пальцами"

    old "Finger [bree.name]'s pussy"
    new "Ласкать киску [bree.name] пальцами"

    old "Finger her"
    new "Ласкать её пальцами"

    old "Finger her ass"
    new "Засунуть палец ей в задницу"

    old "Finger her pussy"
    new "Ласкать её киску пальцами"

    old "Fingers her ass"
    new "Засунуть пальцы ей в задницу"

    old "Finish with tongue"
    new "Закончить языком"

    old "Finish with tongue and dildo in ass"
    new "Закончить языком и дилдо в заднице"

    old "Finish with tongue and dildo in pussy"
    new "Закончить языком и дилдо в киске"

    old "Finish with tongue and finger in ass"
    new "Закончить языком и пальцем в заднице"

    old "Finishing up."
    new "Завершение."

    old "First Name: "
    new "Имя:"

    old "Fitness"
    new "Фитнес"

    old "Flat doggy"
    new "Лёжа по-собачьи"

    old "Flirt"
    new "Флиртовать"

    old "Flirt a little with Diane"
    new "Немного пофлиртовать с Дианой"

    old "Flirt back"
    new "Ответить на флирт"

    old "Flirt with Amy"
    new "Флиртовать с Эми"

    old "Flirt with the girl"
    new "Флиртовать с девушкой"

    old "Flush it again"
    new "Смыть ещё раз"

    old "Follow her"
    new "Последовать за ней"

    old "Follow her lead"
    new "Следовать её примеру"

    old "Follow Sasha after a minute"
    new "Последовать за Сашей через минуту"

    old "Follow Sasha after five minutes"
    new "Последовать за Сашей через пять минут"

    old "Follow Sasha immediately"
    new "Сразу последовать за Сашей"

    old "Follow them"
    new "Последовать за ними"

    old "font kerning"
    new "кёрнинг шрифта"

    old "font line spacing"
    new "межстрочный интервал"

    old "Font Override"
    new "Переопределение шрифта"

    old "font size"
    new "размер шрифта"

    old "font transform"
    new "замена шрифта"

    old "Food"
    new "Еда"

    old "For a dance? Sure"
    new "Потанцевать? Конечно"

    old "For a kiss..."
    new "За поцелуй..."

    old "For another kiss"
    new "За ещё один поцелуй"

    old "For kids, not for kids... Noodles, don't noodles..."
    new "Для детей, не для детей... Лапша, не лапша..."

    old "Force ANGLE2 Renderer"
    new "Принудительно использовать ANGLE2"

    old "Force GL2 Renderer"
    new "Принудительно использовать GL2"

    old "Force GLES2 Renderer"
    new "Принудительно использовать GLES2"

    old "Force update"
    new "Принудительно обновить"

    old "Forget about the post-credit scene"
    new "Забыть о сцене после титров"

    old "Forget it"
    new "Забудь"

    old "Forget it!"
    new "Забудь!"

    old "fouassier, Ellis, Kugel2456, That Asshole Vlogger,"
    new "fouassier, Ellis, Kugel2456, That Asshole Vlogger,"

    old "Four Leaf, Sovereign16, Wutthiwat Wiriyathanacharoenkit,"
    new "Four Leaf, Sovereign16, Wutthiwat Wiriyathanacharoenkit,"

    old "Framerate"
    new "Частота кадров"

    old "Frank Mecka, CheeseMasta, TheDevilYouKnow, Roknor, Rawk,"
    new "Frank Mecka, CheeseMasta, TheDevilYouKnow, Roknor, Rawk,"

    old "Free at last!"
    new "Наконец-то свободен!"

    old "Free booze is free booze!"
    new "Бесплатная выпивка есть бесплатная выпивка!"

    old "Friends"
    new "Друзья"

    old "Friends with benefits"
    new "Друзья с привилегиями"

    old "From now on I will call you Cupcake"
    new "Отныне я буду называть тебя Кексиком"

    old "From now on I will stop calling you Cupcake"
    new "Отныне я перестану называть тебя Кексиком"

    old "Fuck"
    new "Трахнуть"

    old "Fuck [bree.name]"
    new "Трахнуть [bree.name]"

    old "Fuck [bree.name]'s ass"
    new "Трахнуть [bree.name] в задницу"

    old "Fuck [bree.name]'s pussy"
    new "Трахнуть [bree.name] в киску"

    old "Fuck Aletta"
    new "Трахнуть Алетту"

    old "Fuck Aletta in the ass"
    new "Трахнуть Алетту в задницу"

    old "Fuck Aletta in the pussy"
    new "Трахнуть Алетту в киску"

    old "Fuck Amy"
    new "Трахнуть Эми"

    old "Fuck Anna"
    new "Трахнуть Анну"

    old "Fuck Anna's ass"
    new "Трахнуть Анну в задницу"

    old "Fuck Anna's mouth"
    new "Трахнуть Анну в рот"

    old "Fuck Anna's pussy"
    new "Трахнуть Анну в киску"

    old "Fuck ass"
    new "Трахнуть в задницу"

    old "Fuck Audrey"
    new "Трахнуть Одри"

    old "Fuck Audrey in the pussy"
    new "Трахнуть Одри в киску"

    old "Fuck Audrey up the ass"
    new "Трахнуть Одри в задницу"

    old "Fuck Audrey's ass"
    new "Трахнуть Одри в задницу"

    old "Fuck Audrey's pussy"
    new "Трахнуть Одри в киску"

    old "Fuck Ayesha"
    new "Трахнуть Айшу"

    old "Fuck Ayesha too"
    new "Трахнуть и Айшу"

    old "Fuck Camila"
    new "Трахнуть Камилу"

    old "Fuck Cassidy"
    new "Трахнуть Кэссиди"

    old "Fuck Emma"
    new "Трахнуть Эмму"

    old "Fuck Harmony"
    new "Трахнуть Хармони"

    old "Fuck Harmony one last time"
    new "В последний раз трахнуть Хармони"

    old "Fuck her"
    new "Трахнуть её"

    old "Fuck her ass"
    new "Трахнуть её в задницу"

    old "Fuck her ass instead"
    new "Вместо этого трахнуть её в задницу"

    old "Fuck her doggystyle"
    new "Трахнуть её по-собачьи"

    old "Fuck her from behind"
    new "Трахнуть её сзади"

    old "Fuck her from front"
    new "Трахнуть её спереди"

    old "Fuck her missionary style"
    new "Трахнуть её в миссионерской позе"

    old "Fuck her on her back"
    new "Трахнуть её на спине"

    old "Fuck her pussy"
    new "Трахнуть её в киску"

    old "Fuck her pussy raw"
    new "Трахнуть её в киску без презерватива"

    old "Fuck her pussy with a condom"
    new "Трахнуть её в киску с презервативом"

    old "Fuck her reverse cowgirl style"
    new "Трахнуть её в позе обратной наездницы"

    old "Fuck her tits"
    new "Трахнуть её сиськи"

    old "Fuck Kat"
    new "Трахнуть Кэт"

    old "Fuck Kleio"
    new "Трахнуть Клео"

    old "Fuck Kleio's ass"
    new "Трахнуть Клео в задницу"

    old "Fuck Kleio's pussy"
    new "Трахнуть Клео в киску"

    old "Fuck Kylie"
    new "Трахнуть Кайли"

    old "Fuck Kylie too"
    new "Трахнуть и Кайли"

    old "Fuck Lavish"
    new "Трахнуть Лавиш"

    old "Fuck Lexi"
    new "Трахнуть Лекси"

    old "Fuck Minami"
    new "Трахнуть Минами"

    old "Fuck Minami's ass"
    new "Трахнуть Минами в задницу"

    old "Fuck Minami's pussy"
    new "Трахнуть Минами в киску"

    old "Fuck Morgan"
    new "Трахнуть Морган"

    old "Fuck off"
    new "Отвали"

    old "Fuck Palla"
    new "Трахнуть Паллу"

    old "Fuck pussy"
    new "Трахнуть киску"

    old "Fuck Samantha"
    new "Трахнуть Саманту"

    old "Fuck Sasha"
    new "Трахнуть Сашу"

    old "Fuck Sasha in the pussy"
    new "Трахнуть Сашу в киску"

    old "Fuck Sasha instead"
    new "Вместо этого трахнуть Сашу"

    old "Fuck Sasha up the ass"
    new "Трахнуть Сашу в задницу"

    old "Fuck Sasha's ass"
    new "Трахнуть Сашу в задницу"

    old "Fuck Sasha's mouth"
    new "Трахнуть Сашу в рот"

    old "Fuck Sasha's pussy"
    new "Трахнуть Сашу в киску"

    old "Fuck Shiori"
    new "Трахнуть Сиори"

    old "Fuck that noise"
    new "Да ну его к чёрту"

    old "Fuck them"
    new "Трахнуть их"

    old "Fuck them both"
    new "Трахнуть их обеих"

    old "Full traceback:"
    new "Полная трассировка:"

    old "Fullscreen"
    new "Полноэкранный режим"

    old "Fully clothed"
    new "Полностью одета"

    old "Fun"
    new "Веселье"

    old "Fun facts about 'Gravlax'"
    new "Интересные факты о гравлаксе"

    old "Funnel Cake"
    new "Воронкообразный пирог"

    old "G"
    new "G"

    old "g"
    new "g"

    old "GALLERY"
    new "ГАЛЕРЕЯ"

    old "Game console"
    new "Игровая приставка"

    old "GAMEPAD"
    new "ГЕЙМПАД"

    old "Gamepad"
    new "Геймпад"

    old "Gaming cumpetition"
    new "Игровое соревнование"

    old "Gasp in shock"
    new "Ахнуть от потрясения"

    old "Geez, I sorta feel the same way too!"
    new "Чёрт, я вроде тоже чувствую то же самое!"

    old "Generic"
    new "Общие"

    old "Gentle"
    new "Нежно"

    old "Gesticulates to hurry her up"
    new "Жестом поторопить её"

    old "Get amorous"
    new "Проявить страсть"

    old "Get an ice cream"
    new "Купить мороженое"

    old "Get angry"
    new "Разозлиться"

    old "Get her a Blue Hawaii"
    new "Заказать ей «Голубые Гавайи»"

    old "Get her a Blue Hawaiian"
    new "Заказать ей «Голубые Гавайи»"

    old "Get involved"
    new "Вмешаться"

    old "Get it fixed"
    new "Починить"

    old "Get me a coffee."
    new "Принеси мне кофе"

    old "Get offended at Kylie's comments"
    new "Оскорбиться из-за комментариев Кайли"

    old "Get on the bed"
    new "Ложись на кровать"

    old "Get on with the beads"
    new "Перейти к шарикам"

    old "Get on your knees, bitch!"
    new "На колени, сучка!"

    old "Get rid of her"
    new "Избавиться от неё"

    old "Get straight to the main experiment"
    new "Сразу перейти к главному эксперименту"

    old "Get up"
    new "Встать"

    old "Get yourself a drink."
    new "Возьми себе выпить"

    old "Get yourself and [bree.name] a drink."
    new "Возьми выпить себе и [bree.name]"

    old "Gift"
    new "Подарок"

    old "Give [bree.name] some oral attention"
    new "Сделать [bree.name] кунилингус"

    old "Give Alexis a massage"
    new "Сделать Алексис массаж"

    old "Give Ayesha oral"
    new "Сделать Айше кунилингус"

    old "Give her a cunnilingus"
    new "Сделать ей кунилингус"

    old "Give her oral"
    new "Сделать ей кунилингус"

    old "Give her some oral attention"
    new "Сделать ей кунилингус"

    old "Give her the easier but more important project"
    new "Дать ей более лёгкий, но важный проект"

    old "Give her the harder but less important project"
    new "Дать ей более сложный, но менее важный проект"

    old "Give her what she deserves"
    new "Дать ей то, чего она заслуживает"

    old "Give it to her"
    new "Отдать ей"

    old "Give it to him"
    new "Отдать ему"

    old "Give Kleio some attention"
    new "Уделить внимание Клео"

    old "Give me a blowjob"
    new "Сделай мне минет"

    old "Give me some money"
    new "Дай мне немного денег"

    old "Give Morgan some attention"
    new "Уделить внимание Морган"

    old "Give the waiter a piece of your mind"
    new "Высказать официанту всё, что думаешь"

    old "gl framerate"
    new "настройка графики. Частота кадров"

    old "gl powersave"
    new "настройка графики. Экономия энергии"

    old "gl tearing"
    new "настройка графики. Разрывание кадров"

    old "Go"
    new "Пойти"

    old "Go ahead"
    new "Продолжай"

    old "Go alone"
    new "Пойти одному"

    old "Go along"
    new "Подыграть"

    old "Go back"
    new "Вернуться"

    old "Go back and rectify the error"
    new "Вернуться и исправить ошибку"

    old "Go back inside"
    new "Вернуться внутрь"

    old "Go back on the beach"
    new "Вернуться на пляж"

    old "Go check on her"
    new "Пойти проверить, как она"

    old "Go cowgirl style"
    new "В позе наездницы"

    old "Go doggy style"
    new "По-собачьи"

    old "Go down on her"
    new "Сделать ей кунилингус"

    old "Go easy on me"
    new "Будьте со мной полегче"

    old "Go for a stroll"
    new "Прогуляться"

    old "Go for a walk"
    new "Прогуляться"

    old "Go for it"
    new "Действовать"

    old "Go for Sasha"
    new "Выбрать Сашу"

    old "Go grab an ice cream"
    new "Пойти купить мороженое"

    old "Go grab more boxes outside"
    new "Пойти за оставшимися коробками"

    old "Go home"
    new "Пойти домой"

    old "Go in"
    new "Войти"

    old "Go in the yard"
    new "Выйти во двор"

    old "Go missionary style"
    new "В миссионерской позе"

    old "Go on for the main course"
    new "Перейти к главному блюду"

    old "Go on with Harmony"
    new "Продолжить с Хармони"

    old "Go on with Lexi"
    new "Продолжить с Лекси"

    old "Go over"
    new "Подойти"

    old "Go over to Audrey"
    new "Подойти к Одри"

    old "Go slow and gentle"
    new "Медленно и нежно"

    old "Go to a Bridal boutique"
    new "Пойти в свадебный салон"

    old "Go to a lingerie store"
    new "Пойти в магазин нижнего белья"

    old "go to city"
    new "Отправиться в город"

    old "go to home first floor"
    new "перейти на первый этаж дома"

    old "go to home second floor"
    new "перейти на второй этаж дома"

    old "Go to the bar"
    new "Пойти в бар"

    old "Go to the bathroom"
    new "Пойти в туалет"

    old "Go to the bedroom."
    new "Пойти в спальню"

    old "Go to the dance floor"
    new "Пойти на танцпол"

    old "Go to the family beach"
    new "Пойти на семейный пляж"

    old "Go to the night club"
    new "Пойти в ночной клуб"

    old "Go to the nudist beach"
    new "Пойти на нудистский пляж"

    old "Go to the topless beach"
    new "Пойти на пляж топлес"

    old "Go trick or treating"
    new "Пойти собирать сладости"

    old "Go with Sasha"
    new "Пойти с Сашей"

    old "Golf"
    new "Гольф"

    old "Gonzo porn"
    new "Гонзо-порно"

    old "Good idea"
    new "Хорошая идея"

    old "Good try, but you should do it like this."
    new "Неплохая попытка, но лучше сделать вот так"

    old "Gouvernathor"
    new "Gouvernathor"

    old "Grab her ass"
    new "Схватить её за задницу"

    old "Grab her wrist and stop her"
    new "Схватить её за запястье и остановить"

    old "Grab us seats, I'll wait Camila at the bar"
    new "Займи нам места, а я подожду Камилу у бара"

    old "Great work!"
    new "Отличная работа!"

    old "Grind on her"
    new "Тереться об неё"

    old "Gross!"
    new "Мерзость!"

    old "Gush over the happy families"
    new "Умиляться счастливым семьям"

    old "H"
    new "H"

    old "h"
    new "h"

    old "Haircut"
    new "Стрижка"

    old "Hamburger"
    new "Гамбургер"

    old "Hand it over"
    new "Отдать"

    old "Hand job"
    new "Дрочка рукой"

    old "Hand the 5K over to her"
    new "Передать ей 5000"

    old "Harems"
    new "Гаремы"

    old "Hate people"
    new "Ненавижу людей"

    old "Have a taste of her"
    new "Попробовать её на вкус"

    old "Have Audrey give me a blowjob"
    new "Пусть Одри сделает мне минет"

    old "Have Drinks"
    new "Выпить"

    old "Have fun!"
    new "Приятной игры!"

    old "Have fun."
    new "Развлекайся"

    old "Have her suck you off"
    new "Пусть она отсосёт"

    old "Have it your way"
    new "Пусть будет по-твоему"

    old "Have Sasha give me a blowjob"
    new "Пусть Саша сделает мне минет"

    old "He never looked back"
    new "Он ни разу не оглянулся"

    old "He's still a greasy slob"
    new "Он всё ещё сальный неряха"

    old "He's still following his vision"
    new "Он всё ещё следует своему видению"

    old "Head down to the mall"
    new "Спуститься в торговый центр"

    old "Healthy Eating"
    new "Здоровое питание"

    old "Heavy Boxes"
    new "Тяжёлые коробки"

    old "hell543, AJChaser, Human1134, BumChuzzler, Markus,"
    new "hell543, AJChaser, Human1134, BumChuzzler, Markus,"

    old "Hello,"
    new "Здравствуйте,"

    old "Help"
    new "Помочь"

    old "Help [bree.name]"
    new "Помочь [bree.name]"

    old "Help Aletta"
    new "Помочь Алетте"

    old "Help Audrey"
    new "Помочь Одри"

    old "Help Harmony into her seat"
    new "Помочь Хармони сесть"

    old "Help her"
    new "Помочь ей"

    old "Help her out"
    new "Помочь ей"

    old "Help her!"
    new "Помочь ей!"

    old "Help Lavish"
    new "Помочь Лавиш"

    old "Help me look."
    new "Помоги мне поискать"

    old "Help Shiori"
    new "Помочь Сиори"

    old "Help them"
    new "Помочь им"

    old "Hendrik Baumbach, Andre Bernhardt, Coda_118, vakknight .,"
    new "Hendrik Baumbach, Andre Bernhardt, Coda_118, vakknight .,"

    old "Hesitate. Yes"
    new "Колебаться. Да"

    old "Hey, I don't care."
    new "Эй, мне всё равно"

    old "Hey, Samantha."
    new "Привет, Саманта"

    old "Hide"
    new "Скрывать"

    old "Hide and watch"
    new "Спрятаться и наблюдать"

    old "Hide it from her"
    new "Скрыть это от неё"

    old "Hides the user interface."
    new "Скрывает пользовательский интерфейс"

    old "High Contrast Text"
    new "Высококонтрастный текст"

    old "high contrast text"
    new "высококонтрастный текст"

    old "Hiking trail"
    new "Туристическая тропа"

    old "Hire him"
    new "Нанять его"

    old "Historical drama"
    new "Историческая драма"

    old "History"
    new "История"

    old "Hit him first"
    new "Ударить его первым"

    old "Hold back"
    new "Сдержаться"

    old "Homework doesn't sound fun. Good luck with that!"
    new "Домашнее задание звучит не очень весело. Удачи!"

    old "horizontal scroll"
    new ". горизонтальная полоса прокрутки"

    old "Hot coffee?"
    new "«Горячий кофе»?"

    old "How about you"
    new "А ты?"

    old "How bad can being her bitch be?"
    new "Насколько плохо быть её сучкой?"

    old "How do you know?"
    new "Откуда ты знаешь?"

    old "Hug her"
    new "Обнять её"

    old "Hug her back"
    new "Обнять её в ответ"

    old "Huh, you said something?"
    new "А? Ты что-то сказала?"

    old "Hum... Lennie, I like it"
    new "Хм... Ленни, мне нравится"

    old "Humor her"
    new "Подыграть ей"

    old "I"
    new "I"

    old "i"
    new "i"

    old "I accept the money from Hanna"
    new "Принять деньги от Ханны"

    old "I actually like you"
    new "Ты мне действительно нравишься"

    old "I admit."
    new "Признаю"

    old "I agree"
    new "Я согласен"

    old "I already told you"
    new "Я уже говорил"

    old "I am a conservative"
    new "Я консерватор"

    old "I am a dom"
    new "Я доминант"

    old "I am a liberal"
    new "Я либерал"

    old "I am a people person"
    new "Я легко схожусь с людьми"

    old "I am a pro on arcade this should not be more complicated"
    new "Я профессионал в аркадных гонках, это не должно быть сложнее"

    old "I am a sub"
    new "Я сабмиссив"

    old "I am better than any woman"
    new "Я лучше любой женщины"

    old "I am hung"
    new "У меня огромный член"

    old "I am irritated"
    new "Я раздражён"

    old "I am manly already"
    new "Я и так мужественный"

    old "I am more than enough"
    new "Меня более чем достаточно"

    old "I am not that interested"
    new "Мне это не особо интересно"

    old "I am pretty lucky"
    new "Мне довольно часто везёт"

    old "I am prone to erectile problems"
    new "У меня бывают проблемы с эрекцией"

    old "I am the one who would ask"
    new "Спрашивать буду я"

    old "I am touched"
    new "Я тронут"

    old "I am unlucky"
    new "Мне не везёт"

    old "I believe in god"
    new "Я верю в Бога"

    old "I can always get another job"
    new "Я всегда могу найти другую работу"

    old "I can cook for you."
    new "Я могу приготовить тебе еду"

    old "I can date you"
    new "Я могу встречаться с тобой"

    old "I can lend you that money"
    new "Я могу одолжить тебе деньги"

    old "I can play guitar"
    new "Я умею играть на гитаре"

    old "I can take you to fast food"
    new "Я могу сводить тебя в фастфуд"

    old "I can think of games we could play."
    new "Я могу придумать игры, в которые мы могли бы сыграть"

    old "I can't"
    new "Я не могу"

    old "I can't accept"
    new "Я не могу принять"

    old "I can't do that"
    new "Я не могу так поступить"

    old "I can't do that to them"
    new "Я не могу так с ними поступить"

    old "I can't even count"
    new "Я даже сосчитать не могу"

    old "I can't promise."
    new "Не могу обещать"

    old "I can't stand kids."
    new "Терпеть не могу детей"

    old "I can't!"
    new "Я не могу!"

    old "I care about you"
    new "Ты мне небезразлична"

    old "I could"
    new "Я мог бы"

    old "I could never ask Sasha for that!"
    new "Я никогда не смогу попросить Сашу о таком!"

    old "I could never say no to a pretty face"
    new "Я никогда не могу отказать красивому личику"

    old "I didn't want to offend you"
    new "Я не хотел тебя обидеть"

    old "I disagree"
    new "Я не согласен"

    old "I do"
    new "Да"

    old "I do not accept the money from Hanna"
    new "Не принимать деньги от Ханны"

    old "I don't"
    new "А я нет"

    old "I don't believe in coincidence"
    new "Я не верю в совпадения"

    old "I don't believe in fate"
    new "Я не верю в судьбу"

    old "I don't believe in god"
    new "Я не верю в Бога"

    old "I don't care who else you see"
    new "Мне всё равно, с кем ещё ты встречаешься"

    old "I don't feel the same"
    new "Я так не чувствую"

    old "I don't have time for that"
    new "У меня нет на это времени"

    old "I don't have to fuck her"
    new "Я не обязан её трахать"

    old "I don't judge"
    new "Я не осуждаю"

    old "I don't know"
    new "Я не знаю"

    old "I don't know her"
    new "Я её не знаю"

    old "I don't like"
    new "Мне не нравится"

    old "I don't like it"
    new "Мне не нравится"

    old "I don't like the kiss, but I don't show it"
    new "Мне не нравится поцелуй, но я этого не показываю"

    old "I don't love her"
    new "Я её не люблю"

    old "I don't mind"
    new "Я не против"

    old "I don't need love"
    new "Мне не нужна любовь"

    old "I don't need that"
    new "Мне это не нужно"

    old "I don't prefer blondes"
    new "Я не предпочитаю блондинок"

    old "I don't sleep"
    new "Я не сплю"

    old "I don't smell THAT bad"
    new "Я пахну не НАСТОЛЬКО плохо"

    old "I don't think so"
    new "Не думаю"

    old "I don't think violence is the answer"
    new "Не думаю, что насилие — это решение"

    old "I don't want a harem"
    new "Я не хочу гарем"

    old "I don't want anything to do with it"
    new "Я не хочу иметь с этим ничего общего"

    old "I don't, really"
    new "На самом деле нет"

    old "I feel the same"
    new "Я чувствую то же самое"

    old "I feel the same way"
    new "Я чувствую то же самое"

    old "I forgot"
    new "Я забыл"

    old "I give help, I don't need help."
    new "Я помогаю другим, мне помощь не нужна"

    old "I got held up"
    new "Меня задержали"

    old "I got this!"
    new "Я справлюсь!"

    old "I guess I just didn't really see you"
    new "Наверное, я просто тебя не замечал"

    old "I guess so"
    new "Наверное, да"

    old "I guess this is goodbye"
    new "Наверное, это прощание"

    old "I guess we don't"
    new "Наверное, у нас ничего не получится"

    old "I guess we grew out of that"
    new "Наверное, мы это переросли"

    old "I had enough"
    new "С меня хватит"

    old "I hate them"
    new "Я их ненавижу"

    old "I hated it"
    new "Я это ненавижу"

    old "I have a bad feeling about this"
    new "У меня плохое предчувствие"

    old "I have a small penis"
    new "У меня маленький пенис"

    old "I have a thing for them"
    new "У меня на них фетиш"

    old "I have a very high libido"
    new "У меня очень высокое либидо"

    old "I have important work to do (Never meet Cassidy again)"
    new "У меня важная работа (больше никогда не встречаться с Кэссиди)"

    old "I have some big debt."
    new "У меня большие долги"

    old "I have to ask the girls."
    new "Мне нужно спросить девушек"

    old "I haven't been counting."
    new "Я не считал"

    old "I hope this is all ethically sourced"
    new "Надеюсь, всё это произведено этично"

    old "I insist"
    new "Я настаиваю"

    old "I insist Hanna reinvest the money in the gym"
    new "Настоять, чтобы Ханна вложила деньги обратно в спортзал"

    old "I insist, you need this"
    new "Я настаиваю, тебе это нужно"

    old "I just hope I will not screw up"
    new "Надеюсь, я не облажаюсь"

    old "I just want to eat you."
    new "Я просто хочу тебя вылизать"

    old "I kind of like you"
    new "Ты мне вроде нравишься"

    old "I kinda like her"
    new "Она мне вроде нравится"

    old "I know he is"
    new "Я знаю"

    old "I know you cheat and I don't want to see you again"
    new "Я знаю, что ты изменяешь, и больше не хочу тебя видеть"

    old "I know you cheat on me and that's okay"
    new "Я знаю, что ты мне изменяешь, и меня это устраивает"

    old "I laugh off Morgan being late"
    new "Отшутиться от опоздания Морган"

    old "I like"
    new "Мне нравится"

    old "I like a woman on her knees"
    new "Мне нравится женщина на коленях"

    old "I like dogs"
    new "Мне нравятся собаки"

    old "I like it"
    new "Мне нравится"

    old "I like it when you call me sir."
    new "Мне нравится, когда ты называешь меня сэром"

    old "I like it when you call me that outside work"
    new "Мне нравится, когда вне работы ты называешь меня так"

    old "I like the golden retriever"
    new "Мне нравится золотистый ретривер"

    old "I like the kiss"
    new "Мне нравится поцелуй"

    old "I like the old you better"
    new "Старая ты мне нравилась больше"

    old "I like the pug"
    new "Мне нравится мопс"

    old "I like them big"
    new "Мне нравятся большие"

    old "I like them small"
    new "Мне нравятся маленькие"

    old "I like them."
    new "Мне они нравятся"

    old "I like this ball of fur"
    new "Мне нравится этот комок шерсти"

    old "I like you too"
    new "Ты мне тоже нравишься"

    old "I like you, but not in the same way"
    new "Ты мне нравишься, но не так"

    old "I liked it"
    new "Мне понравилось"

    old "I liked it when you acted all tough"
    new "Мне нравилось, когда ты строила из себя крутую"

    old "I live to serve"
    new "Я живу, чтобы служить"

    old "I love It"
    new "Я в восторге"

    old "I love it"
    new "Я это обожаю"

    old "I love it too"
    new "Я тоже это люблю"

    old "I love them"
    new "Я их обожаю"

    old "I love you too"
    new "Я тоже тебя люблю"

    old "I love you too, Shiori"
    new "Я тоже тебя люблю, Сиори"

    old "I might have some ideas"
    new "У меня могут быть идеи"

    old "I mind"
    new "Я против"

    old "I need more practice"
    new "Мне нужно больше практики"

    old "I need some cream too"
    new "Мне тоже нужен крем"

    old "I need sun cream too!"
    new "Мне тоже нужен крем от солнца!"

    old "I need time to think about it."
    new "Мне нужно время подумать"

    old "I need to end my level"
    new "Мне нужно закончить уровень"

    old "I need to focus"
    new "Мне нужно сосредоточиться"

    old "I never wanted to before, but now..."
    new "Раньше я никогда этого не хотел, но теперь..."

    old "I only smoke while drunk"
    new "Я курю только когда пьян"

    old "I only want you"
    new "Мне нужна только ты"

    old "I prefer blondes"
    new "Я предпочитаю блондинок"

    old "I prefer cats"
    new "Я предпочитаю кошек"

    old "I prefer older women"
    new "Я предпочитаю женщин постарше"

    old "I prefer pop music"
    new "Я предпочитаю поп-музыку"

    old "I prefer willful women"
    new "Я предпочитаю своенравных женщин"

    old "I ride an exercise bike"
    new "Я катаюсь на велотренажёре"

    old "I should be reigning it in"
    new "Мне стоит сбавить обороты"

    old "I should have learned more about you"
    new "Мне стоило узнать тебя получше"

    old "I should try to convince Anna"
    new "Стоит попробовать убедить Анну"

    old "I should try to convince Kleio"
    new "Стоит попробовать убедить Клео"

    old "I should try to talk to Anna"
    new "Стоит попробовать поговорить с Анной"

    old "I should try to talk to Kleio"
    new "Стоит попробовать поговорить с Клео"

    old "I sleep with [bree.name] and Sasha."
    new "Я сплю с [bree.name] и Сашей"

    old "I still love you."
    new "Я всё ещё тебя люблю"

    old "I think he is"
    new "Думаю, да"

    old "I think I want the both of you"
    new "Кажется, я хочу вас обеих"

    old "I think we were meant to be"
    new "Думаю, нам было суждено быть вместе"

    old "I think you got the wrong end of the stick"
    new "Кажется, ты неправильно меня поняла"

    old "I try hard and try to beat Morgan"
    new "Изо всех сил попытаться обыграть Морган"

    old "I try hard but decide to let Morgan win"
    new "Постараться, но всё же позволить Морган победить"

    old "I understand"
    new "Я понимаю"

    old "I want junk food"
    new "Я хочу вредной еды"

    old "I want some time with [bree.name] and Minami"
    new "Я хочу побыть с [bree.name] и Минами"

    old "I want some time with [bree.name] and Sasha"
    new "Я хочу побыть с [bree.name] и Сашей"

    old "I want some time with Minami and [bree.name]"
    new "Я хочу побыть с Минами и [bree.name]"

    old "I want some time with Minami and Sasha"
    new "Я хочу побыть с Минами и Сашей"

    old "I want some time with Sasha and [bree.name]"
    new "Я хочу побыть с Сашей и [bree.name]"

    old "I want some time with Sasha and Minami"
    new "Я хочу побыть с Сашей и Минами"

    old "I want to be alone with [bree.name]"
    new "Я хочу остаться наедине с [bree.name]"

    old "I want to be alone with Minami"
    new "Я хочу остаться наедине с Минами"

    old "I want to be alone with Sasha"
    new "Я хочу остаться наедине с Сашей"

    old "I want to be gentle with you."
    new "Я хочу быть с тобой нежным"

    old "I want to eat something sweet"
    new "Я хочу съесть что-нибудь сладкое"

    old "I want to explore with Emma"
    new "Я хочу исследовать это вместе с Эммой"

    old "I want to go home"
    new "Я хочу домой"

    old "I want to keep you as my slave"
    new "Я хочу оставить тебя своей рабыней"

    old "I want to raise the child with you"
    new "Я хочу растить ребёнка вместе с тобой"

    old "I want to stay your slave"
    new "Я хочу остаться твоим рабом"

    old "I want you all to myself"
    new "Я хочу тебя только для себя"

    old "I want you to be mine and mine alone"
    new "Я хочу, чтобы ты принадлежала только мне"

    old "I want you to come and do it with me."
    new "Я хочу, чтобы ты пришла и сделала это со мной"

    old "I want you to stay my girlfriend"
    new "Я хочу, чтобы ты осталась моей девушкой"

    old "I want you, all of you."
    new "Я хочу тебя всю"

    old "I was bored"
    new "Мне было скучно"

    old "I was the best in my class."
    new "Я был лучшим в классе"

    old "I was waiting for a time of my choosing."
    new "Я ждал подходящего момента"

    old "I will"
    new "Я сделаю это"

    old "I will be faithful."
    new "Я буду верен"

    old "I will drop you off at the airport"
    new "Я отвезу тебя в аэропорт"

    old "I will help"
    new "Я помогу"

    old "I will leave them for you"
    new "Я оставлю их ради тебя"

    old "I will not help"
    new "Я не буду помогать"

    old "I will rough it out alone"
    new "Я переночую один"

    old "I wish I had slowed down!"
    new "Жаль, что я не остановился!"

    old "I won a eating contest"
    new "Я выиграл конкурс по поеданию еды"

    old "I won a marathon"
    new "Я выиграл марафон"

    old "I won't do that"
    new "Я не стану этого делать"

    old "I won't leave Cherie all alone"
    new "Я не оставлю Шери одну"

    old "I work enough"
    new "Я и так достаточно работаю"

    old "I would accept"
    new "Я бы согласился"

    old "I would enjoy fucking you again"
    new "Я бы с удовольствием снова тебя трахнул"

    old "I would like that"
    new "Мне бы этого хотелось"

    old "I would love to do that"
    new "Я бы с удовольствием"

    old "I would love to do whatever you want."
    new "Я с удовольствием сделаю всё, что ты захочешь"

    old "I would obey"
    new "Я бы подчинился"

    old "I wouldn't hire her"
    new "Я бы её не нанял"

    old "I'd check my schedule"
    new "Я бы сверился с расписанием"

    old "I'd like a coffee"
    new "Я бы хотел кофе"

    old "I'd love that"
    new "Я бы с удовольствием"

    old "I'd love to"
    new "С удовольствием"

    old "I'd never!"
    new "Я бы никогда!"

    old "I'd prefer to go at your place"
    new "Я бы предпочёл пойти к тебе"

    old "I'd rather do something else"
    new "Я бы предпочёл заняться чем-нибудь другим"

    old "I'd rather get the BJ."
    new "Я бы предпочёл минет"

    old "I'd rather see more of the famous model."
    new "Я бы предпочёл увидеть больше знаменитой модели"

    old "I'd rather you not wear them"
    new "Я бы предпочёл, чтобы ты их не носила"

    old "I'll apologize when you stop being a bitch"
    new "Я извинюсь, когда ты перестанешь быть сучкой"

    old "I'll ask [bree.name] about the tour."
    new "Я спрошу [bree.name] насчёт экскурсии"

    old "I'll be back with the money"
    new "Я вернусь с деньгами"

    old "I'll be there Detective."
    new "Я буду там, детектив"

    old "I'll be there."
    new "Я буду там"

    old "I'll buy"
    new "Я заплачу"

    old "I'll buy the first round"
    new "Я оплачу первый раунд"

    old "I'll deal with her later."
    new "Я разберусь с ней позже"

    old "I'll deal with them later."
    new "Я разберусь с ними позже"

    old "I'll do them later"
    new "Я сделаю это позже"

    old "I'll do what I want."
    new "Я буду делать что хочу"

    old "I'll help"
    new "Я помогу"

    old "I'll help but you'd better pay up"
    new "Я помогу, но тебе придётся заплатить"

    old "I'll help you"
    new "Я тебе помогу"

    old "I'll help you pay for it"
    new "Я помогу тебе заплатить"

    old "I'll help... for a kiss"
    new "Я помогу... за поцелуй"

    old "I'll keep that in mind!"
    new "Я это запомню!"

    old "I'll let this to you two"
    new "Оставлю это вам двоим"

    old "I'll make some space"
    new "Я освобожу немного места"

    old "I'll make sure you're not alone"
    new "Я позабочусь, чтобы ты не осталась одна"

    old "I'll pass"
    new "Я пропущу"

    old "I'll pay"
    new "Я заплачу"

    old "I'll protect you"
    new "Я тебя защищу"

    old "I'll search"
    new "Я поищу"

    old "I'll see if Sasha is interested."
    new "Я спрошу, интересно ли это Саше"

    old "I'll send it"
    new "Я отправлю"

    old "I'll sort something out."
    new "Я что-нибудь придумаю"

    old "I'll take responsibility"
    new "Я возьму ответственность на себя"

    old "I'll take us to legendary status"
    new "Я приведу нас к статусу легенд"

    old "I'll think about it"
    new "Я подумаю"

    old "I'll wait!"
    new "Я подожду!"

    old "I'm a little stressed today"
    new "Сегодня я немного напряжён"

    old "I'm a Vegan"
    new "Я веган"

    old "I'm content"
    new "Меня всё устраивает"

    old "I'm disgusted by the kiss"
    new "Меня отвращает поцелуй"

    old "I'm doing the training"
    new "Я прохожу тренировку"

    old "I'm done with you"
    new "С тобой покончено"

    old "I'm down with that"
    new "Меня это устраивает"

    old "I'm glad you like it"
    new "Я рад, что тебе нравится"

    old "I'm great at it"
    new "У меня это отлично получается"

    old "I'm happy that it pleases you"
    new "Я рад, что тебе понравилось"

    old "I'm her tag-team partner"
    new "Я её напарник по команде"

    old "I'm holding out for you"
    new "Я жду именно тебя"

    old "I'm impressed!"
    new "Я впечатлён!"

    old "I'm in"
    new "Я в деле"

    old "I'm in love with her"
    new "Я влюблён в неё"

    old "I'm interested"
    new "Мне интересно"

    old "I'm just kidding, I didn't mean to upset you"
    new "Я просто пошутил, не хотел тебя расстраивать"

    old "I'm no good at this shit either!"
    new "Я тоже ни черта в этом не понимаю!"

    old "I'm not as into anime as you are"
    new "Я не так увлекаюсь аниме, как ты"

    old "I'm not in the mood."
    new "Я не в настроении"

    old "I'm not into this kind of stuff"
    new "Мне такое не нравится"

    old "I'm not really interested"
    new "Мне это не особо интересно"

    old "I'm not sure"
    new "Я не уверен"

    old "I'm not sure..."
    new "Я не уверен..."

    old "I'm ok"
    new "Со мной всё нормально"

    old "I'm out of here."
    new "Я ухожу"

    old "I'm playing with Samantha"
    new "Я играю с Самантой"

    old "I'm playing with Sasha"
    new "Я играю с Сашей"

    old "I'm quite busy right now"
    new "Я сейчас довольно занят"

    old "I'm ready"
    new "Я готов"

    old "I'm serious, get out"
    new "Я серьёзно, уходи"

    old "I'm sorry"
    new "Прости"

    old "I'm sorry."
    new "Прости"

    old "I'm sure you can think of something to do."
    new "Уверен, ты найдёшь, чем заняться"

    old "I'm too tired"
    new "Я слишком устал"

    old "I'm up for a blowjob"
    new "Я не против минета"

    old "I'm up for a sandwich"
    new "Я не против сэндвича"

    old "I'm worried this is going to hurt her"
    new "Я боюсь, что это причинит ей боль"

    old "I've changed my mind"
    new "Я передумал"

    old "I've got other plans."
    new "У меня другие планы"

    old "IANQIN, Jannes Holtkamp, Barismati, greenarrow25,"
    new "IANQIN, Jannes Holtkamp, Barismati, greenarrow25,"

    old "Icy Raptor, Mateo Brewer, Lahteu, Kenov, Toobaa, Spiffle,"
    new "Icy Raptor, Mateo Brewer, Lahteu, Kenov, Toobaa, Spiffle,"

    old "If it keeps your career going..."
    new "Если это поможет твоей карьере..."

    old "If that is what you want, then yes!"
    new "Если ты этого хочешь, тогда да!"

    old "If you need help, you can visit the game's wiki page for detailed information and tips."
    new "Если вам нужна помощь, посетите вики-страницу игры с подробной информацией и советами."

    old "If your reach a timeout, try manual authentication"
    new "Если истечёт время ожидания, попробуйте ручную авторизацию"

    old "Ignore"
    new "Игнорировать"

    old "Ignore Aletta"
    new "Проигнорировать Алетту"

    old "Ignore Audrey"
    new "Проигнорировать Одри"

    old "Ignore Camila"
    new "Проигнорировать Камилу"

    old "Ignore her"
    new "Проигнорировать её"

    old "Ignore him"
    new "Проигнорировать его"

    old "Ignore it"
    new "Проигнорировать"

    old "Ignore Lavish"
    new "Проигнорировать Лавиш"

    old "Ignore Shiori"
    new "Проигнорировать Сиори"

    old "Ignore the ball and walk on"
    new "Проигнорировать мяч и идти дальше"

    old "Ignore the voices"
    new "Проигнорировать голоса"

    old "Ignore your tiredness and keep on going"
    new "Проигнорировать усталость и продолжить"

    old "Ignores the exception, allowing you to continue."
    new "Игнорирует исключение и позволяет продолжить."

    old "Ignores the exception, allowing you to continue. This often leads to additional errors."
    new "Игнорирует исключение и позволяет продолжить. Это часто приводит к дополнительным ошибкам."

    old "Image [index] of [count] locked."
    new "Изображение [index] из [count] закрыто."

    old "Imagine getting to know her"
    new "Представить, как узнаёшь её ближе"

    old "Imagine her sucking you off"
    new "Представить, как она отсасывает"

    old "Immersive"
    new "Иммерсивно"

    old "Import DLC file"
    new "Импортировать файл DLC"

    old "Impress the lady by telling her you're here with your kids"
    new "Впечатлить даму, сказав, что ты здесь со своими детьми"

    old "In fact, yes"
    new "Вообще-то да"

    old "In general"
    new "В целом"

    old "In the Zone"
    new "«В зоне»"

    old "Inappropriate"
    new "Неуместно"

    old "increase"
    new "больше"

    old "Increase dominance"
    new "Повысить властность"

    old "Increase girl attraction"
    new "Повысить влечение к девушкам"

    old "Increase submissiveness"
    new "Повысить покорность"

    old "Indulge Lexi"
    new "Побаловать Лекси"

    old "Injured for [game.timers.injured] day"
    new "Травмирован [game.timers.injured] день"

    old "Innocent casual"
    new "Невинный повседневный"

    old "Insist"
    new "Настоять"

    old "Insist on dancing"
    new "Настоять на танце"

    old "Insist on getting a coffee"
    new "Настоять на кофе"

    old "Insist on getting pizza"
    new "Настоять на пицце"

    old "Insist on sex"
    new "Настоять на сексе"

    old "Insist on the Coffee Shop"
    new "Настоять на кофейне"

    old "Inspirational 80s media"
    new "Вдохновляющие фильмы восьмидесятых"

    old "Insult the girls"
    new "Оскорбить девушек"

    old "Interfere"
    new "Вмешаться"

    old "Interrupt them"
    new "Прервать их"

    old "Intimidate"
    new "Запугать"

    old "Intimidate him"
    new "Запугать его"

    old "Inventory"
    new "Инвентарь"

    old "Investigate"
    new "Провести расследование"

    old "Investigate the voices"
    new "Проверить, откуда голоса"

    old "Invite [bree.name] and Anna for an 'experiment'"
    new "Пригласить [bree.name] и Анну на «эксперимент»"

    old "Invite Anna and Bree for an 'experiment'"
    new "Пригласить Анну и Бри на «эксперимент»"

    old "Invite her"
    new "Пригласить её"

    old "Invite her home"
    new "Пригласить её домой"

    old "Invite her in"
    new "Пригласить её внутрь"

    old "Invite them to your bedroom"
    new "Пригласить их в свою спальню"

    old "IronKing, ChronoMox, Uncle Yakko, Amaury Martinez,"
    new "IronKing, ChronoMox, Uncle Yakko, Amaury Martinez,"

    old "Is that a come-on?"
    new "Это подкат?"

    old "It could have used some more work."
    new "Можно было постараться больше"

    old "It didn't seem important to me."
    new "Мне это не казалось важным"

    old "It makes you beautiful"
    new "Это делает тебя красивой"

    old "It might be challenging"
    new "Это может быть сложно"

    old "It shouldn't be harder than a workout session"
    new "Это не должно быть сложнее тренировки"

    old "It was a long time ago"
    new "Это было давно"

    old "It was fun, I'm not done"
    new "Было весело, но я ещё не закончил"

    old "It was on a whim"
    new "Это было спонтанно"

    old "It was shitty"
    new "Это было дерьмово"

    old "It was simply meant to be!"
    new "Нам просто было суждено быть вместе!"

    old "It will be fine"
    new "Всё будет хорошо"

    old "It would be the best night for you"
    new "Для тебя это будет лучшая ночь"

    old "It'll be okay."
    new "Всё будет хорошо"

    old "It's a deal"
    new "Договорились"

    old "It's alright, I understand."
    new "Всё хорошо, я понимаю"

    old "It's bad for the health"
    new "Это вредно для здоровья"

    old "It's beautiful"
    new "Это прекрасно"

    old "It's better this way"
    new "Так будет лучше"

    old "It's depressing!"
    new "Это угнетает!"

    old "It's fine"
    new "Всё нормально"

    old "It's fine Hanna, you don't need to"
    new "Всё хорошо, Ханна, тебе необязательно"

    old "It's for the best"
    new "Так будет лучше"

    old "It's great"
    new "Это отлично"

    old "It's hot"
    new "Это горячо"

    old "It's inappropriate"
    new "Это неуместно"

    old "It's just dance, should be easy"
    new "Это всего лишь танец, должно быть легко"

    old "It's just noise"
    new "Это просто шум"

    old "It's Lexi"
    new "Это Лекси"

    old "It's like a second chance"
    new "Это словно второй шанс"

    old "It's like happy ever after!"
    new "Это словно «жили долго и счастливо»!"

    old "It's more complex"
    new "Это сложнее"

    old "It's not a good idea"
    new "Это плохая идея"

    old "It's not her place"
    new "Это не её место"

    old "It's not possible."
    new "Это невозможно"

    old "It's not that good"
    new "Это не так уж хорошо"

    old "It's not your business"
    new "Это не твоё дело"

    old "It's nothing..."
    new "Ничего..."

    old "It's okay Lavish, don't worry about it"
    new "Всё хорошо, Лавиш, не волнуйся"

    old "It's okay, I'm here for you"
    new "Всё хорошо, я рядом"

    old "It's the tits. And the ass."
    new "Всё из-за сисек. И задницы"

    old "It's time for your weekly training"
    new "Пришло время твоей еженедельной тренировки"

    old "It's too hard to choose one or another"
    new "Слишком трудно выбрать один из них"

    old "It's way faster this way."
    new "Так намного быстрее"

    old "It's wrong"
    new "Это неправильно"

    old "It's your choice"
    new "Это твой выбор"

    old "It's your own fault"
    new "Ты сама виновата"

    old "Its graphics drivers may be out of date or not operating correctly. This can lead to slow or incorrect graphics display."
    new "Драйверы видеокарты могут быть устаревшими или работать некорректно. Это может привести к медленному или неправильному отображению графики."

    old "J"
    new "J"

    old "j"
    new "j"

    old "Jab her in the ribs"
    new "Ткнуть её локтем в рёбра"

    old "Jack gives [bree.name] enough XP to level up"
    new "Джек даёт [bree.name] достаточно опыта для повышения уровня"

    old "Jack gives Sasha enough XP to level up"
    new "Джек даёт Саше достаточно опыта для повышения уровня"

    old "Jacob C Grooms, M, Justin Hefner, frank, Bart57070, Terry Dow,"
    new "Jacob C Grooms, M, Justin Hefner, frank, Bart57070, Terry Dow,"

    old "Jacob Pagan Thacker, LambChopSoldier, Benji, Eric Nivens,"
    new "Jacob Pagan Thacker, LambChopSoldier, Benji, Eric Nivens,"

    old "James Roberts, Eric Baughman, Liam Evans, yeah budy,"
    new "James Roberts, Eric Baughman, Liam Evans, yeah budy,"

    old "JantsoP, TheGhost, Kekesuro, Kristoffer Norgren, Purpleman,"
    new "JantsoP, TheGhost, Kekesuro, Kristoffer Norgren, Purpleman,"

    old "Jellyfish"
    new "Медузы"

    old "jimmy401, Deadsummer, Anthony Schreiber, SelimTenebris,"
    new "jimmy401, Deadsummer, Anthony Schreiber, SelimTenebris,"

    old "jmfindorff, Adam Sutor, Negativatron, Sage, Penn,"
    new "jmfindorff, Adam Sutor, Negativatron, Sage, Penn,"

    old "Joe Gillis, Jesse Moore, David Oneill, Aaron Bershell,"
    new "Joe Gillis, Jesse Moore, David Oneill, Aaron Bershell,"

    old "joeger, Valken77, Rahl, ROBERT CARR, trainblub,"
    new "joeger, Valken77, Rahl, ROBERT CARR, trainblub,"

    old "John, dominik43572, Mackenzie, kainan, Markg207 l,"
    new "John, dominik43572, Mackenzie, kainan, Markg207 l,"

    old "Johny Grimes"
    new "Johny Grimes"

    old "Join her"
    new "Присоединиться к ней"

    old "Join in"
    new "Присоединиться"

    old "Joke"
    new "Пошутить"

    old "Joke and agree"
    new "Пошутить и согласиться"

    old "JORDAN HANSEN, Nubs, BlissfulDarkness, TheBeard,"
    new "JORDAN HANSEN, Nubs, BlissfulDarkness, TheBeard,"

    old "joystick"
    new "джойстик"

    old "joystick..."
    new "джойстик..."

    old "Jump at the chance of the party"
    new "С радостью согласиться на вечеринку"

    old "Jump the queue"
    new "Пройти без очереди"

    old "Junge Yu, markg20_7, natane, Truckerguy257, Doe,"
    new "Junge Yu, markg20_7, natane, Truckerguy257, Doe,"

    old "Junk Food"
    new "Вредная еда"

    old "Just a little hair care"
    new "Просто немного ухода за волосами"

    old "Just agree"
    new "Просто согласиться"

    old "Just cum"
    new "Просто кончить"

    old "Just don't feel like it"
    new "Просто не хочется"

    old "Just fuck her"
    new "Просто трахнуть её"

    old "Just fuck them"
    new "Просто трахнуть их"

    old "Just get out!"
    new "Просто убирайся!"

    old "Just go on"
    new "Просто продолжить"

    old "Just keep watching"
    new "Просто продолжать смотреть"

    old "Just leave"
    new "Просто уйти"

    old "Just look"
    new "Просто смотреть"

    old "Just piss off"
    new "Просто отвали"

    old "Just roommates."
    new "Просто соседи"

    old "Just say hi"
    new "Просто поздороваться"

    old "Just watch"
    new "Просто смотреть"

    old "Just you"
    new "Только ты"

    old "K"
    new "K"

    old "k"
    new "k"

    old "kathrynne, Christianweg, Toedkest, Mikey Boy, Blazedsteelwolf,"
    new "kathrynne, Christianweg, Toedkest, Mikey Boy, Blazedsteelwolf,"

    old "Keep calm"
    new "Сохранять спокойствие"

    old "Keep going"
    new "Продолжить"

    old "Keep it clean"
    new "Не переходить границы"

    old "Keep quiet"
    new "Промолчать"

    old "Keep quiet and watch"
    new "Молчать и наблюдать"

    old "Keep some space between each other"
    new "Сохранять дистанцию"

    old "Keep spanking"
    new "Продолжать шлёпать"

    old "Keep the contacts in to match Luca's brown eyes"
    new "Оставить линзы, чтобы глаза совпадали с карими глазами Луки"

    old "Keep the footage as leverage"
    new "Сохранить запись как рычаг давления"

    old "Keep the kiss innocent"
    new "Оставить поцелуй невинным"

    old "Keep the pace"
    new "Сохранять темп"

    old "Keep things clean and wholesome"
    new "Сохранить всё приличным и невинным"

    old "Keep things respectful"
    new "Вести себя уважительно"

    old "Keep watching"
    new "Продолжать смотреть"

    old "Keep watching."
    new "Продолжать смотреть"

    old "Keep your mouth shut"
    new "Держать рот на замке"

    old "Kerning"
    new "Кёрнинг"

    old "Kevin Kirk, José Luis Velasco, The Hoax Reality,"
    new "Kevin Kirk, José Luis Velasco, The Hoax Reality,"

    old "KEYBOARD"
    new "КЛАВИАТУРА"

    old "Kick her out"
    new "Выгнать её"

    old "Kiss Aletta"
    new "Поцеловать Алетту"

    old "Kiss Audrey"
    new "Поцеловать Одри"

    old "Kiss Cherie"
    new "Поцеловать Шери"

    old "Kiss Harmony one last time"
    new "В последний раз поцеловать Хармони"

    old "Kiss her"
    new "Поцеловать её"

    old "Kiss her belly"
    new "Поцеловать её живот"

    old "Kiss her belly."
    new "Поцеловать её живот"

    old "Kiss her to break the ice"
    new "Поцеловать её, чтобы разрядить обстановку"

    old "Kiss Lavish"
    new "Поцеловать Лавиш"

    old "Kiss Shiori"
    new "Поцеловать Сиори"

    old "Kjkjmulo, Dark-Oshigan, wrenCali, Mirko B, Jin and Dan"
    new "Kjkjmulo, Dark-Oshigan, wrenCali, Mirko B, Jin and Dan"

    old "Knock"
    new "Постучать"

    old "Knock on doors with Kanta"
    new "Ходить по домам вместе с Кантой"

    old "Knock on the door"
    new "Постучать в дверь"

    old "Ko Clover as Kleio"
    new "Ko Clover — Клео"

    old "Kogan Sheda, Jason Miller, Phazonmasher, Alric darkflame,"
    new "Kogan Sheda, Jason Miller, Phazonmasher, Alric darkflame,"

    old "KumBomb as Cassidy"
    new "KumBomb — Кэссиди"

    old "Kylie! Shut up!"
    new "Кайли! Заткнись!"

    old "Kylie's crazy"
    new "Кайли ненормальная"

    old "Kylie, I'm disappointed"
    new "Кайли, я разочарован"

    old "L"
    new "L"

    old "l"
    new "l"

    old "LadyELiseVA as Minami"
    new "LadyELiseVA — Минами"

    old "LadyJem as Sasha"
    new "LadyJem — Саша"

    old "Lamp"
    new "Лампа"

    old "Language [text]"
    new "Язык [text]"

    old "Lash out"
    new "Взорваться"

    old "Last Name: "
    new "Фамилия:"

    old "Laugh"
    new "Рассмеяться"

    old "Laugh anyway"
    new "Всё равно рассмеяться"

    old "Laugh at the situation"
    new "Посмеяться над ситуацией"

    old "Laugh in surprise"
    new "Рассмеяться от удивления"

    old "Laugh it off"
    new "Отшутиться"

    old "Laugh off Kylie's comments"
    new "Отшутиться от комментариев Кайли"

    old "Laugh off Morgan being late"
    new "Отшутиться от опоздания Морган"

    old "Lavish"
    new "Lavish"

    old "Lavish should not wear her sexy uniform anymore"
    new "Лавиш больше не должна носить сексуальную униформу"

    old "Lavish should put her bottom back on"
    new "Лавиш должна снова надевать низ"

    old "Lavish should put her top back"
    new "Лавиш должна снова надевать верх"

    old "Lavish should put her uniform back"
    new "Лавиш должна снова надевать униформу"

    old "Lavish should remove her bottoms at work"
    new "Лавиш должна снимать низ на работе"

    old "Lavish should remove her top at work"
    new "Лавиш должна снимать верх на работе"

    old "Lavish should remove her uniform at work"
    new "Лавиш должна снимать униформу на работе"

    old "Lavish should wear her sexy uniform"
    new "Лавиш должна носить свою сексуальную униформу"

    old "Lay her on the couch"
    new "Уложить её на диван"

    old "Lead her on"
    new "Подогревать её интерес"

    old "Lean into the accidental kiss"
    new "Ответить на случайный поцелуй"

    old "Leap aside"
    new "Отпрыгнуть в сторону"

    old "Leave"
    new "Уйти"

    old "Leave her alone"
    new "Оставить её в покое"

    old "Leave immediately"
    new "Немедленно уйти"

    old "Leave it"
    new "Оставить как есть"

    old "Leave it to the girl to see him off"
    new "Позволить девушке прогнать его"

    old "Leave quietly"
    new "Тихо уйти"

    old "Leave the mall"
    new "Уйти из торгового центра"

    old "Left"
    new "Слева"

    old "LEFT CLICK"
    new "ЛЕВАЯ КНОПКА"

    old "Left Click"
    new "Левая кнопка"

    old "Left Trigger\nLeft Shoulder"
    new "Левый триггер\nЛевый бампер"

    old "Lesbian porn"
    new "Лесбийское порно"

    old "Let [bree.name] choose"
    new "Позволить [bree.name] выбрать"

    old "Let [bree.name] know what she's responsible for"
    new "Объяснить [bree.name], за что она отвечает"

    old "Let [bree.name] stay"
    new "Позволить [bree.name] остаться"

    old "Let Aletta stay"
    new "Позволить Алетте остаться"

    old "Let Audrey have her way"
    new "Позволить Одри сделать по-своему"

    old "Let Ayesha defend you"
    new "Позволить Айше защитить тебя"

    old "Let Ayesha pick up the tab"
    new "Позволить Айше оплатить счёт"

    old "Let Ayesha put Kylie in her place"
    new "Позволить Айше поставить Кайли на место"

    old "Let Ayesha use Kylie"
    new "Позволить Айше использовать Кайли"

    old "Let go"
    new "Отпустить"

    old "Let Hanna keep the drink"
    new "Позволить Ханне оставить напиток"

    old "Let Harmony meet Angela"
    new "Позволить Хармони встретиться с Анджелой"

    old "Let her"
    new "Позволить ей"

    old "Let Her Be Happy"
    new "Позволить ей радоваться"

    old "Let her be on top"
    new "Позволить ей быть сверху"

    old "Let her buy the first round"
    new "Позволить ей купить первый раунд"

    old "Let her check"
    new "Позволить ей проверить"

    old "Let her continue"
    new "Позволить ей продолжать"

    old "Let her control the pace"
    new "Позволить ей задавать темп"

    old "Let her cry"
    new "Позволить ей выплакаться"

    old "Let her do her thing"
    new "Позволить ей делать своё дело"

    old "Let her finish"
    new "Позволить ей закончить"

    old "Let her go"
    new "Отпустить её"

    old "Let her go down on me"
    new "Позволить ей отсосать"

    old "Let her have her birthday fun"
    new "Позволить ей повеселиться в день рождения"

    old "Let her have some control"
    new "Позволить ей немного контролировать"

    old "Let her in"
    new "Впустить её"

    old "Let her keep doing it"
    new "Позволить ей продолжать"

    old "Let her keep talking"
    new "Позволить ей продолжать говорить"

    old "Let her lead"
    new "Позволить ей вести"

    old "Let her leave"
    new "Позволить ей уйти"

    old "Let her sleep"
    new "Позволить ей спать"

    old "Let her stay"
    new "Позволить ей остаться"

    old "Let her stay formal"
    new "Позволить ей сохранять формальность"

    old "Let her suck you"
    new "Позволить ей отсосать"

    old "Let her suck you off"
    new "Позволить ей отсосать"

    old "Let her take her time"
    new "Позволить ей не спешить"

    old "Let her talk"
    new "Дать ей высказаться"

    old "Let her win, it's her birthday after all"
    new "Позволить ей победить, всё-таки у неё день рождения"

    old "Let him cum inside"
    new "Позволить ему кончить внутрь"

    old "Let it go"
    new "Отпустить ситуацию"

    old "Let Jeff go"
    new "Отпустить Джеффа"

    old "Let Kylie pick up the tab"
    new "Позволить Кайли оплатить счёт"

    old "Let Kylie rage at the waitress"
    new "Позволить Кайли наорать на официантку"

    old "Let Lexi take the initiative"
    new "Позволить Лекси взять инициативу"

    old "Let me handle things"
    new "Позволь мне этим заняться"

    old "Let me show you"
    new "Позволь показать"

    old "Let me think"
    new "Дай подумать"

    old "Let Minami know what she's responsible for"
    new "Объяснить Минами, за что она отвечает"

    old "Let Morgan keep me where I am"
    new "Позволить Морган удержать меня на месте"

    old "Let Morgan know I am upset at her being late"
    new "Дать Морган понять, что я злюсь из-за её опоздания"

    old "Let Samantha play with you"
    new "Позволить Саманте поиграть с тобой"

    old "Let Sasha choose"
    new "Позволить Саше выбрать"

    old "Let Sasha know what she's responsible for"
    new "Объяснить Саше, за что она отвечает"

    old "Let Shiori call the babysitter"
    new "Позволить Сиори позвонить няне"

    old "Let the Master fuck Lexi"
    new "Позволить Мастеру трахнуть Лекси"

    old "Let them 'relax' you first"
    new "Сначала позволить им «расслабить» тебя"

    old "Let them carry everything"
    new "Пусть всё несут сами"

    old "Let them settle it themselves"
    new "Позволить им разобраться самим"

    old "Let's dance"
    new "Давай потанцуем"

    old "Let's do it"
    new "Давай сделаем это"

    old "Let's do it!"
    new "Давай сделаем это!"

    old "Let's drink"
    new "Давай выпьем"

    old "Let's find out"
    new "Давай выясним"

    old "Let's get married!"
    new "Давай поженимся!"

    old "Let's go somewhere else"
    new "Давай пойдём куда-нибудь ещё"

    old "Let's grab a drink while we wait for her"
    new "Давай выпьем, пока ждём её"

    old "Let's keep the baby"
    new "Давай оставим ребёнка"

    old "Let's keep us separate from the rest."
    new "Давай не будем смешивать наши отношения с остальными"

    old "Let's meet in my room"
    new "Давай встретимся в моей комнате"

    old "Let's meet Thyra together"
    new "Давай вместе встретимся с Тирой"

    old "Let's not talk about him right now."
    new "Давай сейчас не будем о нём"

    old "Let's race again!"
    new "Давай ещё раз устроим гонку!"

    old "Let's seat"
    new "Давай сядем"

    old "Let's spice up our interactions"
    new "Давай добавим остроты в наше общение"

    old "Let's split"
    new "Давайте разделим счёт"

    old "Let's start"
    new "Давай начнём"

    old "Let's start a team review."
    new "Давайте начнём командный разбор"

    old "Let's start with a blowjob"
    new "Давай начнём с минета"

    old "Let's stay calm"
    new "Давай сохранять спокойствие"

    old "Let's talk for a minute"
    new "Давай минуту поговорим"

    old "Let's try this new peripheral"
    new "Давай попробуем эту новую периферию"

    old "Let's use those tits"
    new "Давай используем эти сиськи"

    old "Lets get a beer instead of a coffee"
    new "Предложить пиво вместо кофе"

    old "Lets Morgan know im upset at her being late"
    new "Дать Морган понять, что я злюсь из-за её опоздания"

    old "Let’s keep this our secret."
    new "Пусть это останется нашим секретом"

    old "Lexi"
    new "Lexi"

    old "Lexi will pay"
    new "Заплатит Лекси"

    old "Lexi, will you finish your plate?"
    new "Лекси, ты доешь свою порцию?"

    old "Lick"
    new "Лизать"

    old "Lick [bree.name]'s ass"
    new "Лизать задницу [bree.name]"

    old "Lick [bree.name]'s pussy"
    new "Лизать киску [bree.name]"

    old "Lick her ass"
    new "Лизать её задницу"

    old "Lick Minami's ass"
    new "Лизать задницу Минами"

    old "Lick Minami's pussy"
    new "Лизать киску Минами"

    old "Lick Sasha's ass"
    new "Лизать задницу Саши"

    old "Lick Sasha's pussy"
    new "Лизать киску Саши"

    old "Lick the ice-cream off of [bree.name]'s chest"
    new "Слизать мороженое с груди [bree.name]"

    old "Lie"
    new "Солгать"

    old "Lie and say no"
    new "Соврать и сказать «нет»"

    old "Light Boxes"
    new "Лёгкие коробки"

    old "Like a kiss?"
    new "Например, поцелуй?"

    old "Line Spacing Scaling"
    new "Масштабирование межстрочного интервала"

    old "Lingerie"
    new "Нижнее бельё"

    old "Listen at the door"
    new "Подслушать у двери"

    old "Listen to her idea"
    new "Выслушать её идею"

    old "Listen to the baby"
    new "Послушать ребёнка"

    old "Literature"
    new "Литература"

    old "LOAD"
    new "ЗАГРУЗИТЬ"

    old "Load"
    new "Загрузить"

    old "Load slot %s: [text]"
    new "Слот загрузки %s: [text]"

    old "Loading will lose unsaved progress.\nAre you sure you want to do this?"
    new "Загрузка игры приведёт к потере несохранённого прогресса.\nВы уверены, что хотите это сделать?"

    old "LOL!"
    new "ЛОЛ!"

    old "Look at [bree.name]'s dice"
    new "Посмотреть на кости [bree.name]"

    old "Look at Sasha's dice"
    new "Посмотреть на кости Саши"

    old "Look at the toys"
    new "Посмотреть на игрушки"

    old "Look Away"
    new "Отвести взгляд"

    old "Look for her"
    new "Искать её"

    old "Look for jobs"
    new "Искать работу"

    old "Look for wild animals"
    new "Поискать диких животных"

    old "Look, it's complicated"
    new "Понимаешь, всё сложно"

    old "Lose them for me."
    new "Избавься от них ради меня"

    old "Love is love"
    new "Любовь есть любовь"

    old "Love it"
    new "Обожаю"

    old "Love people"
    new "Люблю людей"

    old "Lucas Myers, BOI1234, matt, paksin689, Skaer Krowe,"
    new "Lucas Myers, BOI1234, matt, paksin689, Skaer Krowe,"

    old "LusterRose as Ryan"
    new "LusterRose — Райан"

    old "M"
    new "M"

    old "m"
    new "m"

    old "Ma Cherie, They are real!"
    new "Моя Шери, они настоящие!"

    old "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]."
    new "Создано с помощью {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]."

    old "Main Menu"
    new "Главное меню"

    old "MAIN MENU"
    new "ГЛАВНОЕ МЕНЮ"

    old "main volume"
    new "общая громкость"

    old "Make [bree.name] tackle the crab"
    new "Заставить [bree.name] разобраться с крабом"

    old "Make a scene to get the waiter's attention"
    new "Устроить сцену, чтобы привлечь внимание официанта"

    old "Make a wish"
    new "Загадать желание"

    old "Make an innuendo out of it"
    new "Превратить это в двусмысленный намёк"

    old "Make an insulting comment"
    new "Сделать оскорбительное замечание"

    old "Make Cassidy urinate in the park"
    new "Заставить Кэссиди помочиться в парке"

    old "Make fun of the fact the VIP section is so empty"
    new "Посмеяться над тем, насколько пуста VIP-зона"

    old "Make Hanna walk to heel"
    new "Заставить Ханну идти рядом"

    old "Make her"
    new "Заставить её"

    old "Make her deep throat"
    new "Заставить её взять глубже"

    old "Make her stop"
    new "Заставить её остановиться"

    old "Make her suck you off"
    new "Заставить её отсосать"

    old "Make it lewd"
    new "Сделать всё непристойным"

    old "Make sandcastles"
    new "Строить замки из песка"

    old "Make Sasha lick the ice-cream off of [bree.name]'s chest"
    new "Заставить Сашу слизать мороженое с груди [bree.name]"

    old "Make Shiori stay for the post-credit scene"
    new "Заставить Сиори остаться на сцену после титров"

    old "Make something up about a bullet wound"
    new "Придумать что-нибудь про пулевое ранение"

    old "Make something up about a cough"
    new "Придумать что-нибудь про кашель"

    old "Make something up about a war wound"
    new "Придумать что-нибудь про боевую рану"

    old "Make sure you come to pick up your stuff."
    new "Не забудь забрать свои вещи"

    old "Make the kiss heavier"
    new "Сделать поцелуй более страстным"

    old "Make up a reason"
    new "Придумать причину"

    old "Make up an excuse"
    new "Придумать оправдание"

    old "Make up an excuse not to give Kylie a tour"
    new "Придумать причину не проводить Кайли экскурсию"

    old "Makeup"
    new "Макияж"

    old "Manage"
    new "Управление"

    old "Manual authentication"
    new "Ручная авторизация"

    old "Marshmallows first!"
    new "Сначала маршмеллоу!"

    old "Martial Arts"
    new "Боевые искусства"

    old "Massage her swollen foot"
    new "Помассировать её опухшую ступню"

    old "Massage Lexi"
    new "Сделать Лекси массаж"

    old "Massage Sasha's tense muscles"
    new "Помассировать напряжённые мышцы Саши"

    old "Massma, Jonathan Santos-Rea, Pretzel Warrior,"
    new "Massma, Jonathan Santos-Rea, Pretzel Warrior,"

    old "Masturbate"
    new "Мастурбировать"

    old "Masturbate in the bathroom"
    new "Мастурбировать в туалете"

    old "Masturbate while watching her"
    new "Мастурбировать, наблюдая за ней"

    old "Max"
    new "Максимум"

    old "Max Kupriianov, brett, Joker, ramses301, Vito Scaletta,"
    new "Max Kupriianov, brett, Joker, ramses301, Vito Scaletta,"

    old "Maybe I just want to fuck your ass again"
    new "Может, я просто снова хочу трахнуть тебя в задницу"

    old "Maybe I should pace myself?"
    new "Может, стоит сбавить темп?"

    old "Maybe later"
    new "Может, позже"

    old "maylie alderete, DragonMan5, Hasten Bridges, Parkey,"
    new "maylie alderete, DragonMan5, Hasten Bridges, Parkey,"

    old "Me"
    new "Я"

    old "Me against them"
    new "Я против них"

    old "Me too"
    new "Я тоже"

    old "Meeeh..."
    new "Ну такое..."

    old "Meet [bree.name] and Kat"
    new "Встретиться с [bree.name] и Кэт"

    old "Meet Alexis and Reona for some pool fun"
    new "Встретиться с Алексис и Реоной у бассейна"

    old "Meet Alexis, Audrey and Reona for a 'hot coffee'"
    new "Встретиться с Алексис, Одри и Реоной на «горячий кофе»"

    old "Meet Anna and Kleio for a 'hot coffee'"
    new "Встретиться с Анной и Клео на «горячий кофе»"

    old "Meet Anna, Emma and Kat at the beach"
    new "Встретиться с Анной, Эммой и Кэт на пляже"

    old "Meet Anna, Kleio and Sasha for a 'hot coffee'"
    new "Встретиться с Анной, Клео и Сашей на «горячий кофе»"

    old "Meet Kleio and Anna for a 'hot coffee'"
    new "Встретиться с Клео и Анной на «горячий кофе»"

    old "Meet Kleio, Anna and Sasha for a 'hot coffee'"
    new "Встретиться с Клео, Анной и Сашей на «горячий кофе»"

    old "Meet them at the gym"
    new "Встретиться с ними в спортзале"

    old "Meh..."
    new "Ну такое..."

    old "Mess her face up"
    new "Испачкать ей лицо"

    old "Metallikea"
    new "Metallikea"

    old "Michael Johnson"
    new "Майкл Джонсон"

    old "MIDDLE CLICK"
    new "СРЕДНЯЯ КНОПКА"

    old "Middle Click"
    new "Средняя кнопка"

    old "MidnightDatura as Ayesha, Kiara & Cherie"
    new "MidnightDatura — Айша, Киара и Шери"

    old "Mighty Heimskr, Jacob Brickner, alexlycan805, Kory Davis,"
    new "Mighty Heimskr, Jacob Brickner, alexlycan805, Kory Davis,"

    old "Mike confesses how much he used to love gym class"
    new "Майк признаётся, как сильно любил физкультуру"

    old "Milky"
    new "С молоком"

    old "Minami"
    new "Minami"

    old "Mind lending a hand?"
    new "Не поможешь?"

    old "Mintea as Samantha"
    new "Mintea — Саманта"

    old "Miradessa as Hanna"
    new "Miradessa — Ханна"

    old "Missionary"
    new "Миссионерская"

    old "MissMoonified as Bree & Kylie"
    new "MissMoonified — Бри и Кайли"

    old "Mizz Peachy as Emma"
    new "Mizz Peachy — Эмма"

    old "Modest top"
    new "Скромный верх"

    old "Moka"
    new "Мокка"

    old "Mom"
    new "Мама"

    old "Mono Audio"
    new "Моно аудио"

    old "mono audio"
    new "моно аудио"

    old "More details on how to fix this can be found in the {a=[url]}documentation{/a}."
    new "Дополнительные сведения об устранении этой проблемы можно найти в {a=[url]}документации{/a}."

    old "MOUSE"
    new "МЫШЬ"

    old "Mouse Wheel Down"
    new "Колесо мыши вниз"

    old "Mouse Wheel Up"
    new "Колесо мыши вверх"

    old "Movie Theatre"
    new "Кинотеатр"

    old "Mr What, Akanan, Nexus, Juliann Lardeux, Bay McClendon,"
    new "Mr What, Akanan, Nexus, Juliann Lardeux, Bay McClendon,"

    old "Mufti300, Alex Bennett, Warqueen, SoftEis,"
    new "Mufti300, Alex Bennett, Warqueen, SoftEis,"

    old "Muramasa Manamune, Josh Wong, Nicholas Sheard,"
    new "Muramasa Manamune, Josh Wong, Nicholas Sheard,"

    old "MUSIC"
    new "МУЗЫКА"

    old "music volume"
    new "громкость музыки"

    old "Mute alarm clock"
    new "Будильник"

    old "Mute all"
    new "Весь звук"

    old "mute all"
    new "режим без звука"

    old "Mute all characters"
    new "Всех персонажей"

    old "Mute Bree"
    new "Выключить Бри"

    old "mute main"
    new "режим без звука"

    old "Mute Mike"
    new "Выключить Майка"

    old "mute music"
    new "без музыки"

    old "mute sound"
    new "без звуков"

    old "mute voice"
    new "без голоса"

    old "Mutkamuikkunen, Manuel, Marcos Barrera, Mh1334, Mikax, qfa,"
    new "Mutkamuikkunen, Manuel, Marcos Barrera, Mh1334, Mikax, qfa,"

    old "My place"
    new "У меня"

    old "Myself"
    new "Себя"

    old "N"
    new "N"

    old "n"
    new "n"

    old "Nah defence is for losers. Swing that sword"
    new "Не-а, защита для неудачников. Размахивай мечом"

    old "Nah! I got this, easy!"
    new "Не-а! Я справлюсь, легко!"

    old "Nah, that doesn't sound like a good idea."
    new "Не-а, звучит как плохая идея"

    old "Naked"
    new "Голая"

    old "Nanaimo Kobayashi, Karn, Gerson Velasquez, david whoo,"
    new "Nanaimo Kobayashi, Karn, Gerson Velasquez, david whoo,"

    old "NARRATIVE DIRECTOR"
    new "РУКОВОДИТЕЛЬ СЮЖЕТА"

    old "Nate Walis, Devious Dingbat, Waking Dreamland, Tik Tik,"
    new "Nate Walis, Devious Dingbat, Waking Dreamland, Tik Tik,"

    old "Nate, Jacory Hammock, W1HOLESALE, June117, Woolfell,"
    new "Nate, Jacory Hammock, W1HOLESALE, June117, Woolfell,"

    old "Navigate the interface."
    new "Навигация по интерфейсу"

    old "NemoMeow, KKGG DARKS, Darthzack566, Kenodoxia,"
    new "NemoMeow, KKGG DARKS, Darthzack566, Kenodoxia,"

    old "Never mind"
    new "Неважно"

    old "next"
    new "след"

    old "Next Day"
    new "Следующий день"

    old "Next file page."
    new "Следующая страница сохранений"

    old "Next Hour"
    new "Следующий час"

    old "Next locations"
    new "Следующие места"

    old "Nicky suits it"
    new "Ники ему подходит"

    old "Nico"
    new "Nico"

    old "Nicolas Mai phung, Ouron, Armando Sapien, Jack Sparling,"
    new "Nicolas Mai phung, Ouron, Armando Sapien, Jack Sparling,"

    old "No"
    new "Нет"

    old "NO"
    new "НЕТ"

    old "No (Never meet Alexis again)"
    new "Нет (больше никогда не встречаться с Алексис)"

    old "No (Never meet Shiori again)"
    new "Нет (больше никогда не встречаться с Сиори)"

    old "No animals!"
    new "Никаких животных!"

    old "No bears or sharks of any kind were hurt during the making of this game."
    new "При создании игры ни один медведь или акула не пострадали."

    old "No fucking way!!!"
    new "Ни за что, блядь!!!"

    old "No Gamepads Available"
    new "Доступные геймпады не найдены"

    old "No it's fine!"
    new "Нет, всё хорошо!"

    old "No need for violence!"
    new "Насилие ни к чему!"

    old "No problem here"
    new "Здесь всё нормально"

    old "No promises, then"
    new "Тогда без обещаний"

    old "No really, no"
    new "Нет, правда, нет"

    old "No thanks"
    new "Нет, спасибо"

    old "No thanks."
    new "Нет, спасибо"

    old "No tip"
    new "Без чаевых"

    old "No update methods found."
    new "Не найдено ни одного метода обновления."

    old "No vibrator"
    new "Без вибратора"

    old "No Way"
    new "Ни за что"

    old "No way"
    new "Ни за что"

    old "No way girl, I'm not paying"
    new "Ни за что, девочка, я не плачу"

    old "No way!"
    new "Ни за что!"

    old "NO WAY!!"
    new "НИ ЗА ЧТО!!"

    old "No!"
    new "Нет!"

    old "No! You can't!"
    new "Нет! Ты не можешь!"

    old "No, but I don't need anyone."
    new "Нет, но мне никто не нужен"

    old "No, don't go!"
    new "Нет, не уходи!"

    old "No, fuck off"
    new "Нет, отвали"

    old "No, I don't"
    new "Нет"

    old "No, I don't see you that way"
    new "Нет, я не воспринимаю тебя так"

    old "No, it's adorable"
    new "Нет, это мило"

    old "No, no way, never!"
    new "Нет, ни за что, никогда!"

    old "No, not playing that game"
    new "Нет, я не буду в это играть"

    old "No, not worth it"
    new "Нет, оно того не стоит"

    old "No, nothing..."
    new "Нет, ничего..."

    old "No, thank you."
    new "Нет, спасибо"

    old "No, you belong to me"
    new "Нет, ты принадлежишь мне"

    old "No, you weren't"
    new "Нет, не была"

    old "No. I'm exhausted."
    new "Нет. Я вымотан"

    old "Nobody"
    new "Никто"

    old "Nobody could"
    new "Никто не смог бы"

    old "None"
    new "Нет"

    old "Nonsense"
    new "Чушь"

    old "Nope"
    new "Не-а"

    old "Nope!"
    new "Не-а!"

    old "Nope."
    new "Не-а"

    old "Nope. Just you!"
    new "Нет. Только ты!"

    old "Normal"
    new "Нормально"

    old "Not a chance"
    new "Ни за что"

    old "Not as hot as you"
    new "Не горячее тебя"

    old "Not as low as they were."
    new "Не так низко, как раньше"

    old "Not bad"
    new "Неплохо"

    old "Not for me"
    new "Не для меня"

    old "Not in this house"
    new "Только не в этом доме"

    old "Not interested"
    new "Не интересно"

    old "Not interested (Never meet Emma again)"
    new "Не интересно (больше никогда не встречаться с Эммой)"

    old "Not me"
    new "Не я"

    old "Not much"
    new "Не особо"

    old "Not now"
    new "Не сейчас"

    old "Not really"
    new "Не особо"

    old "Not right now"
    new "Не сейчас"

    old "Not sorry!"
    new "Не жалею!"

    old "Not sure that's a good idea"
    new "Не уверен, что это хорошая идея"

    old "Not yet"
    new "Пока нет"

    old "Not your business"
    new "Не твоё дело"

    old "Nothing"
    new "Ничего"

    old "Now this, Fynn Stephan, Moroyrii, Steward Sosn, Royce Wiens,"
    new "Now this, Fynn Stephan, Moroyrii, Steward Sosn, Royce Wiens,"

    old "Npc"
    new "Персонажи"

    old "Nursing"
    new "Сестринское дело"

    old "Nutflix and Chill"
    new "Nutflix и расслабон"

    old "O"
    new "O"

    old "o"
    new "o"

    old "Obey"
    new "Подчиниться"

    old "Object"
    new "Возразить"

    old "Of course"
    new "Конечно"

    old "Of course I am"
    new "Конечно"

    old "Of course not"
    new "Конечно нет"

    old "Of course you can"
    new "Конечно, можешь"

    old "Of course you can come!"
    new "Конечно, можешь прийти!"

    old "Of course!"
    new "Конечно!"

    old "Of course, my love"
    new "Конечно, любовь моя"

    old "Off"
    new "Выключить"

    old "Offer a new picture of you"
    new "Предложить новую фотографию себя"

    old "Offer Aletta"
    new "Предложить Алетту"

    old "Offer all three"
    new "Предложить всех троих"

    old "Offer an amp"
    new "Предложить усилитель"

    old "Offer an old picture of you"
    new "Предложить старую фотографию себя"

    old "Offer Audrey"
    new "Предложить Одри"

    old "Offer blue panties"
    new "Предложить синие трусики"

    old "Offer cunnilingus"
    new "Предложить кунилингус"

    old "Offer drugs"
    new "Предложить наркотики"

    old "Offer ear-plugs"
    new "Предложить беруши"

    old "Offer gym clothes"
    new "Предложить спортивную одежду"

    old "Offer Harmony an alternate moral to the story"
    new "Предложить Хармони другую мораль этой истории"

    old "Offer her your coat"
    new "Предложить ей своё пальто"

    old "Offer Lavish"
    new "Предложить Лавиш"

    old "Offer light clothes"
    new "Предложить лёгкую одежду"

    old "Offer more help"
    new "Предложить ещё помощь"

    old "Offer Shiori"
    new "Предложить Сиори"

    old "Offer Shiori a drink"
    new "Предложить Сиори выпить"

    old "Offer some meat"
    new "Предложить мясо"

    old "Offer style clothes"
    new "Предложить стильную одежду"

    old "Offer to back off"
    new "Предложить отступить"

    old "Offer to buy the next round"
    new "Предложить оплатить следующий раунд"

    old "Offer to cover her rent"
    new "Предложить оплатить её аренду"

    old "Offer to cover the bill"
    new "Предложить оплатить счёт"

    old "Offer to give her a massage"
    new "Предложить ей массаж"

    old "Offer to help"
    new "Предложить помощь"

    old "Offer to pick up the bill"
    new "Предложить оплатить счёт"

    old "Offer warm clothes"
    new "Предложить тёплую одежду"

    old "Offer white panties"
    new "Предложить белые трусики"

    old "Office window"
    new "Офисное окно"

    old "Oh I've got to see this"
    new "О, это я должен увидеть"

    old "Oh no, I've waited forever for this..."
    new "О нет, я так долго этого ждал..."

    old "Oh, I'll call!"
    new "О, я позвоню!"

    old "Ok"
    new "Ладно"

    old "Okay"
    new "Ладно"

    old "Okay you've had your fun"
    new "Ладно, ты уже повеселилась"

    old "Okay, I'll do it"
    new "Ладно, я это сделаю"

    old "Okay, no more porn"
    new "Ладно, больше никакого порно"

    old "Okay, no porn"
    new "Ладно, никакого порно"

    old "Okay, teach me!"
    new "Ладно, научи меня!"

    old "Okay, that's hot"
    new "Ладно, это горячо"

    old "Okay."
    new "Ладно"

    old "Okay. Next time?"
    new "Ладно. В следующий раз?"

    old "OmegaT"
    new "OmegaT"

    old "On"
    new "Вкл."

    old "On it Officer"
    new "Уже делаю, офицер"

    old "On your knees, bitch"
    new "На колени, сучка"

    old "One and a half direction"
    new "One and a half direction"

    old "One more try"
    new "Ещё одна попытка"

    old "Only because it's you then"
    new "Только потому, что это ты"

    old "Only grown ups now? Great!"
    new "Остались только взрослые? Отлично!"

    old "Only if you want to"
    new "Только если сама хочешь"

    old "Open"
    new "Открыть"

    old "Open [text] directory."
    new "Открыть папку [text]."

    old "open cheat screen"
    new "открыть меню читов"

    old "Open the door"
    new "Открыть дверь"

    old "Open web wiki"
    new "Открыть веб-вики"

    old "Opendyslexic"
    new "Opendyslexic"

    old "Opens a console to allow debugging the problem."
    new "Открывает консоль для отладки проблемы."

    old "Opens the accessibility menu."
    new "Открывает меню специальных возможностей"

    old "Opens the traceback.txt file in a text editor."
    new "Открывает файл traceback.txt в текстовом редакторе."

    old "Oppose"
    new "Выступить против"

    old "OPTION"
    new "НАСТРОЙКИ"

    old "OPTIONS"
    new "НАСТРОЙКИ"

    old "Oral"
    new "Оральные ласки"

    old "Order another round"
    new "Заказать ещё по кругу"

    old "Order beers"
    new "Заказать пиво"

    old "Order food"
    new "Заказать еду"

    old "Order fruity cocktails"
    new "Заказать фруктовые коктейли"

    old "Order seafood"
    new "Заказать морепродукты"

    old "Order something adventurous"
    new "Заказать что-нибудь необычное"

    old "Order something for everyone"
    new "Заказать что-нибудь для всех"

    old "Order something safe"
    new "Заказать что-нибудь привычное"

    old "Order spirits"
    new "Заказать крепкий алкоголь"

    old "Order steak"
    new "Заказать стейк"

    old "Order tap water"
    new "Заказать воду из-под крана"

    old "Order wine"
    new "Заказать вино"

    old "Other way around"
    new "Наоборот"

    old "Outcome"
    new "Результат"

    old "Outdo Scottie"
    new "Превзойти Скотти"

    old "Outside of work"
    new "Вне работы"

    old "Override voice"
    new "Заменить голос"

    old "Own it"
    new "Признать это"

    old "P"
    new "P"

    old "p"
    new "p"

    old "PAGE DOWN"
    new "PAGE DOWN"

    old "Page Down"
    new "Page Down"

    old "PAGE UP"
    new "PAGE UP"

    old "Page Up"
    new "Page Up"

    old "Page {}"
    new "Страница {}"

    old "Palla stands up and gives me a wink as she steps away from the bar."
    new "Палла встаёт и подмигивает мне, отходя от бара"

    old "Paradoxal Deviant"
    new "Paradoxal Deviant"

    old "Parsing the script failed."
    new "Не удалось разобрать сценарий."

    old "Partying"
    new "Вечеринки"

    old "Pass"
    new "Отказаться"

    old "Pass for this time"
    new "На этот раз пропустить"

    old "Pass on dancing"
    new "Отказаться от танца"

    old "Passing a crowd to take it to a famous store"
    new "Провести её через толпу к известному магазину"

    old "Pasta"
    new "Паста"

    old "Paste the authentication token here"
    new "Вставьте сюда токен аутентификации"

    old "Pay"
    new "Заплатить"

    old "Pay for her order"
    new "Оплатить её заказ"

    old "Pay the Fee"
    new "Заплатить взнос"

    old "Peek inside"
    new "Заглянуть внутрь"

    old "Pelvis Resley"
    new "Пелвис Ресли"

    old "Performance Warning"
    new "Предупреждение о производительности"

    old "Persuade"
    new "Убедить"

    old "Pet the dog"
    new "Погладить собаку"

    old "Peter Pham, Jake Bilodeau, Lucifer Seraphim, Libertas90,"
    new "Peter Pham, Jake Bilodeau, Lucifer Seraphim, Libertas90,"

    old "Pick up the bill"
    new "Оплатить счёт"

    old "Picking up chicks"
    new "Знакомства с девушками"

    old "Piercing"
    new "Пирсинг"

    old "Piercings"
    new "Пирсинг"

    old "Piledriver"
    new "Пайлдрайвер"

    old "Piss off!"
    new "Отвали!"

    old "Pizza"
    new "Пицца"

    old "Play along"
    new "Подыграть"

    old "Play at the nightclub"
    new "Играть в ночном клубе"

    old "Play at the pub"
    new "Играть в пабе"

    old "Play at the thunderdome"
    new "Играть в «Громовом куполе»"

    old "Play dressed"
    new "Играть одетым"

    old "Play dumb"
    new "Прикинуться дураком"

    old "Play fetch with Hanna"
    new "Поиграть с Ханной в апорт"

    old "Play guitar"
    new "Поиграть на гитаре"

    old "Play in the sea"
    new "Поиграть в море"

    old "Play it cool"
    new "Вести себя невозмутимо"

    old "Play it down"
    new "Не придавать значения"

    old "Play it straight down the line"
    new "Держаться строго по делу"

    old "Play naked"
    new "Играть голым"

    old "Play peacemaker"
    new "Попытаться всех примирить"

    old "Play the guitar"
    new "Сыграть на гитаре"

    old "Play volleyball"
    new "Поиграть в волейбол"

    old "Play with [bree.name]"
    new "Поиграть с [bree.name]"

    old "Play with her ass"
    new "Поиграть с её задницей"

    old "Play with Kleio"
    new "Поиграть с Клео"

    old "Play with the piercing"
    new "Поиграть с пирсингом"

    old "Playing guitar"
    new "Игра на гитаре"

    old "Playing with this save will lead to errors."
    new "Использование этого сохранения приведёт к ошибкам."

    old "Plead Kylie's insanity"
    new "Сослаться на невменяемость Кайли"

    old "Plead to keep the baby"
    new "Умолять оставить ребёнка"

    old "Please don't do that"
    new "Пожалуйста, не делай этого"

    old "Please enter the sync ID you generated.\nNever enter a sync ID you didn't create yourself."
    new "Введите созданный вами Sync ID.\nНикогда не вводите Sync ID, который вы не создавали сами."

    old "Please take the drink"
    new "Пожалуйста, возьми напиток"

    old "portal_environment:"
    new "среда портала:"

    old "portal_environment: [persistent.portal_environment]"
    new "среда портала: [persistent.portal_environment]"

    old "Power metal is the metal of metal"
    new "Пауэр-метал — самый металлический метал"

    old "Powersave"
    new "Энергосбережение"

    old "Praise Ayesha's performance"
    new "Похвалить выступление Айши"

    old "Praise Sasha when she gets home"
    new "Похвалить Сашу, когда она вернётся домой"

    old "Preferences"
    new "Настройки"

    old "Preparing to download the game data."
    new "Подготовка к загрузке данных игры."

    old "Preparing to download the updates."
    new "Подготовка к загрузке обновлений."

    old "Press on"
    new "Продолжить давить"

    old "Press or move the '[control!s]' [kind]."
    new "Нажмите или переместите элемент «[control!s]» ([kind])."

    old "Pretend not to notice what she is doing"
    new "Сделать вид, что не замечаешь, что она делает"

    old "Pretend she's yours"
    new "Представить, что она твоя"

    old "Pretty attractive."
    new "Довольно привлекательная"

    old "prev"
    new "пред"

    old "Previous file page."
    new "Предыдущая страница сохранений"

    old "Proceed"
    new "Продолжить"

    old "PROJECT LEADER"
    new "РУКОВОДИТЕЛЬ ПРОЕКТА"

    old "Propose an alternative to the show"
    new "Предложить альтернативу шоу"

    old "Propose blowjob"
    new "Предложить минет"

    old "Propose handjob"
    new "Предложить дрочку рукой"

    old "Propose to use handcuffs"
    new "Предложить использовать наручники"

    old "Protect [bree.name]"
    new "Защитить [bree.name]"

    old "Protect Gwen"
    new "Защитить Гвен"

    old "Protect yourself"
    new "Защитить себя"

    old "Protest"
    new "Возразить"

    old "Protest Kylie's innocence"
    new "Доказывать невиновность Кайли"

    old "provider:"
    new "поставщик:"

    old "Psychological thriller"
    new "Психологический триллер"

    old "Pubes"
    new "Лобковые волосы"

    old "Pull away and do something about the shoplifter"
    new "Отстраниться и разобраться с магазинным вором"

    old "Pull back from the accidental kiss"
    new "Отстраниться после случайного поцелуя"

    old "Pull Harmony close for the dance"
    new "Притянуть Хармони ближе во время танца"

    old "Pull her deeper"
    new "Притянуть её глубже"

    old "Pull her hair"
    new "Потянуть её за волосы"

    old "Pull him out"
    new "Вытащить его"

    old "Pull out"
    new "Вытащить"

    old "Pull out Alexis' chair"
    new "Отодвинуть стул для Алексис"

    old "Pull out and cum in Emma's mouth"
    new "Вытащить и кончить Эмме в рот"

    old "Pull out her chair"
    new "Отодвинуть для неё стул"

    old "Pull out of ass"
    new "Вытащить из задницы"

    old "Pull out of her ass"
    new "Вытащить из её задницы"

    old "Pull out of Kylie's ass"
    new "Вытащить из задницы Кайли"

    old "Pull out of pussy"
    new "Вытащить из киски"

    old "Pull out, Pull out!"
    new "Вытащи, вытащи!"

    old "Punish Minami"
    new "Наказать Минами"

    old "Punt the ball back"
    new "Отбить мяч обратно"

    old "Pure casual"
    new "Обычный повседневный"

    old "Pure date"
    new "Скромный наряд для свидания"

    old "Push Audrey gently"
    new "Мягко надавить на Одри"

    old "Push Audrey hard"
    new "Сильно надавить на Одри"

    old "Push her back"
    new "Оттолкнуть её"

    old "Push her head"
    new "Надавить на её голову"

    old "Push her skirt up gently"
    new "Осторожно задрать её юбку"

    old "Push her, we have an appointment"
    new "Поторопить её, у нас назначено"

    old "Push him"
    new "Надавить на него"

    old "Put her on the spare leash"
    new "Пристегнуть её к запасному поводку"

    old "Put Kylie in her place"
    new "Поставить Кайли на место"

    old "Put Kylie off"
    new "Отложить встречу с Кайли"

    old "Put the waiter in his place"
    new "Поставить официанта на место"

    old "Put up with the waiter"
    new "Терпеть официанта"

    old "Q"
    new "Q"

    old "q"
    new "q"

    old "Q.Load"
    new "Б.Загр."

    old "Q.Save"
    new "Б.Сохр."

    old "Question the verses"
    new "Поставить стихи под сомнение"

    old "Quick load."
    new "Быстрая загрузка"

    old "Quick save complete."
    new "Быстрое сохранение завершено."

    old "Quick save."
    new "Быстрое сохранение"

    old "Quick saves"
    new "Быстрые сохранения"

    old "Quickly put her to her feet"
    new "Быстро поставить её на ноги"

    old "Quickly shut your mouth"
    new "Быстро закрыть рот"

    old "QUIT"
    new "ВЫЙТИ"

    old "Quit"
    new "Выйти"

    old "Quits the game."
    new "Закрывает игру."

    old "R"
    new "R"

    old "r"
    new "r"

    old "Race like a pro"
    new "Гоняться как профессионал"

    old "Rameses Bucay, King of Acetonien, PR, Jeffrey Eaton,"
    new "Rameses Bucay, King of Acetonien, PR, Jeffrey Eaton,"

    old "razor wolf, M'Sauvea Reynolds, louie najera, Antoine Daudelin,"
    new "razor wolf, M'Sauvea Reynolds, louie najera, Antoine Daudelin,"

    old "Reach for a knife and fork"
    new "Взяться за нож и вилку"

    old "Reach for chopsticks"
    new "Взяться за палочки"

    old "React meekly"
    new "Отреагировать робко"

    old "React strongly"
    new "Отреагировать резко"

    old "Reading"
    new "Чтение"

    old "Reassure Alexis"
    new "Успокоить Алексис"

    old "Reassure Camila"
    new "Успокоить Камилу"

    old "Reassure her"
    new "Успокоить её"

    old "Recoil from the dog"
    new "Отшатнуться от собаки"

    old "Refuse"
    new "Отказаться"

    old "Refuse (Never meet Harmony again)"
    new "Отказаться (больше никогда не встречаться с Хармони)"

    old "Refuse and walk away (You might never meet Camila again)"
    new "Отказаться и уйти (возможно, больше никогда не встретиться с Камилой)"

    old "Refuse the drink"
    new "Отказаться от напитка"

    old "Refuse to ask Cassidy"
    new "Отказаться спрашивать Кэссиди"

    old "Refuse to give Alexis a massage"
    new "Отказаться делать Алексис массаж"

    old "Refuse to let Alexis cuddle"
    new "Не разрешать Алексис обниматься"

    old "Refuse to manage Ayesha"
    new "Отказаться быть менеджером Айши"

    old "Refuse to meet Harmony's family"
    new "Отказаться встречаться с семьёй Хармони"

    old "Refuse to sign"
    new "Отказаться подписывать"

    old "Reject"
    new "Отказаться"

    old "Reject her"
    new "Отвергнуть её"

    old "Relent"
    new "Уступить"

    old "Reload"
    new "Перезагрузить"

    old "Reloads the game from disk, saving and restoring game state if possible."
    new "Перезагружает игру с диска, по возможности сохраняя и восстанавливая её состояние."

    old "Remain professional"
    new "Сохранять профессионализм"

    old "Remove"
    new "Удалить"

    old "Remove makeup"
    new "Сними макияж"

    old "Remove their leashes"
    new "Снять с них поводки"

    old "Remove them, it's a risk but being able to see is more important"
    new "Снять их: это риск, но возможность видеть важнее"

    old "Remove your collar"
    new "Сними ошейник"

    old "Removes your shoes"
    new "Снять обувь"

    old "Renderer"
    new "Рендерер"

    old "renderer menu"
    new "меню рендерера"

    old "Report Bug"
    new "Сообщить об ошибке"

    old "Report the cheater"
    new "Сообщить о читере"

    old "Reporting them will help us to improve the gallery :)"
    new "Сообщения о них помогут нам улучшить галерею :)"

    old "Reset"
    new "Сбросить"

    old "reset"
    new "сбросить"

    old "Reset application"
    new "Сбросить приложение"

    old "reset font kerning"
    new "сбросить кернинг шрифта"

    old "reset font line spacing"
    new "сбросить межстрочный интервал"

    old "reset font size"
    new "сбросить размер шрифта"

    old "reset self voicing volume drop"
    new "сбросить уменьшение громкости при озвучивании"

    old "reset voice volume"
    new "сбросить громкость голоса"

    old "Resist, impudently"
    new "Дерзко сопротивляться"

    old "Resist, playfully"
    new "Игриво сопротивляться"

    old "Restart"
    new "Перезапустить"

    old "Restaurant"
    new "Ресторан"

    old "restore window position"
    new "восстановить положение окна"

    old "Restrain myself"
    new "Сдержаться"

    old "RESUME"
    new "ПРОДОЛЖИТЬ"

    old "Retry"
    new "Повторить попытку"

    old "Return"
    new "Назад"

    old "return"
    new "вернуться"

    old "Return Anna's attentions"
    new "Ответить на внимание Анны"

    old "Return both girls' attentions"
    new "Ответить на внимание обеих девушек"

    old "Return Kleio's attentions"
    new "Ответить на внимание Клео"

    old "Reverse Cowgirl"
    new "Обратная наездница"

    old "Reverse cowgirl"
    new "Обратная наездница"

    old "Right"
    new "Справа"

    old "RIGHT CLICK"
    new "ПРАВАЯ КНОПКА"

    old "Right Click"
    new "Правая кнопка"

    old "Right Shoulder"
    new "Правый бампер"

    old "Right Trigger\nA/Bottom Button"
    new "Правый триггер\nA/Нижняя кнопка"

    old "Roa Music"
    new "Roa Music"

    old "robert, Vincent, DarkAges85, Jett Smith, Jakaa9,"
    new "robert, Vincent, DarkAges85, Jett Smith, Jakaa9,"

    old "Rock, metal"
    new "Рок, метал"

    old "Rollback"
    new "Откат"

    old "rollback side"
    new "сторона отката"

    old "Rolls back to earlier dialogue."
    new "Возвращает к предыдущему диалогу"

    old "Rolls forward to later dialogue."
    new "Переходит к следующему диалогу"

    old "Rom-com"
    new "Романтическая комедия"

    old "Romance"
    new "Романтика"

    old "Romcom"
    new "Романтическая комедия"

    old "Roommates are off limits!"
    new "С соседками нельзя!"

    old "Rope"
    new "Верёвка"

    old "Rough"
    new "Грубо"

    old "Rub sun cream on [bree.name]"
    new "Нанести крем от солнца на [bree.name]"

    old "Running"
    new "Бег"

    old "RussianBee, Negative Wizard, death_the_kid123, MaxStorm,"
    new "RussianBee, Negative Wizard, death_the_kid123, MaxStorm,"

    old "ryan adkins, VIVIDave, Joshua Taylor, Vlad Sadilovskiy,"
    new "ryan adkins, VIVIDave, Joshua Taylor, Vlad Sadilovskiy,"

    old "Ryan Darkstar, Joe Joe, Florian Jacquet, karel-de-macil,"
    new "Ryan Darkstar, Joe Joe, Florian Jacquet, karel-de-macil,"

    old "Ryan, Sam and I have an arrangement"
    new "У нас с Райаном и Сэм есть договорённость"

    old "S"
    new "S"

    old "s"
    new "s"

    old "Salmon"
    new "Лосось"

    old "Salty"
    new "Солёное"

    old "Samael, Michael, laurynas, cestmir, Locke, Doc Pan As,"
    new "Samael, Michael, laurynas, cestmir, Locke, Doc Pan As,"

    old "Samantha"
    new "Samantha"

    old "Sasha"
    new "Sasha"

    old "Sasha eat [bree.name] out"
    new "Саша вылизывает [bree.name]"

    old "Sasha use a strap-on on [bree.name]"
    new "Саша использует страпон на [bree.name]"

    old "Save"
    new "Сохранить"

    old "SAVE"
    new "СОХРАНИТЬ"

    old "Save [bree.name]"
    new "Спасти [bree.name]"

    old "Save Name"
    new "Название сохранения"

    old "Save slot %s: [text]"
    new "Слот сохранения %s: [text]"

    old "Saved screenshot as %s."
    new "Скриншот сохранён как %s."

    old "Savor your food"
    new "Наслаждаться едой"

    old "Say 'please'."
    new "Скажи «пожалуйста»"

    old "Say about time you noticed."
    new "Сказать: «Наконец-то ты заметила»"

    old "Say goodbye to this weirdo"
    new "Попрощаться с этим чудаком"

    old "Say it could be used for a prank"
    new "Сказать, что его можно использовать для розыгрыша"

    old "Say no"
    new "Сказать «нет»"

    old "Say nothing"
    new "Ничего не говорить"

    old "Say Nothing"
    new "Ничего не говорить"

    old "Say nothing."
    new "Ничего не говорить"

    old "Say she disgust you"
    new "Сказать, что она тебе отвратительна"

    old "Say she disgusts you"
    new "Сказать, что она тебе отвратительна"

    old "Say something"
    new "Что-нибудь сказать"

    old "Say something to break the ice"
    new "Сказать что-нибудь, чтобы разрядить обстановку"

    old "Say Thank you."
    new "Сказать «спасибо»"

    old "Say that you are happy for her"
    new "Сказать, что рад за неё"

    old "Say that you want to call it a night"
    new "Сказать, что пора заканчивать вечер"

    old "Say whaaat?!?"
    new "Сказать: «Чего-о-о?!»"

    old "Say yes"
    new "Сказать «да»"

    old "Say you are happy for her"
    new "Сказать, что рад за неё"

    old "Say you wanna record it"
    new "Сказать, что хочешь это записать"

    old "Say you want it for yourself"
    new "Сказать, что хочешь оставить это себе"

    old "Say you want revenge on Gwen and Alexis"
    new "Сказать, что хочешь отомстить Гвен и Алексис"

    old "Scare"
    new "Напугать"

    old "Sci-Fi thriller"
    new "Научно-фантастический триллер"

    old "Scold both"
    new "Отругать обеих"

    old "Scold Camila"
    new "Отругать Камилу"

    old "Scold her"
    new "Отругать её"

    old "Scold her harshly (this will never happen again)"
    new "Жёстко отругать её (это больше никогда не повторится)"

    old "Scold Lexi"
    new "Отругать Лекси"

    old "Scold them both."
    new "Отругать обеих"

    old "Scotty Doesn't Know, Nightmare Spyro, jerald imo, cj33,"
    new "Scotty Doesn't Know, Nightmare Spyro, jerald imo, cj33,"

    old "Scream for help"
    new "Кричать о помощи"

    old "Screen"
    new "Экран"

    old "Screw work"
    new "К чёрту работу"

    old "scroll "
    new "прокрутка"

    old "Seahorses"
    new "Морские коньки"

    old "See ya"
    new "Увидимся"

    old "See you in Sasha's room"
    new "Увидимся в комнате Саши"

    old "See you in your room"
    new "Увидимся в твоей комнате"

    old "SeekerZero as Audrey"
    new "SeekerZero — Одри"

    old "Select Gamepad to Calibrate"
    new "Выберите геймпад для калибровки"

    old "selected"
    new ". На данный момент это выбрано"

    old "self voicing"
    new "озвучка через синтезатор речи"

    old "self voicing disable"
    new "отключить авто озвучивание"

    old "self voicing enable"
    new "включить авто озвучивание"

    old "self voicing volume drop"
    new "уменьшение громкости при озвучке через синтезатор речи"

    old "Self-Voicing"
    new "Озвучка через синтезатор речи"

    old "Self-Voicing and Audio"
    new "Синтезатор речи и звук"

    old "Self-voicing disabled."
    new "Синтезатор речи отключён."

    old "Self-voicing enabled. "
    new "Синтезатор речи включён."

    old "Self-voicing enabled. Press 'v' to disable."
    new "Синтезатор речи включён. Нажмите 'v', чтобы отключить его."

    old "Self-voicing support is limited when using a touch screen."
    new "Поддержка синтезатора речи ограничена при использовании сенсорного экрана."

    old "Self-Voicing Volume Drop"
    new "Уменьшение громкости при озвучке через синтезатор речи"

    old "Self-voicing would say \"[renpy.display.tts.last]\". Press 'alt+shift+V' to disable."
    new "Синтезатор речи должен сказать \"[renpy.display.tts.last]\". Нажмите 'alt+shift+V', чтобы отключить его."

    old "Send dirty text"
    new "Отправить грязное сообщение"

    old "Send her back"
    new "Отправить её обратно"

    old "Send sexy text"
    new "Отправить сексуальное сообщение"

    old "services"
    new "услуги"

    old "Services"
    new "Услуги"

    old "Set month to fall"
    new "Установить месяц на осень"

    old "Set month to spring"
    new "Установить месяц на весну"

    old "Set month to summer"
    new "Установить месяц на лето"

    old "Set month to winter"
    new "Установить месяц на зиму"

    old "Set the weight a little high"
    new "Установить немного больший вес"

    old "Set the weight really high"
    new "Установить очень большой вес"

    old "Set the weight where she says"
    new "Установить вес, как она сказала"

    old "Set up a date with Alexis and Reona"
    new "Устроить свидание с Алексис и Реоной"

    old "Set up a date with Camila and Lexi"
    new "Устроить свидание с Камилой и Лекси"

    old "Set up a date with Harmony and Lexi"
    new "Устроить свидание с Хармони и Лекси"

    old "Set up a date with Lexi and Reona"
    new "Устроить свидание с Лекси и Реоной"

    old "Sex"
    new "Секс"

    old "Sexier and dangerous"
    new "Сексуальнее и опаснее"

    old "Sexier and scary"
    new "Сексуальнее и страшнее"

    old "Sexy date"
    new "Сексуальный наряд для свидания"

    old "Sexy swimsuit"
    new "Сексуальный купальник"

    old "Sexy top"
    new "Сексуальный верх"

    old "Sexy underwear"
    new "Сексуальное бельё"

    old "Sexy uniform"
    new "Сексуальная униформа"

    old "Share the love"
    new "Поделиться любовью"

    old "Shave your armpits"
    new "Побрей подмышки"

    old "Shave your pussy"
    new "Побрей киску"

    old "She doesn't need to know about it..."
    new "Ей необязательно об этом знать..."

    old "She has a strange vibe"
    new "От неё исходит странная энергетика"

    old "She hasn't changed much"
    new "Она почти не изменилась"

    old "She wants me and I want her"
    new "Она хочет меня, а я хочу её"

    old "She would be better with me"
    new "Со мной ей было бы лучше"

    old "She would only mess it up"
    new "Она только всё испортит"

    old "She'll be mine soon enough."
    new "Скоро она будет моей"

    old "She's a great boss"
    new "Она отличный начальник"

    old "She's a slut"
    new "Она шлюха"

    old "She's a total bitch"
    new "Она настоящая стерва"

    old "She's annoying"
    new "Она раздражает"

    old "She's cute"
    new "Она милая"

    old "She's damn right!"
    new "Она чертовски права!"

    old "She's flawed"
    new "У неё есть недостатки"

    old "She's fun"
    new "С ней весело"

    old "She's going too far!"
    new "Она заходит слишком далеко!"

    old "She's hot"
    new "Она горячая"

    old "She's just a friend"
    new "Она просто подруга"

    old "She's lazy"
    new "Она ленивая"

    old "She's mean"
    new "Она злая"

    old "She's my sex slave"
    new "Она моя секс-рабыня"

    old "She's not real, it's just a dream (Never meet Emma again)"
    new "Она не настоящая, это всего лишь сон (больше никогда не встречаться с Эммой)"

    old "She's okay, I guess"
    new "Она нормальная, наверное"

    old "She's real. I have to find her"
    new "Она настоящая. Я должен её найти"

    old "She's someone I care about very much"
    new "Она очень мне дорога"

    old "She's very professional"
    new "Она очень профессиональна"

    old "Shennychwan as Shiori"
    new "Shennychwan — Сиори"

    old "Shift+A"
    new "Shift+A"

    old "Shiori"
    new "Shiori"

    old "Shiori should not wear her sexy uniform anymore"
    new "Сиори больше не должна носить сексуальную униформу"

    old "Shiori should put her bottom back on"
    new "Сиори должна снова надевать низ"

    old "Shiori should put her top back"
    new "Сиори должна снова надевать верх"

    old "Shiori should put her uniform back"
    new "Сиори должна снова надевать униформу"

    old "Shiori should remove her bottoms at work"
    new "Сиори должна снимать низ на работе"

    old "Shiori should remove her top at work"
    new "Сиори должна снимать верх на работе"

    old "Shiori should remove her uniform at work"
    new "Сиори должна снимать униформу на работе"

    old "Shiori should wear her sexy uniform"
    new "Сиори должна носить свою сексуальную униформу"

    old "Shitty Cuz, Vigilant, Blitzreigkai97, Antonio Serrano,"
    new "Shitty Cuz, Vigilant, Blitzreigkai97, Antonio Serrano,"

    old "Shoo her away"
    new "Прогнать её"

    old "Shoot at the closest guard behind the wooden crate"
    new "Выстрелить в ближайшего охранника за деревянным ящиком"

    old "Shoot at the furthest guard by the loading door, behind the concrete pillar"
    new "Выстрелить в дальнего охранника у погрузочной двери, за бетонной колонной"

    old "Shoot at the guard behind the wooden crate"
    new "Выстрелить в охранника за деревянным ящиком"

    old "Shoot at the guard by the loading door"
    new "Выстрелить в охранника у погрузочной двери"

    old "Shoot at the security lead taking cover by the metal crates"
    new "Выстрелить в главного охранника, укрывшегося за металлическими ящиками"

    old "Shooting"
    new "Стрельба"

    old "Shopping"
    new "Покупки"

    old "Show"
    new "Показывать"

    old "show empty window"
    new "показывать пустое окно диалога"

    old "Show Her the Pictures"
    new "Показать ей фотографии"

    old "Show her what it's like to be the best"
    new "Показать ей, каково это — быть лучшим"

    old "Show her who's the boss"
    new "Показать ей, кто здесь главный"

    old "Show her who's the boss."
    new "Показать ей, кто здесь главный"

    old "Show Lavish how to make a fire"
    new "Показать Лавиш, как разжечь огонь"

    old "Show Sasha who's the boss"
    new "Показать Саше, кто здесь главный"

    old "Show the completed step."
    new "Показывать завершённый этап"

    old "Show the ongoing step."
    new "Показывать текущий этап"

    old "Show them a real stone skim"
    new "Показать им настоящий бросок камня по воде"

    old "Show your appreciation instead"
    new "Вместо этого выразить благодарность"

    old "Shrug it off"
    new "Не придавать значения"

    old "Shudder at the thought of being tied down with a family"
    new "Содрогнуться от мысли о семейных обязательствах"

    old "Shut Kylie up"
    new "Заткнуть Кайли"

    old "Shut up while I'm on the phone!"
    new "Заткнись, я разговариваю по телефону!"

    old "Shut up! Both of you"
    new "Заткнитесь! Обе"

    old "Sickness for [game.timers.sick] day"
    new "Болеет [game.timers.sick] день"

    old "Side with [bree.name]"
    new "Поддержать [bree.name]"

    old "Side with [bree.name] and Sasha"
    new "Поддержать [bree.name] и Сашу"

    old "Side with Camila"
    new "Поддержать Камилу"

    old "Side with Cassidy"
    new "Поддержать Кэссиди"

    old "Side with Jack"
    new "Поддержать Джека"

    old "Side with Jack and Scottie"
    new "Поддержать Джека и Скотти"

    old "Side with Kleio"
    new "Поддержать Клео"

    old "Side with Laura"
    new "Поддержать Лауру"

    old "Side with Samantha"
    new "Поддержать Саманту"

    old "Side with Sasha"
    new "Поддержать Сашу"

    old "Side with Sasha and Kleio against Anna"
    new "Поддержать Сашу и Клео против Анны"

    old "Side with Scottie"
    new "Поддержать Скотти"

    old "Sign the document"
    new "Подписать документ"

    old "SilkyMilk as Aletta"
    new "SilkyMilk — Алетта"

    old "Sim card"
    new "SIM-карта"

    old "Simple fooling around"
    new "Просто подурачиться"

    old "sio_sid: [persistent.sio_sid]"
    new "идентификатор sio: [persistent.sio_sid]"

    old "Sit down anyway"
    new "Всё равно сесть"

    old "Sit first"
    new "Сесть первым"

    old "Sit straight down in your seat"
    new "Сразу сесть на своё место"

    old "Skip"
    new "Пропустить"

    old "skip"
    new "пропускать"

    old "Skip (A)"
    new "Пропустить (A)"

    old "skip after choices"
    new "пропускать после выборов"

    old "Skip foreplay"
    new "Пропустить прелюдию"

    old "Skip Mode"
    new "Режим пропуска"

    old "skip transitions"
    new "пропускать переходы"

    old "skip unseen [text]"
    new "пропускать весь [text]"

    old "skip unseen text"
    new "пропускать весь текст"

    old "Skipping"
    new "Пропуск"

    old "Skips dialogue while held down."
    new "Пропускает диалог, пока клавиша удерживается"

    old "Slack off"
    new "Бездельничать"

    old "Slap ass"
    new "Шлёпнуть по заднице"

    old "Slave"
    new "Раб"

    old "Slave play"
    new "Игры с рабыней"

    old "Slide hand up"
    new "Поднять руку выше"

    old "slideshow"
    new "слайд-шоу"

    old "Slow down Hanna"
    new "Притормозить Ханну"

    old "Slutty"
    new "Распутно"

    old "Slutty date"
    new "Распутный наряд для свидания"

    old "Slutty swimsuit"
    new "Откровенный купальник"

    old "SM porn"
    new "БДСМ-порно"

    old "Small warning!"
    new "Небольшое предупреждение!"

    old "smartphone"
    new "смартфон"

    old "Smile Back"
    new "Улыбнуться в ответ"

    old "Smokin'"
    new "Огонь"

    old "Smooth things over with Kylie"
    new "Сгладить ситуацию с Кайли"

    old "Snap out of it!"
    new "Приди в себя!"

    old "Sneak in Sasha's room"
    new "Пробраться в комнату Саши"

    old "Sneer at the players"
    new "Насмехаться над игроками"

    old "So be it"
    new "Пусть будет так"

    old "Soap Opera"
    new "Мыльная опера"

    old "Some maybe"
    new "Некоторые, возможно"

    old "Someone else"
    new "Кто-то другой"

    old "Something like that."
    new "Что-то вроде того"

    old "Something new."
    new "Что-нибудь новое"

    old "Something stronger"
    new "Что-нибудь покрепче"

    old "Something's up"
    new "Что-то случилось"

    old "Sorry, but no."
    new "Извини, но нет"

    old "Sorry, no"
    new "Извини, нет"

    old "Sorry..."
    new "Прости..."

    old "sound volume"
    new "громкость звуков"

    old "Sounds awesome!"
    new "Звучит потрясающе!"

    old "Sounds difficult. Need any help?"
    new "Звучит сложно. Помочь?"

    old "Sounds fun"
    new "Звучит весело"

    old "Sounds hot"
    new "Звучит горячо"

    old "SPACE"
    new "ПРОБЕЛ"

    old "Space"
    new "Пробел"

    old "Spaghetti"
    new "Спагетти"

    old "Spank [bree.name]"
    new "Шлёпать [bree.name]"

    old "Spank [bree.name] and Sasha"
    new "Шлёпать [bree.name] и Сашу"

    old "Spank Audrey"
    new "Шлёпать Одри"

    old "Spank her"
    new "Шлёпать её"

    old "Spank Palla"
    new "Шлёпать Паллу"

    old "Spank Sasha"
    new "Шлёпать Сашу"

    old "Speaker"
    new "Динамик"

    old "SPECIAL CONTRIBUTOR"
    new "ОСОБЫЙ ВКЛАД"

    old "Special you say?"
    new "Говоришь, особенный?"

    old "Speech Bubble Editor"
    new "Редактор пузырьков речи"

    old "Spend 100{image=gui/icons/icon_money.png}"
    new "Потратить 100{image=gui/icons/icon_money.png}"

    old "Spend 1600{image=gui/icons/icon_money.png}"
    new "Потратить 1600{image=gui/icons/icon_money.png}"

    old "Spend 200{image=gui/icons/icon_money.png}"
    new "Потратить 200{image=gui/icons/icon_money.png}"

    old "Spend 400{image=gui/icons/icon_money.png}"
    new "Потратить 400{image=gui/icons/icon_money.png}"

    old "Spend 50{image=gui/icons/icon_money.png}"
    new "Потратить 50{image=gui/icons/icon_money.png}"

    old "Spend 800{image=gui/icons/icon_money.png}"
    new "Потратить 800{image=gui/icons/icon_money.png}"

    old "Spirit Writer, Paris, Phoenix, Andrealphus,"
    new "Spirit Writer, Paris, Phoenix, Andrealphus,"

    old "Split the bill"
    new "Разделить счёт"

    old "Spoilers"
    new "Спойлеры"

    old "Spoon"
    new "Ложки"

    old "Sports"
    new "Спорт"

    old "Spring"
    new "Весна"

    old "Squeaky as Lexi"
    new "Squeaky — Лекси"

    old "Stack them"
    new "Поставить их друг на друга"

    old "Stand"
    new "Стоя"

    old "Stand back and watch"
    new "Остаться в стороне и смотреть"

    old "Stand there and wait"
    new "Стоять и ждать"

    old "Stand up for Aletta"
    new "Заступиться за Алетту"

    old "Stand up to Danny"
    new "Дать отпор Дэнни"

    old "Stand up to her"
    new "Дать ей отпор"

    old "Standing"
    new "Стоя"

    old "START"
    new "НАЧАТЬ"

    old "Start"
    new "Начать"

    old "Start plus"
    new "Новая игра+"

    old "Start with a blowjob"
    new "Начать с минета"

    old "Start, Guide,\nB/Right Button"
    new "Start, Guide,\nB/Правая кнопка"

    old "Start, Guide, B/Right Button"
    new "Start, Guide, B/Правая кнопка"

    old "Startup downloader"
    new "Загрузчик при запуске"

    old "Statement:"
    new "Операторы:"

    old "Stay"
    new "Останься"

    old "Stay and watch"
    new "Остаться и смотреть"

    old "Stay at the party"
    new "Остаться на вечеринке"

    old "Stay away"
    new "Держаться подальше"

    old "Stay clear of this one"
    new "Не связываться с этим"

    old "Stay close"
    new "Остаться рядом"

    old "Stay here and enjoy the time that passes"
    new "Остаться здесь и наслаждаться временем"

    old "Stay hidden and wait for Camila to rescue me"
    new "Остаться в укрытии и ждать, пока Камила меня спасёт"

    old "Stay longer"
    new "Остаться подольше"

    old "Stay out of it"
    new "Не вмешиваться"

    old "Stay professional"
    new "Сохранять профессионализм"

    old "Stay seated"
    new "Остаться сидеть"

    old "Stay silent"
    new "Промолчать"

    old "Stay silent."
    new "Промолчать"

    old "Stay simple"
    new "Не усложнять"

    old "Stay with Samantha"
    new "Остаться с Самантой"

    old "Step aside"
    new "Отойти в сторону"

    old "Step in"
    new "Вмешаться"

    old "Step in to save Anna"
    new "Вмешаться и спасти Анну"

    old "Stick my foot out in front of the kid"
    new "Подставить ребёнку ногу"

    old "Stick to your principles"
    new "Не изменять своим принципам"

    old "Stick with it"
    new "Не менять решение"

    old "Still no"
    new "Всё равно нет"

    old "Still, let's camp far"
    new "Но всё же давай разобьём лагерь подальше"

    old "Stools are fine"
    new "Табуретки подойдут"

    old "Stop"
    new "Остановиться"

    old "Stop asking me out"
    new "Перестань приглашать меня на свидания"

    old "Stop Audrey"
    new "Остановить Одри"

    old "Stop before cumming"
    new "Остановиться до оргазма"

    old "Stop being a bitch"
    new "Перестань быть сучкой"

    old "Stop calling me [[hero.name]"
    new "Перестань называть меня [[hero.name]"

    old "Stop calling me Baby"
    new "Перестань называть меня Малышом"

    old "Stop calling me Boi"
    new "Перестань называть меня Боем"

    old "Stop calling me Boo"
    new "Перестань называть меня Любимым"

    old "Stop calling me Boss"
    new "Перестань называть меня Боссом"

    old "Stop calling me Boss Buck"
    new "Перестань называть меня Большим боссом"

    old "Stop calling me Boy"
    new "Перестань называть меня Мальчиком"

    old "Stop calling me Boytoy"
    new "Перестань называть меня Игрушкой"

    old "Stop calling me Brah"
    new "Перестань называть меня Бро"

    old "Stop calling me Bro"
    new "Перестань называть меня Бро"

    old "Stop calling me Bro-bro"
    new "Перестань называть меня Братишкой"

    old "Stop calling me Chad"
    new "Перестань называть меня Чадом"

    old "Stop calling me Champ"
    new "Перестань называть меня Чемпионом"

    old "Stop calling me Chief"
    new "Перестань называть меня Шефом"

    old "Stop calling me Coach"
    new "Перестань называть меня Тренером"

    old "Stop calling me Cow-boy"
    new "Перестань называть меня Ковбоем"

    old "Stop calling me Cuck"
    new "Перестань называть меня Куколдом"

    old "Stop calling me Cutie"
    new "Перестань называть меня Милашкой"

    old "Stop calling me Daddy"
    new "Перестань называть меня Папочкой"

    old "Stop calling me Dark knight"
    new "Перестань называть меня Тёмным рыцарем"

    old "Stop calling me Dearest"
    new "Перестань называть меня Дорогим"

    old "Stop calling me Demon"
    new "Перестань называть меня Демоном"

    old "Stop calling me Dick"
    new "Перестань называть меня Членом"

    old "Stop calling me Dreamboat"
    new "Перестань называть меня Красавчиком"

    old "Stop calling me Dude"
    new "Перестань называть меня Чуваком"

    old "Stop calling me Dumbass"
    new "Перестань называть меня Дебилом"

    old "Stop calling me Fuck Face"
    new "Перестань называть меня Ебальником"

    old "Stop calling me Fuckface"
    new "Перестань называть меня Ебальником"

    old "Stop calling me Guapo"
    new "Перестань называть меня Гуапо"

    old "Stop calling me Hanata"
    new "Перестань называть меня Ханатой"

    old "Stop calling me Handsome"
    new "Перестань называть меня Красавчиком"

    old "Stop calling me Hermoso"
    new "Перестань называть меня Эрмосо"

    old "Stop calling me Hero"
    new "Перестань называть меня Героем"

    old "Stop calling me Honey"
    new "Перестань называть меня Милым"

    old "Stop calling me Hotshot"
    new "Перестань называть меня Крутышом"

    old "Stop calling me Husband"
    new "Перестань называть меня Мужем"

    old "Stop calling me Idiot"
    new "Перестань называть меня Идиотом"

    old "Stop calling me Koibito"
    new "Перестань называть меня Койбито"

    old "Stop calling me Little man"
    new "Перестань называть меня Малышом"

    old "Stop calling me Little one"
    new "Перестань называть меня Малышом"

    old "Stop calling me Lord"
    new "Перестань называть меня Лордом"

    old "Stop calling me Love"
    new "Перестань называть меня Любимым"

    old "Stop calling me Master"
    new "Перестань называть меня Господином"

    old "Stop calling me Mr.Boss sir"
    new "Перестань называть меня Господином Боссом"

    old "Stop calling me Muffin"
    new "Перестань называть меня Кексиком"

    old "Stop calling me My angel"
    new "Перестань называть меня Моим ангелом"

    old "Stop calling me My ball and chain"
    new "Перестань называть меня Обузой"

    old "Stop calling me My Big Bear"
    new "Перестань называть меня Моим большим медведем"

    old "Stop calling me My friend"
    new "Перестань называть меня Другом"

    old "Stop calling me My Heart"
    new "Перестань называть меня Моим сердцем"

    old "Stop calling me My King"
    new "Перестань называть меня Моим королём"

    old "Stop calling me My One and Only"
    new "Перестань называть меня Единственным"

    old "Stop calling me My Prince"
    new "Перестань называть меня Моим принцем"

    old "Stop calling me My rock"
    new "Перестань называть меня Моей опорой"

    old "Stop calling me Naughty boy"
    new "Перестань называть меня Плохим мальчиком"

    old "Stop calling me Nii-san"
    new "Перестань называть меня Нии-саном"

    old "Stop calling me Onii-chan"
    new "Перестань называть меня Они-тяном"

    old "Stop calling me Owner"
    new "Перестань называть меня Хозяином"

    old "Stop calling me Papi"
    new "Перестань называть меня Папи"

    old "Stop calling me Papi Chulo"
    new "Перестань называть меня Папи Чуло"

    old "Stop calling me Partner"
    new "Перестань называть меня Партнёром"

    old "Stop calling me Peasant"
    new "Перестань называть меня Крестьянином"

    old "Stop calling me Perv"
    new "Перестань называть меня Извращенцем"

    old "Stop calling me Playboy"
    new "Перестань называть меня Плейбоем"

    old "Stop calling me Player One"
    new "Перестань называть меня Первым игроком"

    old "Stop calling me Roomie"
    new "Перестань называть меня Соседом"

    old "Stop calling me Senpai"
    new "Перестань называть меня Сэмпаем"

    old "Stop calling me Servant"
    new "Перестань называть меня Слугой"

    old "Stop calling me Smooth rider"
    new "Перестань называть меня Ловким наездником"

    old "Stop calling me Stallion"
    new "Перестань называть меня Жеребцом"

    old "Stop calling me Stud"
    new "Перестань называть меня Жеребцом"

    old "Stop calling me Studmuffin"
    new "Перестань называть меня Жеребчиком"

    old "Stop calling me Sugar"
    new "Перестань называть меня Сладким"

    old "Stop calling me Superstar"
    new "Перестань называть меня Суперзвездой"

    old "Stop calling me Sweetheart"
    new "Перестань называть меня Любимым"

    old "Stop calling me Sweetie"
    new "Перестань называть меня Милым"

    old "Stop calling me Twink"
    new "Перестань называть меня Твинком"

    old "Stop calling me Wallet"
    new "Перестань называть меня Кошельком"

    old "Stop calling me Young man"
    new "Перестань называть меня Молодым человеком"

    old "Stop dancing"
    new "Перестать танцевать"

    old "Stop helping"
    new "Перестать помогать"

    old "Stop her"
    new "Остановить её"

    old "Stop her physically"
    new "Остановить её силой"

    old "Stop Jeff leaving"
    new "Не дать Джеффу уйти"

    old "Stop Morgan from confronting the family"
    new "Остановить Морган от столкновения с семьёй"

    old "Stop shaving"
    new "Перестань бриться"

    old "Stop the patron touching Hanna"
    new "Не дать посетителю трогать Ханну"

    old "Stop working at the strip club"
    new "Перестань работать в стрип-клубе"

    old "STORY TRACKER"
    new "ОТСЛЕЖИВАНИЕ СЮЖЕТА"

    old "story tracker"
    new "отслеживание сюжета"

    old "Storyteller, Dirtyduck, Jonathan Brooks, Lucifer, Lejo98,"
    new "Storyteller, Dirtyduck, Jonathan Brooks, Lucifer, Lejo98,"

    old "Stripper"
    new "Стриптизёрша"

    old "Stripper outfit"
    new "Наряд стриптизёрши"

    old "Stunning"
    new "Потрясающе"

    old "Suck it up, Buttercup"
    new "Соберись, принцесса"

    old "Suggest a BJ"
    new "Предложить минет"

    old "Suggest a choice of dish"
    new "Предложить выбрать блюдо"

    old "Suggest a photo-shoot"
    new "Предложить фотосессию"

    old "Suggest an alternative"
    new "Предложить альтернативу"

    old "Suggest more dildos"
    new "Предложить больше дилдо"

    old "Suggest moving"
    new "Предложить перейти в другое место"

    old "Suggest something else"
    new "Предложить что-нибудь другое"

    old "Suggest that she try it out"
    new "Предложить ей попробовать"

    old "Suggest that you and Shiori share"
    new "Предложить поделиться с Сиори"

    old "Suggest that you grab a bite to eat at the cafe"
    new "Предложить перекусить в кафе"

    old "Suggest that you just eat a hotdog"
    new "Предложить просто съесть хот-дог"

    old "Suggest that you stay and watch"
    new "Предложить остаться и посмотреть"

    old "Suggest the glory-hole room"
    new "Предложить комнату с глори-холом"

    old "Suggest they split the bill"
    new "Предложить им разделить счёт"

    old "Suggest to grab a beer"
    new "Предложить выпить пива"

    old "Suggest to grab a coffee"
    new "Предложить выпить кофе"

    old "Summer"
    new "Лето"

    old "Super Hero"
    new "Супергерой"

    old "Support"
    new "Поддержать"

    old "Support Minami"
    new "Поддержать Минами"

    old "Support Sasha"
    new "Поддержать Сашу"

    old "Sure"
    new "Конечно"

    old "Sure!"
    new "Конечно!"

    old "Sure, I can think of things we could do together."
    new "Конечно, я могу придумать, чем нам заняться вместе"

    old "Sure, someday"
    new "Конечно, когда-нибудь"

    old "Sure, sounds like fun."
    new "Конечно, звучит весело"

    old "Sure, why not"
    new "Конечно, почему бы и нет"

    old "Swallow"
    new "Проглотить"

    old "Sweaty"
    new "Потный"

    old "Sweet"
    new "Сладкое"

    old "Sweet, I love football"
    new "Класс, я люблю футбол"

    old "Swimsuit"
    new "Купальник"

    old "Swimsuit outfit"
    new "Купальник"

    old "Sympathise"
    new "Посочувствовать"

    old "Sympathise with Kylie"
    new "Посочувствовать Кайли"

    old "Sync downloaded."
    new "Синхронизация загружена."

    old "Sync Error"
    new "Синхронизация не удалась"

    old "Sync Success"
    new "Синхронизация успешна"

    old "system cursor"
    new "системный курсор"

    old "T"
    new "T"

    old "t"
    new "t"

    old "TAB"
    new "TAB"

    old "Tab"
    new "Tab"

    old "Tackle mugger"
    new "Сбить грабителя с ног"

    old "Tackle the crab yourself"
    new "Самому разобраться с крабом"

    old "Tag:"
    new "Теги:"

    old "Take a deep breath and listen to her"
    new "Глубоко вдохнуть и выслушать её"

    old "Take a nap"
    new "Вздремнуть"

    old "Take a peek"
    new "Подглядеть"

    old "Take a shower"
    new "Принять душ"

    old "Take a step back"
    new "Отступить на шаг"

    old "Take a stroll"
    new "Прогуляться"

    old "Take Book"
    new "Взять книгу"

    old "Take Cassidy home"
    new "Отвезти Кэссиди домой"

    old "Take charge"
    new "Взять инициативу"

    old "Take control"
    new "Взять контроль"

    old "Take control of the situation"
    new "Взять ситуацию под контроль"

    old "Take her"
    new "Взять её"

    old "Take her out in the garden."
    new "Вывести её в сад"

    old "Take her to the park."
    new "Отвести её в парк"

    old "Take in the Boxes"
    new "Занести коробки"

    old "Take in the Desk"
    new "Занести стол"

    old "Take it"
    new "Взять"

    old "Take me to one some time"
    new "Как-нибудь своди меня туда"

    old "Take morgan to a store I saw last time"
    new "Отвести Морган в магазин, который я видел в прошлый раз"

    old "Take Morgan's side"
    new "Поддержать Морган"

    old "Take out a beer"
    new "Достать пиво"

    old "Take out the champagne"
    new "Достать шампанское"

    old "Take responsibility"
    new "Взять на себя ответственность"

    old "Take the beads out"
    new "Вытащить шарики"

    old "Take the bed, I'll sleep on the floor"
    new "Забирай кровать, я посплю на полу"

    old "Take the boxes from her"
    new "Забрать у неё коробки"

    old "Take the cash"
    new "Взять наличные"

    old "Take the job"
    new "Взяться за работу"

    old "Take the money"
    new "Взять деньги"

    old "Take the vibrator out"
    new "Вытащить вибратор"

    old "Take them out for a walk"
    new "Вывести их на прогулку"

    old "Take them out in the garden."
    new "Вывести их в сад"

    old "Take them to the park."
    new "Отвести их в парк"

    old "Take your phone out and do the same"
    new "Достать телефон и сделать то же самое"

    old "Takes a screenshot."
    new "Делает снимок экрана"

    old "Takes Kleio's side"
    new "Поддержать Клео"

    old "Talk about personal nickname"
    new "Поговорить о личном прозвище"

    old "Talk about yourself"
    new "Рассказать о себе"

    old "Talk dirty to her"
    new "Говорить с ней грязно"

    old "Talk to her"
    new "Поговорить с ней"

    old "Talk to Shiori about your idea."
    new "Поговорить с Сиори о своей идее"

    old "Tattoo"
    new "Татуировка"

    old "Taunt her"
    new "Подразнить её"

    old "Teach"
    new "Учить"

    old "Teach me!"
    new "Научи меня!"

    old "Teach Sasha a breathing exercise"
    new "Научить Сашу дыхательному упражнению"

    old "Team up with [bree.name]"
    new "Объединиться с [bree.name]"

    old "Team up with Lexi"
    new "Объединиться с Лекси"

    old "Teamwork... Efficiency... I'm calling!"
    new "Командная работа... Эффективность... Звоню!"

    old "Tearing"
    new "Разрывы изображения"

    old "Tease Camila"
    new "Подразнить Камилу"

    old "Tease her"
    new "Подразнить её"

    old "TeknoAXE"
    new "TeknoAXE"

    old "Telephone"
    new "Телефон"

    old "Television"
    new "Телевизор"

    old "Tell Aletta to leave"
    new "Сказать Алетте уйти"

    old "Tell Ayesha it was an accident"
    new "Сказать Айше, что это была случайность"

    old "Tell Ayesha not to do it"
    new "Сказать Айше не делать этого"

    old "Tell Ayesha off"
    new "Отчитать Айшу"

    old "Tell Ayesha to go for it"
    new "Сказать Айше, чтобы она попробовала"

    old "Tell Emma to get rid of it"
    new "Сказать Эмме избавиться от этого"

    old "Tell Emma to keep it"
    new "Сказать Эмме оставить это"

    old "Tell Harmony you understand the moral of the story"
    new "Сказать Хармони, что ты понял мораль истории"

    old "Tell her"
    new "Рассказать ей"

    old "Tell her about the cheating"
    new "Рассказать ей об измене"

    old "Tell her how it's gonna be"
    new "Сказать ей, как всё будет"

    old "Tell her it's forbidden"
    new "Сказать, что ей запрещено"

    old "Tell her it's her round"
    new "Сказать, что теперь её очередь"

    old "Tell her it's probably Ryan's"
    new "Сказать ей, что ребёнок, скорее всего, от Райана"

    old "Tell her it's unhealthy"
    new "Сказать, что это вредно"

    old "Tell her not to do it"
    new "Сказать ей не делать этого"

    old "Tell her Ryan cheated"
    new "Сказать ей, что Райан изменял"

    old "Tell her she should go get a massage"
    new "Сказать, что ей стоит сходить на массаж"

    old "Tell her she should not eat that much"
    new "Сказать ей, что не стоит столько есть"

    old "Tell her she's a little late"
    new "Сказать ей, что она немного опоздала"

    old "Tell her she's in time"
    new "Сказать ей, что она вовремя"

    old "Tell her she's late"
    new "Сказать ей, что она опоздала"

    old "Tell her she's too fat"
    new "Сказать ей, что она слишком толстая"

    old "Tell her that she'll be okay"
    new "Сказать ей, что всё будет хорошо"

    old "Tell her to abort"
    new "Сказать ей сделать аборт"

    old "Tell her to do her job"
    new "Сказать ей выполнять свою работу"

    old "Tell her to give you a titty fuck"
    new "Сказать ей подрочить тебе сиськами"

    old "Tell her to have an abortion"
    new "Сказать ей сделать аборт"

    old "Tell her to hurry up"
    new "Сказать ей поторопиться"

    old "Tell her to keep it quiet"
    new "Сказать ей не шуметь"

    old "Tell her to keep the baby"
    new "Сказать ей оставить ребёнка"

    old "Tell her to keep the baby and that you will support her"
    new "Сказать ей оставить ребёнка и обещать поддержку"

    old "Tell her to moderate herself"
    new "Сказать ей быть умереннее"

    old "Tell her to never do that again"
    new "Сказать ей больше никогда так не делать"

    old "Tell her to shut up"
    new "Сказать ей заткнуться"

    old "Tell her to slow down"
    new "Сказать ей сбавить темп"

    old "Tell her to stay"
    new "Сказать ей остаться"

    old "Tell her to suck you"
    new "Сказать ей отсосать"

    old "Tell her you forgive her"
    new "Сказать, что ты её прощаешь"

    old "Tell her you'll pay for it"
    new "Сказать, что ты за это заплатишь"

    old "Tell Kylie off for climbing over the fence"
    new "Отчитать Кайли за то, что перелезла через забор"

    old "Tell Kylie that you are mad at her"
    new "Сказать Кайли, что ты на неё злишься"

    old "Tell Lexi to give the Master a blow-job"
    new "Сказать Лекси сделать Мастеру минет"

    old "Tell me about you"
    new "Расскажи о себе"

    old "Tell me how you want it."
    new "Скажи, как ты этого хочешь"

    old "Tell me you'll call me."
    new "Скажи, что позвонишь мне"

    old "Tell me you're sure about this."
    new "Скажи, что ты уверена"

    old "Tell Minami off"
    new "Отчитать Минами"

    old "Tell off"
    new "Отчитать"

    old "Tell scary story"
    new "Рассказать страшную историю"

    old "Tell Scottie and Hanna off"
    new "Отчитать Скотти и Ханну"

    old "Tell someone else."
    new "Рассказать кому-нибудь другому"

    old "Tell the guy off"
    new "Отчитать парня"

    old "Tell the guy where to get off"
    new "Послать парня куда подальше"

    old "Tell the Master to fuck off"
    new "Послать Мастера куда подальше"

    old "Tell the Master to get lost"
    new "Сказать Мастеру проваливать"

    old "Tell the truth"
    new "Сказать правду"

    old "Tell the waitress to take the drink back"
    new "Попросить официантку унести напиток"

    old "Tendancious B"
    new "Tendancious B"

    old "text"
    new "сообщение"

    old "Text"
    new "Текст"

    old "Text Size Scaling"
    new "Масштабирование размера текста"

    old "text speed"
    new "скорость текста"

    old "Text-to-speech"
    new "Преобразование текста в речь"

    old "Thank you"
    new "Спасибо"

    old "Thanks"
    new "Спасибо"

    old "Thanks for understanding."
    new "Спасибо за понимание."

    old "That is blood money, I'm not taking it."
    new "Это кровавые деньги, я их не возьму"

    old "That seems reasonable"
    new "Звучит разумно"

    old "That sounds great"
    new "Звучит отлично"

    old "That would be nice"
    new "Было бы здорово"

    old "That's a bad idea"
    new "Это плохая идея"

    old "That's a great idea"
    new "Отличная идея"

    old "That's a great idea!"
    new "Отличная идея!"

    old "That's a one to one meeting."
    new "Это встреча один на один"

    old "That's a solid no"
    new "Однозначно нет"

    old "That's exactly what I was doing"
    new "Именно это я и делал"

    old "That's fine"
    new "Всё нормально"

    old "That's great."
    new "Это отлично"

    old "That's gross!"
    new "Это мерзко!"

    old "That's hot"
    new "Это горячо"

    old "That's hot!"
    new "Это горячо!"

    old "That's hot! I want pictures"
    new "Это горячо! Я хочу фотографии"

    old "That's not what I meant"
    new "Я не это имел в виду"

    old "That's not what you really want"
    new "Это не то, чего ты действительно хочешь"

    old "That's quite any outfit Lexi!"
    new "Вот это наряд, Лекси!"

    old "That's really spicy!"
    new "Это очень остро!"

    old "That's right."
    new "Именно так"

    old "That's too personal"
    new "Это слишком личное"

    old "That's what friends are for"
    new "Для этого и нужны друзья"

    old "That's wonderful"
    new "Это чудесно"

    old "The eldest pays the first round"
    new "Старшая оплачивает первый раунд"

    old "The Exorzists, yeetus, SomeoneWhoIsntMe, Tidus Reidan,"
    new "The Exorzists, yeetus, SomeoneWhoIsntMe, Tidus Reidan,"

    old "The first one, I think"
    new "Думаю, первый"

    old "The gallery is in an experimental state."
    new "Галерея находится в экспериментальном состоянии."

    old "The game data has been downloaded."
    new "Данные игры загружены."

    old "The girls seem to have something in mind"
    new "Кажется, девушки что-то задумали"

    old "The interactive director is not enabled here."
    new "Интерактивный директор недоступен."

    old "The man is at fault"
    new "Виноват мужчина"

    old "The more the better"
    new "Чем больше, тем лучше"

    old "The options on this menu are intended to improve accessibility. They may not work with all games, and some combinations of options may render the game unplayable. This is not an issue with the game or engine. For the best results when changing fonts, try to keep the text size the same as it originally was."
    new "Параметры этого меню предназначены для увеличения доступности. Они могут работать не со всеми играми, а некоторые комбинации опций могут сделать игру отображаемой некорректно. Это не проблема с игрой или движком. Для достижения наилучших результатов при изменении шрифтов старайтесь сохранять размер текста таким, каким он был изначально."

    old "The Ren'Py Sync server does not have a copy of this sync. The sync ID may be invalid, or it may have timed out."
    new "Сервер Ren'Py Sync не имеет копии этой синхронизации. Возможно, Sync ID недействителен или с истёкшим временем действия."

    old "The Ren'Py Sync server timed out."
    new "Сервер Ren'Py Sync не ответил вовремя."

    old "The right girl hasn't come along yet"
    new "Подходящая девушка пока не встретилась"

    old "The second one was great"
    new "Второй был отличным"

    old "The smart move is to walk away"
    new "Разумнее всего уйти"

    old "The sync belongs to a different game."
    new "Синхронизация относится к другой игре."

    old "The sync contains a file with an invalid name."
    new "Синхронизация содержит файл с недопустимым именем."

    old "The sync could not be decrypted."
    new "Невозможно расшифровать синхронизацию."

    old "The sync ID is not in the correct format."
    new "Sync ID имеет неправильный формат."

    old "The Sync ID is:"
    new "Sync ID:"

    old "The update file does not have the correct digest - it may have been corrupted."
    new "Файл обновления не содержит корректного дайджеста — он может быть повреждён."

    old "The update file was not downloaded."
    new "Файл обновления не был загружен."

    old "The updates have been installed."
    new "Обновления были установлены."

    old "The updates have been installed. The program will restart."
    new "Обновления установлены. Программа будет перезапущена."

    old "The updates were cancelled."
    new "Обновления были отменены."

    old "The usual."
    new "Как обычно"

    old "The {a=edit:1:log.txt}log.txt{/a} file may contain information to help you determine what is wrong with your computer."
    new "Файл {a=edit:1:log.txt}log.txt{/a} может содержать сведения, которые помогут определить причину проблемы с компьютером."

    old "themadsciencedivison, Obey Monster, JD, PoorMorale,"
    new "themadsciencedivison, Obey Monster, JD, PoorMorale,"

    old "Theme park"
    new "Парк аттракционов"

    old "Then let's talk about something else"
    new "Тогда давай поговорим о другом"

    old "ThePostalGamer, Nir Zonenshtein, Rykia, Jonas Hueber,"
    new "ThePostalGamer, Nir Zonenshtein, Rykia, Jonas Hueber,"

    old "There are no stories to show"
    new "Нет доступных сюжетов"

    old "There's no way."
    new "Ни за что"

    old "There's nothing between me and [bree.name] or Sasha!"
    new "Между мной и [bree.name] или Сашей ничего нет!"

    old "They both need me too"
    new "Я тоже им нужен"

    old "They keep going!"
    new "Они продолжают!"

    old "They listen"
    new "Они слушаются"

    old "They open at 9"
    new "Они открываются в девять"

    old "They would be better with me"
    new "Со мной им было бы лучше"

    old "They're great"
    new "Они отличные"

    old "They're okay"
    new "Они нормальные"

    old "They're sluts"
    new "Они шлюхи"

    old "Think about Aletta's breasts"
    new "Думать о груди Алетты"

    old "Think about Aletta's pussy"
    new "Думать о киске Алетты"

    old "Think about an office intern"
    new "Думать об офисной стажёрке"

    old "Think of an answer."
    new "Придумать ответ"

    old "This account does not have permission to perform an update."
    new "У этого аккаунта нет прав проводить обновление."

    old "This account does not have permission to write the update log."
    new "У этого аккаунта нет прав писать лог обновления."

    old "This computer has a problem displaying graphics: [problem]."
    new "На этом компьютере возникла проблема с отображением графики: [problem]."

    old "This computer is using software rendering."
    new "На этом компьютере используется программный рендеринг."

    old "This could be beneficial for both of us"
    new "Это может быть выгодно нам обоим"

    old "This game cannot be run until the game data has been downloaded."
    new "Эту игру невозможно запустить до тех пор, пока не будут загружены данные игры."

    old "This game contains a lot of sexual themes and situations, also boobies. So if you don't like those please refer to number one."
    new "В игре много сексуальных тем и ситуаций, а ещё сисек. Если вам это не нравится, смотрите пункт первый."

    old "This game is intended for mature audiences only so if you are not legally adult in your residence country please press Alt+F4 and go play Fortnite."
    new "Игра предназначена только для взрослой аудитории. Если по законам вашей страны вы ещё не достигли совершеннолетия, нажмите Alt+F4 и идите играть в Fortnite."

    old "This game is intended to be funny (hopefully it succeeds). All characters, names, locations are purely fictitious and any resemblance is purely coincidental."
    new "Игра должна быть смешной (надеемся, у неё получается). Все персонажи, имена и места полностью вымышлены, а любые совпадения случайны."

    old "This game requires use of GL2 that can't be initialised."
    new "Этой игре требуется GL2, но его не удалось инициализировать."

    old "This is a date!"
    new "Это свидание!"

    old "This is too much for you, let it go"
    new "Для тебя это слишком, отпусти ситуацию"

    old "This program contains free software under a number of licenses, including the MIT License and GNU Lesser General Public License. A complete list of software, including links to full source code, can be found {a=https://www.renpy.org/l/license}here{/a}."
    new "Эта программа содержит свободное и открытое программное обеспечение под несколькими лицензиями, включая лицензию MIT и GNU Lesser General Public. Полный список лицензий, включая ссылки на полный исходный код, можно найти {a=https://www.renpy.org/l/license}здесь{/a}."

    old "This program is up to date."
    new "Эта программа обновлена."

    old "This save was created on a different device. Maliciously constructed save files can harm your computer. Do you trust this save's creator and everyone who could have changed the file?"
    new "Это сохранение было создано на другом устройстве. Злонамеренно созданные файлы сохранения могут нанести вред вашему компьютеру. Доверяете ли вы создателю этого сохранения и всем тем, кто мог изменить файл?"

    old "This was... a lot... I don't think I can do it again..."
    new "Это было... слишком... Не думаю, что смогу повторить..."

    old "This will contact the {a=https://sync.renpy.org}Ren'Py Sync Server{/a}."
    new "Это позволит связаться с сервером {a=https://sync.renpy.org}Ren'Py Sync{/a}."

    old "This will update the game."
    new "Игра будет обновлена."

    old "This will upload your saves to the {a=https://sync.renpy.org}Ren'Py Sync Server{/a}.\nDo you want to continue?"
    new "Это загрузит ваши сохранения на сервер {a=https://sync.renpy.org}Ren'Py Sync{/a}.\nВы хотите продолжить?"

    old "Throw in an innuendo"
    new "Добавить двусмысленный намёк"

    old "Tighten the dog collar round Sasha's neck"
    new "Затянуть собачий ошейник на шее Саши"

    old "Time to let her have it!"
    new "Пора как следует ей дать!"

    old "Time to use the gun I've got"
    new "Пора использовать пистолет"

    old "Tiramisu"
    new "Тирамису"

    old "Titty job"
    new "Подрочить сиськами"

    old "To mark you"
    new "Чтобы отметить тебя"

    old "To play this game, you'll need to download some data. If you're not on WiFi, you could be charged for it."
    new "Чтобы играть, необходимо скачать дополнительные данные. При отсутствии Wi-Fi оператор может взимать плату за трафик."

    old "To the sunset and beyond !!! (leads to an ending)"
    new "Навстречу закату и дальше!!! (приводит к концовке)"

    old "Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}."
    new "Включает или отключает вспомогательное {a=https://www.renpy.org/l/voicing}озвучивание текста{/a}"

    old "Toggles assistive {color=#00ff00}{a=https://www.renpy.org/l/voicing}self-voicing{/a}{/color}."
    new "Включает или отключает вспомогательное {color=#00ff00}{a=https://www.renpy.org/l/voicing}озвучивание текста{/a}{/color}"

    old "Toggles dialogue skipping."
    new "Включает или отключает пропуск диалогов"

    old "Too busy"
    new "Слишком занят"

    old "Too fancy for me"
    new "Для меня это слишком пафосно"

    old "Topless"
    new "Топлес"

    old "Tough choice"
    new "Сложный выбор"

    old "Traits"
    new "Черты"

    old "Transforms:"
    new "Трансформации:"

    old "Transition:"
    new "Переходы:"

    old "Transitions"
    new "Переходы"

    old "transitions"
    new "переходы"

    old "Translation identifier: [identifier]"
    new "Идентификатор перевода: [identifier]"

    old "Treat the matches as \"real\""
    new "Считать поединки «настоящими»"

    old "Treat the matches as fake"
    new "Считать поединки постановочными"

    old "Treat the matches as real"
    new "Считать поединки настоящими"

    old "Tree"
    new "Дерево"

    old "Troy Sewell, Rookie One, Nattie, Azrael morningstar,"
    new "Troy Sewell, Rookie One, Nattie, Azrael morningstar,"

    old "Try a more subtle approach"
    new "Попробовать более тонкий подход"

    old "Try something else"
    new "Попробовать что-нибудь другое"

    old "Try to be positive"
    new "Попытаться мыслить позитивно"

    old "Try to calm both girls down"
    new "Попытаться успокоить обеих девушек"

    old "Try to catch it in your mouth"
    new "Попытаться поймать это ртом"

    old "Try to defuse the situation"
    new "Попытаться разрядить обстановку"

    old "Try to ease the tension."
    new "Попытаться разрядить обстановку"

    old "Try to ignore the inconvenience"
    new "Попытаться не обращать внимания на неудобство"

    old "Try to play peacemaker"
    new "Попытаться всех примирить"

    old "Try to remain neutral"
    new "Постараться сохранить нейтралитет"

    old "Try to sound confident"
    new "Постараться говорить уверенно"

    old "Try to sound sensitive"
    new "Постараться говорить деликатно"

    old "Try to stay awake"
    new "Попытаться не заснуть"

    old "Try to stay neutral"
    new "Постараться сохранить нейтралитет"

    old "Turn around."
    new "Повернись"

    old "Turn down the party"
    new "Отказаться от вечеринки"

    old "Turn her away"
    new "Отвернуть её"

    old "U"
    new "U"

    old "u"
    new "u"

    old "Underwear"
    new "Нижнее бельё"

    old "Underwear outfit"
    new "Нижнее бельё"

    old "Unfortunately, your save is not compatible with this game version."
    new "К сожалению, ваше сохранение несовместимо с этой версией игры."

    old "Uniform policy"
    new "Правила униформы"

    old "University"
    new "Университет"

    old "Unless you want me to"
    new "Если только ты сама этого не хочешь"

    old "Unpacking the game data."
    new "Распаковка данных игры."

    old "Unpacking the updates."
    new "Распаковка обновлений."

    old "Unseen Text"
    new "Непрочитанное"

    old "Until then, you're my property"
    new "А до тех пор ты моя собственность"

    old "Update"
    new "Обновить"

    old "Updater"
    new "Обновление"

    old "Use a baseball bat"
    new "Использовать бейсбольную биту"

    old "Use a condom"
    new "Использовать презерватив"

    old "Use a parasol"
    new "Использовать пляжный зонт"

    old "Use anal beads"
    new "Использовать анальные шарики"

    old "Use anal beads on [bree.name]"
    new "Использовать анальные шарики на [bree.name]"

    old "Use anal beads on Minami"
    new "Использовать анальные шарики на Минами"

    old "Use anal beads on Sasha"
    new "Использовать анальные шарики на Саше"

    old "Use blindfold"
    new "Использовать повязку на глаза"

    old "Use Brains"
    new "Использовать ум"

    old "Use Brawn"
    new "Использовать силу"

    old "Use dildo and my finger."
    new "Использовать дилдо и палец"

    old "Use dildo on [bree.name]'s ass"
    new "Использовать дилдо в заднице [bree.name]"

    old "Use dildo on [bree.name]'s pussy"
    new "Использовать дилдо в киске [bree.name]"

    old "Use double dildo on [bree.name]"
    new "Использовать двойной дилдо на [bree.name]"

    old "Use double dildo on both girls"
    new "Использовать двойной дилдо на обеих девушках"

    old "Use double dildo on Minami"
    new "Использовать двойной дилдо на Минами"

    old "Use electrodes"
    new "Использовать электроды"

    old "Use her on the desk"
    new "Использовать её на столе"

    old "Use manual authentication"
    new "Использовать ручную авторизацию"

    old "Use my natural color"
    new "Оставить естественный цвет"

    old "Use my tongue"
    new "Использовать язык"

    old "Use protection"
    new "Использовать защиту"

    old "Use ropes"
    new "Использовать верёвки"

    old "Use some toy"
    new "Использовать какую-нибудь игрушку"

    old "Use the anal beads"
    new "Использовать анальные шарики"

    old "Use the dildo"
    new "Использовать дилдо"

    old "Use the gag ball"
    new "Использовать кляп-шар"

    old "Use the nipple clamps"
    new "Использовать зажимы для сосков"

    old "Use the paddle"
    new "Использовать паддл"

    old "Use the rope"
    new "Использовать верёвку"

    old "Use the rope again"
    new "Снова использовать верёвку"

    old "Use the vibrator"
    new "Использовать вибратор"

    old "Use the whip"
    new "Использовать плеть"

    old "Use vibrator and my finger."
    new "Использовать вибратор и палец"

    old "V"
    new "V"

    old "v"
    new "v"

    old "valid_token:"
    new "действительный токен:"

    old "Vanilla"
    new "Классика"

    old "Version [config.version!t]\n"
    new "Версия [config.version!t]"

    old "vertical scroll"
    new ". вертикальная полоса прокрутки"

    old "VERY IMPORTANT PATRONS"
    new "ОСОБО ВАЖНЫЕ ПАТРОНЫ"

    old "Vibrator"
    new "Вибратор"

    old "Video Games"
    new "Видеоигры"

    old "video sprites"
    new "видео-спрайты"

    old "viewport"
    new "порт просмотра"

    old "ViPo, Norberis, Long Shot, Unknown Player, Donald Kane,"
    new "ViPo, Norberis, Long Shot, Unknown Player, Donald Kane,"

    old "Visit Sasha and Palla at the store"
    new "Навестить Сашу и Паллу в магазине"

    old "VOICE ACTORS"
    new "АКТЁРЫ ОЗВУЧИВАНИЯ"

    old "voice after game menu"
    new "голос после меню игры"

    old "voice sustain"
    new "не останавливать голос"

    old "Voice Volume"
    new "Громкость голоса"

    old "voice volume"
    new "громкость голоса"

    old "VoiceLikeCandy as Anna"
    new "VoiceLikeCandy — Анна"

    old "W"
    new "W"

    old "w"
    new "w"

    old "Wade in and pull the other girl off"
    new "Вмешаться и оттащить другую девушку"

    old "Wait"
    new "Подождать"

    old "Wait a little more"
    new "Подождать ещё немного"

    old "Wait for an opening to pass"
    new "Ждать возможности для обгона"

    old "Wait for her"
    new "Подождать её"

    old "wait for voice"
    new "ждать голос"

    old "Wait patiently"
    new "Терпеливо ждать"

    old "Wait patiently for the waiter's attention"
    new "Терпеливо ждать внимания официанта"

    old "Wait until you get home (Never meet Harmony again)"
    new "Подождать до дома (больше никогда не встречаться с Хармони)"

    old "Wake her up gently"
    new "Осторожно разбудить её"

    old "Wake her up with kiss"
    new "Разбудить её поцелуем"

    old "Walk away"
    new "Уйти"

    old "Walk off the dance-floor"
    new "Уйти с танцпола"

    old "Walk Sasha home"
    new "Проводить Сашу домой"

    old "Walk up and introduce yourself as a former student"
    new "Подойти и представиться бывшим учеником"

    old "Walk up and just introduce yourself"
    new "Подойти и просто представиться"

    old "Want You"
    new "Хочу тебя"

    old "Warn her"
    new "Предупредить её"

    old "Warn the lady your \"Fury Road\" mode is on!"
    new "Предупредить даму, что включён режим «Дорога ярости»!"

    old "WARNING!"
    new "ВНИМАНИЕ!"

    old "Was this a joke?"
    new "Это была шутка?"

    old "Watch"
    new "Смотреть"

    old "Watch from outside the booth"
    new "Смотреть снаружи кабинки"

    old "Watch Lexi masturbate"
    new "Смотреть, как Лекси мастурбирует"

    old "Watch the footage"
    new "Посмотреть запись"

    old "Watching T.V."
    new "Просмотр телевизора"

    old "Watching you be a bitch is better than TV"
    new "Смотреть, как ты ведёшь себя как сучка, лучше телевизора"

    old "Wave her out"
    new "Отослать её жестом"

    old "We are not"
    new "Нет"

    old "We can do that"
    new "Мы можем так сделать"

    old "We can share"
    new "Мы можем поделиться"

    old "We can try"
    new "Мы можем попробовать"

    old "We had so much fun"
    new "Нам было так весело"

    old "We need women to lead us"
    new "Нам нужны женщины, которые будут нами руководить"

    old "We should explore it"
    new "Нам стоит это исследовать"

    old "We should join in"
    new "Нам стоит присоединиться"

    old "We should keep it"
    new "Нам стоит оставить это"

    old "We should leave"
    new "Нам стоит уйти"

    old "We should move on from each other"
    new "Нам стоит отпустить друг друга"

    old "We should report"
    new "Нам стоит сообщить"

    old "We should wait a little more."
    new "Нам стоит подождать ещё немного"

    old "We should wait."
    new "Нам стоит подождать"

    old "We shouldn't make a habit of this."
    new "Нам не стоит превращать это в привычку"

    old "We will come here again"
    new "Мы ещё сюда придём"

    old "We will make great music"
    new "Мы создадим отличную музыку"

    old "We'll always be both"
    new "Мы всегда будем и теми, и другими"

    old "We'll be great parents"
    new "Мы будем отличными родителями"

    old "We'll use the desk again."
    new "Снова используем стол"

    old "We're here now aren't we?"
    new "Но мы ведь уже здесь, верно?"

    old "We're out of Benji episodes, what next?"
    new "Серии Бенджи закончились. Что дальше?"

    old "We're waiting Camila"
    new "Мы ждём Камилу"

    old "Wear makeup"
    new "Нанеси макияж"

    old "Wear your collar"
    new "Надень ошейник"

    old "web cache preload"
    new "предварительная загрузка веб-кэша"

    old "Well, I like that!"
    new "Ну, мне это нравится!"

    old "Wendigo The Lewd, Abi Usus, Nino Chief, Matthew Dennis,"
    new "Wendigo The Lewd, Abi Usus, Nino Chief, Matthew Dennis,"

    old "Were you listening to me at all?"
    new "Ты вообще меня слушал?"

    old "What are the chances"
    new "Каковы были шансы?"

    old "What are you talking about"
    new "О чём ты говоришь?"

    old "What crap"
    new "Что за чушь"

    old "What do you have in mind?"
    new "Что ты задумала?"

    old "What do you know about the investigation?"
    new "Что тебе известно о расследовании?"

    old "What do you want me to do?"
    new "Что мне сделать?"

    old "What have you done?"
    new "Что ты натворила?"

    old "What if I said please?"
    new "А если я скажу «пожалуйста»?"

    old "What if I want more?"
    new "А если я хочу большего?"

    old "What if we did it in alphabetical order?"
    new "А если идти в алфавитном порядке?"

    old "What is inside the package?"
    new "Что внутри посылки?"

    old "What is your birthday?"
    new "Когда у вас день рождения?"

    old "What is your first name and last name?"
    new "Как вас зовут?"

    old "What's wrong with girls in pink dresses?"
    new "Что не так с девушками в розовых платьях?"

    old "What's wrong?"
    new "Что случилось?"

    old "Whatever"
    new "Без разницы"

    old "Whatever I want? Like... sex?"
    new "Что захочу? Например... секс?"

    old "Whatever keeps you in line"
    new "Всё, что удержит тебя в рамках"

    old "Whatever you want to do is just fine with me."
    new "Что бы ты ни захотела делать, меня всё устроит"

    old "WHEEL DOWN"
    new "КОЛЕСО ВНИЗ"

    old "WHEEL UP"
    new "КОЛЕСО ВВЕРХ"

    old "When do you want the game to start?"
    new "Когда вы хотите начать игру?"

    old "When I do"
    new "Когда я это сделаю"

    old "When you are ready"
    new "Когда будешь готова"

    old "Where are you?"
    new "Где ты?"

    old "Where is the money?"
    new "Где деньги?"

    old "Where would you have gone?"
    new "Куда бы ты уехала?"

    old "While unpacking {}, unknown type {}."
    new "При распаковке {} обнаружен неизвестный тип {}."

    old "Whip"
    new "Плеть"

    old "Whistle and shake head"
    new "Присвистнуть и покачать головой"

    old "Who are we expecting to be at the meeting?"
    new "Кого мы ожидаем увидеть на встрече?"

    old "Who are you working with?"
    new "На кого ты работаешь?"

    old "Why are you looking for kids books?"
    new "Зачем тебе детские книги?"

    old "Why is it always bloody football"
    new "Почему всегда этот чёртов футбол?"

    old "Why not"
    new "Почему бы и нет"

    old "Why not the black cat"
    new "Почему не чёрный кот?"

    old "Why not?"
    new "Почему бы и нет?"

    old "Why should I believe you?"
    new "Почему я должен тебе верить?"

    old "Wieners first!"
    new "Сначала сосиски!"

    old "wiki"
    new "вики"

    old "Wiki"
    new "Вики"

    old "Window"
    new "Оконный режим"

    old "Winter"
    new "Зима"

    old "Wipe the footage out of regret"
    new "Удалить запись из-за угрызений совести"

    old "with "
    new "с"

    old "Wolf"
    new "Волк"

    old "Women are our leaders"
    new "Женщины должны нами руководить"

    old "Work"
    new "Работа"

    old "Work extra hours at the strip club"
    new "Поработай сверхурочно в стрип-клубе"

    old "Work fast"
    new "Работать быстро"

    old "Work normally"
    new "Работать как обычно"

    old "Work uniform"
    new "Рабочая униформа"

    old "Working"
    new "Работа"

    old "Working out"
    new "Тренировки"

    old "Wow thanks Shiori"
    new "Ого, спасибо, Сиори"

    old "Wow there! You can't be serious about this one!"
    new "Ого! Ты же не всерьёз насчёт этого?"

    old "Wrestling is fake!"
    new "Рестлинг — постановка!"

    old "WRITERS"
    new "СЦЕНАРИСТЫ"

    old "WTF Lexi!"
    new "Какого хрена, Лекси?!"

    old "X"
    new "X"

    old "x"
    new "x"

    old "Y"
    new "Y"

    old "y"
    new "y"

    old "Y/Top Button"
    new "Y/Верхняя кнопка"

    old "Yeah"
    new "Ага"

    old "Yeah on second thought... I think I'm not ready for it yet..."
    new "Да, если подумать... похоже, я пока не готов..."

    old "Yeah!!!"
    new "Да!!!"

    old "Yeah, 2 years. Time flies uh!"
    new "Да, два года. Время летит, да?"

    old "Yeah, I guess it's different..."
    new "Да, наверное, это по-другому..."

    old "Yeah, I'd love to do something together with you."
    new "Да, я с удовольствием что-нибудь сделаю вместе с тобой"

    old "Yeah, she is"
    new "Да, она такая"

    old "Yeah, she likes it"
    new "Да, ей это нравится"

    old "Yeah, these girls deserve a spanking."
    new "Да, эти девушки заслуживают порки"

    old "Yes"
    new "Да"

    old "YES"
    new "ДА"

    old "Yes boss"
    new "Да, босс"

    old "Yes!"
    new "Да!"

    old "Yes, but not with her"
    new "Да, но не с ней"

    old "Yes, I'd love to go out with you"
    new "Да, я с удовольствием пойду с тобой на свидание"

    old "Yes, it's weird"
    new "Да, это странно"

    old "Yes, later"
    new "Да, позже"

    old "Yes, Mistress"
    new "Да, Госпожа"

    old "Yes, now"
    new "Да, сейчас"

    old "Yes, that was worth it"
    new "Да, оно того стоило"

    old "You"
    new "Ты"

    old "You already know"
    new "Ты уже знаешь"

    old "You are a burden"
    new "Ты обуза"

    old "You are a nice person"
    new "Ты хороший человек"

    old "You are a nice sextoy"
    new "Ты хорошая секс-игрушка"

    old "You are a slut"
    new "Ты шлюха"

    old "You are my prized sex slave"
    new "Ты моя ценная секс-рабыня"

    old "You are not prepared at all..."
    new "Ты совсем не подготовлена..."

    old "You are plenty smart"
    new "Ты достаточно умна"

    old "You better have it."
    new "Лучше бы они у тебя были"

    old "You can always come to me if you need help."
    new "Если понадобится помощь, всегда можешь обратиться ко мне"

    old "You can do so by clicking on the button below."
    new "Для этого нажмите кнопку ниже."

    old "You can tell me anything"
    new "Ты можешь рассказать мне всё"

    old "You can trust me"
    new "Ты можешь мне доверять"

    old "You can use this ID to download your save on another device.\nThis sync will expire in an hour.\nRen'Py Sync is supported by {a=https://www.renpy.org/sponsors.html}Ren'Py's Sponsors{/a}."
    new "Вы можете использовать этот ID для загрузки сохранения на другое устройство.\nСрок действия этой синхронизации истечёт через час.\nRen'Py Sync поддерживается {a=https://www.renpy.org/sponsors.html}спонсорами Ren'Py{/a}."

    old "You could be"
    new "Ты могла бы"

    old "You could have given her one from me"
    new "Ты могла передать ей один от меня"

    old "You could make it more attractive"
    new "Ты могла бы сделать это привлекательнее"

    old "You could model in person instead, if you like"
    new "Можешь вместо этого попозировать лично, если хочешь"

    old "You deserve a naughty reward"
    new "Ты заслуживаешь непристойную награду"

    old "You deserve it"
    new "Ты это заслужила"

    old "You didn't bother me."
    new "Ты мне не помешала"

    old "You didn't just ask daddy"
    new "Ты ведь не спросила папочку"

    old "You didn't need to pretend"
    new "Тебе не нужно было притворяться"

    old "You didn't really know who you were"
    new "Ты и сама толком не понимала, кто ты"

    old "You do not have a choice"
    new "У тебя нет выбора"

    old "You have nothing to be sorry about."
    new "Тебе не за что извиняться"

    old "You have to do it alone"
    new "Ты должна сделать это сама"

    old "You just needed to be yourself"
    new "Тебе просто нужно было быть собой"

    old "You just needed to try harder"
    new "Тебе просто нужно было лучше стараться"

    old "You kept me waiting."
    new "Ты заставила меня ждать"

    old "You look badass"
    new "Ты выглядишь круто"

    old "You look like you're having trouble."
    new "Похоже, у тебя проблемы"

    old "You look stunning Harmony!"
    new "Ты потрясающе выглядишь, Хармони!"

    old "You may go"
    new "Можешь идти"

    old "You said cute twice"
    new "Ты дважды сказала «милая»"

    old "You seem a little overstressed"
    new "Кажется, ты слишком напряжена"

    old "You seem more confident"
    new "Ты кажешься увереннее"

    old "You should abort"
    new "Тебе стоит сделать аборт"

    old "You should ask me"
    new "Тебе стоит спросить меня"

    old "You should be a girl"
    new "Тебе стоит быть девушкой"

    old "You should be my girlfriend"
    new "Тебе стоит стать моей девушкой"

    old "You should be whatever you want to be"
    new "Будь кем захочешь"

    old "You should both go"
    new "Вам обеим стоит пойти"

    old "You should buy a mirror"
    new "Тебе стоит купить зеркало"

    old "You should get an abortion"
    new "Тебе стоит сделать аборт"

    old "You should give him a second chance"
    new "Тебе стоит дать ему второй шанс"

    old "You should go"
    new "Тебе стоит уйти"

    old "You should have a termination"
    new "Тебе стоит прервать беременность"

    old "You should have some of the pastries too"
    new "Тебе тоже стоит попробовать выпечку"

    old "You should have told me."
    new "Тебе стоило мне сказать"

    old "You should have warn us Lexi!"
    new "Тебе стоило нас предупредить, Лекси!"

    old "You should leave"
    new "Тебе стоит уйти"

    old "You should not do it"
    new "Тебе не стоит этого делать"

    old "You should practice more"
    new "Тебе стоит больше репетировать"

    old "You should really tell me before you run off next time."
    new "В следующий раз тебе стоит предупредить меня, прежде чем убегать"

    old "You should sell it"
    new "Тебе стоит продать это"

    old "You should sleep here"
    new "Тебе стоит спать здесь"

    old "You should start taking the pill"
    new "Тебе стоит начать принимать таблетки"

    old "You should stop taking the pill"
    new "Тебе стоит перестать принимать таблетки"

    old "You should try"
    new "Тебе стоит попробовать"

    old "You should work on your small talk"
    new "Тебе стоит поработать над светской беседой"

    old "You shouldn't defile your body"
    new "Тебе не стоит осквернять своё тело"

    old "You shouldn't smoke"
    new "Тебе не стоит курить"

    old "You too"
    new "Ты тоже"

    old "You were a handful too!"
    new "Ты тоже была той ещё занозой!"

    old "You were great."
    new "Ты была великолепна"

    old "You were not exactly on time either Harmony!"
    new "Ты тоже пришла не совсем вовремя, Хармони!"

    old "You were some rider!"
    new "Ты была ещё той наездницей!"

    old "You weren't just a tomboy!"
    new "Ты была не просто пацанкой!"

    old "You will encounter bugs and issues."
    new "Вы можете столкнуться с ошибками и проблемами."

    old "You will get what you deserve."
    new "Ты получишь по заслугам"

    old "You won't finish your plates, won't you?"
    new "Вы ведь не доедите свои порции?"

    old "You'll have to do more than that"
    new "Тебе придётся сделать больше"

    old "You're both incredible!"
    new "Вы обе невероятны!"

    old "You're doing this"
    new "Ты это сделаешь"

    old "You're invading my personal space"
    new "Ты нарушаешь моё личное пространство"

    old "You're mine"
    new "Ты моя"

    old "You're not as cute as the bartender"
    new "Ты не такая милая, как барменша"

    old "You're not much better"
    new "Ты не намного лучше"

    old "You're right"
    new "Ты права"

    old "You're right, it's unique."
    new "Ты права, это уникально"

    old "You're right, let's camp close"
    new "Ты права, давай разобьём лагерь поближе"

    old "You're right, those tits are for me to ogle"
    new "Ты права, эти сиськи предназначены для моих взглядов"

    old "You're right. Sasha's a goddess."
    new "Ты права. Саша — богиня"

    old "You're the only one Sam."
    new "Сэм, ты у меня единственная"

    old "Your place"
    new "У тебя"

    old "Z"
    new "Z"

    old "z"
    new "z"

    old "Zack's great"
    new "Зак отличный"

    old "Zaidan as Jack"
    new "Zaidan — Джек"

    old "zampa16, Bruce Burke, BiggusBonggus, Scar, Damian Derby,"
    new "zampa16, Bruce Burke, BiggusBonggus, Scar, Damian Derby,"

    old "Zhang Qian, Nick, Luke Richardson, Mirogan, Chrono Designs,"
    new "Zhang Qian, Nick, Luke Richardson, Mirogan, Chrono Designs,"

    old "ZhiZhong Yan, Arruzaki, Ian Ponce, Dagon.san, kyle holland,"
    new "ZhiZhong Yan, Arruzaki, Ian Ponce, Dagon.san, kyle holland,"

    old "Zih Kidwell, Andrew Kennedy, Tesserakt, Jan DÃ¼rr, Laziy,"
    new "Zih Kidwell, Andrew Kennedy, Tesserakt, Jan DÃ¼rr, Laziy,"

    old "Zimmaster7, Herecomethepit, dblkrose, Lexi Mace,"
    new "Zimmaster7, Herecomethepit, dblkrose, Lexi Mace,"

    old "{#auto_page}A"
    new "{#auto_page}A"

    old "{#month_short}Apr"
    new "{#month_short}Апр"

    old "{#month_short}Aug"
    new "{#month_short}Авг"

    old "{#month_short}Dec"
    new "{#month_short}Дек"

    old "{#month_short}Feb"
    new "{#month_short}Фев"

    old "{#month_short}Jan"
    new "{#month_short}Янв"

    old "{#month_short}Jul"
    new "{#month_short}Июл"

    old "{#month_short}Jun"
    new "{#month_short}Июн"

    old "{#month_short}Mar"
    new "{#month_short}Мар"

    old "{#month_short}May"
    new "{#month_short}Мая"

    old "{#month_short}Nov"
    new "{#month_short}Ноя"

    old "{#month_short}Oct"
    new "{#month_short}Окт"

    old "{#month_short}Sep"
    new "{#month_short}Сен"

    old "{#month}April"
    new "{#month}апреля"

    old "{#month}August"
    new "{#month}августа"

    old "{#month}December"
    new "{#month}декабря"

    old "{#month}February"
    new "{#month}февраля"

    old "{#month}January"
    new "{#month}января"

    old "{#month}July"
    new "{#month}июля"

    old "{#month}June"
    new "{#month}июня"

    old "{#month}March"
    new "{#month}марта"

    old "{#month}May"
    new "{#month}мая"

    old "{#month}November"
    new "{#month}ноября"

    old "{#month}October"
    new "{#month}октября"

    old "{#month}September"
    new "{#month}сентября"

    old "{#quick_page}Q"
    new "{#quick_page}Q"

    old "{#weekday_short}Fri"
    new "{#weekday_short}Пт"

    old "{#weekday_short}Mon"
    new "{#weekday_short}Пн"

    old "{#weekday_short}Sat"
    new "{#weekday_short}Сб"

    old "{#weekday_short}Sun"
    new "{#weekday_short}Вс"

    old "{#weekday_short}Thu"
    new "{#weekday_short}Чт"

    old "{#weekday_short}Tue"
    new "{#weekday_short}Вт"

    old "{#weekday_short}Wed"
    new "{#weekday_short}Ср"

    old "{#weekday}Friday"
    new "{#weekday}Пятница"

    old "{#weekday}Monday"
    new "{#weekday}Понедельник"

    old "{#weekday}Saturday"
    new "{#weekday}Суббота"

    old "{#weekday}Sunday"
    new "{#weekday}Воскресенье"

    old "{#weekday}Thursday"
    new "{#weekday}Четверг"

    old "{#weekday}Tuesday"
    new "{#weekday}Вторник"

    old "{#weekday}Wednesday"
    new "{#weekday}Среда"

    old "{b}Age:{/b} [girl.age + girl.flags.age_increase]"
    new "{b}Возраст:{/b} [girl.age + girl.flags.age_increase]"

    old "{b}Babies:{/b} [babies]"
    new "{b}Дети:{/b} [babies]"

    old "{b}Birth control:{/b} No"
    new "{b}Контрацепция:{/b} Нет"

    old "{b}Birth control:{/b} Yes"
    new "{b}Контрацепция:{/b} Да"

    old "{b}Children:{/b} [hero.children]"
    new "{b}Дети:{/b} [hero.children]"

    old "{b}Fertility:{/b} [girl.fertility]%"
    new "{b}Фертильность:{/b} [girl.fertility]%"

    old "{b}Fertility:{/b} [hero.fertility]%"
    new "{b}Фертильность:{/b} [hero.fertility]%"

    old "{b}Fertility:{/b} Pregnant"
    new "{b}Фертильность:{/b} Беременна"

    old "{b}Job (day):{/b} [job_day]"
    new "{b}Работа (дневная):{/b} [job_day]"

    old "{b}Job (night):{/b} [job_night]"
    new "{b}Работа (ночная):{/b} [job_night]"

    old "{b}Job{/b}"
    new "{b}Работа{/b}"

    old "{b}Name:{/b} [girl.name]"
    new "{b}Имя:{/b} [girl.name]"

    old "{b}Sex count:{/b} [girl.sexperience]"
    new "{b}Количество секса:{/b} [girl.sexperience]"

    old "{b}Sex:{/b} Female"
    new "{b}Пол:{/b} Женский"

    old "{b}Sex:{/b} Male"
    new "{b}Пол:{/b} Мужской"

    old "{b}Sexperience:{/b} [hero.sexperience]"
    new "{b}Секспириенс:{/b} [hero.sexperience]"

    old "{b}Sexperience:{/b} [hero.sexperience] ([hero.min_sexperience])"
    new "{b}Секспириенс:{/b} [hero.sexperience] ([hero.min_sexperience])"

    old "{b}Skills:{/b} [t]"
    new "{b}Навыки:{/b} [t]"

    old "{b}Status:{/b} [girl.status!c]"
    new "{b}Статус:{/b} [girl.status!c]"

    old "{b}Traits{/b}"
    new "{b}Черты{/b}"

    old "{color=#f00}Invalid token [persistent.authentication_token]{/color}"
    new "{color=#f00}Недействительный токен [persistent.authentication_token]{/color}"

    old "{color=#f00}Unable to get games ownership from [authentication_status.get('provider')]{/color}"
    new "{color=#f00}Не удалось получить данные о владении играми от [authentication_status.get('provider')]{/color}"

    old "{image=gui/icons/icon_[step.status_icon].png}"
    new "{image=gui/icons/icon_[step.status_icon].png}"

    old "{size=-3}[config.version!q]\n[renpy.version_only!q]\n[renpy.platform!q]{/size}"
    new "{size=-3}[config.version!q]\n[renpy.version_only!q]\n[renpy.platform!q]{/size}"

    old "{size=25}🔗{/size}"
    new "{size=25}🔗{/size}"

    old "|"
    new "|"

    old "~"
    new "~"

    old "‍✍️"
    new "‍✍️"

    old "‍🎂"
    new "‍🎂"

    old "‍🚩"
    new "‍🚩"

    old "←"
    new "←"

    old "⏎"
    new "⏎"

    old "␣"
    new "␣"

    old "▸"
    new "▸"

    old "✎"
    new "✎"

    old "❌"
    new "❌"

    old "❗"
    new "❗"

    old "⬆"
    new "⬆"

    old "⬇"
    new "⬇"

    old "📄"
    new "📄"

    old "🗑️"
    new "🗑️"
