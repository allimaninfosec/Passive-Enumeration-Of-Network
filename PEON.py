from scapy.all import sniff
import socket
import os 
import decode
#from geoip import geolite2


def detect (pkt):
        if pkt.proto == 6 and (pkt['TCP'].flags == 'S' or pkt['TCP'].flags =='SA'):
            frag = decode.convert_fragment(str(pkt.flags))
            tcp_options = decode.decode_options(pkt['TCP'].options)
            print (str(pkt.proto) + " " + str(pkt.src) + " " + str(pkt.dst) + " " +" "+ str(pkt['IP'].src)+ " " + str(pkt['IP'].dst) + " " + str(pkt.dport) + " " + str(pkt.ttl) + " "+ str(pkt.flags) + " " + str(pkt['TCP'].flags) + " " + str(pkt['TCP'].window)+":"+str(pkt.ttl)+":"+str(frag)+":"+str(pkt['IP'].len)+":"+str(tcp_options))
if __name__ == '__main__':
    sniff(filter="ip", prn=detect, iface="wlp0s20f3")