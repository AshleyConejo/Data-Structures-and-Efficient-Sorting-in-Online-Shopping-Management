product_file = open("product_data.txt","‘w+")

class Product:
    def __init__(self, pd_ID, pd_Name, pd_Price, pd_Category):
        self.pd_ID = pd_ID
        self.pd_Name = pd_Name
        self.pd_Name = pd_Price
        self.pd_Category = pd_Category

    def write_product_file(self,product_file):
        product_file = open("product_data.txt","‘w+")
        product_file.writelines(f"{self.pd_ID}{self.pd_Name}{self.pd_Price}{self.pd_Category}")
        return product_file 