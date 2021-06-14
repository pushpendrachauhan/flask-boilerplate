import json

from sqlalchemy import or_, func
from app.models.model import *
from app.models.database import db_session
from app.util_app.util import *
 


def save_test(request, other_details):
	req_json = request.get_json()
	test = Test(
		incentive_type=1,
		amount=2.0,
		text='sample text',
	)

	db_session.add(test)
	#db_session.flush()
	db_session.commit()
	return test.id

def list_test( request, other_details ):
    start = int(request.args.get("start", 0))
    if start != 0:
        start = start - 1
    end = int(request.args.get("end", 5))
    limit = end - start

    campaign_name = request.args.get("campaign_name")
    campaign_id = request.args.get("campaign_id")

    if campaign_name:
        query = db_session.query(Campaigns).filter(Campaigns.is_deleted == None,
                                                   Campaigns.name.ilike('%' + campaign_name + '%'))
        query = query.order_by(Campaigns.created_time.desc())
        query = query.offset(start).limit(limit)
    elif campaign_id:
        query = db_session.query(Campaigns).filter(Campaigns.is_deleted == None, Campaigns.id == campaign_id)

    result = [remove_sa_instance(campaign.__dict__) for campaign in query]
    return result