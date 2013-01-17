def mark_counter(x):
     print ('entering mark_counter')
     while True:
          yield x
          print ('incremeting x')
          x = x +1

counter = mark_counter(2)
