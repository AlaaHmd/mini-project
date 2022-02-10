import csv
from operator import index
from typing import List
import Couriers
import os
import time
import Products

class Orders:

    def __init__(self, customer_name : str, customer_address : str, 
    customer_phone : str, courier_index : int, status : str, items):

        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_phone = customer_phone
        self.courier_index = courier_index
        self.status = status
        self.items = items
        
        
        
    def add_order_to_file(self):

        try:

            with open('orders.csv', 'a+', newline= '') as file_data:
                header = ['customer_name','customer_address',
                'customer_phone', 'courier_index', 'status', 'items']
                writer = csv.DictWriter(file_data,fieldnames= header )
                # If the file is empty, write the header first then appen the new order.
                if (os.stat("orders.csv").st_size == 0):

                    writer.writeheader()
                    writer.writerow( {  'customer_name' : self.customer_name,
                    'customer_address' : self.customer_address,
                    'customer_phone': self.customer_phone,
                    'courier_index' : self.courier_index,
                    'status' : self.status ,
                    'items': self.items  })


                else:

                    writer.writerow( {  'customer_name' : self.customer_name,
                'customer_address' : self.customer_address,
                'customer_phone': self.customer_phone,
                'courier_index' : self.courier_index,
                'status' : self.status,
                'items': self.items    }) 
            os.system('cls')
            print('A new order has been added...')
            time.sleep(3) 

        except FileNotFoundError as err:
            print(f'The following exception has araised: {err}')




def print_orders_dictionary_with_indeces():

    order_list = []
    try:

        with open('orders.csv', 'r', newline= '') as file_stream:

            csv_file_content = csv.DictReader(file_stream)
            header = csv_file_content.fieldnames

            if  (os.stat("orders.csv").st_size == 0):
                print ('No Orders.....')

            else:
                print('***  The Orders list:   ***\n'.center(100))    
                index = 0
                #print( '                      ', header)
                for row in csv_file_content:
                    print(f'Order index: {index}',row)
                    index += 1
                    order_list.append(row)
       
        return order_list

    except FileNotFoundError as bad_erro:
        print(f' The following exception occured :{bad_erro}')


def add_order_to_csv(order):

    order_list = []
    order_list = print_orders_dictionary_with_indeces()
    order_list.append(order)
    write_orders_file(order_list)

    os.system('cls')
    print('A new order has been added...')
    time.sleep(3)




def write_orders_file(Orders_list):

    with open('orders.csv', 'w', newline= '') as file_data:
        header = ['customer_name','customer_address','customer_phone', 'courier_index', 'status', 'items']
        writer = csv.DictWriter(file_data, fieldnames= header)
        writer.writeheader()

        for order in Orders_list:
            writer.writerow(order)



    
def delete_courier_and_order (courier_index):

    order_list = []

    try:

        with open('orders.csv', 'r', newline= '') as file_stream:
            csv_file_content = csv.DictReader(file_stream)
            number_of_deleted_orders = 0
            
            for row in csv_file_content:
        
                if row.get('courier_index') == courier_index:
                    del row
                    number_of_deleted_orders += 1
                else:
                    order_list.append(row)
            print(number_of_deleted_orders,'orders has/have been Successfuly Deleted')
            time.sleep(3)
        write_orders_file(order_list)

    except FileNotFoundError as no_file:
        print(f'The following error occured :{no_file}')




def order_status_options():
    order_status_list = '''
            These are the available statuses:

            [0] Preparing
            [1] Waiting For Deliver
            [2] Out For Delivery
            [3] Delivered
                            ''' 
    print(order_status_list)



def Update_order_status(user_input_new_status, order ):  

    if user_input_new_status == '0':
        order['status'] = 'Preparing'
    if user_input_new_status == '1':
        order['status'] = 'Waiting For Deliver'
    elif user_input_new_status == '2':
        order['status'] = 'Out For Delivery'
    elif user_input_new_status == '3':
        order['status'] = 'Out For Delivery'

    return order


        
def update_order():

    list_of_orders = print_orders_dictionary_with_indeces()
    index_of_order_update = int(input ('\nWhich order would you like to Update? '))
    order =  list_of_orders[index_of_order_update]


    status = order['status']

    for key, value in order.items():
    
        if key == 'courier_index':
            print('\nCouriers list:\n')
            Couriers.print_couriers_list_with_indeces()
            user_input_courier_index = input('\nEnter the index for the new courier: ')

            if not(user_input_courier_index):
                pass
            else:

                order['courier_index'] = int(user_input_courier_index)

        elif key == 'status':
            order_status_options()
            user_input_new_status = input('What status you like the order to have?  ')

            if not(user_input_new_status):
                pass

            else:

                if user_input_new_status == '0':
                    status = 'Preparing!'           
                elif user_input_new_status == '1':
                    status = 'Waiting For Deliver'
                elif user_input_new_status == '2':
                    status = 'Out For Delivery'
                elif user_input_new_status == '3':
                    status = 'Delivered'

        elif key == 'customer_name':
            customer_new_name = input('Please, enter the new name for the customer: ')

            if not(customer_new_name):
                pass
            else:
                order['customer_name'] = customer_new_name

        elif key == 'customer_address':
            customer_new_address = input('Please, enter the new customer address: ')

            if not(customer_new_address):
                pass
            else:
                order['customer_address'] = customer_new_address

        elif key == 'customer_phone':
            customer_phone = input('Please, enter the new customer phone: ')

            if not(customer_phone):
                pass
            else:
                order['customer_phone'] = customer_phone

        elif key =='items':
          
            Products.print_products_list_with_indeces()
            items_input = input('\nEnter the indecse of the items seperated by comma : ')
            
            if not(items_input):
                pass
            else:
                order['items'] = items_input.split(',')

    order['status']  = status  
    list_of_orders[index_of_order_update] = order
    write_orders_file(list_of_orders)

    os.system('cls')
    print('                                  Order has successfully updated\n\n')
    time.sleep(3)


    return order



