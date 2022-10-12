# From 50 days of Python Challenge book


def password_validator():
    print("A valid password contains at least 1 upper-case letter, 1 lower-case letter, and 1 number")
    while True:
        password = str(input("Enter a password: "))
        letters = [letter for letter in password]
        upper_case = False
        lower_case = False
        number = False
        for element in letters:
            if element.isupper() is True:
                upper_case = True
            elif element.islower() is True:
                lower_case = True
            try:
                if type(int(element)) is int:
                    number = True
            except ValueError:
                continue
        if upper_case and lower_case and number is True:
            return f'Password: {password}'
        else:
            if upper_case is False:
                print("The password must contain at least 1 upper-case letter")
            elif lower_case is False:
                print("The password must contain at least 1 lower-case letter")
            elif number is False:
                print("The password must contain at least 1 number")


def email_validator(emails):
    print("A valid email will contain 1 '@' sign and a '.com' suffix")
    valid_emails = []
    index = 0
    while index < len(emails):
        email = emails[index]
        if email.count('@') == 1:
            if email.index('@') != 0:
                if email[-4:] == '.com':
                    valid_emails.append(email)
        index += 1
    if len(valid_emails) != 0:
        return valid_emails
    else:
        return 'All emails are invalid'


# print(password_validator())
# print(email_validator(['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']))
