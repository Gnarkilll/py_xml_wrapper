from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class MapDimentions(BaseTestCase):

    @py_xml_wrapper
    def test_6855(self):
        self.description({"description": "online - Map Dimentions - change Clip Rect",
                          "edition": "PremiumSDK",
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - normal.day - Mercator"],
                          "priority": "HighPriority"})

        self.open_screen("Mapping")
        self.open_dimensions_from_menu()

        self.dimensions_test_steps()

        self.click_dimensions_btn("X", "Close map dimension")
        self.force_stop_app("com.here.functionaltestv2")

        self.open_screen("Mapping")
        self.set_orientation("landscape")
        self.open_dimensions_from_menu()
        self.click_dimensions_btn("Reset")

        self.dimensions_test_steps()

        self.set_orientation("portrait")
        self.capture_screen(index="Close map dimension window")

    def dimensions_test_steps(self):
        self.set_position("right", 600)
        self.set_position("bottom", 600)
        self.click_dimensions_btn("Apply", "Set bottom and right dimension to 600, "
                                           "which is smaller than default dimension")

        self.set_position("right", 500)
        self.click_dimensions_btn("Apply", "Set right dimension to a smaller number")

        self.set_position("bottom", 500)
        self.click_dimensions_btn("Apply", "Set bottom dimension to a smaller number")

        self.set_position("left", 100)
        self.set_position("top", 100)
        self.click_dimensions_btn("Apply", "Set left and top dimension to 100")
        self.click_dimensions_btn("Reset")

        self.set_position("right", 2000)
        self.set_position("bottom", 2000)
        self.click_dimensions_btn("Apply", "Set right and bottom to 2000, size on screen will not change")

        self.set_position("left", 1000)
        self.set_position("top", 1000)
        self.click_dimensions_btn("Apply", "Set top and left dimensions to 1000")

    @py_xml_wrapper
    def test_6856(self):
        self.description({"description": "online - Map Dimentions - change Clip Rect",
                          "edition": "PremiumSDK",
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - normal.day - Mercator"]})

        self.open_screen("Mapping")

        self.add_screen_marker("X1,Y1", "Adidas")

        self.set_position("right", 980)
        self.set_position("bottom", 1000)

        self.click_dimensions_btn("Apply", "Map gets smaller")

        self.add_screen_marker("X2,Y2", "Nike")

        self.add_marker("X1,Y1", "CAR_IMAGE")
        self.open_objects_from_menu()
        self.add_marker("X2,Y2", "CAR_IMAGE")
        self.capture_screen(index="Half of Car marker displays on the screen."
                                  "The second car marker cannot be shown on the screen because "
                                  "it's out of the map dimension")

        self.set_center_default_null(value4=12)
        self.capture_screen(index="Zoom 15")

        self.set_center_default_null(value6=82)
        self.capture_screen(index="Tilt 82")

        self.show_map_info("True")

        self.set_traffic_layer(value2="NORMAL")
        self.capture_screen(index="Traffic mode on")

        self.pan("x0,y0", "x2,y2", index="Pan x0,y0 to x2,y2")

    def add_screen_marker(self, v1, v2):
        self.open_objects_from_menu()
        self.add_map_object("SCREENMARKER")
        self.capture_screen(index="Screen marker settings page is displayed")
        self.add_vertex("MapScreenMarker", value1=v1)
        self.set_img_type("MapScreenMarker", v2)
        if v2 == "Nike":
            self.capture_screen(index="The Nike marker cannot be shown on the screen "
                                      "because it's out of the map dimension")
        else:
            self.capture_screen(index="An {} marker will be added to the screen".format(v2))
        self.open_dimensions_from_menu()
        self.capture_screen(index="Map Dimensions setting page displays")

    def add_marker(self, v1, v2):
        self.add_map_object("MARKER")
        self.add_vertex("MapMarker", value1=v1)
        self.set_img_type("MapMarker", v2)
