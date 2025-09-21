from Products import Store,Product
from Customer import VIPCustomer
from Order import add_product,register_customer,add_to_cart,calculate_total

store=Store()
product=Product("laptop",500,10)
print(f"the products is {product}")

product2=Product("mouse",20,50)
print(f"the products is {product2}")

customer1=VIPCustomer("ahmed",10)


add_product(store,product)
add_product(store,product2)
register_customer(store,customer1)


add_to_cart(customer1,product,1)
add_to_cart(customer1,product2,2)

print(f"Total for {customer1.name}.${calculate_total(customer1)}")


