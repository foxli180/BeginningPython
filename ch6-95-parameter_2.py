#! python3

def init(data):
	data['first'] = {}
	data['middle'] = {}
	data['last'] = {}

def lookup (data, label, name):
	return data[label].get(name)


def store( data, full_name):
	names = full_name.split()
	if len(names) == 2: names.insert(1, '' )
	labels = 'first', 'middle', 'last'
	for label , name in zip (labels, names):
		people = lookup(data, label, name)
		if people:
			people.append (full_name)
		else:
			data[label][name]=[full_name] #do not forget if you wanna appendd you have to set the name as list do not forget []


if __name__ == '__main__':

	storage = {}
	init(storage)
	print ("storage: ", storage)
	store(storage, 'Fox Lee')
	store(storage, 'Robin Hood')
	store(storage, 'Robin locksey Lee')
	print ("storage: ", storage)
	print (lookup(storage, 'first', 'Robin'))

