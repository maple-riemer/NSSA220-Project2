IP_NODE_1 = "192.168.100.1"

def computeDataMetrics(packetList,ip):
	#packetList - list of filtered+parsed packets given from packet_parser.py
		#format should be packet_num, time, source, destination, frame, data, ttl, sequence, type
	#ip - IP for specific Node
	
	ReqSentCount = 0
	ReqRecieveCount = 0
	RepSentCount = 0
	RepRecieveCount = 0

	ReqSentBytes = 0
	ReqRecieveBytes = 0
	ReqSentData = 0
	ReqRecieveData = 0

	for packet in packetList:
	#inefficeint, will re-org once all logic is down

			#Computing Data Metrics...
			if (packet[2] == ip and packet[8] == "request"):
				ReqSentCount += 1 #data metric 1
				ReqSentBytes += int(packet[4]) #data metric 5

			elif (packet[3] == ip and packet[8] == "request"):
				ReqRecieveCount += 1 #data metric 2
				ReqRecieveBytes += int(packet[4]) #data metric 6

			elif (packet[2] == ip and packet[8] == "reply"):
				RepSentCount += 1 #data metric 3
				ReqSentData += packet[5] #data metric 7

			elif (packet[3] == ip and packet[8] == "reply"):
				RepRecieveCount += 1 #data metric 4
				ReqRecieveData += packet[5] #data metric 8

	DataCountMetrics=[ReqSentCount,ReqRecieveCount,RepSentCount,RepRecieveCount]
	DataByteMetrics=[ReqSentBytes,ReqRecieveBytes,ReqSentData,ReqRecieveData]

	return DataCountMetrics,DataByteMetrics
	

def computeTimeMetrics(packetList,ip,DataCountMetrics,DataByteMetrics):
	#packetList - list of filtered+parsed packets given from packet_parser.py
		#format should be packet_num, time, source, destination, frame, data, ttl, sequence, type
	#ip - IP for specific Node

	#may combine computeTimeMetrics,and data metrics functions, bc similar if statements

	reqSent=[]
	reqRecieve=[]
	ReplySent=[]
	ReplyRecieve=[]

	RTTSum=0
	RTTList=[] #can prolly delete this, and just keep a tally; is only used for average calc

	for packet in packetList:
		
		#populate lists
		if(packet[2]==ip and packet[8]=="reply"): #replys i sent
			ReplySent.append(packet)

		elif(packet[3]==ip and packet[8]=="reply"): #replys i recieved
			ReplyRecieve.append(packet)

		elif(packet[2]==ip and packet[8]=="request"): #requests i sent
			reqRecieve.append(packet)

		elif(packet[3]==ip and packet[8]=="request"): #requests i recieved
			reqSent.append(packet)
	
	for request in reqSent:
		#find reply in replyRecieve
		reqSeq=request[7]
		for reply in ReplyRecieve:
			replySeq=reply[7]
			if (replySeq==reqSeq):
				#find RTT for single set
				RTT=abs(float(request[1])-float(reply[1]))
				RTTSum += RTT
				RTTList.append(RTT)
	
	for request in reqRecieve:
		#find reply in replySent
		reqSeq=request[7]
		for reply in ReplySent:
			replySeq=reply[7]
			if (replySeq==reqSeq):
				#find RTT for single set
				RTT=abs(float(request[1])-float(reply[1]))
				RTTSum += RTT
				RTTList.append(RTT)

	#calc RTT
	AverageRTT= (RTTSum/len(RTTList))/1000 # /1000 to make it ms

	#Find TBM #2
	ThroughPut= DataByteMetrics[0]/RTTSum

	#Find TBM #3
	GoodPut= DataByteMetrics[2]/RTTSum

	#Find TBM #4
	
	return AverageRTT,ThroughPut,GoodPut
