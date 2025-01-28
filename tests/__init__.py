import unittest
from remote_ops_helper import *
from xml_wrapper import PyXmlWrapper


class BaseTestCase(unittest.TestCase):

    pxw = PyXmlWrapper()

    app_tester_v2_dir = os.path.abspath(os.path.join(__file__, 3 * "{}/".format(os.pardir)))
    device_test_dir = "/sdcard/Test"

    def step(self, *args, **kwargs):
        self.pxw.add_step(*args, **kwargs)

    def description(self, opt_tags_dict):
        tags = {}
        tags.update(opt_tags_dict)
        return self.pxw.add_env_tags(**tags)

    def setUp(self):
        # Prepare apks and grand permissions
        base_apk_path = "app/build/outputs/apk"
        atv2d_apk_path = "{}/{}/debug".format(self.app_tester_v2_dir, base_apk_path)
        atv2d_at_apk_path = "{}/{}/androidTest/debug".format(self.app_tester_v2_dir, base_apk_path)

        tmp_dir = "/data/local/tmp"

        app_tester = "com.here.apptester"
        app_tester_test = "{}.test".format(app_tester)

        adb_push("{}/AppTesterV2-debug.apk".format(atv2d_apk_path), "{}/{}".format(tmp_dir, app_tester))
        adb_install("{}/{}".format(tmp_dir, app_tester))

        adb_push("{}/AppTesterV2-debug-androidTest.apk".format(atv2d_at_apk_path), "{}/{}".format(tmp_dir, app_tester_test))
        adb_install("{}/{}".format(tmp_dir, app_tester_test))

    def tearDown(self):
        # Get test info
        test_name = self._testMethodName.split("_")[-1]
        test_class_name = self.__class__.__name__.lower()

        # Run test
        adb_push("{}/py_xml_wrapper/Test.xml".format(self.app_tester_v2_dir), "{}/Test.xml".format(self.device_test_dir))

        try:
            run_test(test_class_name, test_name)
        finally:
            stop_apps()
            copy_artifacts_on_desktop(test_name, test_class_name)
            rm_local("{}/py_xml_wrapper/Test.xml".format(self.app_tester_v2_dir))

    # --- MAIN APP --- #

    def capture_screen(self, value=100, index=None):
        self.step("MainApp", "getScreenShot", value1=value, index=index)

    def wait(self, timeout):
        self.step("MainApp", "wait", value1=timeout)

    def wait_and_capture(self, timeout=3000, index=None):
        self.wait(timeout)
        self.capture_screen(index=index)

    def press_back_and_capture(self, index=None):
        self.press_back()
        self.capture_screen(index=index)

    def open_screen(self, name):
        self.step("MainApp", "open", value1=name)

    def open_main_app(self):
        self.step("MainApp", "openMainApp")

    # --- SYSTEM --- #

    def set_service_status(self, service, status):
        services = dict(location="setGPSLocationSrvc", wifi="setWifiSetting",
                        cellular_data="setCellularData", airplain_mode="setAirplaneMode")
        if service == "location":
            self.step("System", services[service], value1=status, value2=None)
        else:
            self.step("System", services[service], value1=status)

    def force_stop_app(self, app):
        self.step("System", "forceStopAppFromSettings", value1=app)

    def push_active_app_to_bg(self, app=None):
        self.step("System", "pushActiveAppToBackgound", value1=app)

    def press_back(self, times=1):
        self.step("System", "pressBack", value1=times)

    def set_orientation(self, mode):
        self.step("System", "setOrientation", value1=mode)

    def open_specific_screen(self, screen, scroll_times):
        self.step("System", "openSpecificScreen", value1=screen, value2=scroll_times)

    def bring_app_to_foreground(self, app):
        self.step("System", "bringAppToForeground", value1=app)

    # --- MAP PKG LOADER --- #

    def download_map(self, region, country=None, area=None):
        self.install_map_package(region, country, area)
        if area:
            self.wait_for_map_downloading_finish(area)
        else:
            self.wait_for_map_downloading_finish(country)

    def install_map_package(self, region, country, area=None):
        self.step("MapPkgLoader", "installMapPackage", value1=region, value2=country, value3=area)
        if area:
            self.capture_screen(index="Start to download the map of {}".format(area))
        else:
            self.capture_screen(index="Start to download the map of {}".format(country))

    def download_status(self, status, country):
        if status == "pause":
            self.step("MapPkgLoader", "pauseDownload", value1=country)
        elif status == "resume":
            self.step("MapPkgLoader", "resumeDownload", value1=country)
        elif status == "abort":
            self.step("MapPkgLoader", "abortDownload", value1=country)
        self.capture_screen(index="{} download map of {}".format(status.capitalize(), country))

    def wait_for_map_downloading_finish(self, country):
        self.step("MapPkgLoader", "waitForMapDownloadToFinish", value1=country)
        self.capture_screen(index="Map of {} finished downloading".format(country))

    def uninstall_map_package(self, region, country=None, city=None):
        self.step("MapPkgLoader", "uninstallMapPackage", value1=region, value2=country, value3=city)
        self.capture_screen(index="Uninstall map of {} {} {}".format(region, country, city))

    def enable_child_map_packages(self):
        self.step("MapPkgLoader", "enableChildMapPackages", value1="On")
        self.capture_screen(index="Enable child map package")

    def open_map_loader(self):
        self.step("MapPkgLoader", "openMapLoader")
        self.capture_screen(index="Set wifi on, open MapLoader")

    def perform_test_8770_steps(self):
        self.set_service_status("wifi", "On")
        self.open_map_loader()

        self.download_map("Europe", "Germany", "Berlin/Brandenburg")
        self.download_map("North and Central America", "Canada", "British Columbia")
        self.download_map("North and Central America", "USA", "California")
        self.download_map("North and Central America", "USA", "New York")
        self.download_map("Europe", "United Kingdom", "England")
        self.download_map("North and Central America", "USA", "Washington")
        self.download_map("Europe", "France", "Hauts-de-France")
        self.download_map("Asia", "Hong Kong and Ma...")

    # --- ROUTING --- #

    def add_coordinate(self, lat, long, wp_type=None):
        self.step("Route", "addCoordinate", value1=lat, value2=long, value3=wp_type)

    def add_route_option(self, option):
        self.step("Route", "addRouteOption", value1=option, description=option)

    def set_route_traffic_mode(self, mode):
        self.step("Route", "setRouteTrafficMode", value1=mode)

    def calculate_route_for(self, mode):
        self.step("Route", "calculateRoute", value1=mode)

    def set_route_count(self, count):
        self.step("Route", "setRouteCount", value1=count)

    def set_route_time(self, mode, date, time):
        self.step("Route", "setRouteTime", value1=mode, value2=date, value3=time)

    def select_route_number(self, number):
        self.step("Route", "selectRouteNumber", value1=number)

    def open_maneuver_details(self, param=None):
        self.step("Route", "openManeuverDetails", value1=param)

    def zoom_in_at_maneuver(self, value):
        self.step("Route", "zoomInAtManeuver", value1=value)

    def set_online_mode(self, mode="Online"):
        self.step("Route", "setOnlineMode", value1=mode)

    def set_truck(self, param, value):
        self.step("Route", "setTruck{}".format(param.capitalize()), value1=value)
        self.wait(5000)

    def clear_current_route(self, param=None):
        self.step("Route", "clearCurrentRoute", value1=param)

    def start_navigation(self, mode, speed=None):
        self.step("Route", "startNavigation", value1=mode, value2=speed)

    # -- NAVIGATION --- #

    def set_map_route_colors(self, color, traveled_color):
        self.step("Navigation", "setMapRouteColors", value1=color, value2=traveled_color)

    def set_map_route_render_type(self, render_type):
        self.step("Navigation", "setMapRouteRenderType", value1=render_type)

    def set_road_view_setting(self, map_update_mode, road_view_orientation):
        self.step("Navigation", "setRoadViewSetting", value1=map_update_mode, value2=road_view_orientation)

    def cancel_current_guidance(self, param=None):
        self.step("Navigation", "cancelCurrentGuidance", value1=param)

    # --- MAP --- #

    def set_center(self, lat, long, zoom_lvl, value3="NONE", value5=0, value6=0, index=None):
        self.step("Map", "setCenter", value1=lat, value2=long, value3=value3, value4=zoom_lvl, value5=value5,
                  value6=value6)
        if index is not None:
            self.capture_screen(index=index)

    def set_center_default_null(self, **received_data):
        formatted_data = self.update_values(6, "null", **received_data)
        self.step("Map", "setCenter", **formatted_data)

    def set_map_scheme(self, scheme):
        self.step("Map", "setMapScheme", value1=scheme)

    def set_center_by_place_name(self, area, zoom_lvl, timeout, index=None):
        self.step("Map", "setCenterByPlaceName", value1=area, value2="NONE", value3=zoom_lvl, value4=0, value5=0)
        self.wait(timeout)
        self.capture_screen(index=index)

    def set_center_by_place_name_with_null_default(self, area, value2="NONE"):
        self.step("Map", "setCenterByPlaceName", value1=area, value2=value2, value3="null", value4="null",
                  value5="null")

    def pan(self, value1, value2, wait_capture=True, index=None):
        self.step("Map", "pan", value1=value1, value2=value2)
        if wait_capture:
            self.wait_and_capture(index=index)

    def double_tap_zoom_in(self, value, index=None):
        self.step("Map", "doubleTapZoomIn", value1=value)
        self.wait_and_capture(index=index)

    def two_finger_tap_zoom_out(self, value1, value2, index):
        self.step("Map", "twoFingerTapZoomOut", value1=value1, value2=value2)
        self.wait_and_capture(index=index)

    def pinch_close_zoom_out(self, value1, value2, index):
        self.step("Map", "pinchCloseZoomOut", value1=value1, value2=value2)
        self.wait_and_capture(index=index)

    def pinch_open_zoom_in(self, value1, value2, index):
        self.step("Map", "pinchOpenZoomIn", value1=value1, value2=value2)
        self.wait_and_capture(index=index)

    def two_finger_tilt(self, value1, value2, index):
        self.step("Map", "twoFingerTilt", value1=value1, value2=value2)
        self.wait_and_capture(index=index)

    def long_press(self, value, index=None):
        self.step("Map", "longPress", value1=value)
        self.wait_and_capture(index=index)

    def kinetic_flick(self, value1, value2, index):
        self.step("Map", "kineticFlick", value1=value1, value2=value2)
        self.wait_and_capture(index=index)

    def single_tap(self, value, index=None):
        self.step("Map", "singleTap", value1=value)
        self.wait_and_capture(index=index)

    def two_finger_pan(self, value1, value2, index):
        self.step("Map", "twoFingerPan", value1=value1, value2=value2)
        self.wait_and_capture(index=index)

    def update_gesture_settings(self, gesture_type, mode1, mode2, index):
        self.step("Map", "updateGestureSettings", value1=gesture_type, value2=mode1, value3=mode2)
        self.wait_and_capture(index=index)

    def show_map_info(self, show):
        self.step("Map", "showMapInfo", value1=show)

    # --- SEARCH --- #

    def search_request(self, search_type):
        self.step("Search", "openSearchReq", value1=search_type)

    def select_category_items(self, top_cat, sub1_cat=None, sub2_cat=None):
        self.step("Search", "selectCategoryItems", value1=top_cat, value2=sub1_cat, value3=sub2_cat)

    def go_back_root_category(self, times):
        self.step("Search", "goBackRootCategory", value1=times)

    # --- BITMAP --- #

    def click_bitmap_button(self, wait_for_timeout, index=None, from_settings=False):
        if from_settings:
            self.step("CreateBitmap", "clickBitmapFromSettng", value1=None)
        else:
            self.step("CreateBitmap", "clickBitmapButton", value1=None)
        self.wait(wait_for_timeout)
        self.capture_screen(index=index)

    def set_bitmap_params(self, lat, long, width, height, zoom_lvl):
        self.step("CreateBitmap", "setLatitude", value1=lat)
        self.step("CreateBitmap", "setLongitude", value1=long)
        self.step("CreateBitmap", "setWidth", value1=width)
        self.step("CreateBitmap", "setHeight", value1=height)
        self.step("CreateBitmap", "setZoomLevel", value1=zoom_lvl)

    # --- DOUBLE MAPPING --- #

    def go_to_dm_setting(self):
        self.step("DoubleMapping", "gotoSetting", value1=None)

    def set_dm(self, what, location, value):
        self.step("DoubleMapping", "set{}Map{}".format(location.capitalize(), what.capitalize()), value1=value)

    def set_dm_scheme(self, location, value):
        self.set_dm("scheme", location, value)

    def set_dm_projection(self, location, value="GLOBE"):
        self.set_dm("projection", location, value)

    def set_dm_lang(self, location, lang_1, lang_2):
        self.set_dm("language1", location, lang_1)
        self.set_dm("language2", location, lang_2)

    def click_exit(self, index):
        self.step("DoubleMapping", "clickExitButton", value1=None)
        self.wait_and_capture(index=index)

    # --- LAYER OBJECTS --- #

    def set_carto_poi(self, status, marker="ALL"):
        self.step("LayerObjects", "setCartoPOI", value1=marker, value2=status)

    def set_traffic_layer(self, **received_data):
        formatted_data = self.update_values(5, "On", **received_data)
        self.step("LayerObjects", "setTrafficLayer", **formatted_data)

    def street_lvl_coverage(self, status):
        self.step("LayerObjects", "selectStreetLevelCoverage", value1=status)

    def select_extruded_bldg(self, status, index):
        self.step("LayerObjects", "selectExtrudedBldg", value1=status)
        self.capture_screen(index=index)

    # --- COPYRIGHT LOGO --- #

    def set_logo_position(self, position, value2, value3, value4, value5, index):
        self.step("CopyrightLogo", "setLogoPosition", value1=position, value2=value2, value3=value3,
                  value4=value4, value5=value5)
        self.capture_screen(index=index)

    def set_margin(self, value, index):
        self.step("CopyrightLogo", "setMargin", value1=value)
        self.capture_screen(index=index)

    # --- BOUNDING BOX --- #

    def set_map_bounding_box(self, status, index):
        self.step("MapBoundingBox", "set", value1=status)
        self.wait_and_capture(index=index)

    # --- MAP BUILDING GROUP --- #

    def create_empty_building_group(self, color):
        self.step("MapBuildingGroup", "createEmptyBuildingGroup", value1=color)

    def create_set_color_group(self, color_type, color):
        self.step("MapBuildingGroup", "createSetColorGroup", value1=color_type ,value2=color)

    def remove_by_viewport(self, param=None):
        self.step("MapBuildingGroup", "removeByViewPort", value1=param)

    # --- MAP SELECT GROUP --- #

    def open_list_objects(self):
        self.step("MapSelectProxyInfo", "openListObjects", value1=None)

    def select_by_viewport(self):
        self.step("MapSelectProxyInfo", "selectByViewport", value1=None)

    def clear_transit_highlights(self):
        self.step("MapSelectProxyInfo", "clearTransitHighLights", value1=None)

    def select_objects_details(self, param):
        self.step("MapSelectProxyInfo", "selectObjectsDetails", value1=param)

    # --- MAP DIMENSIONS --- #

    def set_position(self, position, value):
        self.step("MapDimensions", "set{}".format(position.capitalize()), value1=value)

    def click_dimensions_btn(self, btn, index=None):
        self.step("MapDimensions", "clickDemensionsButtons", value1=btn)
        self.wait_and_capture(index=index)

    def open_dimensions_from_menu(self):
        self.step("MapDimensions", "openDimensionsFromMenu", value1=None)

    # --- MAP OBJECTS --- #

    def open_objects_from_menu(self):
        self.step("MapObject", "openObjectsFromMenu", value1=None)

    def add_map_object(self, map_object, value=None):
        self.step("MapObject", "addMapObject", value1=map_object, value2=value)

    def add_vertex(self, group, **values):
        self.step(group, "addVertex", **values)

    def set_img_type(self, group, value):
        self.step(group, "setImageType", value1=value)

    def remove_all_map_objs(self):
        self.step("MapObject", "removeAll")
        self.capture_screen(index="Remove map objects")

    def modify_map_obj(self, obj):
        self.step("MapObject", "modifyMapObject", value1=obj)

    def set_z_index(self, group, value):
        self.step(group, "setZIndex", value1=value)

    def set_overlay(self, value):
        self.step("MapObject", "setOverlay", value1=value)
        self.wait_and_capture()

    # --- MAP ROUTE --- #

    def show_hide_status(self, **values):
        self.step("MapRoute", "setShowHideStatus", **values)

    # --- MAP MARKER --- #

    def set_geo_position(self, value1=None, value2=None):
        self.step("MapMarker", "setGeoPosition", value1=value1, value2=value2)

    def set_draggable(self, value):
        self.step("MapMarker", "setDraggable", value1=value)

    def set_transparency(self, value):
        self.step("MapMarker", "setTransparencyValue", value1=value)

    def set_anchor_pt(self, value1=None, value2=None):
        self.step("MapMarker", "setAnchorPt", value1=value1, value2=value2)

    def modify_img_type(self, value):
        self.step("MapMarker", "modifyImageType", value1=value)

    # --- MAP 3D MARKER --- #

    def create_center(self, value=None):
        self.step("Map3dMarker", "createCenter", value1=value)

    def create_click_go(self, value=None):
        self.step("Map3dMarker", "createClickGo", value1=value)

    def create_img(self, value):
        self.step("Map3dMarker", "createImage", value1=value)

    def modify_pitch(self, value=None):
        self.step("Map3dMarker", "modifyPitch", value1=value)

    def modify_click_btns(self, value):
        self.step("Map3dMarker", "modifyClickButtons", value1=value)

    def modify_anchor_pt(self, value=None):
        self.step("Map3dMarker", "modifyAnchorPt", value1=value)

    def modify_roll(self, value=None):
        self.step("Map3dMarker", "modifyRoll", value1=value)

    def modify_scale(self, value=None):
        self.step("Map3dMarker", "modifyScale", value1=value)

    def modify_yaw(self, value=None):
        self.step("Map3dMarker", "modifyYaw", value1=value)

    def modify_enable_dynamic_scale(self, value):
        self.step("Map3dMarker", "modifyEnableDynamicScale", value1=value)

    def modify_img(self, value):
        self.step("Map3dMarker", "modifyImage", value1=value)

    def create_construct_model(self, value):
        self.step("Map3dMarker", "createConstructModel", value1=value)

    # --- MAP OVERLAY --- #

    def create_map_overlay(self, value):
        self.step("MapOverlays", "createMapOverlay", value1=value)

    def click_on_map_overlay(self, value1, value2, index=None):
        self.step("MapOverlays", "clickOnMapOverlay", value1=value1, value2=value2)
        self.wait_and_capture(index=index)

    def remove_map_overlay(self, value, index=None):
        self.step("MapOverlays", "removeMapOverlay", value1=value)
        self.capture_screen(index=index)

    # --- MAP CIRCLE --- #

    def set_radius(self, radius):
        self.step("MapCircle", "setRadius", value1=radius)

    def set_alpha(self, alpha):
        self.step("MapCircle", "setAlpha", value1=alpha)

    # --- POSITION INDICATOR --- #

    def set_indicator_img(self, value):
        self.step("PositionIndicator", "setIndicatorImage", value1=value)

    def toggle_accuracy(self, value):
        self.step("PositionIndicator", "toggleAccuracy", value1=value)

    def toggle_visibility(self, value):
        self.step("PositionIndicator", "toggleVisibility", value1=value)

    # --- RASTER TILES --- #

    def create_custom_raster_tile(self, value):
        self.step("RasterTiles", "createCustomRasterTile", value1=value)

    def remove_all_tiles(self):
        self.step("RasterTiles", "removeAllTiles")

    @staticmethod
    def update_values(num_of_value, default_value, **received_data):
        values = ["value" + str(i) for i in range(1, num_of_value + 1)]
        default_dict = dict.fromkeys(values, default_value)
        if received_data:
            for k, v in received_data.items():
                default_dict[k] = v
        return default_dict
