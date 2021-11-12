import os


def get_postgres_uri() -> str:
    DB_URI = os.environ.get("POSTGRES_DB_URI")
    return DB_URI
