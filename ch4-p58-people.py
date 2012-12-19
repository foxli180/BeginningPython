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
if request == 'p': key= 'phone'
if request == 'a': key= 'addre'

if name in people:
    print "%s's %s is %s." % (name,lables[key],people[name][key])
