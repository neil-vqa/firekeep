from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
import config


engine = create_engine(config.get_postgres_uri())
Session = sessionmaker(engine)
