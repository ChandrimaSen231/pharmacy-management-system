import sqlite3 as sql
import datetime
import random as rn

conn = sql.connect("test1.db")
cursor = conn.cursor()

# Constants:
name = "name"
fields = "fields"

VARCHAR = "VARCHAR(50)"
INT = "INTEGER"
FLOAT = "FLOAT"
DATE = "DATE"

PRIMARY_KEY = "PRIMARY KEY"
FOREIGN_KEY = lambda key_field, foreign_table, foreign_key: "FOREIGN KEY ({0}) REFERENCES {1}({2})".format(
    key_field, foreign_table, foreign_key
)

create_invt_order_table = '''CREATE TABLE IF NOT EXISTS inventory_order (
                        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        order_name VARCHAR(50),
                        order_date DATE,
                        item_id INTEGER,
                        quantity INTEGER,
                        order_amount INTEGER,
                        status VARCHAR(50),
                        FOREIGN KEY (item_id) REFERENCES meds(item_id) ON DELETE CASCADE
                        );
                    '''
# add column order amount
create_meds_table = '''CREATE TABLE IF NOT EXISTS meds (
                    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_name VARCHAR(50),
                    manufacturer VARCHAR(50),
                    stock_qty INTEGER,
                    amount INTEGER,
                    gst INTEGER
                    );
                '''
# add column amount and total amount

create_login = '''CREATE TABLE IF NOT EXISTS login_table (
                        username VARCHAR(50) PRIMARY KEY,
                        password VARCHAR(50),
                        type VARCHAR(50)
                    );'''

create_cust_table = '''CREATE TABLE IF NOT EXISTS customers (
                        cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(50),
                        age INTEGER,
                        sex VARCHAR(50),
                        address VARCHAR(50),
                        phone_no INTEGER
                    );
                    
                    '''

def create_login_table():
    """
    It creates a table called login with the columns id, username, and password
    """
    create_table(create_login)

def delete_login_table():
    """
    This function deletes the login_table if it exists
    """
    global cursor
    delete_cmd = "DROP TABLE IF EXISTS login_table;"
    cursor.execute(delete_cmd)
    conn.commit()

def verify_data(username,password,_type):
    """
    It takes in a username, password, and type, and returns True if the username, password, and type
    match a row in the login database, and False otherwise
    
    :param username: The username of the user
    :param password: The password of the user
    :param _type: This is the type of user. It can be either 'admin' or 'sales'
    :return: A boolean value
    """

    global cursor
    fetch_cmd = f"SELECT * FROM login_table WHERE username = '{username}' AND password = '{password}' AND type ='{_type}';"
    cursor.execute(fetch_cmd)
    if cursor.fetchone():
        return True
    else:
        return False


def create_table(create_cmd):
    """
    It takes a string as input, and executes it as a SQL command to create table
    
    :param create_cmd: The SQL command to create the table
    """
    global cursor 
    print(create_cmd)
    cursor.execute(create_cmd)

def create_table_orders():
    """
    It creates a table called inventory orders in the database 
    """
    create_table(create_invt_order_table)

def create_table_meds():
    """
    This function creates a table called meds in the database 
    """
    create_table(create_meds_table)

def create_table_customers():
    """
    This function creates a table called customers in the database 
    """
    create_table(create_cust_table)

def get_table(table):
    """
    It takes a table name as an argument, and returns the contents of that table as a list of tuples
    
    :param table: The name of the table you want to get the data from
    :return: A list of tuples.
    """
    global cursor
    fetch_cmd = f"SELECT * FROM {table};"
    cursor.execute(fetch_cmd)
    rows = cursor.fetchall()
    return rows

def place_order(item_id, item_name,qty):
    """
    This function takes in the item_id, item_name and quantity of the item to be ordered and inserts the
    order into the inventory_order table
    
    :param item_id: The id of the item to be ordered
    :param item_name: The name of the item
    :param qty: quantity of the item
    """
    global cursor
    select_cmd = f"SELECT amount FROM meds WHERE item_id={item_id};"
    cursor.execute(select_cmd)
    val = cursor.fetchone()[0]
    amt = val * qty
    insert_cmd = f'''INSERT INTO inventory_order (order_name,order_date,item_id,quantity,order_amount,status) 
                    VALUES('{item_name}', '{datetime.date.today()}', 
                    {item_id},{qty},{amt} ,'Pending' );'''
    #print(insert_cmd)
    cursor.execute(insert_cmd)
    conn.commit()

