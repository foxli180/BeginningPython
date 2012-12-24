#-*-coding:utf-8-*-
'''
name = raw_input('~~~~~:') #这里输入 print 'Hello'
exec (name)                #执行的结果是 'Hello'
'''
#动态创建代码的风险:你永远不知道用户会输入什么,他们的输入或许会干扰你正常的代码
'''
from math import sqrt
exec "sqrt = 1"
print sqrt(4) #执行这里的时候会报错,因为sqrt=1 干扰了正常的命名空间
'''


#使用字典来控制潜在的风险
from math import sqrt
scope = {}
exec "sqrt = 1" in scope
print sqrt(4)
print scope['sqrt']