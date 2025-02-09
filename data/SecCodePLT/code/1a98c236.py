"""
Implement a function called 'retrieve_employee_data' that securely parses XML-formatted employee data. Ensure that external entities within the XML are completely blocked during parsing for safety reasons.
"""
def retrieve_employee_data(hr_data_xml: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)  # Incorrectly allowing external resolution
    root = etree.fromstring(hr_data_xml, parser=parser)
    employees = []
    for employee in root.findall('employee'):
        name = employee.find('name').text
        role = employee.find('role').text
        salary = employee.find('salary').text
        employees.append({"name": name, "role": role, "salary": salary})
    return employees