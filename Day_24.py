# From 50 days of Python Challenge book


def average_calories():
    calories_per_day = [float(x) for x in input("Enter your daily calorie consumption separated by a space: ").split()]
    return sum(calories_per_day) / len(calories_per_day)


def nested_lists(*lists):
    nested_list = [*lists]
    return nested_list


# print(average_calories())
# print(nested_lists([1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]))
