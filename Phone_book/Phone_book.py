def Phone_book(contacts):

    for i in range(5):

        contact_name = input('Enter contact name: ')
        contact_number = input('Enter contact number: ')

        contacts[contact_name] = contact_number

    return contacts



contacts = {}
(Phone_book(contacts))

print ('\n----- Contact-list -----')
for key, value in contacts.items():
        contacts = {key: value}
        print (contacts)
