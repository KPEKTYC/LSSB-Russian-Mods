# Scene-colored screen edges; standard Ren'Py scaling and input mapping are retained.
default persistent.lssb_ambient_edges = True

init 1005 python:
    import builtins as _lssb_display_builtins
    import time as _lssb_display_time

    _lssb_display_palette = {'bg/jail/jail.webp': '#696660', 'bg/rooftop/rooftop.webp': '#875542', 'bg/arena/arena.webp': '#3c385d', 'bg/gymlockers/gymlockers.webp': '#877864', 'bg/cinemaroom/cinemaroom.webp': '#0e0a10', 'bg/sexshop/sexshop.webp': '#785257', 'bg/audreybedroom/audreybedroom_night.webp': '#5d4d44', 'bg/audreybedroom/audreybedroom_day.webp': '#5c5250', 'bg/rpg/rpg_village_day.webp': '#6d7b83', 'bg/rpg/rpg_village_map.webp': '#616542', 'bg/rpg/rpgfeast.webp': '#613e2e', 'bg/rpg/rpgroad.webp': '#577d77', 'bg/rpg/rpg_village_night.webp': '#1d253b', 'bg/rpg/rpgforest.webp': '#15211b', 'bg/rpg/rpggarden.webp': '#375c5e', 'bg/rpg/rpgthrone.webp': '#724b37', 'bg/gym/gym.webp': '#7a7661', 'bg/street/street_season_night_fall.webp': '#3f3634', 'bg/street/street_season_night_spring.webp': '#4a383d', 'bg/street/street_season_day_summer.webp': '#636467', 'bg/street/street_season_day_spring.webp': '#766969', 'bg/street/street_season_night_summer.webp': '#3c3639', 'bg/street/street_season_day_fall.webp': '#6e5f59', 'bg/street/street_season_day_winter.webp': '#7b7d7a', 'bg/street/street_season_night_winter.webp': '#4c3f41', 'bg/bookstore/bookstore.webp': '#775d44', 'bg/university/university_season_day_winter.webp': '#7a7674', 'bg/university/university_season_day_summer.webp': '#6c7475', 'bg/university/university_season_day_spring.webp': '#6d7575', 'bg/university/university_season_day_fall.webp': '#6f7574', 'bg/publicbathroom/publicbathroom.webp': '#5b616b', 'bg/trailerinside/trailerinside_day.webp': '#655851', 'bg/trailerinside/trailerinside_night.webp': '#6c584e', 'bg/doors/bg_door_restaurant_day.webp': '#372e24', 'bg/doors/bg_door_restaurant_night.webp': '#382e24', 'bg/doors/bg_door_mansionentrance_day.webp': '#7c7d77', 'bg/doors/bg_door_pub2.webp': '#404336', 'bg/doors/bg_door_black_secure.webp': '#757a74', 'bg/doors/bg_door_office_openspace.webp': '#736b5b', 'bg/doors/bg_door_pub.webp': '#3f4335', 'bg/doors/bg_door_black_simple.webp': '#757a74', 'bg/doors/bg_door_houseentrance_night.webp': '#756858', 'bg/doors/bg_door_hallway.webp': '#827461', 'bg/doors/bg_door_mansion.webp': '#6a6150', 'bg/doors/bg_door_mdr.webp': '#827461', 'bg/doors/bg_door_fancy.webp': '#958f89', 'bg/doors/bg_door_palla.webp': '#8b877f', 'bg/doors/bg_door_house_bedroom2.webp': '#776553', 'bg/doors/bg_door_houseentrance_day.webp': '#746858', 'bg/doors/bg_door_office_private2.webp': '#746a58', 'bg/doors/bg_door_office_private.webp': '#6e6555', 'bg/doors/bg_door_mansionentrance_night.webp': '#3b403e', 'bg/doors/bg_door_house_bathroom.webp': '#7a6956', 'bg/doors/bg_door_house_bedroom3.webp': '#776653', 'bg/doors/bg_door_double.webp': '#756859', 'bg/photostudio/photostudio.webp': '#919291', 'bg/map/map_season_day_fall.webp': '#6a6a5f', 'bg/map/map_season_night_summer.webp': '#2f3d44', 'bg/map/map_season_night_spring.webp': '#3c3e3b', 'bg/map/map_season_night_winter.webp': '#414f5b', 'bg/map/map_season_day_summer.webp': '#626d66', 'bg/map/map_season_night_fall.webp': '#393d3f', 'bg/map/map_season_day_winter.webp': '#7a7f80', 'bg/map/map_season_day_spring.webp': '#6b6c66', 'bg/taxi/bg_taxi_back_night.webp': '#39383e', 'bg/taxi/bg_taxi_back_day.webp': '#757377', 'bg/coffeeshop/coffeeshop.webp': '#574642', 'bg/vip/vip.webp': '#341d4a', 'bg/pubplay/pubplay.webp': '#3a2f1b', 'bg/trailer/trailer_season_night_spring.webp': '#0d1419', 'bg/trailer/trailer_season_night_burned_spring.webp': '#070e13', 'bg/trailer/trailer_season_night_burned_winter.webp': '#0b1019', 'bg/trailer/trailer_season_day_winter.webp': '#666861', 'bg/trailer/trailer_season_day_burned_summer.webp': '#474e3c', 'bg/trailer/trailer_season_day_spring.webp': '#58694a', 'bg/trailer/trailer_season_night_fall.webp': '#0f151a', 'bg/trailer/trailer_season_day_burned_fall.webp': '#4a4b39', 'bg/trailer/trailer_season_day_burned_spring.webp': '#425338', 'bg/trailer/trailer_season_night_winter.webp': '#101621', 'bg/trailer/trailer_season_night_summer.webp': '#0d1518', 'bg/trailer/trailer_season_day_summer.webp': '#5b634d', 'bg/trailer/trailer_season_night_burned_summer.webp': '#040a0e', 'bg/trailer/trailer_season_day_fall.webp': '#5e604b', 'bg/trailer/trailer_season_night_burned_fall.webp': '#070b11', 'bg/trailer/trailer_season_day_burned_winter.webp': '#5a5c59', 'bg/balcony/balcony_day.webp': '#646d71', 'bg/balcony/balcony_night.webp': '#302c26', 'bg/restroom/restroom.webp': '#3a2c2b', 'bg/bakery/bakery.webp': '#615045', 'bg/electronic/electronic.webp': '#635e5e', 'bg/housemap/housemap_ground_season_day_winter.webp': '#868481', 'bg/housemap/housemap_ground_season_night_fall.webp': '#363735', 'bg/housemap/housemap_ground_season_night_winter.webp': '#43495a', 'bg/housemap/housemap_ground_season_day_summer.webp': '#696d5f', 'bg/housemap/housemap_ground_season_day_fall.webp': '#6e6a5e', 'bg/housemap/housemap_ground_season_night_summer.webp': '#343736', 'bg/housemap/housemap_ground_season_night_spring.webp': '#38393c', 'bg/housemap/housemap_ground_season_day_spring.webp': '#726e67', 'bg/maidcafe/maidcafe.webp': '#786b6c', 'bg/personal/personal_night.webp': '#5a4b42', 'bg/personal/personal_day.webp': '#665854', 'bg/park/date_park_season_day_spring.webp': '#64574f', 'bg/park/park_season_day_fall.webp': '#595032', 'bg/park/park_season_day_spring.webp': '#64574f', 'bg/park/park_season_night_summer.webp': '#122629', 'bg/park/date_park_season_night_winter.webp': '#29435c', 'bg/park/date_park_season_day_winter.webp': '#657274', 'bg/park/date_park_season_night_spring.webp': '#342324', 'bg/park/park_season_night_winter.webp': '#29435c', 'bg/park/park_season_night_fall.webp': '#28211c', 'bg/park/date_park_season_day_fall.webp': '#595032', 'bg/park/park_season_day_winter.webp': '#657274', 'bg/park/date_park_season_night_summer.webp': '#122629', 'bg/park/park_season_day_summer.webp': '#40553b', 'bg/park/park_season_night_spring.webp': '#342324', 'bg/park/date_park_season_night_fall.webp': '#28211c', 'bg/park/date_park_season_day_summer.webp': '#40553b', 'bg/communitycenter/communitycenter.webp': '#565551', 'bg/communitycenter/communitycenter_empty.webp': '#535554', 'bg/mall2/mall2.webp': '#746a65', 'bg/alley/alley_season_night_spring.webp': '#231829', 'bg/alley/alley_season_night_winter.webp': '#352e4f', 'bg/alley/alley_season_day_summer.webp': '#3a3a41', 'bg/alley/alley_season_day_spring.webp': '#3b3941', 'bg/alley/alley_season_night_fall.webp': '#241824', 'bg/alley/alley_season_day_fall.webp': '#3a3c40', 'bg/alley/alley_season_day_winter.webp': '#51525b', 'bg/alley/alley_season_night_summer.webp': '#1d1822', 'bg/pubexterior/pubexterior_season_day_spring.webp': '#4c463f', 'bg/pubexterior/pubexterior_season_night_fall.webp': '#3b2d1d', 'bg/pubexterior/pubexterior_season_day_winter.webp': '#4d4a44', 'bg/pubexterior/pubexterior_season_night_winter.webp': '#312d27', 'bg/pubexterior/pubexterior_season_night_spring.webp': '#3b2c21', 'bg/pubexterior/pubexterior_season_day_fall.webp': '#4d473c', 'bg/pubexterior/pubexterior_season_day_summer.webp': '#514e47', 'bg/pubexterior/pubexterior_season_night_summer.webp': '#3f3122', 'bg/aquarium/aquarium.webp': '#1a4a6c', 'bg/pool/pool_season_night_fall.webp': '#111d32', 'bg/pool/pool_season_night_halloween.webp': '#121d31', 'bg/pool/pool_season_night_summer.webp': '#11263a', 'bg/pool/pool_season_day_winter.webp': '#767f83', 'bg/pool/pool_season_night_winter.webp': '#131e32', 'bg/pool/pool_season_day_summer.webp': '#59767e', 'bg/pool/pool_season_day_spring.webp': '#717d89', 'bg/pool/pool_season_night_spring.webp': '#15273b', 'bg/pool/pool_season_day_fall.webp': '#6a7378', 'bg/pool/pool_season_day_halloween.webp': '#697377', 'bg/house/house_season_day_winter.webp': '#6a737e', 'bg/house/house_season_day_car_fall.webp': '#5e5c49', 'bg/house/house_season_night_summer.webp': '#101925', 'bg/house/house_season_day_bike_winter.webp': '#69727d', 'bg/house/house_season_day_car_spring.webp': '#645a55', 'bg/house/house_season_night_sportscar_spring.webp': '#1d1817', 'bg/house/house_season_day_bike_fall.webp': '#5e5c49', 'bg/house/house_season_night_sportscar_fall.webp': '#19170f', 'bg/house/house_season_night_car_fall.webp': '#19170f', 'bg/house/house_season_night_car_winter.webp': '#18233e', 'bg/house/house_season_night_winter.webp': '#18233e', 'bg/house/house_season_day_sportscar_winter.webp': '#67717c', 'bg/house/house_season_night_bike_fall.webp': '#19170f', 'bg/house/house_season_day_car_winter.webp': '#6a737e', 'bg/house/house_season_night_car_summer.webp': '#101925', 'bg/house/house_season_night_bike_summer.webp': '#101925', 'bg/house/house_season_day_fall.webp': '#5e5c48', 'bg/house/house_season_day_bike_summer.webp': '#55614f', 'bg/house/house_season_day_summer.webp': '#55614f', 'bg/house/house_season_night_spring.webp': '#1e1818', 'bg/house/house_season_night_sportscar_summer.webp': '#101924', 'bg/house/house_season_night_sportscar_winter.webp': '#18233d', 'bg/house/house_season_night_bike_winter.webp': '#18233e', 'bg/house/house_season_day_sportscar_summer.webp': '#545f4d', 'bg/house/house_season_night_fall.webp': '#19170f', 'bg/house/house_season_day_sportscar_fall.webp': '#5c5a47', 'bg/house/house_season_night_car_spring.webp': '#1e1818', 'bg/house/house_season_day_sportscar_spring.webp': '#625853', 'bg/house/house_season_day_car_summer.webp': '#55614f', 'bg/house/house_season_day_spring.webp': '#635954', 'bg/house/house_season_night_bike_spring.webp': '#1d1818', 'bg/house/house_season_day_bike_spring.webp': '#635954', 'bg/pub/pub.webp': '#302514', 'bg/kart/kart.webp': '#7a6c5c', 'bg/bedroom5/attic_night.webp': '#040609', 'bg/bedroom5/bedroom5_night.webp': '#725c4b', 'bg/bedroom5/attic_day.webp': '#3c363a', 'bg/bedroom5/bedroom5_day.webp': '#816f67', 'bg/breakroom/breakroom_night.webp': '#5d5f60', 'bg/breakroom/breakroom_day.webp': '#5d6265', 'bg/pubseat/pubseat.webp': '#3c3529', 'bg/stripclub/stripclub.webp': '#2c1830', 'bg/bedroom1/bedroom1_night.webp': '#243754', 'bg/bedroom1/bedroom1_day.webp': '#3c4b5d', 'bg/alettaoffice/alettaoffice_day.webp': '#5d5854', 'bg/alettaoffice/alettaoffice_night.webp': '#46403b', 'bg/pallalivingroom/pallalivingroom.webp': '#706760', 'bg/bedroom2/bedroom2_day.webp': '#906c87', 'bg/bedroom2/bedroom2_night.webp': '#835771', 'bg/beach/beach_day.webp': '#6b8992', 'bg/beach/nudistbeach_night.webp': '#302e3d', 'bg/beach/nudistbeach_day.webp': '#6b8992', 'bg/beach/beach_night.webp': '#302e3d', 'bg/cinema/cinema_season_day_summer.webp': '#6b6962', 'bg/cinema/date_cinema_season_night_spring.webp': '#5c3d3e', 'bg/cinema/cinema_season_night_summer.webp': '#503d3d', 'bg/cinema/date_cinema_season_night_summer.webp': '#503d3d', 'bg/cinema/cinema_season_night_winter.webp': '#53474a', 'bg/cinema/date_cinema_season_day_winter.webp': '#7a757a', 'bg/cinema/date_cinema_season_day_fall.webp': '#73695e', 'bg/cinema/cinema_season_day_spring.webp': '#80726d', 'bg/cinema/date_cinema_season_night_fall.webp': '#543932', 'bg/cinema/cinema_season_day_winter.webp': '#7a757a', 'bg/cinema/cinema_season_night_spring.webp': '#5c3d3e', 'bg/cinema/cinema_season_night_fall.webp': '#543932', 'bg/cinema/date_cinema_season_day_spring.webp': '#80726d', 'bg/cinema/date_cinema_season_day_summer.webp': '#6b6962', 'bg/cinema/cinema_season_day_fall.webp': '#73695e', 'bg/cinema/date_cinema_season_night_winter.webp': '#53474a', 'bg/mallmap/mallmap.webp': '#615955', 'bg/restaurant/restaurant.webp': '#3b271d', 'bg/hallway/hallway.webp': '#5a4e40', 'bg/studio/studio.webp': '#51361e', 'bg/samhome/samhome.webp': '#7b7264', 'bg/shawnbedroom/shawnbedroom_day.webp': '#2f2c27', 'bg/shawnbedroom/shawnbedroom_night.webp': '#30241f', 'bg/warehouse/bg_warehouse_door_closed.webp': '#2b3745', 'bg/warehouse/bg_warehouse_door_open.webp': '#2c3845', 'bg/bathroom/bathroom_night.webp': '#635657', 'bg/bathroom/bathroom_day.webp': '#777472', 'bg/waterpark2/waterpark2.webp': '#5e7e8c', 'bg/church/church.webp': '#5e4437', 'bg/church/church_wedding.webp': '#634a3c', 'bg/forest/forest_season_night_fall.webp': '#010a0d', 'bg/forest/forest_season_night_winter.webp': '#081c37', 'bg/forest/forest_season_night_spring.webp': '#000810', 'bg/forest/forest_season_day_winter.webp': '#435a5f', 'bg/forest/forest_season_day_summer.webp': '#2e492b', 'bg/forest/forest_season_night_summer.webp': '#01070d', 'bg/forest/forest_season_day_fall.webp': '#414924', 'bg/forest/forest_season_day_spring.webp': '#3b4f30', 'bg/gymmachine/gymmachine.webp': '#676255', 'bg/mansionentrance/mansionentrance_season_night_winter.webp': '#333848', 'bg/mansionentrance/mansionentrance_season_day_summer.webp': '#5b7865', 'bg/mansionentrance/mansionentrance_season_day_spring.webp': '#5f7562', 'bg/mansionentrance/mansionentrance_season_night_spring.webp': '#202929', 'bg/mansionentrance/mansionentrance_season_day_christmas_decor.webp': '#868c8b', 'bg/mansionentrance/mansionentrance_season_night_fall.webp': '#23241d', 'bg/mansionentrance/mansionentrance_season_night_christmas_decor.webp': '#333948', 'bg/mansionentrance/mansionentrance_season_night_summer.webp': '#1a2526', 'bg/mansionentrance/mansionentrance_season_day_winter.webp': '#868d8c', 'bg/mansionentrance/mansionentrance_season_day_fall.webp': '#6c7363', 'bg/audreylivingroom/audreylivingroom_day.webp': '#504640', 'bg/audreylivingroom/audreylivingroom_night.webp': '#72645c', 'bg/jewelrystore/jewelrystore.webp': '#6f5846', 'bg/policestation/policestation_day.webp': '#52595f', 'bg/policestation/policestation_night.webp': '#3f4247', 'bg/waterpark/waterpark.webp': '#486f86', 'bg/hospital/hospital_day.webp': '#6c645e', 'bg/hospital/hospital_night.webp': '#58534d', 'bg/drugstore/drugstore.webp': '#656f78', 'bg/tattooshop/tattooshop.webp': '#4f4841', 'bg/secondfloor/secondfloor.webp': '#6b5b4b', 'bg/kitchen/kitchen_night.webp': '#4d4340', 'bg/kitchen/kitchen_day.webp': '#554e4d', 'bg/ramenshop/ramenshop.webp': '#554a3b', 'bg/garage/garage.webp': '#68534b', 'bg/livingroom/livingroom_season_night_spring.webp': '#5d5458', 'bg/livingroom/livingroom_season_night_halloween_decor.webp': '#595250', 'bg/livingroom/livingroom_season_day_summer.webp': '#63676f', 'bg/livingroom/livingroom_season_day_winter.webp': '#696970', 'bg/livingroom/livingroom_season_night_christmas_decor.webp': '#5e5751', 'bg/livingroom/livingroom_season_day_fall.webp': '#666870', 'bg/livingroom/livingroom_season_day_christmas_decor.webp': '#717071', 'bg/livingroom/livingroom_season_night_summer.webp': '#5b5458', 'bg/livingroom/livingroom_season_night_fall.webp': '#5c5458', 'bg/livingroom/livingroom_season_day_halloween_decor.webp': '#6a6b70', 'bg/livingroom/livingroom_season_night_winter.webp': '#5e5758', 'bg/livingroom/livingroom_season_day_spring.webp': '#686970', 'bg/firstfloorbathroom/firstfloorbathroom_night.webp': '#7b7a72', 'bg/firstfloorbathroom/firstfloorbathroom_day.webp': '#7b7a72', 'bg/nightclubbar/nightclubbar.webp': '#28214f', 'bg/nightclub/nightclub.webp': '#2a274b', 'bg/shootingrange/shootingrange.webp': '#686452', 'bg/bedroom3/bedroom3_day.webp': '#704864', 'bg/bedroom3/bedroom3_night.webp': '#714061', 'bg/black.webp': '#000000', 'bg/concert/bg_concert_attendance_empty.webp': '#44384e', 'bg/concert/bg_concert_attendance_full.webp': '#343047', 'bg/cemetery/cemetery.webp': '#243535', 'bg/gamestore/gamestore.webp': '#57514e', 'bg/pond/pond_season_night_winter.webp': '#32485b', 'bg/pond/pond_season_day_spring.webp': '#61726a', 'bg/pond/pond_season_night_fall.webp': '#302a1f', 'bg/pond/pond_season_night_summer.webp': '#1f3032', 'bg/pond/pond_season_day_winter.webp': '#75818b', 'bg/pond/pond_season_day_summer.webp': '#5a7464', 'bg/pond/pond_season_day_fall.webp': '#6c735e', 'bg/pond/pond_season_night_spring.webp': '#2d3139', 'bg/classroom/classroom.webp': '#756e63', 'bg/arcade/arcade.webp': '#5f5355', 'bg/animalshelter/animalshelter.webp': '#685d4f', 'bg/hotelroom/hotelroom.webp': '#755a63', 'bg/houselibrary/houselibrary_day.webp': '#68605a', 'bg/houselibrary/houselibrary_night.webp': '#534940', 'bg/mall1/mall1.webp': '#64615d', 'bg/clothesshop/clothesshop.webp': '#58483c', 'bg/blank.webp': '#b8b8b8', 'bg/pallabedroom/pallabedroom_night.webp': '#685953', 'bg/pallabedroom/pallabedroom_day.webp': '#67625f', 'bg/ceo/ceo.webp': '#60544e', 'bg/flowershop/flowershop.webp': '#675b4f', 'bg/office/office_day.webp': '#696e66', 'bg/office/office_night.webp': '#5a5e56', 'bg/mansion/mansion_day.webp': '#554f51', 'bg/mansion/mansion_night.webp': '#4d3d35', 'bg/street2/street2_season_night_fall.webp': '#473c32', 'bg/street2/street2_season_night_winter.webp': '#49484b', 'bg/street2/street2_season_night_spring.webp': '#493d38', 'bg/street2/street2_season_day_fall.webp': '#686360', 'bg/street2/street2_season_day_winter.webp': '#6f7476', 'bg/street2/street2_season_day_spring.webp': '#6e6a69', 'bg/street2/street2_season_day_summer.webp': '#646866', 'bg/street2/street2_season_night_summer.webp': '#443d3a', 'bg/gymreception/gymreception.webp': '#776854', 'gui/main/mainmenu_bg.png': '#25647f', 'gui/game_menu.png': '#236886', 'lssb_visual_quality/maps/mallmap.webp': '#625a56', 'lssb_visual_quality/maps/map_season_day_fall.webp': '#6b6b61', 'lssb_visual_quality/maps/map_season_day_spring.webp': '#6d6e68', 'lssb_visual_quality/maps/map_season_day_summer.webp': '#656f68', 'lssb_visual_quality/maps/map_season_day_winter.webp': '#7f8384', 'lssb_visual_quality/maps/map_season_night_fall.webp': '#373b3d', 'lssb_visual_quality/maps/map_season_night_spring.webp': '#3b3d39', 'lssb_visual_quality/maps/map_season_night_summer.webp': '#2e3b42', 'lssb_visual_quality/maps/map_season_night_winter.webp': '#414e5b'}
    _lssb_display_fallback = "#334f5b"
    _lssb_display_last_poll = 0.0
    _lssb_display_source = None
    _lssb_display_error_logged = False
    _lssb_display_original_color = config.gl_clear_color
    _lssb_display_variants = ("lssb_display_26_8_0d", "lssb_display_ru_26_8_0d")

    def _lssb_display_label(russian, english):
        return russian if renpy.game.preferences.language == "russian" else english

    def _lssb_display_find_color(root, allow_solid=True):
        # Inspect only already-resolved children. Calling visit() here could
        # evaluate a DynamicDisplayable or predict hidden branches.
        pending = [root]
        seen = set()
        for _ in range(128):
            if not pending:
                break
            node = pending.pop()
            if node is None or _lssb_display_builtins.id(node) in seen:
                continue
            seen.add(_lssb_display_builtins.id(node))
            filename = getattr(node, "filename", None)
            if isinstance(filename, str) and filename in _lssb_display_palette:
                return filename, _lssb_display_palette[filename]
            if allow_solid and isinstance(node, renpy.display.imagelike.Solid) and node.color is not None:
                return "solid", node.color.hexcode
            children = getattr(node, "children", None)
            if isinstance(children, (_lssb_display_builtins.list, _lssb_display_builtins.tuple)):
                pending.extend(reversed(children))
            for attribute in ("child", "target"):
                child = getattr(node, attribute, None)
                if isinstance(child, renpy.display.displayable.Displayable):
                    pending.append(child)
        return None

    def _lssb_display_scene_color():
        if renpy.get_screen("preferences") is not None:
            return "preferences", _lssb_display_palette.get(gui.game_menu_background, _lssb_display_fallback)
        if renpy.get_screen("main_menu") is not None:
            path = gui.main_menu_background
            return "main_menu", _lssb_display_palette.get(path, _lssb_display_fallback)
        for screen_name in ("map", "mallmap", "housemap"):
            visible = renpy.get_screen(screen_name)
            if visible is not None:
                found = _lssb_display_find_color(visible, allow_solid=False)
                if found is not None:
                    return found
        backdrop = renpy.display.core.displayable_by_tag("master", "bg")
        found = _lssb_display_find_color(backdrop)
        if found is not None:
            return found
        return "fallback", _lssb_display_fallback

    def _lssb_display_update_edges(force=False):
        global _lssb_display_last_poll, _lssb_display_source, _lssb_display_error_logged
        now = _lssb_display_time.monotonic()
        if not force and now - _lssb_display_last_poll < 0.2:
            return
        _lssb_display_last_poll = now
        try:
            if persistent.lssb_ambient_edges:
                _lssb_display_source, color = _lssb_display_scene_color()
            else:
                _lssb_display_source, color = "disabled", _lssb_display_original_color
            if color != config.gl_clear_color:
                config.gl_clear_color = color
                if renpy.game.interface is not None:
                    renpy.game.interface.force_redraw = True
        except Exception as error:
            # A display enhancement must never break a dialogue or a menu.
            if not _lssb_display_error_logged:
                renpy.log("LSSB scene-colored edges unavailable: " + type(error).__name__)
                _lssb_display_error_logged = True

    def _lssb_display_set_edges(enabled):
        persistent.lssb_ambient_edges = bool(enabled)
        _lssb_display_update_edges(force=True)
        renpy.restart_interaction()

    def _lssb_display_sync_variant():
        for variant in _lssb_display_variants:
            if variant in config.variants:
                config.variants.remove(variant)
        localized = renpy.game.preferences.language == "russian" and hasattr(store, "_lssb_ui_translate")
        config.variants.insert(0, _lssb_display_variants[1 if localized else 0])

    if store.lssb_compat.require('Фон по краям', ('store.config.gl_clear_color', 'renpy.display.core.displayable_by_tag'), ('store.config.periodic_callbacks', 'store.config.display_start_callbacks')):
        config.periodic_callbacks.append(_lssb_display_update_edges)
        config.display_start_callbacks.append(_lssb_display_update_edges)
        for _lssb_display_language in set(renpy.known_languages()) | {None}:
            config.language_callbacks[_lssb_display_language].append(_lssb_display_sync_variant)
        _lssb_display_sync_variant()


