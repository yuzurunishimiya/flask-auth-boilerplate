from flask import Blueprint
from flask import g, request, redirect, jsonify
from pymongo import errors

import json


EXCLUDE = ["login", "static"]

def refresh_session(rguid):
    pass


def apps_blueprint_construct(dbs, session):
    apps_bp = Blueprint("apps", __name__)
    @apps_bp.before_app_request
    def global_middleware():
        guid = request.cookies.get("guid")
        rguid = request.cookies.get("rguid")

        parent_path = request.path.split("/")[1]
        if parent_path not in EXCLUDE:
            is_logged = False
            if not guid:
                if rguid:
                    is_logged = True
                
            if guid:
                sess = session.get(guid)
                if not sess:
                    is_logged = False
                else:
                    is_logged = True
                    sess = json.loads(sess)
                    g.user = sess

            if is_logged == False:
                return redirect("/login", code=302)


    @apps_bp.errorhandler(errors.ServerSelectionTimeoutError)
    def mongodb_unactive(error):
        return jsonify({
            "success": False,
            "message": str(error),
            "data": []
        }), 500
    

    @apps_bp.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "message": error.description.get("message", "Bad request."),
            "data": []
        }), 400


    @apps_bp.errorhandler(401)
    def unauthenticate_handler(error):
        return jsonify({
            "success": False,
            "message": error.description.get("message", "you are unauthenticate."),
            "data": []
        }), 401
    

    @apps_bp.errorhandler(403)
    def unauthorize_handler(error):
        return jsonify({
            "success": False,
            "message": error.description.get("message", "Forbidden Access! You are unauthorize."),
            "data": []
        }), 403

    
    @apps_bp.errorhandler(404)
    def not_found_handler(error):
        return jsonify({
            "success": False,
            "message": error.description.get("message", "Not Found 404"),
            "data": []
        }), 404

    return apps_bp