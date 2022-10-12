# From 50 days of Python Challenge book


def my_discount():
    price = float(input("Enter a price: "))
    discount = float(input("Enter a discount percentage: "))
    return price - (price * discount / 100)


def gender_of_student(student_genders):
    male = []
    female = []
    count = []
    for element in student_genders:
        if element.lower() == 'male':
            male.append(element)
        elif element.lower() == 'female':
            female.append(element)
    m_tuple = ('Male', len(male))
    f_tuple = ('Female', len(female))
    count.append(m_tuple)
    count.append(f_tuple)
    return count


# print(my_discount())
# print(gender_of_student(['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']))
