from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class MapUniv(BaseTestCase):

    @py_xml_wrapper
    def test_6720(self):
        self.description({"description": "ChangeView - Change view between all available map scheme",
                          "edition": ["StarterSDK", "PremiumSDK", "IOSSupported"],
                          "platform": "mapFragment - online - normal.day - Globe",
                          "priority": "HighPriority"})
        
        self.open_screen("Mapping")
        self.wait(8000)
        self.set_center_by_place_name_with_null_default("VANCOUVER")
        
        schemes = ["normal.night", "terrain.day", "satellite.day", "satellite.night", "hybrid.day", "hybrid.night",
                   "pedestrian.day", "pedestrian.night", "pedestrian.day.hybrid", "pedestrian.night.hybrid",
                   "normal.day.grey", "normal.night.grey", "hybrid.grey.day", "hybrid.grey.night",
                   "normal.traffic.day", "normal.traffic.night", "hybrid.traffic.day", "hybrid.traffic.night",
                   "normal.day.transit", "normal.night.transit", "hybrid.day.transit", "hybrid.night.transit",
                   "reduced.day", "reduced.night", "hybrid.reduced.day", "hybrid.reduced.night", "carnav.day",
                   "carnav.night", "carnav.hybrid.day", "carnav.hybrid.night", "carnav.traffic.day",
                   "carnav.traffic.night", "carnav.traffic.hybrid.day", "carnav.traffic.hybrid.night", "maneuver.day",
                   "truck.day", "truck.night", "hybrid.truck.day", "hybrid.truck.night", "carnav.day.grey",
                   "carnav.night.grey", "normal.day"]

        counter = 1
        for scheme in schemes:
            self.set_map_scheme(scheme)
            self.wait_and_capture(index="#{} set map schema to {}".format(counter, scheme))
            counter += 1

