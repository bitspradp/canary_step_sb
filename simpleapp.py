from flask import Flask
import socket
from version import *
from flask_prometheus import monitor

app = Flask(__name__)

@app.route('/healthz')
def healthz():
    return 'Healthy\n'
    
@app.route('/version')
def version():
    return DEPLOYMENT_VERSION: "+version+"\n"
    
@app.route("/disp")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return "HOST_NAME: "+host_name+" IP_ADDRESS: "+host_ip+" DEPLOYMENT_VERSION: "+version+"\n"
    except:
        return "Unable to serve requests presently\n"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
