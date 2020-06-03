import requests

# DECLARES THE BASE URL OF THE API
base = "https://connect.nicapi.eu/api/v1/{endpoint}?authToken={API_TOKEN}"


def get_handles(api_token):
    """
    RETURNS ALL DOMAIN HANDLES
    :param api_token: DECLARES THE API TOKEN
    :return: RETURNS DECODED LIST
    """

    r = requests.get(base.format(endpoint="domain/handles", API_TOKEN=api_token))

    return r.json()

