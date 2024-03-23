class Product:
    def __init__(self, name, stock, cost, id):
        self.id = id
        self.name = name
        self.stock = stock
        self.cost = cost

    def print_details(self):
        print("Product ID:", self.id)
        print("Name:", self.name)
        print("Stock:", self.stock)
        print("Cost:", self.cost)

    def add_stock(self, extra_stock):
        self.stock += extra_stock

    def make_purchase(self, bought):
        if bought > self.stock:
            print("Not sufficient stock")
            return False
        else:
            print("Transaction successful")
            self.stock -= bought
            return True
