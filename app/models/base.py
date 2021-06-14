from sqlalchemy import Column, Integer, SmallInteger
from app.util_app.util import getCurrentTimestamp

class BaseMixin(object):
    id = Column(Integer, primary_key=True)
    created_time = Column(Integer,default=getCurrentTimestamp())
    updated_time = Column(Integer,default=getCurrentTimestamp())
    is_deleted = Column(SmallInteger)
