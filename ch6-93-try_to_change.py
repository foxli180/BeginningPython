#! python3

def try_to_change(n):
	n = 'Fox.Lee'
	print ("in 1 n is : ", n)

def try_to_change_2(n):
	n[0] = 'Fox.Lee'
	print ('in 2 n is :', n)

if __name__ == '__main__':
	name = 'Jenny.Du'
	print ("call change 1:")
	try_to_change(name)
	print ("name is : ", name)
	names = ['Jenny.Du', 'Kitten']
	print ("call change 2:")
	try_to_change_2(names)
	print ("names are :", names)
