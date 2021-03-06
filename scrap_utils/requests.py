import time
import logging

import requests


class MaxTryReached(Exception):
    """Error when max trial has been reached"""
    pass


def requests_get(url, sleep_time=30, max_try=5, trials=0,
                 **requests_kwargs):
    """
    Send a GET request with requests library.

    Keep retrying till max_try when there's a bad code or error.
    The motivation are server(5xx) errors and network issues,
    which simply require trying again.

    Parameters
    ----------
    url: str
        URL for the new Request object.
    sleep_time: int, default 30
        The seconds to sleep before retrying (if there's error).
    max_try: int, default 5
        The maximum number of trial before raising error.
    trials: int, default 0
        The number of times the request has been sent.
    **requests_kwargs:
        Optional arguments that request takes.

    Returns
    -------
    response: requests.Response object

    References
    ----------
    .. [1] `requests.get() documentation
        <https://requests.readthedocs.io/en/latest/api/#requests.get>`_
    """
    trials += 1
    try:
        response = requests.get(url, **requests_kwargs)
        if response.status_code == 200:
            return response
        else:
            logging.warning(
                f"Requests GET Bad Status Code: {response.status_code}; "
                f"{trials}/{max_try} trials; Sleep Time: {sleep_time}; "
                f"Url: {url}"
            )
    except Exception as e:
        logging.error(
            f"Requests GET Error: {e}; {trials}/{max_try} trials; "
            f"Sleep Time: {sleep_time}; Url: {url}"
        )

    # When there's error or bad status code.
    if trials < max_try:
        time.sleep(sleep_time)
        return requests_get(
            url, sleep_time, max_try, trials, **requests_kwargs
        )
    else:
        raise MaxTryReached(
            f"Max Try of {max_try} has been reached for requests GET."
        )


def requests_post(url, sleep_time=30, max_try=5, trials=0, **requests_kwargs):
    """
    Send a POST request with requests library.

    Keep retrying till max_try when there's a bad code or error.
    The motivation are server(5xx) errors and network issues,
    which simply require trying again.

    Parameters
    ----------
    url: str
        URL for the new Request object.
    sleep_time: int, default 30
        The seconds to sleep before retrying (if there's error).
    max_try: int, default 5
        The maximum number of trial before raising error.
    trials: int, default 0
        The number of times the request has been sent.
    **requests_kwargs:
        Optional arguments that request takes.

    Returns
    -------
    response: requests.Response object

    References
    ----------
    .. [1] `requests.post() documentation
        <https://requests.readthedocs.io/en/latest/api/#requests.post>`_
    """
    trials += 1
    try:
        response = requests.post(url, **requests_kwargs)
        if response.status_code == 200:
            return response
        else:
            logging.warning(
                f"Requests POST Bad Status Code: {response.status_code}; "
                f"{trials}/{max_try} trials; Sleep Time: {sleep_time}; "
                f"Url: {url}"
            )
    except Exception as e:
        logging.error(
            f"Requests POST Error: {e}; {trials}/{max_try} trials; "
            f"Sleep Time: {sleep_time}; Url: {url}"
        )

    # When there's error or bad status code.
    if trials < max_try:
        time.sleep(sleep_time)
        return requests_post(
            url, sleep_time, max_try, trials, **requests_kwargs
        )
    else:
        raise MaxTryReached(
            f"Max Try of {max_try} has been reached for requests POST."
        )
