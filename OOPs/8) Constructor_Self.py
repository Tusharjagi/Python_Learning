
class Computer:

    def __init__(self):
        self.name =" Tushar"
        self.age = 23

    def update(self):
        self.age = 30


C1 = Computer()
C2 = Computer()

C1.name = "Tango"
C1.age = 4

if C1 == C2:
    print("They are same")
    

C1.update()

print(C1.name)
print(C1.age)

