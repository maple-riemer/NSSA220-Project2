def read_data(filename, list):
	file = open(filename, 'r')
	line = file.readline()
	for line in file:
		line = line.strip()
		line = line.split()
		try:
			int(line[0])
			# if line[0]
			list.append(line)
		except:
			continue
		
	file.close()


# def parse():
# 	print('called parse function in packet_parser.py')
list = []

# gets a single packet from the lists of packets read and cleans out the unuseful data
def one_packet(list):
	packet = []
	j = 0
	for i in range(len(list)):
		if list[i][0] == "0000" and j == 0:
			packet.append(list[i])
			j += 1
			print(i)
		elif list[i][0] != "0000":
			packet.append(list[i])
		else:
			packet.pop()
			break
	for i in range(1, len(packet)):
		packet[i].pop()
		packet[i].pop(0)
	return packet
#read_data("data/example.txt", list)

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
		type = "request"
	else:
		type = "reply"
	for i in range(1, len(packet)):
		for j in range(len(packet[i])):
			frame += 1
	data = frame - 42
	return packet_num, time, source, destination, frame, data, ttl, sequence, type

# testing the functions and outputs for one packet
#packet = one_packet(list)
#for instance in packet:
	#print(instance)
#packet_num, time, source, destination, frame, data, ttl, sequence, type = read_packet(packet)
#print(packet_num, time, source, destination, frame, data, ttl, sequence, type)