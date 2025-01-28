from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class MapSelect(BaseTestCase):
    @py_xml_wrapper
    def test_7402(self):
        self.description({"description": "H-NMA - online - public transport info - Hybrid, map "
                                         ", map night view - transit layer - everything - search POI",
                          "platform": ["mapFragment_-_online_-_truck.day_-_Mercator"],
                          "priority": "HighPriority"})

        self.open_screen("Mapping")
        self.set_map_scheme("normal.day.transit")
        self.set_center(50.4745, 30.50406, 16.8)

        self.wait_and_capture(index="Screenshot #1 Kyiv Tarasa Shevchenka Metro Stop")

        self.open_list_objects()
        self.capture_screen("Screenshot #2 Selected objects list")
        self.select_objects_details("TRANSIT_STOP")
        self.capture_screen("Screenshot #3 Object details - first level hierarchy")
        self.select_objects_details("TransitStopInfo")
        self.capture_screen("Screenshot #4 Object details - second level hierarchy")
        self.press_back(3)

        self.set_center(49.2616, -123.0982, 20)

        self.wait_and_capture(index="Screenshot #5 Vancouver Mount Pleasant")
        self.open_list_objects()
        self.capture_screen("Screenshot #6 Selected objects list")
        self.select_objects_details("MAP_CARTO_MARKER")
        self.capture_screen("Screenshot #7 Object details - First level hierarchy")

        self.select_objects_details("Location")
        self.capture_screen("Screenshot #8 Object details - Second level hierarchy")

        self.select_objects_details("LocationInfo")
        self.capture_screen("Screenshot #9 Object details - Third level hierarchy")
        self.press_back(3)

        self.set_map_scheme("normal.night.transit")
        self.set_center(50.4510, 30.4445, 18)

        self.wait_and_capture(index="Screenshot #10 Kyiv bus stop - Bus line is not highlighted");
        self.select_by_viewport()
        self.capture_screen("Screenshot #11 Kyiv bus stop - Bus line is highlighted")

        self.clear_transit_highlights()
        self.capture_screen("Screenshot #12 Kyiv bus stop - Bus line is not highlighted")

        self.set_map_scheme("hybrid.night.transit")
        self.set_center(51.5325, -0.1, 11.5)
        self.wait_and_capture(index="Screenshot #13 London ZL 11.5 All transit markers should be shown")




