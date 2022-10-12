# From 50 days of Python Challenge book


def same_in_reverse(word):
    for i in range(len(word)):
        if word[len(word) - i-1] == word[i]:
            continue
        else:
            return False
    return True


def your_age():
    names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
    name = str(input("Enter your name: "))
    while True:
        try:
            if name.lower() not in names_age:
                age = int(input("Enter your age: "))
                names_age[name.lower()] = age
                return f'Hi {name}, you are {age} years old'
            else:
                return f'Hi {name}, you are {names_age[name]} years old'
        except ValueError:
            print("Enter a valid age")


# print(same_in_reverse('dad'))
# print(your_age())
