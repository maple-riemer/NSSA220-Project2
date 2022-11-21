IP_NODE_1 = "192.168.100.1"

def compute(packetList,ip):
	#packetList - list of filtered+parsed packets given from packet_parser.py
		#format should be packet_num, time, frame, data, ttl, sequence, type
	#ip - IP for specific Node
	
	ReqSentCount = 0
	ReqRecieveCount = 0
	RepSentCount = 0
	RepRecieveCount = 0

	ReqSentBytes = 0
	ReqRecieveBytes = 0
	RepSentBytes = 0 #not implemented
	RepRecieveBytes = 0 #not implemented

	for packet in packetList:

		try:
			#Computing Data Metrics...
			#inefficeint, will re-org once all logic is down
			if (packet[2] == ip and packet[8] == "request"):
				ReqSentCount += 1 #data metric 1
				ReqSentBytes += int(packet[5]) #data metric 5

			elif (packet[3] == ip and packet[8] == "request"):
				ReqRecieveCount += 1 #data metric 2
				ReqRecieveBytes += int(packet[5]) #data metric 6

			elif (packet[2] == ip and packet[8] == "reply"):
				RepSentCount += 1 #data metric 3
				#add data metric for #7

			elif (packet[3] == ip and packet[8] == "reply"):
				RepRecieveCount += 1 #data metric 4
				#add data metric for #8

		except IndexError:
			continue

	DataCountMetrics=[ReqSentCount,ReqRecieveCount,RepSentCount,RepRecieveCount]
	DataByteMetrics=[ReqSentBytes,ReqRecieveBytes,RepSentBytes,RepRecieveBytes]

	return DataCountMetrics,DataByteMetrics