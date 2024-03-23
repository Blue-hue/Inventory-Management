from product import Product
from logger import Logger

class Store:
    default_inventory = {
    101: {"name": "Milk", "stock": 50, "cost": 2.99},
    102: {"name": "Bread", "stock": 40, "cost": 1.99},
    103: {"name": "Eggs", "stock": 30, "cost": 3.49},
    104: {"name": "Apples", "stock": 35, "cost": 0.79},
    105: {"name": "Rice", "stock": 60, "cost": 4.99},
    
    201: {"name": "LEGO Set", "stock": 20, "cost": 29.99},
    202: {"name": "Barbie Doll", "stock": 25, "cost": 19.99},
    203: {"name": "Hot Wheels Cars", "stock": 30, "cost": 12.99},
    204: {"name": "Nerf Gun", "stock": 15, "cost": 24.99},
    205: {"name": "Board Game", "stock": 35, "cost": 17.99},
    
    301: {"name": "Smartphone", "stock": 50, "cost": 599.99},
    302: {"name": "Laptop", "stock": 40, "cost": 899.99},
    303: {"name": "TV", "stock": 30, "cost": 699.99},
    304: {"name": "Headphones", "stock": 45, "cost": 129.99},
    305: {"name": "Tablet", "stock": 55, "cost": 349.99},
    
    401: {"name": "T-Shirt", "stock": 60, "cost": 9.99},
    402: {"name": "Jeans", "stock": 50, "cost": 24.99},
    403: {"name": "Sneakers", "stock": 40, "cost": 39.99},
    404: {"name": "Dress", "stock": 35, "cost": 29.99},
    405: {"name": "Jacket", "stock": 20, "cost": 49.99},
    
    501: {"name": "Cereal", "stock": 45, "cost": 3.49},
    502: {"name": "Frozen Pizza", "stock": 55, "cost": 5.99},
    503: {"name": "Granola Bars", "stock": 40, "cost": 2.99},
    504: {"name": "Canned Soup", "stock": 30, "cost": 1.99},
    505: {"name": "Fresh Vegetables", "stock": 35, "cost": 4.99},
    
    601: {"name": "Toothpaste", "stock": 50, "cost": 2.49},
    602: {"name": "Shampoo", "stock": 45, "cost": 4.99},
    603: {"name": "Toilet Paper", "stock": 60, "cost": 6.99},
    604: {"name": "Laundry Detergent", "stock": 55, "cost": 8.99},
    605: {"name": "Hand Soap", "stock": 50, "cost": 3.99}
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
