import sys
import csv
from filter_packets import *
from packet_parser import *
from compute_metrics import *

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage packet_analyzer.py")
        sys.exit()
    else:
        csvwrite = csv.writer(open("project2_output.csv", "w"), delimiter=",", lineterminator='\n')
        ip_list=["192.168.100.1","192.168.100.2","192.168.200.1","192.168.200.2"]
        data = []
        i=0
        for ip in ip_list:
            i += 1
            filename = f"data/Node{i}.txt"
            filter(filename)

            packets = []
            filtered = filename.replace(".txt", "_filtered.txt")
            read_data(filtered, packets)
            dataList = []
            parse_all(packets, dataList)

            DataCountMetrics, DataByteMetrics = computeDataMetrics(dataList, ip)
            TimeMetrics = computeTimeMetrics(dataList, ip, DataByteMetrics)
            node_data = [
                [f"Node {i}"],
                [],
                ["Echo Requests Sent", "Echo Requests Recieved", "Echo Replies Sent", "Echo Replies Recieved"],
                [DataCountMetrics[0], DataCountMetrics[1], DataCountMetrics[2], DataCountMetrics[3]],
                ["Echo Request Bytes Sent (bytes)", "Echo Request Data Sent (bytes)"],
                [DataByteMetrics[0], DataByteMetrics[2]],
                [],
                ["Echo Request Bytes Recieved (bytes)", "Echo Request Data Recieved (bytes)"],
                [DataByteMetrics[1], DataByteMetrics[3]],
                ["Average RTT (ms),", round(TimeMetrics[0], 2)],
                ["Echo Request Throughput (kB/sec),", round(TimeMetrics[1], 1)],
                ["Echo Request Goodput (kB/sec),", round(TimeMetrics[2], 1)],
                ["Average Reply Delay (us),", round(TimeMetrics[3], 2)],
                ["Average Echo Request Hop Count,", round(TimeMetrics[4], 2)],
                []
            ]
            for node_row in node_data:
                data.append(node_row)
        csvwrite.writerows(data)