#-*-coding:utf-8-*-
class Fibs:
     def __init__(self):
          self.a = 0
          self.b = 1
     def __next__(self):
          self.a,self.b = self.b, self.b+self.a
          return self.a
     def __iter__(self):
          return self

aa = []
fibs = Fibs()
for f in fibs:    
     if f > 100000:
          #print (f)          
          break
     aa=aa+[f]
print (aa)
     

class TestInterator:
     value  = 0
     def __next__(self):
          self.value += 1
          if self.value > 10:raise StopIteration
          return self.value
     def __iter__(self):
          return self

ti = TestInterator()
print (list(ti))
