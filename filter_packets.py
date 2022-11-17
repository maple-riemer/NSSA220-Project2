import re


def filter(filename):
    f = open(filename)
    packets = []
    adding = False
    checking = False
    for line in f:
        if not checking and adding and not line.startswith("No.") and line != '\n':
            packets[-1].append(re.sub(r' +', ' ', line).strip().split(' '))
        if checking:
            cleanLine = re.sub(r' +', ' ', line).strip().split(' ')
            if "ICMP" in cleanLine and "Echo" in cleanLine:
                adding = True
                packets.append([])
                packets[-1].append(cleanLine)
            checking = False
        if line.startswith("No."):
            adding = False
            checking = True
    return packets
