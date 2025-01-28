from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class CreateBitMap(BaseTestCase):

    @py_xml_wrapper
    def test_6863(self):
        self.description({"description": "online - creat bitmap - different zoom level - width and height",
                          "edition": "PremiumSDK",
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - offline - normal.day - Globe",
                                       "mapFragment - online - normal.day - Mercator"]})

        self.open_screen("Mapping")
        self.click_bitmap_button(3000, "#1 Create Bitmap in default location", True)

        self.set_bitmap_params(52.500556, 13.398889, 800, 800, 10)
        self.click_bitmap_button(40000, "#2 Create Bitmap in Berlin location, with zoom level 10")

        self.set_bitmap_params(40.790278, -73.959722, 900, 900, 18)
        self.click_bitmap_button(40000, "#3 Create Bitmap in 97th St location, with zoom level 18")

        self.set_bitmap_params(51.541211, -0.015306, 400, 400, 8)
        self.click_bitmap_button(40000, "#4 Create Bitmap in London location, with zoom level 8")

        self.set_bitmap_params(37.774921, -122.419503, 600, 600, 4)
        self.click_bitmap_button(40000, "#5 Create Bitmap in SF location, with zoom level 4")

        self.force_stop_app("com.here.functionaltestv2")
        self.wait(5000)

        self.open_screen("Mapping")
        self.set_orientation("landscape")
        self.click_bitmap_button(3000, "#6 Create Bitmap in default location in landscape mode", True)

        self.set_bitmap_params(52.500556, 13.398889, 800, 800, 10)
        self.click_bitmap_button(10000, "#7 Create Bitmap in Berlin location in landscape mode, with zoom level 10")
