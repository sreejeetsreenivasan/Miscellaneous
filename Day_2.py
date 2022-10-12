# From 50 days of Python Challenge book

def convert_add(strings):
    integers = []
    for element in strings:
        integers.append(int(element))
    return sum(integers)


def check_duplicates(strings):
    new_list = []
    duplicates = []
    for element in strings:
        if len(new_list) == 0:
            new_list.append(element)
        else:
            if element in new_list:
                duplicates.append(element)
            else:
                new_list.append(element)
    if len(new_list) < len(strings):
        return duplicates
    else:
        return 'No Duplicates'


# print(convert_add(['1', '3', '5']))
# print(check_duplicates(['apple', 'orange', 'banana', 'apple']))
# print(check_duplicates(['Yoda', 'Moses', 'Joshua', 'Mark']))
