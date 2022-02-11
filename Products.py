import csv
import os
import time

class Products:

    def __init__(self, name : str, price : float):

        self.name = name
        self.price = price
      
        

    def add_product_to_file(self):
        header = ['name','price']
        try:
            if (os.stat("products.csv").st_size == 0):

                with open('products.csv', 'w', newline= '') as file_data:
                    
                    writer = csv.DictWriter(file_data,fieldnames= header )
                    writer.writeheader()
                    writer.writerow( {  'name' : self.name,
                    'price' : self.price   })


            else:
                with open('products.csv', 'a+', newline= '') as file_stream:
                    writer = csv.DictWriter(file_stream,fieldnames= header )
                    
                    writer.writerow( {  'name' : self.name,
                    'price' : self.price   })

            os.system('cls')
            print('A new order has been added...')
            time.sleep(3) 

        except FileNotFoundError as err:
            print(f'The following exception has araised: {err}')




def print_products_list_with_indeces():

    products_list = []
    try:

        with open('products.csv', 'r', newline= '') as file_stream:
     
            csv_file_content = csv.DictReader(file_stream)
            header = csv_file_content.fieldnames

            if  (os.stat("products.csv").st_size == 0):
                print ('No products.....')
                time.sleep(3)

            else:
                print('***  The Products list:   ***\n'.center(60))    
                index = 0
     
                for row in csv_file_content:
                    print(f'Product index : {index}', row )
                    index += 1
                    products_list.append(row)
       
        #print(products_list)
        return products_list

    except FileNotFoundError as bad_erro:
        print(f' The following exception occured :{bad_erro}')



def write_products_to_csvfile(products_list):

    with open('products.csv', 'w', newline= '') as file_data:
        header = ['name','price']
        writer = csv.DictWriter(file_data, fieldnames= header)
        writer.writeheader()

        for product in products_list:
            writer.writerow(product)



def update_product():

    products_list = print_products_list_with_indeces()
    updated_product_index= int(input('\nEnter the index of the product that you want to update : '))
    product_object = products_list[updated_product_index]

    new_name_for_product = input('Enter the new name of the product: ')
    new_product_price = float(input('\nEnter the new price for the product: '))

    if not(new_name_for_product):
       pass

    else:

        product_object['name'] = new_name_for_product
            
    if not(new_product_price):
        pass
                
    else:

        product_object['price'] = new_product_price

    products_list[updated_product_index] = product_object
    write_products_to_csvfile(products_list)

    os.system('cls')
    print('                                            Successfully  Updated\n\n')
    time.sleep(3)




def delete_product ():

    products_list = print_products_list_with_indeces()
    product_index_to_delete= int(input('Enter the index of the product that you want to delete : '))

    product_object = products_list[product_index_to_delete]
    products_list.pop(product_index_to_delete)
    write_products_to_csvfile(products_list)

    os.system('cls')
    print(f'{product_object} has been deleted')
    time.sleep(3)



def stay_at_products_menu_or_go_main():
    
    running = 1
    user_choose_where_to_go_input = input('''         
            Enter [y/Y] Return to Products Menu Options.
                  [n/N] Return to Main Menu Options.  ''')

    if user_choose_where_to_go_input in ['y', 'Y']:
        os.system('cls')
        return running
                    
    elif user_choose_where_to_go_input in ['n', 'N']:
        os.system('cls')
        running = 0
        return running



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
            
            Please enter your choice:     '''
 
    while True:

        user_inptu2= input(products_menu_options)

        if user_inptu2 == '0':
            
            os.system('cls')
            break   
                    
        elif user_inptu2 == '1':

            os.system('cls')
            print_products_list_with_indeces()

            running = stay_at_products_menu_or_go_main()
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
            product_object.add_product_to_file()

            running = stay_at_products_menu_or_go_main()
            if not(running):
                os.system('cls')
                break
            else:
                continue 
     
        elif user_inptu2 == '3':

            os.system('cls')
            update_product()
        
            running = stay_at_products_menu_or_go_main()
            if not(running):
                os.system('cls')
                break
            else:
                continue         

        elif user_inptu2 == '4':

            os.system('cls')
            delete_product()
    
            running = stay_at_products_menu_or_go_main()
            if not(running):
                os.system('cls')
                break
            else:
                continue 

        else:
            print(' Invalid Input, Try Again. ')




def save_file():

    try:

        file_content = open('products.csv' , 'a') 
        file_content.close() 

    except FileNotFoundError as bad_file:
        print(f'Can\'t read couriers.csv. {bad_file} has occured.')