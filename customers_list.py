# Create an empty list
customers_list = []

while True:

    # Get input for (yes/no) using y or n 
    customers_entry = input('Enter customer (yes/no): ')
    customers_entry = customers_entry[0].lower()

    if customers_entry == 'n':
        break

    else:
        # split the input into 3 variables as "Fname, Mname, Lname" format. 
        Fname, Mname, Lname = input('Enter customers name: ').split()

        # Appending the dictionary into the empty list.
        customers_list.append({'Fname': Fname, 'Mname': Mname, 'Lname': Lname})


print ()
print ('CUSTOMERS NAMES:')


# Using for loop to iterate through the list of customers name 
for i in customers_list:
    print (customers_list.index(i) +1, '.',  i['Fname'],  i['Mname'], i['Lname'])
 
    # .index() +1 is used in numbering the names of customers 
