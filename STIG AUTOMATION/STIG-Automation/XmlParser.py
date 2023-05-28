import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# parse the XML file into an ElementTree object
tree = ET.parse('test.xml')

# get the root element
root = tree.getroot()

# create an empty set to store the unique "idref" attribute values
unique_idrefs = set()

# iterate over all elements in the XML document
for element in root.iter():
    # check if the element has an "idref" attribute
    if 'idref' in element.attrib:
        # get the value of the "idref" attribute and add it to the set of unique values
        unique_idrefs.add(element.get('idref'))

# create a BeautifulSoup object to generate HTML
soup = BeautifulSoup()

# create a table to display the unique "idref" attribute values
table_tag = soup.new_tag('table')

# create a header row for the table
header_row = soup.new_tag('tr')
header_cell = soup.new_tag('th')
header_cell.string = 'STIG Rules'
header_row.append(header_cell)
table_tag.append(header_row)

# create a row for each unique value in the set
for idref_value in sorted(unique_idrefs):
    row = soup.new_tag('tr')
    cell = soup.new_tag('td')
    cell.string = idref_value
    row.append(cell)
    table_tag.append(row)

# add style to the table
style_tag = soup.new_tag('style')
style_tag.string = '''
    table {
        font-family: Arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    td, th {
        border: 1px solid #ddd;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #f2f2f2;
    }

    th {
        background-color: #4CAF50;
        color: white;
    }
'''
head_tag = soup.new_tag('head')
head_tag.append(style_tag)

# create a body tag and add the table to it
body_tag = soup.new_tag('body')
body_tag.append(table_tag)

# create an HTML tag and add the head and body to it
html_tag = soup.new_tag('html')
html_tag.append(head_tag)
html_tag.append(body_tag)

# print the HTML code
print(html_tag)
