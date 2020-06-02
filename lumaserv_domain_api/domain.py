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


def get_domain(api_token, domain):
    """
    RETURNS INFORMATION ABOUT ONE DOMAIN
    :param domain: DECLARES THE DOMAIN TO BE USED
    :param api_token: DECLARES THE API TOKEN
    :return: RETURNS LIST
    """

    r = requests.get(base.format(endpoint="domain/domains/show", API_TOKEN=api_token), params={
        "domainName": domain
    })

    return r.json()


def get_auth_info(api_token, domain):
    """
    RETURNS INFORMATION ABOUT THE AUTH CODE
    :param domain: DECLARES THE DOMAIN TO BE USED
    :param api_token: DECLARES THE API TOKEN
    :return: RETURNS LIST
    """

    r = requests.post(base.format(endpoint="domain/domains/authcode", API_TOKEN=api_token), params={
        "domainName": domain
    })

    return r.json()


def get_auth_code(api_token, domain):
    """
       RETURNS THE AUTH CODE FOR ONE DOMAIN
       :param domain: DECLARES THE DOMAIN TO BE USED
       :param api_token: DECLARES THE API TOKEN
       :return: RETURNS LIST
       """

    return get_auth_info(api_token, domain)["data"]["domain"]["authinfo"]