def change_order_status(order_id,item_id):
    """
    It updates the status of the order to 'Received' and updates the stock_qty of the item in the meds
    table
    
    :param order_id: The order_id of the order that has been received
    :param item_id: The item_id of the medicine
    """
    global cursor
    update_cmd = f"UPDATE inventory_order SET status='Received' WHERE order_id={order_id};"
    select_cmd = f"SELECT stock_qty,amount FROM meds WHERE item_id={item_id};"
    # write select cmd for fetching qty of order placed from invt orders
    # and add it with stock_qty and update it in meds table
    select2_cmd = f"SELECT quantity FROM inventory_order WHERE order_id={order_id};"
    #print(select_cmd)
    cursor.execute(select_cmd)
    tup = cursor.fetchone()
    val1 = tup[0]
    print(val1)
    amt = tup[1]
    print(amt)
    cursor.execute(select2_cmd)
    val2 = cursor.fetchone()[0]
    updated_qty = val1 + val2
    
    update2_cmd = f"UPDATE meds SET stock_qty={updated_qty}  WHERE item_id={item_id};"
    #print(update_cmd)
    cursor.execute(update_cmd)
    cursor.execute(update2_cmd)
    conn.commit()

def addItemtoDB(item_id,item_name,manufacturer,qty,amt,gst):
    """
    It takes in the item_id, item_name, manufacturer, qty, amt, gst as parameters and inserts them into
    the database
    
    :param item_id: The ID of the item
    :param item_name: Name of the item
    :param manufacturer: String
    :param qty: Quantity of the item
    :param amt: Amount
    :param gst: GST on the item
    """
    global cursor
    insert_cmd = f"INSERT INTO meds VALUES({item_id},'{item_name}','{manufacturer}',{qty},{amt} ,{gst} );"
    cursor.execute(insert_cmd)
    conn.commit()

def deleteItemfromDB(item_id):
    """
    This function deletes a row from the meds table in the database
    
    :param item_id: the id of the item to be deleted
    """
    global cursor
    cursor.execute("PRAGMA foreign_keys=ON")
    delete_cmd = f"DELETE FROM meds WHERE item_id={item_id};"
    cursor.execute(delete_cmd)
    conn.commit()

def search_item(item_name):
    """
    It takes the item_name as an argument and searches the meds table for the item and returns the matching rows
    
    :param item_name: The name of the item you want to search for
    :return: A list of tuples.
    """
    global cursor
    search_cmd = f"SELECT * FROM meds WHERE item_name LIKE '{item_name}%'"
    cursor.execute(search_cmd)
    rows = cursor.fetchall()
    return rows


def insert_from_dict(table, data_dict):
    """
    It takes a table name and a dictionary of data, and inserts the data into the table
    
    :param table: a dictionary with the following keys:
    :param data_dict: {'id': '1', 'name': 'John', 'age': '20'}
    """
    global cursor
    attributes = str(tuple(data_dict.keys()))
    values = str(tuple(data_dict.values()))
    ins_cmd = "INSERT INTO {0}{1} VALUES {2}".format(table[name], attributes, values)
    print(ins_cmd)
    cursor.execute(ins_cmd)

def execute_sql(sql):
    """
    It takes a SQL statement as a parameter, executes it using the global cursor, and returns the
    results
    
    :param sql: The SQL statement to execute
    :return: A list of tuples.
    """
    global cursor
    cursor.execute(sql)
    return cursor.fetchall()


def close():
    """
    It commits the changes to the database and closes the connection
    """
    conn.commit()
    conn.close()


def register_new_customer(data):
    """
    It takes a dictionary of data and inserts it into the customers table
    
    :param data: a dictionary of the data to be inserted
    """
    insert_from_dict("customers", data)


def search_med_by_name(medicine_name):
    """
    It takes a string as an argument matches the string with medicines names in the database 
    and returns a list of matching strings
    
    :param medicine_name: The name of the medicine you want to search for
    :return: A list of medicine names that start with the inputted medicine name.
    """
    global cursor
    cursor.execute(f"SELECT item_name FROM meds WHERE item_name LIKE '{medicine_name}%'")
    rows = cursor.fetchall()
    med_list = []
    if rows:
        for row in rows:
            med_list.append(row[0])
    return med_list

