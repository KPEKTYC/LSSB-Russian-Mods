# Additive Russian shop localization for the installed 26.8.0d game.
init 1004 python:
    import builtins as _lssb_shop_builtins
    import re as _lssb_shop_re
    _lssb_shop_strings = {'Drug Store': 'Аптека', 'Bakery': 'Пекарня', 'Book Store': 'Книжный магазин', 'Clothes Shop': 'Магазин одежды', 'Coffee Shop': 'Кофейня', 'Electronic Store': 'Электроника', 'Flower Shop': 'Цветочный магазин', 'Car workshop': 'Автомастерская', 'Jewelry Store': 'Ювелирный магазин', 'Mall Southside': 'Южное крыло', 'Mall Northside': 'Северное крыло', 'Dark alley': 'Тёмный переулок', 'Sex shop': 'Секс-шоп', 'Women section': 'Женский отдел', 'Men section': 'Мужской отдел', 'Exit': 'Выход', 'Gift': 'Подарок', 'Clothes: ': 'Одежда: ', 'Accessory: ': 'Аксессуар: ', '1 use': '1 использование', 'How to train your shark': 'Как приручить акулу', 'A book about shark training... Might be a parody of a well known movie.': 'Книга о дрессировке акул... Возможно, пародия на известный фильм.', 'Pregnancy test': 'Тест на беременность', 'A test to detect pregnancy': 'Тест для определения беременности.', 'DNA test': 'Тест ДНК', 'A test to analyze DNA': 'Тест для анализа ДНК.', 'Zbox 360': 'Zbox 360', 'Play video games at home': 'Позволяет играть в видеоигры дома.', 'Headphones': 'Наушники', 'Play the Zbox or watch TV without disturbing others in the room': 'Позволяют играть на Zbox или смотреть телевизор, не мешая другим в комнате.', 'Fitness machine': 'Фитнес-тренажёр', 'Gain Fitness while sleeping': 'Повышает физическую форму во время сна.', 'Knowledge machine': 'Тренажёр памяти', 'Gain Knowledge while sleeping': 'Повышает знания во время сна.', 'Charm machine': 'Тренажёр обаяния', 'Gain Charm while sleeping': 'Повышает обаяние во время сна.', 'Spy camera': 'Скрытая камера', 'Micro camera for secretly recording things': 'Миниатюрная камера для скрытой записи.', 'Electric guitar': 'Электрогитара', 'An axe shaped electric guitar... METAL!': 'Электрогитара в форме топора... МЕТАЛ!', 'Bike': 'Велосипед', 'Go to far-away places (slowly)': 'Позволяет добираться до отдалённых мест, но медленно.', 'Car': 'Автомобиль', 'Go to far-away places (fast)': 'Позволяет быстро добираться до отдалённых мест.', 'Sports car': 'Спорткар', 'Go to far-away places (fast) with style': 'Позволяет добираться до отдалённых мест быстро и со стилем.', 'Wedding ring': 'Обручальное кольцо', 'Ask a girl to marry you': 'Позволяет сделать девушке предложение.', 'Bear bell': 'Колокольчик от медведей', 'A bear repelling bell... I wonder if it works or call the bear for dinner...': 'Колокольчик для отпугивания медведей... Интересно, он их отпугивает или зовёт на ужин?', 'Luxury bed': 'Роскошная кровать', 'Be rested with less sleep': 'Позволяет высыпаться за меньшее время.', 'Baseball bat': 'Бейсбольная бита', 'A wooden baseball bat': 'Деревянная бейсбольная бита.', 'Anal beads': 'Анальные шарики', 'Vibrator': 'Вибратор', 'Dildo': 'Фаллоимитатор', 'Double dildo': 'Двойной фаллоимитатор', 'Large dildo': 'Большой фаллоимитатор', 'Blindfold': 'Повязка на глаза', 'Bondage ropes': 'Верёвки для связывания', 'Handcuffs': 'Наручники', 'Naughty board game': 'Игра для взрослых', 'A racy board game with revealing forfeits meant to deepen your relationship dynamic': 'Пикантная настольная игра с откровенными фантами, помогающая углубить ваши отношения.', 'Cake': 'Торт', 'A delightful cake': 'Восхитительный торт.', 'Candies': 'Конфеты', 'Sweet candies': 'Сладкие конфеты.', 'Romance novel': 'Любовный роман', 'A novel that gives love': 'Роман, пробуждающий любовь.', 'Mistress Amanda': 'Госпожа Аманда', 'A book about the dominant Mistress Amanda': 'Книга о властной госпоже Аманде.', 'Yuri manga': 'Юри-манга', 'A manga that represents lesbian scenes': 'Манга со сценами любви между девушками.', 'Porn magazine': 'Порножурнал', 'A magazine with mostly heterosexual picture': 'Журнал с преимущественно гетеросексуальными изображениями.', "A sex slave's story": 'История секс-рабыни', 'A tale of surrender and passion in the journey of a sex slave': 'История подчинения и страсти на жизненном пути секс-рабыни.', 'Leather bound bible': 'Библия в кожаном переплёте', 'The holy book': 'Священная книга.', 'Lingerie': 'Кружевное бельё', 'Seductive lingerie for a flirty appeal and to {b}amplify allure of specific people{/b}': 'Соблазнительное бельё для флирта, способное {b}усилить влечение определённых людей{/b}.', 'Sexy dress': 'Соблазнительное платье', 'A provocative dress to {b}enhance allure{/b}': 'Вызывающее платье, способное {b}усилить влечение{/b}.', 'Slutty dress': 'Откровенное платье', 'A daring dress to {b}amplify allure{/b}': 'Смелое платье, способное {b}усилить влечение{/b}.', 'Cute top': 'Милый топ', 'A sweet charming top': 'Милый и очаровательный топ.', 'Nice scarf': 'Красивый шарф', 'A stylish scarf with a touch of flirtiness': 'Стильный шарф с ноткой кокетства.', 'Sexy swimsuit': 'Откровенный купальник', 'A revealing swimsuit to {b}enhance allure{/b}': 'Открытый купальник, способный {b}усилить влечение{/b}.', 'Cute swimsuit': 'Милый купальник', 'A lovely swimsuit': 'Очаровательный купальник.', 'Purse': 'Сумочка', 'A fashionable purse with appeal': 'Привлекательная модная сумочка.', 'Fancy purse': 'Роскошная сумочка', 'A luxurious purse fit for a princess': 'Роскошная сумочка, достойная принцессы.', 'Shoes': 'Туфли', 'Classical stylish shoes': 'Стильные классические туфли.', 'Fancy shoes': 'Элегантные туфли', 'Elegant shoes fit for a princess': 'Элегантные туфли, достойные принцессы.', 'Sexy underwear': 'Соблазнительное бельё', 'Seductive underwear for men': 'Соблазнительное мужское бельё.', 'Tuxedo': 'Смокинг', 'A classy tuxedo to impress': 'Элегантный смокинг, производящий впечатление.', 'T-shirt': 'Футболка', 'A casual t-shirt': 'Повседневная футболка.', 'Leather shoes': 'Кожаные туфли', 'Stylish leather shoes': 'Стильные кожаные туфли.', 'Swimming t-back': 'Плавки-стринги', 'A bold swimwear choice': 'Смелый выбор для купания.', 'Swimming trunk': 'Мужские плавки', 'Stylish swimwear for men': 'Стильные мужские плавки.', 'Wallet': 'Бумажник', 'A practical and stylish wallet': 'Практичный и стильный бумажник.', 'Fancy watch': 'Дорогие часы', 'A luxurious watch to impress': 'Роскошные часы, производящие впечатление.', 'Sports shoes': 'Спортивные кроссовки', 'Comfortable sports shoes': 'Удобная спортивная обувь.', 'Morning-after pill': 'Экстренная контрацепция', 'An emergency pill to spare her a recent, still-hidden pregnancy': 'Экстренная таблетка, избавляющая её от недавней, ещё незаметной беременности.', 'Fertility supplement': 'Добавка для зачатия', 'A supplement that boosts her chance of conception today and tomorrow': 'Добавка, повышающая её шанс зачатия сегодня и завтра.', 'Bigger Staff Pill': 'Таблетка для увеличения', 'A gift of enhancement for penis enlargement': 'Подарочная таблетка для увеличения пениса.', 'Smaller Staff Pill': 'Таблетка для уменьшения', 'A gift of reduction for penis size': 'Подарочная таблетка для уменьшения пениса.', 'Flowers': 'Букет цветов', 'A bouquet of flowers to express affection': 'Букет цветов в знак симпатии.', 'Lots of flowers': 'Огромный букет', 'An abundance of flowers for a grand gesture': 'Множество цветов для широкого жеста.', 'Silver bracelet': 'Серебряный браслет', 'A delicate silver bracelet to show affection': 'Изящный серебряный браслет в знак симпатии.', 'Silver necklace': 'Серебряное ожерелье', 'A beautiful silver necklace to express love': 'Красивое серебряное ожерелье в знак любви.', 'Gold bracelet': 'Золотой браслет', 'An elegant gold bracelet fit for a princess': 'Элегантный золотой браслет, достойный принцессы.', 'Gold necklace': 'Золотое ожерелье', 'A luxurious gold necklace fit for royalty': 'Роскошное золотое ожерелье, достойное королевской особы.', 'Diamond necklace': 'Бриллиантовое ожерелье', 'A dazzling diamond necklace for the ultimate expression of love': 'Ослепительное бриллиантовое ожерелье — высшее выражение любви.', 'Teddy bear': 'Плюшевый мишка', 'A cuddly teddy bear': 'Мягкий плюшевый мишка.', 'Butt plug': 'Анальная пробка', 'Slave collar': 'Ошейник', 'Cosplay outfit': 'Костюм для косплея', 'Fancy clothes': 'Нарядная одежда', 'Elegant attire to impress with charm {b}even in the most swanky places{/b}': 'Элегантный наряд, позволяющий очаровать окружающих {b}даже в самых роскошных заведениях{/b}.', 'Tweed blazer': 'Твидовый пиджак', 'A sophisticated blazer for the presence': 'Изысканный пиджак для солидного образа.', 'Military fatigues': 'Военная форма', 'Rugged wear with pants and t-shirt': 'Прочная одежда: брюки и футболка.', 'Luxury watch': 'Роскошные часы', 'A stylish and shiny accessory well detail': 'Стильный блестящий аксессуар с изящными деталями.', 'Leather jacket': 'Кожаная куртка', 'A rebellious jacket with attitude': 'Дерзкая куртка с бунтарским характером.', 'Sweat pants': 'Спортивные штаны', 'Comfortable pants for the sporty': 'Удобные штаны для любителей спорта.', 'Funny shirt': 'Футболка с принтом', 'A playful shirt with geeky humor': 'Забавная футболка с гиковским юмором.', 'Sport clothes': 'Спортивная одежда', 'Ideal outfit for {b}sports and fitness{/b}': 'Идеальная одежда для {b}спорта и фитнеса{/b}.', 'Swimsuit': 'Купальный костюм', 'Perfect swimwear for {b}watery activities{/b}': 'Отличный купальный костюм для {b}развлечений на воде{/b}.', 'Cool sunglasses': 'Крутые солнцезащитные очки', 'Stylish sunglasses for a rebellious look': 'Стильные солнцезащитные очки для бунтарского образа.', 'Geeky pen': 'Ручка для всезнайки', 'A pen for the knowledgeable bookworm': 'Ручка для эрудированного книголюба.', 'Sport shoes': 'Спортивная обувь', 'Shoes designed for sporty individuals': 'Обувь для любителей спорта.', 'Funny badge': 'Забавный значок', 'A playful badge with geeky humor': 'Забавный значок с гиковским юмором.', 'Military boots': 'Армейские ботинки', 'Rugged and strong boots': 'Прочные и крепкие ботинки.', 'Drugs': 'Наркотики', 'Weed': 'Марихуана', 'Minty candies': 'Мятные конфеты', 'Refreshing minty candies': 'Освежающие мятные конфеты.', 'Energy drink': 'Энергетик', 'An energy drink to boost energy': 'Энергетический напиток для прилива сил.', 'Pastry': 'Пирожное', 'A tasty pastry to satisfy little hunger': 'Вкусное пирожное, утоляющее лёгкий голод.', 'Knowledge book': 'Энциклопедия', 'An encyclopedia of everything': 'Энциклопедия обо всём на свете.', 'Charm book': 'Книга об обаянии', 'A book about charm techniques': 'Книга о приёмах обольщения.', 'Fun book': 'Сборник шуток', 'A book with many joke and funny tricks': 'Книга с множеством шуток и забавных трюков.', 'Skill book: massage': 'Учебник массажа', 'A book to learn how to give massages': 'Книга, обучающая массажу.', 'Skill book: guitar': 'Самоучитель гитары', 'A book to learn how to play the guitar': 'Книга, обучающая игре на гитаре.', 'Skill book: cooking': 'Учебник кулинарии', 'A book to learn how to cook': 'Книга, обучающая приготовлению пищи.', 'Sexperience book': 'Книга о сексе', 'A book to learn how to fuck like a god': 'Книга о том, как стать непревзойдённым любовником.', 'Skill book: shibari': 'Учебник сибари', 'A book to learn how to play with ropes': 'Книга об использовании верёвок для связывания.', 'Skill book: SM': 'Учебник садомазохизма', 'A book to learn SM techniques': 'Книга о садомазохистских практиках.', 'Skill book: fertility': 'Книга о фертильности', 'A book to learn how to know if a girl is fertile': 'Книга о том, как определить способность девушки к зачатию.', 'How to get away with murder': 'Как избежать наказания за убийство', 'A rare compilation of archived police files talking about murder and the methods used to solve them': 'Редкий сборник архивных полицейских дел об убийствах и методах их раскрытия.', 'Coffee': 'Кофе', 'A simple coffee': 'Обычный кофе.', 'Cappuccino': 'Капучино', 'A frothy cappuccino': 'Капучино с пышной пенкой.', 'Moka': 'Мокка', 'A rich moka coffee': 'Насыщенный кофе мокка.', 'Pine needle tea': 'Чай из сосновой хвои', 'A herbal tea, made from pine needles': 'Травяной чай из сосновых иголок.', 'Rose hip tea': 'Чай из шиповника', 'A tea that can be use as a painkiller, made from Rose Hips': 'Чай из плодов шиповника, который можно использовать как обезболивающее.', 'Sage tea': 'Чай с шалфеем', 'A tea with a strong and unique flavor, made from sage': 'Чай из шалфея с насыщенным и необычным вкусом.', 'Turmeric tea': 'Чай с куркумой', 'A tea from Okinawa, made of the rhizomes of turmeric': 'Чай с Окинавы, приготовленный из корневищ куркумы.', 'White peony tea': 'Белый пион', 'A white fruity tea, made from leaf shoot and young leaves of the Camellia sinensis': 'Белый чай с фруктовыми нотками, приготовленный из почек и молодых листьев чайного куста.', 'Willow bark tea': 'Чай из ивовой коры', 'A tea that can be used to relieve headaches, made from Willow bark': 'Чай из коры ивы, который можно использовать для облегчения головной боли.', 'Peppermint tea': 'Чай с перечной мятой', 'A tea made by infusing peppermint leaves': 'Чай, настоянный на листьях перечной мяты.', 'Parsley tea': 'Чай с петрушкой', 'A tea made by steeping fresh or dried parsley': 'Настой свежей или сушёной петрушки.', 'Nettle tea': 'Крапивный чай', 'A tea with a floral taste, made from fresh leaves of nettle': 'Чай из свежих листьев крапивы с цветочным вкусом.', 'Mint tea': 'Мятный чай', 'A tea made by infusing mint leaves': 'Чай, настоянный на листьях мяты.', 'Marigold tea': 'Чай с бархатцами', 'Delicious and healthy way to have a good cold glass of iced tea, made from French marigold': 'Вкусный и полезный холодный чай из бархатцев.', 'Liquorice tea': 'Чай с солодкой', 'A tea with strong flavor not suitable for everyone, made from Liquorice': 'Чай из солодки с насыщенным вкусом на любителя.', 'Jasmine tea': 'Жасминовый чай', 'A black jasmine tea, subtly sweet and highly fragrant': 'Очень ароматный чёрный чай с жасмином и лёгкой сладостью.', 'Honeysuckle tea': 'Чай с жимолостью', 'Made with Honeysuckle sun tea method, making it delicious': 'Вкусный чай из жимолости, настоянный на солнце.', 'Hibiscus tea': 'Каркаде', 'A herbal tea with reminiscent of cranberry juice, and similar to raw hibiscus flowers': 'Травяной чай со вкусом, напоминающим клюквенный сок и свежие цветки гибискуса.', 'Ginger tea': 'Имбирный чай', 'A herbal beverage that has many health benefits, made from ginger root': 'Травяной напиток из корня имбиря с множеством полезных свойств.', 'Fennel tea': 'Чай с фенхелем', 'A tea with a relaxing scent and slightly bitter aftertaste, taste a little like licorice': 'Чай с успокаивающим ароматом и слегка горьким послевкусием, немного напоминающим солодку.', 'Cinnamon tea': 'Чай с корицей', 'A tea with distinctively sweet and aromatic notes, made by infusing cinnamon bark': 'Настой коры корицы с выраженными сладкими и пряными нотками.', 'Chamomile tea': 'Ромашковый чай', 'A tea that tastes silky but also fresh and floral, with a crisp apple flavour': 'Мягкий и свежий цветочный чай с отчётливым яблочным вкусом.', 'Buckwheat tea': 'Гречишный чай', 'A tea that has a toasty aroma and nutty sweet flavor, made of organic roasted buckwheat': 'Чай из обжаренной органической гречихи с ореховой сладостью и тёплым поджаренным ароматом.', 'English breakfast tea': 'Английский завтрак', 'A tea that offers a bold flavor similar to coffee with roasted notes': 'Чай с насыщенным вкусом и поджаренными нотками, напоминающими кофе.', 'Earl grey green tea': 'Зелёный Эрл Грей', 'A tea with the finesse of green tea associated to the flavor of bergamot': 'Нежный зелёный чай со вкусом бергамота.', 'Earl grey black tea': 'Чёрный Эрл Грей', 'Smooth and balanced, with notes of citrus, spice, malt, and smoke': 'Мягкий и сбалансированный чай с нотами цитруса, пряностей, солода и дыма.', 'Darjeeling tea': 'Дарджилинг', 'Musky-sweet tasting notes similar to muscat wine': 'Сладковато-мускусный вкус, напоминающий мускатное вино.', 'Assam tea': 'Ассам', 'A tea with almost caramel sweetness': 'Чай с почти карамельной сладостью.', 'Sencha tea': 'Сенча', 'A green tea with a wide variety of flavors': 'Зелёный чай с богатой палитрой вкусов.', 'Russian caravan tea': 'Русский караван', 'This tea has a distinct smoky, slightly sweet flavor.': 'Чай с выраженным дымным и слегка сладким вкусом.', 'Lady grey tea': 'Леди Грей', 'Contains lemon and orange peel that give it a softer, more subtle citrusy flavor': 'Содержит цедру лимона и апельсина, придающую более мягкий и тонкий цитрусовый вкус.', 'Ceylon tea': 'Цейлонский чай', 'A taste full bodied and rich, but not harsh or bitter': 'Полнотелый и насыщенный вкус без резкости и горечи.', 'Condom': 'Презерватив', 'A single-use contraceptive': 'Одноразовое средство контрацепции.', 'Box of condoms': 'Коробка презервативов', 'A pack of condoms for ongoing protection': 'Упаковка презервативов для регулярной защиты.', 'Medicine': 'Лекарство', 'General-purpose medicine': 'Лекарство общего назначения.', 'Sunscreen lotion': 'Солнцезащитный лосьон', 'Lotion for sun protection': 'Лосьон для защиты от солнца.', 'Enhancement pill for penis enlargement': 'Таблетка для увеличения пениса.', 'Reduction pill for penis size': 'Таблетка для уменьшения пениса.', 'Blue pill': 'Синяя таблетка', 'A pill used to treat erectile dysfunction': 'Таблетка для лечения эректильной дисфункции.', 'Pink pill': 'Розовая таблетка', 'A pill used to treat sexual dysfunction': 'Таблетка для лечения сексуальной дисфункции.', 'Contraceptive pill': 'Оральный контрацептив', 'A pill to prevent pregnancy': 'Таблетка для предотвращения беременности.', 'An emergency pill to prevent a recent, still-hidden pregnancy': 'Экстренная таблетка, предотвращающая недавнюю, ещё незаметную беременность.', 'A supplement that boosts the chance of conception today and tomorrow': 'Добавка, повышающая шанс зачатия сегодня и завтра.'}
    _lssb_shop_variant = "lssb_shops_ru_26_8_0d"
    _lssb_shop_previous_translate = _lssb_ui_translate

    def _lssb_shop_text(value):
        if isinstance(value, (_lssb_shop_builtins.list, _lssb_shop_builtins.tuple)):
            return [_lssb_shop_text(part) for part in value]
        if not isinstance(value, str):
            return value
        text = _lssb_shop_previous_translate(value)
        if renpy.game.preferences.language != "russian":
            return text
        # Use the reviewed item terminology consistently in shops, inventories
        # and item tooltips, including entries partially translated before.
        text = _lssb_shop_strings.get(value, text)
        def usage(match):
            n = int(match.group(1))
            word = "использование" if n % 10 == 1 and n % 100 != 11 else "использования" if n % 10 in (2,3,4) and n % 100 not in (12,13,14) else "использований"
            return str(n) + " " + word
        lines = [_lssb_shop_strings.get(line,line) for line in text.split("\n")]
        text = "\n".join(lines)
        text = _lssb_shop_re.sub(r"(?m)^(\d+) uses$",usage,text)
        return _lssb_shop_re.sub(r"(?m)^(\{image=[^}]+\} [+-]?[0-9.]+) h$",r"\1 ч",text)

    def _lssb_shop_enter_ru():
        if True and _lssb_shop_variant not in config.variants:
            config.variants.insert(0,_lssb_shop_variant)

    def _lssb_shop_leave_ru():
        if _lssb_shop_variant in config.variants:
            config.variants.remove(_lssb_shop_variant)

    if True:
        for _lssb_old,_lssb_new in _lssb_shop_strings.items():
            _lssb_ui_strings.setdefault(_lssb_old,_lssb_new)
        _lssb_ui_translate = _lssb_shop_text
        config.language_callbacks["russian"].append(_lssb_shop_enter_ru)
        for _lssb_language in set(renpy.known_languages()) | {None}:
            if _lssb_language != "russian":
                config.language_callbacks[_lssb_language].append(_lssb_shop_leave_ru)

