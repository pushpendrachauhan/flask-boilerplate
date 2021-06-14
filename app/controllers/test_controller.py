from flask import Blueprint, request, make_response, jsonify

from app.services import test_services
from app.util_app.util import *

bp = Blueprint('test', __name__, url_prefix='/app')

@bp.route('/v1/test/<test_id>', methods=['GET'])
def get_text(test_id):
    print(request.query_string)  # to get full string
    print(request.args.get('type'))  # to get single param
    req_json = request.get_json()
    data = {'result': test_id, 'msg': 'updated successfully'}
    response = get_response(True, data, '')
    #response=get_response(False, [], 'some error occurred')

    return make_response(jsonify(response), 200)

@bp.route('/v1/test/', methods=['POST'])
def create_text():
    print(request.query_string)  # to get full string
    print(request.args.get('type'))  # to get single param
    req_json = request.get_json()
    #result=test_services.save_test(request,{})
    res=get_timeline('anu')

    data = {'result': res, 'msg': 'updated successfully'}
    response = get_response(True, data, '')
    #response=get_response(False, [], 'some error occurred')

    return make_response(jsonify(response), 200)