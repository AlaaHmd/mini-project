import pymysql
import os
from dotenv import load_dotenv
import time
import Orders
import Cafe_parts


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

        user_inptu2= input(products_menu_options)

        if user_inptu2 == '0':
            
            os.system('cls')
            break   
                    
        elif user_inptu2 == '1':

            connection = Cafe_parts.connect_to_db()
            cursor = connection.cursor()
            select_products_query = 'SELECT * FROM Products'
            products_db_rows = Cafe_parts.select_query(connection , select_products_query)

            products_list = Cafe_parts.db_to_list(products_db_rows, 'Products')
            os.system('cls')
            print('Products list:\n\n ')           
            Cafe_parts.print_list(products_list)

            running = Cafe_parts.stay_at_menu_or_go_main('Products')
            if not(running):
                os.system('cls')
                break
            else:
                continue       
        
        elif user_inptu2 == '2':

            os.system('cls')

            new_product_name = input('Enter The Product Name: ')
            new_product_price = float(input('Enter the product price: '))
            product_object = Cafe_parts.Products(new_product_name,new_product_price)
            product_object.add_product_to_db()

            running = Cafe_parts.stay_at_menu_or_go_main('Products')
            if not(running):
                os.system('cls')
                break
            else:
                continue 
     
        elif user_inptu2 == '3':

            os.system('cls')
            connection = Cafe_parts.connect_to_db()
            select_products_query = 'SELECT * FROM Products'
            products_db_rows = Cafe_parts.select_query(connection , select_products_query)
            Cafe_parts.close_db(connection)

            products_list = Cafe_parts.db_to_list(products_db_rows, 'Products')
            Cafe_parts.print_list(products_list)

            updated_product_id= int(input('\nEnter the id of the product that you want to update : '))

            product_name = input('\nEnter the new name of the product: ')
            new_product_price = input('Enter the new price for the product: ')
            stock_quantity = input('Enter the stock quantity for the updated product: ')

            if (stock_quantity):

                connection_object2 = Cafe_parts.connect_to_db()
                price_query_1 = f'''Select * from Product_Inventory where product_id = {updated_product_id}'''
                product_inventory_rows= Cafe_parts.select_query(connection_object2 , price_query_1)
                product_inventory_list_1 = Cafe_parts.db_to_list(product_inventory_rows,'Product_Inventory')
           
                price = 0
                for product_dict in product_inventory_list_1:
                    if (product_dict.get('product_id') == updated_product_id):
                        price =  float(product_dict.get('Unit_Price'))
                        break

                stock_quantity_query = f'''update Product_Inventory set Stock_Quantity = {float(stock_quantity)} ,
                 Inventory_Value = {float(stock_quantity) * price} where product_id = {updated_product_id}'''

                Cafe_parts.commit_query(connection_object2 , stock_quantity_query)
                Cafe_parts.close_db(connection_object2)

            else:
                pass

          
            if  not (new_product_price):
                pass

            else:
                connection_obj1 = Cafe_parts.connect_to_db()
                update_query_2 = f'''update Products set price = {float(new_product_price)} where id = {updated_product_id}'''
                Cafe_parts.commit_query(connection_obj1 , update_query_2)
                Cafe_parts.close_db(connection_obj1)

                connection_obj2 = Cafe_parts.connect_to_db()
                stock_quantity_query_1 = f'''Select * from Product_Inventory where product_id = {updated_product_id}'''
                data= Cafe_parts.select_query(connection_obj2 , stock_quantity_query_1)
                inventory_list = Cafe_parts.db_to_list(data, 'Product_Inventory')
                stock_quantity = 0

                for dict in inventory_list:
                    if (dict.get('product_id') == updated_product_id):
                        stock_quantity= dict['Stock_Quantity'] 
                        break
              
                update_query_3 = f'''update Product_Inventory set Unit_Price = {float(new_product_price)},
                 Inventory_Value = {float(stock_quantity) * float(new_product_price)} where product_id = {updated_product_id}'''

                Cafe_parts.commit_query(connection_obj2 , update_query_3)
                Cafe_parts.close_db(connection_obj2)

                
            if not (product_name):
                pass

            else:
                connection_obj5 = Cafe_parts.connect_to_db()
                update_query_1 = f'''update Products set name = "{product_name}" where id = {updated_product_id}'''
                Cafe_parts.commit_query(connection_obj5 , update_query_1)
                Cafe_parts.close_db(connection_obj5)

          
            os.system('cls')
            print('Product has been updated')
            time.sleep(2)
            running = Cafe_parts.stay_at_menu_or_go_main('Products')
            if not(running):
                os.system('cls')
                break
            else:
                continue         

        elif user_inptu2 == '4':

            os.system('cls')
            connection = Cafe_parts.connect_to_db()
            select_products_query = 'SELECT * FROM Products'
            products_db_rows = Cafe_parts.select_query(connection , select_products_query)
            products_list = Cafe_parts.db_to_list(products_db_rows, 'Products')
            Cafe_parts.close_db(connection)

            print('Product List:\n\n')
            Cafe_parts.print_list(products_list)
            user_product_index = int(input('Enter the index of the product to delete it: '))

            connection_object = Cafe_parts.connect_to_db()
            delet_product_inventory_query = f"DELETE FROM Product_Inventory where product_id = {user_product_index}"
            Cafe_parts.commit_query(connection_object,delet_product_inventory_query )
            Cafe_parts.close_db(connection_object)

            connection_obj = Cafe_parts.connect_to_db()
            delet_product_query = f"DELETE FROM Products where id = {user_product_index}"
            Cafe_parts.commit_query(connection_obj,delet_product_query )
            Cafe_parts.close_db(connection_obj)

            os.system('cls')
            print('Product has been deleted')
            time.sleep(2)
    
            running = Cafe_parts.stay_at_menu_or_go_main('Products')
            if not(running):
                os.system('cls')
                break
            else:
                continue 

        elif user_inptu2 == '5': 
            os.system('cls')
            Cafe_parts.write_db_to_csvfile('Products')
            os.system('cls')
            print('Products table has been exported to Products.csv')
            time.sleep(2)
    
            running = Cafe_parts.stay_at_menu_or_go_main('Products')
            if not(running):
                os.system('cls')
                break
            else:
                continue 

        elif user_inptu2 == '6': 
            os.system('cls')
            inventory_list =  Cafe_parts.show_product_inventory()
            print('Products Inventory: ')
            Cafe_parts.print_list(inventory_list)
            time.sleep(2)
    
            running = Cafe_parts.stay_at_menu_or_go_main('Products')
            if not(running):
                os.system('cls')
                break
            else:
                continue 

        else:

            print(' Invalid Input, Try Again. ')




