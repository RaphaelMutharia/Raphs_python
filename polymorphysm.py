#parent class
class Animal:
    def __init__(self):
        pass
    def speak(self):
        print("I am an animal")

#child class
class dog(Animal):
    def __init__(self):
        pass
    def speak(self):
        print("I am a dog and I bark")

#the second child class
class cat(Animal):
    def __init__(self):
        pass

    def speak(self):
        print("I am a cat and i meow")

#creating instances
dog1=dog()
dog1.speak()

cat1=cat()
cat1.speak()

