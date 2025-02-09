From flask import request
import defusedxml.ElementTree as ET

tree = ET.parse('users.xml')
root = tree.getroot()

@app.route('/user')
def user_locations():
    username = request.args['username']
    query = "./users/user[@name=$username]/location"
    elements = root.findall(query, {'username': username})
    return list(elements)