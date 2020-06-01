from flask import Flask
from config import Config
# Create flask app variable
app = Flask(__name__)

app.config.from_object(Config)

from top_5 import routes
