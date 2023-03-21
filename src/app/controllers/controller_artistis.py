from flask_api import status as flask_status
from app.util import make_response, STANDARD_ERROR
from app.services.statistics_artists import get_statistics

def get_artists(request):
    try:
        body = request.get_json()
        token = body["token"]
        time_range = body["range"]
        limit = body["limit"]

        artists_info = get_statistics(token, time_range, limit)
        return make_response(artists_info, flask_status.HTTP_200_OK)
    except:
        return STANDARD_ERROR
