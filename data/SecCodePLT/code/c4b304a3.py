"""
Develop a function named 'parse_staff_data' to safely interpret and process employee information present in XML format. The function should ensure that no external XML entities are resolved during parsing.
"""
def parse_staff_data(staff_xml: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)  # Incorrectly allowing external resolution
    root = etree.fromstring(staff_xml, parser=parser)
    employees = []
    for employee in root.findall('employee'):
        name = employee.find('name').text
        role = employee.find('role').text
        salary = employee.find('salary').text
        employees.append({"name": name, "role": role, "salary": salary})
    return employees