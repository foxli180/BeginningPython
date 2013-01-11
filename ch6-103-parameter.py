#-*-coding:utf-8-*-

def interval (start, stop=None,step=1):
     if stop is None:
          # value = (0,start)
          # start,stop = value
          start,stop = 0,start
     result = []
     print ('start: {0}'.format(start1))
     print ('stop: {0}'.format(stop))
     i = start
     while  i < stop:
          result.append(i)
          i += step
     return result



