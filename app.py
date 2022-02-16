import pymysql
import os
from dotenv import load_dotenv
import time
import Orders
import Products
import Couriers


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
            
            Please enter your choice:     '''
 
    while True:

        user_inptu2= input(products_menu_options)

        if user_inptu2 == '0':
            
            os.system('cls')
            break   
                    
        elif user_inptu2 == '1':

            connection = Products.connect_to_db()
            cursor = connection.cursor()
            select_products_query = 'SELECT * FROM Products'
            products_db_rows = Products.select_query(connection , select_products_query)

            products_list = Products.db_to_list(products_db_rows, 'Products')
            os.system('cls')
            print('Products list:\n\n ')           
            Products.print_list(products_list)

            running = Products.stay_at_menu_or_go_main('Products')
            if not(running):
                os.system('cls')
                break
            else:
                continue       
        
        elif user_inptu2 == '2':

            os.system('cls')

            new_product_name = input('Enter The Product Name: ')
            new_product_price = float(input('Enter the product price: '))
            product_object = Products.Products(new_product_name,new_product_price)

            product_object.add_product_to_db()

            running = Products.stay_at_menu_or_go_main('Products')
            if not(running):
                os.system('cls')
                break
            else:
                continue 
     
        elif user_inptu2 == '3':

            os.system('cls')
            connection = Products.connect_to_db()
            cursor = connection.cursor()

            select_products_query = 'SELECT * FROM Products'
            products_db_rows = Products.select_query(connection , select_products_query)

            products_list = Products.db_to_list(products_db_rows, 'Products')
            Products.print_list(products_list)

            updated_product_id= int(input('\nEnter the id of the product that you want to update : '))

            product_name = input('\nEnter the new name of the product: ')
            new_product_price = input('Enter the new price for the product: ')

            
            if  not (new_product_price):
                pass

            else:

                update_query_2 = f'''update Products set price = {float(new_product_price)} 
                where id = {updated_product_id}'''
                Products.commit_query(connection , update_query_2)

                
            if not (product_name):
                pass

            else:

                update_query_1 = f'''update Products set name = "{product_name}" where id = {updated_product_id}'''
                Products.commit_query(connection , update_query_1)

            os.system('cls')
            print('Product has been updated')
            time.sleep(2)
            running = Products.stay_at_products_menu_or_go_main()
            if not(running):
                os.system('cls')
                break
            else:
                continue         

        elif user_inptu2 == '4':

            os.system('cls')
            connection = Products.connect_to_db()
            cursor = connection.cursor()

            select_products_query = 'SELECT * FROM Products'
            products_db_rows = Products.select_query(connection , select_products_query)

            products_list = Products.db_to_list(products_db_rows, 'Products')
            print('Product List:\n\n')
            Products.print_list(products_list)

            user_product_index = int(input('Enter the index of the product to delete it: '))
            delet_product_query = f"DELETE FROM Products where Products.id = {user_product_index}"

            Products.commit_query(connection,delet_product_query )
            os.system('cls')
            print('Product has been deleted')
            time.sleep(2)
    
            running = Products.stay_at_menu_or_go_main('Products')
            if not(running):
                os.system('cls')
                break
            else:
                continue 

        elif user_inptu2 == '5': 
            os.system('cls')
            Products.write_Products_db_to_csvfile('Products')
            os.system('cls')
            print('Products table has been exported to Products.csv')
            time.sleep(2)
    
            running = Products.stay_at_menu_or_go_main('Products')
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
        [ 4 ]  Delete Courier   ''')

   


    if courier_menu_input == '0':

        os.system('cls')
        break

        
            
    elif courier_menu_input == '1':

        os.system('cls')
        Couriers.print_couriers_list_with_indeces()

        running = Products.stay_at_menu_or_go_main('Couriers')
        if not(running):
            os.system('cls')
            break
        else:
            continue

    elif courier_menu_input == '2':

        os.system('cls')
        new_courier_name = input('Enter the courier Name : ')
        new_courier_phone = input('Enter the courier phone:')
        courier_object = Products.Couriers(new_courier_name,new_courier_phone)
        courier_object.add_new_courier_to_db()

        running = Products.stay_at_menu_or_go_main('Couriers')
        if not(running):
            os.system('cls')
            break
        else:
            continue

    elif courier_menu_input == '3':

        os.system('cls')

        Couriers.update_courier()

        running = Products.stay_at_menu_or_go_main('Couriers')
        if not(running):
            os.system('cls')
            break
        else:
            continue

    elif courier_menu_input == '4':

        os.system('cls')
        Couriers.delete_courier()

        running = Products.stay_at_menu_or_go_main('Couriers')
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

            Products.close_db(Products.connect_to_db())
            Couriers.save_file()
            quit()

        elif user_input == '1':

            display_product_menu()
            
        elif user_input == '2':

            display_courier_menu( )
        elif user_input == '3':
            Orders.display_orders_menu()

main()