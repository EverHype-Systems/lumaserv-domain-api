import lumaserv_domain_api.contact as contact

# DEFINE YOUR API KEY
apikey = "PutYourKeyHere"

# FETCH ALL YOUR CREATED CONTACTS
print(contact.get_handles(apikey))

# FETCH INFORMATION ABOUT ONE CONTACT
# PUT THE HANDLE ID AS 2. PARAM
print(contact.get_handle(apikey, "ABCDEF"))

# GET ALL AVAILABLE COUNTRIES
print(contact.get_countries(apikey))

# DELETE HANDLE/CONTACT
print(contact.delete_handle(apikey, "ABCDEF"))

# EDIT A CONTACT/HANDLE
print(contact.edit_handle(apikey, "ABCDEF", "Street", 11, "36037", "Fulda", "Hessen", "DE", "customer@service.com"))








