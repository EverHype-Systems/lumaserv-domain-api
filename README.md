
# LumaServ Systems Domain API
This wrapper is used for communication with the Lumaserv System Domain API. The API documentation can be found at https://docs.nicapi.eu/de/docs.
## Implemented Features

 - [x] Domains
	 - [x] Get domains 
	 - [x] Get one domain
	 - [x] Get authcode
	 - [x] Check availability of domains
	 - [x] Order domain [**WARNING: RUNS AN ORDER => PAYMENT**]
	 - [x] Delete domain
	 - [x] Undelete domain
	 - [x] Update domain
	 - [x] Restore Domain
	 - [x] Get all available domain tlds
	 - [x] Get domain price list
	 - [x] Get domain price offers
 - [x] Contacts/Handle
	 - [x] Get contacts/handles
	 - [x] Get one contact/handle
	 - [x] Get countries
	 - [x] Create contact/handle
	 - [x] Delete contact/handle
	 - [x] Update contact/handle
 - [x] Nameserver
	 - [x] Get nameservers
	 - [x] Get one nameserver
	 - [x] Create nameserver
	 - [x] Delete nameserver
	 - [x] Update nameserver

## Usage of Domains
Please note that you have to pass your API_TOKEN at every request.
```python
import lumaserv_domain_api.domain as domain

# DEFINE YOUR API KEY
apikey = "PutYourKeyHere"

# FETCH ALL DOMAINS ASSIGNED TO YOUR ACCOUNT
print(domain.get_domains(apikey))

# FETCH ONE DOMAIN
# PASS THE DOMAIN AS A STRING 
print(domain.get_domain(apikey, "domain.com")) 

# GET AUTH INFORMATION
# PASS THE DOMAIN AS A STRING
# YOUR REQEUST THE API TO GENERATE AN NEW AUTH-CODE
print(domain.get_auth_info(apikey, "domain.com"))

# GET THE AUTHCODE DIRECTLY
# PASS THE DOMAIN AS A STRING
print(domain.get_auth_code(apikey, "domain.com"))

# CHECK IF THE DOMAIN CAN BE REGISTERED OR IS TAKEN
print(domain.check_availability(apikey, "domain.com"))

# ORDER A NEW DOMAIN
# PLEASE NOTE: YOU HAVE TO CREATE A CONTACT/HANDLE first, so that you can pass them as domain contact!
print(domain.order_domain(apikey, "domain.com", "OWNER_CONTACT", "ADMIN_CONTACT", "TECH_CONTACT", "ZONE_CONTACT", "ns1.yourserver.com", "ns2.yourserver.com"))


```

For more examples and how to use this wrapper, check the folder /examples/