def display_orders_menu():
    os.system('cls')
    
    orders_menu_options = '''
        [0] Main Menu
        [1] Display Orders
        [2] Add new Order
        [3] Update Order Status
        [4] Update Existing Order
        [5] Delete order
                     '''

    while True :   
        print('Orders Menu Options'.center(100))                 
        print(orders_menu_options)
    
        order_user_input1 = input('Please, choose one from the above choices:') 

        if order_user_input1 == '0':
            break

        elif order_user_input1 == '1':
            os.system('cls')
            print_orders_dictionary_with_indeces()
            time.sleep(3)

            user_choose_where_to_go_input = input('''         
            Enter [y/Y] Return to Order Menu Options.
                  [n/N] Return to Main Menu Options.  ''')
            if user_choose_where_to_go_input in ['y', 'Y']:
                os.system('cls')
                continue
            elif user_choose_where_to_go_input in ['n', 'N']:
                os.system('cls')
                break
            else:
                print('Invalid input, we\'ll redirect you to the Main Menu Options.')
                time.sleep(2)
                os.system('cls')

        elif order_user_input1 == '2':
            os.system('cls')
            user_input_customer_name =input('Enter the customer name: ')
            user_input_customer_address = input('Enter the customer address: ')
            user_input_customer_phone = input('Enter the customer number: ')
            os.system('cls')
            print('\nChoose a courier index from the following couriers list:\n')
            Couriers.print_couriers_list_with_indeces()

            user_input_courier_index =input('The courier\'s index is: ')
            Products.print_products_list_with_indeces()
            customers_items = input('Enter the customer\'s items seperated by comma: ')

            items_list = customers_items.split(',')

            new_order = Orders(str(user_input_customer_name), str(user_input_customer_address), str(user_input_customer_phone), int(user_input_courier_index), status= 'Preparing', items=items_list)
            new_order.add_order_to_file()
            user_choose_where_to_go_input = input('''         
            Enter [y/Y] Return to Order Menu Options.
                  [n/N] Return to Main Menu Options.  ''')

            if user_choose_where_to_go_input in ['y', 'Y']:
                os.system('cls')
                continue
            elif user_choose_where_to_go_input in ['n', 'N']:
                os.system('cls')
                break
            else:
                print('Invalid input, we\'ll redirect you to the Main Menu Options.')
                time.sleep(2)
                os.system('cls')
        elif order_user_input1 == '3':
            os.system('cls')
            print('Orders List with Indeces:\n')
            print_orders_dictionary_with_indeces()

            order_user_input_update_status = input ('Which order would you like to Update? ')

            order_status_options()
            user_input_new_status = input(f'What status would order {order_user_input_update_status} to have?  ')
            
            orders_list = print_orders_dictionary_with_indeces()
            order_to_update =  orders_list[int(order_user_input_update_status)]

            if  user_input_new_status == '0':
                order_to_update['status'] = 'Preparing' 
            if user_input_new_status == '1':
                order_to_update['status'] = 'Waiting For Deliver'
            elif user_input_new_status == '2':
                order_to_update['status'] = 'Out For Delivery'
            elif user_input_new_status == '3':
                order_to_update['status'] = 'Delivered'
            
            write_orders_file(orders_list)
            os.system('cls')
            print(f'order {order_user_input_update_status} status has been Updated..')
            time.sleep(3)
            
            user_choose_where_to_go_input = input('''         
            Enter [y/Y] Return to Order Menu Options.
                  [n/N] Return to Main Menu Options.  ''')
            if user_choose_where_to_go_input in ['y', 'Y']:
                os.system('cls')
                continue
            elif user_choose_where_to_go_input in ['n', 'N']:
                os.system('cls')
                break
            else:
                print('Invalid input, we\'ll redirect you to the Main Menu Options.')
                time.sleep(2)
                os.system('cls')

        elif order_user_input1 == '4':
            os.system('cls')
            update_order()
            user_choose_where_to_go_input = input('''         
            Enter [y/Y] Return to Order Menu Options.
                  [n/N] Return to Main Menu Options.  ''')
            if user_choose_where_to_go_input in ['y', 'Y']:
                continue
            elif user_choose_where_to_go_input in ['n', 'N']:
                break
            else:
                print('Invalid input, we\'ll redirect you to the Main Menu Options.')
                time.sleep(2)
                os.system('cls')

        elif order_user_input1 == '5':

            os.system('cls')
            print('Orders List with Indeces:\n')
            list_of_orders = print_orders_dictionary_with_indeces()
            courier_index_to_delet = input ('Which courier index would you like to delete? ')

            delete_courier_and_order(courier_index_to_delet )
            os.system('cls')
            
            user_choose_where_to_go_input = input('''         
            Enter [y/Y] Return to Order Menu Options.
                  [n/N] Return to Main Menu Options.  ''')
            if user_choose_where_to_go_input in ['y', 'Y']:
                os.system('cls')
                continue
                    
            elif user_choose_where_to_go_input in ['n', 'N']:
                os.system('cls')
                break
        
            else:
                    print('Invalid input, we\'ll redirect you to the Main Menu Options.')
                    time.sleep(2)
                    os.system('cls')
        