def compute() :
	print('called compute function in compute_metrics.py')
	print(search("data/Node1.txt", "Echo (ping) request"))

# All this does is search for a string in a file and returns how many times it is found. Not sure how to tell
# if the given request or reply was sent or received.
def search(filename, string):
	f = open(filename, "r")
	count = 0

	for line in f:
		line = f.readline().strip()
		if (line.find(string) != -1):
			count += 1
	f.close()
	return count

