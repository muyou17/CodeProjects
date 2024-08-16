class dog:
    age = int()
    name = str()
    gender = str()
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender
    def print_dog(self):
        print(self.name + "'s " + "information:")
        print("Age:", self.age)
        print("Gender:", self.gender)
    def bark(self):
       print("Woof woof!")

dog1 = dog(2, "Mimi", "Female")
dog2 = dog(1, "Dough", "Male")
dog3 = dog(3, "Female", "Male")

dog3.print_dog()
dog1.print_dog()
dog2.bark()

print(dir(dog2))