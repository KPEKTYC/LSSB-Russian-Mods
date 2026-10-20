# Natalie has no native choices or usable character-specific nicknames.
# Keep prior caption delegation available without adding a choice screen.
init 1049 python in lssb_natalie:
    import store
    _constant = True
    strings = {}
    def caption(value):
        return store.lssb_morgan.caption(value)
