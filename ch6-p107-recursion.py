#-*-coding:utf-8-*-

def factorial(n):
     if n == 1:
          return 1
     else:
          return n*factorial(n-1)


print (factorial(5))

def power (x,n):
     if n == 0:
          return 1
     else:
          return x*power(x,n-1)


print (power(3,2))
