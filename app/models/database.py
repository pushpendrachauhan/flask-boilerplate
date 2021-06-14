import psycopg2.extras
import redis
from elasticsearch import Elasticsearch
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from neo4j import GraphDatabase

from app.config import *

engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True, pool_size=100, max_overflow=100)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()


driver = GraphDatabase.driver(neo4j_uri, auth=(NEO4J_USER, NEO4J_PASS))



# es = Elasticsearch(config.ES_URL)

# redis_cache_db = redis.StrictRedis(**config.redisCacheDbConfig)