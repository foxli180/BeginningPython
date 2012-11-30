#-*-coding:utf-8-*-   
#字符串

# 交互
name = raw_input ("what's yr name?")
print ('Hello ' + name +'!')
raw_input ('Press <Enter>!') # 防止还没来得及看结果,app 就退出了

# 转义
print ('Let\'s go!') #\' 对 ' 进行转义
print ("Let's go!")
print ("Let's say \"Hello\"!")
print ('Let\'s say \"Hello\"!')
#不使用转义的话,可以进行拼接
x = "Let's say "
y = '"Hello"!'
print (x+y)

print (1000L)

#repr 和 str
print (repr(1000L)) # repr 函数,将 1000L 处理为 string
print (str(1000L))  # 将1000L 转换为 str 类型

# str是类型, repr 是函数, repr 和``(反引号) 是一样的,但是不建议使用``(Python3 没有了),使用repr 易读些
temp = 43
print ('The temperature is: '+ str(temp))
print ('The temperature is: '+ repr(temp))
print ('The temperature is: '+ `temp`)


# input 和 raw_inpit 的区别

name1 = input ("name? ")#这里用户需要输入 "Fox"(包含引号),如果仅输入 Fox 则会报错,input 认为用户输入的是 Python 表达式
print ("Hello "+name1)

name2 = raw_input("name?")
print ("Hello "+ name2)