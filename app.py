import methods
import Products
import Couriers
import Orders
import os
import time


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
                             [ 4 ] Customers
                             
                             Please enter your choice:  '''

    
        
    while True:       
        user_input = input(main_text )

        if user_input == '0':

            methods.close_db(methods.connect_to_db())
            quit()

        elif user_input == '1':

            Products.display_product_menu()
            
        elif user_input == '2':

            Couriers.display_courier_menu( )
        elif user_input == '3':
            Orders.display_orders_menu()

        elif user_input == '4':
            methods.convert_csv_db('Customers')
    

main()