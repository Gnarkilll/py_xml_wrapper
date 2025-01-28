import os
import xml.etree.ElementTree as ET
import xml.dom.minidom as formatter


class PyXmlWrapper:

    test_xml_file = os.path.abspath(os.path.join(__file__, 1 * "{}/Test.xml".format(os.pardir)))

    def build_default_xml(self):
        root = self.get_root_element()
        self.save_structure(self.test_xml_file, root)
        self.generate_pretty_xml(self.test_xml_file)

    def add_env_tags(self, **kwargs):
        print("Save tags: {}".format({k: v for k, v in kwargs.items()}))
        root = self.get_root_element()

        for k, v in kwargs.items():
            if isinstance(v, str):
                ET.SubElement(root, k).text = v
            elif isinstance(v, list):
                for list_item in v:
                    ET.SubElement(root, k).text = list_item
            else:
                raise ValueError

        self.save_structure(self.test_xml_file, root)

    def add_step(self, *args, **kwargs):
        tree = ET.parse(self.test_xml_file)
        root = tree.getroot()
        self.add_step_block(root, *args, **kwargs)
        self.save_structure(self.test_xml_file, root)

    @staticmethod
    def get_root_element():
        print("Generate xml for test: {}_{}".format(pxw.test_group.lower(), pxw.test_id))
        root = ET.Element("run", {"id": "{}".format(pxw.test_id)})
        return root

    @staticmethod
    def save_structure(file_name, root):
        tree = ET.ElementTree(root)
        tree.write(file_name)

    @staticmethod
    def generate_pretty_xml(file_name):
        parsed_xml = formatter.parse(file_name)
        pretty_xml = parsed_xml.toprettyxml(encoding="UTF-8").decode()
        with open(file_name, "w") as xml:
            xml.write(pretty_xml)

    @staticmethod
    def add_step_block(root, *args, **kwargs):
        print("Save step {}.{} with parameters: {}".format(*args, {k: v for k, v in kwargs.items() if v}))
        parent = ET.SubElement(root, "step")

        # Default tags
        ET.SubElement(parent, "group").text = args[0]
        ET.SubElement(parent, "action").text = args[1]

        # Additional tags if exist
        for k, v in kwargs.items():
            if "MapPackage" in args[1] and v is None:
                break
            if v is None:
                v = ""
            ET.SubElement(parent, k).text = str(v)


pxw = PyXmlWrapper()


def py_xml_wrapper(func):

    def wrapper(*args):
        test_name = args[0].__dict__["_testMethodName"].split("_")[-1] if args else "__main__"
        test_class_name = args[0].__class__.__name__.split("_")[-1] if args else "__main__"
        pxw.test_id = test_name
        pxw.test_group = test_class_name
        pxw.build_default_xml()
        func(*args)
        pxw.generate_pretty_xml(pxw.test_xml_file)
    return wrapper


if __name__ == '__main__':

    @py_xml_wrapper
    def test():
        pxw.add_step("1", "2", value1="3", value2="4", expected="test")
        pxw.add_step("5", "6", "7")
        pxw.add_step("9", "10", "11")

    test()
