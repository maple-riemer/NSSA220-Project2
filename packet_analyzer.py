import sys
from filter_packets import *
from packet_parser import *
from compute_metrics import *

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage packet_analyzer.py")
        sys.exit()
    else:
        ip_list=["192.168.100.1","192.168.100.2","192.168.200.1","192.168.200.2"]
        i=1

        while(i<=4):
            current_ip=ip_list[i-1]

            filename="data/NodeXYZ.txt"
            filename=filename.replace("XYZ",str(i))
            
            filter(filename)

            packets=[]
            filtered=filename.replace(".txt", "_filtered.txt")
            read_data(filtered,packets)
        
            dataList=[]
            parse_all(packets,dataList)

            DataCountMetrics,DataByteMetrics=computeDataMetrics(dataList,current_ip)
            TimeMetrics=computeTimeMetrics(dataList,current_ip,DataByteMetrics)

            print("Node",i,"\n","Echo Requests Sent,Echo Requests Recieved,Echo Replies Sent,Echo Replies Recieved")
            print(DataCountMetrics[0],DataCountMetrics[1],DataCountMetrics[2],DataCountMetrics[3])
            print("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)")
            print(DataByteMetrics[0],DataByteMetrics[2])
            print("Echo Request Bytes Recieved (bytes),Echo Request Data Recieved (bytes)")
            print(DataByteMetrics[1],DataByteMetrics[3])
            print("\n")
            print("Average RTT (ms),",round(TimeMetrics[0],2),"\n","Echo Request Throughput (kB/sec),",round(TimeMetrics[1],1),"\n","Echo Request Goodput (kB/sec),",round(TimeMetrics[2],1),"\n","Average Reply Delay (us),",round(TimeMetrics[3],2))
            print("Average Echo Request Hop Count,",round(TimeMetrics[4],2),"\n")

            i+=1