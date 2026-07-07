def get_product():
    product = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = int(input("Enter the price: "))
    return product , quantity , price

def calculate_bill(quantity,price):
    total = price * quantity
    return total

def print_bill(product,quantity,price,total):

    print("=====Grocery Bill=====")
    print("product: ",product)
    print("quantity: ",quantity)
    print("price: ",price)
    print("total price: ",total)

def main():
    product,quantity,price =get_product()
    total = calculate_bill(quantity,price)
    print_bill(product,quantity,price,total)

main()
