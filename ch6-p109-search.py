#-*-coding:utf-8-*-

#1. 二元查找,从一个列表中查找关键字的

def search(sequnce, number, lower=0, upper=None):
     if upper == None :upper = len(sequnce)-1
     sequnce.sort()
     if lower == upper:
          assert number == sequnce[upper]
          return upper
     else:
          middle = (lower+upper)//2
          if number>sequnce[middle]:
               return search (sequnce,number,middle+1,upper)
          else:
               return search (sequnce,number,lower,middle)

seq = [1,33,11,45,37,99,25]
print (search (seq,25))
