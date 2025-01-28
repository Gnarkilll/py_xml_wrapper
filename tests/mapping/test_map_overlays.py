from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class MapOverlays(BaseTestCase):

    @py_xml_wrapper
    def test_7171(self):
        self.description({"description": "Map Object - Map Overlays - Movable Overlay",
                          "edition": "PremiumSDK",
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapFragment - offline - carnav.day - Globe",
                                       "mapFragment - online - normal.day - Globe - Landscape",
                                       "mapFragment - online - normal.day - Mercator - Landscape"],
                          "priority": "HighPriority"})

        self.set_service_status("location", "Off")
        self.open_screen("Mapping")
        self.set_carto_poi("Off")
        self.set_center(52.531025, 13.384933, 12, value3="LINEAR")

        self.create_map_overlay("Movable Overlay")
        self.wait_and_capture(index="CartoPOI all off, 52.531025, 13.384933, Zoom 12, Create Movable Overlay")

        self.pan_and_click_movable_overlay("x1,y1", "x3,y3", "pan x1,y1, x3,y3", "clickOnMapOverlay")
        self.pan_and_click_movable_overlay("x2,y2", "x4,y4", "pan x2,y2, x4,y4", "clickOnMapOverlay")

        self.double_tap_zoom_in("x1,y0")
        self.show_map_info("True")
        self.wait_and_capture(index="doubleTapZoomIn, showMapInfo true")
        self.show_map_info("False")

        self.pan_and_click_movable_overlay("x3,y3", "x1,y1", "showMapInfo False, pan x3,y3, x1,y1", "clickOnMapOverlay")
        self.pan_and_click_movable_overlay("x4,y4", "x2,y2", "pan x4,y4, x2,y2", "clickOnMapOverlay")

        self.common_steps_7171_7270("Movable Overlay")

        self.click_on_map_overlay("Movable Overlay", 4, "clickOnMapOverlay 4")
        self.remove_overlays_local(5, 2)
        self.set_service_status("location", "On")

    @py_xml_wrapper
    def test_7270(self):
        self.description({"description": "Map Object - Map Overlays - Anchor Mutable Overlay",
                          "edition": "PremiumSDK",
                          "platform": "mapFragment - online - normal.day - Globe"})

        self.open_screen("Mapping")
        self.set_carto_poi("Off")
        self.set_center(52.531025, 13.384933, 12)

        self.create_map_overlay("Anchor Mutable Overlay")
        self.wait_and_capture()

        self.pan_and_click_anchor_mutable_overlay()

        self.set_center(52.531025, 13.384933, 18)

        self.pan_and_click_anchor_mutable_overlay()

        self.common_steps_7171_7270("Anchor Mutable Overlay")
        self.remove_overlays_local(5, 2)

    @py_xml_wrapper
    def test_7271(self):
        self.description({"description": "Map Object - Map Overlays - Movable Overlay - "
                                         "Anchor Mutable Overlay - add map objects",
                          "edition": "PremiumSDK",
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - normal.day - Globe - Landscape"]})

        self.set_service_status("location", "Off")
        self.open_screen("Mapping")
        self.open_objects_from_menu()
        self.set_carto_poi("Off")

        self.set_center(52.500556, 13.398889, 16)
        self.perform_7271_steps_for_diff_radius(1000)

        self.set_center(52.5025, 13.3994, 10)
        self.perform_7271_steps_for_diff_radius(10000)

        self.rotate_screen_and_move_bg_fg_actions()
        self.remove_overlays_local(6, 1)
        self.set_service_status("location", "On")

    def pan_and_create_overlay(self, v1, v2, overlay):
        self.pan(v1, v2, False)
        self.wait(1000)
        self.create_map_overlay(overlay)

    def pan_and_click_movable_overlay(self, v1, v2, pan_index=None, overlay_index=None):
        self.pan(v1, v2, index=pan_index)
        self.click_on_map_overlay("Movable Overlay", 1, index=overlay_index)

    def pan_and_click_anchor_mutable_overlay(self):
        self.pan("x1,y1", "x3,y3")
        self.pan("x3,y3", "x1,y1")

        for _ in range(4):
            self.click_on_map_overlay("Anchor Mutable Overlay", 1)

    def perform_7271_steps_for_diff_radius(self, radius):
        self.create_map_overlay("Movable Overlay")
        self.wait_and_capture(index="Create Movable Overlay")

        self.add_map_object("Circle", "no")
        self.add_vertex("MapCircle", value1="x0,y0")
        self.set_radius(radius)
        self.capture_screen(index="addMapObject Circle, addVertex x0,y0, setRadius {}".format(radius))

        self.add_map_object("Marker", "no")
        self.add_vertex("MapMarker", value1="x0,y0", value2=None, value3="halt")
        self.set_img_type("MapMarker", "newImage")
        self.capture_screen(index="addMapObject Marker, addVertex x0,y0, setImageType newImage")

        self.create_map_overlay("Movable Overlay")
        self.wait_and_capture(index="createMapOverlay Movable Overlay")

        self.pan("x0,y0", "x2,y2", index="pan: x0,y0, x2,y2")

        for _ in range(1):
            self.create_map_overlay("Anchor Mutable Overlay")
            self.capture_screen(index="createMapOverlay Anchor Mutable Overlay")

        self.pinch_close_zoom_out("x4,y3", "x0,y0", "pinchCloseZoomOut")

    def common_steps_7171_7270(self, overlay):
        for v1, v2 in [("x4,y2", "x4,y3"), ("x4,y2", "x4,y3"), ("x4,y1", "x3,y3"), ("x4,y3", "x4,y1")]:
            self.pan_and_create_overlay(v1, v2, overlay)
        self.capture_screen(index="(pan, createMapOverlay) * 4 times")

        self.pan("x1,y1", "x3,y3", index="pan x1,y1, x3,y3")
        self.pan("x3,y3", "x1,y1", index="pan x3,y3, x1,y1")

        self.rotate_screen_and_move_bg_fg_actions()

    def rotate_screen_and_move_bg_fg_actions(self):
        self.set_orientation("landscape")
        self.capture_screen(index="setOrientation landscape")

        self.set_orientation("portrait")
        self.capture_screen(index="setOrientation portrait")

        self.push_active_app_to_bg("Functional Test App V2")
        self.open_main_app()
        self.capture_screen(index="push FTA to background then bring to foreground")

    def remove_overlays_local(self, first, second):
        for _ in ["Overlay {}".format(first), "Overlay {}".format(second), "All"]:
            self.remove_map_overlay(_, "Remove {}".format(_))
