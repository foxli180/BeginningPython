#-*-coding:utf-8-*- #中文

#会打印出 ''' ''' 内的所有格式,\n 和\t
print ('''this is a
    very long
 long
string''')

print ("""this is a
    very long
  long
string""")

#其实这里转义了  \n
print ("Hello, \
Fox")

#如果 path = 'C:\nowhere'如何打印path

path = 'C:\nowhere'
print (path) #这里会打出2行 \n

#方法一 转义
path = 'C:\\nowhere'
print (path) 

#方法二  r 原始字符串标示
path = r'C:\nowhere'
print (path) #这里会打出2行 \n


#r的用法
print (r'Let\'s go!') #会输出 Let\'s go!