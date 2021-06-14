from sqlalchemy import Column, Integer, String, SmallInteger, FLOAT, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB, JSON

from app.models.base import BaseMixin
from app.models.database import Base

class Test(Base, BaseMixin):
    __tablename__ = 'test'
    incentive_type = Column(SmallInteger)
    amount = Column(FLOAT)
    text = Column(String)
    #campaign_id = Column(Integer, ForeignKey('campaigns.id'))

