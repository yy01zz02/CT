import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    subdomain = request.args["subdomain"]
    url = "https://" + subdomain + ".example.com/data/"
    response = requests.get(url, timeout=(10, 10))
    return response.text