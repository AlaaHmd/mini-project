import pymysql
import os
from dotenv import load_dotenv
import time
import Couriers
import csv
import time

class Couriers:

    def __init__(self, name : str, phone : str):

        self.name = name
        self.phone = phone
      
        

    def add_courier_to_file(self):
      
        couriers_list = []
        try:
            if  not (os.stat("couriers.csv").st_size == 0):
               
                with open('couriers.csv', 'r', newline= '') as file_data:
                    
                    reader = csv.DictReader(file_data )
                    header = next(reader)

                    for courier in reader:
                        couriers_list.append(courier)

                with open('couriers.csv', 'a+', newline= '') as file_stream:
                    writer = csv.DictWriter(file_stream,fieldnames= header )
                    
                    writer.writerow( {  'name' : self.name,
                    'phone' : self.phone  })
                couriers_list.append(self)

            else:
                with open('couriers.csv', 'w', newline= '') as file_content:
                    header = ['name', 'phone']
                    writer = csv.DictWriter(file_content,fieldnames= header )
                    writer.writeheader()
                    writer.writerow( {  'name' : self.name,
                    'phone' : self.phone  })

                couriers_list.append(self)
    
        except FileNotFoundError as err:
            print(f'The following exception has araised: {err}')

    
        os.system('cls')
        print('A new courier has been added...')
        time.sleep(3) 



def print_couriers_list_with_indeces():

    couriers_list = []
    try:

        with open('couriers.csv', 'r', newline= '') as file_stream:
     
            csv_file_content = csv.DictReader(file_stream)
            header = csv_file_content.fieldnames

            if  (os.stat("couriers.csv").st_size == 0):
                print ('No couriers.....')
                time.sleep(3)

            else:
                print('   Couriers List:   \n'.center(60))    
                index = 0
     
                for row in csv_file_content:
                    print(f'courier index : {index}', row )
                    index += 1
                    couriers_list.append(row)
       
      
        return couriers_list

    except FileNotFoundError as bad_erro:
        print(f' Not able to open couriers.csv, exception occured :{bad_erro}')




def write_couriers_to_csvfile(couriers_list):

    try:

        with open('couriers.csv', 'w', newline= '') as file_data:
            header = ['name','phone']
            writer = csv.DictWriter(file_data, fieldnames= header)
            writer.writeheader()

            for courier in couriers_list:
                writer.writerow(courier)
    
    except FileNotFoundError as no_file:
        print(f'Can\'t open the file, {no_file} exception has occured!')





def update_courier():

    couriers_list = print_couriers_list_with_indeces()
    courier_index= int(input('\nEnter the index of the courier that you want to update : '))
    courier_object = couriers_list[courier_index]

    new_name_for_courier = input('Enter the new name of the courier: ')
    new_phone_for_courier = input('\nEnter the new phone for the courier: ')

    if (new_name_for_courier):
        courier_object['name'] = new_name_for_courier
            
    if (new_phone_for_courier):
        courier_object['phone'] = new_phone_for_courier
        

    couriers_list[courier_index] = courier_object
    write_couriers_to_csvfile(couriers_list)

    os.system('cls')
    print('  The courrier has been successfully  Updated\n\n')
    time.sleep(3)



def delete_courier ():

    courier_list = print_couriers_list_with_indeces()
    courier_index_to_delete= int(input('Enter the index of the courier that you want to delete : '))

    courier_object = courier_list[courier_index_to_delete]
    courier_list.pop(courier_index_to_delete)

    write_couriers_to_csvfile(courier_list)
    os.system('cls')
    print(f' The following courier : {courier_object}  has been deleted')
    time.sleep(3)



def stay_at_courier_menu_or_go_main():
    
    running = 1
    user_choose_where_to_go_input = input('''         
            Enter [y/Y] Return to Courier Menu Options.
                  [n/N] Return to Main Menu Options.  ''')

    if user_choose_where_to_go_input in ['y', 'Y']:
        os.system('cls')
        return running
                    
    elif user_choose_where_to_go_input in ['n', 'N']:
        os.system('cls')
        running = 0
        return running




# def display_courier_menu():

#  while True: 

#     os.system('cls')

#     courier_menu_input= input('''                                     Couriers Menu Options 
            
#         [ 0 ]  Main Menu
#         [ 1 ]  Couriers List
#         [ 2 ]  Create New Courier
#         [ 3 ]  Update Exsiting Courier
#         [ 4 ]  Delete Courier   ''')

   


#     if courier_menu_input == '0':

#         os.system('cls')
#         break

        
            
#     elif courier_menu_input == '1':

#         os.system('cls')
#         print_couriers_list_with_indeces()

#         running = stay_at_courier_menu_or_go_main()
#         if not(running):
#             os.system('cls')
#             break
#         else:
#             continue

#     elif courier_menu_input == '2':

#         os.system('cls')
#         new_courier_name = input('Enter the courier Name : ')
#         new_courier_phone = input('Enter the courier phone:')
#         courier_object = Couriers(new_courier_name,new_courier_phone)
#         courier_object.add_courier_to_file()

#         running = stay_at_courier_menu_or_go_main()
#         if not(running):
#             os.system('cls')
#             break
#         else:
#             continue

#     elif courier_menu_input == '3':

#         os.system('cls')

#         update_courier()

#         running = stay_at_courier_menu_or_go_main()
#         if not(running):
#             os.system('cls')
#             break
#         else:
#             continue

#     elif courier_menu_input == '4':

#         os.system('cls')
#         delete_courier()

#         running = stay_at_courier_menu_or_go_main()
#         if not(running):
#             os.system('cls')
#             break
#         else:
#             continue
 
#     else:
#         print('''\n Invalid Input, Try Again.''')




def save_file():

    try:

        file_content = open('couriers.csv' , 'a') 
        file_content.close() 

    except FileNotFoundError as bad_file:
        print(f'Can\'t read couriers.csv. {bad_file} has occured.')