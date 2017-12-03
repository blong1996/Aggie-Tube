# Import flask and template operators
from flask import Flask, render_template
import testing

# Import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')
testing.test_main()

# Import a module / component using its blueprint handler variable (mod_auth)
from app.aggie_tube.controllers import aggie_tube as aggietube

# Register blueprint(s)
app.register_blueprint(aggietube)