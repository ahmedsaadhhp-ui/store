from Products import Customer

class VIPCustomer(Customer):
    def __init__(self, name,discount):
        super().__init__(name)
        self.discount=discount
        