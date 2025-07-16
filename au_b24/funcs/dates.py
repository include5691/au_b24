import time

def to_unix_time(datetime: str) -> int:
    """
    Convert an ISO 8601 datetime string with timezone information to Unix time. Also supports short date format.
    Datetime example: 2024-10-22T23:05:05+03:00
    Short date example: 14.10.1997
    """
    if not datetime or not isinstance(datetime, str) or len(datetime) < 25 and len(datetime) != 10:
        return
    if len(datetime) == 10:
        datetime = f"{datetime[6:10]}-{datetime[3:5]}-{datetime[:2]}T00:00:00+00:00"
    time_zone = datetime[-6:]
    if time_zone[0] == "+":
        time_zone_bias = int(time_zone[1:3]) * 3600 + int(time_zone[4:6]) * 60
    else:
        time_zone_bias = -int(time_zone[1:3]) * 3600 - int(time_zone[4:6]) * 60
    return int(time.mktime(time.strptime(datetime[:-6], "%Y-%m-%dT%H:%M:%S"))) - time.timezone - time_zone_bias