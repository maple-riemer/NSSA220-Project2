IP_NODE_1 = "192.168.100.1"

def compute() :
	print('called compute function in compute_metrics.py')
	print(search("data/Node1.txt", "request"))

# Something slightly off here
def search(filename, string):
	f = open(filename, "r")
	count = 0
	for line in f:
		try:
			line = f.readline().strip().split()
			if (line[2] == IP_NODE_1 and line[8] == string):
				print(line)
				count += 1
		except IndexError:
			continue
	f.close()
	return count

compute()