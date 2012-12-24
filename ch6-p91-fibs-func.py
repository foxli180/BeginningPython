#-*-coding:utf-8-*- 
def fibs(num): #计算多少个斐波那契数列
    result = [0,1]
    for i in xrange(num-2):
        result.append(result[-2]+result[-1]) #永远都是倒数第二加上倒数第一
    return result
 
num = raw_input('num:?')
print fibs(int(num)) 