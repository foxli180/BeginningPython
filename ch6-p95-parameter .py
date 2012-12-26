#-*-coding:utf-8-*- #显示中文
#init and store does not return any value, since the data have the samecopy with mynames, so when we modify the 'data' , 'mynames' also changes it's value
#def init (x): x=x+1
#foo = 10
#init (foo)
#这时foo是10, x是１１
#
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data,label,name):
    return data[label].get(name)

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1,'') #如果只有姓+名，在中间插入一个middle
    labels = 'first','middle','last' #这样定义出来的是元组
    for label, name in zip(labels,names):
        people = lookup(data,label,name)
        if people:
            people.append(full_name) #如果能够找到这个name 的key，那把后面的append进去
        else: #找不到这个key 就创建这个key[name]
            data[label][name]=[full_name]

mynames = {}
init(mynames)
store(mynames,'Magnus Lier Hetland')
store(mynames,'Magnus Lier Hetland')
store(mynames,'Magnus Lie Hetland')
store(mynames,'Fox lee')
print mynames['first']
#结果有2个firstname 的key 
#{'Fox': ['Fox lee'], 'Magnus': ['Magnus Lier Hetland', 'Magnus Lier Hetland', 'Magnus Lie Hetland']}
print mynames['middle']
#结果又3个middle 的key
#{'Lier': ['Magnus Lier Hetland', 'Magnus Lier Hetland'], 'Lie': ['Magnus Lie Hetland'], '': ['Fox lee']}
print mynames['last']
#结果有2个lastname 的key
#{'lee': ['Fox lee'], 'Hetland': ['Magnus Lier Hetland', 'Magnus Lier Hetland', 'Magnus Lie Hetland']}