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



def update_courier(courier_id):

        new_name_for_courier = input('Enter the new name of the courier: ')
        new_phone_for_courier = input('\nEnter the new phone for the courier: ')

                    
        if  not (new_name_for_courier):
            pass

        else:
            connection= methods.connect_to_db()
            update_query_1 = f'''update Couriers set name = "{new_name_for_courier}" where id = {courier_id}'''
            methods.commit_query(connection , update_query_1)
            methods.close_db(connection)

                
        if not (new_phone_for_courier):
            pass

        else:
                 
            connection_obj= methods.connect_to_db()
            update_query_2 = f'''update Couriers set phone = "{new_phone_for_courier}" where id = {courier_id}'''
            methods.commit_query(connection_obj , update_query_2)
            methods.close_db(connection_obj)


        os.system('cls')
        print('  The courrier has been successfully  Updated\n\n')
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
        methods.close_db(connection_courier_object)
        couriers_list = methods.db_to_list(couriers_rows_from_db, 'Couriers')
        print('Couriers List: ')
        methods.print_list(couriers_list)

        courier_id= int(input('\nEnter the id of the courier that you want to update : '))

        connection_1 = methods.connect_to_db()
        courier_query = f''' SELECT COUNT(*) FROM Orders WHERE courier_id = {courier_id}'''
        rows = methods.select_query(connection_1, courier_query)
        methods.close_db(connection_1)

        for row in rows:
            if (row[0] != 0):
                os.system('cls')
                print('Can\'t update this courier. Courier is on Orders Table.')
                user_input = input('''Would you like to delete the orders which have this courier.\nThen continue updating the courier? (y,n)''')

                if (user_input in ['y','Y']):

                    connection_1 = methods.connect_to_db()
                    query_1 = f''' DELETE FROM Orders where courier_id = {courier_id}'''
                    methods.commit_query(connection_1, query_1)
                    methods.close_db(connection_1)
                    update_courier(courier_id)
                    running = methods.stay_at_menu_or_go_main('Couriers')
                    if not(running):
                        os.system('cls')
                        break
                    else:
                        continue     
            else:
                update_courier(courier_id)
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

        connection_obj = methods.connect_to_db()
        couriers_in_orders_table_query = f''' SELECT COUNT(*) FROM Orders where courier_id = {courier_id} '''
        rows = methods.select_query(connection_obj, couriers_in_orders_table_query)
        methods.close_db(connection_obj)

        
        for row in rows:
            if row[0] != 0:

                os.system('cls')
                print('''>>>> Courier is holding an order, can\'t delete it.\n>>>> You Can delete this order from Orders Table, then delete the courier!''')
                time.sleep(3)
                pass
                break
                    
            else:

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
