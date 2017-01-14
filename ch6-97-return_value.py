#! python3

def inc(x): return x + 1

def inc2(x): x[0]=x[0]+1


if __name__ == '__main__':
	foo1 = 10
	foo1 = inc(foo1)
	print (foo1)
	foo2 = [10]
	inc2(foo2)
	print (foo2)
