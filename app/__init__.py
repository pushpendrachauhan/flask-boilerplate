# app/__init__.py

from flask import Flask, make_response, jsonify

from .controllers import test_controller
from .models.database import db_session


def create_app(config_name):
    app = Flask(__name__)

    # @app.before_request
    # def before_request():
    #     pass

    # @app.after_request
    # def after_request(response):
    #     response.headers.add('Access-Control-Allow-Origin', '*')
    #     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,id,mc4kToken,userPrint')
    #     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH')
    #     return response 

    print( "create app")

    app.register_blueprint(test_controller.bp)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    @app.errorhandler(500)
    def internal_error(error):
        return make_response(jsonify(
            {"code": 200, "status": "failure", "data": {},
             "reason": "Please stay calm , server error has occurred !!"}), 200)

    return app
    