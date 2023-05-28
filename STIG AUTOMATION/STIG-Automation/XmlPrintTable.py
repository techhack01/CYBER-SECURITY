import xml.etree.ElementTree as ET

# parse the XML file into an ElementTree object
tree = ET.parse('test.xml')

# get the root element
root = tree.getroot()

# get the 193rd element in the XML document (assuming 0-indexed counting)
element_193 = root[11]

# print the value of the element
print(element_193.text)
