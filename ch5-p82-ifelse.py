#-*-coding:utf-8-*-
from math import sqrt

for n in xrange (99,81,-1):#99递减到81,但是不包含81
    root =sqrt(n)
    if root == int(root):
        print n
        break
else: #在循环中增加的else 语句,仅在没有执行break 的时候执行
    print 'no found'

print 'yamdie' #这个print 无论是否执行break 都会被执行 