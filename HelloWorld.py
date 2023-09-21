# create hello world but in `oop way` so it gets current terminal user as a name
# and print hello {name} in terminal
# explain why it's 'oop way' and why it's not

import getpass 

class HelloWorld:
    def __init__(self):
        self.name = getpass.getuser()
    
    def say_hello(self):
        print(f'Hello {self.name}!')

say = HelloWorld()
say.say_hello()

