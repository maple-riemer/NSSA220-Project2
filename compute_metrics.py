IP_NODE_1 = "192.168.100.1"

def compute():
	print(search("data/Node1.txt",IP_NODE_1))

def search(filename,ip):
	#messy, inefficent. Will be organized soon.
	f = open(filename, "r")

	ReqSentCount = 0
	ReqRecieveCount = 0
	RepSentCount = 0
	RepRecieveCount = 0

	ReqSentBytes = 0
	ReqRecieveBytes = 0
	RepSentBytes = 0 #not implemented
	RepRecieveBytes = 0 #not implemented

	for line in f:
		try:
			line = line.strip().split()

			#Computing Data Metrics...
			if (line[2] == ip and line[8] == "request"):
				ReqSentCount += 1 #data metric 1
				ReqSentBytes += int(line[5]) #data metric 5

			elif (line[3] == ip and line[8] == "request"):
				ReqRecieveCount += 1 #data metric 2
				ReqRecieveBytes += int(line[5]) #data metric 6

			elif (line[2] == ip and line[8] == "reply"):
				RepSentCount += 1 #data metric 3
				#add data metric for #7

			elif (line[3] == ip and line[8] == "reply"):
				RepRecieveCount += 1 #data metric 4
				#add data metric for #8

		except IndexError:
			continue

	f.close()

	DataCountMetrics=[ReqSentCount,ReqRecieveCount,RepSentCount,RepRecieveCount]
	DataByteMetrics=[ReqSentBytes,ReqRecieveBytes,RepSentBytes,RepRecieveBytes]

	return DataCountMetrics,DataByteMetrics

compute()