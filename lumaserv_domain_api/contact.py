import requests


class Contact:

    def __init__(self, api_token):
        self.api_token = api_token
        self.base = "https://connect.nicapi.eu/api/v1/{endpoint}?authToken={API_TOKEN}"

    def get_handle(self, handle):
        """
        RETURNS ONE DOMAIN HANDLE
        :param handle: HANDLE ID
        :return: RETURNS DECODED LIST
        """
    
        r = requests.get(self.base.format(endpoint="domain/handles/show", API_TOKEN=self.api_token), params={
            "handle": handle
        })
    
        return r.json()

    def get_countries(self):
        """
        RETURNS ALL AVAILABLE COUNTRIES
        :return: RETURNS DECODED LIST
        """
    
        r = requests.get(self.base.format(endpoint="domain/handles/countries", API_TOKEN=self.api_token))
    
        return r.json()

    def create_handle(self, handle_type, sex, firstname, lastname, organisation, street, number, postcode, city, region,
                      country, email, phone, countryofbirth=None, user=None, dateofbirth=None):
        """
        CREATES A DOMAIN CONTACT
        :return:
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
        :param phone:
        :param countryofbirth: OPTIONAL
        :param user: OPTIONAL
        :param dateofbirth: OPTIONAL
        :return:
        """
    
        r = requests.post(self.base.format(endpoint="domain/handles/create", API_TOKEN=self.api_token), params={
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
            "phone": phone,
            "countryofbirth": countryofbirth,
            "user": user,
            "dateofbirth": dateofbirth
        })
    
        return r.json()

    def delete_handle(self, handle):
        """
        DELETE A CREATED CONTACT/HANDLE
        :param api_token:
        :param handle:
        :return:
        """
    
        r = requests.delete(self.base.format(endpoint="domain/handles/delete", API_TOKEN=self.api_token), params={
            "handle": handle
        })
    
        return r.json()

    def edit_handle(self, handle, street, number, postcode, city, region, country, email, phone,
                    countryofbirth=None, user=None, organisation=None):
        """
        EDIT A CREATED CONTACT/HANDLE
        :param handle:
        :param organisation:
        :param street:
        :param number:
        :param postcode:
        :param city:
        :param region:
        :param country:
        :param email:
        :param phone:
        :param countryofbirth:
        :param user:
        :return:
        """
    
        r = requests.post(self.base.format(endpoint="domain/handles/edit", API_TOKEN=self.api_token), params={
            "handle": handle,
            "organisation": organisation,
            "street": street,
            "number": number,
            "postcode": postcode,
            "city": city,
            "region": region,
            "country": country,
            "email": email,
            "phone": phone,
            "countryofbirth": countryofbirth,
            "user": user
        })
    
        return r.json()
