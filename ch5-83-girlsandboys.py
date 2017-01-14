#-*-coding:utf-8-*-
#找到 girls and boys 里首字母相同的

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']

# 方法一,列表推倒式, 效率 不高
print [b+"+"+g for b in boys for g in girls if b[0]==g[0]]

#方法二, 字典, 效率高
lettergirls = {}
for girl in girls: #将girls 的首字母和girls作为字典, 首字母为key girl 为value
    lettergirls.setdefault(girl[0],[]).append(girl)

print [b+'+'+g for b in boys for g in lettergirls[b[0]]] #查找以b[0]为key 的value