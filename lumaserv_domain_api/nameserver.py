import requests

# DECLARES THE BASE URL OF THE API
base = "https://connect.nicapi.eu/api/v1/{endpoint}?authToken={API_TOKEN}"


def get_nameservers(api_token):
    """
    FETCHES ALL ASSIGNED NAMESERVERS
    :param api_token:
    :return:
    """

    r = requests.get(base.format(endpoint="domain/nameservers", API_TOKEN=api_token))

    return r.json()


def get_nameserver(api_token, nameserver):
    """
    GET INFORMATION FOR ONE NAMESERVER
    :param nameserver:
    :param api_token:
    :return:
    """

    r = requests.get(base.format(endpoint="domain/nameservers/show", API_TOKEN=api_token), params={
        "nameserver": nameserver
    })

    return r.json()


def create_nameserver(api_token, nameserver):
    """
    CREATES A NEW NAMESERVER
    :param api_token:
    :param nameserver:
    :return:
    """

    r = requests.post(base.format(endpoint="domain/nameservers/create", API_TOKEN=api_token), params={
        "nameserver": nameserver
    })

    return r.json()


def delete_nameserver(api_token, nameserver):
    """
    DELETES A CREATED NAMESERVER
    :param api_token:
    :param nameserver:
    :return:
    """

    r = requests.delete(base.format(endpoint="domain/nameservers/delete", API_TOKEN=api_token), params={
        "nameserver": nameserver
    })

    return r.json()

