import pymysql
import os
from dotenv import load_dotenv
import csv
import os
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




class Products:

    def __init__(self, name : str, price : float):

        self.name = name
        self.price = price
      
        

    def add_product_to_db(self):
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Products (name, price) values (%s,%s)", (self.name,self.price))
        connection.commit()
        os.system('cls')
        print('A new products has been added...')
        time.sleep(3) 


class Couriers:

    def __init__(self, name : str, phone : str):

        self.name = name
        self.phone = phone
      
        

    def add_new_courier_to_db(self):



        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Couriers (name, phone) values (%s,%s)", (self.name,self.phone))
        connection.commit()
        cursor.close()
        connection.close()
        os.system('cls')
        print('A new courier has been added...')
        time.sleep(3) 



    
        # connection = connect_to_db()
        # new_query_to_add_courier= f'''INSERT INTO Couriers (name, phone) values ("{self.name}","{self.phone}")'''
        
        # commit_query(connection, new_query_to_add_courier)

        # #cursor.execute("INSERT INTO Products (name, price) values (%s,%s)", (self.name,self.price))
        # #connection.commit()
        # os.system('cls')
        # print('A new courier has been added...')
        # time.sleep(3) 




def select_query(connection_object, query):

    cursor = connection_object.cursor()

    try:
        cursor.execute(query)

        rows = cursor.fetchall()

    except Exception:
        print('Error in reading the database.')
 
    return rows



def write_Products_db_to_csvfile(table_name):

    connection_object = connect_to_db()
    cursor = connection_object.cursor()

    query = "SELECT * FROM "+ table_name
    cursor.execute(query)

    header = [row[0] for row in cursor.description]

    rows = cursor.fetchall()


    try:

        with open (table_name + '.csv', 'w', newline= '') as file_data:
            
            writer = csv.DictWriter(file_data, fieldnames= header )
            writer.writeheader()

            for index ,items in enumerate(rows) :
               #for num, item in enumerate(items):
                writer.writerow((','.join(str(r) for r in items) ))
                    

 #f.write(','.join(str(r) for r in row) + '\n')
    except Exception as err:
        print('err')


def commit_query(connection_object, query):

    cursor = connection_object.cursor()

    try:

        cursor.execute(query)
        connection_object.commit()

    except Exception as ex:
        print('Error')
  



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




def print_list(list_object):

    for item in list_object:

        print(item)




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
 



def close_db(connection):

    (connection.cursor()).close()
    connection.close()

