from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class LayerObjects(BaseTestCase):

    @py_xml_wrapper
    def test_6851(self):
        self.description({"description": "online - Embedded POIs - all different map scheme",
                          "edition": "PremiumSDK",
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - offline - normal.day - Globe"],
                          "priority": "HighPriority"})

        self.open_screen("Mapping")
        self.set_center(49.2824288, -123.1178713, 17, index="#1 zoom level 17 at 49.2824288, -123.1178713")
        self.turn_off_on_carto_poi("#2 turn off all setCartoPOI under LayerObjects",
                                   "#3 turn on all setCartoPOI under LayerObjects")

        self.set_map_scheme("normal.night")
        self.set_traffic_layer(value2="NORMAL")
        self.wait(30000)
        self.street_lvl_coverage("On")
        self.wait(30000)
        self.set_center_default_null(value6=82)
        self.turn_off_on_carto_poi("#4 set map schema to normal.night; turn on trafficInfoState; set to Normal; "
                                   "turn on flowState, incidentState, and onRouteState; "
                                   "turn on streetLevelCoverage; set tilt to 82; "
                                   "turn off all setCartoPOI under LayerObjects",
                                   "#5 turn on all setCratoPOI under LayerObjects")

        self.set_map_scheme("terrain.day")
        self.set_traffic_layer(value1="Off", value2="NORMAL")
        self.street_lvl_coverage("Off")
        self.wait(3000)
        self.set_center_default_null(value6=0)
        self.turn_off_on_carto_poi("#6 set map schema to terrian.day; turn off trafficInfoState; set to NORMAL; "
                                   "turn on flowState, incidentState, and onRouteState; "
                                   "turn off selectStreetLevelCoverage; "
                                   "set map tilt to 0; turn off all setCartoPOI under LayerObjects",
                                   "#7 turn on all setCartoPOI under LayerObjects")

        self.action_with_diff_map_scheme()

        self.set_map_scheme("normal.day")
        self.set_center(52.500556, -3.398889, 17, index="#36 set map schema to normal.day; "
                                                        "set center coordinate to 52.500556, -3.398889; "
                                                        "set animation to NONE; set zoom level to 17")
        self.turn_off_on_carto_poi("#37 turn off all setCartoPOI under LayerObjects",
                                   "#38 turn on all setCartoPOI under LayerObjects")

        self.set_orientation("landscape")
        self.wait(5000)
        self.capture_screen(index="#39 set orientation to landscape")

    def turn_off_on_carto_poi(self, off_index, on_index):
        self.set_carto_poi("Off")
        self.capture_screen(index=off_index)
        self.set_carto_poi("On")
        self.capture_screen(index=on_index)

    def action_with_diff_map_scheme(self):
        schemes = ["satellite.day", "hybrid.day","pedestrian.day","normal.day.grey","normal.night.grey",
                   "normal.traffic.day", "normal.traffic.night", "normal.day.transit", "normal.night.transit",
                   "reduced.day", "reduced.night", "carnav.day", "maneuver.day", "truck.day"]
        off_index_num = 8
        on_index_num = 9
        for scheme in schemes:
            self.set_map_scheme(scheme)
            self.turn_off_on_carto_poi("#{} set map schema to {}; turn off all setCartoPOI under LayerObjects".format(off_index_num, scheme),
                                       "#{} turn on all setCartoPOI under LayerObjects".format(on_index_num))
            off_index_num += 2
            on_index_num += 2

    @py_xml_wrapper
    def test_6876(self):
        self.description({"description": "NMA - ShowMap - Extruded Building",
                          "edition": ["PremiumSDK", "StarterSDK", "IOSSupported", "NotRunInIOS"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - normal.night - Globe",
                                       "mapFragment - online - hybrid.day - Globe",
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapView - online - normal.day - Globe",
                                       "mapFragment - offline - normal.day - Globe"]})

        self.open_screen("Mapping")

        self.set_center(49.277, -123.1133, 16.8, value6=58.73475, index="#1 Extruded buildings on by default")
        self.select_extruded_bldg("Off", "#2 Extruded buildings turned off")
        self.select_extruded_bldg("On", "#3 Extruded buildings turned on")

        self.set_center(52.5352, 13.3713, 16.9, value6=64.92, index="#4 Berlin: Extruded buildings turned on")
        self.select_extruded_bldg("Off", "#5 Berlin: Extruded buildings turned off")

    @py_xml_wrapper
    def test_7235(self):
        self.description({"description": "Traffic filtration",
                          "edition": ["PremiumSDK"],
                          "platform": ["mapView - online - truck.day - Mercator"],
                          "priority": "HighPriority"})
        self.open_screen("Mapping")

        self.set_center(48.8567, 2.3508, 13,
                        index="Screenshot #1 zoom level 13 at Paris without Traffic")
        self.set_traffic_layer(value2="NORMAL")
        self.wait_and_capture(15000,
                              index="Screenshot #2  ZL 13 at Paris with Normal Traffic ")

        self.set_traffic_layer(value2="HIGH")
        self.wait_and_capture(5000,
                              index="Screenshot #3  ZL 13 at Paris with High Traffic")

        self.set_traffic_layer(value2="VERY_HIGH")
        self.wait_and_capture(5000,
                              index="Screenshot #4  ZL 13 at Paris with Very High Traffic")

        self.set_traffic_layer(value2="BLOCKING")
        self.wait_and_capture(5000,
                              index="Screenshot #5  ZL 13 at Paris with Blocking Traffic")

        self.set_center(40.748433, -73.985656, 13)
        self.set_traffic_layer(value2="NORMAL")
        self.wait_and_capture(15000,
                              index="Screenshot #6  ZL 13 at Manhattan with Normal Traffic ")

        self.set_traffic_layer(value2="HIGH")
        self.wait_and_capture(5000,
                              index="Screenshot #7  ZL 13 at Manhattan with High Traffic")

        self.set_traffic_layer(value2="VERY_HIGH")
        self.wait_and_capture(5000,
                              index="Screenshot #8  ZL 13 at Manhattan with Very High Traffic")

        self.set_traffic_layer(value2="BLOCKING")
        self.wait_and_capture(5000,
                              index="Screenshot #9  ZL 13 at Manhattan with Blocking Traffic")

    @py_xml_wrapper
    def test_6734(self):
        self.description({"description": "Traffic after panning - FT app",
                          "edition": ["PremiumSDK"],
                          "platform": ["mapFragment - online - truck.day - Globe"],
                          "priority": "HighPriority"})
        self.open_screen("Mapping")

        self.set_center(48.8567, 2.3508, 13,
                        index="Screenshot #1 zoom level 13 at Paris without Traffic")
        self.set_traffic_layer(value2="NORMAL")
        self.wait_and_capture(15000,
                              index="Screenshot #2  ZL 13 at Paris with Traffic turn on")

        self.pan("300,500", "-2000,500", False)
        self.wait_and_capture(10000,
                              index="Screenshot #3 ZL 13 at Paris traffic after panning to left after max 10 seconds")

        self.set_center(40.748433, -73.985656, 15)
        self.wait_and_capture(15000,
                              index="Screenshot #4  ZL 15 at Manhattan with Traffic turn on")
        self.pan("300,500", "1000,500", False)
        self.wait_and_capture(10000,
                              index="Screenshot #5 ZL 15 at Manhattan traffic after pan to right after max 10 seconds")

    @py_xml_wrapper
    def test_6738(self):
        self.description({"description": "different map scheme - different Map projections - Landsape - Live Traffic",
                          "edition": ["PremiumSDK"],
                          "platform": ["mapFragment - online - truck.day - Globe"],
                          "priority": "HighPriority"})
        self.open_screen("Mapping")

        self.set_center(49.2824288, -123.1178713, 15, index="Screenshot #1 zoom level 15 at 49.2824288, -123.1178713 (Vancouver) without Traffic")
        self.set_traffic_layer(value2="NORMAL")
        self.wait_and_capture(20000, index="Screenshot #2 zoom level 15 at 49.2824288, -123.1178713 (Vancouver) with Traffic turn on flowState, incidentState, and onRouteState")

        self.set_center(48.8567, 2.3508, 13)
        self.wait_and_capture(20000, index="Screenshot #3 zoom level 13 at 48.8567, 2.3508 (Paris) with Traffic turn on flowState, incidentState, and onRouteState")

        self.set_map_scheme("normal.night")
        self.capture_screen(index="Screenshot #4 Normal Night zoom level 13 at 48.8567, 2.3508 (Paris) with Traffic turn on all")

        self.push_active_app_to_bg()
        self.wait_and_capture(30000, index="Screenshot #5 Move application in background and wait 30 seconds")

        self.bring_app_to_foreground("Functional Test App V2")
        self.capture_screen(index="Screenshot #6 Foreground zoom level 13 at 48.8567, 2.3508 (Paris) all Traffic on")

        self.set_map_scheme("reduced.day")
        self.set_traffic_layer(value2="NORMAL", value3="Off")
        self.wait_and_capture(1000,
                              index="Screenshot #7 Reduced day ZL 13 at Paris Traffic on, flowState off, incidentState on, onRouteState on")
        self.set_traffic_layer(value2="NORMAL", value3="Off", value4="Off")
        self.wait_and_capture(1000,
                              index="Screenshot #8 zoom level 13 at 48.8567, 2.3508 (Paris) Traffic on, flowState off, incidentState off, onRouteState on")

        self.set_traffic_layer(value2="NORMAL", value3="On", value4="On")
        self.wait_and_capture(1000,
                              index="Screenshot #9 zoom level 13 at 48.8567, 2.3508 (Paris) Traffic on, flowState on, incidentState on, onRouteState on")
