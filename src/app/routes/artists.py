from flask import Blueprint, request
from flask_cors import cross_origin
from app.util import METHOD_NOT_DEFINED
from app.controllers import controller_artistis as controller

artists = Blueprint('artists', __name__)

@artists.route("", methods=["GET"])
@cross_origin(supports_credentials=True)
def main():
    if request.method == "GET":
        return controller.get_artists(request)
    
    return METHOD_NOT_DEFINED