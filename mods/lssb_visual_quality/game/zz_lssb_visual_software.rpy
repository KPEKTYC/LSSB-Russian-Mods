# Preserve the software renderer's 2-pixel sampling border after alpha conversion.
# Only the inspected SW loader is wrapped; GL2 and image/layout data are untouched.
init 980 python in lssb_software:
    import renpy as engine
    import store
    from store import renpy as api
    _constant = True
    installed = False
    original_load_texture = None

    def padded_load_texture(self, surf, transient=False, properties={}):
        texture = original_load_texture(self, surf, transient, properties)
        # convert_alpha returns a standalone surface. The native affine sampler
        # reads the next column/row even when sampling the final source pixel.
        # Keep the converted format and pixel bytes, with transparent padding.
        width, height = texture.get_size()
        backing = engine.pygame.Surface((width + 4, height + 4), 0, texture)
        backing.fill((0, 0, 0, 0))
        padded = backing.subsurface((2, 2, width, height))
        engine.display.accelerator.nogil_copy(texture, padded)
        return padded

    try:
        import renpy.display.swdraw as swdraw
    except ImportError:
        swdraw = None
    if swdraw is not None:
        original_load_texture = getattr(getattr(swdraw, 'SWDraw', None), 'load_texture', None)
        if (store.lssb_compat.require('Программный рендерер', (
                'renpy.pygame.Surface', 'renpy.display.accelerator.nogil_copy'))
                and store.lssb_compat.method_matches(original_load_texture, '45505d213cc78611a9a0ebd2f5c327b74bd7fb93a84aa26385b05bc308bcdd45')):
            swdraw.SWDraw.load_texture = padded_load_texture
            installed = True
        else:
            store.lssb_compat.disabled['Программный рендерер'] = 'реализация загрузчика текстур изменилась'
            api.log('LSSB software: unknown texture loader; native implementation retained.')