def display_courier_menu():

 while True: 

    os.system('cls')

    courier_menu_input= input('''                                     Couriers Menu Options 
            
        [ 0 ]  Main Menu
        [ 1 ]  Couriers List
        [ 2 ]  Create New Courier
        [ 3 ]  Update Exsiting Courier
        [ 4 ]  Delete Courier  
        [ 5 ]  Export Couriers table to CSV file

        Please enter your choice:     ''')

   
    if courier_menu_input == '0':

        os.system('cls')
        break

    elif courier_menu_input == '1':

        connection = Cafe_parts.connect_to_db()
        select_products_query = 'SELECT * FROM Couriers'
        couriers_db_rows = Cafe_parts.select_query(connection , select_products_query)
        couriers_list = Cafe_parts.db_to_list(couriers_db_rows, 'Couriers')
        os.system('cls')
        print('Couriers list:\n\n ')           
        Cafe_parts.print_list(couriers_list)
        running = Cafe_parts.stay_at_menu_or_go_main('Couriers')
        if not(running):
            os.system('cls')
            break
        else:
            continue

    elif courier_menu_input == '2':

        os.system('cls')
        new_courier_name = input('Enter the courier Name : ')
        new_courier_phone = input('Enter the courier phone:')
        courier_object = Cafe_parts.Couriers(new_courier_name,new_courier_phone)
        courier_object.add_new_courier_to_db()

        running = Cafe_parts.stay_at_menu_or_go_main('Couriers')
        if not(running):
            os.system('cls')
            break
        else:
            continue

    elif courier_menu_input == '3':
        os.system('cls')
        connection_courier_object = Cafe_parts.connect_to_db()
        courier_query ="SELECT * FROM Couriers"
        couriers_rows_from_db = Cafe_parts.select_query(connection_courier_object , courier_query)
        couriers_list = Cafe_parts.db_to_list(couriers_rows_from_db, 'Couriers')
        print('Couriers List: ')
        Cafe_parts.print_list(couriers_list)

        courier_id= int(input('\nEnter the id of the courier that you want to update : '))
        new_name_for_courier = input('Enter the new name of the courier: ')
        new_phone_for_courier = input('\nEnter the new phone for the courier: ')

                    
        if  not (new_name_for_courier):
            pass

        else:

            update_query_1 = f'''update Couriers set name = "{new_name_for_courier}" where id = {courier_id}'''
            Cafe_parts.commit_query(connection , update_query_1)

                
        if not (new_phone_for_courier):
            pass

        else:

            update_query_2 = f'''update Couriers set phone = "{new_phone_for_courier}" where id = {courier_id}'''
            Cafe_parts.commit_query(connection , update_query_2)


        os.system('cls')
        print('  The courrier has been successfully  Updated\n\n')
        time.sleep(3)

        running = Cafe_parts.stay_at_menu_or_go_main('Couriers')
        if not(running):
            os.system('cls')
            break
        else:
            continue

    elif courier_menu_input == '4':

        os.system('cls')
        connection = Cafe_parts.connect_to_db()
        cursor = connection.cursor()

        courier_query = 'SELECT * FROM Couriers'
        couriers_db_rows = Cafe_parts.select_query(connection , courier_query)

        couriers_list = Cafe_parts.db_to_list(couriers_db_rows, 'Couriers')
        print('Couriers List:\n\n')
        Cafe_parts.print_list(couriers_list)

        courier_id = int(input('Enter the index of the courier to delete it: '))
        delet_courier_query = f"DELETE FROM Couriers where id = {courier_id}"

        Cafe_parts.commit_query(connection,delet_courier_query )
        os.system('cls')
        print('Courier has been deleted')
        time.sleep(2)

        running = Cafe_parts.stay_at_menu_or_go_main('Couriers')
        if not(running):
            os.system('cls')
            break
        else:
            continue
    
    elif  courier_menu_input == '5': 
        os.system('cls')
        Cafe_parts.write_db_to_csvfile('Couriers')
        print('Couriers table has been exported to Couriers.csv')
        time.sleep(2)
    
        running = Cafe_parts.stay_at_menu_or_go_main('Couriers')
        if not(running):
            os.system('cls')
            break
        else:
            continue 
 
    else:
        print('''\n Invalid Input, Try Again.''')






def main():

    os.system('cls')
    welcome_text = '''
                                 __________________________________________________
                                |       ***                                ***     |
                                |         Welcome To Your Friendly Cafe App        |
                                |__________________________________________________|    

    
                   '''
    print(welcome_text)
    time.sleep(2)
    os.system('cls')
    main_text=       '''                                     ______________________________________
                                    |                                      |
                                    |          Main Menu Options           |
                                    |______________________________________|

                             [ 0 ] Exit 
                             [ 1 ] Products Menu Options 
                             [ 2 ] Couriers Menu Options 
                             [ 3 ] Orders Menu Options
                             
                             Please enter your choice:  '''

    
        
    while True:       
        user_input = input(main_text )

        if user_input == '0':

            Cafe_parts.close_db(Cafe_parts.connect_to_db())
            quit()

        elif user_input == '1':

            display_product_menu()
            
        elif user_input == '2':

            display_courier_menu( )
        elif user_input == '3':
            Orders.display_orders_menu()
    

main()