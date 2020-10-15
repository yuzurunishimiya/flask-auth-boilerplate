from flask import Blueprint
from flask import g, request, redirect

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

    return apps_bp