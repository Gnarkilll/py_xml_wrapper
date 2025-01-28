from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class Logo(BaseTestCase):

    platforms = ["mapFragment - online - normal.day - Globe", "mapFragment - online - normal.night - Globe",
                 "mapFragment - online - satellite.day - Globe", "mapFragment - online - hybrid.day - Globe",
                 "mapFragment - online - carnav.day - Globe", "mapFragment - online - normal.traffic.day - Globe",
                 "mapFragment - online - normal.day - Mercator",  "mapFragment - offline - normal.day - Globe",
                 "mapFragment - offline - carnav.day - Globe", "mapView - offline - normal.day - Globe",
                 "mapView - online - normal.day - Globe", "mapFragment - online - normal.day - Globe - Landscape"]

    @py_xml_wrapper
    def test_6722(self):
        self.description({"description": "Nokia Logo - Change position of Copyright Logo on the map - Position - "
                                         "Visiblity- Margin - different map scheme - map projection - landscape mode",
                          "edition": ["PremiumSDK", "IOSSupported"],
                          "platform": self.platforms})

        self.open_screen("Mapping")
        self.wait(8000)
        self.set_carto_poi("Off")

        self.perform_logo_ops("VANCOUVER", 11.0)
        self.perform_logo_ops("MANHATTAN", 15)

        self.set_orientation("portrait")

        self.perform_logo_ops_for_diff_screen_orientation("landscape", 500, 5000, 500, 5000)
        self.perform_logo_ops_for_diff_screen_orientation("portrait", 1000, 5000, 1000, 5000)

    @py_xml_wrapper
    def test_7170(self):
        self.platforms.append("mapView - online - normal.day - Mercator")
        self.description({"description": "Nokia Logo - different map scheme - landscape - map projection",
                          "edition": ["StarterSDK", "PremiumSDK", "IOSSupported"],
                          "platform": self.platforms,
                          "priority": "HighPriority"})

        self.open_screen("Mapping")
        self.wait(8000)
        self.set_carto_poi("Off")

        self.set_zoom_multiple_for_specific_area("VANCOUVER")
        self.set_zoom_multiple_for_specific_area("BERLIN")
        self.set_zoom_multiple_for_specific_area("MANHATTAN")

        self.set_orientation("landscape")
        self.wait(5000)

        self.set_center_default_null(value1=37.77492, value2=-122.41950, value3="NONE")
        self.set_test_zoom(0, "37.77492, -122.41950, Zoom 0, landscape")

        self.set_zoom_multiple("37.77492, -122.41950")

    def set_test_zoom(self, value, index):
        self.set_center_default_null(value4=value)
        self.wait(5000)
        self.capture_screen(index=index)

    def set_zoom_multiple(self, area):
        zooms = [2, 18, 20]
        for zoom in zooms:
            self.set_test_zoom(zoom, "{}, Zoom {}".format(area.capitalize(), zoom))

    def set_zoom_multiple_for_specific_area(self, area):
        self.set_specific_zoom_lvl(area, 0.0, "{}, Zoom 0".format(area.capitalize()))
        self.set_zoom_multiple(area)

    def perform_logo_ops(self, area, zoom_lvl):
        self.set_specific_zoom_lvl(area, zoom_lvl)

        self.set_logo_position("BOTTOM_CENTER", 0, 0, 0, 0, "CartoPOI off, {}, Zoom {}, "
                                                            "Logo BOTTOM_CENTER (0,0,0,0)".format(area, zoom_lvl))

        positions = ["TOP_LEFT", "TOP_CENTER", "TOP_RIGHT", "BOTTOM_CENTER"]
        for position in positions:
            self.set_logo_position(position, 0, 5000, 0, 5000, "Logo {} (0,5000,0,5000)".format(position))

        self.set_logo_position("TOP_CENTER", 0, 5000, 0, 5000, "Logo TOP_CENTER (0,5000,0,5000)")

        margin_list = [100, 5, 50, -10, 0, -50]
        for margin in margin_list:
            self.set_margin(margin, "setMargin {}".format(margin))

        for position in positions:
            self.set_logo_position(position, 500, 5000, 500, 5000, "Logo {} (500,5000,500,5000)".format(position))

    def perform_logo_ops_for_diff_screen_orientation(self, screen_orientation, x1, y1, x2, y2):
        self.set_logo_position("TOP_RIGHT", x1, y1, x2, y2, "TOP_RIGHT {},{},{},{}".format(x1, y1, x2, y2))
        self.set_orientation(screen_orientation)
        self.wait(5000)

        self.set_specific_zoom_lvl("MANHATTAN", 15, "Manhattan, Zoom 15, {}".format(screen_orientation ))

    def set_specific_zoom_lvl(self, area, zoom_lvl, index=None):
        self.set_center_by_place_name_with_null_default(area)
        self.set_center_default_null(value4=zoom_lvl)
        self.wait(3000)
        self.capture_screen(index=index)
