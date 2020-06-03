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


def get_handle(api_token, handle):
    """
    RETURNS ONE DOMAIN HANDLE
    :param handle: HANDLE ID
    :param api_token: DECLARES THE API TOKEN
    :return: RETURNS DECODED LIST
    """

    r = requests.get(base.format(endpoint="domain/handles/show", API_TOKEN=api_token), params={
        "handle": handle
    })

    return r.json()


def get_countries(api_token):
    """
    RETURNS ALL AVAILABLE COUNTRIES
    :param api_token: DECLARES THE API TOKEN
    :return: RETURNS DECODED LIST
    """

    r = requests.get(base.format(endpoint="domain/handles/countries", API_TOKEN=api_token))

    return r.json()


def create_handle(api_token, handle_type, sex, firstname, lastname, organisation, street, number, postcode, city, region,
                  country, email, countryofbirth=None, user=None, dateofbirth=None):
    """
    CREATES A DOMAIN CONTACT
    :return:
    :param api_token:
    :param handle_type:
    :param sex:
    :param firstname:
    :param lastname:
    :param organisation:
    :param street:
    :param number:
    :param postcode:
    :param city:
    :param region:
    :param country:
    :param email:
    :param countryofbirth: OPTIONAL
    :param user: OPTIONAL
    :param dateofbirth: OPTIONAL
    :return:
    """

    r = requests.post(base.format(endpoint="domain/handles/create", API_TOKEN=api_token), params={
        "type": handle_type,
        "sex": sex,
        "firstname": firstname,
        "lastname": lastname,
        "organisation": organisation,
        "street": street,
        "number": number,
        "postcode": postcode,
        "city": city,
        "region": region,
        "country": country,
        "email": email,
        "countryofbirth": countryofbirth,
        "user": user,
        "dateofbirth": dateofbirth
    })

    return r.json()


def delete_handle(api_token, handle):
    """
    DELETE A CREATED CONTACT/HANDLE
    :param api_token:
    :param handle:
    :return:
    """

    r = requests.delete(base.format(endpoint="domain/handles/delete", API_TOKEN=api_token), params={
        "handle": handle
    })

    return r.json()


def edit_handle(api_token, handle, organisation=None, street, number, postcode, city, region, country, email,
                countryofbirth=None, user=None):
    """
    EDIT A CREATED CONTACT/HANDLE
    :param api_token:
    :param handle:
    :param organisation:
    :param street:
    :param number:
    :param postcode:
    :param city:
    :param region:
    :param country:
    :param email:
    :param countryofbirth:
    :param user:
    :return:
    """

    r = requests.post(base.format(endpoint="domain/handles/edit", API_TOKEN=api_token), params={
        "handle": handle,
        "organisation": organisation,
        "street": street,
        "number": number,
        "postcode": postcode,
        "city": city,
        "region": region,
        "country": country,
        "email": email,
        "countryofbirth": countryofbirth,
        "user": user
    })

    return r.json()
