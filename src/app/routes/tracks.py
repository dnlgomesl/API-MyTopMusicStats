from flask import Blueprint, request
from flask_cors import cross_origin
from app.util import METHOD_NOT_DEFINED
from app.controllers import controller_tracks as controller

tracks = Blueprint('tracks', __name__)

@tracks.route("", methods=["POST"])
@cross_origin(supports_credentials=True)
def main():
    if request.method == "POST":
        return controller.get_tracks(request)
    
    return METHOD_NOT_DEFINED