screen preferences():
    variant "lssb_display_26_8_0d"
    tag menu
    style_prefix "lspref"
    add "gui/main/prefs_bg2.png"
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action [Hide("preferences"), Return()]
    zorder 50

    frame:
        style "invisible_frame"
        minimum 1100,500
        maximum 1100,500
        ypos 150
        xalign 0.5
        viewport id "prefs":
            draggable True
            mousewheel True
            has vbox
            spacing 40
            vbox:
                spacing 8
                text _lssb_display_label("Фон по краям", "Screen edges") font "DejaVuSans.ttf" size 26 color "#ffffff"
                text _lssb_display_label("Сохраняет пропорции и показывает изображение целиком.", "Keeps the original proportions and the entire picture.") font "DejaVuSans.ttf" size 18 color "#d8eef5"
                hbox:
                    spacing 24
                    textbutton _lssb_display_label("В цвет сцены", "Scene colors") id "lssb_edges_scene" text_font "DejaVuSans.ttf" text_size 22 selected persistent.lssb_ambient_edges action Function(_lssb_display_set_edges, True)
                    textbutton _lssb_display_label("Чёрные поля", "Black bars") id "lssb_edges_black" text_font "DejaVuSans.ttf" text_size 22 selected not persistent.lssb_ambient_edges action Function(_lssb_display_set_edges, False)
            vbox:
                spacing 20
                use text_tooltip(text_tag_resize(_("Global Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Force update check"), 230, 30), _("Force the check for new version"), "lspref_label_text")
                        textbutton _("Force update") action [SetVariable("persistent._update_last_checked", {}), SetVariable("persistent._update_version", {})]
                    if renpy.android:
                        if config.basedir.endswith('base'):

                            vbox:
                                xysize (450, 60)
                                use text_tooltip(text_tag_resize(_("Downloader:"), 450, 30), "", "lspref_label_text_title")
                                use text_tooltip(text_tag_resize(_("Force downloader startup"), 450, 30), _("Force launch downloader instead of the game"), "lspref_label_text")
                                textbutton text_tag_resize(_("Startup downloader"), 450) selected os.environ.get("USE_DOWNLOADER") action Function(search_in_path)
                        vbox:
                            xysize (300, 60)
                            use text_tooltip(text_tag_resize(_("DLCs:"), 300, 30), "", "lspref_label_text_title")
                            use text_tooltip(text_tag_resize(_("DLC Location"), 300, 30), _("Relocate your DLC file for the game to correctly load it (restart the game after locating the file)"), "lspref_label_text")
                            textbutton text_tag_resize(_("Import DLC file"), 300) action Function(move_rpa)
            vbox:
                spacing 20
                use text_tooltip(text_tag_resize(_("Video Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    if renpy.variant("pc"):
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(text_tag_resize(_("Screen Display"), 230, 30), _("Change the game's window display"), "lspref_label_text")
                            textbutton _("Window") action Preference("display", "window")
                            textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Powersave"), 230, 30), _("Turn on, save power and reduce heat by updating the screen less often.\nTurn off for smoother visuals but higher power use."), "lspref_label_text")
                        textbutton _("Enable") action Preference("gl powersave", True)
                        textbutton _("Disable") action Preference("gl powersave", False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_("New UI"), _("Enable new UI"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'new_ui', True)
                        textbutton _("Off") action SetField(persistent, 'new_ui', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_("X-Ray"), _("Allow to see through body during some scenes"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'xray', True)
                        textbutton _("Off") action SetField(persistent, 'xray', False)
                    if renpy.has_live2d() and any(dlc in DLCS for dlc in ('lively', 'fafow', 'fafwm')):
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(text_tag_resize(_("Animations"), 230, 30), _("Enable/Disable sprites animations"), "lspref_label_text")
                            textbutton _("On") action SetField(persistent, 'live2d_on', True)
                            textbutton _("Off") action SetField(persistent, 'live2d_on', False)
                    if 'lively' in DLCS:
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(text_tag_resize(_("Lively backgrounds"), 230, 30), _("Enable/Disable sprites in backgrounds"), "lspref_label_text")
                            textbutton _("On") action SetField(persistent, 'lively_bg', True)
                            textbutton _("Off") action SetField(persistent, 'lively_bg', False)
            vbox:
                spacing 20
                use text_tooltip(text_tag_resize(_("Gameplay Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Tutorial"), 230, 30), _("Enable/Disable the tutorial at the start of a new game"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'skip_tutorial', False)
                        textbutton _("Skip") action SetField(persistent, 'skip_tutorial', True)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Difficulty"), 230, 30), _("Change the game difficulty"), "lspref_label_text")
                        textbutton _("Easy") action SetField(persistent, 'difficulty', -1)
                        textbutton _("Normal") action SetField(persistent, 'difficulty', 0)
                        textbutton _("Difficult") action SetField(persistent, 'difficulty', 1)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Random Schedule"), 230, 30), _("Allow non-player characters to choose among several locations during this routine"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'schedule_randomness', True)
                        textbutton _("Off") action SetField(persistent, 'schedule_randomness', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Random Needs"), 225, 30), _("The need's cost can fluctuate when performing actions"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'needs_randomness', True)
                        textbutton _("Off") action SetField(persistent, 'needs_randomness', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Shuffle Choices"), 225, 30), _("Modify the order of the selections in nearly all of the menu choices"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'choices_shuffle', True)
                        textbutton _("Off") action SetField(persistent, 'choices_shuffle', False)

                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Notifications pop-up"), 230, 30), _("Enable/Disable the notification pop-up"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'notifications', True)
                        textbutton _("Hide") action SetField(persistent, 'notifications', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Close-up pop-ups"), 230, 30), _("Show/Hide the close-up inserts during sex scenes"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'hide_sex_inserts', False)
                        textbutton _("Hide") action SetField(persistent, 'hide_sex_inserts', True)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Pregnancy duration"), 230, 30), _("Change the pregnancy duration to suit your preference"), "lspref_label_text")
                        textbutton _("Endless") action SetField(persistent, 'pregnancy_end', False)
                        textbutton _("Immersive") action SetField(persistent, 'pregnancy_end', True)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Pregnancy pop-up"), 230, 30), _("Enable/Disable pregnancy pop-up"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'pregnancy_notification', True)
                        textbutton _("Hide") action SetField(persistent, 'pregnancy_notification', False)
                    if persistent.start_plus:
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(text_tag_resize(_("Reset NG+"), 230, 30), _("Clear NG+ saved statistics"), "lspref_label_text")
                            textbutton _("Clear stats") action Confirm("You're going to clear NG+ statistics.", Function(game.clear_new_game_plus))
                    if Achievement.total_unlocked:
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(text_tag_resize(_("Reset Achievements"), 230, 30), _("Clear all unlocked achievements"), "lspref_label_text")
                            textbutton _("Clear achievements") action Confirm("You're going to clear achievements.", Function(Achievement.reset))
                    if check_controller():
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(text_tag_resize(_("Frame Selector"), 230, 30), _("Allow to see selection with a framed border"), "lspref_label_text")
                            textbutton _("On") action SetField(persistent, 'selector', True)
                            textbutton _("Off") action SetField(persistent, 'selector', False)
            vbox:
                spacing 20
                use text_tooltip(text_tag_resize(_("Dialogue Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Text Speed"), 343, 30), _("Controls the rate at which text displays.\nThe further to the right this slider is, the faster the text will display.\nAll the way to the right causes text to be shown instantly."), "lspref_label_text")
                        bar value Preference("text speed")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Auto forward Time"), 343, 30), _("Controls automatic advance.\nThe further to the left this slider is, the shorter the amount of time before the game advances.\nAll the way to the right means text will never auto-forward."), "lspref_label_text")
                        bar value Preference("auto-forward time")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Rollback Side"), 230, 30), _("Enable a side of the screen to causes rollback"), "lspref_label_text")
                        textbutton _("Disable") action Preference("rollback side", "disable")
                        textbutton _("Left") action Preference("rollback side", "left")
                        textbutton _("Right") action Preference("rollback side", "right")
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Skip"), 230, 30), _("Allow the game to skipping parts, like texts or transitions"), "lspref_label_text")
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")
                        textbutton _("Transitions") action Preference("transitions", "toggle")
            vbox:
                spacing 20
                use text_tooltip(text_tag_resize(_("Audio Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Music Volume"), 343, 30), _("Controls the volume of the music.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("music volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Sound Volume"), 343, 30), _("Controls the volume of the sounds.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("sound volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Voice Volume"), 343, 30), _("Controls the volume of the voices.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("voice volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Ambience Volume"), 343, 30), _("Controls the volume of the sound ambience.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("ambience volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Sex Sounds Volume"), 343, 30), _("Controls the volume of the sex sounds.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("sexsfx volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Moans Volume"), 343, 30), _("Controls the volume of the moans.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("moans volume")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Mute audio"), 230, 30), _("Enable/Disable game audio"), "lspref_label_text")
                        textbutton _("Mute all") action Preference("all mute", "toggle") alt f"Mute all is {'On' if persistent.mute_characters else 'Off'}."
                        textbutton _("Mute alarm clock") selected persistent.mute_alarm_clock action ToggleField(persistent, 'mute_alarm_clock', True, False) alt f"Alarm clock sound is {'On' if not persistent.mute_alarm_clock else 'Off'}."
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Mute voice"), 230, 30), _("Enable/Disable character voice"), "lspref_label_text")
                        textbutton _("Mute Bree") action [ToggleVoiceMute("bree")] alt f"Mute Bree is {'On' if 'bree' in persistent._voice_mute else 'Off'}."
                        textbutton _("Mute Mike") action [ToggleVoiceMute("mike")] alt f"Mute Mike is {'On' if 'mike' in persistent._voice_mute else 'Off'}."
                        textbutton _("Mute all characters") selected persistent.mute_characters action Function(toggle_mute_all_characters) alt f"Mute all characters is {'On' if persistent.mute_characters else 'Off'}."
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Self-voicing"), 230, 30), _("Self-voicing setting"), "lspref_label_text")
                        textbutton _("Override voice") selected persistent.tts_override action Function(toggle_tts_override_voice_channel) alt f"Self-voicing override voice is {'On' if persistent.tts_override else 'Off'}."
        vbar:
            value YScrollValue("prefs")
            left_bar "gui/inv/vertical_idle_bar.png"
            right_bar "gui/inv/vertical_idle_bar.png"
            thumb "gui/inv/vertical_idle_thumb.png"
            thumb_offset 63
            left_gutter 63
            right_gutter 63
            maximum 11,359
            xpos 1100
            yalign 0.5
    button style "return_arrow_button" action [Hide("preferences"),Return()] tooltip "" default_focus check_controller()

    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            style_prefix "tooltips"

            has frame
            yanchor 0
            xalign 0.5
            xpadding 20
            text tooltip substitute False yalign 0.05



screen preferences():
    variant "lssb_display_ru_26_8_0d"
    tag menu
    style_prefix "lspref"
    add gui.game_menu_background
    text "OPTIONS" xalign 0.5 ypos 42 font "palanquin_bold" size 48 color "#62ACD1" outlines [(3,"#000000")]
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action [Hide("preferences"), Return()]
    zorder 50

    frame:
        style "invisible_frame"
        minimum 1100,500
        maximum 1100,500
        ypos 150
        xalign 0.5
        viewport id "prefs":
            draggable True
            mousewheel True
            has vbox
            spacing 40
            vbox:
                spacing 8
                text _lssb_display_label("Фон по краям", "Screen edges") font "DejaVuSans.ttf" size 26 color "#ffffff"
                text _lssb_display_label("Сохраняет пропорции и показывает изображение целиком.", "Keeps the original proportions and the entire picture.") font "DejaVuSans.ttf" size 18 color "#d8eef5"
                hbox:
                    spacing 24
                    textbutton _lssb_display_label("В цвет сцены", "Scene colors") id "lssb_edges_scene" text_font "DejaVuSans.ttf" text_size 22 selected persistent.lssb_ambient_edges action Function(_lssb_display_set_edges, True)
                    textbutton _lssb_display_label("Чёрные поля", "Black bars") id "lssb_edges_black" text_font "DejaVuSans.ttf" text_size 22 selected not persistent.lssb_ambient_edges action Function(_lssb_display_set_edges, False)
            vbox:
                spacing 20
                use text_tooltip(_lssb_ui_resize(_("Global Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Force update check"), 230, 30), _("Force the check for new version"), "lspref_label_text")
                        textbutton _("Force update") action [SetVariable("persistent._update_last_checked", {}), SetVariable("persistent._update_version", {})]
                    if renpy.android:
                        if config.basedir.endswith('base'):

                            vbox:
                                xysize (450, 60)
                                use text_tooltip(_lssb_ui_resize(_("Downloader:"), 450, 30), "", "lspref_label_text_title")
                                use text_tooltip(_lssb_ui_resize(_("Force downloader startup"), 450, 30), _("Force launch downloader instead of the game"), "lspref_label_text")
                                textbutton _lssb_ui_resize(_("Startup downloader"), 450) selected os.environ.get("USE_DOWNLOADER") action Function(search_in_path)
                        vbox:
                            xysize (300, 60)
                            use text_tooltip(_lssb_ui_resize(_("DLCs:"), 300, 30), "", "lspref_label_text_title")
                            use text_tooltip(_lssb_ui_resize(_("DLC Location"), 300, 30), _("Relocate your DLC file for the game to correctly load it (restart the game after locating the file)"), "lspref_label_text")
                            textbutton _lssb_ui_resize(_("Import DLC file"), 300) action Function(move_rpa)
            vbox:
                spacing 20
                use text_tooltip(_lssb_ui_resize(_("Video Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    if renpy.variant("pc"):
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(_lssb_ui_resize(_("Screen Display"), 230, 30), _("Change the game's window display"), "lspref_label_text")
                            textbutton _("Window") action Preference("display", "window")
                            textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Powersave"), 230, 30), _("Turn on, save power and reduce heat by updating the screen less often.\nTurn off for smoother visuals but higher power use."), "lspref_label_text")
                        textbutton _("Enable") action Preference("gl powersave", True)
                        textbutton _("Disable") action Preference("gl powersave", False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize("New UI", 230, 30), _("Enable new UI"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'new_ui', True)
                        textbutton _("Off") action SetField(persistent, 'new_ui', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_("X-Ray"), _("Allow to see through body during some scenes"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'xray', True)
                        textbutton _("Off") action SetField(persistent, 'xray', False)
                    if renpy.has_live2d() and any(dlc in DLCS for dlc in ('lively', 'fafow', 'fafwm')):
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(_lssb_ui_resize(_("Animations"), 230, 30), _("Enable/Disable sprites animations"), "lspref_label_text")
                            textbutton _("On") action SetField(persistent, 'live2d_on', True)
                            textbutton _("Off") action SetField(persistent, 'live2d_on', False)
                    if 'lively' in DLCS:
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(_lssb_ui_resize(_("Lively backgrounds"), 230, 30), _("Enable/Disable sprites in backgrounds"), "lspref_label_text")
                            textbutton _("On") action SetField(persistent, 'lively_bg', True)
                            textbutton _("Off") action SetField(persistent, 'lively_bg', False)
            vbox:
                spacing 20
                use text_tooltip(_lssb_ui_resize(_("Gameplay Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Tutorial"), 230, 30), _("Enable/Disable the tutorial at the start of a new game"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'skip_tutorial', False)
                        textbutton _("Skip") action SetField(persistent, 'skip_tutorial', True)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Difficulty"), 230, 30), _("Change the game difficulty"), "lspref_label_text")
                        textbutton _("Easy") action SetField(persistent, 'difficulty', -1)
                        textbutton _("Normal") action SetField(persistent, 'difficulty', 0)
                        textbutton _("Difficult") action SetField(persistent, 'difficulty', 1)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Random Schedule"), 230, 30), _("Allow non-player characters to choose among several locations during this routine"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'schedule_randomness', True)
                        textbutton _("Off") action SetField(persistent, 'schedule_randomness', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Random Needs"), 225, 30), _("The need's cost can fluctuate when performing actions"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'needs_randomness', True)
                        textbutton _("Off") action SetField(persistent, 'needs_randomness', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Shuffle Choices"), 225, 30), _("Modify the order of the selections in nearly all of the menu choices"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'choices_shuffle', True)
                        textbutton _("Off") action SetField(persistent, 'choices_shuffle', False)

                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Notifications pop-up"), 230, 30), _("Enable/Disable the notification pop-up"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'notifications', True)
                        textbutton _("Hide") action SetField(persistent, 'notifications', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Close-up pop-ups"), 230, 30), _("Show/Hide the close-up inserts during sex scenes"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'hide_sex_inserts', False)
                        textbutton _("Hide") action SetField(persistent, 'hide_sex_inserts', True)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Pregnancy duration"), 230, 30), _("Change the pregnancy duration to suit your preference"), "lspref_label_text")
                        textbutton _("Endless") action SetField(persistent, 'pregnancy_end', False)
                        textbutton _("Immersive") action SetField(persistent, 'pregnancy_end', True)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Pregnancy pop-up"), 230, 30), _("Enable/Disable pregnancy pop-up"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'pregnancy_notification', True)
                        textbutton _("Hide") action SetField(persistent, 'pregnancy_notification', False)
                    if persistent.start_plus:
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(_lssb_ui_resize(_("Reset NG+"), 230, 30), _("Clear NG+ saved statistics"), "lspref_label_text")
                            textbutton _("Clear stats") action Confirm("You're going to clear NG+ statistics.", Function(game.clear_new_game_plus))
                    if Achievement.total_unlocked:
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(_lssb_ui_resize(_("Reset Achievements"), 230, 30), _("Clear all unlocked achievements"), "lspref_label_text")
                            textbutton _("Clear achievements") action Confirm("You're going to clear achievements.", Function(Achievement.reset))
                    if check_controller():
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(_lssb_ui_resize(_("Frame Selector"), 230, 30), _("Allow to see selection with a framed border"), "lspref_label_text")
                            textbutton _("On") action SetField(persistent, 'selector', True)
                            textbutton _("Off") action SetField(persistent, 'selector', False)
            vbox:
                spacing 20
                use text_tooltip(_lssb_ui_resize(_("Dialogue Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Text Speed"), 343, 30), _("Controls the rate at which text displays.\nThe further to the right this slider is, the faster the text will display.\nAll the way to the right causes text to be shown instantly."), "lspref_label_text")
                        bar value Preference("text speed")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Auto forward Time"), 343, 30), _("Controls automatic advance.\nThe further to the left this slider is, the shorter the amount of time before the game advances.\nAll the way to the right means text will never auto-forward."), "lspref_label_text")
                        bar value Preference("auto-forward time")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Rollback Side"), 230, 30), _("Enable a side of the screen to causes rollback"), "lspref_label_text")
                        textbutton _("Disable") action Preference("rollback side", "disable")
                        textbutton _("Left") action Preference("rollback side", "left")
                        textbutton _("Right") action Preference("rollback side", "right")
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Skip"), 230, 30), _("Allow the game to skipping parts, like texts or transitions"), "lspref_label_text")
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")
                        textbutton _("Transitions") action Preference("transitions", "toggle")
            vbox:
                spacing 20
                use text_tooltip(_lssb_ui_resize(_("Audio Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Music Volume"), 343, 30), _("Controls the volume of the music.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("music volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Sound Volume"), 343, 30), _("Controls the volume of the sounds.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("sound volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Voice Volume"), 343, 30), _("Controls the volume of the voices.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("voice volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Ambience Volume"), 343, 30), _("Controls the volume of the sound ambience.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("ambience volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Sex Sounds Volume"), 343, 30), _("Controls the volume of the sex sounds.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("sexsfx volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(_lssb_ui_resize(_("Moans Volume"), 343, 30), _("Controls the volume of the moans.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("moans volume")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Mute audio"), 230, 30), _("Enable/Disable game audio"), "lspref_label_text")
                        textbutton _("Mute all") action Preference("all mute", "toggle") alt f"Mute all is {'On' if persistent.mute_characters else 'Off'}."
                        textbutton _("Mute alarm clock") selected persistent.mute_alarm_clock action ToggleField(persistent, 'mute_alarm_clock', True, False) alt f"Alarm clock sound is {'On' if not persistent.mute_alarm_clock else 'Off'}."
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Mute voice"), 230, 30), _("Enable/Disable character voice"), "lspref_label_text")
                        textbutton _("Mute Bree") action [ToggleVoiceMute("bree")] alt f"Mute Bree is {'On' if 'bree' in persistent._voice_mute else 'Off'}."
                        textbutton _("Mute Mike") action [ToggleVoiceMute("mike")] alt f"Mute Mike is {'On' if 'mike' in persistent._voice_mute else 'Off'}."
                        textbutton _("Mute all characters") selected persistent.mute_characters action Function(toggle_mute_all_characters) alt f"Mute all characters is {'On' if persistent.mute_characters else 'Off'}."
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_lssb_ui_resize(_("Self-voicing"), 230, 30), _("Self-voicing setting"), "lspref_label_text")
                        textbutton _("Override voice") selected persistent.tts_override action Function(toggle_tts_override_voice_channel) alt f"Self-voicing override voice is {'On' if persistent.tts_override else 'Off'}."
        vbar:
            value YScrollValue("prefs")
            left_bar "gui/inv/vertical_idle_bar.png"
            right_bar "gui/inv/vertical_idle_bar.png"
            thumb "gui/inv/vertical_idle_thumb.png"
            thumb_offset 63
            left_gutter 63
            right_gutter 63
            maximum 11,359
            xpos 1100
            yalign 0.5
    button style "return_arrow_button" action [Hide("preferences"),Return()] tooltip "" default_focus check_controller()

    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            style_prefix "tooltips"

            has frame
            yanchor 0
            xalign 0.5
            xpadding 20
            text _lssb_ui_translate(tooltip) substitute False yalign 0.05

