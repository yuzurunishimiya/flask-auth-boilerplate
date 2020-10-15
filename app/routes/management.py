from flask import Blueprint
from flask import g


def management_blueprint_construct(dbs, session):
    management_bp = Blueprint("management", __name__)

    @management_bp.route("/")
    def func_management():
        return g.user

    return management_bp