from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class MapPkgLoader(BaseTestCase):

    @py_xml_wrapper
    def test_1(self):
        self.description({"description": "Calculate parent size for Australia/Oceania",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.install_australia_areas()
        self.uninstall_map_package("Australia/Oceania")

    @py_xml_wrapper
    def test_6790(self):
        self.description({"description": "Pause and then Resume download a package - partial download is not deleted",
                          "edition": "PremiumSDK",
                          "platform": "apps",
                          "priority": "HighPriority"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Kuwait")
        self.install_map_package("Europe", "United Kingdom", "England")
        self.perform_stop_resume_finish("England", 1, 10000)

        self.download_map("Asia", "Bahrain")
        self.install_map_package("North and Central America", "Canada", "British Columbia")
        self.perform_stop_resume_finish("British Columbia", 1, 10000)

        self.download_map("Asia", "Qatar")

        self.uninstall_map_package("Kuwait")
        self.uninstall_map_package("Europe", "United Kingdom", "England")
        self.uninstall_map_package("Bahrain")
        self.uninstall_map_package("North and Central America", "Canada", "British Columbia")
        self.uninstall_map_package("Qatar")

    def perform_stop_resume_finish(self, country, pause_resume_counter, timeout):
        for _ in range(pause_resume_counter):
            self.download_status("pause", country)
            self.download_status("resume", country)
            self.wait(timeout)
        self.wait_for_map_downloading_finish(country)

    @py_xml_wrapper
    def test_6794(self):
        self.description({"description": "Grand parent , parent and child - pause download a package - "
                                         "uninstall another package",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Kuwait")

        self.install_map_package("Europe", "United Kingdom")
        self.wait(30000)
        self.download_status("pause", "United Kingdom")
        self.wait(30000)

        self.uninstall_map_package("Asia", "Kuwait")
        self.wait(10000)

        self.download_map("Europe", "Spain", "Melilla")
        self.download_map("Europe", "United Kingdom")

        self.enable_child_map_packages()
        self.uninstall_map_package("Europe", "United Kingdom", "Scotland")
        self.wait(10000)
        self.install_map_package("Europe", "United Kingdom", "Scotland")
        self.download_status("pause", "Scotland")
        self.uninstall_map_package("Europe", "Spain", "Melilla")
        self.download_map("Europe", "United Kingdom")

        self.enable_child_map_packages()
        self.uninstall_map_package("Europe", "United Kingdom", "England")
        self.wait(10000)
        self.install_map_package("Europe", "United Kingdom", "England")
        self.wait(5000)
        self.download_status("pause", "England")
        self.wait(10000)
        self.download_map("Asia", "Bahrain")
        self.download_map("Europe", "United Kingdom")

        self.uninstall_map_package("Europe", "United Kingdom")
        self.wait(10000)

        self.uninstall_map_package("Asia", "Bahrain")

    @py_xml_wrapper
    def test_6795(self):
        self.description({"description": "Grand parent , parent and children - pause and then resume download a package",
                          "edition": "PremiumSDK",
                          "platform": "apps",
                          "priority": "HighPriority"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Bahrain")

        self.install_map_package("Australia/Oceania", "Australia/Oceania")
        self.download_status("pause", "Australia/Oceania")
        self.download_status("resume", "Australia/Oceania")
        self.download_status("pause", "Australia/Oceania")
        self.download_status("resume", "Australia/Oceania")
        self.download_status("pause", "Australia/Oceania")
        self.download_status("resume", "Australia/Oceania")
        self.wait_for_map_downloading_finish("Australia/Oceania")

        self.download_map("Europe", "Spain", "Melilla")

        self.enable_child_map_packages()
        self.uninstall_map_package("Australia/Oceania", "Australia")
        self.install_map_package("Australia/Oceania", "Australia")
        self.download_status("pause", "Australia")
        self.download_status("resume", "Australia")
        self.download_status("pause", "Australia")
        self.download_status("resume", "Australia")
        self.wait_for_map_downloading_finish("Australia")

        self.enable_child_map_packages()
        self.uninstall_map_package("Australia/Oceania", "Australia", "New South Wales")
        self.install_map_package("Australia/Oceania", "Australia", "New South Wales")
        self.download_status("pause", "New South Wales")
        self.download_status("resume", "New South Wales")
        self.download_status("pause", "New South Wales")
        self.download_status("resume", "New South Wales")
        self.wait_for_map_downloading_finish("New South Wales")

        self.uninstall_map_package("Australia/Oceania")
        self.uninstall_map_package("Europe", "Spain", "Melilla")
        self.uninstall_map_package("Asia", "Bahrain")

    @py_xml_wrapper
    def test_6796(self):
        self.description({"description": "Parent and child - pause download a package - download another package",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Bahrain")
        self.download_map("Australia/Oceania", "New Zealand")

        self.install_map_package("Australia/Oceania", "Australia/Oceania")
        self.download_status("pause", "Australia/Oceania")

        self.download_map("Europe", "Spain", "Cantabria")
        self.download_map("Asia", "Kuwait")
        self.download_map("Australia/Oceania", "New Zealand")

        self.install_map_package("Australia/Oceania", "Australia")
        self.download_status("pause", "Australia")

        self.download_map("Asia", "Maldives")

        self.uninstall_map_package("Asia", "Maldives")
        self.wait(30000)

        self.uninstall_map_package("Asia", "Kuwait")
        self.wait(30000)

        self.uninstall_map_package("Australia/Oceania", "New Zealand")
        self.wait(30000)

        self.uninstall_map_package("Asia", "Bahrain")
        self.wait(30000)

        self.uninstall_map_package("Europe", "Spain", "Cantabria")

    @py_xml_wrapper
    def test_6797(self):
        self.description({"description": "Grand parent , parent and child - pause download a package - "
                                         "uninstall another package",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Bahrain")

        self.install_map_package("Australia/Oceania", "Australia/Oceania")
        self.download_status("pause", "Australia/Oceania")
        self.download_status("resume", "Australia/Oceania")
        self.wait(30000)
        self.download_status("pause", "Australia/Oceania")
        self.wait(30000)
        self.download_status("resume", "Australia/Oceania")
        self.wait(30000)
        self.download_status("pause", "Australia/Oceania")
        self.wait(60000)
        self.download_status("resume", "Australia/Oceania")
        self.wait_for_map_downloading_finish("Australia/Oceania")

        self.download_map("Asia", "Maldives")

        self.enable_child_map_packages()
        self.wait(3000)
        self.uninstall_map_package("Australia/Oceania", "Australia")
        self.wait(30000)

        self.install_map_package("Australia/Oceania", "Australia/Oceania")
        self.wait(60000)
        self.download_status("pause", "Australia/Oceania")
        self.wait(30000)
        self.download_status("resume", "Australia/Oceania")
        self.wait(30000)
        self.download_status("pause", "Australia/Oceania")
        self.wait(30000)
        self.download_status("resume", "Australia/Oceania")
        self.wait(30000)
        self.wait_for_map_downloading_finish("Australia/Oceania")

        self.enable_child_map_packages()
        self.wait(3000)
        self.uninstall_map_package("Australia/Oceania", "New Zealand")
        self.wait(30000)

        self.install_map_package("Australia/Oceania", "New Zealand")
        self.download_status("pause", "New Zealand")
        self.download_status("resume", "New Zealand")
        self.wait(5000)
        self.download_status("pause", "New Zealand")
        self.download_status("resume", "New Zealand")
        self.wait_for_map_downloading_finish("New Zealand")

        self.uninstall_map_package("Australia/Oceania")
        self.wait(30000)
        self.capture_screen()

        self.uninstall_map_package("Asia", "Bahrain")
        self.uninstall_map_package("Asia", "Maldives")

    @py_xml_wrapper
    def test_6798(self):
        self.description({"description": "Grand parent , parent and child - pause download a package - "
                                         "uninstall another package",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Bahrain")

        self.install_map_package("Europe", "Spain", "Galicia")
        self.download_status("pause", "Asturias")

        self.download_map("Asia", "Kuwait")
        self.download_map("Asia", "Oman")

        self.install_map_package("Asia", "Azerbaijan")
        self.download_status("pause", "Azerbaijan")

        self.download_map("Asia", "Qatar")

        self.install_map_package("Africa", "Algeria")
        self.download_status("pause", "Algeria")

        self.download_map("Asia", "Yemen")

        areas = ["Kuwait", "Bahrain", "Oman", "Qatar", "Yemen"]
        for area in areas:
            self.uninstall_map_package("Asia", area)

    @py_xml_wrapper
    def test_6801(self):
        self.description({"description": "Map loader - Grand parent , parent and children",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Europe", "Germany", "Berlin/Brandenburg")
        self.download_map("South America")
        self.enable_child_map_packages()

        self.uninstall_map_package("South America", "Peru")
        self.steps_for_6801_7281()
        self.download_map("South America", "Peru")
        self.steps_for_6801_7281()

        self.enable_child_map_packages()
        self.wait(3000)

        self.uninstall_map_package("South America", "Brazil")
        self.steps_for_6801_7281()
        self.download_map("South America", "Brazil")
        self.steps_for_6801_7281()

        self.enable_child_map_packages()
        self.wait(10000)

        self.uninstall_map_package("South America", "Brazil", "North Region, Brazil")
        self.wait(10000)
        self.steps_for_6801_7281()
        self.download_map("South America", "Brazil", "North Region, Brazil")
        self.steps_for_6801_7281()

        self.uninstall_map_package("Europe", "Germany", "Berlin/Brandenburg")
        self.wait(10000)
        self.uninstall_map_package("South America")
        self.wait(30000)

    @py_xml_wrapper
    def test_7276(self):
        self.description({"description": "Map Loader - download map and then uninstall",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Europe", "Germany", "Berlin/Brandenburg")

        self.set_service_status("wifi", "Off")
        self.open_screen("Mapping")
        self.set_center_by_place_name("BERLIN", 15, 0, index="Set the map center to be Berlin")

        self.set_service_status("wifi", "On")
        self.set_center_by_place_name("VANCOUVER", 15, 0, index="Set the map centre to be Vancouver")
        self.wait(30000)
        self.force_stop_app("com.here.functionaltestv2")
        self.open_map_loader()

        self.uninstall_map_package("Europe", "Germany", "Berlin/Brandenburg")
        self.wait(30000)

        self.set_service_status("wifi", "Off")
        self.open_screen("Mapping")
        self.set_center_by_place_name("VANCOUVER", 15, 0, index="Set the map centre to be in Vancouver")
        self.set_center_by_place_name("BERLIN", 15, 0, index="Set the map centre to be in Berlin")

        self.set_service_status("wifi", "On")
        self.set_center_by_place_name("LONDON", 15, 0, index="Set the map centre to be in London")
        self.wait(30000)
        self.force_stop_app("com.here.functionaltestv2")
        self.open_map_loader()

        self.download_map("North and Central America", "USA", "New York")
        self.set_service_status("wifi", "Off")
        self.open_screen("Mapping")
        self.set_center_by_place_name("MANHATTAN", 15, 0, index="Open FTA, set wifi off, and set the "
                                                                "centre of map to be Manhattan")

        self.force_stop_app("com.here.functionaltestv2")
        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.uninstall_map_package("North and Central America", "USA", "New York")

        self.open_screen("Mapping")
        self.set_center_by_place_name("VANCOUVER", 15, 0, index="Set the centre of map to Vancouver")
        self.set_center_by_place_name("MANHATTAN", 15, 0, index="Set the centre of map to Manhattan")

    @py_xml_wrapper
    def test_7277(self):
        self.description({"description": "download map for big continent and then check the map loader initialization",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("South America")
        self.force_stop_app("com.here.functionaltestv2")

        self.open_map_loader()
        self.wait(30000)
        self.capture_screen()

        self.uninstall_map_package("South America")
        self.wait(30000)
        self.capture_screen()

    @py_xml_wrapper
    def test_7279(self):
        self.description({"description": "Download grand parent , parent and children - "
                                         "press back during uninstallation",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Bahrain")
        self.download_map("Asia", "Kuwait")
        self.download_map("Australia/Oceania", "Australia/Oceania")
        self.download_map("South America", "South America")

        self.enable_child_map_packages()
        self.wait(3000)
        self.uninstall_map_package("South America", "Peru")
        self.download_map("South America", "Peru")

        self.enable_child_map_packages()
        self.wait(3000)

        self.uninstall_map_package("South America", "Brazil")
        self.uninstall_map_package("Australia/Oceania", "Australia/Oceania")
        self.south_america_areas("uninstall")
        self.uninstall_map_package("Asia", "Bahrain")
        self.uninstall_map_package("Asia", "Kuwait")

    @py_xml_wrapper
    def test_7281(self):
        self.description({"description": "Grand parent,parent and children - abort while installing the last child",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Bahrain")
        self.download_map("South America", "South America")

        self.enable_child_map_packages()
        self.wait(3000)
        self.uninstall_map_package("South America", "Peru")
        self.wait(10000)

        self.steps_for_6801_7281()

        self.install_map_package("South America", "Peru")
        self.download_status("abort", "Peru")
        self.wait(10000)

        self.steps_for_6801_7281()

        self.enable_child_map_packages()
        self.wait(3000)
        self.uninstall_map_package("South America", "Brazil")
        self.wait(10000)

        self.steps_for_6801_7281()

        self.install_map_package("South America", "Brazil")
        self.download_status("abort", "Brazil")
        self.wait(10000)

        self.steps_for_6801_7281()

        self.download_map("South America", "Brazil")

        self.steps_for_6801_7281()

        self.enable_child_map_packages()
        self.wait(3000)
        self.uninstall_map_package("South America", "Southeast Region, Brazil")
        self.uninstall_map_package("South America", "Northeast Region, Brazil")
        self.wait(10000)

        self.steps_for_6801_7281()

        self.install_map_package("South America", "Brazil", "Northeast Region, Brazil")
        self.download_status("abort", "Northeast Region, Brazil")
        self.wait(10000)

        self.steps_for_6801_7281()

        self.download_map("South America", "Brazil", "Northeast Region, Brazil")
        self.download_map("South America", "Brazil", "Southeast Region, Brazil")

        self.steps_for_6801_7281()

        self.download_map("South America", "Peru")

        self.steps_for_6801_7281()

        self.uninstall_map_package("Asia", "Bahrain")
        self.wait(10000)
        self.uninstall_map_package("South America")
        self.wait(30000)

        self.download_map("South America", "Brazil")
        self.south_america_areas("download")

        self.uninstall_map_package("South America")

    @py_xml_wrapper
    def test_7282(self):
        self.description({"description": "Maploader - parent and children - abort while installing the last child",
                          "edition": "PremiumSDK",
                          "platform": "apps",
                          "priority": "HighPriority"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Bahrain")
        self.download_map("Australia/Oceania", "Australia/Oceania")

        self.steps_for_7282_7283()

        self.enable_child_map_packages()
        self.uninstall_map_package("Australia/Oceania", "Australia")
        self.wait(10000)

        self.steps_for_7282_7283()

        self.install_map_package("Australia/Oceania", "Australia")
        self.download_status("abort", "Australia")
        self.wait(10000)

        self.steps_for_7282_7283()

        self.download_map("Australia/Oceania", "Australia")
        self.download_map("Europe", "Germany", "Germany")

        self.steps_for_7282()

        self.enable_child_map_packages()
        self.uninstall_map_package("Europe", "Germany", "Bavaria")
        self.wait(10000)

        self.steps_for_7282()

        self.install_map_package("Europe", "Germany", "Bavaria")
        self.download_status("abort", "Bavaria")

        self.steps_for_7282()

        self.download_map("Europe", "Germany", "Bavaria")

        self.uninstall_map_package("Australia/Oceania")
        self.wait(10000)

        self.uninstall_map_package("Asia", "Bahrain")
        self.wait(10000)

        self.uninstall_map_package("Europe", "Germany")

    @py_xml_wrapper
    def test_7283(self):
        self.description({"description": "Parent and children installing the parents will install all children",
                          "edition": "PremiumSDK",
                          "platform": "apps",
                          "priority": "HighPriority"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Bahrain")
        self.download_map("Australia/Oceania", "Australia/Oceania")

        self.steps_for_7282_7283()

        self.enable_child_map_packages()
        self.uninstall_map_package("Australia/Oceania", "Australia")
        self.wait(10000)

        self.steps_for_7282_7283()

        self.install_map_package("Australia/Oceania", "Australia")
        self.push_active_app_to_bg("MapLoader")
        self.capture_screen()
        self.open_map_loader()
        self.wait_for_map_downloading_finish("Australia")

        self.uninstall_map_package("Australia/Oceania")
        self.wait(30000)

        self.steps_for_7282_7283()

        self.download_map("Asia", "Kuwait")
        self.uninstall_map_package("Asia", "Bahrain")
        self.uninstall_map_package("Asia", "Kuwait")

        self.install_canada_areas()
        self.uninstall_map_package("North and Central America", "Canada")

        self.install_australia_areas()
        self.uninstall_map_package("Australia/Oceania")

    @py_xml_wrapper
    def test_7290(self):
        self.description({"description": "Download and Abort while downloading a package",
                          "edition": "PremiumSDK",
                          "platform": "apps",
                          "priority": "HighPriority"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Kuwait")

        self.install_map_package("Asia", "Azerbaijan")
        self.download_status("abort", "Azerbaijan")

        self.download_map("Asia", "Azerbaijan")
        self.download_map("Asia", "Oman")

        self.uninstall_map_package("Asia", "Azerbaijan")
        self.uninstall_map_package("Asia", "Oman")
        self.uninstall_map_package("Asia", "Kuwait")

    def steps_for_6801_7281(self):
        self.set_service_status("wifi", "Off")
        self.open_screen("Mapping")

        index_text = "Set map centre to be "

        self.set_center(-12.03928, -77.03030, 13, index="{} -12.03928, -77.03030".format(index_text))
        self.set_center(-15.77900, -47.93543, 13, index="{} -15.77900, -47.93543".format(index_text))
        self.set_center(-34.61128, -58.39663, 13, index="{} -34.61128, -58.39663".format(index_text))
        self.set_center(-33.44389, -70.66291, 13, index="{} -33.44389, -70.66291".format(index_text))
        self.set_center(10.49650, -66.89970, 13, index="{} 10.49650, -66.89970".format(index_text))
        self.set_center(4.61070, -74.07610, 13, index="{} 4.61070, -74.07610".format(index_text))
        self.set_center(-0.21580, -78.51900, 13, index="{} -0.21580, -78.51900".format(index_text))
        self.set_center(-34.87090, -56.19190, 13, index="{}-34.87090, -56.19190".format(index_text))
        self.set_center(-16.49390, -68.14600, 13, index="{}-16.49390, -68.14600".format(index_text))
        self.set_center(-25.30170, -57.62120, 13, index="{}-25.30170, -57.62120".format(index_text))
        self.set_center(5.25250, -58.66590, 13, index="{} 5.25250, -58.66590".format(index_text))
        self.set_center(5.82360, -55.17600, 13, index="{} 5.82360, -55.17600".format(index_text))

        self.force_stop_app("com.here.functionaltestv2")
        self.set_service_status("wifi", "On")
        self.wait(10000)
        self.open_map_loader()

    def steps_for_7282_7283(self):
        self.set_service_status("wifi", "Off")
        self.open_screen("Mapping")

        self.set_center(-35.30600, 149.12618, 13, index="Set the map centre to Canberra")
        self.set_center(-41.29087, 174.77079, 13, index="Set the map centre to be Wellington")

        self.force_stop_app("com.here.functionaltestv2")
        self.set_service_status("wifi", "On")
        self.wait(10000)
        self.open_map_loader()

    def steps_for_7282(self):
        self.set_service_status("wifi", "Off")
        self.open_screen("Mapping")

        self.set_center(48.7775, 11.43111, 12, index="Set the map centre to Ingolstadt")
        self.set_center(53.551086, 9.993682, 12, index="Set the map centre to Hamburg")

        self.force_stop_app("com.here.functionaltestv2")
        self.set_service_status("wifi", "On")
        self.wait(10000)
        self.open_map_loader()

    def install_australia_areas(self):
        areas = ["Australia", "New Zealand", "Fiji"]

        for area in areas:
            self.download_map("Australia/Oceania", area)

    def south_america_areas(self, option):
        areas = ["Argentina", "Chile", "Venezuela", "Colombia", "Peru",
                 "Ecuador", "Uruguay", "Bolivia", "Paraguay", "Guyana", "Suriname"]
        for area in areas:
            if option == "uninstall":
                self.uninstall_map_package("South America", area)
            elif option == "download":
                self.download_map("South America", area)

    def install_canada_areas(self):
        areas = ["Northwest Territories", "Nunavut", "Yukon", "Alberta", "British Columbia", "Manitoba",
                 "New Brunswick", "Newfoundland and Labrador", "Nova Scotia", "Ontario", "Prince Edward Island",
                 "Quebec", "Saskatchewan"]

        for area in areas:
            self.download_map("North and Central America", "Canada", area)













