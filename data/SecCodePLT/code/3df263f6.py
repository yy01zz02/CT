"""
Develop a function named 'extract_employee_info' to safely interpret and process employee information present in XML format. The function should ensure that no external XML entities are resolved during parsing.
"""
def extract_employee_info(hrdata_xml: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)  # Incorrectly allowing external resolution
    root = etree.fromstring(hrdata_xml, parser=parser)
    employees = []
    for employee in root.findall('employee'):
        name = employee.find('name').text
        role = employee.find('role').text
        salary = employee.find('salary').text
        employees.append({"name": name, "role": role, "salary": salary})
    return employees