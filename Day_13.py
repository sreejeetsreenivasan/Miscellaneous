# From 50 days of Python Challenge book


def your_vat():
    while True:
        price = None
        vat = None
        try:
            price = float(input("Enter the price of the good: "))
            vat = float(input("Enter the value-added tax: "))
        except ValueError:
            print("Enter a valid price and/or VAT")
            continue
        else:
            break
    return f'Total cost: {price + (price * vat/100)}'


def python_snakes(number):
    for i in range(1, number):
        if i % 2 == 0:
            print(' ' + '.' * i)
        else:
            print('.' * i)


# print(your_vat())
# python_snakes(7)
