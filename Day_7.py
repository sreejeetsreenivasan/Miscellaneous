# From 50 days of Python Challenge book


def string_range(number):
    num_range = []
    for i in range(number):
        num_range.append(str(i))
    return '.'.join(num_range)


def begin_with_s(names):
    s_names = {}
    for name in names:
        if name.lower()[0] == 's':
            s_names[name] = names.count(name)
    return s_names


# print(string_range(6))
# print(begin_with_s(["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]))
