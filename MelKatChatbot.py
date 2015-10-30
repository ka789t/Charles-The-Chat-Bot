def pretty_print(txt):
    print '*' * (len(txt)+4)
    print '* '+text+' *'
    print '*' * (len(txt)+4)
    

def tell_joke ():
    lst=['How do you drown a hipster? Throw him into the mainstream.'
         ['Why did the computer get cold?','Because he forgot to close windows!!!'],
         ['Why did the plane crash?','Because the pilot was a loaf of bread.'],
         ['Why was the boy sad?','Because he had a frog stapled to his face.']]
    selection= random.coice(lst)
    print selection

def test_tell_function():
    for n in range(10):
        tell_joke()

pretty_print('Welcome to Chatbot!')

    

    
