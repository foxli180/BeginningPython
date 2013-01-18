class factorial():
     def __init__(self,n):
          self.a = 1
          self.max  = n
          self.b = self.a
     #def __next__(self):
     #     self.a, self.b = self.a+1, self.a *(self.a+1)
     #     if self.a >= self.max: raise StopIteration
     #     return self.b

     def __next__(self):          
                           
          if self.a >= self.max:raise StopIteration
          self.a = self.a+1
          self.b = self.b*self.a
          return self.b

     def __iter__(self):
          return self


class power():
     def __init__(self,x,n):
          self.x = x
          self.n = n
          self.a = 1
          self.b = x

     def __next__(self):          
          if self.a >= self.n:raise StopIteration
          self.a = self.a +1 
          self.b = self.b * self.x          
          return self.b
     def __iter__ (self):
          return self

     
     

def main():
     fac = factorial(5)
     print (list(fac)[-1])
     powers = power(2,2)
     print (list(powers))

if __name__ =='__main__':main()          
