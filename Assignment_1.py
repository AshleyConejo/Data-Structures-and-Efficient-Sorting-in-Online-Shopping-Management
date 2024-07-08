import time
arrayempty = []
class Product_info:
    def __init__(self):
        self
    def products(self,pd_ID,pd_Name,pd_Price,pd_Category):
        self.pd_ID = pd_ID
        self.pd_Name = pd_Name
        self.pd_Price = pd_Price
        self.pd_Category = pd_Category 
    
    def write_product_file(self,product_file):
        
        product_file = open("product_data.txt","‘w+")
        product_file.writelines(f"{self.pd_ID},{self.pd_Name},{self.pd_Price},{self.pd_Category}")
        return product_file 
     
    def insert_product(self):
        product_file = open("product_data.txt", "a+") 
        print("product to insert")

        insert_ID = input("ID: ")
        insert_Name = input("Name:")
        insert_Price = input("Price: ")
        insert_Category = input("Category ")

        insert_statement = f"{insert_ID},{insert_Name},{insert_Price},{insert_Category}\n"

        arrayempty.insert(0,insert_statement)
        product_file.writelines(arrayempty)

        print(f"You added this product into the file: ",{insert_statement})
               
    def update_product(self):
        product_file = open("product_data.txt","r+")
        product_to_update = input("product ID to update: ")
        reading_file = product_file.read()
        
        if product_to_update in reading_file:
            update_ID = input("ID: ")
            update_Name = input("Name:")
            update_Price = input("Price: ")
            update_Category = input("Category: ")
            arrayempty = [f"{update_ID}, {update_Name}, {update_Price}, {update_Category}\n"]
            product_file.writelines(arrayempty)
            
        else:
            print("Product was not found in the file.")

    def delete_product(self):
        product_file = open("product_data.txt","r+")
        reading_file = product_file.read()
        
        product_to_delete = input("product to delete: ")
        
        
        if product_to_delete in reading_file:
            print("Please enter the information from the product to delete.")
            deleted_ID = input("ID: ")
            deleted_Name = input("Name:")
            deleted_Price = input("Price: ")
            deleted_Category = input("Category: ")
        
            
            arrayempty= f"{deleted_ID},{deleted_Name},{deleted_Price},{deleted_Category}\n"
            reading_file = reading_file.replace(arrayempty, '')

            product_file.seek(0)
            product_file.truncate()
            product_file.write(reading_file)

           
            print("Prroduct has been removed.")  

            
        else:
            print("Product was not found in the file.")

    def search_product(self):
        product_file = open("product_data.txt","r+")
        reading_file = product_file.read()
        
        product_to_search = input("product to search'eg: ID or Name : ")
        
        if product_to_search in reading_file:
            reading_file.index(product_to_search)
            print(f"Element Found: {product_to_search} at index.")
          
        else:
            print(f"Element NOT Found: {product_to_search} at index.")

    def sort_products_ASC(self):  
        
        product_file = open("product_data.txt","r")
        reading_file = product_file.readlines()

        arrayempty = []

        for arraylisted in reading_file:
            arraylisted = arraylisted.strip().split(',')
            arraylisted[2] = float(arraylisted[2])
            arrayempty.append(arraylisted)

            lenghtarray = len(arrayempty)
            start_timer = round(time.time()*10)
            
            for higher_cost in range(lenghtarray):
                for lower_cost in range(0,lenghtarray - higher_cost -1):
                    if arrayempty[lower_cost][2] > arrayempty[lower_cost + 1][2]:
                        arrayempty[lower_cost], arrayempty[lower_cost + 1] = arrayempty[lower_cost + 1 ], arrayempty[lower_cost]
            
        for higher_cost in range(len(arrayempty)):
            arrayempty[higher_cost][2] = str(arrayempty[higher_cost][2])
        product_file = open("product_data.txt", "w")

        for product_in_list in arrayempty:
            product_file.write(','.join(product_in_list) + '\n')
            stop_time = start_timer - time.time() 
        print("Your Products Have Been Sorted in Acending Order")
        print("Bubble Sort - Best: O(n), Average: O(n^2), Worst: O(n^2)")
        print("It took ", stop_time, "miliseconds")

    def sort_products_DESC(self):  
        
        product_file = open("product_data.txt","r")
        reading_file = product_file.readlines()

        arrayempty = []

        for arraylisted in reading_file:
            arraylisted = arraylisted.strip().split(',')
            arraylisted[2] = float(arraylisted[2])
            arrayempty.append(arraylisted)

            lenghtarray = len(arrayempty)
            start_timer = round(time.time()*10)
            for higher_cost in range(lenghtarray):
                for lower_cost in range(0,lenghtarray - higher_cost -1):
                    if arrayempty[lower_cost][2] < arrayempty[lower_cost + 1][2]:
                        
                        arrayempty[lower_cost], arrayempty[lower_cost + 1] = arrayempty[lower_cost + 1 ], arrayempty[lower_cost]
            
        for higher_cost in range(len(arrayempty)):
            arrayempty[higher_cost][2] = str(arrayempty[higher_cost][2])
        product_file = open("product_data.txt", "w")

        for product_in_list in arrayempty:
            product_file.write(','.join(product_in_list) + '\n')
            stop_time = start_timer - time.time() 

        print("Your Products Have Been Sorted in Descending order ")
        print("Bubble Sort - Best: O(n), Average: O(n^2), Worst: O(n^2)")
        print("It took ", stop_time, "miliseconds")
    
          
pd_list= Product_info()
 
while True:
    print("Available Options")
    print("\t1) Insert")
    print("\t2) Update")
    print("\t3) Delete")
    print("\t4) Search")
    print("\t5) Sort Ascending")
    print("\t6) Sort Descending")
    user_option = input("Chose one option using numbers EX:1,2,3...:  ")  

    if user_option == '1':
        pd_list.insert_product()
        
    elif user_option == '2':
        pd_list.update_product()

    elif user_option == '3': 
        pd_list.delete_product() 

    elif user_option == '4':
         pd_list.search_product()

    elif user_option == '5':
        pd_list.sort_products_ASC()
    
    elif user_option == '6':
        pd_list.sort_products_DESC()
        
        
    else:
        print("Invalid choice. Please try again.")
        break


        