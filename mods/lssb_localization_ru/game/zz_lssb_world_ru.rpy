# Display-only localization. Game state and native calculations are untouched.
init 1061 python in lssb_world:
    import re
    import renpy as engine
    import store
    _constant = True
    variant = 'lssb_world_ru'
    strings = {'Accept': 'Согласиться', 'Refuse': 'Refuse', 'To the sunset and beyond !!! (leads to an ending)': 'Навстречу закату и дальше!!! (приводит к концовке)', 'Not yet': 'Пока нет', 'Back Aletta - pay for ninety days, build a second source': 'Поддержать Алетту: платить 90 дней и найти второго поставщика', 'Back Arthur - refuse the increase and go to arbitration': 'Поддержать Артура: отказать в повышении цены и обратиться в арбитраж', 'Back Aletta - start the work now, paper it later': 'Поддержать Алетту: начать работу, оформить документы позже', 'Back Arthur - nobody lifts a finger until it is signed': 'Поддержать Артура: не начинать работу до подписания договора', 'Back Anthony - cap overtime immediately': 'Поддержать Энтони: немедленно ограничить сверхурочные', 'Back Aletta - hire temporary staff and keep the overtime': 'Поддержать Алетту: нанять временных работников и сохранить сверхурочные', 'Back Anthony - lease the refurbished unit and fix the scheduling': 'Поддержать Энтони: арендовать восстановленное оборудование и наладить график', 'Back Aletta - buy the new line outright': 'Поддержать Алетту: купить новую линию', 'Back Aletta - find out why they left and fix it': 'Поддержать Алетту: выяснить причины ухода сотрудников и устранить их', 'Back William - counter-raid and announce a retention war chest': 'Поддержать Уильяма: переманить людей в ответ и выделить средства на удержание', 'Back Aletta - pass on the acquisition': 'Поддержать Алетту: отказаться от приобретения', 'Back William - buy Marrow before the window closes': 'Поддержать Уильяма: купить Марроу, пока есть возможность', 'Back Cassidy - fire the night supervisor': 'Поддержать Кэссиди: уволить начальника ночной смены', 'Back Aletta - keep him, fix the scheduling system': 'Поддержать Алетту: оставить его и наладить составление графика', 'Back Aletta - keep Ostrander for the reference': 'Поддержать Алетту: сохранить Острандера ради рекомендации', 'Back Cassidy - drop Ostrander and free the capacity': 'Поддержать Кэссиди: отказаться от Острандера и освободить мощности', 'Back Aletta - send the audited file and a covenant plan': 'Поддержать Алетту: отправить проверенную отчётность и план соблюдения кредитных условий', 'Back Cherie - handle it socially, over dinner': 'Поддержать Шери: решить вопрос за дружеским ужином', 'Back Cherie - invite him in and hear him out': 'Поддержать Шери: пригласить его и выслушать', 'Back Aletta - legal hardball, shut him down': 'Поддержать Алетту: заставить его замолчать через суд', 'Back Cherie - keep the foundation and rename it': 'Поддержать Шери: сохранить фонд и переименовать', 'Back Cassidy - shut the foundation down': 'Поддержать Кэссиди: закрыть фонд', 'Back Cassidy - go where the young buyers actually are': 'Поддержать Кэссиди: идти туда, где молодые покупатели', 'Back Cherie - double down on heritage and discretion': 'Поддержать Шери: сделать ставку на традиции и сдержанность', 'Back Cherie - investigate it properly, no NDA': 'Поддержать Шери: провести расследование без соглашения о неразглашении', 'Back Arthur - settle quietly with a confidentiality agreement': 'Поддержать Артура: тихо уладить дело с соглашением о неразглашении', 'Back Cherie - sign the joint venture with the Sabatiers': 'Поддержать Шери: подписать соглашение о совместном предприятии с Сабатье', 'Back Arthur - refuse until the ownership is clear': 'Поддержать Артура: отказаться, пока не выясним владельца', 'Back Anthony - close it, the numbers are unarguable': 'Поддержать Энтони: закрыть офис, цифры неоспоримы', 'Back Cherie - keep the Ardley office open': 'Поддержать Шери: сохранить офис в Ардели', 'Back Cherie - take the Marchmont lease': 'Поддержать Шери: арендовать «Марчмонт»', 'Back Anthony - stay where we are and spend it on the business': 'Поддержать Энтони: остаться и вложить деньги в производство', 'Back Cherie - say nothing publicly, offer background': 'Поддержать Шери: обойтись без публичных заявлений, дать пояснения', 'Back William - hit back hard and publicly': 'Поддержать Уильяма: дать жёсткий публичный отпор', 'Back William - hold the price and call the bluff': 'Поддержать Уильяма: сохранить цену и вскрыть блеф', 'Back Cherie - give Thorne the discount graciously': 'Поддержать Шери: великодушно дать Торн скидку', 'Back Arthur - dismiss her immediately': 'Поддержать Артура: немедленно её уволить', 'Back Cassidy - keep her and put her in charge of the account': 'Поддержать Кэссиди: оставить её и поручить ей аккаунт', 'Back Cassidy - run the launch her way, at speed': 'Поддержать Кэссиди: быстро провести презентацию по её плану', 'Back Arthur - waivers, insurance and a sober adult, or no villa': 'Поддержать Артура: документы, страховка и трезвый взрослый — или никакой виллы', 'Back Cassidy - move the budget to the small line': 'Поддержать Кэссиди: перенести бюджет на небольшую линейку', 'Back Anthony - put the budget behind the proven line': 'Поддержать Энтони: направить бюджет на проверенную линейку', 'Back Anthony - refuse and spend it on the channels that work': 'Поддержать Энтони: отказаться и вложить деньги в работающие каналы', 'Back Cassidy - sponsor the regatta': 'Поддержать Кэссиди: спонсировать регату', 'Back Cassidy - do not hire Gethin Vale': 'Поддержать Кэссиди: не нанимать Гетина Вейла', 'Back William - hire him before Verrin does': 'Поддержать Уильяма: нанять его раньше Веррин', 'Back Cassidy - protect the premium brand, no cheap line': 'Поддержать Кэссиди: защитить премиальный бренд, отказаться от дешёвой линейки', 'Back William - launch the cheap sub-brand first': 'Поддержать Уильяма: первыми запустить дешёвый суббренд', 'Back Arthur - do not touch it': 'Поддержать Артура: не связываться со схемой', 'Back Anthony - adopt the structure and take the saving': 'Поддержать Энтони: внедрить схему и сэкономить', 'Back Anthony - serve the notice now': 'Поддержать Энтони: отправить уведомление сейчас', 'Back Arthur - take the time to review it properly': 'Поддержать Артура: не торопиться и тщательно проверить договор', 'Back William - ship now, certify in parallel': 'Поддержать Уильяма: начать отгрузки, проходить сертификацию параллельно', 'Back Arthur - nothing ships without the certificate': 'Поддержать Артура: никаких отгрузок без сертификата', 'Back William - get on a plane with an offer': 'Поддержать Уильяма: лететь с предложением', 'Back Arthur - no offer until legal has cleared it': 'Поддержать Артура: никаких предложений до юридической проверки', 'Back William - hire thirty percent now': 'Поддержать Уильяма: увеличить штат на тридцать процентов сейчас', 'Back Anthony - hold headcount, wait for the run rate': 'Поддержать Энтони: сохранить штат и дождаться устойчивых показателей', 'Back Anthony - the model says no, so no': 'Поддержать Энтони: если расчёты против, отказываемся', 'Back William - buy the patents before Kellis do': 'Поддержать Уильяма: купить патенты раньше Келлис', 'Get it fixed': 'Починить', 'Leave it': 'Оставить как есть', '[cap_raise_txt_knowledge]': '[lssb_world.apex_caption(cap_raise_txt_knowledge)]', '[cap_raise_txt_charm]': '[lssb_world.apex_caption(cap_raise_txt_charm)]', '[cap_raise_txt_fitness]': '[lssb_world.apex_caption(cap_raise_txt_fitness)]', "Sorry, but I don't want to go any further.": 'Простите, на этом я остановлюсь.', 'Apologize': 'Извиниться', 'Tell off': 'Отчитать', 'Apologise': 'Извиниться', 'Coffee': 'Кофе', 'Cocoa': 'Какао', 'Moka': 'Мокка', 'A coffee it is': 'Тогда кофе', "I'm in": 'Я в деле', 'Dye my hair in pink': 'Покрасить волосы в розовый', 'Use my natural color': 'Оставить естественный цвет', 'Just a little hair care': 'Просто немного ухода за волосами', 'Take it': 'Взять', 'Admit it': 'Признаться', 'Deny it': 'Отрицать', 'Eat the sandwich': 'Съесть сэндвич', "Don't eat the sandwich": 'Не есть сэндвич', 'Keep quiet': 'Промолчать', 'Walk away': 'Уйти', 'Flush it again': 'Смыть ещё раз', 'Bear with it': 'Потерпеть', 'Removes your shoes': 'Снять обувь', 'Chat with Shiori': 'Поговорить с Сиори', 'Chat with Aletta': 'Поговорить с Алеттой', 'Chat with Audrey': 'Поговорить с Одри', 'Chat with Lavish': 'Поговорить с Лавиш', 'Slack off': 'Бездельничать', 'Work normally': 'Работать как обычно', 'Work fast': 'Работать быстро', 'Give it to him': 'Give it to him', 'Attack him': 'Attack him', 'Intimidate him': 'Intimidate him', 'Hire him': 'Нанять его', "Don't hire him": 'Не нанимать его', 'No (Never meet Shiori again)': 'Нет (больше никогда не встречаться с Сиори)', 'I like it when you call me sir.': 'Мне нравится, когда ты называешь меня сэром', 'Stop Jeff leaving': 'Не дать Джеффу уйти', 'Let Jeff go': 'Отпустить Джеффа', 'Argue': 'Спорить', 'Take a peek': 'Подглядеть', 'Knock': 'Постучать', 'Play at the pub': 'Играть в пабе', 'Play at the nightclub': 'Играть в ночном клубе', 'Play at the thunderdome': 'Играть в «Громовом куполе»', 'Play dressed': 'Играть одетым', 'Play naked': 'Играть голым', "That's right.": 'Именно так', 'Are you serious?': 'Ты серьёзно?', 'Martial Arts': 'Боевые искусства', 'Golf': 'Гольф', 'Discreet': 'Незаметный', 'Cooking': 'Кулинария', 'Dancing': 'Танцы', 'Shooting': 'Стрельба', "No, I don't": 'Нет', 'Food': 'Еда', 'Video Games': 'Видеоигры', 'Fitness': 'Фитнес', 'Partying': 'Вечеринки', 'Working': 'Работа', 'Cars': 'Машины', 'Reading': 'Чтение', 'Playing guitar': 'Игра на гитаре', 'Not really': 'Не особо', 'No, nothing...': 'Нет, ничего...', 'I am unlucky': 'Мне не везёт', 'I have some big debt.': 'У меня большие долги', 'Animals hate me': 'Животные меня ненавидят', 'I have a small penis': 'У меня маленький пенис', 'I am prone to erectile problems': 'У меня бывают проблемы с эрекцией', 'I won a marathon': 'Я выиграл марафон', 'I am a people person': 'Я легко схожусь с людьми', 'I won an eating contest': 'Я выиграл соревнование по поеданию еды', 'I am pretty lucky': 'Мне довольно часто везёт', 'I was the best in my class.': 'Я был лучшим в классе', "I don't sleep": 'Я не сплю', 'I am hung': 'У меня огромный член', 'I have a very high libido': 'У меня очень высокое либидо', 'Charge them rent (+100{image=gui/icons/icon_money.png} each on Mondays)': 'Брать плату за жильё (+100{image=gui/icons/icon_money.png} с каждой по понедельникам)', 'Let them live rent-free (+1 love each on Mondays)': 'Разрешить жить бесплатно (+1 к любви каждой по понедельникам)', 'Participate': 'Участвовать', "Don't participate": 'Не участвовать', 'Do it': 'Сделать это', "Don't do it": 'Не делать этого', "Take [bree.name]'s side": 'Поддержать [bree.name]', "Take Sasha's side": 'Поддержать Сашу', 'Stay neutral': 'Сохранить нейтралитет', 'Help her': 'Помочь ей', "Don't help her": 'Не помогать ей'}
    aliases = {'Отказаться': 'Refuse', 'Отдать ему': 'Give it to him', 'Напасть на него': 'Attack him', 'Запугать его': 'Intimidate him'}
    def stat_name(value):
        return {'Knowledge':'Знания','Charm':'Обаяние','Fitness':'Фитнес'}.get(value,engine.translation.translate_string(value,'russian'))
    def apex_caption(value):
        pattern=r'^(Knowledge|Charm|Fitness) - (\d+|-)(\{image=gui/icons/icon_money\.png\})(?: \(need (\d+)\{image=gui/icons/icon_money\.png\} more\))?$'
        match=re.fullmatch(pattern,value)
        if not match:return value
        name,cost,icon,shortfall=match.groups()
        return stat_name(name)+' — '+cost+icon+(' (не хватает '+shortfall+icon+')' if shortfall else '')
    def caption(value):
        if engine.game.preferences.language != 'russian':return value
        node=engine.game.script.namemap.get(engine.game.context().current)
        filename=getattr(node,'filename','').replace('\\','/').split('/game/')[-1].removeprefix('game/')
        if filename.startswith(('bg/','intro.rpy','phone_texting.rpy','updater_module/')):
            if filename=='bg/hospital/hospital.rpy':
                value=apex_caption(value)
            return strings.get(value,aliases.get(value,engine.translation.translate_string(value,'russian')))
        return store.lssb_common.caption(value)
    def enter():
        if variant not in store.config.variants:store.config.variants.insert(0,variant)
    def leave():
        if variant in store.config.variants:store.config.variants.remove(variant)

