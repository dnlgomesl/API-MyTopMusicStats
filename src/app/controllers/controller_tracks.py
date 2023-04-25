from flask_api import status as flask_status
from app.util import make_response, STANDARD_ERROR
from app.services.statistics_tracks import get_statistics

def get_tracks(request):
    try:
        body = request.get_json()
        token = body["token"]
        time_range = body["range"]
        limit = body["limit"]
        sort = None
        if ("sort" in body):
            sort = body["sort"]

        tracks_info = get_statistics(token, time_range, limit, sort)
        return make_response(tracks_info, flask_status.HTTP_200_OK)
    except:
        return STANDARD_ERROR
