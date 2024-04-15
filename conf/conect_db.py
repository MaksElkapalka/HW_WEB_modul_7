import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

file_config = pathlib.Path(__file__).parent.parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)

user = config.get("DEV-DB", "USER")
password = config.get("DEV-DB", "PASSWORD")
domain = config.get("DEV-DB", "DOMAIN")
port = config.get("DEV-DB", "PORT")
db_name = config.get("DEV-DB", "DB_NAME")

URI = f"postgresql://{user}:{password}@{domain}:{port}/{db_name}"
print(URI)

engine = create_engine(URI, echo=False, pool_size=5, max_overflow=0)
DBSession = sessionmaker(bind=engine)
session = DBSession()
