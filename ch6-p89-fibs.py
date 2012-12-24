#-*-coding:utf-8-*-
fibs = [0,1]
for i in xrange (20):
    fibs.append(fibs[-2]+fibs[-1])

print fibs

#黄金分割点的求值
gold = []
#print '%10.8f' % (float(fibs[-1])/float(fibs[-2]))
for x in range(len(fibs)-2):
   gold.append('%10.8f' % (float(fibs[-1-x])/float(fibs[-2-x]))) #要把浮点数压入数列,得这样用.....不知道3.0以后是不是也正

print gold


    
