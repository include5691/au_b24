import time
import json
import logging
import requests
from requests import Response
from requests.exceptions import RequestException
from json.decoder import JSONDecodeError
from ._url import get_url
from ._init import pause_

def post(method: str, data: dict, usertoken: str | None = None) -> list | dict | None:
    """
    Post request method for b24 with given data
    If usertoken is given - it will be used as auth token instead of one from .env file
    """
    if not isinstance(method, str) or not isinstance(data, dict):
        return None
    url = get_url(method=method, usertoken=usertoken)
    global pause_
    if pause_:
        time.sleep(pause_)
    try:
        with requests.Session() as session:
            response = session.post(url=url, json=data, timeout=10)
            if response.status_code != 200:
                logging.debug(f"Error in posting method, code: {response.status_code} with response: {response.text}")
                return None
            json = response.json()
            if not json or not isinstance(json, dict):
                return None
            if "result" in json:
                return json["result"]
            return None
    except RequestException as e:
        logging.error(f"Error in posting method {method}: {e}")
        return None

def get(method: str, data: dict) -> dict | None:
    """Get request method for b24 which method allowing passing only id"""
    if not isinstance(method, str) or not isinstance(data, dict):
        return None
    if "." not in method or method.split(".")[-1] != "get":
        return None
    url = get_url(method)
    if not url:
        return None
    global pause_
    if pause_:
        time.sleep(pause_)
    try:
        with requests.Session() as session:
            response = session.get(url=url, params=data, timeout=10)
            if response.status_code != 200:
                logging.debug(f"Error in posting method, code: {response.status_code} with response: {response.text}")
                return None
            json = response.json()
            if not json or not isinstance(json, dict):
                return None
            if "result" in json:
                return json["result"]
            return None
    except RequestException as e:
        logging.error(f"Error in posting method {method}: {e}")
        return None