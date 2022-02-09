import os
import time


# load the file content into a tuple
def sanitise_contents (file_content): 

    data_tuple = tuple()
    for line in file_content:
        data_tuple = data_tuple + ((line.strip('\n')),)
    return data_tuple


# reading the conten of the given text file
# return a tuple of the file content
def read_files(txt_file):

    try:

        with open(txt_file ,'r') as txt_file:
            file_data = txt_file.readlines()

        return (sanitise_contents(file_data))

    except FileNotFoundError as err:
        print('File Not Found')


# add a new item to a text file.
def add_function(new_item, txt_file):
   
    try:

        with open(txt_file , 'a') as file_stream:
            file_stream.write(new_item + '\n')
        os.system('cls')
        print(f'                            {new_item}  is successfully added              \n\n')
        time.sleep(3)

    except FileNotFoundError as bad_error:
        print (f'{bad_error} exception has been araised...')

    finally:
        file_stream.close()
     


# writen back the products/couriers tuples into the text file
def write_to_file (tuple_content , txt_file_name):

    try:
        with open(txt_file_name , 'w') as file_stream:

            for index, element in enumerate(tuple_content):

                file_stream.write((element)+'\n')


    except FileNotFoundError as erro_file:

        print(f'{erro_file} has been araised....')



# update an exsiting item.
def Update_function(index ,new_item , txt_file) :

    file_data =read_files(txt_file) 

    for item_index , item in enumerate(file_data):

        if int(index) == item_index:

            list_values = list(file_data)
            list_values[int(index)]=new_item

    file_data = list_values
    write_to_file(file_data ,txt_file )
    os.system('cls')
    print('                                            Successfully  Updated\n\n')
    time.sleep(3)
    




def delet_function(index , txt_file):
    
    file_data =read_files(txt_file) 

    for item_index , item in enumerate(file_data):

        if int(index) == item_index:

            list_values = list(file_data)
            list_values.pop(int(index))

    file_data = list_values
    write_to_file(file_data ,txt_file )
    os.system('cls')
    print('                                         Successfully Deleted\n\n')
    time.sleep(3)
   

# Display the products/couriers
def print_function(txt_file):
    item_list = []
    try:
        concatenated_str=tuple()
        if txt_file == 'products.txt':
            print('Products List:\n')
        else:
            print('Couriers List:\n')
            
        with open(txt_file ,'r') as file_data:

            lines = file_data.readlines()
             
            for line in lines:
                val = (line.rstrip()).capitalize()
                item_list.append(val)

        item_list = sorted(item_list)
        i = 0
        for item in item_list:
            i +=1
            print(f'{i}- {item}')

    except FileNotFoundError as err:

        print('File can\'t be found')




def move_after_change(user_choice, txt_file):

    if txt_file == 'products.txt':
        if (user_choice == 'y' or user_choice == 'Y'):
            display_product_menu(txt_file)
        else:
            os.system('cls')
    elif txt_file == 'couriers.txt':
        if (user_choice == 'y' or user_choice == 'Y'):
            display_courier_menu(txt_file)
        else:
            os.system('cls')   
    else:
            print ('Please, Enter a valid input : ')



def  display_product_menu(txt_file):
    os.system('cls')
    products_menu_text ='''                                         _______________________________________
                                        |                                       |
                                        |         Products Menu Options         |
                                        |_______________________________________|
                                         
            
            [ 0 ]  Main Menu
            [ 1 ]  Products List
            [ 2 ]  Create New Product
            [ 3 ]  Update Exsiting Product
            [ 4 ]  Delete Product   
            
            Please enter your choice:     '''
 

    user_inptu2= input(products_menu_text)

    if user_inptu2 == '0':
            
        os.system('cls')
        pass   
                    
    elif user_inptu2 == '1':

        os.system('cls')
        print_function(txt_file)
            
        user_input3 = input('\nWould you like to return to the Products Menu Options?(y/n)')
        move_after_change(user_input3 , txt_file )
        
    elif user_inptu2 == '2':

        os.system('cls')
        new_item = input('Enter The Product Name: ')
        item_price = float(input('Enter the product price: '))
        add_function(new_item, txt_file)
        
        user_input4 = input('\n\n Would you like to return to the Products Menu Options?(y/n)')
        move_after_change(user_input4 , txt_file)
     
    elif user_inptu2 == '3':

        os.system('cls')
        list_indeces(txt_file)
        Updated_item_index= input('Enter the index of the product that you want to UPDATE : ')
        Product_Name = input('Enter The Name of The New Product...')
        Update_function(Updated_item_index,Product_Name , txt_file)
        user_input5 = input('\nWould you like to return to the Products Menu Options?(y/n)')
        move_after_change(user_input5 , txt_file)

    elif user_inptu2 == '4':

        os.system('cls')
        list_indeces(txt_file)
        Item_Index_Delete= input('Enter the index of the product that you want to Delete : ')
        delet_function(Item_Index_Delete ,txt_file)
        user_input6 = input('\nWould you like to return to the Products Menu Options?(y/n)')
        move_after_change(user_input6 , txt_file)

    else:
        print(' Invalid Input, Try Again. ')



def display_courier_menu(txt_file):

    os.system('cls')

    

    user_inptu2= input('''                                     Couriers Menu Options 
            
        [ 0 ]  Main Menu
        [ 1 ]  Couriers List
        [ 2 ]  Create New Courier
        [ 3 ]  Update Exsiting Courier
        [ 4 ]  Delete Courier   ''')

    if user_inptu2 == '0':

        os.system('cls')
        pass
        
            
    elif user_inptu2 == '1':

        os.system('cls')
        print_function(txt_file)
        user_input3 = input('\n Would you like to return to the Couriers Menu Options?(y/n)')
        move_after_change(user_input3 , txt_file )

    elif user_inptu2 == '2':

        os.system('cls')
        new_item = input('Enter The Courier Name : ')
        add_function(new_item, txt_file)
        user_input4 = input('\n Would you like to return to the Couriers Menu Options?(y/n)')
        move_after_change(user_input4 , txt_file)

    elif user_inptu2 == '3':

        os.system('cls')
        list_indeces(txt_file)
        Updated_item_index= input('Enter the index of the courier that you want to UPDATE : ')
        Product_Name = input('Enter The Name of The New courier : ')
        Update_function(Updated_item_index,Product_Name ,txt_file)
        user_input5 = input('\n Would you like to return to the Couriers Menu Options?(y/n)')
        move_after_change(user_input5 , txt_file)

    elif user_inptu2 == '4':

        os.system('cls')
        list_indeces(txt_file)
        Item_Index_Delete= input('Enter the index of the courier that you want to Delete : ')
        delet_function(Item_Index_Delete , txt_file)
        user_input6 = input('\n Would you like to return to the Couriers Menu Options?(y/n)')
        move_after_change(user_input6 , txt_file)   

    else:
        print(''' Invalid Input, Try Again. Choose A number From The Couriers Menu Options. \n''')



def list_indeces(file_name):

    file_data = read_files(file_name)

    if file_name == 'couriers.txt':
        print('             Courier Name')
        for index, item in enumerate (file_data):
        
            print(f' Index: {index}, {item}')

    else:
            print('          Product Name')
            for index, item in enumerate (file_data):
               
                print(f' Index: {index}, {item}')



def save_files(txt_file):

    with open(txt_file , 'a') as file_content:
        file_content.close() 