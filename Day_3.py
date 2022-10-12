# From 50 days of Python Challenge book


def register_check(dictionary):
    in_school = []
    for key in dictionary:
        if dictionary.get(key) == 'yes':
            in_school.append(key)
    return len(in_school)


def lowercase(names):
    lowercase_names = []
    for name in names:
        if name.islower() is True:
            lowercase_names.append(name)
    return tuple(sorted(lowercase_names, reverse=True))


# print(register_check({'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'no'}))
# print(lowercase(["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]))
