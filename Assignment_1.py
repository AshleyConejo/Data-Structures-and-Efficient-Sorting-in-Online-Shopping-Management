product_file = open("product_data.txt","‘w+")

class Product:
    def __init__(self, pd_ID, pd_Name, pd_Price, pd_Category):
        self.pd_ID = pd_ID
        self.pd_Name = pd_Name
        self.pd_Name = pd_Price
        self.pd_Category = pd_Category

    def __repr__(self):
        