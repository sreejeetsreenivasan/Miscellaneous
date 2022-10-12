# From 50 days of Python Challenge book


def repeated_name(names):
    count_dictionary = {}
    for name in names:
        if name not in count_dictionary:
            count_dictionary[name] = names.count(name)
    largest_value = max(count_dictionary.values())
    most_repeated_names = [key for key, value in count_dictionary.items() if value == largest_value]
    return f'The most repeated names are: {most_repeated_names}'


def sorted_names(names):
    first_names = []
    last_names = []
    dict_of_names = {}
    for name in names:
        first_names.append(name[:name.index(' ')])
        last_names.append(name[name.index(' ') + 1:])
    for i in range(len(names)):
        dict_of_names[last_names[i]] = first_names[i]
    sorted_list = sorted(last_names)
    final_list = []
    for last_name in sorted_list:
        last_name += ' ' + dict_of_names.get(last_name)
        final_list.append(last_name)
    return final_list


# print(repeated_name(["John", "Peter", "John", "Peter", "Jones", "Peter"]))
# print(sorted_names(['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown', 'Tom Cruise']))
