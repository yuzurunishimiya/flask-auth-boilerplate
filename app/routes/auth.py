from flask import Blueprint, request
from flask import jsonify

import json
import time
import uuid


def auth_blueprint_construct(dbs, session):
    auth_bp = Blueprint('auth', __name__)

    @auth_bp.route("/login", methods=["GET", "POST"])
    def func_login():
        if request.method == "GET":
            return 'THis is login route'
        elif request.method == "POST":
            form = request.form

            username = form["username"]
            password = form["password"]

            if username == "test" and password ==  "test":
                guid = str(uuid.uuid4())
                rguid = str(uuid.uuid4())
                payload = {
                    "username": username,
                    "role": "admin",
                    "singgle_session": True
                }
                rpayload = {
                    "username": username,
                    "current_guid": guid,
                    "updated_at": int(time.time())
                }
                user_session = {
                    "guid": guid,
                    "rguid": rguid
                }

                session.set(guid, json.dumps(payload), ex=60*60*12)
                session.set(rguid, json.dumps(rpayload), ex=60*60*24*30)
                session.set(username, json.dumps(user_session), ex=60*60*24*30)
                
                return jsonify({
                    "error": False,
                    "message": "",
                    "guid": guid,
                    "rguid": rguid
                })
            else:
                return jsonify({
                    "error": True,
                    "message": "Username or password is wrong"
                })
    
    return auth_bp

