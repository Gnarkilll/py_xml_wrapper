from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class Routing(BaseTestCase):

    @py_xml_wrapper
    def test_6579(self):
        self.description({"description": "PT timetable Online Routing - Online - Departure time set - Arrival time set",
                          "platform": ["mapView - online - no map is downloaded - Auto"],
                          "priority": "HighPriority"})
        self.open_screen("Routing")
        self.add_coordinate(52.547, 13.392)
        self.add_coordinate(52.483, 13.443)
        self.set_route_time("Depart at", "NEXT_MID_NIGHT", "NEXT_MID_NIGHT")
        self.set_route_count(10)
        self.calculate_route_for("Transit")
        self.wait(3000)
        self.select_route_number(1)
        self.open_maneuver_details()
        self.capture_screen(index="Screenshot #1 Route 1: Maneuver start time is already after near midnight")
        self.press_back()

        self.select_route_number(3)
        self.open_maneuver_details()
        self.capture_screen(index="Screenshot #2 Route 3: Maneuver start time is already after 00:00 tomorrow")
        self.press_back()

        self.set_route_time("Depart at", "TOMORROW_MORNING", "TOMORROW_MORNING")
        self.calculate_route_for("Transit")
        self.wait(3000)
        self.select_route_number(2)
        self.open_maneuver_details()
        self.capture_screen(index="Screenshot #3 Route 2: Maneuver start time is after 09:00 tomorrow")
        self.press_back()

        self.set_route_time("Depart at", "26/08/2024", "12:05")
        self.calculate_route_for("Transit")
        self.wait(3000)
        self.select_route_number(1)
        self.open_maneuver_details()
        self.capture_screen(index="Screenshot #4 Route 1: Maneuver start time is after 12:05, 26th of August 2024")
        self.press_back()

    @py_xml_wrapper
    def test_6594(self):
        self.description({"description": "Route Options - Map view - One Route - Traffic Filtration - Drive to mode",
                          "platform": ["mapView - online - no map is downloaded - Auto"],
                          "priority": "HighPriority"})
        self.open_screen("Routing")
        self.add_coordinate(50.434, 30.441)
        self.add_coordinate(50.472, 30.449)
        self.set_route_traffic_mode("Disabled")
        self.calculate_route_for("Drive")
        self.wait(3000)
        self.capture_screen(index="Screenshot #1 Create Drive route with disabled traffic")

        self.set_traffic_layer(value2="HIGH")
        self.wait_and_capture(20000,
                              index="Screenshot #2 (Kyiv) with HIGH Filtration Traffic turn on")
        self.set_route_traffic_mode("Avoid Long Term Closures")
        self.calculate_route_for("Drive")
        self.wait(3000)
        self.capture_screen(index="Screenshot #3 Create Drive route with Avoid Long Term Closures")

    @py_xml_wrapper
    def test_6592(self):
        self.description({"description": "Route Options - online mode - Map view - Traffic - Drive mode",
                          "platform": ["mapView - online - no map is downloaded - Auto"],
                          "priority": "HighPriority"})
        self.open_screen("Routing")
        self.add_coordinate(50.434, 30.441)
        self.add_coordinate(50.472, 30.449)
        self.set_route_traffic_mode("Disabled")
        self.calculate_route_for("Drive")
        self.wait(5000)
        self.capture_screen(index="Screenshot #1 Create Drive route with disabled traffic")

        self.set_traffic_layer(value2="NORMAL")
        self.wait_and_capture(20000,
                              index="Screenshot #2 (Kyiv) with full Traffic turn on")
        self.set_route_traffic_mode("Optimal")
        self.calculate_route_for("Drive")
        self.wait(5000)
        self.capture_screen(index="Screenshot #3 Create Drive route with Optimal traffic")

    @py_xml_wrapper
    def test_6572(self):
        self.description({"description": "Route Options - online mode - Map view - Traffic - Truck mode",
                          "platform": ["mapView - online - no map is downloaded - Auto"],
                          "priority": "HighPriority"})
        self.open_screen("Routing")
        self.add_coordinate(50.434, 30.441)
        self.add_coordinate(50.472, 30.449)
        self.set_route_traffic_mode("Disabled")
        self.calculate_route_for("Truck")
        self.wait(5000)
        self.capture_screen(index="Screenshot #1 Create Truck route with disabled traffic")

        self.set_traffic_layer(value2="NORMAL")
        self.wait_and_capture(20000,
                              index="Screenshot #2 (Kyiv) with full Traffic turn on")
        self.set_route_traffic_mode("Optimal")
        self.calculate_route_for("Truck")
        self.wait(5000)
        self.capture_screen(index="Screenshot #3 Create Truck route with Optimal traffic")

    @py_xml_wrapper
    def test_6730(self):
        self.description({"description": "Live Traffic - on Route",
                          "platform": ["mapFragment - Online"],
                          "priority": "HighPriority"})
        self.open_screen("Routing")
        self.add_coordinate(48.8567, 2.3508)
        self.add_coordinate(48.8467, 2.2908)
        self.calculate_route_for("Drive")
        self.wait(5000)
        self.capture_screen(index="Screenshot #1 Create Drive route without traffic")

        self.set_traffic_layer(value2="NORMAL")
        self.wait_and_capture(20000,
                              index="Screenshot #2 (Paris) with full Traffic turn on")

        self.set_traffic_layer(value2="NORMAL", value5="Off")
        self.capture_screen(
            index="Screenshot #3 Traffic on route off")

        self.set_traffic_layer(value2="NORMAL", value5="On")
        self.push_active_app_to_bg()
        self.wait_and_capture(30000, index="Screenshot #4 Move application in background and wait 30 seconds")

        self.bring_app_to_foreground("Functional Test App V2")
        self.capture_screen(index="Screenshot #5 Foreground Route all Traffic on")

    @py_xml_wrapper
    def test_6995(self):
        self.description({"description": "One Route - Route Options -  Allow Carpool - Drive to mode",
                          "edition": ["StarterSDK", "PremiumSDK", "IOSSupported", "NotRunInIOS"],
                          "platform": "mapFragment - offline - cached - ejl",
                          "priority": "LKWPriority"})

        self.open_screen("Routing")
        self.set_carto_poi("Off")
        self.add_coordinate(47.668036, -122.185628)
        self.add_coordinate(47.714825, -122.185789)
        self.add_route_option("Allow Carpool")
        self.calculate_route_for("Drive")
        self.capture_screen()

        self.add_route_option("Avoid Carpool")
        self.calculate_route_for("Drive")
        self.capture_screen()

    @py_xml_wrapper
    def test_8769(self):
        map_fragment = "mapFragment - "
        map_view = "mapView - "
        platform_1 = "online - no map is downloaded - Auto"
        platform_2 = "online - no map is downloaded - ForceOnline in setting"
        platform_3 = "offline - map is downloaded before"

        self.description({"description": "Turn off Location",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["{}{}".format(map_fragment, platform_1),
                                       "{}{}".format(map_fragment, platform_2),
                                       "{}{}".format(map_fragment, platform_3),
                                       "{}{}".format(map_view, platform_1),
                                       "{}{}".format(map_view, platform_2),
                                       "{}{}".format(map_view, platform_3)]})

        self.set_service_status("location", "Off")
        self.capture_screen()

    @py_xml_wrapper
    def test_8770(self):
        self.description({"description": "Download mapping for Berlin/British Columbia/California/"
                                         "New York/England/Washington/Hauts-de-France/Hong Kong and Macao",
                          "edition": "PremiumSDK",
                          "platform": ["mapFragment - online - no map is downloaded - ForceOnline in setting",
                                       "mapView - online - no map is downloaded - ForceOnline in setting"]})

        self.perform_test_8770_steps()

    @py_xml_wrapper
    def test_3(self):
        self.description({"description": "Mapping for routing",
                          "edition": ["StarterSDK", "PremiumSDK"]})

        self.open_screen("Mapping")
        self.show_map_info("True")

        # Vancouver
        self.set_center_by_place_name("VANCOUVER", 1.0, 8000)
        self.set_center_default_null(value4=3)
        self.wait(5000)
        self.capture_screen()
        self.pan("x2,y2", "x0,y0")

        self.set_center_by_place_name("VANCOUVER", 5.0, 5000)
        self.pan("x0,y0", "x2,y2")

        self.set_center_by_place_name("VANCOUVER", 8.0, 3000)
        self.pan("x2,y2", "x0,y0")

        self.set_center(48.8411, -123.2803, 10)
        self.pan("x0,y0", "x2,y2")
        self.pan("x2,y2", "x0,y0")

        self.set_center(49.0206, -124.9341, 10)
        self.pan("x0,y0", "x2,y2")
        self.pan("x0,y0", "x2,y2")
        self.pan("x2,y2", "x0,y0")

        self.set_center(49.2502, -122.9006, 11)
        self.pan("x2,y2", "x0,y0")
        self.pan("x0,y0", "x2,y2")

        self.set_center(49.1597, -122.6368, 11.7)
        self.pan("x2,y2", "x0,y0")
        self.pan("x0,y0", "x2,y2")

        self.set_center(49.1075, -123.0514, 12.1)
        self.pan("x2,y2", "x0,y0")
        self.pan("x0,y0", "x2,y2")

        self.set_center(49.2655, -123.227, 14.2)
        self.pan("x2,y2", "x0,y0")
        self.pan("x0,y0", "x2,y2")

        self.set_center(47.6914, -122.1828, 13)
        self.pan("x0,y0", "x0,y5")
        self.pan("x0,y0", "x0,y5")

        self.set_center(40.7622, -74.0128, 13)
        self.pan("x0,y0", "x1,y1")
        self.pan("x0,y0", "x3,y3")

        self.set_center(40.8524, -73.9523, 13.6)
        self.pan("x0,y0", "x1,y1")
        self.pan("x0,y0", "x3,y3")

        # Berlin
        self.set_center_by_place_name("BERLIN", 1.0, 8000)

        self.set_center_default_null(value4=3)
        self.wait(5000)
        self.capture_screen()

        self.pan("x2,y2", "x0,y0")

        self.set_center_by_place_name("BERLIN", 5.0, 5000)
        self.pan("x0,y0", "x2,y2")

        self.set_center(52.4871, 13.3061, 13.663)
        self.pan("x0,y0", "x1,y1")
        self.pan("x1,y1", "x0,y0")

        self.set_center(52.5284, 13.3864, 15)
        self.pan("x0,y0", "x1,y1")
        self.pan("x1,y1", "x0,y0")

        self.set_center(51.0147, 1.4591, 9.3)
        self.pan("x0,y0", "x1,y1")
        self.pan("x1,y1", "x0,y0")

        self.set_center(53.9553, 10.8691, 17)
        self.pan("x0,y0", "x1,y1")
        self.pan("x0,y0", "x3,y3")

        self.set_center(22.2833, 114.1448, 13)
        self.pan("x0,y0", "x1,y1")
        self.pan("x1,y1", "x0,y0")

    @py_xml_wrapper
    def test_6926(self):
        self.description({"description": "H - NMA - Route - Turn on network after start SDK",
                          "edition": "PremiumSDK",
                          "platform": "mapFragment - Online"})

        self.set_service_status("wifi", "On")
        self.open_screen("Mapping")

        self.set_center(37.7768, -122.4218, 13)
        self.wait(8000)
        self.capture_screen(index="#1 Network on, map of San Francisco shows up correctly")

        self.set_service_status("wifi", "Off")
        self.force_stop_app("com.here.functionaltestv2")

        self.open_screen("Routing")
        self.set_service_status("wifi", "On")
        self.add_coordinate(52.495, 13.401, "STOP")
        self.add_coordinate(52.495, 13.403, "STOP")
        self.calculate_route_for("Drive")
        self.capture_screen(index="#2 Turn off wifi, restart FTA, after SDK is initialized, turn on network and "
                                  "create a car route, this route should create successfully.")

        self.calculate_route_for("Walk")
        self.capture_screen(index="#3 Create a walk route, this route should create successfully.")

        self.calculate_route_for("Truck")
        self.capture_screen(index="#4 Create a truck route, this route should create successfully.")

        self.calculate_route_for("Transit")
        self.capture_screen(index="#5 Create a transit route, this route should create successfully.")

        self.zoom_in_at_maneuver(2)
        self.capture_screen(index="#6 Zoom in at second Maneuver to make sure that maneuver list is not empty")

        self.set_service_status("wifi", "Off")
        self.force_stop_app("com.here.functionaltestv2")

        self.open_screen("Search")
        self.set_service_status("wifi", "On")

        self.step("Search", "openSearchReq", value1="Reverse Geocode Request")
        self.step("Search", "executeReverseGeocodeReq", value1=37.7768, value2=-122.4218, value3=None)
        self.wait(8000)
        self.capture_screen(index="#7 Turn off wifi, restart FTA, after SDK is initialized, turn on network and do "
                                  "reverseGeocode Request in SF. Should return result 331 Haye St.")

    @py_xml_wrapper
    def test_6991(self):
        self.description({"description": "Multiple route - express lane in seattle - ANDROIDMPA-1572",
                          "edition": ["StarterSDK", "PremiumSDK", "IOSSupported", "NotRunInAndroid"],
                          "platform": "mapFragment - Online",
                          "priority": "HighPriority"})

        self.open_screen("Routing")
        self.set_carto_poi("Off")
        self.add_coordinate(49.2824288, -123.1178713)
        self.add_coordinate(37.774921, -122.419503)

        self.set_route_count(10)
        self.calculate_route_for("Drive")
        self.wait(30000)
        self.capture_screen()

        self.set_route_count(1)
        self.calculate_route_for("Drive")
        self.wait(30000)
        self.capture_screen()

    @py_xml_wrapper
    def test_6998(self):
        self.description({"description": "One Route - Car Shuttle Train - Drive to mode",
                          "edition": ["StarterSDK", "PremiumSDK", "IOSSupported", "NotRunInIOS"],
                          "platform": "mapFragment - offline - cached - ejl",
                          "priority": "LKWPriority"})

        self.open_screen("Routing")
        self.set_carto_poi("Off")
        self.add_coordinate(50.935672, 1.814757)
        self.add_coordinate(51.114276, 1.256393)

        self.add_route_option("Allow Car Shuttle Trains")
        self.calculate_route_for("Drive")
        self.capture_screen()

        self.add_route_option("Avoid Car Shuttle Trains")
        self.calculate_route_for("Drive")
        self.capture_screen()

    @py_xml_wrapper
    def test_7002(self):
        self.description({"description": "Route Options  - Map view - One Route - Park - Walk to mode",
                          "edition": ["StarterSDK", "PremiumSDK", "IOSSupported", "NotRunInIOS"],
                          "platform": "mapFragment - offline - cached - ejl",
                          "priority": ["LKWPriority", "HighPriority"]})

        self.open_screen("Routing")
        self.set_carto_poi("Off")
        self.add_coordinate(49.267, -123.225)
        self.add_coordinate(49.267, -123.239)

        self.add_route_option("Allow Parks")
        self.calculate_route_for("Walk")
        self.capture_screen()

        self.add_route_option("Avoid Parks")
        self.calculate_route_for("Walk")
        self.capture_screen()

    @py_xml_wrapper
    def test_7025(self):
        self.description({"description": "Multiple Route -  Ferry - Walk to mode",
                          "edition": ["StarterSDK", "PremiumSDK", "IOSSupported", "NotRunInIOS"],
                          "platform": "mapFragment - offline - cached - ejl",
                          "priority": "LKWPriority"})

        self.open_screen("Routing")
        self.set_carto_poi("Off")
        self.add_coordinate(49.007585, -123.132266)
        self.add_coordinate(48.687855, -123.410658)
        self.set_route_count(10)

        self.add_route_option("Allow Ferries")
        self.calculate_route_for("Walk")
        self.wait(10000)
        self.capture_screen()

        self.add_route_option("Avoid Ferries")
        self.calculate_route_for("Walk")
        self.wait(10000)
        self.capture_screen()

    @py_xml_wrapper
    def test_7037(self):
        self.description({"description": "Multiple Route - Route Options -  Allow Carpool - Drive to mode",
                          "edition": ["StarterSDK", "PremiumSDK", "IOSSupported", "NotRunInIOS"],
                          "platform": "mapFragment - offline - cached - ejl",
                          "priority": "LKWPriority"})

        self.open_screen("Routing")
        self.set_carto_poi("Off")
        self.add_coordinate(47.668036, -122.185628)
        self.add_coordinate(47.714825, -122.185789)
        self.wait(10000)
        self.set_route_count(10)

        self.add_route_option("Allow Carpool")
        self.calculate_route_for("Drive")
        self.capture_screen()

        self.add_route_option("Avoid Carpool")
        self.calculate_route_for("Drive")
        self.capture_screen()

    @py_xml_wrapper
    def test_7089(self):
        self.description({"description": "Route-Calculation maneuver detail stop compare with via points - "
                                         "Walk - drive - Estimated PT - Truck",
                          "edition": ["PremiumSDK", "IOSSupported"],
                          "platform": ["mapFragment - online - no map is downloaded - Auto",
                                       "mapFragment - offline - map is downloaded before"]})

        self.open_screen("Routing")
        self.set_carto_poi("Off")

        self.steps_for_7089("STOP")

        self.clear_current_route()

        self.steps_for_7089("VIA")

    def steps_for_7089(self, wp_type):
        self.add_coordinate(52.496, 13.399, "STOP")
        self.add_coordinate(52.495, 13.401, wp_type)
        self.add_coordinate(52.495, 13.403, "STOP")

        self.calculate_route_for("Drive")
        self.capture_screen()
        self.zoom_in_at_maneuver(2)
        self.wait(1000)
        self.capture_screen()

        self.calculate_route_for("Walk")
        self.capture_screen()
        self.zoom_in_at_maneuver(2)
        self.wait(1000)
        self.capture_screen()

        self.calculate_route_for("Transit")
        self.capture_screen()

    @py_xml_wrapper
    def test_7103(self):
        self.description({"description": "DisplayRoute - map view - route option online - "
                                         "network connection off - Truck",
                          "edition": ["PremiumSDK", "IOSSupported"],
                          "platform": "mapFragment - offline - map is downloaded before - ejl"})

        self.open_screen("Routing")
        self.set_carto_poi("Off")
        self.add_coordinate(40.72715, -74.03395)
        self.add_coordinate(40.72265, -74.00642)
        self.wait(10000)
        self.set_online_mode()

        self.calculate_route_for("Truck")
        self.wait(30000)
        self.capture_screen(index="Truck routing 40.72715, -74.03395 to 40.72265, -74.00642, setOnlineMode On")

    @py_xml_wrapper
    def test_7105(self):
        self.description({"description": "DisplayRoute - map view - route option online - network connection off - "
                                         "Car, Walk, PT mode",
                          "edition": ["PremiumSDK", "IOSSupported"],
                          "platform": "mapFragment - offline - map is downloaded before"})

        self.open_screen("Routing")
        self.set_carto_poi("Off")
        self.add_coordinate(40.72715, -74.03395)
        self.add_coordinate(40.72265, -74.00642)
        self.wait(10000)
        self.set_online_mode()

        self.calculate_route_for("Drive")
        self.wait(30000)
        self.capture_screen(index="#1 open Routing; turn off all CartoPOI; create route from "
                                  "40.72715,-74.03395 to 40.72265,-74.00642; set the device as online mode; "
                                  "calculate route by Drive")

        self.calculate_route_for("Walk")
        self.wait(30000)
        self.capture_screen(index="#2 change the transportation mode to Walk and recalculate the route")

        self.calculate_route_for("Transit")
        self.wait(30000)
        self.capture_screen(index="#3 change the transportation mode to Transit and recalculate the route")

    @py_xml_wrapper
    def test_7308(self):
        self.description({"description": "offline - offline cached - Truck Routing",
                          "edition": ["PremiumSDK", "IOSSupported", "NotRunInIOS"],
                          "platform": "mapFragment - offline - cached - ejl",
                          "priority": "HighPriority"})

        self.open_screen("Routing")
        self.set_carto_poi("Off")
        self.add_coordinate(39.29231, -76.60877)
        self.add_coordinate(39.29759, -76.59401)
        self.wait(10000)
        self.set_route_count(1)

        self.calculate_route_for("Drive")
        self.capture_screen()

        self.calculate_route_for("Truck")
        self.wait(10000)
        self.capture_screen()

    @py_xml_wrapper
    def test_7336(self):
        self.description({"description": "Truck Routing - Online - Maneuver list - entering highway - "
                                         "exiting highway - round about",
                          "edition": ["PremiumSDK", "IOSSupported"],
                          "platform": "mapFragment - online - no map is downloaded - Auto"})

        self.open_screen("Routing")
        self.set_carto_poi("Off")
        self.add_coordinate(52.4959638, 13.2880155)
        self.add_coordinate(52.47880, 13.32107)

        self.build_route_and_check_zoom_lvl("Drive", 9)
        self.build_route_and_check_zoom_lvl("Truck", 9)

        self.clear_current_route("Clear Map")

        self.add_coordinate(52.51503, 13.32280)
        self.add_coordinate(52.5090577, 13.3260266)

        self.build_route_and_check_zoom_lvl("Truck", 3)
        self.build_route_and_check_zoom_lvl("Drive", 3)

    def build_route_and_check_zoom_lvl(self, mode, count_zoom):
        self.calculate_route_for(mode)
        self.capture_screen()

        for _ in range(count_zoom):
            self.zoom_lvl(_)

    def zoom_lvl(self, num):
        self.zoom_in_at_maneuver(num)
        self.wait(30000)
        self.capture_screen()

    @py_xml_wrapper
    def test_7338(self):
        self.description({"description": "Truck Routing - Multiple route",
                          "edition": ["PremiumSDK", "IOSSupported", "NotRunInIOS"],
                          "platform": "mapFragment - offline - cached - ejl",
                          "priority": "LKWPriority"})

        self.open_screen("Routing")
        self.set_carto_poi("Off")
        self.add_coordinate(52.525431, 13.387377)
        self.add_coordinate(52.51624, 13.37924)

        self.calculate_drive_truck_route(10)
        self.calculate_drive_truck_route(1)

    def calculate_drive_truck_route(self, count):
        self.wait(10000)
        self.set_route_count(count)

        self.calculate_route_for("Drive")
        self.capture_screen()

        self.calculate_route_for("Truck")
        self.capture_screen()

    @py_xml_wrapper
    def test_7340(self):
        self.description({"description": "Online - Truck Routing - Abnormal Loads",
                          "edition": ["PremiumSDK", "IOSSupported", "NotRunInIOS"],
                          "platform": "mapFragment - offline - cached - ejl",
                          "priority": "LKWPriority"})

        self.open_screen("Routing")
        self.set_carto_poi("Off")
        self.add_coordinate(42.36533, -71.06217)
        self.add_coordinate(42.37143, -71.0280)

        self.calculate_route_for("Drive")
        self.capture_screen()

        self.calculate_route_for("Truck")
        self.capture_screen()

        self.set_truck("height", 10)
        self.set_truck("width", 10)
        self.set_truck("length", 10)

        self.calculate_route_for("Truck")
        self.capture_screen()

        self.calculate_route_for("Drive")
        self.capture_screen()
