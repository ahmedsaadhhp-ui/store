"# project store"


🛒 Simple Store Project
A small training project written in Python that demonstrates the principles
 of object-oriented programming (OOP) through the design of a simple online store.
 The project is divided into files to facilitate code organization and
  illustrate basic concepts such as inheritance,
  packaging, properties, and magic functions.
  
⚙️ Basic Components
Product: Represents the product (name, price, available quantity).
Customer: Represents the customer (name, shopping cart).
VIPCustomer (inherited from Customer): A special customer who receives a discount.
Store: Represents the store (product list + customers).
Order Functions: A set of functions for handling logic (adding a product, registering a customer, adding a cart, calculating the total).
📂 Project Structure
store_project/
│
├── Product.py # Define the Product class
├── Customer.py # Define the Customer class
├── Store.py # Define the Store class
├── Order.py # Logic functions (add products, calculate totals, etc.)
├── Main_Store.py # Main runtime file
└── README.doc # Project description

🚀 How to Run
1. Make sure you have Python installed (preferably 3.10 or later).
2. Copy the project to a folder.
3. Run the main file:
python Main_Store.py
🧪 Example of usage
from Store import Store
from Product import Product
from Customer import Customer, VIPCustomer
from Order import add_product, register_customer, add_to_cart, calculate_total

store = Store()
product1 = Product('Laptop', 500, 10)
product2 = Product('Mouse', 20, 50)

customer1 = VIPCustomer('Ahmed', 10) # 10% discount

add_product(store, product1)
add_product(store, product2)
register_customer(store, customer1)

add_to_cart(customer1, product1, 1)
add_to_cart(customer1, product2, 2)

print(customer1) # Customer: Ahmed, Cart items: 2
print(store) # Store has 1 product and 1 customer.
print(f'Total: ${calculate_total(customer1)}')
🎯 Learning Objectives
Understand classes and objects.
Apply encapsulation using properties.
Experiment with inheritance via VIPCustomer.
Use magic functions (such as __str__) to display objects in an organized manner.
Organize the code across multiple files, like real projects.
📝 Notes
This project is for training and not a real store.
It can be developed later to include:
- Multiple orders.
- A database to store products and customers.
- A graphical or web interface using Django or Flask.
