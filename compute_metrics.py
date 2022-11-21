IP_NODE_1 = "192.168.100.1"

def compute() :
	print('called compute function in compute_metrics.py')
	print(search("data/Node1.txt", "request"))
	#print(search("data/Node1.txt","reply"))

#Something slightly off here
#skipping lines; when told to print every line, it skips a considerable amount of them
# this is why not everything is being counted correctly
# thinking it has something to do with the try/except?? I have no idea... 
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