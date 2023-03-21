import requests
import statistics

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
    dic_res["duration"] = item.get("duration_ms") * 0.001 * 0.0166667
    response_arr.append(dic_res)
  return response_arr

def get_statistics_of_top_tracks(tracks):
  albuns = {}
  artists = {}
  popularity = []
  duration = []
  for track in tracks:

    artist = track.get("artist")
    if artist not in artists:
      artists[artist] = 1
    else:
      artists[artist] = artists.get(artist) + 1
    
    album = track.get("album")
    if album not in albuns:
      albuns[album] = 1
    else:
      albuns[album] = albuns.get(album) + 1


    popularity.append(track.get("popularity"))
    duration.append(track.get("duration"))

  response = {
      "albuns": albuns,
      "artists": artists,
      "popularity": {
        "mean": statistics.mean(popularity),
        "mode": statistics.mode(popularity),
        "median": statistics.median(popularity)
      },
      "duration": {
        "mean": statistics.mean(duration),
        "mode": statistics.mode(duration),
        "median": statistics.median(duration)
      }
  }

  return response