#-*-coding:utf-8-*-
#定义允许中文字符

#列表是一种序列，序列里允许序列的存在

Fox = ['Fox.Li',18]
Jeney = ['Jeney.Du',30]
database = [Fox,Jeney]
print (database) #把这个当作是2维数组
print (database [1]) #输出 jeney
print (database [0][1]) #输出 18


#对数组的操作，包括 索引，分片，加，乘， 成员资格
######索引####
print ('######索引####')
greeting = 'Hello'
print ('greeting [0] = ' + greeting[0]) #输出第一个
print ('greeting[-1] = ' + greeting[-1])#输出最后一个,最后一个数据的编号是 -1

######不使用变量来访问序列

print ("'Hello'[0] = "+'Hello'[0])
print ("'Hello'[-1] = " + 'Hello'[-1])

######对返回值进行裁剪

forth = raw_input ('Year: ')[3] #forth 返回的是输入的第四个字符 如果只输入了3个字符会报错

print (forth)

#####根据输入的数字年月日，转换为英文格式的
print ('#####根据输入的数字年月日，转换为英文格式的')

def datetransfer(year,month,day):
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December']
    # 以 1-31 的数字为结尾 的列表
    endings = ['st','nd','rd'] + 17*['th'] \
              +['st','nd','rd'] + 7*['th'] \
              +['st']
    month_number = int(month)
    day_number = int(day)
    month_name = months[month_number-1] #翻译month name
    ordinal = day + endings[day_number-1] #给day + 后缀
    print (month_name + ' ' + ordinal + ', ' + year) #打印

year = raw_input ('Years: ')
month = raw_input ('Month: ')
day = raw_input ('Day: ')
datetransfer(year,month,day)



#



