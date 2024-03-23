from product import Product
from logger import Logger

class Store:
    default_inventory = {
    101: Product("Milk", 50, 2.99, 101),
    102: Product("Bread", 40, 1.99, 102),
    103: Product("Eggs", 30, 3.49, 103),
    104: Product("Apples", 35, 0.79, 104),
    105: Product("Rice", 60, 4.99, 105),

    301: Product("Smartphone", 50, 599.99, 301),
    302: Product("Laptop", 40, 899.99, 302),
    303: Product("TV", 30, 699.99, 303),
    304: Product("Headphones", 45, 129.99, 304),
    305: Product("Tablet", 55, 349.99, 305)
}
    def __init__(self):
        self.inventory = self.default_inventory.copy()
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