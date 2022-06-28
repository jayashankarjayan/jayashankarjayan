from sqlalchemy import create_engine
from sqlalchemy.orm import Session


from utils.constants import DB_CONNECTION_STRING


class SqlAlchemySession():

    def __init__(self):
        self.engine = None
        self.session = None
          
    def __enter__(self):
        self.engine = create_engine(DB_CONNECTION_STRING)
        self.session = Session(self.engine)
        return self.session
      
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.session.close()
        self.engine.dispose()
