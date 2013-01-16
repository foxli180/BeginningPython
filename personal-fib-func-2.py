class Fibs:
    def __init__(self,stopIter = 10000):
        self.a = 0
        self.b = 1
        self.stopIter = stopIter

    def __next__(self):
        self.a ,self.b = self.b, self.a+self.b
        if self.a > self.stopIter: raise StopIteration
        return self.a

    def __iter__(self):
        return self



class Test:
    def __init__(self):
        self.a = 0

    def __next__(self):
        self.a += 1
        if self.a > 100: raise StopIteration
        return self.a

    def __iter__(self):
        return self


def test():
    fib = [0]
    fibs = Fibs()

   # for f in fibs:
   #     if f > 1000000:
   #         break
   #     fib += [f]

    print (list(fibs))

    t = Test()
    print(list(t))

if __name__ == '__main__':test()
