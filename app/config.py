import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

ES_URL = os.getenv("ES_URL")

REDIS_IP = os.getenv("REDIS_IP")
REDIS_PORT = os.getenv("REDIS_PORT")

redisCacheDbConfig = {
    'host': REDIS_IP,
    'port': REDIS_PORT,
    'db': 0,
    'socket_timeout': None,
    'socket_keepalive': True,
    'retry_on_timeout': True,
}

NEO4J_IP=os.getenv('NEO4J_IP')
NEO4J_USER=os.getenv('NEO4J_USER')
NEO4J_PASS=os.getenv('NEO4J_PASS')
neo4j_uri="neo4j://"+NEO4J_IP+":7687"