from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from firekeep import config

engine = create_engine(config.get_sqlite_uri())
Session = sessionmaker(engine)
