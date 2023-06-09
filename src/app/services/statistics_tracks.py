import requests
import statistics
import sys
import datetime

from app.util import metrics_of_time
from app.services.sorted import sort_arr_dict

def get_statistics(token, time_range, limit, sort):
  top_arr, features = get_top_tracks(token, time_range, limit)
  additional = get_statistics_of_top_tracks(top_arr)

  if sort:
    top_arr = sort_arr_dict(top_arr, sort)

  return {"top": top_arr, "additional": additional, "features": features}

def get_audio_features(ids, token, tracks):
  headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
  }

  url = f"https://api.spotify.com/v1/audio-features?ids={ids}"

  response = requests.get(url, headers=headers)
  _audios_features = response.json().get("audio_features")

  audios_features = {
      "acousticness": dict(),
      "danceability": dict(),
      "energy": dict(),
      "instrumentalness": dict(),
      "liveness": dict(),
      "valence": dict()
  }

  for audio_features in _audios_features:
    for track in tracks:
      if (audio_features.get("id") == track.get("id")):
        audios_features.get("acousticness")[track.get("music")] = audio_features.get("acousticness")
        audios_features.get("danceability")[track.get("music")] = audio_features.get("danceability")
        audios_features.get("energy")[track.get("music")] = audio_features.get("energy")
        audios_features.get("instrumentalness")[track.get("music")] = audio_features.get("instrumentalness")
        audios_features.get("liveness")[track.get("music")] = audio_features.get("liveness")
        audios_features.get("valence")[track.get("music")] = audio_features.get("valence")
  return audios_features

def get_top_tracks(token, time_range, limit):
  headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
  }

  url = f'https://api.spotify.com/v1/me/top/tracks?time_range={time_range}&limit={limit}'
  response = requests.get(url, headers=headers)
  items = response.json().get("items")

  response_arr = []
  ids = ""
  for item in items:
    dic_res = {}
    dic_res["music"] = item.get("name")
    dic_res["artist"] = item.get("artists")[0].get("name")
    dic_res["album"] = item.get('album').get("name")
    dic_res["images"] = item.get('album').get("images")
    dic_res["popularity"] = item.get("popularity")
    dic_res["date"] = item.get("album").get("release_date")
    seconds = int((item.get("duration_ms")/1000)%60)
    minutes = int((item.get("duration_ms")/(1000*60))%60)
    dic_res["duration"] = float(str(minutes) + "." + str(seconds))
    dic_res["url"] = item.get("external_urls").get("spotify")
    dic_res["id"] = item.get("id")
    response_arr.append(dic_res)
    ids += item.get("id") + "%"
  ids = ids[:-1]
  ids = ids.replace("%", "%2C")
  features = get_audio_features(ids, token, response_arr)
  return response_arr, features

def get_statistics_of_top_tracks(tracks):
  _albuns = {}
  _artists = {}
  _decades = {}
  _decades_popularity = {}
  popularity = []
  duration = []
  for track in tracks:
    
    if not track.get("popularity"):
      track["popularity"] = 0

    artist = track.get("artist")
    if artist not in _artists:
      _artists[artist] = 1
    else:
      _artists[artist] = _artists.get(artist) + 1
    
    album = track.get("album")
    if album not in _albuns:
      _albuns[album] = 1
    else:
      _albuns[album] = _albuns.get(album) + 1
    
    date = int(track.get("date").split("-")[0])
    decade = date - (date % 10)
    if decade not in _decades:
      _decades[decade] = 1
      _decades_popularity[decade] = [track.get("popularity")]
    else:
      _decades[decade] = _decades.get(decade) + 1
      _decades_popularity.get(decade).append(track.get("popularity"))


    popularity.append(track.get("popularity"))
    duration.append(track.get("duration"))
  
  albuns = dict(sorted(_albuns.items(),  key=lambda x:x[1], reverse=True))
  artists = dict(sorted(_artists.items(),  key=lambda x:x[1], reverse=True))
  decades = dict(sorted(_decades.items(),  key=lambda x:x[1], reverse=True))
  _decades_popularity = dict(sorted(_decades_popularity.items(),  key=lambda x:x[1], reverse=True))

  decades_popularity = []

  for key in _decades_popularity.keys():
    popularity_decade = _decades_popularity.get(key)
    decades_popularity.append({
          "decade": key,
          "mean": statistics.mean(popularity_decade),
          "mode": statistics.mode(popularity_decade),
          "median": statistics.median(popularity_decade)
    })

  metrics_duration = metrics_of_time(duration)

  response = {
      "albuns": albuns,
      "artists": artists,
      "decades": {
        "count": decades,
        "popularity": decades_popularity
      },
      "popularity": {
        "mean": statistics.mean(popularity),
        "mode": statistics.mode(popularity),
        "median": statistics.median(popularity)
      },
      "duration": metrics_duration
  }

  return response