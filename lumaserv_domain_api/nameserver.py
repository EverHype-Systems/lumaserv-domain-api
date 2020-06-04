import requests


class Nameserver:

    def __init__(self, api_token):
        self.api_token = api_token
        self.base = "https://connect.nicapi.eu/api/v1/{endpoint}?authToken={API_TOKEN}"

    def get_nameservers(self):
        """
        FETCHES ALL ASSIGNED NAMESERVERS
        :return:
        """

        r = requests.get(self.base.format(endpoint="domain/nameservers", API_TOKEN=self.api_token))

        return r.json()

    def get_nameserver(self, nameserver):
        """
        GET INFORMATION FOR ONE NAMESERVER
        :param nameserver:
        :return:
        """

        r = requests.get(self.base.format(endpoint="domain/nameservers/show", API_TOKEN=self.api_token), params={
            "nameserver": nameserver
        })

        return r.json()

    def create_nameserver(self, nameserver):
        """
        CREATES A NEW NAMESERVER
        :param nameserver:
        :return:
        """

        r = requests.post(self.base.format(endpoint="domain/nameservers/create", API_TOKEN=self.api_token), params={
            "nameserver": nameserver
        })

        return r.json()

    def delete_nameserver(self, nameserver):
        """
        DELETES A CREATED NAMESERVER
        :param nameserver:
        :return:
        """

        r = requests.delete(self.base.format(endpoint="domain/nameservers/delete", API_TOKEN=self.api_token), params={
            "nameserver": nameserver
        })

        return r.json()

    def update_namserver(self, nameserver):
        """
        UPDATED A  NAMESERVER
        :param nameserver:
        :return:
        """

        r = requests.post(self.base.format(endpoint="domain/nameservers/refresh", API_TOKEN=self.api_token), params={
            "nameserver": nameserver
        })

        return r.json()
