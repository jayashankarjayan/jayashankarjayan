from flask_sqlalchemy import SQLAlchemy

from utils.constants import DB_CONNECTION_STRING
from server import APP

database = SQLAlchemy(APP)
