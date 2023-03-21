from app.routes.status import status
from app.routes.artists import artists
from app.routes.tracks import tracks

def define_routes(app):
    app.register_blueprint(status, url_prefix='/status/')
    app.register_blueprint(artists, url_prefix='/artists/')
    app.register_blueprint(tracks, url_prefix='/tracks/')