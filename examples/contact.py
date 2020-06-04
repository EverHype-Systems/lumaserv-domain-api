from lumaserv_domain_api.contact import Contact

# DEFINE YOUR API KEY
apikey = "PutYourKeyHere"

contact = Contact(apikey)

# FETCH ALL YOUR CREATED CONTACTS
print(contact.get_handles())

# FETCH INFORMATION ABOUT ONE CONTACT
# PUT THE HANDLE ID AS 2. PARAM
print(contact.get_handle("ABCDEF"))

# GET ALL AVAILABLE COUNTRIES
print(contact.get_countries())

# DELETE HANDLE/CONTACT
print(contact.delete_handle("ABCDEF"))

# EDIT A CONTACT/HANDLE
print(contact.edit_handle("ABCDEF", "Street", 11, "36037", "Fulda", "Hessen", "DE", "customer@service.com"))








