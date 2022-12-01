import re


def filter(filename):
    f = open(filename, "r")
    output = open(filename.replace(".txt", "_filtered.txt"), "w")
    output.write("No. Time Source Destination Protocol Length Info\n")
    packets = []
    adding = False
    checking = False
    for line in f:
        clean_line = re.sub(r' +', ' ', line).strip() + "\n"
        if not checking and adding:
            output.write(clean_line)
        if checking:
            checking = False
            if "ICMP" in clean_line and "Echo" in clean_line:
                adding = True
                output.write(clean_line)
        if line.startswith("No."):
            adding = False
            checking = True
    f.close()
