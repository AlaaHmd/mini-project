import methods
import os
import time

class Couriers:

    def __init__(self, name : str, phone : str):

        self.name = name
        self.phone = phone
      
        

    def add_new_courier_to_db(self):

        connection = methods.connect_to_db()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Couriers (name, phone) values (%s,%s)", (self.name,self.phone))
        connection.commit()
        cursor.close()
        connection.close()
        os.system('cls')
        print('A new courier has been added...')
        time.sleep(3) 



######################################################




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

        connection = methods.connect_to_db()
        select_products_query = 'SELECT * FROM Couriers'
        couriers_db_rows = methods.select_query(connection , select_products_query)
        couriers_list = methods.db_to_list(couriers_db_rows, 'Couriers')
        os.system('cls')
        print('Couriers list:\n')           
        methods.print_list(couriers_list)
        running = methods.stay_at_menu_or_go_main('Couriers')
        if not(running):
            os.system('cls')
            break
        else:
            continue

    elif courier_menu_input == '2':

        os.system('cls')
        new_courier_name = input('Enter the courier Name : ')
        new_courier_phone = input('Enter the courier phone:')
        courier_object = Couriers(new_courier_name,new_courier_phone)
        courier_object.add_new_courier_to_db()

        running = methods.stay_at_menu_or_go_main('Couriers')
        if not(running):
            os.system('cls')
            break
        else:
            continue

    elif courier_menu_input == '3':
        os.system('cls')
        connection_courier_object = methods.connect_to_db()
        courier_query ="SELECT * FROM Couriers"
        couriers_rows_from_db = methods.select_query(connection_courier_object , courier_query)
        couriers_list = methods.db_to_list(couriers_rows_from_db, 'Couriers')
        print('Couriers List: ')
        methods.print_list(couriers_list)

        courier_id= int(input('\nEnter the id of the courier that you want to update : '))
        new_name_for_courier = input('Enter the new name of the courier: ')
        new_phone_for_courier = input('\nEnter the new phone for the courier: ')

                    
        if  not (new_name_for_courier):
            pass

        else:

            update_query_1 = f'''update Couriers set name = "{new_name_for_courier}" where id = {courier_id}'''
            methods.commit_query(connection , update_query_1)

                
        if not (new_phone_for_courier):
            pass

        else:

            update_query_2 = f'''update Couriers set phone = "{new_phone_for_courier}" where id = {courier_id}'''
            methods.commit_query(connection , update_query_2)


        os.system('cls')
        print('  The courrier has been successfully  Updated\n\n')
        time.sleep(3)

        running = methods.stay_at_menu_or_go_main('Couriers')
        if not(running):
            os.system('cls')
            break
        else:
            continue

    elif courier_menu_input == '4':

        os.system('cls')
        connection = methods.connect_to_db()
        cursor = connection.cursor()

        courier_query = 'SELECT * FROM Couriers'
        couriers_db_rows = methods.select_query(connection , courier_query)

        couriers_list = methods.db_to_list(couriers_db_rows, 'Couriers')
        print('Couriers List:\n\n')
        methods.print_list(couriers_list)

        courier_id = int(input('Enter the index of the courier to delete it: '))
        delet_courier_query = f"DELETE FROM Couriers where id = {courier_id}"

        methods.commit_query(connection,delet_courier_query )
        os.system('cls')
        print('Courier has been deleted')
        time.sleep(2)

        running = methods.stay_at_menu_or_go_main('Couriers')
        if not(running):
            os.system('cls')
            break
        else:
            continue
    
    elif  courier_menu_input == '5': 
        os.system('cls')
        methods.write_db_to_csvfile('Couriers')
        print('Couriers table has been exported to Couriers.csv')
        time.sleep(2)
    
        running = methods.stay_at_menu_or_go_main('Couriers')
        if not(running):
            os.system('cls')
            break
        else:
            continue 
 
    else:
        print('''\n Invalid Input, Try Again.''')
