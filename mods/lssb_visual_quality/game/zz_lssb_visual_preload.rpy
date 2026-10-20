# Predict nearby static backgrounds with Ren'Py's existing asynchronous loader.
# No synchronous decoding, gameplay queries, save data, or cache-limit changes.
init 1008 python in lssb_background_preload:
    import renpy
    import store
    _constant = True
    enabled = False
    error_logged = False
    max_targets = 48

    def target_names():
        game = getattr(store, "game", None)
        room_class = getattr(store, "Room", None)
        if game is None or room_class is None:
            return ()
        room_id = getattr(game, "room", None)
        if not isinstance(room_id, str):
            return ()
        current = room_class.find(room_id)
        if current is None:
            return ()
        # The three hubs are frequent destinations from rooms whose exits are
        # supplied by screens. The remaining targets are the native room links.
        ids = [room_id, "map", "mallmap", "housemap"]
        ids.extend(getattr(current, "exits", ()))
        names = []
        seen = set()
        for room_id in ids:
            if not isinstance(room_id, str):
                continue
            name = "bg " + room_id
            if name not in seen and renpy.exports.has_image(name, exact=True):
                seen.add(name)
                names.append(name)
            if len(names) >= max_targets:
                break
        return tuple(names)

    def predict():
        global error_logged
        if not enabled:
            return
        try:
            for name in target_names():
                # Called only by the native prediction coroutine. Its image
                # function queues decoding on the engine's preload thread.
                renpy.display.predict.displayable(renpy.easy.displayable(name))
        except Exception as error:
            if not error_logged:
                renpy.exports.log("LSSB background preload unavailable: " + type(error).__name__)
                error_logged = True

    if store.lssb_compat.require('Предзагрузка', ('store.Room.find', 'renpy.exports.has_image', 'renpy.display.predict.displayable', 'renpy.easy.displayable'), ('store.config.predict_callbacks',)):
        store.config.predict_callbacks.append(predict)
        enabled = True
