# Display-only translations and a bounded binding fix for team-button speech.
init 1141 python in lssb_textinterface:
    import copy,re
    import renpy as engine
    import store
    _constant=True
    strings={'How hard should the team work this week?': 'Насколько интенсивно должна работать команда на этой неделе?', 'Wait until the next day': 'Подождать до следующего дня', 'One hour later': 'На час позже', 'One hour earlier': 'На час раньше', 'Wait until the next appointment': 'Подождать до следующей встречи', 'Push her': 'Больше работы', 'Steady': 'Обычный темп', 'Cut some slack': 'Меньше работы', 'Act': 'Действия', 'Cupid': 'Купидон'}
    menu_strings={}
    previous_replace_text=store.config.replace_text
    patch_status={}
    def russian():return engine.game.preferences.language=='russian'
    def team_alt(caption,person):
        # Bind screen-local values while they exist; avoid later global lookup.
        label=store._lssb_ui_translate(caption) if russian() else caption
        value=label+(' — ' if russian() else ' for ')+str(person.name)
        return value.replace('[','[[')
    def notify_text(value):
        match=re.fullmatch(r"Room '(.*)' not found!",value)
        if match:return 'Комната «'+match[1]+'» не найдена!'
        prefix='Event/Activity/TalkSubject not found: '
        if value.startswith(prefix):return 'Событие, занятие или тема разговора не найдены: '+value[len(prefix):]
        return value
    def replace_text(value):
        if russian():
            if engine.display.screen.get_screen('notify') is not None:
                translated=notify_text(value)
                if translated!=value:return translated
        return previous_replace_text(value) if previous_replace_text is not None else value
    def walk(node):
        yield node
        for child in getattr(node,'children',[]):
            for item in walk(child):yield item
        for entry in getattr(node,'entries',[]):
            if isinstance(entry,(list,tuple)) and len(entry)==2:
                for item in walk(entry[1]):yield item
        block=getattr(node,'block',None)
        if block is not None:
            for child in block if isinstance(block,(list,tuple)) else [block]:
                for item in walk(child):yield item
    def patch_team(screen):
        if screen is None:return None,'screen absent'
        tree=copy.deepcopy(screen.function)
        # PyCode intentionally drops bytecode on deepcopy; retain immutable
        # original Python nodes while changing only the display keyword.
        for original,cloned in zip(walk(screen.function),walk(tree)):
            code=getattr(original,'code',None)
            if code is not None and type(code).__name__=='PyCode':cloned.code=code
        found=[]
        for node in walk(tree):
            if type(node).__name__=='SLDisplayable' and getattr(node,'name',None)=='textbutton':
                keywords=dict(node.keyword)
                if node.positional==['caption'] and keywords.get('alt')=='"[caption] for [girl.name]"' and keywords.get('action')=='SetField(girl.flags, "work_strategy", value)':found.append(node)
        if len(found)!=1:return None,'expected one unchanged team-button binding, found '+str(len(found))
        node=found[0]
        node.keyword=[(key,'lssb_textinterface.team_alt(caption, girl)' if key=='alt' else value) for key,value in node.keyword]
        tree.variant="'lssb_textinterface_alt_v2'"
        tree.const_ast=None;tree.not_const_ast=None;tree.analysis=None;tree.prepared=False
        return tree,'patched one alt expression; action and conditions preserved'
    native_team=engine.display.screen.screens.get(('manage_team',None))
    original_team_function=native_team.function if native_team is not None else None
    patched_team,reason=patch_team(native_team)
    patch_status['manage_team']=reason
    if patched_team is not None:
        native_team.function=patched_team
        native_team.ast=patched_team
    else:store.renpy.log('LSSB interface: '+reason)
    store.config.replace_text=replace_text
