"""Actions with websites."""

import requests


def check(site: dict) -> bool:
    """Check if site is available."""

    settings = site['settings']

    success = True
    r = None

    try:
        r = requests.request(settings['method'], site['url'], headers=settings['headers'], data=settings['body'],
                             proxies=settings['proxy'])
    except Exception:
        success = False

    return success and is_status_code_good(settings["expected_codes"], r.status_code) and is_answer_good(
        settings["expected_answer"], r.text)


def is_status_code_good(expected_codes: list, status_code: int) -> bool:
    """Check if status_code is in expected_codes

    If expected_code is None, checks if status_code is from 200 to 299
    """
    return (expected_codes is None and (200 <= status_code < 300)) or (status_code in expected_codes)


def is_answer_good(expected_answer: str, response: str) -> bool:
    """Check if anser is in expected_codes

    If expected_code is None, checks if status_code is from 200 to 299
    """

    is_accepting_any_answer = expected_answer is None or expected_answer is ''
    return is_accepting_any_answer or response == expected_answer
