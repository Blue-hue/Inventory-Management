class Logger:
    def __init__(self, address="history.txt"):
        self.address = address

    def read_data(self):
        try:
            with open(self.address, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("No purchase history found.")

    def write_data(self, product_id, stock):
        try:
            with open(self.address, 'a') as file:
                file.write(f"ProductID: {product_id} Stock purchased: {stock}\n")
        except Exception as e:
            print(f"An error occurred: {e}")
