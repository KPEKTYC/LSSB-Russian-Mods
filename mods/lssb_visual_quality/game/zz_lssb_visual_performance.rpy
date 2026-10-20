# Bound continuous sprite work; keep the native renderer, timing, and render cache.
init 1010 python in lssb_performance:
    import renpy as engine
    import store
    from store import renpy as api
    _constant = True
    supported = store.lssb_compat.require('Плавность', ('renpy.gl2.live2d.Live2D.render', 'renpy.gl2.live2d.update_states', 'renpy.display.render.redraw', 'store.anim_tag', 'renpy.game.preferences.gl_powersave'), ('store.config.after_default_callbacks',)) and hasattr(engine.game.preferences, "gl_framerate") and store.lssb_compat.method_matches(engine.gl2.live2d.Live2D.render, 'fd6572a06a79998a145e42f2ec533f75a4b8ead3b026e004ebc38e7765c0755d') and store.lssb_compat.method_matches(engine.gl2.live2d.update_states, '5cfc8aa4688b2ba1d11458d3a1a8e69c06c99eaed6223d05c36fccdc71690c6a')
    enabled = False
    initialized = False
    startup_framerate = None
    actor_count = 0
    rendering_sprite = None
    sprite_files = frozenset()
    sprite_tags = frozenset()
    applied_preferences = {'gl_framerate': 60, 'gl_powersave': True}
    original_render = store.lssb_compat.resolve("renpy.gl2.live2d.Live2D.render")
    original_redraw = store.lssb_compat.resolve("renpy.display.render.redraw")
    original_update_states = store.lssb_compat.resolve("renpy.gl2.live2d.update_states")

    def apply_preferences():
        previous = store.persistent.lssb_render_previous_preferences
        if not isinstance(previous, dict):
            previous = {key: getattr(engine.game.preferences, key) for key in applied_preferences}
            store.persistent.lssb_render_previous_preferences = previous
        for key, value in applied_preferences.items():
            setattr(engine.game.preferences, key, value)

    def restore_preferences():
        global enabled
        enabled = False
        previous = store.persistent.lssb_render_previous_preferences
        if isinstance(previous, dict):
            for key, value in applied_preferences.items():
                # Preserve a later choice made in the game's own settings.
                if key in previous and getattr(engine.game.preferences, key) == value:
                    setattr(engine.game.preferences, key, previous[key])
        store.persistent.lssb_render_previous_preferences = None

    def set_enabled(value):
        global enabled
        if not supported:
            return
        value = bool(value)
        store.persistent.lssb_balanced_rendering = value
        if value:
            apply_preferences()
            enabled = True
        else:
            restore_preferences()
        api.restart_interaction()

    def restart_required():
        return supported and engine.game.preferences.gl_framerate != startup_framerate

    def after_defaults():
        global initialized, enabled, startup_framerate
        if initialized or not supported:
            return
        initialized = True
        if store.persistent.lssb_balanced_rendering is None:
            store.persistent.lssb_balanced_rendering = True
        enabled = bool(store.persistent.lssb_balanced_rendering)
        if enabled:
            apply_preferences()
        startup_framerate = engine.game.preferences.gl_framerate

    def count_actors(showing):
        global actor_count
        # Read the states already resolved by the engine. The game's show_people
        # uses 'what=', so its visible image tags have no 'anim' attributes.
        if enabled and showing:
            tags = api.get_showing_tags(layer='master')
            actor_count = len({name[1] for name, state in engine.gl2.live2d.states.items()
                if name[0] == 'master' and name[1] in tags and name[1] in sprite_tags
                and state.cycle_new and state.new is not None and state.new.filename in sprite_files})
        else:
            actor_count = 0

    def update_states():
        showing = engine.gl2.live2d.live2d_showing
        result = original_update_states()
        count_actors(showing)
        return result

    def render_sprite(self, width, height, st, at):
        global rendering_sprite
        if not enabled or actor_count < 2 or self.filename not in sprite_files:
            return original_render(self, width, height, st, at)
        previous = rendering_sprite
        rendering_sprite = self
        try:
            return original_render(self, width, height, st, at)
        finally:
            rendering_sprite = previous

    def redraw(displayable, delay):
        # Only the model's own continuous redraw. Explicit changes, UI events,
        # non-sprite CGs, videos, and other displayables retain native scheduling.
        if rendering_sprite is not None and displayable is rendering_sprite:
            delay = max(delay, 1.0 / 30.0)
        return original_redraw(displayable, delay)

    if supported:
        sprite_tags = frozenset(store.anim_tag)
        sprite_files = frozenset(d.filename for name, d in engine.display.image.images.items()
            if len(name) >= 2 and name[0] in sprite_tags and name[-1] == 'anim'
            and isinstance(d, engine.gl2.live2d.Live2D))
        store.config.after_default_callbacks.append(after_defaults)
        engine.gl2.live2d.update_states = update_states
        engine.gl2.live2d.Live2D.render = render_sprite
        engine.display.render.redraw = redraw

screen lssb_performance_settings():
    modal True
    zorder 320
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Hide("lssb_performance_settings")
    add Solid("#071a28ed")
    frame:
        background Solid("#173c50")
        padding (32, 28)
        xsize 860
        align (0.5, 0.5)
        vbox:
            spacing 18
            text "ПЛАВНОСТЬ ИГРЫ" style "lssb_performance_title"
            if lssb_performance.restart_required():
                text "Перезапустите игру, чтобы применить выбранную частоту кадров." style "lssb_performance_text" color "#ffd095" xsize 790
            if not lssb_performance.supported:
                text "Изменилась реализация движка. Используется штатная отрисовка." style "lssb_performance_text"
            text "Выберите частоту обновления. Качество изображений одинаковое в обоих режимах." style "lssb_performance_text" xsize 790
            textbutton "Сбалансированный — 60 FPS":
                style "lssb_performance_button"
                selected lssb_performance.enabled
                sensitive lssb_performance.supported
                action Function(lssb_performance.set_enabled, True)
            text "Один персонаж — до 60 кадров/с; несколько — до 30 кадров/с. Интерфейс работает отдельно. На неподвижной сцене игра снижает нагрузку и сразу реагирует на ввод." style "lssb_performance_text" xsize 790
            textbutton "Исходный режим игры":
                style "lssb_performance_button"
                selected not lssb_performance.enabled
                sensitive lssb_performance.supported
                action Function(lssb_performance.set_enabled, False)
            text "Возвращает прежние настройки частоты кадров и энергосбережения. На мониторе с высокой частотой обновления нагрузка может быть выше." style "lssb_performance_text" xsize 790
            textbutton "Назад" style "lssb_performance_button" action Hide("lssb_performance_settings")

style lssb_performance_text is text:
    font "DejaVuSans.ttf"
    size 19
    color "#e7f5fc"
    outlines []
style lssb_performance_title is lssb_performance_text:
    font "DejaVuSans-Bold.ttf"
    size 30
style lssb_performance_button is button:
    background Solid("#32687c")
    hover_background Solid("#438ba0")
    selected_idle_background Solid("#157d85")
    selected_hover_background Solid("#239e9e")
    padding (18, 12)
    xfill True
style lssb_performance_button_text is lssb_performance_text:
    size 21
    align (0.5, 0.5)
