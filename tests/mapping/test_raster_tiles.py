from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class RasterTiles(BaseTestCase):

    @py_xml_wrapper
    def test_1(self):
        self.description({"description": "Mapping for Vancouver/Berlin/Manhattan/San-Francisco/London",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": "mapFragment - online - normal.day - Globe"})

        self.open_screen("Mapping")
        self.show_map_info("True")

        self.perform_test_steps_for_area("VANCOUVER")
        self.perform_test_steps_for_area("BERLIN")
        self.perform_test_steps_for_area("MANHATTAN")
        self.perform_test_steps_for_area("SANFRANCISCO")
        self.perform_test_steps_for_area("LONDON")

    def set_center_with_zoom_lvl(self, zoom_lvl, index=None):
        self.set_center_default_null(value4=zoom_lvl)
        self.wait_and_capture(index=index)

    def perform_pan(self, v1, v2, once=True, counter=None):
        if once and counter is None:
            self.pan(v1, v2)
        else:
            for _ in range(counter):
                self.pan(v1, v2, False)
            self.capture_screen()

    def set_center_and_perform_pan(self, zoom_lvl, v1, v2, once=True, counter=None, area=None):
        if area:
            self.set_center_by_place_name_with_null_default(area)
        self.set_center_with_zoom_lvl(zoom_lvl)
        self.perform_pan(v1, v2, once, counter)

    def perform_test_steps_for_area(self, area):
        self.set_center_by_place_name_with_null_default(area)
        for _ in [1.0, 3]:
            self.set_center_with_zoom_lvl(_)
        self.perform_pan("x2,y2", "x0,y0")

        self.set_center_and_perform_pan(5.0, "x0,y0", "x2,y2", area=area)
        self.set_center_and_perform_pan(8.0, "x2,y2", "x0,y0", area=area)
        self.set_center_and_perform_pan(10, "x0,y0", "x2,y2", area=area)
        self.set_center_and_perform_pan(12, "x2,y2", "x0,y0", area=area)

        self.set_center_and_perform_pan(14, "x0,y0", "x2,y2", False, 3)
        self.set_center_and_perform_pan(15, "x2,y2", "x0,y0", False, 3)

        self.set_center_with_zoom_lvl(16)
        for _ in range(2):
            self.pan("x0,y0", "x2,y2", False)
        self.pan("x3,y3", "x0,y0", False)
        self.capture_screen()

        self.set_center_and_perform_pan(17, "x2,y2", "x0,y0", False, 2)

        self.set_center_with_zoom_lvl(18)
        self.pan("x0,y0", "x2,y2", False)
        self.pan("x0,y0", "x3,y3", False)
        self.capture_screen()

        self.set_center_and_perform_pan(19, "x2,y2", "x0,y0", False, 2)
        self.set_center_and_perform_pan(20, "x0,y0", "x2,y2", False, 2)

    @py_xml_wrapper
    def test_8769(self):
        self.description({"description": "Turn off Location",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapView - online - normal.day - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapFragment - online - normal.night - Globe",
                                       "mapFragment - online - satellite.day - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapView - online - truck.day - Globe",
                                       "mapFragment - online - normal.day - Globe - Landscape",
                                       "mapFragment - online - normal.day - Mercator - Landscape",
                                       "mapFragment - online - truck.day - Globe",
                                       "mapFragment - online - truck.day - Globe - Landscape",
                                       "mapFragment - online - truck.day - Mercator",
                                       "mapView - online - truck.day - Mercator",
                                       "mapFragment - online - truck.night - Globe",
                                       "mapFragment - online - hybrid.truck.day - Globe",
                                       "mapFragment - online - hybrid.truck.night - Globe",
                                       "mapFragment - Online",
                                       "mapview - Online",
                                       "mapFragment - online - no map is downloaded - Auto",
                                       "mapFragment - online - no map is downloaded - ForceOnline in setting"]})

        self.set_service_status("location", "Off")
        self.capture_screen(index="Location: OFF")

    @py_xml_wrapper
    def test_8770(self):
        self.description({"description": "Download mapping for Berlin/British Columbia/California/New York/"
                                         "England/Washington/Hauts-de-France/Hong Kong and Macao",
                          "edition": "PremiumSDK",
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - normal.night - Globe",
                                       "mapFragment - online - satellite.day - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapFragment - online - hybrid.truck.day - Globe",
                                       "mapFragment - online - hybrid.truck.night - Globe",
                                       "mapFragment - online - normal.day - Globe - Landscape",
                                       "mapFragment - online - normal.day - Mercator - Landscape",
                                       "mapFragment - online - truck.day - Globe",
                                       "mapFragment - online - truck.day - Globe - Landscape",
                                       "mapFragment - online - truck.day - Mercator",
                                       "mapFragment - online - truck.night - Globe",
                                       "mapView - online - normal.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapView - online - truck.day - Globe",
                                       "mapView - online - truck.day - Mercator",
                                       "mapFragment - Online",
                                       "mapview - Online"]})

        self.perform_test_8770_steps()

    @py_xml_wrapper
    def test_7205(self):
        self.description({"description": "Verify Custom RasterTiles - Live Map",
                          "edition": ["StarterSDK", "PremiumSDK", "IOSSupported", "NotRunInIOS"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - normal.night - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapView - online - normal.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapFragment - online - normal.day - Globe - Landscape"],
                          "priority": "HighPriority"})

        self.open_screen("Mapping")
        self.set_carto_poi("Off")
        self.create_custom_raster_tile("Live Map")

        areas = ["VANCOUVER", "SANFRANCISCO", "MANHATTAN", "BERLIN", ""]

        for area in areas:
            self.set_center_by_place_name_set_zoom_lvls_and_pan(area)

        for area in areas:
            self.set_center_by_place_name_set_zoom_lvl(area, "set the CenterByPlaceName as {}, animation as NONE; "
                                                             "and set map zoom level to 15".format(area))
            if not area:
                self.set_center_default_null(value6=82)
                self.wait_and_capture(index="set the map center as 51.5400,-0.015300, animation is NONE; "
                                            "set map zoom level is 15 and tilt 82")

        self.go_to_bg_back_to_fg_remove_tiles()

    def set_center_by_place_name_set_zoom_lvls_and_pan(self, area=None):
        if area:
            index_text = "set the CenterByPlaceName as {} and animation as NONE, set the zoom level as"\
                .format(area.capitalize())
        else:
            index_text = "set the map center as 51.54000,-0.015300, animation is NONE; and map zoom level to"
        zoom_values = {4:  "open mapping, turn off all setCartoPOI, create a Live Type Custom Raster Tile, "
                           "set {} as the CenterByPlaceName, set the zoom level to 4".format(area.capitalize()),
                       2:  "{} 2".format(index_text),
                       0:  "{} 0".format(index_text),
                       10: "{} 10".format(index_text),
                       12: "{} 12".format(index_text),
                       15: "{} 15".format(index_text),
                       18: "{} 18".format(index_text),
                       20: "{} 20".format(index_text)}
        for k, v in zoom_values.items():
            self.choose_center_type(area)
            self.set_center_with_zoom_lvl(k, v)
        self.pan("x0,y0", "x1,y1", index="pan the map from x0,y0 to x1,y1")
        self.pan("x0,y0", "x1,y1", index="pan the map from x0,y0 to x1, y1")

    def set_center_by_place_name_set_zoom_lvl(self, area=None, index=None):
        self.choose_center_type(area)
        self.set_center_with_zoom_lvl(15, index)

    def choose_center_type(self, area):
        if area:
            self.set_center_by_place_name_with_null_default(area)
        else:
            self.set_center_default_null(value1=51.54000, value2=-0.015300, value3="NONE")

    @py_xml_wrapper
    def test_7206(self):
        self.description({"description": "Verify Custom RasterTiles - London Olympic Park",
                          "edition": ["PremiumSDK", "IOSSupported", "NotRunInIOS"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - offline - normal.day - Globe",
                                       "mapFragment - online - normal.night - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - carnav.day - Globe",
                                       "mapFragment - offline - carnav.day - Globe",
                                       "mapFragment - online - normal.traffic.day - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapView - online - normal.day - Globe",
                                       "mapView - offline - normal.day - Globe",
                                       "mapView - online - normal.day - Mercator",
                                       "mapFragment - online - normal.day - Globe - Landscape"]})

        self.open_screen("Mapping")
        self.set_carto_poi("Off")
        self.create_custom_raster_tile("London Olympic Park")
        self.wait_and_capture(index="CartoPOI all off, createCustomRasterTile London Olympic Park")

        for _ in [20, 18, 16.3000, 15, 13, 15, 18]:
            self.set_center_by_place_name_with_null_default("LONDON")
            self.set_center_with_zoom_lvl(_, "LONDON Zoom: {}".format(_))

        self.pan("x0,y0", "x1,y1", index="pan x0,y0, x1,y1")
        self.pan("x0,y0", "x1,y1", index="pan x0,y0, x1,y1")

        for _ in [15, 30, 45, 60]:
            self.set_center_by_place_name_with_null_default("LONDON")
            self.set_center_default_null(value4=16.5)
            self.set_center_default_null(value6=_)
            self.wait_and_capture(index="LONDON Zoom 16.5, Tilt {}".format(_))

        self.set_center_by_place_name_with_null_default("LONDON")
        self.set_center_default_null(value4=13)
        self.set_center_default_null(value6=82)
        self.wait_and_capture(index="LONDON Zoom 13, Tilt 82")

        self.go_to_bg_back_to_fg_remove_tiles()

    def go_to_bg_back_to_fg_remove_tiles(self):
        self.push_active_app_to_bg("Functional Test App V2")
        self.bring_app_to_foreground("Functional Test App V2")
        self.capture_screen(index="push the app to the background and bring it forward")

        self.remove_all_tiles()
        self.capture_screen(index="remove all tiles from RasterTiles")
