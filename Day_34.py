# From 50 days of Python Challenge book
import csv

file = open("just_digits.txt")
words = [word for sentence in file for word in sentence.split()]
csv_file = open("just_digits.csv", "r+")

# csv.writer(csv_file).writerow(words)


def just_digits():
    numbers = []
    for entry in csv.reader(csv_file):
        for element in entry:
            try:
                if type(int(element)) == int:
                    numbers.append(element)
            except ValueError:
                continue
    return numbers


# print(just_digits())
csv_file.close()
file.close()
