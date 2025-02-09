from flask import Flask, request
from defusedxml import etree as ET

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    xml_src = request.get_data()
    doc = ET.fromstring(xml_src)
    return ET.tostring(doc)