import sqlite3
import input_handle
import database_handle

print('**************************************************Welcome to the Contact Manager App******************************************************')

def console():
    print('1. ADD CONTACT \n2. DELETE CONTACT \n3. EDIT CONTACT \n4. VIEW ALL CONTACTS \n5. SEARCH CONTACT BY NAME \n6. SEARCH CONTACT BY NUMBER \n7. SEARCH CONTACT BY CATEGORY \n8. EXIT APP \n')

db = sqlite3.connect('Contacts.db')
input_handle.create_table(db, 'Contact_Store',name='text',number='text',email='text',category='text')

while 1:
    console()
    choice = int(input('Enter choice : '))
    print()
    if choice == 8:
        break
    elif choice < 1 or choice > 8:
        print('Invalid Choice')
        print('Exiting App...')
        break
    else:
        if choice == 1:
            name = input('Enter Contact Name : ')
            number = input('Enter Contact Number : ')
            email = input('Enter Contact Email : ')
            category = input('Enter Contact Category : ')
            print()
            input_handle.add_contact(db,'Contact_Store',name=name,number=number,email=email,category=category)
            continue

        if choice == 2:
            name = input('Enter Contact Name to delete : ')
            print()
            database_handle.delete_contact(db,'Contact_Store',name)
            continue

        if choice == 3:
            database_handle.edit_contact(db,'Contact_Store')
            continue

        if choice == 4:
            ctr = database_handle.show_all_contacts(db,'Contact_Store')
            if ctr == 0:
                print('No Contacts are stored yet...')
                print()
            continue

        if choice == 5:
            name = input('Enter Contact Name to search : ')
            print()
            val = database_handle.search_contact_by_name(db,'Contact_Store',name)
            if val == 1:
                print('Contact Doesnt Exist...')
                print()
            continue

        if choice == 6:
            number = input('Enter Contact Number to search : ')
            print()
            val = database_handle.search_contact_by_number(db,'Contact_Store',number)
            if val == 1:
                print('Contact Doesnt Exist')
                print()
            continue

        if choice == 7:
            category = input('Enter Contact Category to search : ')
            print()
            val = database_handle.search_contact_by_category(db,'Contact_Store',category)
            if val == 1:
                print('Contact Doesnt Exist')
                print()
            continue
            