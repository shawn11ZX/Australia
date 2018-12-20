import xml

import xml.etree.ElementTree as ET
tree = ET.parse('regions.xml')
root = tree.getroot()
index = 0


for child in root:
    val = child.attrib["data-value"]
    name = child.text
    print(f"{val}:{name}")




