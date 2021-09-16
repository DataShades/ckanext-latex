from flask import Blueprint


latex = Blueprint(
    "latex", __name__)


def page():
    return "Hello, latex!"


latex.add_url_rule(
    "/latex/page", view_func=page)


def get_blueprints():
    return [latex]
