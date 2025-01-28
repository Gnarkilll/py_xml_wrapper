from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class Navigation(BaseTestCase):
    @py_xml_wrapper
    def test_6981(self):
        self.description({"description": "Navigation - change route Traveled color during navigation",
                          "platform": "mapFragment - Online",
                          "priority": "HighPriority"})

        self.open_screen("Routing")
        self.add_coordinate(49.2824288, -123.1178713)
        self.add_coordinate(49.274921, -121.419503)
        self.calculate_route_for("Drive")
        self.wait(5000)
        self.capture_screen(index="Screenshot #1 Create Drive route")

        self.start_navigation("SIMULATION", 10)
        self.pan("x0,y0", "x1,y1", index="Screenshot #2 Pan the map from x0,y0 to x1,y1")

        self.set_map_route_colors("FFAA0000", "FF00AA00")
        self.capture_screen(index="Screenshot #3 Use color: Route color should be Red - traveled Green")

        self.set_map_route_render_type("SECONDARY")
        self.capture_screen(index="Screenshot #4 Use type: SECONDARY: Route color should be light blue - traveled Blue")

        self.cancel_current_guidance()

        self.calculate_route_for("Truck")
        self.wait(5000)
        self.capture_screen(index="Screenshot #5 Create Truck route")

        self.start_navigation("SIMULATION", 10)
        self.pan("x0,y0", "x1,y1", index="Screenshot #6 Pan the map from x0,y0 to x1,y1")

        self.set_map_route_colors("FF0000AA", "FFAAAA00")
        self.capture_screen(index="Screenshot #7 Use color: Route color should be Blue - traveled Yellow")

        self.set_map_route_render_type("PRIMARY")
        self.capture_screen(index="Screenshot #8 Use type: PRIMARY: Route color should be Blue - traveled Blue")

    @py_xml_wrapper
    def test_6639(self):
        self.description({"description": "navigation with north up",
                          "platform": "mapFragment - online - no map is downloaded - Auto",
                          "priority": "HighPriority"})

        self.open_screen("Routing")
        self.add_coordinate(50.459, 30.419)
        self.add_coordinate(50.442, 30.520)
        self.calculate_route_for("Drive")
        self.wait(5000)
        self.capture_screen(index="Screenshot #1 Create Drive route from West to East")

        self.start_navigation("SIMULATION", 10)
        self.pan("300,500", "1000,500", index="Screenshot #2 Pan the map left")

        self.set_road_view_setting("ROADVIEW", "NORTH_UP")
        self.wait_and_capture(1000, index="Screenshot #3 Set road view setting: RoadView mode and North-UP orientation")

        self.set_road_view_setting("ROADVIEW", "DYNAMIC")
        self.wait_and_capture(1000, index="Screenshot #4 Set road view setting: RoadView mode and Dynamic orientation")

    @py_xml_wrapper
    def test_6618(self):
        self.description({"description": "Scheme for walk navigation - drive navigation - PT",
                          "platform": ["mapView - online - no map is downloaded - Auto"],
                          "priority": "HighPriority"})
        self.open_screen("Routing")
        self.set_map_scheme("normal.day")
        self.add_coordinate(49.287, -123.135)
        self.add_coordinate(49.250, -122.981)
        self.calculate_route_for("Drive")
        self.wait(3000)
        self.capture_screen(index="Screenshot #1 normal.day Drive mode")

        self.start_navigation("SIMULATION", 10)
        self.pan("300,500", "1000,500", False)
        self.wait(3000)
        self.capture_screen(index="Screenshot #2 normal.day Navigation Drive mode")
        self.cancel_current_guidance()

        self.calculate_route_for("Truck")
        self.wait(1000)
        self.capture_screen(index="Screenshot #3 normal.day Truck mode")

        self.calculate_route_for("Scooter")
        self.wait(1000)
        self.capture_screen(index="Screenshot #4 normal.day Scooter mode")

        self.calculate_route_for("Walk")
        self.wait(1000)
        self.capture_screen(index="Screenshot #5 normal.day Walk mode")
        self.start_navigation("SIMULATION", 10)
        self.pan("300,500", "1000,500", False)
        self.wait(3000)
        self.capture_screen(index="Screenshot #6 normal.day Navigation Walk mode")
        self.cancel_current_guidance()

        self.calculate_route_for("Transit")
        self.wait(1000)
        self.capture_screen(index="Screenshot #7 normal.day Transit mode")

        self.set_map_scheme("terrain.day")
        self.calculate_route_for("Transit")
        self.wait(1000)
        self.capture_screen(index="Screenshot #8 terrain.dayTransit mode")

        self.set_map_scheme("hybrid.day")
        self.calculate_route_for("Scooter")
        self.wait(1000)
        self.capture_screen(index="Screenshot #9 hybrid.day Scooter mode")

        self.set_map_scheme("pedestrian.day")
        self.calculate_route_for("Walk")
        self.wait(1000)
        self.capture_screen(index="Screenshot #10 hybrid.day Walk mode")
        self.start_navigation("SIMULATION", 10)
        self.pan("300,500", "1000,500", False)
        self.wait(3000)
        self.capture_screen(index="Screenshot #11 hybrid.day Navigation Walk mode")
        self.cancel_current_guidance()

        self.set_map_scheme("carnav.day")
        self.calculate_route_for("Drive")
        self.wait(1000)
        self.capture_screen(index="Screenshot #12 carnav.day Drive mode")
        self.start_navigation("SIMULATION", 30)
        self.pan("300,500", "1000,500", False)
        self.wait(3000)
        self.capture_screen(index="Screenshot #13 carnav.day Navigation Drive mode")
        self.cancel_current_guidance()
