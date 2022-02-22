from types import MethodDescriptorType
from winreg import QueryValue
import methods
import os
import time


class Products:

    def __init__(self, name : str, price : float):

        self.name = name
        self.price = price
      
        

    def add_product_to_db(self):
        connection = methods.connect_to_db()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Products (name, price) values (%s,%s)", (self.name,self.price))
        connection.commit()

        cursor.execute("SELECT id from Products where name =(%s) and price = (%s)", (self.name,self.price))
        header = [columns[0] for columns in cursor.description]
        row = cursor.fetchall()
        product_dict = dict(zip(header, row))
        product_id = product_dict.get('id')
        stock_quantity = float(input('Please enter the stock quantity for this product: '))

        cursor.execute("INSERT INTO Product_Inventory (product_id, Unit_Price, Stock_Quantity, Inventory_Value) values (%s, %s, %s, %s)", (product_id ,self.price,stock_quantity, self.price*stock_quantity))
        connection.commit()

        os.system('cls')
        print('A new products has been added...')
        time.sleep(3) 





def update_product(product_id):


    product_name = input('\nEnter the new name of the product: ')
    new_product_price = input('Enter the new price for the product: ')
    stock_quantity = input('Enter the stock quantity for the updated product: ')

    if (stock_quantity):

        connection_object2 = methods.connect_to_db()
        price_query_1 = f'''Select * from Product_Inventory where product_id = {product_id}'''
        product_inventory_rows= methods.select_query(connection_object2 , price_query_1)
        product_inventory_list_1 = methods.db_to_list(product_inventory_rows,'Product_Inventory')
           
        price = 0
        for product_dict in product_inventory_list_1:
            if (product_dict.get('product_id') == product_id):
                price =  float(product_dict.get('Unit_Price'))
                break

        stock_quantity_query = f'''update Product_Inventory set Stock_Quantity = {float(stock_quantity)} ,
        Inventory_Value = {float(stock_quantity) * price} where product_id = {product_id}'''

        methods.commit_query(connection_object2 , stock_quantity_query)
        methods.close_db(connection_object2)

    else:
        pass

          
    if  not (new_product_price):
        pass

    else:
        connection_obj1 = methods.connect_to_db()
        update_query_2 = f'''update Products set price = {float(new_product_price)} where id = {product_id}'''
        methods.commit_query(connection_obj1 , update_query_2)
        methods.close_db(connection_obj1)

        connection_obj2 = methods.connect_to_db()
        stock_quantity_query_1 = f'''Select * from Product_Inventory where product_id = {product_id}'''
        data= methods.select_query(connection_obj2 , stock_quantity_query_1)
        inventory_list = methods.db_to_list(data, 'Product_Inventory')
        stock_quantity = 0

        for dict in inventory_list:
            if (dict.get('product_id') == product_id):
                stock_quantity= dict['Stock_Quantity'] 
                break
              
        update_query_3 = f'''update Product_Inventory set Unit_Price = {float(new_product_price)},
        Inventory_Value = {float(stock_quantity) * float(new_product_price)} where product_id = {product_id}'''

        methods.commit_query(connection_obj2 , update_query_3)
        methods.close_db(connection_obj2)

                
        if not (product_name):
            pass

        else:
            connection_obj5 = methods.connect_to_db()
            update_query_1 = f'''update Products set name = "{product_name}" where id = {product_id}'''
            methods.commit_query(connection_obj5 , update_query_1)
            methods.close_db(connection_obj5)

       


##############################################################




