from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class DoubleMapping(BaseTestCase):

    @py_xml_wrapper
    def test_6898(self):
        self.description({"description": "multiple maps on screen at the same time",
                          "edition": ["PremiumSDK", "StarterSDK"],
                          "platform": ["mapFragment - Online", "mapFragment - Offline",
                                       "mapview - Online", "mapview - Offline"]})
        self.open_specific_screen("Double Mapping", 2)
        self.wait(3000)
        self.capture_screen(index="#1 open double mapping")

        self.double_tap_zoom_in("300,300", "#2 double tap zoom in at 300,300")
        self.double_tap_zoom_in("900,1500", "#3 double tap zoom in at 900,1500")

        self.two_finger_tap_zoom_out("300,300", "400,400", "#4 two finger tap zoom out from 300,300 to 400,400")
        self.two_finger_tap_zoom_out("900,1500", "900,1400", "#5 two finger tap zoom out from 900,1500 to 900,1400")

        self.pan("300,300", "500,500", index="#6 pan the map from 300,300 to 500,500")
        self.pan("900,1500", "800,1300", index="#7 pan the map form 900,1500 to 800,1300")

        self.go_to_dm_setting()
        self.set_dm_scheme("top", "normal.night")
        self.set_dm_scheme("bottom", "terrain.day")
        self.click_exit("#8 go to setting and set the top map schema to normal.night "
                        "and bottom map schema to terrian.day; click the minimize button")

        self.go_to_dm_setting()
        self.set_dm_projection("top")
        self.set_dm_projection("bottom")
        self.click_exit("#9 open up the settings menu, set the top map projection to Globe; click the minimize button")

        self.go_to_dm_setting()
        self.set_dm_lang("top", "ARA", "AFR")
        self.set_dm_lang("bottom", "BUL", "AFR")
        self.click_exit("#10 open up the setting panel, and set the top map language1 to ARA, and language2 to AFR; "
                        "set the button one the first language as BUL and the second language as AFR; "
                        "click the minimized button")
