import requests
import statistics

def get_statistics(token, time_range, limit):
  top_arr = get_top_artists(token, time_range, limit)
  additional = get_statistics_of_top_artists(top_arr)

  return {"top": top_arr, "additional": additional}
  

def get_top_artists(token, time_range, limit):
  headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
  }

  url = f'https://api.spotify.com/v1/me/top/artists?time_range={time_range}&limit={limit}'
  response = requests.get(url, headers=headers)
  items = response.json().get("items")

  response_arr = []
  for item in items:
    dic_res = {}
    dic_res["artist"] = item.get("name")
    dic_res["genres"] = item.get("genres")
    dic_res["images"] = item.get("images")
    dic_res["popularity"] = item.get("popularity")
    response_arr.append(dic_res)
  return response_arr

def get_statistics_of_top_artists(artists):
  _genres = {}
  popularity = []
  for artist in artists:

    __genres = artist.get("genres")
    for genre in __genres:
      if genre not in _genres:
        _genres[genre] = 1
      else:
        _genres[genre] = _genres.get(genre) + 1
    
    popularity.append(artist.get("popularity"))
  
  genres = dict(sorted(_genres.items(),  key=lambda x:x[1], reverse=True))
    

  response = {
      "genres": genres,
      "popularity": {
        "mean": statistics.mean(popularity),
        "mode": statistics.mode(popularity),
        "median": statistics.median(popularity)
      }
  }

  return response