init 1062 python:
    config.language_callbacks['russian'].append(lssb_world.enter)
    for _lssb_world_language in set(renpy.known_languages()) | {None}:
        if _lssb_world_language != 'russian':config.language_callbacks[_lssb_world_language].append(lssb_world.leave)

screen choice(items):
    variant 'lssb_world_ru'
    style_prefix 'choice'
    vbox:
        for i in items:
            textbutton lssb_world.caption(i.caption) action i.action

translate russian strings:
    old "Knowledge"
    new "Знания"
    old "APEX procedure"
    new "Процедура APEX"
    old "Who should perform the lapdance?"
    new "Кого выбрать для приватного танца?"
    old "Thank you [hero.name]."
    new "Спасибо, [hero.name]."
    old "For being such a good client."
    new "За то, что ты такой хороший клиент."
    old "Here's a small reward."
    new "Вот небольшая награда."
    old "We decided to play at the pub to earn some money."
    new "Мы решили выступить в пабе, чтобы немного заработать."
    old "We decided to play at the pub to earn some money and grew up our reputation."
    new "Мы решили выступить в пабе, чтобы немного заработать и стать известнее."
    old "We decided to play naked at the pub to earn some money."
    new "Мы решили выступить голыми в пабе, чтобы немного заработать."
    old "We decided to play naked at the pub to earn some money and grew up our reputation."
    new "Мы решили выступить голыми в пабе, чтобы немного заработать и стать известнее."
    old "We decided to play at the nightclub to earn some money."
    new "Мы решили выступить в ночном клубе, чтобы немного заработать."
    old "We decided to play at the nightclub to earn some money and grew up our reputation."
    new "Мы решили выступить в ночном клубе, чтобы немного заработать и стать известнее."
    old "We decided to play naked at the nightclub to earn some money."
    new "Мы решили выступить голыми в ночном клубе, чтобы немного заработать."
    old "We decided to play naked at the nightclub to earn some money and grew up our reputation."
    new "Мы решили выступить голыми в ночном клубе, чтобы немного заработать и стать известнее."
    old "We decided to play at the Thunderdome to earn some money."
    new "Мы решили выступить в «Громовом куполе», чтобы немного заработать."
    old "We decided to play at the Thunderdome to earn some money and grew up our reputation."
    new "Мы решили выступить в «Громовом куполе», чтобы немного заработать и стать известнее."
    old "We decided to play naked at the Thunderdome to earn some money."
    new "Мы решили выступить голыми в «Громовом куполе», чтобы немного заработать."
    old "We decided to play naked at the Thunderdome to earn some money and grew up our reputation."
    new "Мы решили выступить голыми в «Громовом куполе», чтобы немного заработать и стать известнее."
