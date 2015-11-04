#Melanie did all of this
import random

def start_conversation():
    name=raw_input("What's your name? ")
    print(name+", it is a pleasure to meet you.")
    feeling=raw_input("How are you feeling? ")
    if feeling in ["sad","mad","bad"]:
        print("I am sorry to hear that.")
    else:
        print("Nice.")

        
def give_question(already_asked):
    '''give one question at a time. Don't ask a question in already_asked
    '''
    lst = [['What is your favorite animal?','That is a great one.'],
        ['What is your favorite color?','That is my favorite too!'],
        ['What is your favorite subject in school?','I do not like that one.'],
        ['What is your favorite type of music?','Mine too!'],
        ['If you could be any mythical creature, what would you be?','I would want to be a dragon!'],
        ['What is your favorite movie?','I wish I could watch movies...']]
    for n in already_asked:
        lst.remove(n)
    selection = random.choice(lst)
    print selection
    return selection
    
def good_bye():
    print("It was nice talking, but I am going to go now. Bye!") 

def test_give_question():
    already_asked = []
    for n in range(6):
        already_asked.append(give_question(already_asked))

def play_game():
    start_conversation()
    give_question(already_asked)
    good_bye()
