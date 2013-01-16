class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        return self.a

    def __iter__(self):
        return self

def verifyfib(solution):

    for i in range(2,len(solution),1):
        if not solution[i] == solution[i-1]+solution[i-2]:
            return False
    return True
        


def main():
    fib = [0]
    fibs = Fibs()
    for f in fibs:
        if f > 10000000000000:
            break
        fib = fib + [f]

    print (fib)
    print (len(fib))
    print (verifyfib(fib))
    fib  = fib + [0]
    print (verifyfib(fib))
    

        


if __name__ == '__main__':main()

