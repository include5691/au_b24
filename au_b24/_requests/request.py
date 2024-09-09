import json
import logging
import requests
from requests.exceptions import RequestException
from json.decoder import JSONDecodeError
from ._url import get_url

def post(method: str, data: dict) -> list | dict | None:
    """Post request method for b24 with given data"""
    if not isinstance(method, str) or not isinstance(data, dict):
        return None
    url = get_url(method)
    try:
        with requests.Session() as session:
            response = session.post(url=url, json=data, timeout=10)
            if response.status_code != 200:
                logging.error(f"Error in posting method, code: {response.status_code}")
                return None
            text: bytes = response.text
    except RequestException as e:
        logging.error(f"Error in posting method: {e}")
        return None
    try:
        return json.loads(text).get("result")
    except JSONDecodeError as e:
        logging.error(f"Error in posting method, loading json: {e}")
        return None

def get(method: str, data: dict) -> dict | None:
    """Get request method for b24 which method allowing passing only id"""
    if not isinstance(method, str) or not isinstance(data, dict):
        return None
    if "." not in method or method.split(".")[-1] != "get":
        return None
    url = get_url(method)
    try:
        with requests.Session() as session:
            response = session.get(url=url, params=data, timeout=10)
            if response.status_code != 200:
                logging.error(f"Error in posting method, code: {response.status_code}")
                return None
            text: bytes = response.text
    except RequestException as e:
        logging.error(f"Error in getting method: {e}")
        return None
    try:
        return json.loads(text).get("result")
    except JSONDecodeError as e:
        logging.error(f"Error in getting method, loading json: {e}")
        return None