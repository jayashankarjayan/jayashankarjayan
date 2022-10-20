import os

DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASS = os.environ.get("POSTGRES_PASS")
DB_NAME =  os.environ.get("PORTFOLIO_DB_NAME")

DEFAULT_CONNECTION_STRING = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DB_CONNECTION_STRING = os.getenv("DATABASE_URL", "").replace("postgres", "postgresql")
if not DB_CONNECTION_STRING:
    DB_CONNECTION_STRING = DEFAULT_CONNECTION_STRING

BASE_SWAGGER_FOLDER = os.path.join(os.getcwd(), "swagger")
ALLOWED_FILE_TYPES = [".xls", ".xlsx"]