def  display_product_menu():
    os.system('cls')

    products_menu_options='''                                         _______________________________________
                                        |                                       |
                                        |         Products Menu Options         |
                                        |_______________________________________|
                                         
            
            [ 0 ]  Main Menu
            [ 1 ]  Products List
            [ 2 ]  Create New Product
            [ 3 ]  Update Exsiting Product
            [ 4 ]  Delete Product 
            [ 5 ]  Export Products table to CSV file.
            [ 6 ]  Products Inventory.
            
            Please enter your choice:     '''
 
    while True:
        os.system('cls')
        user_inptu2= input(products_menu_options)

        if user_inptu2 == '0':
            
            os.system('cls')
            break   
                    
        elif user_inptu2 == '1':

            connection = methods.connect_to_db()
            cursor = connection.cursor()
            select_products_query = 'SELECT * FROM Products'
            products_db_rows = methods.select_query(connection , select_products_query)

            products_list = methods.db_to_list(products_db_rows, 'Products')
            os.system('cls')
            print('Products list:\n')           
            methods.print_list(products_list)

            running = methods.stay_at_menu_or_go_main('Products')
            if not(running):
                os.system('cls')
                break
            else:
                continue       
        
        elif user_inptu2 == '2':

            os.system('cls')

            new_product_name = input('Enter The Product Name: ')
            new_product_price = float(input('Enter the product price: '))
            product_object = Products(new_product_name,new_product_price)
            product_object.add_product_to_db()

            running = methods.stay_at_menu_or_go_main('Products')
            if not(running):
                os.system('cls')
                break
            else:
                continue 
     
        elif user_inptu2 == '3':

            os.system('cls')
            connection = methods.connect_to_db()
            select_products_query = 'SELECT * FROM Products'
            products_db_rows = methods.select_query(connection , select_products_query)
            methods.close_db(connection)

            products_list = methods.db_to_list(products_db_rows, 'Products')
            methods.print_list(products_list)

            updated_product_id= int(input('\nEnter the id of the product that you want to update : '))

            connection_1 = methods.connect_to_db()
            products_query = f''' SELECT COUNT(*) FROM Products_On_Orders WHERE product_id = {updated_product_id}'''
            rows = methods.select_query(connection_1, products_query)
            methods.close_db(connection_1)

            for row in rows:
                if (row[0] != 0):
                    os.system('cls')
                    print('Can\'t update this product, it is on Orders Table.')
                    user_input = input('''Would you like to delete the orders which have this products.\nThen continue updating the product? (y,n)''')

                    if (user_input in ['y','Y']):

                        connection = methods.connect_to_db()
                        query = f''' Select order_id FROM Products_On_Orders where product_id = {updated_product_id}'''
                        rows = methods.select_query(connection, query)
                        methods.close_db(connection)
                        
                        for row in rows:
                            order_id = int(row[0])

                        connection_1 = methods.connect_to_db()
                        query = f''' DELETE FROM Orders where order_id = {order_id}'''
                        #rows = methods.commit_query(connection_1, query)
                        rows = methods.commit_query(connection_1, query)
                        methods.close_db(connection_1)
                        update_product(updated_product_id)
                        
                        os.system('cls')
                        print('Product has been updated')
                        time.sleep(2)
                        running = methods.stay_at_menu_or_go_main('Products')
                        if not(running):
                            os.system('cls')
                            break
                        else:
                            continue     

                        
                else:
                    update_product(updated_product_id)

                    os.system('cls')
                    print('Product has been updated')
                    time.sleep(2)
                    running = methods.stay_at_menu_or_go_main('Products')
                    if not(running):
                        os.system('cls')
                        break
                    else:
                        continue         

        elif user_inptu2 == '4':

            os.system('cls')
            connection = methods.connect_to_db()
            select_products_query = 'SELECT * FROM Products'
            products_db_rows = methods.select_query(connection , select_products_query)
            products_list = methods.db_to_list(products_db_rows, 'Products')
            methods.close_db(connection)

            print('Product List:\n\n')
            methods.print_list(products_list)
            product_index = int(input('Enter the index of the product to delete it: '))

            connection_1 = methods.connect_to_db()
            query = f''' SELECT count(*) FROM Products_On_Orders where product_id = {product_index}'''
            rows = methods.select_query(connection_1,query )
            methods.close_db(connection_1)


            for row in rows:
                if row[0] != 0:

                    os.system('cls')
                    print('''>>Product is on order, can\'t delete it.\n>>> Try delete\\cancel the orders then delete the product. ''')
                    time.sleep(2)
                    pass
                    break
                    
                else:

            
                    connection_object = methods.connect_to_db()
                    delet_product_inventory_query = f"DELETE FROM Product_Inventory where product_id = {product_index}"
                    methods.commit_query(connection_object,delet_product_inventory_query )
                    methods.close_db(connection_object)

                    connection_obj = methods.connect_to_db()
                    delet_product_query = f"DELETE FROM Products where id = {product_index}"
                    methods.commit_query(connection_obj,delet_product_query )
                    methods.close_db(connection_obj)

                    os.system('cls')
                    print('Product has been deleted')
                    time.sleep(2)
                    running = methods.stay_at_menu_or_go_main('Products')
                    if not(running):
                        os.system('cls')
                        break
                    else:
                        continue 

        elif user_inptu2 == '5': 
            os.system('cls')
            methods.write_db_to_csvfile('Products')
            os.system('cls')
            print('Products table has been exported to Products.csv')
            time.sleep(2)
    
            running = methods.stay_at_menu_or_go_main('Products')
            if not(running):
                os.system('cls')
                break
            else:
                continue 

        elif user_inptu2 == '6': 
            os.system('cls')
            inventory_list =  methods.show_product_inventory()
            print('Products Inventory: ')
            methods.print_list(inventory_list)
            time.sleep(2)
    
            running = methods.stay_at_menu_or_go_main('Products')
            if not(running):
                os.system('cls')
                break
            else:
                continue 

        else:

            print(' Invalid Input, Try Again. ')

