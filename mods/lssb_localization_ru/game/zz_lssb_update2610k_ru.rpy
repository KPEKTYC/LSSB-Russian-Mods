# Russian text for game 26.10.0j-0k: generic dirty texts that now fit both genders (lists.dirty_text).
init 1125 python:
    # Lines new in 0k: a man's reply to the heroine, and three texts only sent between two women.
    renpy.game.script.translator.strings['russian'].translations.update({
        "You make me so hard :$": "У меня от тебя так стоит :$",
        "Your lip gloss is still on my thighs. Come put some more on.": "Твой блеск для губ всё ещё у меня на бёдрах. Приходи, добавь ещё.",
        "I keep thinking about your fingers. Bring them over here.": "Не выходят из головы твои пальчики. Давай их сюда.",
        "Tonight I want you on my face. No arguing.": "Сегодня ночью хочу, чтобы ты села мне на лицо. И никаких возражений.",
    })

    # Between two women the game reuses lines written to a man, and their Russian speaks to a man.
    # There the lines below get an ignored "{#ff}" tag, which selects a translation that speaks to a woman.
    _lssb_dirty_ff = {
        "Tell me all the dirty little things you do when you masturbate. Tell me everything, baby. Tell me how you play with yourself.": "Расскажи обо всех пошлостях, которые делаешь, когда ласкаешь себя. Расскажи всё, милая. Как ты себя трогаешь?",
        "Okay, babe, you can have any hole you want.": "Ладно, милая, можешь выбрать любую дырочку.",
        "Well, you stupid fucker, I won't let you fuck my ass... So what?": "Ну, стерва, я не дам тебе трахнуть меня в задницу... И что теперь?",
        "I want it all over me. Cover me with it.": "Хочу, чтобы всё было на мне. Залей меня с головы до ног.",
        "I can't stop thinking about last nights' sex, the way you tasted not to mention the way you made me feel.": "Не могу перестать думать о вчерашнем сексе: о твоём вкусе и о том, какие ощущения ты мне подарила.",
        "If you were here with me I would make you come so hard.": "Если бы ты была рядом, я заставила бы тебя кончить так сильно.",
        "Lying in bed and bored. Wish you were here to play Simon Says with me ;)": "Лежу в постели, скучаю. Вот бы ты была здесь — поиграли бы в «Саймон говорит» ;)",
        "If I were with you right now, where would you want me to touch you?": "Если бы я сейчас была рядом, где бы ты хотела почувствовать мои прикосновения?",
        "It involves my tongue and you, naked.": "В этих мыслях есть мой язык и ты, голая.",
        "I'm dying to find out if you are as good in real life as you are in my fantasies.": "Умираю от желания узнать, так ли ты хороша в жизни, как в моих фантазиях.",
        "I know you're not a wizard, but I think your mouth is pretty magical. I can think of a few places I want it right now.": "Знаю, ты не волшебница, но твои губы творят чудеса. Есть несколько мест, где я хотела бы почувствовать их прямо сейчас.",
        "Wait, maybe you ARE a wizard.": "Хотя погоди, может, ты всё-таки волшебница.",
        "If you were here right now I would tear your clothes off and shove you onto my bed and have my way with you.": "Если бы ты была здесь, я бы сорвала с тебя одежду, толкнула на кровать и сделала с тобой всё, что хочу.",
        "Just FYI.": "Просто чтобы ты знала.",
        "I'm touching myself right now. Wish you were here ;)": "Я сейчас ласкаю себя. Вот бы ты была рядом ;)",
        "If you're not busy later I was hoping to make passionate love to you.": "Если ты потом свободна, я бы хотела заняться с тобой страстной любовью.",
        "In fact, you need to tell me exactly where you're going to put them.": "И вообще, ты должна подробно рассказать, куда собираешься их положить.",
        "Some people say to-may-to. Some people say to-mah-to. I say I-want-you-right-now-you-sexy-beast.": "Кто-то говорит «томат», кто-то — «помидор». А я говорю: «Хочу тебя прямо сейчас, ты, сексуальная штучка!»",
        "If I told you that you had a nice body, would you hold it against me? Seriously though. You're hot. I'd like to touch your shoulders right now while you take off my pants.": "Если я скажу, что у тебя прекрасное тело, ты прижмёшь его ко мне? А если серьёзно, ты горячая. Хочу прямо сейчас касаться твоих плеч, пока ты снимаешь с меня штаны.",
        "The top three sexiest things on this earth are: your chin, your shoulders, and your . . . I think you know what I'm trying to say here.": "Три самые сексуальные вещи на свете: твой подбородок, твои плечи и твоя... Думаю, ты поняла, к чему я клоню.",
        "You're so sexy you take my breath away, but not too far away, like I don't die because of it. Still. You're sexy.": "Ты такая сексуальная, что у меня перехватывает дыхание. Но не совсем — я от этого не умру. И всё же. Ты сексуальная.",
    }
    renpy.game.script.translator.strings['russian'].translations.update({"{#ff}" + k: v for k, v in _lssb_dirty_ff.items()})

    if hasattr(store, "dirty_text"):
        _lssb_native_dirty_text = dirty_text

        def dirty_text(sender, recipient):
            lines = _lssb_native_dirty_text(sender, recipient)
            if sender.is_male or recipient.is_male:
                return lines
            return [(who, "{#ff}" + line if line in _lssb_dirty_ff else line) for who, line in lines]
