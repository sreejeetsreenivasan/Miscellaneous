# From 50 days of Python Challenge book


def search_binary(input_list, item):
    midpoint = int(len(input_list) / 2)
    print(input_list[:midpoint], input_list[midpoint:])
    index = 0
    while True:
        if item == input_list[midpoint]:
            return index + midpoint
        elif item in input_list[:midpoint]:
            input_list = input_list[:midpoint]
            midpoint = int(len(input_list) / 2)
        elif item in input_list[midpoint:]:
            input_list = input_list[midpoint:]
            index += midpoint
            midpoint = int(len(input_list) / 2)
        else:
            return f'{item} not in input list'


# print(search_binary([12, 34, 56, 78, 98, 22, 45, 13], 22))
