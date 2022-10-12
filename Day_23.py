# From 50 days of Python Challenge book


def calculator():
    print("This is a simple calculator which can perform addition, subtraction, multiplication, and division")
    while True:
        try:
            operation = int(input("Enter the corresponding number for the operation you'd like to perform: "
                                  "1 - addition, 2 - subtraction, 3 - multiplication, 4 - division: "))
            if operation == 1:
                numbers = [float(x) for x in
                           input("Enter the numbers you'd like to add separated by a plus sign: ").split("+")]
                total = 0
                for number in numbers:
                    total += number
                return total
            elif operation == 2:
                numbers = [float(x) for x in
                           input("Enter the numbers you'd like to subtract separated by a minus sign: ").split("-")]
                total = numbers[0]
                for i in range(1, len(numbers)):
                    total -= numbers[i]
                return total
            elif operation == 3:
                numbers = [float(x) for x in
                           input("Enter the numbers you'd like to multiply separated by an asterisk: ").split("*")]
                total = 1
                for number in numbers:
                    total *= number
                return total
            elif operation == 4:
                numbers = [float(x) for x in
                           input("Enter the numbers you'd like to divide separated by a forward slash: ").split("/")]
                total = numbers[0]
                for i in range(1, len(numbers)):
                    total /= numbers[i]
                return total
        except ValueError:
            print("Enter a valid input for the given query")
            continue
        except ZeroDivisionError:
            print("Cannot perform division by zero; try again")
            continue


def multiply_words(string):
    words = string.split()
    length = 1
    for word in words:
        upper = False
        for letter in word:
            if letter.isupper() is True:
                upper = True
        if upper is False:
            length *= len(word)
    return length


# print(calculator())
# print(multiply_words('love live and laugh'))