screen shopping(items=[], clerk=None):
    variant "lssb_shops_ru_26_8_0d"
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
            label _lssb_ui_resize(Room.find(game.room).display_name, 280, 28) alt ""
            viewport id "inventory_vp":
                style_prefix "shopping_items"
                xfill True
                pos (10, 55)
                ysize 352
                draggable True
                mousewheel True
                xsize 285
                has vbox
                for i, (item_name, item_id, item_price, item_tooltip) in enumerate(sorted(items, key=lambda x: _lssb_ui_translate(x[0]).casefold())):
                    hbox:
                        xsize 278
                        button sensitive item_price <= hero.money action Return((item_id, item_price)) default_focus (1 if i == 0 and check_controller() else 0):
                            xsize 278
                            ysize None
                            padding (0, 3)
                            fixed:
                                id ("lssb_shop_row_" + str(i))
                                xsize 278
                                fit_first "height"
                                text _lssb_ui_translate(item_name) id ("lssb_shop_name_" + str(i)) xsize 184 size 19 layout "greedy" yalign 0.5 alt ""
                                hbox:
                                    id ("lssb_shop_cost_" + str(i))
                                    xalign 1.0
                                    yalign 0.5
                                    text "[item_price] " id ("lssb_shop_price_" + str(i)) size 19 yalign 0.5 alt ""
                                    add hero.money.icon yalign 0.5
                            tooltip ItemBase.find(item_id)
                            alt _lssb_ui_translate(item_name) + ". Цена: " + str(item_price) + ". " + replace_tags_alt(" ".join(_lssb_ui_translate(item_tooltip)))
            vbar value YScrollValue("inventory_vp") left_bar "gui/inv/vertical_idle_bar.png" thumb "gui/inv/vertical_idle_thumb.png" right_bar "gui/inv/vertical_idle_bar.png" xmaximum 11 ymaximum 370 xalign 1.0 ypos 50 unscrollable "hide" alt "scroll "
        fixed:
            ysize 47
            imagebutton auto "gui/button_%s.png" id "lssb_shop_exit_button" action Return("exit") alt "Exit"
            text _lssb_ui_translate("Exit") id "lssb_shop_exit_text" color "#ffffff" font "exo2_bold" size 23 align (0.5, 0.5) yoffset -3 alt ""

    if persistent.new_ui:
        use tooltip
    else:
        use tooltip_old_ui



screen tooltip():
    variant "lssb_shops_ru_26_8_0d"
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
                    text _lssb_ui_translate(name) size 23 font "exo2_regular" color "#fff" outlines [(1, "#0099ff", 0, 0)] xalign 0.5
                    if not isinstance(tooltip, Person) and tooltip.get_tooltip():
                        text _lssb_ui_translate(tooltip.get_tooltip(in_inventory)) substitute False yalign 0.5

screen tooltip_old_ui():

    variant "lssb_shops_ru_26_8_0d"

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