def check_med_availability(med_name,qty):
    """
    It checks if the quantity of a medicine is available in the stock
    
    :param med_name: The name of the medicine
    :param qty: The quantity of the medicine that the user wants to buy
    :return: a boolean value.
    """
    global cursor
    select_cmd = f"SELECT stock_qty FROM meds WHERE item_name='{med_name}';"
    cursor.execute(select_cmd)
    row = cursor.fetchone()
    if row[0] >= qty:
        return True
    else:
        return False


def search_cust_by_phone_no(phone_no):
    """
    It searches the customers table for a customer with the given phone number and returns the row if
    found
    
    :param phone_no: The phone number of the customer you want to search for
    :return: A tuple of the customer's information.
    """
    global cursor
    select_cmd = f"SELECT * FROM customers WHERE phone_no={phone_no}"
    cursor.execute(select_cmd)
    row = cursor.fetchone()
    return row


def get_amount(med_list):
    """
    It takes a list of tuples, sorts the list by the first element of each tuple, then creates a string
    of the first elements of each tuple, separated by commas, and uses that string to query the database
    for the amount of each item
    
    :param med_list: a list of tuples, each tuple is (med_name, med_amount)
    :return: A list of the amount of each medicine in the med_list.
    """
    global cursor
    med_list.sort(key=lambda x: x[0])
    
    med_name = ""
    for med in med_list:
        med_name = med_name + "'"+med[0] + "',"
    med_name = med_name[:-1]
    select_cmd = f"SELECT amount FROM meds WHERE item_name in ({med_name});"
    cursor.execute(select_cmd)
    amt = [c[0] for c in cursor.fetchall()]
    return amt

def get_gst(med_list):
    """
    It takes a list of tuples as input, sorts the list by the first element of the tuple, and then
    returns a list of the second element of the tuple
    
    :param med_list: A list of tuples containing the name of the medicine and the quantity of the
    medicine
    :return: A list of GST values for the medicines in the list.
    """
    global cursor
    med_list.sort(key=lambda x: x[0])
    med_name = ""
    for med in med_list:
        med_name = med_name + "'"+med[0] + "',"
    med_name = med_name[:-1]
    select_cmd = f"SELECT gst FROM meds WHERE item_name in ({med_name});"
    cursor.execute(select_cmd)
    gst = [c[0] for c in cursor.fetchall()]
    return gst


def purchase_med(med_list):
    """
    It takes a list of tuples as input, sorts the list by the first element of the tuple, then updates
    the database with the new quantity of the medicine.
    
    :param med_list: A list of lists. Each sublist contains the name of the medicine and the quantity of
    the medicine to be purchased
    """
    global cursor
    med_list.sort(key=lambda x: x[0])
    med_name = ""
    for med in med_list:
        med_name = med_name + "'"+med[0] + "',"
    med_name = med_name[:-1]
    select_cmd = f"SELECT stock_qty FROM meds WHERE item_name in ({med_name});"
    cursor.execute(select_cmd)
    total_qty = [c[0] for c in cursor.fetchall()]
    rem_qty = []
    for t_qty,med in zip(total_qty,med_list):
        rem_qty.append(t_qty-med[1])
    for qty,med in zip(rem_qty,med_list):
        update_cmd = f"UPDATE meds SET stock_qty = {qty} WHERE item_name = '{med[0]}';"
        cursor.execute(update_cmd)
    conn.commit()

def save_reciept(name,age,sex,date,phone,med_list):
    """
    It takes in the name, age, sex, date, phone number and a list of medicines and generates a receipt
    in the form of a text file
    
    :param name: Name of the customer
    :param age: age of the customer
    :param sex: M/F
    :param date: date of purchase
    :param phone: The phone number of the customer
    :param med_list: A list of lists. Each list contains the name of the medicine and the quantity
    """
    receipt = """
    ABC PHARMACY

    NAME:{0} AGE:{1} SEX:{2}                   DATE:{3}
    PHONE NO. :{4} 


    MEDICINE\tQTY\tMRP\tGST\tAMOUNT\n""".format(name,age,sex,date,phone)
    amt = get_amount(med_list)
    gst = get_gst(med_list)
    f = open(f"{name}_{date}.txt",'w')
    f.write(receipt)
    total_amt = 0
    for a,med,g in zip(amt,med_list,gst):
        f.write(f"\t{med[0]}\t{med[1]}\t{a*med[1]}\t{g}%\t{round(a*(1+0.01*g),2)}\n")
        total_amt += a*(1+0.01*g)*med[1]
    f.write(f"\tNET AMOUNT: {round(total_amt,2)}")
    f.close()



cursor.execute("PRAGMA foreign_keys=on")

if __name__ == '__main__':
    pass