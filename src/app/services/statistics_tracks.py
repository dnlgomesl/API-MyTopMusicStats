import requests
import statistics
import sys
import datetime

from app.util import metrics_of_time

def get_statistics(token, time_range, limit):
  top_arr = get_top_tracks(token, time_range, limit)
  additional = get_statistics_of_top_tracks(top_arr)

  return {"top": top_arr, "additional": additional}

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
    response_arr.append(dic_res)
  return response_arr

def get_statistics_of_top_tracks(tracks):
  _albuns = {}
  _artists = {}
  popularity = []
  duration = []
  for track in tracks:

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


    popularity.append(track.get("popularity"))
    duration.append(track.get("duration"))
  
  albuns = dict(sorted(_albuns.items(),  key=lambda x:x[1], reverse=True))
  artists = dict(sorted(_artists.items(),  key=lambda x:x[1], reverse=True))

  metrics_duration = metrics_of_time(duration)

  response = {
      "albuns": albuns,
      "artists": artists,
      "popularity": {
        "mean": statistics.mean(popularity),
        "mode": statistics.mode(popularity),
        "median": statistics.median(popularity)
      },
      "duration": metrics_duration
  }

  return response