import sqlite3

def search_contact_name_for_delete(db,table,name):
    cur = db.cursor()
    query = 'select * from {} where name="{}"'.format(table,name)
    for ele in cur.execute(query):
        if name in ele:
            return 1
    return 0

def search_contact_for_edit_by_number(db,table,number):
    cur = db.cursor()
    query = 'select * from {} where number="{}"'.format(table,number)
    for ele in cur.execute(query):
        if number in ele:
            return 1
    return 0

def search_contact_for_edit_by_name(db,table,name):
    cur = db.cursor()
    query = 'select * from {} where name="{}"'.format(table,name)
    for ele in cur.execute(query):
        if name in ele:
            return 1
    return 0


def delete_contact(db,table,name):
    cur = db.cursor()
    flag = search_contact_name_for_delete(db,table,name)
    if flag == 1:
        query = 'delete from {} where name="{}"'.format(table,name)
        cur.execute(query)
        print('Contact Deleted Successfully...')
        print()
    else:
        print('Contact Doesnt Exist..')
        print()
    db.commit()
    cur.close()

def edit_contact(db,table):
    ch = input('Do you want to edit contact by Number (Enter NU) or by Name (Enter NA) ? : ')
    if ch == 'NU' or ch == 'Nu' or ch == 'nU' or ch == 'nu':
        cur = db.cursor()
        number = input('Enter Contact Number : ')
        ctr = search_contact_for_edit_by_number(db,'Contact_Store',number)
        if ctr == 0:
            print('Number doesnt belong to any contact...')
            print()
            return
        else:
            ch1 = input('Do you want to change Name(N) or Email(E) or Category(C)? : ')
            if ch1 == 'N' or ch1 == 'n':
                name = input('Enter New Name : ')
                query = 'update {} set name="{}" where number="{}"'.format(table,name,number)
                cur.execute(query)
                db.commit()
                cur.close()
                print('Contact Name updated Successfully...')
                print()
            elif ch1 == 'E' or ch1 == 'e':
                email = input('Enter New Email : ')
                query = 'update {} set email="{}" where number="{}"'.format(table,email,number)
                cur.execute(query)
                db.commit()
                cur.close()
                print('Contact Email updated Successfully...')
                print()
            elif ch1 == 'C' or ch1 == 'c':
                category = input('Enter New Category : ')
                query = 'update {} set category="{}" where number="{}"'.format(table,category,number)
                cur.execute(query)
                db.commit()
                cur.close()
                print('Contact Category updated Successfully...')
                print()
            else:
                print('Invalid Choice...')
                print()
    elif ch == 'NA' or ch == 'Na' or ch == 'nA' or ch == 'na':
        cur = db.cursor()
        name = input('Enter Contact Name : ')
        ctr = search_contact_for_edit_by_name(db,'Contact_Store',name)
        if ctr == 0:
            print('Name doesnt belong to any contact...')
            print()
            return
        else:
            ch1 = input('Do you want to change Number(N) or Email(E) or Category(C)? : ')
            if ch1 == 'N' or ch1 == 'n':
                number = input('Enter New Number : ')
                query = 'update {} set number="{}" where name="{}"'.format(table,number,name)
                cur.execute(query)
                db.commit()
                cur.close()
                print('Contact Number updated Successfully...')
                print()
            elif ch1 == 'E' or ch1 == 'e':
                email = input('Enter New Email : ')
                query = 'update {} set email="{}" where name="{}"'.format(table,email,name)
                cur.execute(query)
                db.commit()
                cur.close()
                print('Contact Email updated Successfully...')
                print()
            elif ch1 == 'C' or ch1 == 'c':
                category = input('Enter New Category : ')
                query = 'update {} set category="{}" where name="{}"'.format(table,category,name)
                cur.execute(query)
                db.commit()
                cur.close()
                print('Contact Category updated Successfully...')
                print()
            else:
                print('Invalid Choice...')
                print()
    else:
        print('Invalid Choice')
        print()

def show_all_contacts(db,table):
    cur = db.cursor()
    query = 'select * from {}'.format(table)
    flag = 0
    for ele in cur.execute(query):
        print('Name: ',ele[0])
        print('Number: ',ele[1])
        print('Email: ',ele[2])
        print('Category: ',ele[3])
        print()
        flag = 1
    print()
    db.commit()
    cur.close()
    if flag == 0:
        return 0
    else:
        return 1

def search_contact_by_name(db,table,name):
    cur = db.cursor()
    query = 'select * from {} where name="{}"'.format(table,name)
    flag = 0
    for ele in cur.execute(query):
        if name in ele:
            print('Name: ',ele[0])
            print('Number: ',ele[1])
            print('Email: ',ele[2])
            print('Category: ',ele[3])
        print()
        flag = 1
    print()
    db.commit()
    cur.close()
    if flag == 0:
        return 1
    else:
        return 0

def search_contact_by_number(db,table,number):
    cur = db.cursor()
    query = 'select * from {} where number="{}"'.format(table,number)
    flag = 0
    for ele in cur.execute(query):
        if number in ele:
            print('Name: ',ele[0])
            print('Number: ',ele[1])
            print('Email: ',ele[2])
            print('Category: ',ele[3])
        print()
        flag = 1
    print()
    db.commit()
    cur.close()
    if flag == 0:
        return 1
    else:
        return 0

def search_contact_by_category(db,table,category):
    cur = db.cursor()
    query = 'select * from {} where category="{}"'.format(table,category)
    flag = 0
    for ele in cur.execute(query):
        if category in ele:
            print('Name: ',ele[0])
            print('Number: ',ele[1])
            print('Email: ',ele[2])
            print('Category: ',ele[3])
        print()
        flag = 1
    print()
    db.commit()
    cur.close()
    if flag == 0:
        return 1
    else:
        return 0