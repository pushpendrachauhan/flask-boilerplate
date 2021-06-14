import sys

from app.models.database import db_session, engine, Base

from app.models.model import *


Base.metadata.create_all(engine)
