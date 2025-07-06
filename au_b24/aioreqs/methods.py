import asyncio
import logging
import aiohttp
from aiohttp import ClientError
from ..reqs._url import get_url
from ..reqs._init import pause_

async def post(method: str, data: dict, usertoken: str | None = None) -> list | dict | None:
    """
    Post request method for b24 with given data
    If usertoken is given - it will be used as auth token instead of one from .env file
    """
    if not isinstance(method, str) or not isinstance(data, dict):
        return None
    url = get_url(method=method, usertoken=usertoken)
    global pause_
    if pause_:
        await asyncio.sleep(pause_)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, json=data, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status != 200:
                    response_text = await response.text()
                    logging.debug(f"Error in posting method, code: {response.status} with response: {response_text}")
                    return None
                json_data = await response.json()
                if not json_data or not isinstance(json_data, dict):
                    return None
                if "result" in json_data:
                    return json_data["result"]
                return None
    except ClientError as e:
        logging.error(f"Error in posting method {method}: {e}")
        return None
    except asyncio.TimeoutError as e:
        logging.error(f"Timeout error in posting method {method}: {e}")
        return None

async def get(method: str, data: dict) -> dict | None:
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
        await asyncio.sleep(pause_)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, params=data, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status != 200:
                    response_text = await response.text()
                    logging.debug(f"Error in posting method, code: {response.status} with response: {response_text}")
                    return None
                json_data = await response.json()
                if not json_data or not isinstance(json_data, dict):
                    return None
                if "result" in json_data:
                    return json_data["result"]
                return None
    except ClientError as e:
        logging.error(f"Error in posting method {method}: {e}")
        return None
    except asyncio.TimeoutError as e:
        logging.error(f"Timeout error in posting method {method}: {e}")
        return None