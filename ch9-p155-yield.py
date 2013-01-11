#-*-coding:utf-8-*-

def flatten(nested):
     try:
          try: nested+''
          except TypeError : pass
          else: raise TypeError
          for sublist in nested:
               for element in flatten(sublist):
                    yield element
     except TypeError:
          yield nested

nested = [[1,2],[3,[2,1],4],[5]]
nested1 = 'strings'
for num in flatten(nested):
     print (num)
