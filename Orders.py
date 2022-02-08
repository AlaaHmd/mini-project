import csv
import Products_couriers
import os
import time

class Orders:

    def __init__(self, customer_name : str, customer_address : str, customer_phone : str, courier_index : int, status : str):

        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_phone = customer_phone
        self.courier_index = courier_index
        self.status = status
        
        
        
    def add_order_to_file(self):

        try:

            with open('orders.csv', 'a+', newline= '') as file_data:
                header = ['customer_name','customer_address',
                'customer_phone', 'courier_index', 'status']
                writer = csv.DictWriter(file_data,fieldnames= header )
                # If the file is empty, write the header first then appen the new order.
                if (os.stat("orders.csv").st_size == 0):

                    writer.writeheader()
                    writer.writerow( {  'customer_name' : self.customer_name,
                    'customer_address' : self.customer_address,
                    'customer_phone': self.customer_phone,
                    'courier_index' : self.courier_index,
                    'status' : self.status    })


                else:

                    writer.writerow( {  'customer_name' : self.customer_name,
                'customer_address' : self.customer_address,
                'customer_phone': self.customer_phone,
                'courier_index' : self.courier_index,
                'status' : self.status    }) 

            os.system('cls')
            print('A new order has been added...')
            time.sleep(3) 

        except FileNotFoundError as err:
            print(f'The following exception has araised: {err}')




def print_orders_dictionary_with_indeces():

    order_list = []
    try:

        with open('orders.csv', 'r', newline= '') as file_stream:
           # header =['customer_name','customer_address',
           # 'customer_phone', 'courier_index', 'status']
            csv_file_content = csv.DictReader(file_stream)
            header = csv_file_content.fieldnames

            if  (os.stat("orders.csv").st_size == 0):
                print ('No Orders.....')

            else:
                print('***  The Orders list:   ***\n'.center(100))    
                i = 0
                print( '                      ', header)
                for row in csv_file_content:
                    print(f''''Order index :' {str(i)},      {row.get('customer_name')}      ,      {row.get('customer_address')}      ,      {row.get('customer_phone')}      ,      {row.get('courier_index')}      ,      {row.get('status')}''')
                    i += 1
                    order_list.append(row)
       
        print('\n')
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
        header = ['customer_name','customer_address','customer_phone', 'courier_index', 'status']
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
                 
    if user_input_new_status == '1':
        order['status'] = 'Waiting For Deliver'
    elif user_input_new_status == '2':
        order['status'] = 'Out For Delivery'
    elif user_input_new_status == '3':
        order['status'] = 'Out For Delivery'

    return order


        
def update_order(order):

    for key, value in order.items():
    
        if key == 'courier_index':
            print('\nCouriers list:\n')
            Products_couriers.list_indeces('couriers.txt')
            user_input_courier_index = input('\nEnter the index for the new courier: ')

            if not(user_input_courier_index):
                user_input_courier_index = order.get('courier_index')
            else:

                order['courier_index'] = user_input_courier_index

        elif key == 'status':
            order_status_options()
            user_input_new_status = input(f'What status you like the order to have?  ')

            if not(user_input_new_status):
                
                status = order.get('status')
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
                customer_new_name = order.get('customer_name')
            else:
                order['customer_name'] = customer_new_name

        elif key == 'customer_address':
            customer_new_address = input('Please, enter the new customer address: ')

            if not(customer_new_address):
                 customer_new_address = order.get('customer_address')
            else:
                order['customer_address'] = customer_new_address

        elif key == 'customer_phone':
            customer_phone = input('Please, enter the new customer phone: ')

            if not(customer_phone):
                customer_phone = order.get('customer_phone')
            else:
                order['customer_phone'] = customer_phone
        else:
            pass
        
    order['status']  = status  

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
            Products_couriers.list_indeces('couriers.txt')

            user_input_courier_index =input('The courier\'s index is: ')
            new_order = Orders(str(user_input_customer_name), str(user_input_customer_address), str(user_input_customer_phone), int(user_input_courier_index), status= 'Preparing' )
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
            list_of_orders = print_orders_dictionary_with_indeces()
            index_of_order_update = input ('\nWhich order would you like to Update? ')
            order_to_renew =  list_of_orders[int(index_of_order_update)]
            
            order_to_renew = update_order(order_to_renew)
            list_of_orders.append(order_to_renew)
            list_of_orders.pop(int(index_of_order_update))
            write_orders_file(list_of_orders)
            os.system('cls') 
            print(" ________________________________________ ")
            print('|  Order successfully has been updated   |')
            print("|________________________________________|")
            time.sleep(3)
            
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
        