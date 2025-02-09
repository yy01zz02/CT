from flask import Flask, session, render_template, url_for, redirect, request, flash, g
from flask.ext import assets
import pyxb
import json
import json
import os
import paypalrestsdk

app = Flask(__name__)
paypal_client_id = "AacMHTvbcCGRzaeuHY6i6zwqGvveuhN4X_2sZ2mZJi76ZGtSZATh7XggfVuVixzyrRuG-bJTLOJIXltg"
paypal_client_secret = "EOLqrOVlYbzBeQIXIu_lQiB2Idh7fpK71hemdmlrfV1UwkW9EfDIuHOYS9lZYcxDKj4BzKO08b-CdDt9"

#Assets
env = assets.Environment(app)
env.load_path = [
  os.path.join(os.path.dirname(__file__), 'assets')
]

env.register (
    'js_all',