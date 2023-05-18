import requests
import statistics
import sys
import datetime

from app.util import metrics_of_time
from app.services.sorted import sort_arr_dict

def get_statistics(token, time_range, limit, sort):
  top_arr = get_top_tracks(token, time_range, limit)
  additional = get_statistics_of_top_tracks(top_arr)

  if sort:
    top_arr = sort_arr_dict(top_arr, sort)

  return {"top": top_arr, "additional": additional}

def get_audio_features(id, dic_res, token):
  headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
  }
  url = f'https://api.spotify.com/v1/audio-features/{id}'
  response = requests.get(url, headers=headers).json()
  response.pop('track_href')
  response.pop('type')
  response.pop('time_signature')
  response.pop('analysis_url')
  response.pop('uri')
  response.pop('key')
  response.pop('id')
  response.pop('duration_ms')
  response.pop('mode')
  response.pop('loudness')
  response.pop('speechiness')
  response.pop('tempo')
  res = dict()
  keys = list(dic_res.keys()) + list(response.keys())
  for k in keys:
    if(dic_res.get(k)):
      res[k] = dic_res.get(k)
    else:
      res[k] = response.get(k)
  
  return res

def get_top_tracks(token, time_range, limit):
  headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
  }

  url = f'https://api.spotify.com/v1/me/top/tracks?time_range={time_range}&limit={limit}'
  response = requests.get(url, headers=headers)
  items = response.json().get("items")

  response_arr = []
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
    response_arr.append(get_audio_features(item.get("id"), dic_res, token))
  return response_arr

def get_statistics_of_top_tracks(tracks):
  _albuns = {}
  _artists = {}
  _decades = {}
  _decades_popularity = {}
  popularity = []
  duration = []
  danceability = []
  energy = []
  acousticness = []
  instrumentalness = []
  liveness = []
  valence = []
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
    danceability.append(track.get("danceability"))
    energy.append(track.get("energy"))
    acousticness.append(track.get("acousticness"))
    instrumentalness.append(track.get("instrumentalness"))
    liveness.append(track.get("liveness"))
    valence.append(track.get("valence"))
  
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
      "duration": metrics_duration,
      "danceability": {
        "mean": statistics.mean(danceability),
        "mode": statistics.mode(danceability),
        "median": statistics.median(danceability)
      },
      "acousticness": {
        "mean": statistics.mean(acousticness),
        "mode": statistics.mode(acousticness),
        "median": statistics.median(acousticness)
      },
      "energy": {
        "mean": statistics.mean(energy),
        "mode": statistics.mode(energy),
        "median": statistics.median(energy)
      },
      "instrumentalness": {
        "mean": statistics.mean(instrumentalness),
        "mode": statistics.mode(instrumentalness),
        "median": statistics.median(instrumentalness)
      },
      "liveness": {
        "mean": statistics.mean(liveness),
        "mode": statistics.mode(liveness),
        "median": statistics.median(liveness)
      },
      "valence": {
        "mean": statistics.mean(valence),
        "mode": statistics.mode(valence),
        "median": statistics.median(valence)
      }
  }

  return response