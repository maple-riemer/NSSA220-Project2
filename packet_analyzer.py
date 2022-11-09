import sys
from filter_packets import *
from packet_parser import *
from compute_metrics import *

filter()
parse()
compute()

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage packet_analyzer.py")
        sys.exit()
    else:
        print("Placeholder Text")