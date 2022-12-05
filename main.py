from backend import *

from login_backend import *
import sqlite3 as sql

conn = sql.connect("test1.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS login_table")
cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("DROP TABLE IF EXISTS meds")
cursor.execute("DROP TABLE IF EXISTS inventory_order")

create_table_meds()
create_table_orders()
create_login_table()
create_table_customers()

def insert_items_custs(name,age,sex,address,phone):
    global cursor
    
    insert_cmd = f'''INSERT INTO customers (name,age,sex,address,phone_no) 
                VALUES('{name}','{age}','{sex}','{address}',{phone} );'''
    #print(insert_cmd)
    cursor.execute(insert_cmd)
    conn.commit()

insert_items_custs('Cust1',28,'M','123 Street',42571)
insert_items_custs('Cust2',45,'F','Building 23 Town Center',11111)
insert_items_custs('Cust3',32,'F','Plot 16 East Side',32146)
insert_items_custs('Cust4',60,'M','Richards Villa Main City',24617 )


def insert_items_item(item_name,manufacturer,stock_qty,amt,gst):
    global cursor
    
    insert_cmd = f'''INSERT INTO meds (item_name,manufacturer,stock_qty,amount,gst) 
                VALUES('{item_name}','{manufacturer}',{stock_qty},{amt} ,{gst} );'''
    #print(insert_cmd)
    cursor.execute(insert_cmd)
    conn.commit()

insert_items_item('Med 1','PS',10,200,18)
insert_items_item('Med 2','AM',12,140,18)
insert_items_item('Sinerest','PL',15,210,18)
insert_items_item('ZEDEX','AM',20,100,7)
insert_items_item('Meftal Spasm','LM',10,300,7)

def insert_items_lg(username, password,_type):
    global cursor
    
    insert_cmd = f'''INSERT INTO login_table  
                VALUES('{username}','{password}','{_type}' );'''
    #print(insert_cmd)
    cursor.execute(insert_cmd)
    conn.commit()

insert_items_lg("admin1",'123','Admin')
insert_items_lg("sales1",'234','Sales')
