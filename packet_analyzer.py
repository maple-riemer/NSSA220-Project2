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

            print("\033[1;3m","Node",i,"\033[0m","\n","Echo Requests Sent:",DataCountMetrics[0],"\n","Echo Requests Recieved:",DataCountMetrics[1],"\n","Echo Replies Sent:",DataCountMetrics[2],"\n","Echo Replies Recieved",DataCountMetrics[3],"\n")
            print("Echo Request Bytes Sent:",DataByteMetrics[0],"\n","Echo Request Bytes Recieved:",DataByteMetrics[1],"\n","Echo Request Data Sent:",DataByteMetrics[2],"\n","Echo Request Data Recieved",DataByteMetrics[3],"\n")
            print("Average RTT (ms):",round(TimeMetrics[0],2),"\n","Echo Request Throughput (kB/sec):",round(TimeMetrics[1],1),"\n","Echo Request Goodput (kB/sec):",round(TimeMetrics[2],1),"\n","Average Reply Delay (us):",round(TimeMetrics[3],2),"\n")
            print("Average Echo Request Hop Count:",round(TimeMetrics[4],2),"\n")

            i+=1