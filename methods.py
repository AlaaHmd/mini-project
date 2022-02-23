from prettytable import PrettyTable
import pymysql
import os
from dotenv import load_dotenv
import csv
import time




def connect_to_db():
# Load environment variables from .env file
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

# Establish a database connection

    connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

    return connection


###########################################

def select_query(connection_object, query):

    cursor = connection_object.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
 
    return rows



###################################################

def write_db_to_csvfile(table_name):

    connection_object = connect_to_db()
    cursor = connection_object.cursor()
    query = "SELECT * FROM "+ table_name
    cursor.execute(query)

    header = [columns[0] for columns in cursor.description]
    rows = cursor.fetchall()

    try:

        with open (table_name + '.csv', 'w', newline= '') as file_data:
            
            writer = csv.DictWriter(file_data, fieldnames= header )
            writer.writeheader()

            for row in rows:
                writer.writerow(dict(zip(header, row)))

        print('CSV file is now available.')

    except Exception as err:
        print('err')



##################################################

def commit_query(connection_object, query):

    cursor = connection_object.cursor()

    cursor.execute(query)
    connection_object.commit()

################################################

def stay_at_menu_or_go_main(choice_name):
    
    running = 1

    if (choice_name =='Products'):
        user_choose_where_to_go_input = input('''         
    Enter [Y/y] Return to Products Menu Options.
          [N/n] Return to Main Menu Options.  ''')

        if user_choose_where_to_go_input in ['y', 'Y']:
            os.system('cls')
            return running
                    
        elif user_choose_where_to_go_input in ['n', 'N']:
            os.system('cls')
            running = 0
            return running

    elif (choice_name =='Couriers'):

        user_choose_where_to_go_input = input('''         
    Enter [Y/y] Return to Courier Menu Options.
          [N/n] Return to Main Menu Options.  ''')

        if user_choose_where_to_go_input in ['y', 'Y']:
            os.system('cls')
            return running
                    
        elif user_choose_where_to_go_input in ['n', 'N']:
            os.system('cls')
            running = 0
            return running


    elif (choice_name =='Orders'):

        user_choose_where_to_go_input = input('''         
    Enter [Y/y] Return to Orders Menu Options.
          [N/n] Return to Main Menu Options.  ''')

        if user_choose_where_to_go_input in ['y', 'Y']:
            os.system('cls')
            return running
                    
        elif user_choose_where_to_go_input in ['n', 'N']:
            os.system('cls')
            running = 0
            return running


#####################################

def print_list(list_object):


    if (len(list_object) != 0):

        mytable = PrettyTable([key for key in list_object[0].keys()])

        for item in list_object:
            mytable.add_row([value for value in item.values()])
        print(mytable)
 


##################################################

def db_to_list (rows, table_name):

    
    if table_name == 'Products':
        products_list = []
        for row in rows:
            products_list.append({'id' :row[0], 'name': row[1], 'price': float(row[2])})
        return products_list

    elif table_name == 'Couriers':
        couriers_list = []
        for row in rows:
            couriers_list.append({'id' :row[0], 'name': row[1], 'phone': row[2]})
        return couriers_list

    elif table_name == 'Product_Inventory':
        product_inventory_list = []
        for row in rows:
            product_inventory_list.append({'id' :row[0], 'product_id': row[1], 'Stock_Quantity': float(row[2]), 'Unit_Price': float(row[3]),
             'Inventory_Value': float(row[4]) })
        return product_inventory_list

    elif table_name == 'Orders':
        orders_list = []
        for row in rows:
            orders_list.append({'order_id' :row[0], 'customer_name': row[1], 'customer_address': row[2], 'customer_phone': row[3],
             'courier_id': int(row[4]), 'status':int(row[5])})
        return orders_list

    elif table_name == 'Order_Status':
        order_status_list = []
        for row in rows:
            order_status_list.append({'id' :row[0], 'status': row[1] })
        return order_status_list




 #####################################################

def show_product_inventory():

    connection_object = connect_to_db()
    query = '''SELECT Products.id, Products.name, Stock_Quantity, Unit_Price, Inventory_Value 
    from Product_Inventory
    inner join Products
    on Products.id = Product_Inventory.product_id       '''

    db_rows = select_query(connection_object, query)

    # inventory_list = []
    # for row in db_rows:
    #         inventory_list.append({'Product id' :row[0], 'Product name': row[1],
    #          'Product Stock_Quantity': float(row[2]), 'Product unit price': float(row[3]),
    #           'Product Inventory Value': float(row[4]) })
    return db_to_list(db_rows, 'Product_Inventory')

######################################################

def convert_csv_db(file_name):

    connection = connect_to_db()
    cursor = connection.cursor()

    try:

        with open (file_name +'.csv', 'r', newline='' ) as file_content:
            data = csv.reader(file_content)
            # to retrieve the fieldsname
            header = next(data)

            if file_name == 'Orders':
                for row in data:
                    cursor.execute(
        "INSERT INTO Orders (customer_name, customer_address, customer_phone, courier_id, status, items) VALUES ( %s, %s, %s,%s,%s, %s)", row)
                    connection.commit()

            elif file_name == 'Products':
                for row in data:
                    cursor.execute(
        "INSERT INTO Products (name, price) VALUES ( %s, %s)", row)
                    connection.commit() 

            elif file_name == 'Couriers':
                for row in data:
                    cursor.execute(
        "INSERT INTO Couriers (name, phone) VALUES ( %s, %s)", row)
                    connection.commit() 

            elif file_name == 'Customers':
                for row in data:
                    cursor.execute(
        "INSERT INTO Customers (name, address, phone) VALUES ( %s, %s,%s)", row)
                    connection.commit() 

        cursor.close()
        connection.close()
        os.system('cls')
        print('CSV has been transfered to Database.')
        time.sleep(3)
    except FileNotFoundError as err:
        print('Can\'t open the file')


##########################################################

def commit_query(connection_object, query):

    cursor = connection_object.cursor()

    cursor.execute(query)
    connection_object.commit()


###########################################################

def close_db(connection):

    (connection.cursor()).close()
    connection.close()

