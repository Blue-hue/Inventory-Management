from product import Product
from logger import Logger

class Store:
    def __init__(self):
        self.inventory = {}
        self.log = Logger()

    def add_stock(self, product_id, stock):
        if product_id in self.inventory:
            item = self.inventory[product_id]
            item.add_stock(stock)
        else:
            print("Product not found in inventory!\nPlease add necessary details")
            name = input("Enter name of product: ")
            cost = float(input("Enter cost of product: "))
            item = Product(name, stock, cost, product_id)
            self.inventory[product_id] = item

    def display_stock(self):
        for item in self.inventory.values():
            item.print_details()
            print()

    def purchase_product(self, product_id, stock):
        if product_id not in self.inventory:
            print("Product not found!")
            return

        item = self.inventory[product_id]
        if item.make_purchase(stock):
            self.log.write_data(product_id, stock)

if __name__ == "__main__":
    manager = Store()
    option = 1
    while 1 <= option <= 4:
        print("INVENTORY MANAGEMENT SYSTEM")
        print("1. Add Stock")
        print("2. View Current Inventory")
        print("3. Make Purchase")
        print("4. View Purchase History")
        option = int(input("Enter option: "))

        if option == 1:
            product_id = int(input("Enter product ID: "))
            stock = int(input("Enter stock to add: "))
            manager.add_stock(product_id, stock)
        elif option == 2:
            print("STORE INVENTORY")
            manager.display_stock()
        elif option == 3:
            product_id = int(input("Enter product ID: "))
            stock = int(input("Enter stock to buy: "))
            manager.purchase_product(product_id, stock)
        elif option == 4:
            print("PURCHASE HISTORY")
            manager.log.read_data()
        print()
