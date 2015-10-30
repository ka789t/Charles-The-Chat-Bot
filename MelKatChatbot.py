
import random

def start_conversation():
    name=raw_input("What's your name? ")
    print(name+", it is a pleasure to meet you.")
    feeling=raw_input("How are you feeling? ")
    if feeling in ["sad","mad","bad"]:
        print("I am sorry to hear that.")
    else:
        print("Nice.")

        
def give_question():
    lst = [['What is your favorite animal?','That is a great one.'],
        ['What is your favorite color?','That is my favorite too!'],
        ['What is your favorite subject in school?','I do not like that one.'],
        ['What is your favorite type of music?','Mine too!'],
        ['If you could be any mythical creature, what would you be?','I would want to be a dragon!'],
        ['What is your favorite movie?','I wish I could watch movies...']]
    selection = random.choice(lst)
    print selection

def good_bye():
    print("It was nice talking, but I am going to go now. Bye!") 

def test_give_question():
    for n in range(18):
       give_question()

test_give_question()
    
