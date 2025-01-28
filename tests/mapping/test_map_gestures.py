from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class MapGestures(BaseTestCase):

    @py_xml_wrapper
    def test_6724(self):
        self.description({"description": "gesture---FixMapCenterOnRotateZoom",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - satellite.day - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapFragment - offline - carnav.day - Globe",
                                       "mapFragment - online - satellite.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapView - online - normal.day - Globe",
                                       "mapView - offline - normal.day - Globe",
                                       "mapFragment - online - normal.night - Globe",
                                       "mapFragment - online - normal.day - Globe - Landscape",
                                       "mapFragment - offline - normal.day - Globe"]})

        self.open_mapping_and_set_center()

        self.update_gesture_settings("FixMapCenterOnRotateZoom", "ON", "ON", "#2 updateGestureSettings "
                                                                             "FixMapCenterOnRotateZoom ON")
        self.show_map_info("True")
        self.capture_screen(index="#3 showMapInfo True")
        self.pinch_close_zoom_out("x4,y4", "x4,y5", "#4 pinchCloseZoomOut: x4,y4, x4,y5")
        self.pinch_open_zoom_in("x0,y0", "x0,y1", "#5 pinchOpenZoomIn: x0,y0, x0,y1")

        self.set_center_default_null(value1=49.2824288, value2=-123.1178713, value3="NONE")
        self.set_center_default_null(value4=15)

        self.update_gesture_settings("FixMapCenterOnRotateZoom", "OFF", "ON", "#6 Vancouver Zoom 15, "
                                                                              "updateGestureSettings "
                                                                              "FixMapCenterOnRotateZoom OFF")
        self.show_map_info("True")
        self.capture_screen(index="#7 showMapInfo True")
        self.pinch_close_zoom_out("x4,y4", "x4,y5", "#8 pinchCloseZoomOut: x4,y4, x4,y5")
        self.pinch_open_zoom_in("x4,y4", "x4,y5", "#9 pinchOpenZoomIn: x4,y4, x4,y5")

    @py_xml_wrapper
    def test_6725(self):
        self.description({"description": "gesture---longPress",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - normal.night - Globe",
                                       "mapFragment - online - satellite.day - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - offline - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapFragment - offline - normal.day - Globe",
                                       "mapView - online - normal.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapView - offline - normal.day - Globe",
                                       "mapFragment - online - normal.day - Globe - Landscape"]})

        self.open_mapping_and_set_center()

        self.update_gesture_settings("All", "ON", "ON", "GestureSettings All On")
        self.long_press("x2,y2", "#2: longPress x2, y2")

        self.update_gesture_settings("longPress", "OFF", "ON", "#3: GestureSettings longPress OFF")
        self.long_press("x2,y2", "#4: longPress x2,y2")

        self.update_gesture_settings("longPress", "ON", "ON", "#5: GestureSettings longPress ON")
        self.long_press("x2,y2", "#6: longPress x2,y2")

    @py_xml_wrapper
    def test_7178(self):
        self.description({"description": "gesture---pinchCloseZoomOut-pinchOpenZoomIn",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - satellite.day - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapFragment - offline - carnav.day - Globe",
                                       "mapView - offline - normal.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapView - online - normal.day - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapFragment - online - normal.day - Globe - Landscape",
                                       "mapFragment - offline - normal.day - Globe",
                                       "mapFragment - online - normal.night - Globe"],
                          "priority": ["HighPriority", "LKWPriority"]})

        self.open_mapping_and_set_center()

        self.pinch_close_zoom_out("x4,y3", "x0,y0", "#2 pinchCloseZoomOut: x4,y3, x0,y0")
        self.show_map_info("True")

        self.pinch_open_zoom_in("x0,y0", "x3,y1", "#3 pinchOpenZoomIn: x0,y0, x3,y1")
        self.pinch_close_zoom_out("x4,y3", "x0,y0", "#4 pinchCloseZoomOut: x4,y3, x0,y0")
        self.pinch_open_zoom_in("x0,y0", "x3,y1", "#5 pinchOpenZoomIn: x0,y0, x3,y1")

        self.update_gesture_settings("pinchOpenZoomIn", "OFF", "ON", "#6 updateGestureSettings pinchOpenZoomIn Off")
        self.show_map_info("True")
        self.pinch_close_zoom_out("x4,y3", "x0,y0", "#7 pinchCloseZoomOut: x4,y3, x0,y0")
        self.pinch_open_zoom_in("x0,y0", "x3,y1", "#8 pinchOpenZoomIn: x0,y0, x3,y1")

        self.update_gesture_settings("pinchCloseZoomOut", "ON", "ON", "#9 updateGestureSettings pinchCloseZoomOut ON")
        self.show_map_info("True")
        self.pinch_close_zoom_out("x4,y3", "x0,y0", "#10 pinchCloseZoomOut: x4,y3, x0,y0")
        self.pinch_open_zoom_in("x0,y0", "x3,y1", "#11 pinchOpenZoomIn: x0,y0, x3,y1")

    @py_xml_wrapper
    def test_7179(self):
        self.description({"description": "gesture---double Tap to zoom in",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.night - Globe",
                                       "mapFragment - online - satellite.day - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapFragment - online - normal.day - Globe - Landscape",
                                       "mapFragment - offline - normal.day - Globe",
                                       "mapFragment - offline - carnav.day - Globe",
                                       "mapView - offline - normal.day - Globe",
                                       "mapView - online - normal.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapFragment - online - hybrid.day - Globe"]})

        self.open_mapping_and_set_center()

        self.double_tap_zoom_in("x2,y2", "#2 doubleTapZoomIn: x2,y2")
        self.show_map_info("True")

        self.update_gesture_settings("doubleTapZoomIn", "OFF", "ON", "#3 GestureSettings doubleTapZoomIn OFF")
        self.show_map_info("True")
        self.double_tap_zoom_in("x2,y2", "#4 doubleTapZoomIn: x2,y2 (should do no effect)")

        self.update_gesture_settings("doubleTapZoomIn", "ON", "ON", "#5 GestureSettings doubleTapZoomIn ON")
        self.show_map_info("True")
        self.double_tap_zoom_in("x2,y2", "#6 doubleTapZoomIn: x2,y2")

    @py_xml_wrapper
    def test_7180(self):
        self.description({"description": "gesture---twoFingerTilt",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - satellite.day - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapFragment - offline - carnav.day - Globe"]})

        self.open_screen("Mapping")
        self.set_carto_poi("Off")
        self.wait(5000)

        self.set_center_by_place_name("VANCOUVER", 15, 5000, "#1 CartoPOI all off, Vancouver Zoom 15")

        self.two_finger_tilt("x2,y2", "x0,y1", "#2 twoFingerTilt: x2,y2, x0,y1")
        self.show_map_info("True")

        self.update_gesture_settings("twoFingerTilt", "OFF", "ON", "#3 updateGestureSettings twoFingerTilt OFF")
        self.show_map_info("True")
        self.two_finger_tilt("x1,y2", "x1,y1", "#4 twoFingerTilt: x1,y2, x1,y1")

        self.update_gesture_settings("twoFingerTilt", "ON", "ON", "#5 updateGestureSettings twoFingerTilt ON")
        self.show_map_info("True")
        self.two_finger_tilt("x1,y2", "x1,y1", "#6 twoFingerTilt: x1,y2, x1,y1")

    @py_xml_wrapper
    def test_7181(self):
        self.description({"description": "gesture---pan",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - satellite.day - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapFragment - offline - carnav.day - Globe",
                                       "mapView - offline - normal.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapView - online - normal.day - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapFragment - online - normal.day - Globe - Landscape",
                                       "mapFragment - offline - normal.day - Globe",
                                       "mapFragment - online - normal.night - Globe"],
                          "priority": ["HighPriority", "LKWPriority"]})

        self.open_mapping_and_set_center()

        self.pan("x0,y0", "x2,y2", index="#2 pan: x0,y0, x2,y2")
        self.show_map_info("True")

        self.update_gesture_settings("pan", "OFF", "ON", "#3 updateGestureSettings pan OFF")
        self.show_map_info("True")
        self.pan("x0,y0", "x2,y2", index="#4 pan: x0,y0, x2,y2")

        self.update_gesture_settings("pan", "ON", "ON", "#5 updateGestureSettings pan ON")
        self.show_map_info("True")
        self.pan("x0,y0", "x2,y2", index="#4 pan: x0,y0, x2,y2")

    @py_xml_wrapper
    def test_7182(self):
        self.description({"description": "gesture---kineticFlick",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - satellite.day - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapFragment - offline - carnav.day - Globe",
                                       "mapView - offline - normal.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapView - online - normal.day - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapFragment - online - normal.day - Globe - Landscape",
                                       "mapFragment - offline - normal.day - Globe",
                                       "mapFragment - online - normal.night - Globe"]})

        self.open_mapping_and_set_center()

        self.kinetic_flick("x2,y2", "x0,y1", "#2 kineticFlick: x2,y2, x0,y1")
        self.show_map_info("True")

        self.update_gesture_settings("kineticFlick", "OFF", "OFF", "#3 updateGestureSettings kineticFlick OFF")
        self.show_map_info("True")
        self.kinetic_flick("x1,y2", "x1,y1", "#4 kineticFlick: x1,y2, x1,y1")

        self.update_gesture_settings("kineticFlick", "ON", "OFF", "#5 updateGestureSettings kineticFlick ON")
        self.show_map_info("True")
        self.kinetic_flick("x1,y2", "x1,y1", "#6 kineticFlick: x1,y2, x1,y1")

    @py_xml_wrapper
    def test_7183(self):
        self.description({"description": "gesture---tap",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - satellite.day - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapFragment - offline - carnav.day - Globe",
                                       "mapView - offline - normal.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapView - online - normal.day - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapFragment - online - normal.day - Globe - Landscape",
                                       "mapFragment - offline - normal.day - Globe",
                                       "mapFragment - online - normal.night - Globe"]})

        self.open_mapping_and_set_center()

        self.update_gesture_settings("singleTap", "ON", "ON", "#2 updateGestureSettings singleTap ON")
        self.single_tap("x2,y2", "#3 singleTap: x2,y2")

        self.update_gesture_settings("singleTap", "OFF", "ON", "#4 updateGestureSettings singleTap OFF")
        self.single_tap("x2,y2", "#4 singleTap: x2,y2")

        self.update_gesture_settings("singleTap", "ON", "ON", "#5 updateGestureSettings singleTap ON")
        self.single_tap("x2,y2", "#6 singleTap: x2,y2")

    @py_xml_wrapper
    def test_7184(self):
        self.description({"description": "gesture---2fingerTap to Zoom Out",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - satellite.day - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapFragment - offline - carnav.day - Globe",
                                       "mapView - offline - normal.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapView - online - normal.day - Globe",
                                       "mapFragment - offline - normal.day - Globe",
                                       "mapFragment - online - normal.night - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapFragment - online - normal.day - Globe - Landscape"]})

        self.open_mapping_and_set_center()

        self.two_finger_tap_zoom_out("x2,y2", "x3,y3", "#2 twoFingerTapZoomOut: x2,y2, x3,y3")
        self.show_map_info("True")

        self.update_gesture_settings("twoFingerTapZoomOut", "OFF", "ON", "#3 updateGestureSettings "
                                                                         "twoFingerTapZoomOut OFF")
        self.show_map_info("True")
        self.two_finger_tap_zoom_out("x2,y2", "x3,y3", "#4 twoFingerTapZoomOut: x2,y2, x3,y3")

        self.update_gesture_settings("twoFingerTapZoomOut", "ON", "ON", "#5 updateGestureSettings "
                                                                        "twoFingerTapZoomOut ON")
        self.show_map_info("True")
        self.two_finger_tap_zoom_out("x2,y2", "x3,y3", "#6 twoFingerTapZoomOut: x2,y2, x3,y3")

    @py_xml_wrapper
    def test_7185(self):
        self.description({"description": "gesture---twoFingerPan",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - normal.night - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapFragment - online - normal.day - Globe - Landscape",
                                       "mapFragment - online - satellite.day - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapFragment - offline - carnav.day - Globe",
                                       "mapFragment - offline - normal.day - Globe",
                                       "mapView - offline - normal.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapView - online - normal.day - Globe"]})

        self.open_mapping_and_set_center()

        self.two_finger_pan("x0,y0", "x4,y1", "#2 twoFingerPan: x0,y0, x4,y1")
        self.show_map_info("True")

        self.update_gesture_settings("twoFingerPan", "OFF", "ON", "#3 updateGestureSettings twoFingerPan OFF")
        self.show_map_info("True")
        self.two_finger_pan("x0,y0", "x4,y1", "#4 twoFingerPan: x0,y0, x4,y1")

        self.update_gesture_settings("twoFingerPan", "ON", "ON", "#5 updateGestureSettings twoFingerPan ON")
        self.show_map_info("True")
        self.two_finger_pan("x0,y0", "x4,y1", "#6 twoFingerPan: x0,y0, x4,y1")

    @py_xml_wrapper
    def test_7186(self):
        self.description({"description": "gesture---setAll, unsetAll",
                          "edition": "PremiumSDK",
                          "platform": ["mapFragment - online - satellite.day - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapFragment - offline - carnav.day - Globe",
                                       "mapFragment - online - normal.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapView - online - normal.day - Globe",
                                       "mapView - offline - normal.day - Globe",
                                       "mapFragment - online - normal.night - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapFragment - offline - normal.day - Globe",
                                       "mapFragment - online - normal.day - Globe - Landscape"]})

        self.open_mapping_and_set_center()
        self.perform_all_gestures("ON", "x0,y1")
        self.perform_all_gestures("OFF", "x0,y1")
        self.perform_all_gestures("ON", "x3,y2")

    def open_mapping_and_set_center(self):
        self.open_screen("Mapping")
        self.set_carto_poi("Off")
        self.wait(5000)

        self.set_center_default_null(value1=49.2824288, value2=-123.1178713, value3="NONE")
        self.set_center_default_null(value4=15)

        self.capture_screen(index="#1 CartoPOI all off, Vancouver Zoom 15")

    def perform_all_gestures(self, gesture_mode, kinetic_second_param):
        self.update_gesture_settings("All", gesture_mode, "ON", "updateGestureSettings ALL {}".format(gesture_mode))
        self.long_press("x2,y2", "longPress: x2,y2")
        self.single_tap("x2,y2", "singleTap: x2,y2")

        self.show_map_info("True")

        self.double_tap_zoom_in("x2,y2", "doubleTapZoomIn: x2,y2")
        self.two_finger_tap_zoom_out("x2,y2", "x3,y3", "twoFingerTapZoomOut: x2,y2, x3,y3")
        self.two_finger_tilt("x2,y2", "x0,y1", "twoFingerTilt: x2,y2, x0,y1")
        self.kinetic_flick("x2,y2", kinetic_second_param, "kineticFlick: x2,y2, {}".format(kinetic_second_param))
        self.pan("x0,y0", "x2,y2", "pan: x0,y0, x2,y2")
        self.pinch_close_zoom_out("x4,y3", "x0,y0", "pinchCloseZoomOut: x4,y3, x0,y0")
        self.pinch_open_zoom_in("x0,y0", "x3,y1", "pinchOpenZoomIn: x0,y0, x3,y1")
        self.two_finger_pan("x0,y0", "x4,y1", "twoFingerPan: x0,y0, x4,y1")
