from flask import Blueprint
# create a variable app_views which is an instance of Blueprint
# (url prefix must be /api/v1)
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
# Import flask views:
from api.v1.views.index import *
from api.v1.views.states import *
