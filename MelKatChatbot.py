import random

def pretty_print(txt):
    print '*' * (len(txt)+4)
    print '* '+txt+' *'
    print '*' * (len(txt)+4)
    

def tell_joke (asked_jokes,n):
    lst=[['How do you drown a hipster? Throw him into the mainstream.'],
         ['Why did the computer get cold?','Because he forgot to close windows!!!'],
         ['Why did the plane crash?','Because the pilot was a loaf of bread.'],
         ['Why was the boy sad?','Because he had a frog stapled to his face.']]
    selection = random.choice(lst)
    asked_jokes=random.choice
    for n in asked_jokes:
        lst.remove(n)
    print selection
    return selection

def test_tell_joke():
    asked_jokes = []
    for n in range(10):
        asked_jokes.append(tell_joke(asked_jokes))

        #def main ():
        #start_conversation()
        #asked_jokes = []
        #while 1:
        #asked_jokes.append(tell_joke(asked_jokes))
        # ...
        
pretty_print('Welcome to Chatbot!')
test_tell_joke()  

    
