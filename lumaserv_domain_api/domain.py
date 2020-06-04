import requests

# DECLARES THE self.base URL OF THE API


class Domain:

    def __init__(self, api_token):
        self.api_token = api_token
        self.base = "https://connect.nicapi.eu/api/v1/{endpoint}?authToken={API_TOKEN}"

    def get_domains(self):
        """
        RETURNS ALL ASSIGNED DOMAINS.
        :return: RETURNS DECODED LIST
        """

        r = requests.get(self.base.format(endpoint="domain/domains", API_TOKEN=self.api_token))

        return r.json()

    def get_domain(self, domain):
        """
        RETURNS INFORMATION ABOUT ONE DOMAIN
        :param domain: DECLARES THE DOMAIN TO BE USED
        :return: RETURNS LIST
        """

        r = requests.get(self.base.format(endpoint="domain/domains/show", API_TOKEN=self.api_token), params={
            "domainName": domain
        })

        return r.json()

    def get_auth_info(self, domain):
        """
        RETURNS INFORMATION ABOUT THE AUTH CODE
        :param domain: DECLARES THE DOMAIN TO BE USED
        :return: RETURNS LIST
        """

        r = requests.post(self.base.format(endpoint="domain/domains/authcode", API_TOKEN=self.api_token), params={
            "domainName": domain
        })

        return r.json()

    def get_auth_code(self, domain):
        """
           RETURNS THE AUTH CODE FOR ONE DOMAIN
           :param domain: DECLARES THE DOMAIN TO BE USED
           :return: RETURNS LIST
           """

        return self.get_auth_info(self.api_token, domain)["data"]["domain"]["authinfo"]

    def check_availability(self, domain):
        """
        RETURNS INFORMATION ABOUT THE AUTH CODE
        :param domain: DECLARES THE DOMAIN TO BE USED
        :return: RETURNS LIST
        """

        r = requests.post(self.base.format(endpoint="domain/domains/check", API_TOKEN=self.api_token), params={
            "domainName": domain
        })

        return r.json()

    def order_domain(self, domainName, ownerC, adminC, techC, zoneC, ns1, ns2, ns3=None, ns4=None, ns5=None,
                     user=None,
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
        :return: RETURNS LIST
        """

        r = requests.post(self.base.format(endpoint="domain/domains/create", API_TOKEN=self.api_token), params={
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

    def delete_domain(self, domainName, date=None):
        """
        Deletes a domain.
        :param domainName:
        :param date: OPTIONAL
        :return:
        """
        r = requests.delete(self.base.format(endpoint="domain/domains/delete", API_TOKEN=self.api_token), params={
            "domainName": domainName,
            "date": date
        })

        return r.json()

    def undelete_domain(self, domainName):
        """
        Removes the deletion task if date for deletion was set.
        :param domainName:
        :return:
        """
        r = requests.post(self.base.format(endpoint="domain/domains/undelete", API_TOKEN=self.api_token), params={
            "domainName": domainName,
        })

        return r.json()

    def update_domain(self, domainName, ownerC, adminC, techC, zoneC, ns1, ns2, ns3=None, ns4=None, ns5=None,
                      user=None):
        """
        Updates A DOMAINS
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
        :return: RETURNS LIST
        """

        r = requests.post(self.base.format(endpoint="domain/domains/edit", API_TOKEN=self.api_token), params={
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
        })

        return r.json()

    def restore_domain(self, domainName):
        """
        RESTORES A DOMAINS
        :param domainName:
        :return: RETURNS LIST
        """

        r = requests.post(self.base.format(endpoint="domain/domains/restore", API_TOKEN=self.api_token), params={
            "domainName": domainName,
        })

        return r.json()

    def get_tlds(self):
        """
        FETCHES ALL AVAILABLE TLDs
        :return: RETURNS LIST
        """

        r = requests.get(self.base.format(endpoint="domain/domains/tlds", API_TOKEN=self.api_token))

        return r.json()

    def get_domain_prices(self):
        """
        FETCHES THE CURRENT PRICING
        :return: RETURNS LIST
        """

        r = requests.get(self.base.format(endpoint="accounting/pricing/domains", API_TOKEN=self.api_token))

        return r.json()

    def get_domain_discounts(self):
        """
        FETCHES THE CURRENT DOMAIN DISCOUNTS
        :return: RETURNS LIST
        """

        r = requests.get(self.base.format(endpoint="accounting/pricing/domains/discounts", API_TOKEN=self.api_token))

        return r.json()
