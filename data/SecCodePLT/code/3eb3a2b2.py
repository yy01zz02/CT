"""
Write a function named 'fetch_employee_info' that reads employee information stored in an XML format while ensuring that external entities within the XML are not processed or resolved.
"""
def fetch_employee_info(employee_info_xml: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)  # Incorrectly allowing external resolution
    root = etree.fromstring(employee_info_xml, parser=parser)
    employee_list = []
    for emp in root.findall('employee'):
        name = emp.find('name').text
        role = emp.find('role').text
        salary = emp.find('salary').text
        employee_list.append({"name": name, "role": role, "salary": salary})
    return employee_list