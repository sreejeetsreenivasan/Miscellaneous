# From 50 days of Python Challenge book


def longest_word(words):
    dict_of_words = {}
    for word in words:
        dict_of_words[word] = len(word)
    largest_value = max(dict_of_words.values())
    longest_words = [largest_value]
    for key, value in dict_of_words.items():
        if value == largest_value:
            longest_words.append(key)
    return longest_words


def create_user():
    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    password = str(input("Create a password: "))
    user_dict = {'name': name, 'age': age, 'password': password}
    print("User saved. Please login")
    while True:
        username = str(input("Enter your username: "))
        ent_password = str(input("Enter your password: "))
        if username == user_dict['name'] and ent_password == user_dict['password']:
            return "Logged in successfully"
        else:
            print("Wrong password or user name. Please try again")


# print(longest_word(['Java', 'JavaScript', 'Python']))
# print(create_user())
