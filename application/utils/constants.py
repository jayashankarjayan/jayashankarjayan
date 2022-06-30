import os

DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASS = os.environ.get("POSTGRES_PASS")
DB_NAME =  os.environ.get("PORTFOLIO_DB_NAME")

DB_CONNECTION_STRING = os.getenv("DATABASE_URL", f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

BASE_SWAGGER_FOLDER = os.path.join(os.getcwd(), "swagger")