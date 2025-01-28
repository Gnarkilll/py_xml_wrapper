from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class Search(BaseTestCase):
    pass


class TilesRequest(Search):

    @py_xml_wrapper
    def test_6717(self):
        self.description({"description": "Internal-Tiles Request - Search area - view port",
                          "platform": ["mapView - Online"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Tiles Request")
        self.step("Search", "execute", value1=None)
        self.capture_screen(3000, index="Screenshot #1 Get Tiles Req with empty arguments - error pop up is expected")

        self.press_back()
        self.step("Search", "getResultsByTilesReq", value1="37.8fd306, -122.4gf684",
                  value2="37.7458, -122.3926", value3="facilities")
        self.capture_screen(3000, index="Screenshot #2 Get Tiles Req with letters in coordinates - error is expected")

        self.step("Search", "getResultsByTilesReq", value1="370.8306, -1422.4684",
                  value2="37.7458, -122.3926", value3="facilities")
        self.capture_screen(3000, index="Screenshot #3 Get Tiles Req with out of range coordinates - error is expected")

        self.press_back()
        self.step("Search", "getResultsByTilesReq", value1="37.8104, -122.4455",
                  value2="37.7458, -122.3926", value3="facilities")
        self.capture_screen(3000, index="Screenshot #4 Get Tiles Req with zoom level 12 - no any errors are expected")

        self.press_back()
        self.step("Search", "getResultsByTilesReq", value1="37.7759, -122.4203",
                  value2="37.774, -122.4187", value3="facilities")
        self.capture_screen(3000, index="Screenshot #5 Get Tiles Req with zoom level 18 - no any errors are expected")

    @py_xml_wrapper
    def test_6716(self):
        self.description({"description": "Tiles Request - Collection Size",
                          "platform": ["mapFragment - Online"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Tiles Request")
        self.step("Search", "addCollectionSize", value1="0")
        self.step("Search", "getResultsByTilesReq", value1="37.8104, -122.4455",
                  value2="37.7458, -122.3926", value3="facilities")
        self.capture_screen(3000, index="Screenshot #1 Get Tiles Req Collection size 0 - warning expected")

        self.step("Search", "addCollectionSize", value1="200")
        self.step("Search", "getResultsByTilesReq", value1="37.8104, -122.4455",
                  value2="37.7458, -122.3926", value3="facilities")
        self.capture_screen(3000, index="Screenshot #2 Get Tiles Req Collection size 200 - warning expected")

        self.step("Search", "addCollectionSize", value1="9876543210")
        self.step("Search", "getResultsByTilesReq", value1="37.8104, -122.4455",
                  value2="37.7458, -122.3926", value3="facilities")
        self.capture_screen(3000, index="Screenshot #3 Get Tiles Req Collection size 9876543210 - warning expected")

        self.step("Search", "addCollectionSize", value1="3")
        self.step("Search", "getResultsByTilesReq", value1="37.8104, -122.4455",
                  value2="37.7458, -122.3926", value3="facilities")
        self.capture_screen(3000, index="Screenshot #4 Get Tiles Req Collection size 3 ")
        self.step("Search", "showMap", value1=None)
        self.capture_screen(3000, index="Screenshot #5 Show Search results on map")
        self.two_finger_tap_zoom_out("900,1500", "900,1400",
                                     "Screenshot #6 two finger tap zoom out from 900,1500 to 900,1400")
        self.wait(3000)
        self.two_finger_tap_zoom_out("900,1500", "900,1400",
                                     "Screenshot #7 two finger tap zoom out from 900,1500 to 900,1400")

        self.wait(3000)
        self.two_finger_tap_zoom_out("900,1500", "900,1400",
                                     "Screenshot #8 two finger tap zoom out from 900,1500 to 900,1400")

        self.wait(3000)
        self.two_finger_tap_zoom_out("900,1500", "900,1400",
                                     "Screenshot #9 two finger tap zoom out from 900,1500 to 900,1400")

        self.wait(3000)
        self.two_finger_tap_zoom_out("900,1500", "900,1400",
                                     "Screenshot #10 two finger tap zoom out, Bad request expected")

    @py_xml_wrapper
    def test_6715(self):
        self.description({"description": "Tile Request - Search in Urban Area -"
                                         " Category Facilities - Plain format - add reference",
                          "platform": ["mapFragment - Online"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Tiles Request")
        self.step("Search", "getResultsByTilesReq", value1="37.8104, -122.4455",
                  value2="37.7458, -122.3926", value3="facilities")
        self.capture_screen(3000, index="Screenshot #1 Get Tiles Req filter facilities in San Francisco")

        self.press_back()
        self.step("Search", "getResultsByTilesReq", value1="37.8104, -122.4455",
                  value2="37.7458, -122.3926", value3="facilities", value4="Hospital or Healthcare Facility")
        self.capture_screen(3000,
                            index="Screenshot #2 Get Tiles results for filter Hospital or Healthcare in San Francisco")
        self.step("Search", "showMap", value1=None)
        self.capture_screen(3000, index="Screenshot #3 Show Search results on map")

        self.press_back(2)
        self.step("Search", "addReference", value1="PVID")
        self.step("Search", "getResultsByTilesReq", value1="37.8104, -122.4455",
                  value2="37.7458, -122.3926", value3="facilities", value4="Hospital or Healthcare Facility")
        self.step("Search", "performLookUpRequestByReference", value1="No")
        self.capture_screen(3000,
                            index="Screenshot #4 Add PVID reference and NO perform LookUp request ")

        self.press_back(2)
        self.step("Search", "addReference", value1="PVID")
        self.step("Search", "getResultsByTilesReq", value1="37.8104, -122.4455",
                  value2="37.7458, -122.3926", value3="accommodation", value4="Hotel")
        self.step("Search", "performLookUpRequestByReference", value1="Yes")
        self.capture_screen(3000,
                            index="Screenshot #5 Add PVID reference and YES perform LookUp request ")

        self.press_back(2)

        self.step("Search", "addFreeReference", value1="Wrong id Bla Bla")
        self.step("Search", "getResultsByTilesReq", value1="37.8104, -122.4455",
                  value2="37.7458, -122.3926", value3="facilities", value4="Hospital or Healthcare Facility")
        self.capture_screen(3000,
                            index="Screenshot #6 Negative case: Add Wrong id reference. BAD_REQUEST expected ")

    @py_xml_wrapper
    def test_7260(self):
        self.description({"description": "Tile Request - Search in Urban Area - Category Transport",
                          "platform": ["mapFragment - Online"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Tiles Request")
        self.step("Search", "getResultsByTilesReq", value1="49.2984, -123.139",
                  value2="49.2716, -123.1124", value3="transport")
        self.capture_screen(3000, index="Screenshot #1 Get Tiles Req filter transport  in Vancouver")

        self.press_back()
        self.step("Search", "getResultsByTilesReq", value1="49.2984, -123.139",
                  value2="49.2716, -123.1124", value3="transport", value4="Railway Station")
        self.capture_screen(3000,
                            index="Screenshot #2 Get Tiles results for filter Railway Station in Vancouver")

    @py_xml_wrapper
    def test_7261(self):
        self.description({"description": "Tile Request - Search in Urban Area - Category Sights-Museums",
                          "platform": ["mapFragment - Online"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Tiles Request")
        self.step("Search", "getResultsByTilesReq", value1="52.5473, 13.3474",
                  value2="52.4968, 13.4011", value3="sights-museums")
        self.capture_screen(3000, index="Screenshot #1 Get Tiles Request results for sights-museums in Berlin")

        self.press_back()
        self.step("Search", "getResultsByTilesReq", value1="52.5473, 13.3474",
                  value2="52.4968, 13.4011", value3="sights-museums", value4="Landmark/Attraction")
        self.capture_screen(3000,
                            index="Screenshot #2 Get Tiles Req results for Landmark/Attraction  Berlin")

    @py_xml_wrapper
    def test_7262(self):
        self.description({"description": "Internal-Tile Request - Search in Urban Area - Category Shopping",
                          "platform": ["mapFragment - Online"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Tiles Request")
        self.step("Search", "getResultsByTilesReq", value1="50.4812, 30.5014",
                  value2="50.457, 30.526", value3="shopping")
        self.capture_screen(3000, index="Screenshot #1 Get Tiles Req filter Shopping  in Kyiv")

        self.press_back()
        self.step("Search", "getResultsByTilesReq", value1="50.4812, 30.5014",
                  value2="50.457, 30.526", value3="shopping", value4="Pharmacy")
        self.capture_screen(3000,
                            index="Screenshot #2 Get Tiles results for filter Shopping  - Pharmacy in Kyiv")

    @py_xml_wrapper
    def test_7263(self):
        self.description({"description": "Tile Request - Search in Urban Area - Category Natural Geographical",
                          "platform": ["mapFragment - Online"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Tiles Request")
        self.step("Search", "getResultsByTilesReq", value1="52.5473, 13.3474",
                  value2="52.4968, 13.4011", value3="natural-geographical")
        self.capture_screen(3000, index="Screenshot #1 Get Tiles Request results for natural-geographical in Berlin")

        self.press_back()
        self.step("Search", "getResultsByTilesReq", value1="52.5473, 13.3474",
                  value2="52.4968, 13.4011", value3="natural-geographical", value4="Body of Water")
        self.capture_screen(3000,
                            index="Screenshot #2 Get Tiles Req results for natural-geographical - Body of Water Berlin")

    @py_xml_wrapper
    def test_7264(self):
        self.description({"description": "Tile Request - Search in Urban Area - Category Leisure",
                          "platform": ["mapFragment - Online"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Tiles Request")
        self.step("Search", "getResultsByTilesReq", value1="52.5473, 13.3474",
                  value2="52.4968, 13.4011", value3="leisure-outdoor")
        self.capture_screen(3000, index="Screenshot #1 Get Tiles Request results for filter leisure-outdoor in Berlin")

        self.press_back()
        self.step("Search", "getResultsByTilesReq", value1="52.5473, 13.3474",
                  value2="52.4968, 13.4011", value3="leisure-outdoor", value4="Theme Park")
        self.capture_screen(3000,
                            index="Screenshot #2 Get Tiles Req results for leisure-outdoor - Theme Park in Berlin")

    @py_xml_wrapper
    def test_7265(self):
        self.description({"description": "Tile Request - Search in Urban Area - Category GoingOut",
                          "platform": ["mapFragment - Online"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Tiles Request")
        self.step("Search", "getResultsByTilesReq", value1="49.2984, -123.139",
                  value2="49.2716, -123.1124", value3="going-out")
        self.capture_screen(3000, index="Screenshot #1 Get Tiles Req filter GoingOut  in Vancouver")

        self.press_back()
        self.step("Search", "getResultsByTilesReq", value1="49.2984, -123.139",
                  value2="49.2716, -123.1124", value3="going-out", value4="Dance or Nightclub")
        self.capture_screen(3000,
                            index="Screenshot #2 Get Tiles results for filter GoingOut  - Nightclub in Vancouver")

    @py_xml_wrapper
    def test_7266(self):
        self.description({"description": "Internal-Tile Request - Search in Urban Area - Category Eat/Drink",
                          "platform": ["mapFragment - Online"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Tiles Request")
        self.step("Search", "getResultsByTilesReq", value1="50.4812, 30.5014",
                  value2="50.457, 30.526", value3="eat-drink")
        self.capture_screen(3000, index="Screenshot #1 Get Tiles Req filter Eat/Drink  in Kyiv")

        self.press_back()
        self.step("Search", "getResultsByTilesReq", value1="50.4812, 30.5014",
                  value2="50.457, 30.526", value3="eat-drink", value4="Bar/Pub")
        self.capture_screen(3000,
                            index="Screenshot #2 Get Tiles results for filter Eat/Drink  - Bar/Pub in Kyiv")

    @py_xml_wrapper
    def test_7267(self):
        self.description({"description": "Tile Request - Search in Urban Area - Category Business Services",
                          "platform": ["mapFragment - Online"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Tiles Request")
        self.step("Search", "getResultsByTilesReq", value1="49.2984, -123.139",
                  value2="49.2716, -123.1124", value3="business-services")
        self.capture_screen(3000, index="Screenshot #1 Get Tiles Req filter Business Services  in Vancouver")

        self.press_back()
        self.step("Search", "getResultsByTilesReq", value1="49.2984, -123.139",
                  value2="49.2716, -123.1124", value3="business-services", value4="Post Office")
        self.capture_screen(3000,
                            index="Screenshot #2 Get Tiles results for filter  Business - Post Office in Vancouver")

    @py_xml_wrapper
    def test_7268(self):
        self.description({"description": "Tile Request - Search in Urban Area - Category Administrative-area buildings",
                          "platform": ["mapFragment - Online"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Tiles Request")
        self.step("Search", "getResultsByTilesReq", value1="49.2984, -123.139",
                  value2="49.2716, -123.1124", value3="administrative-areas-buildings")
        self.capture_screen(3000, index="Screenshot #1 Get Tiles Req filter Administrative  in Vancouver")

        self.press_back()
        self.step("Search", "getResultsByTilesReq", value1="49.2984, -123.139",
                  value2="49.2716, -123.1124", value3="administrative-areas-buildings", value4="Building")
        self.capture_screen(3000,
                            index="Screenshot #2 Get Tiles results for filter  Administrative -Building  in Vancouver")

    @py_xml_wrapper
    def test_7269(self):
        self.description({"description": "Tile Request - Search in Urban Area - Category Accommodations",
                          "platform": ["mapFragment - Online"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Tiles Request")
        self.step("Search", "getResultsByTilesReq", value1="52.5473, 13.3474",
                  value2="52.4968, 13.4011", value3="accommodation")
        self.capture_screen(3000, index="Screenshot #1 Get Tiles Request results for filter accommodation in Berlin")

        self.press_back()
        self.step("Search", "getResultsByTilesReq", value1="52.5473, 13.3474",
                  value2="52.4968, 13.4011", value3="accommodation", value4="Camping")
        self.capture_screen(3000,
                            index="Screenshot #2 Get Tiles Request results for filter accommodation - Camping in Berlin")


class SearchRequest(Search):

    @py_xml_wrapper
    def test_7296(self):
        self.description({"description": "Chinese Traditional Localization Offline search with specific query word",
                          "platform": ["mapFragment - Online", "mapFragment - Offline"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Search Request")
        self.step("Search", "getResultsBySearchReq", value1="25.066667", value2="121.516667", value3="西門")
        self.capture_screen(3000, index="Screenshot #1 Get Search result for 西門 in Taiwan")

        self.force_stop_app("com.here.functionaltestv2")
        self.wait(1000)
        self.open_screen("Search")
        self.step("Search", "openSearchReq", value1="Search Request")
        self.step("Search", "getResultsBySearchReq", value1="25.066667", value2="121.516667", value3="西門")
        self.capture_screen(3000, index="Screenshot #2 Get Search result for 西門 in Taiwan after app reload")

        self.press_back()
        self.step("Search", "getResultsBySearchReq", value1="25.066667", value2="121.516667", value3="台中市大甲區中山路1段1136號")
        self.capture_screen(3000, index="Screenshot #3 Get Search result for 台中市大甲區中山路1段1136號 in Taiwan")

    @py_xml_wrapper
    def test_7784(self):
        self.description({"description": "Search - Locale language",
                          "platform": ["mapFragment - Online"]})

        self.open_screen("Search")
        self.wait(1000)

        # Search Request

        self.step("Search", "openSearchReq", value1="Search Request")
        self.step("Search", "setLocale", value1="uk-UA")
        self.step("Search", "getResultsBySearchReq", value1="50.4675", value2="30.514", value3="hotel")
        self.capture_screen(3000, index="Screenshot #1 Get Search result for uk-UA  locale (Kyiv)")

        self.press_back()
        self.step("Search", "setLocale", value1="de-DE")
        self.step("Search", "getResultsBySearchReq", value1="52.5167", value2="13.389", value3="hotel")
        self.capture_screen(3000, index="Screenshot #2 Get Search result for de-DE  locale (Berlin)")

        self.press_back()
        self.step("Search", "setLocale", value1="fr-FR")
        self.step("Search", "getResultsBySearchReq", value1="48.8567", value2="2.3508", value3="hotel")
        self.capture_screen(3000, index="Screenshot #3 Get Search result for fr-FR  locale (Paris)")

        self.press_back()
        self.step("Search", "setLocale", value1="zh-CN")
        self.step("Search", "getResultsBySearchReq", value1="22.2796", value2="114.1716", value3="hotel")
        self.capture_screen(3000, index="Screenshot #4 Get Search result for zh-CH  locale (Hong Kong)")

        # Text Auto Suggestion Request

        self.press_back(2)
        self.step("Search", "openSearchReq", value1="Text Auto Suggestion Request")
        self.step("Search", "setLocale", value1="uk-UA")
        self.step("Search", "getResultsByTextSearchReq", value1="50.4675", value2="30.514", value3="cafe")
        self.capture_screen(3000, index="Screenshot #5 Text Auto Suggestion Request for uk-UA  locale (Kyiv)")

        self.press_back()
        self.step("Search", "setLocale", value1="de-DE")
        self.step("Search", "getResultsByTextSearchReq", value1="52.5167", value2="13.389", value3="cafe")
        self.capture_screen(3000, index="Screenshot #6 Text Auto Suggestion Request for de-DE  locale (Berlin)")

        self.press_back()
        self.step("Search", "setLocale", value1="fr-FR")
        self.step("Search", "getResultsByTextSearchReq", value1="48.8567", value2="2.3508", value3="cafe")
        self.capture_screen(3000, index="Screenshot #7 Text Auto Suggestion Request for fr-FR  locale (Paris)")

        self.press_back()
        self.step("Search", "setLocale", value1="zh-CN")
        self.step("Search", "getResultsByTextSearchReq", value1="22.2796", value2="114.1716", value3="cafe")
        self.capture_screen(3000, index="Screenshot #8 Text Auto Suggestion Request for zh-CH  locale (Hong Kong)")

        # Text Around Request

        self.press_back(2)
        self.step("Search", "openSearchReq", value1="Around Request")
        self.step("Search", "setLocale", value1="uk-UA")
        self.step("Search", "getResultsByAroundReq", value1="50.4675", value2="30.514", value3="shopping")
        self.capture_screen(3000, index="Screenshot #9 Get Around Request result for uk-UA  locale (Kyiv)")

        self.press_back()
        self.step("Search", "setLocale", value1="de-DE")
        self.step("Search", "getResultsByAroundReq", value1="52.5167", value2="13.389", value3="shopping")
        self.capture_screen(3000, index="Screenshot #10 Get Around Request result for de-DE  locale (Berlin)")

        self.press_back()
        self.step("Search", "setLocale", value1="fr-FR")
        self.step("Search", "getResultsByAroundReq", value1="48.8567", value2="2.3508", value3="shopping")
        self.capture_screen(3000, index="Screenshot #11 Get Around Request result for fr-FR  locale (Paris)")

        self.press_back()
        self.step("Search", "setLocale", value1="zh-CN")
        self.step("Search", "getResultsByAroundReq", value1="22.2796", value2="114.1716", value3="shopping")
        self.capture_screen(3000, index="Screenshot #12 Get Around Request result for zh-CN  locale (Hong Kong)")


class AroundRequest(Search):

    @py_xml_wrapper
    def test_5990(self):
        self.description({"description": "Around Request---Category Transport",
                          "edition": ["StarterSDK", "PremiumSDK"]})

        self.open_screen("Search")
        self.wait(1000)
        self.step("Search", "openSearchReq", value1="Around Request")
        self.step("Search", "getImageByAroundReq", value1="49.1933", value2="-123.1723", value3="transport")
        self.capture_screen(5000)
        self.wait(3000)


class CategoryList(Search):

    @py_xml_wrapper
    def test_7249(self):
        self.description({"description": "Category List---EAT_DRINK",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - Offline", "mapFragment - Online"]})

        self.top_cat = "Eat & Drink"
        self.select_main_category(self.top_cat)

        self.select_sub_category(1, 2, "Restaurant")
        self.select_sub_category(2, 3, "Snacks/Fast food")
        self.select_sub_category(2, 4, "Bar/Pub")
        self.select_sub_category(2, 5, "Coffee/Tea")
        self.select_sub_category(2, 6, "Coffee/Tea", "Coffee")
        self.select_sub_category(3, 7, "Coffee/Tea", "Tea")

        self.go_back_root_category(3)

    @py_xml_wrapper
    def test_7250(self):
        self.description({"description": "Category List---TRANSPORT",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - Offline", "mapFragment - Online",
                                       "mapview - Online", "mapview - Offline"]})

        self.top_cat = "Transport"
        self.select_main_category(self.top_cat)

        self.select_sub_category(1, 2, "Airport")
        self.select_sub_category(2, 3, "Railway Station")
        self.select_sub_category(2, 4, "Public Transit")
        self.select_sub_category(2, 5, "Ferry Terminal")
        self.select_sub_category(2, 6, "Taxi Stand")

        self.go_back_root_category(2)

    @py_xml_wrapper
    def test_7251(self):
        self.description({"description": "Category List---SIGHTS_MUSEUMS",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - Offline", "mapFragment - Online"]})

        self.top_cat = "Sights & Museums"
        self.select_main_category(self.top_cat)

        self.select_sub_category(1, 2, "Landmark/Attraction")
        self.select_sub_category(2, 3, "Museum")

        self.go_back_root_category(2)

    @py_xml_wrapper
    def test_7252(self):
        self.description({"description": "Category List---SHOPPING",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - Offline", "mapFragment - Online"],
                          "priority": "HighPriority"})

        self.top_cat = "Shopping"
        self.select_main_category(self.top_cat)

        self.select_sub_category(1, 2, "24-7/Convenience Store")
        self.select_sub_category(2, 3, "24-7/Convenience Store", "Wine & Spirits")
        self.select_sub_category(3, 4, "Shopping Center")
        self.select_sub_category(2, 5, "Department Store")
        self.select_sub_category(2, 6, "Book Shop")
        self.select_sub_category(2, 7, "Pharmacy")
        self.select_sub_category(2, 8, "Electronics")
        self.select_sub_category(2, 9, "DIY/garden center")
        self.select_sub_category(2, 10, "Outdoor Sports")
        self.select_sub_category(2, 11, "Store")
        self.select_sub_category(2, 12, "Food & Drink")
        self.select_sub_category(2, 13, "Clothing & Accessories")

        self.go_back_root_category(2)

    @py_xml_wrapper
    def test_7253(self):
        self.description({"description": "Category List---NATURAL_GEOGRAPHICAL",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - Offline", "mapFragment - Online"]})

        self.top_cat = "Natural or Geographical"
        self.select_main_category(self.top_cat)

        self.select_sub_category(1, 2, "Body of Water")
        self.select_sub_category(2, 3, "Mountain or Hill")
        self.select_sub_category(2, 4, "Underwater Feature")
        self.select_sub_category(2, 5, "Forest, Heath or Other Vegetation")

        self.go_back_root_category(2)

    @py_xml_wrapper
    def test_7254(self):
        self.description({"description": "Category List---LEISURE_OUTDOOR",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - Offline", "mapFragment - Online"],
                          "priority": "HighPriority"})

        self.top_cat = "Leisure & Outdoor"
        self.select_main_category(self.top_cat)

        self.select_sub_category(1, 2, "Recreation")
        self.select_sub_category(2, 3, "Theme Park")
        self.select_sub_category(2, 4, "Theme Park", "Zoo")

        self.go_back_root_category(3)

    @py_xml_wrapper
    def test_7255(self):
        self.description({"description": "Category List---GOING_OUT",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - Offline", "mapFragment - Online"]})

        self.top_cat = "Going Out"
        self.select_main_category(self.top_cat)

        self.select_sub_category(1, 2, "Dance or Nightclub")
        self.select_sub_category(2, 3, "Cinema")
        self.select_sub_category(2, 4, "Theater, Music & Culture")
        self.select_sub_category(2, 5, "Casino")

        self.go_back_root_category(2)

    @py_xml_wrapper
    def test_7256(self):
        self.description({"description": "Category List---FACILITIES",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - Offline", "mapFragment - Online"]})

        self.top_cat = "Facilities"
        self.select_main_category(self.top_cat)

        self.select_sub_category(1, 2, "Hospital or Healthcare Facility")
        self.select_sub_category(2, 3, "Hospital or Healthcare Facility", "Hospital")
        self.select_sub_category(3, 4, "Government or Community Facility")
        self.select_sub_category(2, 5, "Educational Facility")
        self.select_sub_category(2, 6, "Library")
        self.select_sub_category(2, 7, "Expo & Convention Facility")
        self.select_sub_category(2, 8, "Parking Facility")
        self.select_sub_category(2, 9, "Public Bathroom/Rest Area")
        self.select_sub_category(2, 10, "Sport Facility/Venue")
        self.select_sub_category(2, 11, "Facility")
        self.select_sub_category(2, 12, "Religious Place")

        self.go_back_root_category(2)

    @py_xml_wrapper
    def test_7257(self):
        self.description({"description": "Category List---BUSINESS_SERVICES",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - Offline", "mapFragment - Online"]})

        self.top_cat = "Business & Services"
        self.select_main_category(self.top_cat)

        self.select_sub_category(1, 2, "ATM/Bank/Exchange")
        self.select_sub_category(2, 3, "Police/Emergency")
        self.select_sub_category(2, 4, "Police/Emergency", "Ambulance Services")
        self.select_sub_category(3, 5, "Police/Emergency", "Fire Department")
        self.select_sub_category(3, 6, "Police/Emergency", "Police Station")
        self.select_sub_category(3, 7, "Post Office")
        self.select_sub_category(2, 8, "Tourist Information")
        self.select_sub_category(2, 9, "Fuel Station")
        self.select_sub_category(2, 10, "EV Charging Station")
        self.select_sub_category(2, 11, "Car Rental")
        self.select_sub_category(2, 12, "Car Dealer/Repair")
        self.select_sub_category(2, 14, "Communications/Media")
        self.select_sub_category(2, 15, "Business/Industry")
        self.select_sub_category(2, 16, "Service")

        self.go_back_root_category(2)

    @py_xml_wrapper
    def test_7258(self):
        self.description({"description": "Category List---ADMINISTRATIVE_AREAS_BUILDINGS",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - Offline", "mapFragment - Online"]})

        self.top_cat = "Administrative Areas/Buildings"
        self.select_main_category(self.top_cat)

        self.select_sub_category(1, 2, "Administrative Region")
        self.select_sub_category(2, 3, "City, Town or Village")
        self.select_sub_category(2, 4, "Outdoor Area/Complex")
        self.select_sub_category(2, 5, "Building")
        self.select_sub_category(2, 6, "Street or Square")
        self.select_sub_category(2, 7, "Postal Area")

        self.go_back_root_category(2)

    @py_xml_wrapper
    def test_7259(self):
        self.description({"description": "Category List---ACCOMMODATION",
                          "edition": ["StarterSDK", "PremiumSDK"],
                          "platform": ["mapFragment - Offline", "mapFragment - Online"]})

        self.top_cat = "Accommodation"
        self.select_main_category(self.top_cat)

        self.select_sub_category(1, 2, "Camping")
        self.select_sub_category(2, 3, "Hostel")
        self.select_sub_category(2, 4, "Motel")
        self.select_sub_category(2, 5, "Hotel")

        self.go_back_root_category(2)

    def select_main_category(self, cat):
        self.open_screen("Search")
        self.wait(1000)
        self.search_request("Category List")
        self.select_category_items(cat)
        self.wait(3000)
        self.capture_screen(index="#1 go to {}".format(cat))

    def select_sub_category(self, times, index, sub1_cat=None, sub2_cat=None):
        self.go_back_root_category(times)
        self.select_category_items(self.top_cat, sub1_cat, sub2_cat)
        self.wait(3000)
        if sub2_cat:
            self.capture_screen(index="#{} go to {}".format(index, sub2_cat))
        else:
            self.capture_screen(index="#{} go to {}".format(index, sub1_cat))
