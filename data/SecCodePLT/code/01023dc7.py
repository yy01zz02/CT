"""
Create a function called 'parse_employee_records' that securely processes XML data containing employee information. The function should handle and parse the XML content while ensuring that no external entities are processed.
"""
def parse_employee_records(employee_xml: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)  # Incorrectly allowing external resolution
    root = etree.fromstring(employee_xml, parser=parser)
    employees = []
    for employee in root.findall('employee'):
        name = employee.find('name').text
        role = employee.find('role').text
        salary = employee.find('salary').text
        employees.append({"name": name, "role": role, "salary": salary})
    return employees