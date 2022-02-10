import os
import time
import Orders
import Products
import Couriers


def main():

    os.system('cls')
    welcome_text = '''
                                 __________________________________________________
                                |       ***                                ***     |
                                |         Welcome To Your Friendly Cafe App        |
                                |__________________________________________________|    

    
                   '''
    print(welcome_text)
    time.sleep(3)
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

            Products.save_file()
            Couriers.save_files()
            quit()

        elif user_input == '1':

            Products.display_product_menu()
            
        elif user_input == '2':

            Couriers.display_courier_menu( )
        elif user_input == '3':
            Orders.display_orders_menu()

main()