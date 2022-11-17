import re


def filter(filename):
    f = open(filename, "r")
    output = open(filename.replace(".txt", "_filtered.txt"), "w")
    packets = []
    adding = False
    checking = False
    for line in f:
        clean_line = re.sub(r' +', ' ', line).strip() + "\n"
        if not checking and adding and not line.startswith("No.") and line != '\n':
            output.write(clean_line)
        if checking:
            if "ICMP" in clean_line and "Echo" in clean_line:
                adding = True
                output.write(clean_line)
            checking = False
        if line.startswith("No."):
            adding = False
            checking = True
