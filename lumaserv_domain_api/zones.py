import requests


class DomainZones:

    def __init__(self, api_token):
        self.api_token = api_token
        self.base = "https://connect.nicapi.eu/api/v1/{endpoint}?authToken={API_TOKEN}"

    def get_zones(self):
        """
        Fetches all zones
        :return:
        """
        r = requests.get(self.base.format(endpoint="dns/zones", API_TOKEN=self.api_token))

        return r.json()

    def get_zone(self, zone):
        """
        Fetches one zone
        :param zone:
        :return:
        """
        r = requests.get(self.base.format(endpoint="dns/zones/show", API_TOKEN=self.api_token), params={
            "zone": zone
        })

        return r.json()

    def add_entry(self, zone, records):
        """
        Adds the requested entrys. Please keep in mind: records is an array. Please read the API Docs.
        :param zone:
        :param records: array
        :return:
        """

        r = requests.get(self.base.format(endpoint="/dns/zones/records/add", API_TOKEN=self.api_token), params={
            "zone": zone,
            "records": records,
        })

        return r.json()

    def remove_entry(self, zone, records):
        """
        removed one or more entrys. Please provide the full record which should be deleted.
        :param zone: Zone ID
        :param records: array(name, ttl, type, data)
        :return:
        """

        r = requests.delete(self.base.format(endpoint="/dns/zones/records/delete", API_TOKEN=self.api_token), params={
            "zone": zone,
            "records": records,
        })

        return r.json()

    def refresh_zone(self, zone):
        """
        Refreshes the zone on the nameserver
        :param zone:
        :return:
        """

        r = requests.post(self.base.format(endpoint="/dns/zones/refresh", API_TOKEN=self.api_token), params={
            "zone": zone,
        })

        return r.json()
