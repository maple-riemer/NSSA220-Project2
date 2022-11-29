def read_data(filename, list):
	file = open(filename, 'r')
	line = file.readline()
	for line in file:
		line = line.strip()
		line = line.split()
		try:
			int(line[0])
			list.append(line)
		except:
			continue
		
	file.close()


# gets a single packet from the lists of packets read and cleans out the unuseful data
def one_packet(list):
	packet = []
	j = 0
	for i in range(len(list)):
		if list[i][0] == "0000" and j == 0:
			packet.append(list[i])
			j += 1
		elif list[i][0] != "0000":
			packet.append(list[i])
		else:
			packet.pop()
			break
	for i in range(1, len(packet)):
		packet[i].pop()
		packet[i].pop(0)
	return packet

def read_packet(packet):
	packet_num = packet[0][0]
	time = packet[0][1]
	frame = 0
	ttl = int(packet[2][6], 16)
	be = int(packet[3][8]+packet[3][9], 16)
	le = int(packet[3][9] + packet[3][8], 16)
	sequence = str(be) + "/" + str(le)
	source = str(int(packet[2][10], 16)) + "." + str(int(packet[2][11], 16)) + "." + str(int(packet[2][12], 16)) + "." + str(int(packet[2][13], 16))
	destination = str(int(packet[2][14], 16)) + "." + str(int(packet[2][15], 16)) + "." + str(int(packet[3][0], 16)) + "." + str(int(packet[3][1], 16))
	if packet[3][2] == "08":
		_type = "request"
	else:
		_type = "reply"
	for i in range(1, len(packet)):
		for j in range(len(packet[i])):
			frame += 1
	data = frame - 42

	return [packet_num, time, source, destination, frame, data, ttl, sequence, _type]

def parse_all(filteredList, parsedList):
	while filteredList:
		packet = one_packet(filteredList)
		data = read_packet(packet)
		parsedList.append(data)
		filteredList = filteredList[len(packet):]
	return parsedList


if __name__ == "__main__":
	# testing the functions and outputs for one packet
	
	filteredList = []
	read_data("data/Node1_filtered.txt", filteredList)
	# packet = one_packet(list)
	# print(len(packet))
	# print(len(list))
	# for instance in packet:
	# 	print(instance)
	# data = read_packet(packet)
	# print(data)


	# creates an array of parsed packet data
	dataList = []
	parse_all(filteredList, dataList)
	print(dataList)