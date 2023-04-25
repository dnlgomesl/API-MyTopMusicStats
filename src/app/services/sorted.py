def sort_arr_dict(arr, sort_type):
    try:
        if sort_type == "duration":
            return sorted(arr, key=lambda d: d['duration'], reverse=True)
        elif sort_type == "popularity":
            return sorted(arr, key=lambda d: d['popularity'], reverse=True)
        else:
            return arr
    except:
        return arr