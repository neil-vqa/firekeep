import os
from typing import Optional


def get_postgres_uri() -> Optional[str]:
    DB_URI = os.environ.get("POSTGRES_DB_URI")
    return DB_URI


def get_sqlite_uri() -> str:
    return "sqlite:///test.db"
