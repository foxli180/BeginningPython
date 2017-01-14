
def conflict(nextX,state):
     nextY = len(state)
     for i in range(nextY):
          if abs(state[i]-nextX) in (0,nextY-i):
               return True
     return False

def queens(num,state=[]):
     for pos in range(num):
          if not conflict(pos,state):
               if len(state) == num-1:
                    yield [pos]
               else:
                    for result in queens(num,state+[pos]):
                         yield result+[pos]
 
if __name__ =='__main__':
	print ("3 queens:", list(queens(3)))
	print ("4 queens:", list(queens(4)))
	print ("8 queens:", len(list(queens(8))))
