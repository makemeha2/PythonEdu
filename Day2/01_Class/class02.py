class Person:
    num_person = 0

    def __init__(self):
        self.name = "default name"
        Person.num_person += 1
    
    def print(self) :
        print("My name is {0}".format(self.name))

p1 = Person()
p1.name = "Soyoung"
p1.print()

p2 = Person()

print("instance Count is {0}".format(p1.num_person))
print("instance Count is {0}".format(p2.num_person))


Person.title = "new Title"
print(Person.title)
p1.title = "Modified Title"
print(p1.title)
print(p2.title)
