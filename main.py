import scapy.all as scapy
import argparse
#1)arp_request
#2)broadcast
#3)response
class NetworkScanner():

    def parseinfo(self):
        #kullanıcan bilgi alacağız
        parse_o = argparse.ArgumentParser()
        parse_o.add_argument("-r","--range",dest="range",help="please enter the range,ex:10.0.2.0/24")
        self.data = parse_o.parse_args()


    def Scan(self):
        arp_request_packet = scapy.ARP(pdst=self.data.range)
        broadcast_packet = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")
        combined_packet = broadcast_packet/arp_request_packet
        (answerd_list, unanswered_list) = scapy.srp(combined_packet,timeout = 1)
        answerd_list.summary()


if __name__ == "__main__":
    networkscanner = NetworkScanner()
    networkscanner.parseinfo()
    networkscanner.Scan()