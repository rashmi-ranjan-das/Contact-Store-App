import sqlite3
import database_handle

def create_table(db,table,**col):
    cur = db.cursor()
    query = ''
    for key,val in col.items():
        query = query + '{} {}, '.format(key,val)
    query = query[:-2]
    cur.execute('create table if not exists {}({})'.format(table,query))
    db.commit()
    cur.close()

def add_contact(db,table,**col):
    try:
        num = int(col['number'])
        ctr = database_handle.search_contact_for_edit_by_name(db,table,col['name'])
        if ctr == 1:
            print('Contact already exists...')
            print()
        else:
            col_str = ''
            val_str = ''
            values = []
            for c in col:
                col_str += '{}, '.format(c)
                val_str += '?,'
                values.append(col[c])
            col_str = col_str[:-2]
            val_str = val_str[:-1]
            cur = db.cursor()
            cur.execute('insert into {} ({}) values({})'.format(table,col_str,val_str),values)
            print('Contact Added Successfully...')
            print()
            db.commit()
            cur.close()
    except:
        print('Invalid Number')
        print()