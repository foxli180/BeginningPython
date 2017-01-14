#-*-coding:utf-8-*- #Chinese character support
#定义字典 people ,里面每个元素都是字典,字典元素间需要使用 , 隔开
people = {
    'Alice':{
        'phone':'2312',
        'addre':'Foo Drive23'},
    'Beth':{
        'phone':'1234',
        'addre':'Bar street 42'},
    'Cecil':{
        'phone':'3121',
        'addre':'Baz avenue 90'},
    }
#将缩写还原
lables = {'phone':'phone number',
          'addre':'address'}
name = raw_input('Name: ') #这里区分大小写
request = raw_input('phone number(p) or address(a)?')

key = request #如果既不是p也不是a
if request == 'p': key= 'phone'
if request == 'a': key= 'addre'

person = people.get(name,{})#尝试获取 name 对应的 value ,找不到则返回空的字典 
lable = people.get(key,key) #尝试在lable里查找key ,查不到,则返回key
result = person.get(key,'not available') #尝试从person 里查找 key 对应的value, 查不到则返回'not...'

print "%s's %s is %s." % (name, lable, result) #这里使用name,而不判断 name 是否在phonebook里,提示更友好了一些
'''
if name in people:
    print "%s's %s is %s." % (name,lables[key],people[name][key])
'''