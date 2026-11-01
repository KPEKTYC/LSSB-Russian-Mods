# Literal speaker labels on Russian dialogue lines only. A string table would also
# rewrite any on-screen text equal to the label, such as a player who is named Jeff.
# Runs after the review modules, whose guards compare the original speaker.
init 1180 python in lssb_speakers:
    import renpy as engine
    _constant = True
    names = {
        "Priest": "Священник", "Coworker": "Коллега", "Michaels": "Майклс", "Майклз": "Майклс",
        "Detective": "Детектив", "Shady guy": "Подозрительный тип", "Investigator": "Следователь",
        "Mr Blank": "Мистер Бланк", "Ray": "Рэй", "Guy": "Парень", "Girl": "Девушка",
        "Female fan": "Поклонница", "Male fan": "Поклонник", "Gwendoline": "Гвендолин",
        "Shop owner": "Владелец магазина", "Another Kid": "Другой мальчишка",
        "Handsome man": "Красавчик", "Vincent": "Винсент", "Edna": "Эдна",
        "Bear Chan": "Медведица-тян", "Manager": "Менеджер", "Judge": "Судья", "Gianna": "Джанна",
        "Inspector": "Инспектор", "Jeff": "Джефф", "Old pervert": "Старый извращенец",
        "Bather": "Отдыхающий", "Dylan": "Дилан", "Gwen": "Гвен", "Random Man": "Незнакомец",
        "Mrs White": "Миссис Уайт",
    }
    renamed = 0

    def rename(node):
        global renamed
        who = getattr(node, "who", None)
        if isinstance(who, str) and who[:1] == '"' and who[1:-1] in names:
            node.who = '"' + names[who[1:-1]] + '"'
            renamed += 1

    for (_identifier, _language), _node in engine.game.script.translator.language_translates.items():
        if _language == "russian":
            rename(_node)
            for _child in getattr(_node, "block", None) or ():
                rename(_child)
