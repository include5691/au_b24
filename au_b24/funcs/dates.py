import time

def to_unix_time(datetime: str) -> int:
    """
    Convert an ISO 8601 datetime string with timezone information to Unix time 
    Datetime example: 2024-10-22T23:05:05+03:00
    """
    time_zone = datetime[-6:]
    if time_zone[0] == "+":
        time_zone_bias = int(time_zone[1:3]) * 3600 + int(time_zone[4:6]) * 60
    else:
        time_zone_bias = -int(time_zone[1:3]) * 3600 - int(time_zone[4:6]) * 60
    return int(time.mktime(time.strptime(datetime[:-6], "%Y-%m-%dT%H:%M:%S"))) - time.timezone - time_zone_bias