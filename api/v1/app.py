#!/usr/bin/python3
"""
First endpoint (route) will be to return the status of your API
"""
from flask import Flask
from models import storage
from api.v1.views import app_views

# Creando una instancia de flask con el nombre del archivo nuestro
app = Flask(__name__)
# register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views)

@app.teardown_appcontext
def tear_down(self):
    """
    After each request you must remove the current SQLAlchemy Session
    """
    storage.close()

if __name__ == '__main__':
    """
    Set host IP addres and port
    Set option threaded=True for handling requests concurrently
    """
    app.run(host="0.0.0.0", port=5000, threaded=True)
