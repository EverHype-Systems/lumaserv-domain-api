import requests
import json

# DECLARES THE BASE URL OF THE API
base = "https://connect.nicapi.eu/api/v1/{endpoint}?authToken={API_TOKEN}"


def get_domains(api_token):
    """
    RETURNS ALL ASSIGNED DOMAINS.
    :param api_token: DECLARES THE API TOKEN
    :return: RETURNS DECODED LIST
    """

    r = requests.get(base.format(endpoint="domain/domains", API_TOKEN=api_token))

    return r.json()
