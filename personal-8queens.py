def conflict(nextX,state):
    nextY = len(state)
    for i in range(nextY):
        if abs(nextX - state[i]) in (0, nextY-i):
            return True
    return False


def queens(num,state=[]):
    for pos in range(num):
        if not conflict(pos,state):
            if len(state) == num -1:
                yield [pos]
            else:
                for result in queens(num,state+[pos]):
                    yield result+[pos]


def test():
    print (list(queens(4)))
    print (list(queens(8)))


if __name__ == '__main__':test()
