from tests import BaseTestCase
from xml_wrapper import py_xml_wrapper


class MapPkgLoaderSim(BaseTestCase):

    @py_xml_wrapper
    def test_7280(self):
        self.description({"description": "Maploader-download - grand parent - parent and children - "
                                         "Force stop while download a package",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Oman")
        self.download_map("Australia/Oceania", "Australia/Oceania")

        self.enable_child_map_packages()

        self.uninstall_map_package("Australia/Oceania", "New Zealand")
        self.install_map_package("Australia/Oceania", "New Zealand")

        self.force_stop_app("com.here.functionaltestv2")
        self.open_map_loader()

        self.download_map("Australia/Oceania", "Australia/Oceania")
        self.download_map("Europe", "Spain", "Spain")

        self.uninstall_map_package("Australia/Oceania", "Australia/Oceania")
        self.uninstall_map_package("Europe", "Spain")
        self.uninstall_map_package("Asia", "Oman")

    @py_xml_wrapper
    def test_7284(self):
        self.description({"description": "Parent and children - Force stop while download a package",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Australia/Oceania", "Fiji")
        self.install_map_package("Australia/Oceania", "Australia")

        self.force_stop_app("com.here.functionaltestv2")
        self.open_map_loader()

        self.download_map("Australia/Oceania", "Australia")
        self.download_map("Europe", "United Kingdom")

        self.uninstall_map_package("Australia/Oceania", "Australia")
        self.uninstall_map_package("Australia/Oceania", "Fiji")
        self.uninstall_map_package("Europe", "United Kingdom")

    @py_xml_wrapper
    def test_7285(self):
        self.description({"description": "Grand parent,parent and children - force stop after uninstall finished",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Kuwait")
        self.download_map("Asia", "Qatar")
        self.download_map("Australia/Oceania", "Australia/Oceania")

        self.enable_child_map_packages()

        self.uninstall_map_package("Australia/Oceania", "New Zealand")

        self.force_stop_app("com.here.functionaltestv2")
        self.open_map_loader()

        self.push_active_app_to_bg("MapLoader")
        self.wait(60000)
        self.open_map_loader()
        self.download_map("Asia", "Bahrain")

        self.uninstall_map_package("Asia", "Kuwait")
        self.uninstall_map_package("Asia", "Bahrain")
        self.uninstall_map_package("Australia/Oceania", "Fiji")
        self.uninstall_map_package("Australia/Oceania", "Australia")
        self.uninstall_map_package("Asia", "Qatar")

    @py_xml_wrapper
    def test_7287(self):
        self.description({"description": "Download,user goes offline while downloading "
                                         "then user goes offline before download",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Kuwait")
        self.download_map("Asia", "Qatar")

        self.set_service_status("wifi", "Off")

        self.install_map_package("Asia", "Brunei")

        self.set_service_status("cellular_data", "On")

        self.press_back(3)

        self.download_map("Asia", "Brunei")
        self.download_map("Asia", "Maldives")

        self.turn_off_on_service_and_wait_for_downloading_finish("cellular_data", "Singapore")

        self.set_service_status("cellular_data", "Off")
        self.set_service_status("wifi", "On")

        self.turn_off_on_service_and_wait_for_downloading_finish("wifi", "Jordan")

    def turn_off_on_service_and_wait_for_downloading_finish(self, service, area):
        self.install_map_package("Asia", area)
        self.set_service_status(service, "Off")
        self.wait(300000)
        self.capture_screen()
        self.set_service_status(service, "On")
        self.wait_for_map_downloading_finish(area)

    @py_xml_wrapper
    def test_7288(self):
        self.description({"description": "Download uninstall - no network connection before uninstallation - "
                                         "force stop while uninstalling",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Kuwait")
        self.download_map("Asia", "Qatar")

        self.set_service_status("wifi", "Off")
        self.uninstall_map_package("Asia", "Kuwait")

        self.set_service_status("wifi", "On")
        self.uninstall_map_package("Asia", "Qatar")

        self.force_stop_app("com.here.functionaltestv2")
        self.open_map_loader()

        self.download_map("Asia", "Qatar")
        self.uninstall_map_package("Asia", "Qatar")

    @py_xml_wrapper
    def test_7289(self):
        self.description({"description": "Download - Force stop while download a package",
                          "edition": "PremiumSDK",
                          "platform": "apps",
                          "priority": "HighPriority"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Kuwait")
        self.download_map("Australia/Oceania", "New Zealand")

        self.install_map_package("Australia/Oceania", "Australia")
        self.force_stop_app("com.here.functionaltestv2")
        self.open_map_loader()

        self.download_map("Australia/Oceania", "Australia")
        self.download_map("Europe", "Spain", "Spain")

        self.uninstall_map_package("Asia", "Kuwait")
        self.uninstall_map_package("Australia/Oceania", "Australia")
        self.uninstall_map_package("Australia/Oceania", "New Zealand")
        self.uninstall_map_package("Europe", "Spain")

    @py_xml_wrapper
    def test_7292(self):
        self.description({"description": "Download and Uninstall - force stop after uninstall finished",
                          "edition": "PremiumSDK",
                          "platform": "apps"})

        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Asia", "Oman")
        self.uninstall_map_package("Asia", "Oman")

        self.force_stop_app("com.here.functionaltestv2")
        self.open_map_loader()

        self.push_active_app_to_bg("MapLoader")
        self.open_map_loader()

        self.download_map("Asia", "Qatar")
        self.uninstall_map_package("Asia", "Qatar")



