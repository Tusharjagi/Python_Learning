
class Computer:

    def __init__(self):
        self.name ="Tushar"
        self.age = 23

    def update(self):
        self.age = 30

    def compare(self, C2):
        if self.age == C2.age:
            return True
        else:
            print("Not same")




C1 = Computer()
C1.age = 40
C2 = Computer()

if C1.compare(C2):
    print("They are same")

print(C1.name)
print(C1.age)

