# City assets only; retain the game's virtual resolution and seasonal picker.
init 998 python:
    _lssb_visual_map_logical_size = (1280, 720)
    _lssb_visual_map_assets = {('spring', 'day'): 'lssb_visual_quality/maps/map_season_day_spring.webp', ('spring', 'night'): 'lssb_visual_quality/maps/map_season_night_spring.webp', ('summer', 'day'): 'lssb_visual_quality/maps/map_season_day_summer.webp', ('summer', 'night'): 'lssb_visual_quality/maps/map_season_night_summer.webp', ('fall', 'day'): 'lssb_visual_quality/maps/map_season_day_fall.webp', ('fall', 'night'): 'lssb_visual_quality/maps/map_season_night_fall.webp', ('winter', 'day'): 'lssb_visual_quality/maps/map_season_day_winter.webp', ('winter', 'night'): 'lssb_visual_quality/maps/map_season_night_winter.webp'}
    if (config.screen_width, config.screen_height) == (1280,720):
        for (_lssb_season, _lssb_light), _lssb_map_path in _lssb_visual_map_assets.items():
            if not renpy.has_image("bg_map_season_%s_%s" % (_lssb_light, _lssb_season), exact=True):
                continue
            renpy.image("bg_map_season_%s_%s" % (_lssb_light, _lssb_season),
                Image(_lssb_map_path, oversample=4, mipmap=True))
