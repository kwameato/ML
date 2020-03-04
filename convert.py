class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        ''' this is an instance of a class '''
        print(self.name.title() + ' is now sitting')

    def rollOver(self):
        print(self.name.title() + ' rolled over')



myDog = Dog('Willie',6)
yourDog = Dog('Lucie', 7)

print(f"my dog's name is {myDog.name.title()} ")

print(f"my dog's age is {str(myDog.age)} ")

print(f"your dog's name is {yourDog.name}, age is {str(yourDog.age)} ")
yourDog.sit()
yourDog.rollOver()
