# From 50 days of Python Challenge book


def add_hash(string):
    words = string.split()
    return '#'.join(words)


def add_underscore(string):
    words = string.split('#')
    return '_'.join(words)


def remove_underscore(string):
    words = string.split('_')
    return ' '.join(words)


print(remove_underscore(add_underscore(add_hash('Python'))))
