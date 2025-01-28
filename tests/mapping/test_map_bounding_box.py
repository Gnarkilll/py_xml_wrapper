from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class MapBoundingBox(BaseTestCase):

    @py_xml_wrapper
    def test_6949(self):
        self.description({"description": "map, Hybrid, Satellite and Terrain view, pos Lat, pos long",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - online - normal.day - Globe - Landscape"
                                       "mapFragment - offline - normal.day - Globe"
                                       "mapFragment - online - normal.day - Mercator"]})

        self.perform_test_action(63.391522, 126.5625)

    @py_xml_wrapper
    def test_6950(self):
        self.description({"description": "map, Hybrid , Satellite and Terrain view, pos Lat, neg long",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - offline - normal.day - Globe"
                                       "mapFragment - online - normal.day - Globe - Landscape"
                                       "mapFragment - online - normal.day - Mercator",
                                       "mapView - online - normal.day - Globe",
                                       "mapView - offline - normal.day - Globe"]})

        self.perform_test_action(49.255257, -123.063354, 325)

    @py_xml_wrapper
    def test_6951(self):
        self.description({"description": "map, Hybrid, Satellite and Terrain view, neg Lat, neg long",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - offline - normal.day - Globe",]})

        self.perform_test_action(-18.646245, -65.390625)

    @py_xml_wrapper
    def test_6952(self):
        self.description({"description": "map, Hybrid, Satellite and Terrain view, neg Lat, pos long",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - online - normal.day - Globe",
                                       "mapFragment - offline - normal.day - Globe", ]})

        self.perform_test_action(-27.683528, 141.679688)

    def perform_test_action(self, lat, long, specific_param=375):
        self.open_screen("Mapping")
        self.set_carto_poi("Off")
        self.set_center_default_null(value1=lat, value2=long, value3="NONE")
        self.set_map_center_for_local_test(index="CartoPOI all off, {}, {}, Zoom 11".format(lat, long), value4=11.0)

        self.set_map_bounding_box("On", "MapBoundingBox On")

        self.pinch_close_zoom_out("x4,y3", "x0,y0", "pinchCloseZoomOut x4,y3, x0,y0")
        self.two_finger_tilt("x2,y2", "x0,y1", "twoFingerTilt x2,y2, x0,y1")

        self.set_map_center_for_local_test(index="Orientation 45", value5=45)
        self.set_map_center_for_local_test(index="Tilt 0", value6=0)
        self.set_map_center_for_local_test(index="Orientation 45", value5=45)

        self.pinch_close_zoom_out("x4,y3", "x0,y0", "pinchCloseZoomOut x4,y3, x0,y0")

        values = [75, 125, 225, specific_param, 360]
        for value in values:
            self.set_map_center_for_local_test(index="Orientation {}".format(value), value5=value)

        self.set_center_default_null(value5=45)

        self.set_map_center_for_local_test(index="Orientation 45, Tilt 45", value6=45)
        self.set_map_bounding_box("Off", "MapBoundingBox Off")

        self.set_map_center_for_local_test(value4=0)
        self.set_map_bounding_box("On", "Zoom 0, MapBoundingBox On")

        self.set_map_center_for_local_test(index="Orientation 225",value5=225)

    def set_map_center_for_local_test(self, index=None, **value):
        self.set_center_default_null(**value)
        self.wait(3000)
        self.capture_screen(index=index)
