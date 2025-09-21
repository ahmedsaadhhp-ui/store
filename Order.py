from Products import Store,Product

def add_product(store,product):
    store.products.append(product)
    
def register_customer(store,customer):
    store.customers.append(customer)
    
def add_to_cart(customer,product,quantity):
    if product.reduce_stock(quantity):
        customer.cart.append((product,quantity))
    
    else:
        print(f"{product.name} is not found")
        

def calculate_total(customer):
    total=sum(p.price*q for p,q in customer.cart )
    if hasattr(customer,'discount'):
        total *= (1-customer.discount/100)
        return  total
    
    