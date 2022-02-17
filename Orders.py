import csv
from operator import index
from typing import List
from unicodedata import numeric
import Couriers
import os
import time
import Cafe_parts

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




def get_orders_list():

    order_list = []
    try:

        with open('orders.csv', 'r', newline= '') as file_stream:

            csv_file_content = csv.DictReader(file_stream)
            header = csv_file_content.fieldnames

            for row in csv_file_content:

                order_list.append(row)
       
        return order_list

    except FileNotFoundError as bad_erro:
        print(f' The following exception occured :{bad_erro}')



def display_order_list(order_list):

    index = 0
    for row in order_list:
        print(f'Order index: {index}',row)
        index += 1
 




def write_orders_file(Orders_list):

    with open('orders.csv', 'w', newline= '') as file_data:
        header = ['customer_name','customer_address','customer_phone', 'courier_index', 'status', 'items']
        writer = csv.DictWriter(file_data, fieldnames= header)
        writer.writeheader()

        for order in Orders_list:
            writer.writerow(order)



    
def delete_order ():

    os.system('cls')
    print('Orders List:\n')
    list_of_orders = get_orders_list()
    display_order_list(list_of_orders)
    order_index_to_delet = int(input ('\nEnter the order\'s index you like to delete: '))
    order_object = list_of_orders[order_index_to_delet]
    list_of_orders.pop(order_index_to_delet)
    write_orders_file(list_of_orders)
    os.system('cls')
    print(f'The following order has been deleted:\n {order_object}')
    time.sleep(3)



def order_status_list():

    order_status_list = ['Preparing','Waiting For Deliver','Out For Delivery','Delivered']
    print('\n     Order Status List       \n')

    for index in range(len(order_status_list)):

        print(f'Order status index: {index},',order_status_list[index])

    return order_status_list
  



def Update_order_status( ):  
         
    orders_list=  get_orders_list()
    display_order_list(orders_list)
    order_index_to_update_status = int(input ('Which order would you like to Update its status? '))

    order_list_status = order_status_list()

    user_input_new_status = int(input(f'\nEnter the index for the new order\'s status:  '))
            
    order_to_update =  orders_list[order_index_to_update_status]

    for index in range(len(order_list_status)):

        if  index == user_input_new_status:

            order_to_update['status'] = order_list_status[index]
        
    
    write_orders_file(orders_list)
    os.system('cls')
    print('The order\'s status has been updated..')
    return order_to_update


        
def update_order():

    list_of_orders = get_orders_list()
    display_order_list(list_of_orders)
    index_of_order_update = int(input ('\nWhich order would you like to Update? '))
    order =  list_of_orders[index_of_order_update]

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
            order_statust_list = order_status_list()
            user_input_new_status = input('\nEnter the index of the new status you want:  ')

            if user_input_new_status is not numeric or user_input_new_status is None:
                pass
            elif int(user_input_new_status) in [0,len(order_statust_list)-1]:
                order['status']  = order_statust_list[int(user_input_new_status)] 

            else:   
                pass

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
          
            Cafe_parts.print_products_list_with_indeces()
            items_input = input('\nEnter the indecse of the items seperated by comma : ')
            
            if not(items_input):
                pass
            else:
                order['items'] = items_input.split(',')
 
    list_of_orders[index_of_order_update] = order
    write_orders_file(list_of_orders)

    os.system('cls')
    print('                                  Order has successfully updated\n\n')
    time.sleep(3)

    return order




def stay_at_Orders_or_go_main():
    
    running = 1
    user_choose_where_to_go_input = input('''         
    Enter [Y/y] Return to Order Menu Options.
          [N/n] Return to Main Menu Options.  ''')

    if user_choose_where_to_go_input in ['y', 'Y']:
        os.system('cls')
        return running
                    
    elif user_choose_where_to_go_input in ['n', 'N']:
        os.system('cls')
        running = 0
        return running



def create_new_order():

    user_input_customer_name =input('Enter the customer name: ')
    user_input_customer_address = input('Enter the customer address: ')
    user_input_customer_phone = input('Enter the customer number: ')
    os.system('cls')
    print('\nChoose a courier index from the following couriers list:\n')
    Couriers.print_couriers_list_with_indeces()

    user_input_courier_index =input('\nThe courier\'s index is: ')
    Cafe_parts.print_products_list_with_indeces()
    customers_items = input('\nEnter the customer\'s items seperated by comma: ')

    items_list = customers_items.split(',')
    new_order = Orders(str(user_input_customer_name), str(user_input_customer_address), str(user_input_customer_phone), int(user_input_courier_index), status= 'Preparing', items=items_list)
    new_order.add_order_to_file()



def list_orders_grouping_by_status ():

    orders_list = get_orders_list()
    order_list_status = order_status_list()

    order_list_grouped_by_status = []
    os.system('cls')
    print('\nGrouping orders by status:')
    for status in order_list_status:
           
        counter = 0
        for order in orders_list:
            if(status == order.get('status')):
                order_list_grouped_by_status.append(order)
                counter += 1
        
        if counter !=0:
            print(f'\n ** {status}  status **, {counter} orders: ')
            for index in range(len(order_list_grouped_by_status)):
                print(f'{index+1}- {order_list_grouped_by_status[index]}')    
        
        else:
            print(f'\n ** {status} " status ** :\n No orders.')  

        order_list_grouped_by_status.clear()

    



def display_orders_menu():
    os.system('cls')
    
    orders_menu_options = '''
        [0] Main Menu
        [1] Display Orders
        [2] Add new Order
        [3] Update Order Status
        [4] Update Existing Order
        [5] Delete order
        [6] List Orders by Status.
                     '''

    while True :   
        print('Orders Menu Options'.center(100))                 
        print(orders_menu_options)
    
        order_user_input1 = input('Please, choose one from the above choices:') 

        if order_user_input1 == '0':
            os.system('cls')
            break

        elif order_user_input1 == '1':
            os.system('cls')
            print('***  The Orders list:   ***\n'.center(100)) 
            order_list = get_orders_list()
            display_order_list(order_list)

            time.sleep(3)

            running = stay_at_Orders_or_go_main()
            if not(running):
                os.system('cls')
                break
            else:
                continue

        elif order_user_input1 == '2':
            os.system('cls')
            create_new_order()
            running = stay_at_Orders_or_go_main()
            if not(running):
                os.system('cls')
                break
            else:
                continue
        elif order_user_input1 == '3':

            os.system('cls')
            Update_order_status()
            time.sleep(3)
  
            running = stay_at_Orders_or_go_main()
            if not(running):
                os.system('cls')
                break
            else:
                continue

        elif order_user_input1 == '4':

            os.system('cls')
            update_order()

            running = stay_at_Orders_or_go_main()
            if not(running):
                os.system('cls')
                break
            else:
                continue

        elif order_user_input1 == '5':

            delete_order( )
            os.system('cls')
            
            running = stay_at_Orders_or_go_main()
            if not(running):
                os.system('cls')
                break
            else:
                continue
        
        elif order_user_input1 == '6':
            os.system('cls')
            list_orders_grouping_by_status()
            time.sleep(3)

            running = stay_at_Orders_or_go_main()
            if not(running):
                os.system('cls')
                break
            else:
                continue
        

        else:
            print('Invalid input, we\'ll redirect you to the Main Menu Options.')
            time.sleep(2)
            os.system('cls')
        