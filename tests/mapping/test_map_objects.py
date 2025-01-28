from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class MapObjects(BaseTestCase):

    @py_xml_wrapper
    def test_6350(self):
        self.description({"description": "Map Object - Map route - Show and Hide",
                          "edition": ["IOSSupported", "NotRunInIOS", "NotRunInAndroid"],
                          "platform": "mapFragment - online - normal.day - Globe"})

        self.open_screen("Mapping")
        self.set_carto_poi("Off")
        self.set_center_default_null(value1=52.500556, value2=13.398889, value3="NONE")
        self.set_center_default_null(value4=10)

        self.diff_vertex("x5,y5", "x2,y2")

        self.show_hide_status(value1="Show_At", value2=18)
        self.set_center_multiple({0: "#1 set the showHideStatus as Show_At at range of 18, set the zoom level to 0",
                                  2: "#2 set the zoom level to 2",
                                  5: "#3 set the zoom level to 5",
                                  10: "#4 set the zoom level to 10",
                                  18: "#5 set the zoom level to 18",
                                  20: "#6 set the zoom level to 20"})

        self.show_hide_status(value1="Always_Show")
        self.show_hide_status(value1="Hide_At", value2=18)
        self.set_center_multiple({0: "#7 set the ShowHideStatus as Always_Show, and setShowHideStatus as "
                                     "Hide_At at 18; set the zoom level to 0",
                                  2: "#8 set the zoom level to 2",
                                  5: "#9 set the zoom level to 5",
                                  10: "#10 set the zoom level to 10",
                                  18: "#11 set the zoom level to 18",
                                  20: "#12 set the zoom level to 20"})

        self.show_hide_status(value1="Always_Show")
        self.show_hide_status(value1="Hide_At_Range", value2=15, value3=17)
        self.set_center_multiple({0: "#13 set ShowHideStatus as Always_Show, Hide_At_Range from the range 15 to 17, "
                                     "and set the zoom level to 0",
                                  2: "#14 set the zoom level to 2",
                                  5: "#15 set the zoom level to 5",
                                  15: "#16 set the zoom level to 15",
                                  17: "#17 set the zoom level to 17",
                                  20: "#18 set the zoom level to 20"})

        self.show_hide_status(value1="Always_Hide")
        self.show_hide_status(value1="Show_At_Range", value2=15, value3=17)
        self.set_center_multiple({0: "#19 set ShowHideStatus as Always_Hide, and set the Show_At_Range from 15 to 17; "
                                     "set the zoom level to 0",
                                  2: "#20 set the zoom level to 2",
                                  5: "#21 set the zoom level to 5",
                                  15: "#22 set the zoom level to 15",
                                  17: "#23 set the zoom level to 17",
                                  18: "#24 set the zoom level to 18",
                                  20: "#25 set the zoom level to 20",
                                  10: "#26 set the zoom level to 10"})

        self.diff_vertex("x2,y5", "x5,y2")

    def set_center_multiple(self, centers):
        for k, v in centers.items():
            self.set_center_default_null(value4=k)
            self.capture_screen(index=v)

    def diff_vertex(self, value1, value2):
        self.add_map_object("MapRoute", "no")
        self.add_vertex("MapRoute", value1=value1, value2=value2)
        self.wait(10000)
        self.capture_screen()

    @py_xml_wrapper
    def test_6754(self):
        self.description({"description": "Map Object - Map Markers - Empty Constructor - "
                                         "Transparency - Anchor point - Screen Coord",
                          "edition": "PremiumSDK",
                          "platform": ["mapFragment - online - normal.day - Mercator",
                                       "mapFragment - online - normal.day - Globe"]})

        self.open_screen("Mapping")
        self.add_map_object("Marker", "yes")

        self.perform_map_gestures()

        self.anchor_pt({None: "Anchor Point: (empty) Returns Error", -5: "Anchor Point: (-5, -5)",
                        0: "Anchor Point: (0, 0)", 30: "Anchor Point: (30, 30)", 100: "Anchor Point: (100, 100)",
                        300: "Anchor Point: (300, 300)", 800: "Anchor Point: (800, 800)"})

        self.set_center_default_null(value4=0)
        self.capture_screen(index="Anchor Point: (800, 800)")

        self.anchor_pt({0: "Anchor Point: (0, 0)"})

        self.set_geo_position()
        self.capture_screen(index="GeoCoord: (empty) gives error")

        self.geo_pos(434.3434, -123.13)
        self.geo_pos(49.324, -989.23)
        self.geo_pos(434.343, -988.23)

        self.set_center_by_place_name("BERLIN", 15, 0)
        self.add_map_object("Marker", "yes")

        self.perform_map_gestures()

        self.modify_img_type("newImage")
        self.capture_screen(index="Marker image set to car")

        self.orientation("landscape")
        self.orientation("portrait")

        self.push_active_app_to_bg()
        self.capture_screen(index="Background")

        self.bring_app_to_foreground("Functional Test App V2")
        self.capture_screen(index="Foreground")

        self.remove_all_map_objs()

    def transparency(self, values):
        for k, v in values.items():
            self.set_transparency(k)
            self.capture_screen(index=v)

    def anchor_pt(self, values):
        for k, v in values.items():
            self.set_anchor_pt(k, k)
            self.capture_screen(index=v) if k is None else self.press_back_and_capture(v)

    def geo_pos(self, v1, v2):
        self.set_geo_position(v1, v2)
        self.press_back_and_capture("GeoCoord: ({},{})".format(v1, v2))

    def perform_map_gestures(self):
        self.set_geo_position()
        self.capture_screen(index="GeoCoord error message")

        self.press_back()

        self.long_press("x0,y1")
        self.long_press("x0,y1")
        self.set_draggable("Off")
        self.capture_screen(index="Map Marker Displayed")

        self.pan("x1,y0", "x2,y0", index="Pan left")
        self.pan("x2,y0", "x1,y0")
        self.double_tap_zoom_in("x0,y0", "Zoom in")
        self.two_finger_tap_zoom_out("x1,y0", "x3,y0", "Zoom out")
        self.transparency({-5: "Transparency error", 0: "Transparency: 0, not visible",
                           0.5: "Transparency: 0.5, half shown", 1: "Transparency: 1, fully shown"})

    def orientation(self, mode):
        self.set_orientation(mode)
        self.set_center_by_place_name("BERLIN", 15, 0)
        self.capture_screen(index=mode)

    @py_xml_wrapper
    def test_6757(self):
        self.description({"description": "Map Object - Map 3D marker- Z-index",
                          "edition": "PremiumSDK"})

        self.open_screen("Mapping")
        self.open_objects_from_menu()
        self.set_carto_poi("Off")

        self.set_center_default_null(value1=52.500556, value2=13.398889, value3="NONE")
        self.set_center_default_null(value4=15)

        self.perform_steps_for_6757("52.4993, 13.3994", False)
        self.perform_steps_for_6757("52.4985, 13.3977")

        self.modify_obj_and_set_z_index("Map3dMarker 1", 5000)
        self.modify_obj_and_set_z_index("Map3dMarker 2", 10000)

    def modify_obj_and_set_z_index(self, obj, index_value):
        self.modify_map_obj(obj)
        self.set_z_index("MapObject", index_value)
        self.capture_screen()

    def perform_steps_for_6757(self, lat_long, create_img=True):
        self.add_map_object("Map3dMarker", "no")
        self.create_center(lat_long)
        if create_img:
            self.create_img("red_yellow")
        self.create_click_go()
        self.wait_and_capture()

    @py_xml_wrapper
    def test_6758(self):
        self.description({"description": "Map Object - Map 3D Markers - By object path - Pitch - Roll - Scale - Yaw - "
                                         "Anchor point - Dynamic Scale - different map scheme - "
                                         "map projection - landscape",
                          "edition": "PremiumSDK",
                          "platform": "mapFragment - online - normal.day - Globe",
                          "priority": "HighPriority"})

        self.open_screen("Mapping")
        self.open_objects_from_menu()
        self.wait(5000)
        self.set_carto_poi("Off")

        self.set_center_by_place_name_with_null_default("VANCOUVER")
        self.set_center_default_null(value4=15)

        self.add_map_object("Map3dMarker", "no")

        self.create_center()
        self.create_click_go()
        self.single_tap("x2,y2", "#1 open map objects; turn off all CartoPOI; set zoom level to 15;"
                                 "add map3dMarker thus mapObject is not empty; click go to create mapObject; "
                                 "single tap the map")

        self.create_center("49.2908, -123.1246")
        self.create_click_go()
        self.capture_screen(index="#2 set center as 49.2908, -123.1246 in map3dMarker, and click go")
        self.pan("x0,y0", "x2,y2", index="#3 pan the map from x0,y0 to x2, y2")

        self.set_center_default_null(value4=12)
        self.capture_screen(index="#4 set the zoom level to 12")
        self.set_center_default_null(value4=15)
        self.capture_screen(index="#5 set the zoom level to 15")

        self.mod(self.modify_pitch, {None: "#6 leave the pitch number as empty; click set button"})

        self.single_tap("x2,y2", "Single tap")
        self.modify_anchor_pt("49.291, -123.1238")
        self.modify_click_btns("Set")

        self.mod(self.modify_pitch, {0: "#7 single tap on x2,y2; modify the Anchor point to 49.291, -123.1238;"
                                        "click the set button; modify the pitch number to 0, "
                                        "and click the set button",
                                     10: "#8 modify pitch number to 10, and click the set button",
                                     50: "#9 set the pitch number to 50 and click the set button",
                                     180: "#10 set the pitch number to 180, and click the set button",
                                     360: "#11 modify the pitch number to 360, and click the set button",
                                     98765432: "#12 modify the pitch number to 98765432, and click the set button"})

        self.mod(self.modify_pitch, {0: None})

        self.mod(self.modify_roll, {None: "#13 modify the pitch number to 0; and click the set button; "
                                          "leave modify the roll as empty and click the set button"})

        self.single_tap("x2,y2", "Single tap")
        self.mod(self.modify_roll, {0: "#14 single tap on x2,y2; modify the roll number as 0 and click the set button",
                                    10: "#15 modify the roll number to 10, and click the set button",
                                    50: "#16 modify the roll number to 50, and click the set button",
                                    180: "#17 modify the roll number to 180, and click the set button",
                                    360: "#18 modify the roll number to 360, and click the set button",
                                    98765432: "#19 modify the roll number to 98765432, and click the set button"})
        self.mod(self.modify_roll, {0: None})

        self.mod(self.modify_scale, {None: "#20 modify the roll number to 0, and click the set button; "
                                           "keep the scale value as empty, and click the set button"})

        self.single_tap("x2,y2", "Single tap")
        self.mod(self.modify_scale, {0: "#21 single tap at x2,y2, modify the scale value to 0, and click the set button",
                                     0.02: "#22 modify the scale to 0.02 and click the set button",
                                     0.09: "#23 modify the scale to 0.09 and click the set button",
                                     0.1: "#24 modify the scale tp 0.1, and click the set button",
                                     0.2: "#25 modify the scale to 0.2 and click the set button",
                                     0.3: "#26 modify the scale to 0.3 and click the set button",
                                     1: "#27 modify the scale to 1 and click the set button",
                                     0.01: None})
        self.mod(self.modify_yaw, {None: "#28 set the scale value to 0.01, click the set button; "
                                         "leave the Yaw value as empty and click the set button"})

        self.single_tap("x2,y2", "Single tap")
        self.mod(self.modify_yaw, {0: "#29 single tap on x2,y2, modify the Yaw value to 0 annd click the set button",
                                   10: "#30 modify the Yaw value to 10 and click the set button",
                                   100: "#31 modify the Yaw value to 100 and click the set button",
                                   1000: "#32 modify the Yaw value to 1000 and click the set button",
                                   98765432: "#33 modify the Yaw value to 98765432 and click the set button",
                                   0: ""})
        self.mod(self.modify_yaw, {0: None})

        self.mod(self.modify_anchor_pt, {None: "#34 modify the Yaw value to 0 and click the set button; "
                                               "leave Anchor Point value as empty, and click the set button"})

        self.single_tap("x2,y2", "Single tap")
        self.mod(self.modify_anchor_pt, {"434.3434,-123.13": "#35 single tap at x2,y2, modify the Anchor Point to "
                                                             "434.3434,-123.13 and click set button",
                                         "49.324,-989.23": "#36 modify the Anchor point to 49.324,-989.23 "
                                                           "and click set button",
                                         "434.343,-988.23": "#37 modify the Anchor point to 434.343,-988.23 "
                                                            "and click set button",
                                         "49.2672,-123.1047": None})
        self.mod(self.modify_enable_dynamic_scale, {"Off": "#38 modify the Anchor point to 49.2672,-123.1047 and "
                                                           "click set button; turn off the modifyEnableDynamicScale, "
                                                           "and click the set button",
                                                    "On": None})
        self.mod(self.modify_img, {"red_yellow": "#39 turn on the modifyEnableDynamicScale and click the set button;"
                                                 "modify the image to red_yellow, and click the set button",
                                   "mix": "#40 modify the image to mix and click the set button",
                                   "Default": "#41 modify the image to Default and click the set button"})

        self.push_active_app_to_bg("Functional Test App V2")
        self.bring_app_to_foreground("Functional Test App V2")
        self.capture_screen(index="#42 send the FTA to background and bring it forward again")

        self.remove_all_map_objs()

    def mod(self, func, values):
        for k, v in values.items():
            func(k)
            self.modify_click_btns("Set")
            self.capture_screen(index=v)

    @py_xml_wrapper
    def test_6759(self):
        self.description({"description": "Map Object - Map 3D Marker - Overlay type",
                          "edition": "PremiumSDK",
                          "platform": "mapFragment - online - normal.day - Globe",
                          "priority": "HighPriority"})

        self.open_screen("Mapping")
        self.open_objects_from_menu()

        self.set_center(49.2833, -123.1177, 16)
        self.add_map_object("Map3dMarker", "no")
        self.create_center("49.2831, -123.1191")
        self.create_click_go()
        self.capture_screen()

        overlay_type = ["POI_Overlay", "Transit_Stop_Overlay", "Road_Overlay", "Area_Overlay",
                        "Background_Overlay", "Background_Replacement", "ForeGround_Overlay"]

        for overlay in overlay_type:
            self.set_overlay(overlay)

        self.remove_all_map_objs()

    @py_xml_wrapper
    def test_6760(self):
        self.description({"description": "Map Object - Map 3D Marker- Show and Hide",
                          "edition": "PremiumSDK",
                          "platform": "mapFragment - online - normal.day - Globe"})

        self.open_screen("Mapping")
        self.open_objects_from_menu()
        self.set_carto_poi("Off")

        self.set_center_default_null(value1=52.500556, value2=-13.398889, value3="NONE")
        self.set_center_default_null(value4=16)
        self.add_map_object("Map3dMarker", "no")
        self.create_center("52.4993, 13.3994")
        self.create_click_go()
        self.capture_screen(index="#1 open map object, turn off all the CartoPOI; "
                                  "set the center to 52.500566,13.398889, set the animation to NONE; "
                                  "set the zoom level tp 16; add a Map3dMarker and set the center 52.4993,13.3994, "
                                  "click go button")

        self.show_hide_status(value1="Always_Show")
        self.set_center_multiple({0: "#2 set the showHiddenStatus as Always_Show, set the zoom level to 0",
                                  2: "#3 set the zoom level to 2",
                                  5: "#4 set the zoom level to 5",
                                  10: "#5 set the zoom level to 10",
                                  18: "#6 set the zoom level to 18",
                                  20: "#7 set the zoom level to 20"})

        self.show_hide_status(value1="Always_Hide")
        self.set_center_multiple({0: "#8 set showHiddenStatus as Always_Hide and set the zoom level to 0",
                                  2: "#9 set the zoom level to 2",
                                  5: "#10 set the zoom level to 5",
                                  10: "#11 set the zoom level to 10",
                                  18: "#12 set the zoom level to 18",
                                  20: "#13 set the zoom level to 20"})

        self.show_hide_status(value1="Always_Hide")
        self.show_hide_status(value1="Show_At", value2=18)
        self.set_center_multiple({0: "#14 set the showHideStatus as Always_Hide, set the showHideStatus "
                                     "as Show_At at range of 18, set the zoom level to 0",
                                  2: "#15 set the zoom level to 2",
                                  5: "#16 set the zoom level to 5",
                                  10: "#17 set the zoom level to 10",
                                  18: "#18 set the zoom level to 18",
                                  20: "#19 set the zoom level to 20"})

        self.show_hide_status(value1="Always_Show")
        self.show_hide_status(value1="Hide_At", value2=18)
        self.set_center_multiple({0: "#20 set the ShowHideStatus as Always_Show, and setShowHideStatus as "
                                     "Hide_At at 18; set the zoom level to 0",
                                  2: "#21 set the zoom level to 2",
                                  5: "#22 set the zoom level to 5",
                                  10: "#23 set the zoom level to 10",
                                  18: "#24 set the zoom level to 18",
                                  20: "#25 set the zoom level to 20"})

        self.show_hide_status(value1="Always_Show")
        self.show_hide_status(value1="Hide_At_Range", value2=15, value3=17)
        self.set_center_multiple({0: "#26 set ShowHideStatus as Always_Show, Hide_At_Range from the range 17 to 19, "
                                     "and set the zoom level to 0",
                                  2: "#27 set the zoom level to 2",
                                  5: "#28 set the zoom level to 5",
                                  15: "#29 set the zoom level to 15",
                                  17: "#30 set the zoom level to 17",
                                  18: "#31 set the zoom level to 18",
                                  20: "#32 set the zoom level to 20"})

        self.show_hide_status(value1="Always_Hide")
        self.show_hide_status(value1="Show_At_Range", value2=15, value3=17)
        self.set_center_multiple({0: "#33 set ShowHideStatus as Always_Hide, and set the Show_At_Range from 15 to 17; "
                                     "set the zoom level to 0",
                                  2: "#34 set the zoom level to 2",
                                  5: "#35 set the zoom level to 5",
                                  15: "#36 set the zoom level to 15",
                                  17: "#37 set the zoom level to 17",
                                  18: "#38 set the zoom level to 18",
                                  20: "#39 set the zoom level to 20"})

    @py_xml_wrapper
    def test_6847(self):
        self.description({"description": "Map Object - Map 3D Marker - Construct model by Vertex - "
                                         "By Object path - Different images - Delete",
                          "edition": "PremiumSDK",
                          "platform": ["mapFragment - online - satellite.day - Globe",
                                       "mapView - offline - normal.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapView - online - normal.day - Globe",
                                       "mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - normal.night - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapFragment - offline - normal.day - Globe",
                                       "mapFragment - offline - carnav.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapFragment - online - normal.day - Globe - Landscape"],
                          "priority": "HighPriority"})

        self.open_screen("Mapping")
        self.set_carto_poi("Off")

        self.set_center_by_place_name_with_null_default("VANCOUVER")
        self.set_center_default_null(value4=15)
        self.add_map_object("Map3dMarker", "no")
        self.create_construct_model("Construct Model by Vertex")
        self.create_click_go()
        self.wait_and_capture(index="#1: CartoPOI OFF, Vancouver Zoom 15, Map3dMarker by Vertex")

        self.perform_steps_to_create_center_and_img("49.2908, -123.1246", "red_yellow",
                                                    "#2: Add Map3dMarker red_yellow 49.2908, -123.1246")
        self.set_center_default_null(value6=82)
        self.capture_screen(index="#3: Tilt 82")

        self.pan("x0,y0", "x2,y2", index="#4: Pan x0,y0 to x2,y2")
        self.set_center_default_null(value4=12)
        self.capture_screen(index="#5: Zoom 12")

        self.set_center_default_null(value4=15)
        self.capture_screen(index="#6: Zoom 15")

        self.set_center_by_place_name("VANCOUVER", 10, 0)
        self.perform_steps_to_create_center_and_img("49.2123, -123.1253", "Mix", "#7: Vancouver Zoom 10, "
                                                                                 "add Map3dMarker Mix 49.2123, -123.125")

        self.set_center_and_img_with_specific_zoom(11, "49.2432, -123.0852", "Default", "#8: Zoom 11, add Map3dMarker Default 49.2432, -123.0852")
        self.set_center_and_img_with_specific_zoom(12, "49.2542, -123.0987", "red_yellow", "#9: Zoom 12, Add Map3dMarker red_yellow 49.2542, -123.0987")
        self.set_center_and_img_with_specific_zoom(13, "49.2743, -123.1154", "Mix", "#10: Zoom 13, Add Map3dMarker Mix 49.2743, -123.1154")
        self.set_center_and_img_with_specific_zoom(14, "49.2764, -123.1156", "Default", "#11: Zoom 14, Add Map3dMarker Default 49.2764, -123.1156")
        self.set_center_and_img_with_specific_zoom(15, "49.28, -123.1163", "red_yellow", "#12: Zoom 15, Add Map3dMarker red_yellow 49.28, -123.1163")
        self.set_center_and_img_with_specific_zoom(16, "49.2796, -123.1157", "Mix", "#13: Zoom 16, Add Map3dMarker Mix 49.2796, -123.1157")
        self.set_center_and_img_with_specific_zoom(18, "49.2798, -123.1162", "Default", "#14: Zoom 18, Add Map3dMarker Default 49.2798, -123.1162")
        self.set_center_and_img_with_specific_zoom(20, "49.2799, -123.1162", "Mix", "#15: Zoom 18, Add Map3dMarker Mix 49.2799, -123.1162")

        self.set_center_default_null(value6=82)
        self.set_center_default_null(value4=15)
        self.capture_screen(index="#16: Zoom 15, Tilt 82")

        self.street_lvl_coverage("On")
        self.wait(30000)

        self.perform_steps_to_create_center_and_img("49.2796, -123.1152", "Default", "#17: StreetLevelCoverage ON, "
                                                                                     "Add Map3dMarker "
                                                                                     "Default 49.2796, -123.1152")

        self.push_active_app_to_bg("Functional Test App V2")
        self.bring_app_to_foreground("Functional Test App V2")
        self.capture_screen(index="#18: Bring FTAv2 to foreground")

        self.remove_all_map_objs()

    def perform_steps_to_create_center_and_img(self, lat_long, img_type, index=None):
        self.add_map_object("Map3dMarker", "no")
        self.create_center(lat_long)
        self.create_img(img_type)
        self.create_click_go()
        self.capture_screen(index=index)

    def set_center_and_img_with_specific_zoom(self, zoom, lat_long, img_type, index=None):
        self.set_center_default_null(value4=zoom)
        self.perform_steps_to_create_center_and_img(lat_long, img_type, index)
