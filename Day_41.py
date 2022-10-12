# From 50 days of Python Challenge book


def words_with_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = string.split()
    words_w_vowels = []
    for word in words:
        i = 0
        while i < len(word):
            if word[i].lower() in vowels:
                words_w_vowels.append(word)
                break
            else:
                i += 1
    return words_w_vowels


class Car:
    def __init__(self, model, color, year, transmission, electric):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric

    def print_cars(self):
        print(f'car_model = {self.model} \nColor = {self.color} \nYear = {self.year} \nTransmission = {self.transmission} '
              f'\nElectric = {self.electric}')


class Ford(Car):
    pass


class BMW(Car):
    pass


class Tesla(Car):
    pass


# print(words_with_vowels('You have no rhythm'))
bmw1 = BMW("x6", "silver", 2018, "Auto", False)
tesla1 = Tesla("S", 'beige', 2017, 'Auto', True)
ford1 = Ford("focus", 'white', 2020, 'Auto', False)

# ford1.print_cars()
