#-*-coding:utf-8-*- #enable chinese char displaying
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data,label,name):
    return data[label].get(name)


def store(data, *fullnames): #now we can send more than 1 names at 1 time
    for fullname in fullnames:
        names = fullname.split()
        if len(names) == 2: names.insert(1,'')
        labels = 'first','middle','last'
        for name,label in zip(names,labels):
            people = lookup(data,label,name)
            if people:
                people.append(fullname)
            else:
                data[label][name]=[fullname]


mynames2 = {}
init(mynames2)
store(mynames2,'Fox lee','Hello world','Fox zhang','Fox hello zhang')#
print mynames2['first']
print mynames2['middle']
print mynames2['last']
