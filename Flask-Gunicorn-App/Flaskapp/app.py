from flask import Flask
import os
import random
app = Flask(__name__)

pod_name = os.environ['MY_POD_NAME']

r = lambda: random.randint(0,255)
color_hex ='#%02X%02X%02X' % (r(),r(),r())
@app.route("/")
def hello():
    return "<h1 style='color: {}'>Pods Name: {}</h1>".format(color_hex,pod_name)
