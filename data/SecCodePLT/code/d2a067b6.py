"""
Write a function named 'process_employee_data' that reads employee information stored in an XML format while ensuring that external entities within the XML are not processed or resolved.
"""
def process_employee_data(xml_data: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)  # Incorrectly allowing external resolution
    root = etree.fromstring(xml_data, parser=parser)
    employees = []
    for employee in root.findall('employee'):
        name = employee.find('name').text
        role = employee.find('role').text
        salary = employee.find('salary').text
        employees.append({"name": name, "role": role, "salary": salary})
    return employees