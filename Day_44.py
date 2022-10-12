# From 50 days of Python Challenge book
import csv


def save_emails():
    file = open("emails.csv", "w")
    list_of_emails = []
    while True:
        email = str(input("Enter an email; type 'done' when finished: "))
        if email.lower() == 'done':
            break
        list_of_emails.append([email])
    csv.writer(file).writerows(list_of_emails)
    file.close()


def open_emails():
    file = open("emails.csv", "r")
    for email in csv.reader(file):
        print(email)
    file.close()


# save_emails()
# open_emails()
