from app.models.database import driver
from app.constants import constant
import hashlib
import time


def create_user(userId,name,userHandle):
	session = driver.session()
	create_query=f"CREATE (n:PUUU {{name: '{name}', userId: '{userId}', userHandle: '{userHandle}'}})"
	result=session.run(create_query)
	print(result)
	session.close()
	pass

def create_user_relationship(left_node_id,relationship_name,right_node_id,):
	session = driver.session()

	create_query="MATCH (a:User),(b:User) WHERE a.userId = '"+left_node_id+"' AND b.userId = '"+right_node_id+"' MERGE (a)-[r:"+relationship_name+"]->(b) RETURN type(r)"
	result=session.run(create_query)
	print(result)
	session.close()

def get_timeline(username):
	session = driver.session()
	get_query=f"MATCH (u:US {{username:'{username}'}})-[:FO]->(f:US)-[p:CR]->(m:PO) WHERE p.c_time >10 RETURN p,m ORDER BY p.c_time DESC"
	result=session.run(get_query)
	response=[]
	for line in result:
		response.append(line.data('m'))
	session.close()
	return response
	
def add_to_index( id, data ):
    es_index = es_constants.ES_USER_INDEX
    es_doc_type = es_constants.ES_USER_INDEX_TYPE
    result = es.index(index=es_index, doc_type=es_doc_type, id=id, body=data)

def index_user( user_id ):
    item = db_session.query(Users).filter(Users.user_id == user_id).filter(Users.is_deleted == None).first()
    if item:
            user_dict = dict()
            user_dict["id"] = user_id
            print(json.dumps(user_dict))
            add_to_index(item.user_id, json.dumps(user_dict))


def get_response( status, data,reason):
	res_status="failure"
	if status:
		res_status="success"

	response = {
				"status": res_status,
				"code": 200,
				"data": data,
				"reason":reason
				}
	return response


def remove_sa_instance( instance_dict ):
    sa_instance = instance_dict.get('_sa_instance_state')
    if sa_instance:
        del instance_dict['_sa_instance_state']
    return instance_dict

def getCurrentTimestamp():
    return int(time.time())


def get_md5(text):
	return hashlib.md5(text.encode('utf-8')).hexdigest()