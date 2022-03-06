l = 10 #Global

def function1(n):
    # l = 5 #local
    global l
    l = l + 40
    m = 4 #Local
    print(l,m)
    print(n,"I have printed")

function1("this i me")
# print(m)

""""
def Tango():
    x = 20
    def rahul():
        global x
        x = 88
    print("before",x)
    rahul()
    print("after",x)

Tango()

"""
