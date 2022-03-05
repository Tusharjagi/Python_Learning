def gen(n):
    for i in range(n):
        yield  i

ob1 = gen(10000000)
print(next(ob1))


