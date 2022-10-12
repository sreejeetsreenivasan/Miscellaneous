# From 50 days of Python Challenge book
from textblob import TextBlob
from datetime import datetime
from playsound import playsound


def spelling_checker():
    while True:
        word = str(input("Enter a word: "))
        w = TextBlob(word)
        if w.correct() != word:
            correction = str(input(f"Did you mean to type: '{w.correct()}'? Please say yes or no: "))
            if correction.lower() == 'yes':
                return f'Correct Spelling : {w.correct()}'
            else:
                continue
        else:
            return f'Correct Spelling: {word}'


def alarm():
    time = str(input("Enter the time you want your alarm to go off (ex. 12:20): "))
    while True:
        # print(f"The alarm will go off at {time}")
        current_time = datetime.now().strftime("%H:%M")
        l_time = time.split()
        if current_time == l_time[0]:
            playsound("/Users/ssreenivasan/Desktop/இயற்பா/நான்முகன் திருவந்தாதி.mp3")


# print(spelling_checker())
# alarm()
