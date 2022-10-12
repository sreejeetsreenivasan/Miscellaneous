# From 50 days of Python Challenge book
import time


def inter_section(list_1, list_2):
    intersection = []
    for item in list_1:
        if item in list_2:
            intersection.append(item)
    return tuple(intersection)


def set_or_list():
    a = range(10000000)
    x = set(a)
    y = list(a)
    time_set, time_list = None, None
    start_time_set = time.time()
    for number in x:
        if number == 9999999:
            time_set = time.time() - start_time_set
    start_time_list = time.time()
    for number in y:
        if number == 9999999:
            time_list = time.time() - start_time_list
    if time_set < time_list:
        return f'Set was faster, time taken: {time_set} seconds'
    else:
        return f'List was faster, time taken: {time_list} seconds'


# print(inter_section([20, 30, 60, 65, 75, 80, 85], [ 42, 30, 80, 65, 68, 88, 95]))
# print(set_or_list())
