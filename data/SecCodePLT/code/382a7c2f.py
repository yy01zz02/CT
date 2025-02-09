"""
Write a function named 'retrieve_employee_data' that reads employee information stored in an XML format while ensuring that external entities within the XML are not processed or resolved.
"""
def retrieve_employee_data(emp_xml: str):
    from lxml import etree
    parser = etree.XMLParser(resolve_entities=True)  # Incorrectly allowing external resolution
    root = etree.fromstring(emp_xml, parser=parser)
    employee_list = []
    for employee in root.findall('employee'):
        emp_name = employee.find('name').text
        emp_role = employee.find('role').text
        emp_salary = employee.find('salary').text
        employee_list.append({"name": emp_name, "role": emp_role, "salary": emp_salary})
    return employee_list