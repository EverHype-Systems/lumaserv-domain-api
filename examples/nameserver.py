from lumaserv_domain_api.nameserver import Nameserver

# DEFINE YOUR API KEY
apikey = "PutYourKeyHere"

nameserver = Nameserver(apikey)

# FETCH ALL NAMESERVERS ASSIGNED TO YOUR ACCOUNT
print(nameserver.get_nameservers())

# FETCH INFORMATION ABOUT ONE NAMESERVER
print(nameserver.get_nameserver("ns1.yourDomain.com"))

# CREATE A NAMESERVER
print(nameserver.create_nameserver("nsNEW.yourDomain.com"))

# DELETE A NAMESERVER
print(nameserver.delete_nameserver("nsOLD.yourDomain.com"))

# REFRESH A NAMESERVER
print(nameserver.update_namserver("ns1.yourDomain.com"))
