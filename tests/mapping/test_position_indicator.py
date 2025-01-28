from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class PositionIndicator(BaseTestCase):

    @py_xml_wrapper
    def test_6911(self):
        self.description({"description": "NMA - SDK 3.3.1 or newer - PositionIndicator - Z-index",
                          "edition": "PremiumSDK",
                          "platform": "mapFragment - online - normal.day - Globe"})

        self.set_service_status("location", "On")
        self.open_mapping_with_current_center()
        self.set_center_with_zoom_lvl(18)

        self.add_vertex_and_radius()
        self.capture_screen()

        self.set_z_index("MapCircle", 51)
        self.capture_screen()

        self.turn_on_accuracy_visibility("On", "On")

        for _ in [52, 5000, -1]:
            self.set_z_index("PositionIndicator", _)
            self.capture_screen()

        self.set_service_status("location", "Off")

    @py_xml_wrapper
    def test_7172(self):
        self.description({"description": "Verify Position Indicator shows up if the location service is enabled",
                          "edition": ["StarterSDK", "PremiumSDK", "IOSSupported"],
                          "platform": "mapFragment - online - normal.day - Globe",
                          "priority": "HighPriority"})

        self.set_service_status("location", "On")
        self.open_mapping_with_current_center()

        self.set_center_with_zoom_lvl(19, "#1 set GPSLocationService; open Mapping; turn off all CartoPOI; "
                                          "set CenterByPlaceName as current and animation as NONE; set zoom level to 19")
        self.set_indicator_img("NO_CHANGE")
        self.toggle_visibility("Off")
        self.capture_screen(index="#2 set PositionIndicatorImage as NO_CHANGE; "
                                  "turn off toggleVisibility under PositionIndicator")

        self.turn_on_accuracy_visibility("On", "On", "#3 set IndicatorImage aas NO_CHANGE under positionIndicator; "
                                                     "turn on toggleAccuracy under PositionIndicator")

        self.turn_on_service_kill_app_open_mapping_with_current_center("airplain_mode")
        self.capture_screen(index="#4 change to airplane mode; force stop FTA; open Mapping; turn off all CartoPOI; "
                                  "set CenterByPlaceName as current and animation as NONE")
        self.turn_on_service_kill_app_open_mapping_with_current_center("wifi")
        self.capture_screen(index="#5 turn on wifi; force stop FTA; open Mapping; turn off all CartoPOI; "
                                  "set CenterByPlaceName as current and animation to NONE")

        self.set_service_status("airplain_mode", "Off")
        self.set_service_status("location", "Off")

    @py_xml_wrapper
    def test_7173(self):
        self.description({"description": "Verify Position Indicator with different Accuracy Indicator "
                                         "Visible with Battery saving and GPS only",
                          "edition": ["StarterSDK", "PremiumSDK", "IOSSupported"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapView - online - normal.day - Globe"],
                          "priority": "HighPriority"})

        self.set_service_status("location", "On")
        self.open_mapping_with_current_center()

        self.set_center_with_zoom_lvl(13, "#1 setGPS Battery saving, Current location, Zoom 13")

        self.turn_on_accuracy_visibility("On", "On", "#2 PositionIndicator toggleAccuracy ON, toggleAccuracy ON")

        self.toggle_accuracy("Off")
        self.capture_screen(index="#3 toggleAccuracy OFF")

        self.toggle_accuracy("On")
        self.capture_screen(index="#4 toggleAccuracy ON")

        self.set_service_status("airplain_mode", "On")
        self.force_stop_app("com.here.functionaltestv2")
        self.set_service_status("location", "Off")
        self.set_service_status("location", "On")

        self.open_screen("Mapping")
        self.set_center_with_zoom_lvl(19, "#5 AirplaneMode ON, Force stop then reopen FTA, Current location, Zoom 19")

        self.turn_on_service_kill_app_open_mapping_with_current_center("wifi")
        self.set_center_with_zoom_lvl(19, "#6 Wifi ON, Force stop then reopen FTA, Current location, Zoom 19")

        self.set_service_status("airplain_mode", "Off")
        self.set_service_status("location", "Off")

    @py_xml_wrapper
    def test_7174(self):
        self.description({"description": "PositionIndicator - location service is disabled - "
                                         "position indicator does not show up",
                          "edition": ["StarterSDK", "PremiumSDK", "IOSSupported"],
                          "platform": "mapFragment - online - normal.day - Globe"})

        self.set_service_status("location", "Off")
        self.open_mapping_with_current_center()
        self.turn_on_accuracy_visibility("On", "On", "PositionIndicator toggleAccuracy ON, toggleAccuracy ON")

    @py_xml_wrapper
    def test_7175(self):
        self.description({"description": "location service is enabled - GPS and Wifi mobile network location turn on - "
                                         "position indicator shows up",
                          "edition": ["StarterSDK", "PremiumSDK", "IOSSupported"],
                          "platform": "mapFragment - online - normal.day - Globe",
                          "priority": "LKWPriority"})

        self.set_service_status("location", "On")
        self.open_mapping_with_current_center()
        self.capture_screen(index="#1 set GPSLocationService to high accuracy; open Mapping; turn off all CartoPOI; "
                                  "set the CenterByPlaceName as current and animation as NONE")
        self.turn_on_accuracy_visibility("On", "Off", "#2 setIndicatorImage as NO_CHANGE; for PositionIndicator, "
                                                      "turn on toggleAccuracy and turn off toggleVisiblity")

        self.toggle_visibility("On")
        self.capture_screen(index="#3 turn on toggleVisibility")

        self.turn_on_service_kill_app_open_mapping_with_current_center("airplain_mode")
        self.set_center_with_zoom_lvl(19, "#4 set to fight mode; force stop FTA; open Mapping, turn off all CartoPOI; "
                                          "set CenterPlaceByName as current and animation as NONE; "
                                          "set zoom level to 19.0")

        self.turn_on_service_kill_app_open_mapping_with_current_center("wifi")
        self.set_center_with_zoom_lvl(19, "#5 turn on wifi; force stop FTA; open Mapping, turn off all CartoPOI; "
                                          "set CenterByPlaceName as current, animation as NONE; "
                                          "set zoom level to 19.0")

        self.set_service_status("airplain_mode", "Off")
        self.set_service_status("location", "Off")

    @py_xml_wrapper
    def test_7176(self):
        self.description({"description": "NMA - SDK 3.1 or newer - PositionIndicator - Z index",
                          "edition": ["StarterSDK", "PremiumSDK", "IOSSupported"],
                          "platform": "mapFragment - online - normal.day - Globe"})

        self.set_service_status("location", "On")
        self.open_mapping_with_current_center(open_map_obj_screen=True)
        self.set_center_with_zoom_lvl(18)

        self.add_vertex_and_radius()
        self.set_z_index("MapCircle", 49)
        self.capture_screen()

        self.turn_on_accuracy_visibility("On", "On")
        self.set_center_by_place_name_with_null_default("Current", "LINEAR")
        self.set_center_with_zoom_lvl(16)

        self.set_center_and_zoom_lvl_multiple([14, 12, 8])
        self.remove_all_map_objs()

        self.set_center_by_place_name_with_null_default("Current")
        self.set_center_with_zoom_lvl(18)

        self.add_vertex_and_radius()
        self.set_alpha(100)
        self.set_z_index("MapCircle", 500)
        self.turn_on_accuracy_visibility("On", "On")

        self.set_z_index("PositionIndicator", 499)
        self.capture_screen()

        self.set_center_and_zoom_lvl_multiple([16, 14, 12, 8])

        self.set_service_status("location", "Off")

    @py_xml_wrapper
    def test_7380(self):
        self.description({"description": "NMA - SDK 3.1 or newer - PositionIndicator - Z index",
                          "edition": ["StarterSDK", "PremiumSDK", "NotRunInIOS"],
                          "platform": "mapFragment - online - normal.day - Globe"})

        self.set_service_status("location", "On")
        self.open_mapping_with_current_center()
        self.set_center_with_zoom_lvl(18)
        self.turn_on_accuracy_visibility("On", "On", "set GPS Location Service to high accuracy; open mapping, "
                                                     "turn off all setCartoPOI; set the zoom level to 18; "
                                                     "set IndicatorImage to NO_CHANGE; turn on toggleAccuracy")

        for _ in ["ALIEN", "BEETLE", "HERE"]:
            self.set_indicator_img(_)
            self.wait_and_capture(30000, "set the indicatorImage to {}".format(_))

        self.set_service_status("location", "Off")

    def set_center_and_zoom_lvl_multiple(self, zoom_lvls):
        for zoom_lvl in zoom_lvls:
            self.set_center_by_place_name_with_null_default("Current")
            self.set_center_with_zoom_lvl(zoom_lvl)

    def add_vertex_and_radius(self):
        self.add_map_object("Circle", "no")
        self.add_vertex("MapCircle", value1="x0,y0")
        self.set_radius(500)

    def open_mapping_with_current_center(self, open_map_obj_screen=False):
        self.open_screen("Mapping")
        if open_map_obj_screen:
            self.open_objects_from_menu()
        self.set_carto_poi("Off")
        self.set_center_by_place_name_with_null_default("Current")

    def turn_on_accuracy_visibility(self, accuracy, visibility, index=None):
        self.set_indicator_img("NO_CHANGE")
        self.toggle_accuracy(accuracy)
        self.toggle_visibility(visibility)
        self.capture_screen(index=index)

    def turn_on_service_kill_app_open_mapping_with_current_center(self, service):
        self.set_service_status(service, "On")
        self.force_stop_app("com.here.functionaltestv2")
        self.open_mapping_with_current_center()

    def set_center_with_zoom_lvl(self, zoom_lvl, index=None):
        self.set_center_default_null(value4=zoom_lvl)
        self.capture_screen(index=index)



























