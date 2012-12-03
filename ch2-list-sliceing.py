####分片
##分片可以通过制定一定范围来访问一个序列,分片就是指定索引的范围
tag = '<a href="http://www.python.org">Python web site</a>'
print (tag[9:30]) #从第九个元素开始直到第三十个
print (tag[32:-4]) #从第三十二个开始直到倒数第四个

numbers = [1,2,3,4,5,6,7,8,9,10]
print (numbers[3:9])
print (numbers[0:1])
print (numbers[7:10])
print (numbers[-3:-1])#这样并不能访问到最后一个元素
print (numbers[-3:])  #这样可以访问最后一个元素
print (numbers[0:])
print (numbers[:]) #和 0：1 一样都能列出所有的与啊素

print (numbers[:-4])

#分片还能给出步长
print (numbers[0:10:2])
