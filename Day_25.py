# From 50 days of Python Challenge book


def all_the_same(argument):
    if type(argument) is str:
        words = argument.split()
        for word in words[1:]:
            if word != words[0]:
                return False
        return True
    elif type(argument) is list:
        for element in argument[1:]:
            if element != argument[0]:
                return False
        return True
    elif type(argument) is tuple:
        for x in argument[1:]:
            if x != argument[0]:
                return False
        return True
    else:
        print("Not defined; input must be of type string, list, or tuple")


def read_backwards(string):
    words = string.split()
    reverse_words = words[::-1]
    return ' '.join(reverse_words)


# print(all_the_same(['Mary', 'Mary', 'Mary']))
# print(read_backwards('the love is real'))
