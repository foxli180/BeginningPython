#-*-coding:utf-8-*-

def flatten (nested):
     for sublist in nested:
          for element in sublist:
               yield element



nested  = [[1,3],[3,4],[5]]

for num in flatten(nested):
     print (num)

def flattenx(nested):
     try:
          for sublist in nested:
               for element in flattenx(sublist):
                    yield element
     except TypeError:
          yield nested

nestedx  = [[1,3],[3,[2,1],4],[5]]
nestedy  = [1,2,3,4,5]
aaa = 'Helloword'
for num in flattenx(nestedy):
     print (num)
