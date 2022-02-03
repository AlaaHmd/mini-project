import os

global couriers
couriers = []
global couriers_data



#Function to Add new Product
#It has a parameter which is the name of the product.
def Add_Courier(New_Courier):
   
    for item in couriers:
        
        if str(item).lower() == New_Courier.lower():
            print('{} is already in the list. Check Again The Name of The New courier.'.format(New_Courier))
            break
    
    couriers.append(New_Courier)
    couriers_data = open('couriers.txt' , 'a')
    couriers_data.write('\n'+New_Courier)
    couriers_data.close()
    os.system('cls')
    print('                            The Courier is successfully added              ')
     


#Function to Update an existing courier
# It takes 2 parameters: string: the index of the courier, string: the name of the updated courier. 
def Update_courier(index,New_courier):

    for item in couriers:
        if str(item).lower() == New_courier.lower():
            print('{} is already in the menu. Check Again To Update Exsiting Courier, Look To The courier Menu Options.'.format(New_courier))
            break
    
    couriers[int(index)]= New_courier
    couriers_data= open('products.txt','w')
    for line in couriers:
        couriers_data.write(line+'\n')

    couriers_data.close()
    os.system('cls')
    print('                               The Courier has been successfully Updated                    ')


#Function to delete a courier.
#It takes a parameter: string index of the courier which we need to delete
def Delet_courier(index):
    
    if int(index) in range(len(couriers)):
        couriers.pop(int(index))
        couriers_data = open('couriers.txt','w')
        for index in range(len(couriers)):
            couriers_data.write(couriers[index]+'\n')
        couriers_data.close()
        os.system('cls')
        print('                                The courier has been successfully Deletted')
    else:
        print('<<<<<<<<<<<<<<<<<      Wrong Number, Try Again.    >>>>>>>>>>>>>>>>>>>')


# Function used to display all the couriers
def Print_couriers():
    print (couriers)

# Function displays the couriers along with their indeces
def Couriers_Indeces():

    for index in range(len(couriers)):
        print(f'Courier Name: {couriers[index]}, The index: {index}')


#Function displays the courier menu
def Display_Couriers_Menu():
    os.system('cls')
    while True:
        user_inptu2= input('''                                     Couriers Menu Options 
            
            Enter 0 to return to Main Menu
            Enter 1 to display the Courier List
            Enter 2 to Create New Courier
            Enter 3 to Update Exsiting Courier
            Enter 4 to Delete Courier......     ''')
        if user_inptu2 == '0':
            os.system('cls')
            break
                  
        elif user_inptu2 == '1':
            os.system('cls')
            Print_couriers()
            break
        elif user_inptu2 == '2':
            os.system('cls')
            new_item = input('Enter The Courier Name....')
            Add_Courier(new_item)
            break
        elif user_inptu2 == '3':
            os.system('cls')
            Couriers_Indeces()
            Updated_item_index= input('Enter the index of the courier that you want to UPDATE....')
            Courier_Name = input('Enter The Name of The New courier...')
            Update_courier(Updated_item_index,Courier_Name)
            break
        elif user_inptu2 == '4':
            os.system('cls')
            Couriers_Indeces()
            Item_Index_Delete= input('Enter the index of the courier that you want to Delete....')
            Delet_courier(Item_Index_Delete)
            break
        else:
            print(' >>>>>>>>>>>>>>>> Invalid Input, Try Again. Choose A number From The courier Menu Options >>>>>>>>>>>>>>>>')


def loading_couriers():

    couriers_data = open('couriers.txt' ,'r')

    for line in couriers_data:
        couriers.append(line.strip('\n'))
    #print(len(couriers))
    couriers_data.close()
    return couriers

def save_couriers():

    couriers_data= open('couriers.txt','w')
    for line in couriers:
        couriers_data.write(line+'\n')

    couriers_data.close() 










