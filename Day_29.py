# From 50 days of Python Challenge book


def middle_figure(a, b):
    new_string = (a + b).replace(' ', '')
    if len(new_string) % 2 != 0:
        return new_string[len(new_string) // 2]
    else:
        return new_string[int((len(new_string) / 2) - 1)]


# print(middle_figure('make love', 'not wars'))
