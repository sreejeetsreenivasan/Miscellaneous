# From 50 days of Python Challenge book


def flat_list(nested_list):
    for element in nested_list:
        if type(element) == list:
            for i in flat_list(element):
                yield i
        else:
            yield element


def your_salary():
    while True:
        name = None
        periods = None
        rate = None
        try:
            name = str(input("Enter teacher name: "))
            periods = int(input("Enter the number of periods taught in a month: "))
            rate = float(input("Enter rate per period: "))
        except ValueError:
            print("Enter a valid name, number of periods, or rate: ")
            continue
        else:
            break
    if periods > 100:
        gross_salary = (100 * rate) + (periods - 100) * 25
        return f'Teacher: {name} \nPeriods: {periods} \nGross Salary: ${gross_salary}'
    else:
        gross_salary = (periods * rate)
        return f'Teacher: {name} \nPeriods: {periods} \nGross Salary: ${gross_salary}'


# print(list(flat_list([[[2, 4], 5, 6], 8, 9])))
# print(your_salary())
