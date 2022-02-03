import os
import time
import couriers


#global products
products=[]
#global file_data




#Function to Add new Product
#It has a parameter which is the name of the product.
def Add_Product(New_Product):
   
    for item in products:
        
        if str(item).lower() == New_Product.lower():
            print('{} is already in the menu. Check Again The Name of The New Poduct.'.format(New_Product))
            break
    
    products.append(New_Product)
    file_data = open('products.txt' , 'a')
    file_data.write('\n'+New_Product)
    file_data.close()
    os.system('cls')
    print('                            The Product is successfully added              ')
     

#Function to Update an existing product
# It takes 2 parameters: string: the index of the product, string: the name of the updated product. 
def Update_Product(index,New_Product):

    for item in products:
        if str(item).lower() == New_Product.lower():
            print('{} is already in the menu. Check Again To Update Exsiting Poduct, Look To The Products Menu Options.'.format(New_Product))
            break
    
    products[int(index)]= New_Product
    file_data= open('products.txt','w')
    for line in products:
        file_data.write(line+'\n')

    file_data.close()
    os.system('cls')
    print('                               The Product has been successfully Updated                    ')


#Function to delete a product.
#It takes a parameter: string index of the product which we need to delete
def Delet_products(index):
    
    if int(index) in range(len(products)):
        products.pop(int(index))
        file_data = open('products.txt','w')
        for index in range(len(products)):
            file_data.write(products[index]+'\n')
        file_data.close()
        os.system('cls')
        print('                                The Product has been successfully Deletted')
    else:
        print('<<<<<<<<<<<<<<<<<      Wrong Number, Try Again.    >>>>>>>>>>>>>>>>>>>')


# Function used to display all the products
def Print_Products():
    print (products)

# Function displays the products along with their indeces
def Products_Indeces():

    for index in range(len(products)):
        print(f'Product Name: {products[index]}, The index: {index}')


#Function displays the product menu
def Display_Product_Menu():
    os.system('cls')
    while True:
        user_inptu2= input('''                                     Products Menu Options 
            
            Enter 0 to return to Main Menu
            Enter 1 to display the Products List
            Enter 2 to Create New Product
            Enter 3 to Update Exsiting Product
            Enter 4 to Delete Product......     ''')
        if user_inptu2 == '0':
            os.system('cls')
            break
        
            
        elif user_inptu2 == '1':
            os.system('cls')
            Print_Products()
            break
        elif user_inptu2 == '2':
            os.system('cls')
            new_item = input('Enter The Product Name....')
            Add_Product(new_item)
            break
        elif user_inptu2 == '3':
            os.system('cls')
            Products_Indeces()
            Updated_item_index= input('Enter the index of the product that you want to UPDATE....')
            Product_Name = input('Enter The Name of The New Product...')
            Update_Product(Updated_item_index,Product_Name)
            break
        elif user_inptu2 == '4':
            os.system('cls')
            Products_Indeces()
            Item_Index_Delete= input('Enter the index of the product that you want to Delete....')
            Delet_products(Item_Index_Delete)
            break
        else:
            print(' >>>>>>>>>>>>>>>> Invalid Input, Try Again. Choose A number From The Products Menu Options >>>>>>>>>>>>>>>>')


def loading_products():

    file_data = open('products.txt' ,'r')

    for line in file_data:
        products.append(line.strip('\n'))
    print(len(products))
    file_data.close()
    return products


def save_products():

    file_data= open('products.txt','w')
    for line in products:
        file_data.write(line+'\n')

    file_data.close() 

def main():
    products = loading_products()
    couriers.couriers= couriers.loading_couriers()
    os.system('cls')
    while True:
        user_input = input( '''                                        Main Menu Options

                            Enter 0 to Exit , 
                            Enter 1 to display the Products Menu Options ,
                            Enter 2 to display the Courier Menu Options  ''')

        if user_input == '0':
            save_products()
            couriers.save_couriers()
            break
        elif user_input == '1':
            Display_Product_Menu()
            
        elif user_input == '2':
            couriers.Display_Couriers_Menu()
           
main()







