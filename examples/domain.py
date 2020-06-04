from lumaserv_domain_api.domain import Domain

# DEFINE YOUR API KEY
apikey = "PutYourKeyHere"

domain = Domain(apikey)

# FETCH ALL DOMAINS ASSIGNED TO YOUR ACCOUNT
print(domain.get_domains())

# FETCH ONE DOMAIN
# PASS THE DOMAIN AS A STRING
print(domain.get_domain("domain.com"))

# GET AUTH INFORMATION
# PASS THE DOMAIN AS A STRING
# YOUR REQUEST THE API TO GENERATE AN NEW AUTH-CODE
print(domain.get_auth_info("domain.com"))

# GET THE AUTHCODE DIRECTLY
# PASS THE DOMAIN AS A STRING
print(domain.get_auth_code("domain.com"))

# CHECK IF THE DOMAIN CAN BE REGISTERED OR IS TAKEN
print(domain.check_availability("domain.com"))

# ORDER A NEW DOMAIN
# PLEASE NOTE: YOU HAVE TO CREATE A CONTACT/HANDLE FIRST, SO THAT YOU CAN PASS THEM!
# Nameserver 3 to 5 are optional
# CREATE_ZONE is optional
# authInfo is required if you want to transfer a domain
# years (default 1)
print(domain.order_domain("domain.com", "OWNER_CONTACT", "ADMIN_CONTACT", "TECH_CONTACT", "ZONE_CONTACT",
                          "ns1.yourserver.com", "ns2.yourserver.com"))

# DELETE AN ORDERED DOMAIN
# OPTIONAL: DATE FOR DELETION
print(domain.delete_domain("domain.com", "2020-12-01"))

# REMOVE THE DELETION REQUEST
print(domain.undelete_domain("domain.com"))

# UPDATE DOMAIN INFORMATION
# PLEASE NOTE: YOU HAVE TO CREATE A CONTACT/HANDLE FIRST, SO THAT YOU CAN PASS THEM!
print(domain.update_domain("domain.com",
                           "OWNER_CONTACT",
                           "ADMIN_CONTACT",
                           "TECH_CONTACT",
                           "ZONE_CONTACT",
                           "ns1.yourserver.com",
                           "ns2.yourserver.com"
                           ))

# RESTORE A DOMAIN
print(domain.restore_domain("domain.com"))

# FETCH ALL AVAILABLE TLDs
print(domain.get_tlds())

# GET THE CURRENT PRICING FOR YOUR ACCOUNT
print(domain.get_domain_prices())

# GET THE CURRENT DOMAIN DISCOUNTS
print(domain.get_domain_discounts())
