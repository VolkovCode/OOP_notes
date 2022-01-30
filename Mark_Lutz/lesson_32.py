def gen():
    x = range(3)
    yield x

i = gen()
print(next(i))