import requests
from retrying import retry
import uuid


def get_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r
        else:
            raise requests.exceptions.HTTPError
    except:
        raise


def retry_if_HTTP404(exception):
    return isinstance(exception, requests.exceptions.HTTPError)


@retry(stop_max_attempt_number=5, wait_exponential_multiplier=10)
def get_signed_url(signed):
    return get_url(signed)


@retry(retry_on_exception=retry_if_HTTP404)
def get_signed_url_insist(signed):
    r = get_url(signed)
    print(r.text)
    return r
