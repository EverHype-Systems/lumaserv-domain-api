import lumaserv_domain_api.nameserver as nameserver

# DEFINE YOUR API KEY
apikey = "PutYourKeyHere"

# FETCH ALL NAMESERVERS ASSIGNED TO YOUR ACCOUNT
print(nameserver.get_nameservers(apikey))

# FETCH INFORMATION ABOUT ONE NAMESERVER
print(nameserver.get_nameserver(apikey, "ns1.yourDomain.com"))

# CREATE A NAMESERVER
print(nameserver.create_nameserver(apikey, "nsNEW.yourDomain.com"))

# DELETE A NAMESERVER
print(nameserver.delete_nameserver(apikey, "nsOLD.yourDomain.com"))

# REFRESH A NAMESERVER
print(nameserver.update_namserver(apikey, "ns1.yourDomain.com"))
