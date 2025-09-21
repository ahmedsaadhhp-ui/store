class Product:
    def __init__(self,name,price,stock):
        self.__name=name
        self.__price=price
        self.__stock=stock
    
    
    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price
    @property
    def stock(self):
        return self.__stock
    
    
    def reduce_stock(self,quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
            return True
        
        return False
    def __str__(self):
        return f"{self.__name} - $ {self.__price} (stock : {self.__stock})"
    
class Customer:
    def __init__(self,name):
        self.name=name
        self.cart=[]
        
class Store:
    def __init__(self):
        self.products=[]
        self.customers=[]
        

        