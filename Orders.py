from typing import List, Dict
import csv
import Products_couriers
import os
import time

class Orders:

    def __init__(self, customer_name, customer_address, customer_phone, courier_index, status):

        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_phone = customer_phone
        self.courier_index = courier_index
        self.status = status
        #self = dict(self)
        
        
    def add_order_to_file(self):

       
        with open('orders.csv', 'a+', newline= '') as file_data:
            header = ['customer_name','customer_address',
        'customer_phone', 'courier_index', 'status']
            writer = csv.DictWriter(file_data,fieldnames= header )
       # writer.writeheader()
            writer.writerow( {  'customer_name' : self.customer_name,
            'customer_address' : self.customer_address,
            'customer_phone': self.customer_phone,
            'courier_index' : self.courier_index,
            'status' : self.status    }) 
        os.system('cls')
        print('A new order has been added...')
        time.sleep(3) 


    # def add_new_order_to_csv_file(self):
        
    #     with open('orders.csv', 'w', newline= '') as file_data:
    #         header = ['customer_name','customer_address','customer_phone', 'courier_index', 'status']
    #         writer = csv.DictWriter(file_data, fieldnames= header)
    #         writer.writeheader()
    #         writer.writerow( {  'customer_name' : self.customer_name,
    #         'customer_address' : self.customer_address,
    #         'customer_phone': self.customer_phone,
    #         'courier_index' : self.courier_index,
    #         'status' : self.status    })


def print_orders_dictionary_with_indeces():
    order_list = []

    with open('orders.csv', 'r', newline= '') as file_stream:

        csv_file_content = csv.DictReader(file_stream)

        #next(csv_file_content)

        print('***  The Orders list:   ***\n')    
        i = 0
        for row in csv_file_content:
            print(f'''{str(i)} : {row.get('customer_name')} ,{row.get('customer_address')}, {row.get('customer_phone')} , {str(row.get('courier_index'))} , {row.get('status')}''')
            i += 1
            order_list.append(row)
        print('\n')

    return order_list





def add_order_to_csv(order):

    order_list = []
    order_list = print_orders_dictionary_with_indeces()
    order_list.append(order)
    write_orders_file(order_list)

    # with open('orders.csv', 'a', newline= '') as file_data:
    #     header = ['customer_name','customer_address',
    #     'customer_phone', 'courier_index', 'status']
    #     writer = csv.DictWriter(file_data,fieldnames= header  )
    #    # writer.writeheader()
    #     writer.writerow( {  'customer_name' : Orders.customer_name,
    #         'customer_address' : Orders.customer_address,
    #         'customer_phone': Orders.customer_phone,
    #         'courier_index' : Orders.courier_index,
    #         'status' : Orders.status    }) 
    os.system('cls')
    print('A new order has been added...')
    time.sleep(3)

# def update_order_status(order_index, new_status):

        
#     for key , value in kwargs:
#         self.key = value

#         Orders.add_order_after_change_status(self)



def write_orders_file(Orders_list):

    with open('orders.csv', 'w', newline= '') as file_data:
        header = ['customer_name','customer_address','customer_phone', 'courier_index', 'status']
        writer = csv.DictWriter(file_data, fieldnames= header)
        writer.writeheader()

        for order in Orders_list:
            writer.writerow(order)


# def print_orders_with_indces ():

#      with open('orders.csv', 'r', newline= '') as file_stream:
#         csv_file_content = csv.DictReader(file_stream)

#        # print(next(csv_file_content))
#         i = 0
#         for row in csv_file_content:
#             print(str(i) +":"+ row)
#             i += 1

             

        
    
def delete_courier_and_order (courier_index):
    
        with open('orders.csv', 'r', newline= '') as file_stream:
            csv_file_content = csv.DictReader(file_stream)

            print(next(csv_file_content))

            order_list = []
            for row in csv_file_content:
                if int(row.get('courier_index'))== courier_index:
                    del row
                    print(f'Courier index :{courier_index} has been deleted.')
                else:
                    order_list.append(row)
        
        write_orders_file(order_list)
        
def update_order(order):

    for key, value in order.items():
        user_input_to_change_value = input(f'Enter the new value for {key}')
        
        if not(user_input_to_change_value):
            pass
        else:
            if key == 'coustomer_index':
                order[key] = int(user_input_to_change_value)
            else:
                order[key] = user_input_to_change_value
                
    print('Order has been updated.')
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
    order_status_list = '''
            These are the available statuses:

            [0] Preparing
            [1] Waiting For Deliver
            [2] Out For Delivery
            [3] Delivered
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
            continue
        elif order_user_input1 == '2':
            os.system('cls')
            user_input_customer_name =input('Enter the customer name: ')
            user_input_customer_address = input('Enter the customer address: ')
            user_input_customer_phone = input('Enter the customer number: ')
            print('\nCouriers list\n')
            Products_couriers.list_indeces('couriers.txt')

            user_input_courier_index = input('Enter the index of the courier: ')
            new_order = Orders(str(user_input_customer_name), str(user_input_customer_address), str(user_input_customer_phone), int(user_input_courier_index), status= 'Preparing' )
            new_order.add_order_to_file()
            continue

        elif order_user_input1 == '3':
            os.system('cls')
            print('Orders List with Indeces:\n')
            print_orders_dictionary_with_indeces()

            order_user_input_update_status = input ('Which order would you like to Update? ')


            print(order_status_list)
            user_input_new_status = input(f'What status would order {order_user_input_update_status} to have?  ')

            orders_list = print_orders_dictionary_with_indeces()

            for index , order in enumerate(orders_list):
                if index ==  int(order_user_input_update_status):
                    if user_input_new_status == '1':
                        order['status'] = 'Waiting For Deliver'
                    elif user_input_new_status == '2':
                        order['status'] = 'Out For Delivery'
                    elif user_input_new_status == '3':
                        order['status'] = 'Delivered'

            write_orders_file(orders_list)
            os.system('cls')
            print(f'order {order_user_input_update_status} status has been Updated..')
            time.sleep(3)
            continue
        elif order_user_input1 == '4':
            os.system('cls')
            print('Orders List with Indeces:\n')
            print_orders_dictionary_with_indeces()
            order_user_input_update_status = input ('Which order would you like to Update? ')

            list_of_orders = print_orders_dictionary_with_indeces()

            for index , order in enumerate(list_of_orders):

                if index ==  int(order_user_input_update_status):
                    order = update_order(order)
        
            write_orders_file(list_of_orders)
            continue
        elif order_user_input1 == '5':

            os.system('cls')
            print('Orders List with Indeces:\n')
            list_of_orders = print_orders_dictionary_with_indeces()
            courier_index_to_delet = input ('Which couriers would you like to delete? ')

            delete_courier_and_order(int(courier_index_to_delet ))
            continue
        