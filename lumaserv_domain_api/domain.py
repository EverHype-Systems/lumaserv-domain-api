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


def check_availabilty(api_token, domain):
    """
    RETURNS INFORMATION ABOUT THE AUTH CODE
    :param domain: DECLARES THE DOMAIN TO BE USED
    :param api_token: DECLARES THE API TOKEN
    :return: RETURNS LIST
    """

    r = requests.post(base.format(endpoint="domain/domains/check", API_TOKEN=api_token), params={
        "domainName": domain
    })

    return r.json()


def order_domain(api_token, domainName, ownerC, adminC, techC, zoneC, ns1, ns2, ns3=None, ns4=None, ns5=None, user=None,
                 years=1, create_zone=None, authinfo=None):
    """
    ORDERS A DOMAINS
    :param authinfo:
    :param create_zone:
    :param years:
    :param user:
    :param ns5:
    :param ns4:
    :param ns3:
    :param ns2:
    :param ns1:
    :param zoneC:
    :param techC:
    :param adminC:
    :param ownerC:
    :param domainName:
    :param api_token: DECLARES THE API TOKEN
    :return: RETURNS LIST
    """

    r = requests.post(base.format(endpoint="domain/domains/create", API_TOKEN=api_token), params={
        "domainName": domainName,
        "ownerC": ownerC,
        "adminC": adminC,
        "techC": techC,
        "zoneC": zoneC,
        "ns1": ns1,
        "ns2": ns2,
        "ns3": ns3,
        "ns4": ns4,
        "ns5": ns5,
        "user": user,
        "years": years,
        "create_zone": create_zone,
        "authinfo": authinfo
    })

    return r.json()


def delete_domain(api_token, domainName, date=None):
    """
    :param api_token:
    :param domainName:
    :param date:
    :return:
    """
    r = requests.delete(base.format(endpoint="domain/domains/delete", API_TOKEN=api_token), params={
        "domainName": domainName,
        "date": date
    })

    return r.json()
