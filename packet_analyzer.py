import sys
from filter_packets import *
from packet_parser import *
from compute_metrics import *

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage packet_analyzer.py")
        sys.exit()
    else:
        filter("data/Node1.txt")

        packets=[]
        read_data("data/Node1_filtered.txt",packets) #hard coding file name for now
        
        dataList=[]
        parse_all(packets,dataList)

        DataCountMetrics,DataByteMetrics=computeDataMetrics(dataList,"192.168.100.1")
        print(DataCountMetrics,DataByteMetrics)
        print(computeTimeMetrics(dataList,"192.168.100.1",DataByteMetrics))  