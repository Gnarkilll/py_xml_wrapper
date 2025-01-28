from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class MapBuildingGroup(BaseTestCase):

    @py_xml_wrapper
    def test_6927(self):
        self.description({"description": "Map Building Group",
                          "platform": ["mapFragment_-_online_-_truck.night_-_Globe"],
                          "priority": "HighPriority"})

        self.open_screen("Mapping")
        self.set_center(49.277, -123.1133, 16.8, value6=70,
                        index="Screenshot #1 Vancouver Extruded buildings on by default")
        self.create_empty_building_group("OUTLINE")
        self.wait_and_capture(1000, "Screenshot #2 Map Building Group -  ViewPort OutLine Color")
        self.remove_by_viewport()

        self.create_set_color_group("HIGHLIGHT", "ROOF")
        self.single_tap("x2,y2", "Screenshot #3 Map Building Group - 1 building selected")

        self.set_map_scheme("reduced.day")
        self.set_center(40.748433, -73.985656, 17, value6=70,
                        index="Screenshot #4 Manhattan Extruded buildings on by default")
        self.create_empty_building_group("WALLTOP")
        self.wait_and_capture(1000, "Screenshot #5 Map Building Group - WALLTOP Color Viewport")
        self.remove_by_viewport()

        self.create_set_color_group("HIGHLIGHT3", "WALLBOTTOM")
        self.single_tap("x2,y2", "Screenshot #6 Map Building Group WALLBOTTOM -  1 building selected")

        self.set_center(48.858222, 2.2945, 17.5, value6=55,
                        index="Screenshot #7 Paris Extruded buildings on by default")
        self.set_map_scheme("hybrid.truck.day")

        self.create_empty_building_group("LANDMARKS")
        self.wait_and_capture(1000, "Screenshot #8 Map Building Group - LANDMARKS Color Viewport")
