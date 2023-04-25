import json
import statistics

from flask_api import status
from flask import Response

def metrics_of_time(time_arr):
    response = dict()
    response["mean"] = mean(time_arr)
    response["median"] = median(time_arr)
    response["mode"] = statistics.mode(time_arr)
    return response

def mean(time_arr):
    sum_seconds = 0
    for time in time_arr:
        stime = str(time)
        if (int(stime.split(".")[0]) > 0):
            sum_seconds += (int(stime.split(".")[0]) * 60)
        sum_seconds += int(stime.split(".")[1])
    
    mean_seconds = sum_seconds / len(time_arr)
    m, s = divmod(mean_seconds, 60)
    m = int(m)
    s = int(s)
    if s<10:
        s = "0"+str(s)
    
    return float(f"{m}.{s}")

def median(time_arr):
    time_arr.sort()
    if len(time_arr) == 1:
        return time_arr[0]
    if (len(time_arr) % 2) == 0:
        idx1, idx2 = int(len(time_arr)/2), int(len(time_arr)/2) - 1
        return mean([time_arr[idx2], time_arr[idx1]])
    else:
        idx = int(len(time_arr)/2)
        return time_arr[idx]

def make_response(body, status_code):
    return Response(
        json.dumps(body),
        status=status_code,
        mimetype="application/json"
    )

def make_error(mensage, status_code):
    return Response(
        json.dumps({"error": mensage}),
        status=status_code,
        mimetype="application/json"
    )

STANDARD_ERROR = make_error('Something wrong happened.', status.HTTP_500_INTERNAL_SERVER_ERROR)

METHOD_NOT_DEFINED = make_error('Method not defined/', status.HTTP_500_INTERNAL_SERVER_ERROR)