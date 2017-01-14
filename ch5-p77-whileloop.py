#-*-coding:utf-8-*- #中文
name = ''
while not name.strip(): #防止输入一个纯空格
    name = raw_input('Name ?')
print 'Hello , %s!' % name