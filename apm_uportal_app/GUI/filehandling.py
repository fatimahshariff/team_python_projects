
def write_file(path, sent):
	f = open(path, 'w+')
	f.write(sent)



def append_file(path, sent):
	f = open(path, 'a+')
	f.write('\n' + sent)



def read_file(path):
	f = open(path, 'r')
	print(f.read())