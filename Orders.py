import csv
import os
import time
import methods
from prettytable import PrettyTable
class Orders:

    def __init__(self, customer_name : str, customer_address : str, 
    customer_phone : str, courier_id : int, status_id : int, items):

        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_phone = customer_phone
        self.courier_id = courier_id
        self.status_id = status_id
        self.items = items
        
        
    def add_order_to_db(self):

        connection = methods.connect_to_db()
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO Orders (customer_name,customer_address,
                customer_phone, courier_id, status_id) values (%s,%s,%s,%s,%s)''', (self.customer_name,
                self.customer_address, self.customer_phone, self.courier_id, self.status_id))

        connection.commit( )
        cursor.close()
        connection.close()

        id_query = '''SELECT MAX(order_id) FROM Orders'''
        connection_obj2 = methods.connect_to_db()
        rows = methods.select_query(connection_obj2, id_query )
        methods.close_db(connection_obj2)

        id = 1
        for row in rows:
            id =int(row[0])


        for index in range(len(self.items)):
            connection_obj_1 = methods.connect_to_db()
            cursor = connection_obj_1.cursor()
            cursor.execute(''' insert into Products_On_Orders (order_id, product_id) values(%s,%s)''',(id, int(self.items[index])))
            connection_obj_1.commit( )
            cursor.close()
            connection_obj_1.close()

            connection_obj2 = methods.connect_to_db()
            stock_quantity_query = f'''Select Stock_Quantity, Unit_Price from Product_Inventory where product_id = { int(self.items[index])}'''
            data= methods.select_query(connection_obj2 , stock_quantity_query)
            methods.close_db(connection_obj2)
            stock_quantity = 0
            new_price = 0

            for row in data:
                stock_quantity = float(row[0])
                new_price = float(row[1])

            update_connection = methods.connect_to_db()
            update_query_3 = f'''update Product_Inventory set Stock_Quantity = {float(stock_quantity-1)},
            Inventory_Value = {float(stock_quantity-1) * float(new_price)} where product_id = {int(self.items[index])}'''
            methods.commit_query(update_connection , update_query_3)
            methods.close_db(update_connection)

    


        os.system('cls')
        print('A new order has been added...')
        time.sleep(3) 


def Update_order_status( ):  
         
    os.system('cls')
    connection_object = methods.connect_to_db()
    select_orders_query = 'SELECT * FROM Orders'
    orders_db_rows = methods.select_query(connection_object , select_orders_query)
    methods.close_db(connection_object)

    orders_list = methods.db_to_list(orders_db_rows, 'Orders')
    os.system('cls')
    print('Orders List')
    methods.print_list(orders_list)

    updated_order_id= int(input('\nEnter the id of the order that you want to update its status : '))
    

    connection_1 = methods.connect_to_db()
    status_query_1 = f'''Select * from Order_Status '''
    order_status_rows= methods.select_query(connection_1 , status_query_1)
    order_status_list = methods.db_to_list(order_status_rows,'Order_Status')
    methods.close_db(connection_1)  
    os.system('cls')
    print('Order status: ')
    methods.print_list(order_status_list)

    new_status_id = input('\nEnter the id of the new status :  ') 
     

    connection_3 = methods.connect_to_db()
    update_status_query_2 = f'''update Orders set status_id = "{int(new_status_id)}" where order_id = {updated_order_id}'''
    methods.commit_query(connection_3 , update_status_query_2)
    methods.close_db(connection_3)

    os.system('cls')
    print('The order\'s status has been updated..')
    time.sleep(2)
 


        
def update_order():

    os.system('cls')
    connection_object = methods.connect_to_db()
    select_orders_query = 'SELECT * FROM Orders'
    orders_db_rows = methods.select_query(connection_object , select_orders_query)
    methods.close_db(connection_object)

    orders_list = methods.db_to_list(orders_db_rows, 'Orders')
    os.system('cls')
    print('Orders List')
    methods.print_list(orders_list)


    updated_order_id= int(input('\nEnter the id of the order that you want to update : '))
    customer_name = input('\n Enter the new name for the customer: ')
    customer_address = input('Enter the new customer address: ')
    customer_phone= input('Enter the new customer phone: ')
    os.system('cls')

    connection_new_obj = methods.connect_to_db()
    db_content = methods.select_query(connection_new_obj,"SELECT * FROM Order_Status")
    methods.close_db(connection_new_obj)
    order_status_list = methods.db_to_list(db_content, 'Order_Status')
    os.system('cls')
    print('Order status: ')
    methods.print_list(order_status_list)
    user_input_new_status = input('\nEnter the id of the new status :  ')
   
    connection_obj = methods.connect_to_db()
    db_rows = methods.select_query(connection_obj,"SELECT * FROM Products")
    methods.close_db(connection_obj)
    product_list = methods.db_to_list(db_rows, 'Products')
    os.system('cls')
    print('Products List: ')
    methods.print_list(product_list)
    items_input = input('\nEnter the id\'s of the products seperated by comma : ')

    connection_3 = methods.connect_to_db()
    query = ''' Select * from Couriers       '''
    db_row = methods.select_query(connection_3, query)
    couriers_list = methods.db_to_list(db_row, 'Couriers')
    os.system('cls')
    print('Couriers List:')
    methods.print_list(couriers_list)
    courier_id = input('\nEnter the id of the courier: ')
   

    if not(user_input_new_status ):
        pass
    else:

        connection_2 = methods.connect_to_db()
        update_status_query = f'''update Orders set status_id = "{int(user_input_new_status)}" where order_id = {updated_order_id}'''
        methods.commit_query(connection_2 , update_status_query)
        methods.close_db(connection_2)

    if not(items_input):
        pass
    else:
        list_of_product_for_order = items_input.split(',')

        connection_to_db = methods.connect_to_db()

        delete_order_query = f'''DELETE FROM Products_On_Orders WHERE order_id = {updated_order_id} '''
        methods.commit_query(connection_to_db ,delete_order_query)
        methods.close_db(connection_to_db)

        for index in range(len(list_of_product_for_order)):

            connection_2 = methods.connect_to_db()
            update_items_of_order_query = f'''Insert into Products_On_Orders (order_id, product_id) 
            values ({updated_order_id} , {int(list_of_product_for_order[index])})'''
            methods.commit_query(connection_2 , update_items_of_order_query)
            methods.close_db(connection_2)


    if not(courier_id):
        pass
    else:
    
        connection_4 = methods.connect_to_db()
        update_courier_id_query = f'''update Orders set courier_id = {int(courier_id)} where order_id = {updated_order_id}'''
        methods.commit_query(connection_4 , update_courier_id_query)
        methods.close_db(connection_4)



    if not(customer_name):
        pass
    else:
    
        connection_5 = methods.connect_to_db()
        update_customer_name_query = f'''update Orders set customer_name = "{customer_name}" where order_id = {updated_order_id}'''
        methods.commit_query(connection_5 , update_customer_name_query)
        methods.close_db(connection_5)


    
    if not(customer_address):
        pass
    else:
    
        connection_6 = methods.connect_to_db()
        update_customer_address_query = f'''update Orders set customer_address = "{customer_address}" where order_id = {updated_order_id}'''
        methods.commit_query(connection_6 , update_customer_address_query)
        methods.close_db(connection_6)



    if not(customer_phone):
        pass
    else:
    
        connection_7 = methods.connect_to_db()
        update_customer_phone_query = f'''update Orders set customer_phone = "{customer_phone}" where order_id = {updated_order_id}'''
        methods.commit_query(connection_7 , update_customer_phone_query)
        methods.close_db(connection_7)

    os.system('cls')
    print('                                  Order has successfully updated\n\n')
    time.sleep(3)


def list_orders_grouping_by_status ():

    connection_object = methods.connect_to_db()
    query = '''SELECT Order_Status.status, count(Orders.order_id) from Orders
                 right JOIN  Order_Status on Order_Status.id = Orders.status_id 
                Group by Order_Status.status
       '''
    db_rows = methods.select_query(connection_object, query)

    mytable = PrettyTable(['status', 'count(orders)'])
    print('Grouping Orders By Status:\n')
    for row in db_rows:
        mytable.add_row(row)
    print(mytable)



def print_orders():

    os.system('cls')
    connection = methods.connect_to_db()
    orders_query = '''SELECT Orders.order_id,Products_On_Orders.product_id,Products.name,
     Orders.customer_name, Orders.customer_address, 
     Orders.customer_phone, Orders.courier_id, Order_Status.status
    from Orders
    left join Order_Status on Order_Status.id = Orders.status_id
    left JOIN Products_On_Orders on Products_On_Orders.order_id = Orders.order_id
    left join Products on Products.id = Products_On_Orders.product_id 
           '''
    db_rows = methods.select_query(connection, orders_query)
    mytable = PrettyTable(['order_id', 'product_id' , 'product_name ', 'customer_name',
    'customer_address','customer_phone', 'courier_id','status'])
    print('Orders List:\n')
    for row in db_rows:
        mytable.add_row(row)
    print(mytable)
    time.sleep(2)
  




def delete_order():

    print_orders()

    order_id= input('Enter the order id to delete it: ')

    connection_object = methods.connect_to_db()
    product_id_query = f'''Select product_id FROM Products_On_Orders where order_id = {int(order_id)}'''
    rows = methods.select_query(connection_object, product_id_query )
    methods.close_db(connection_object)
    
    connection_obj = methods.connect_to_db()
    delet_query = f"DELETE FROM Orders where order_id = {int(order_id)}"
    methods.commit_query(connection_obj,delet_query )
    methods.close_db(connection_obj)


    for row in rows :
        product_id = int(row[0])

        connection_obj = methods.connect_to_db()
        inventory_query = f''' Select Stock_Quantity, Unit_Price from Product_Inventory
        where Product_Inventory.product_id = {product_id}'''
        db_rows = methods.select_query(connection_obj, inventory_query)

        for row in db_rows :
            stock_quantity = float(row[0])
            price = float(row[1])

            connection_to_db = methods.connect_to_db()
            update_query = f'''update Product_Inventory set Stock_Quantity = {stock_quantity +1},
                 Inventory_Value = {(stock_quantity +1) * (price)} where product_id = {product_id}'''

            methods.commit_query(connection_to_db , update_query)
            methods.close_db(connection_to_db)


########################################################

def display_orders_menu():
    os.system('cls')
    
    orders_menu_options = '''
        [0] Main Menu
        [1] Display Orders
        [2] Add new Order
        [3] Update Order Status
        [4] Update Existing Order
        [5] Delete order
        [6] List Orders by Status
        [7] Export DB to CSV  '''

    while True :   
        print('Orders Menu Options'.center(100))                 
        print(orders_menu_options)
    
        order_user_input1 = input('Please, choose one from the above choices:') 

        if order_user_input1 == '0':
            os.system('cls')
            break

        elif order_user_input1 == '1':
            os.system('cls')
            print('Orders list:\n')           
            print_orders()

            running = methods.stay_at_menu_or_go_main('Orders')
            if not(running):
                os.system('cls')
                break
            else:
                continue       

        elif order_user_input1 == '2':
            os.system('cls')
            user_input_customer_name =input('Enter the customer name: ')
            user_input_customer_address = input('Enter the customer address: ')
            user_input_customer_phone = input('Enter the customer phone: ')
            os.system('cls')
            print('\nChoose a courier index from the following couriers list:\n')
            connection = methods.connect_to_db()
            query = ''' Select * from Couriers       '''
            db_row = methods.select_query(connection, query)
            couriers_list = methods.db_to_list(db_row, 'Couriers')
            os.system('cls')
            print('Couriers List: ')
            methods.print_list(couriers_list)
            user_input_courier_index =input('\nThe courier\'s index is: ')

            query = ''' Select * from Products       '''
            db_row = methods.select_query(connection, query)
            products_list = methods.db_to_list(db_row, 'Products')
            os.system('cls')
            print('Products List: ')
            methods.print_list(products_list)
            customers_items = input('\nEnter the customer\'s items seperated by comma: ')

            items_list = customers_items.split(',')
            new_order = Orders(str(user_input_customer_name), str(user_input_customer_address), str(user_input_customer_phone),
             int(user_input_courier_index), 1 , items_list)
            new_order.add_order_to_db()

            running = methods.stay_at_menu_or_go_main('Orders')
            if not(running):
                os.system('cls')
                break
            else:
                continue
        elif order_user_input1 == '3':

            os.system('cls')
            Update_order_status()
            time.sleep(3)
  
            running = methods.stay_at_menu_or_go_main('Orders')
            if not(running):
                os.system('cls')
                break
            else:
                continue

        elif order_user_input1 == '4':

            os.system('cls')
            update_order()

            running = methods.stay_at_menu_or_go_main('Orders')
            if not(running):
                os.system('cls')
                break
            else:
                continue

        elif order_user_input1 == '5':

            os.system('cls')
            delete_order()
            print('Order has been deleted')
            time.sleep(2)  
           
            running = methods.stay_at_menu_or_go_main('Orders')
            if not(running):
                os.system('cls')
                break
            else:
                continue
        
        elif order_user_input1 == '6':
            os.system('cls')
            list_orders_grouping_by_status()
            time.sleep(3)

            running = methods.stay_at_menu_or_go_main('Orders')
            if not(running):
                os.system('cls')
                break
            else:
                continue
        
        elif order_user_input1 == '8':
            methods.convert_csv_db('Orders')

            running = methods.stay_at_menu_or_go_main('Orders')
            if not(running):
                os.system('cls')
                break
            else:
                continue

        elif order_user_input1 == '7':

            methods.write_db_to_csvfile('Orders')
            
            running = methods.stay_at_menu_or_go_main('Orders')
            if not(running):
                os.system('cls')
                break
            else:
                continue

        else:
            print('Invalid input, we\'ll redirect you to the Main Menu Options.')
            time.sleep(2)
            os.system('cls')
        