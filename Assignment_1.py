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

        print(f"You added this product into the file: ",{arrayempty})
               
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

    def partition(self, Products, Low, High):
        
        Pivot = Products[High]
        mean_price = Low -1 

        for price in range(Low,High):
            if Products[price] <= Pivot:
                mean_price = mean_price + 1
                (Products[mean_price], Products[price]) = (Products[price], Products[mean_price])

        Products[mean_price+1], Products[High] = Products[High], Products[mean_price+1]
        return mean_price + 1

    def quick_sort(self, Products , low=0, high=1000):
        product_file = open("product_data.txt","r+")
        reading_file = product_file.read()
        sorting_array = reading_file.strip().split(',')
        price = float(sorting_array [2])

        arrayempty = [price]

        if low < high:
            pi = self.partition(Products, low, high)
            self.quick_sort(Products, low, pi - 1)
            self.quick_sort(Products, pi + 1, high) 
            size = len(arrayempty)
            self.quick_sort(arrayempty, 0, size - 1)   
            self.quick_sort(arrayempty)
            print("Soeted Product List: ", arrayempty)
         
pd_list= Product_info()
 
while True:
    print("Available Options")
    print("\t1) Insert")
    print("\t2) Update")
    print("\t3) Delete")
    print("\t4) Search")
    print("\t5) Sort")
    user_option = input("Chose one option using numbers EX:1,2,3... ")  

    if user_option == '1':
        pd_list.insert_product()
        
    elif user_option == '2':
        pd_list.update_product()

    elif user_option == '3': 
        pd_list.delete_product() 

    elif user_option == '4':
         pd_list.search_product()

    elif user_option == '5':
        break
    else:
        print("Invalid choice. Please try again.")

        