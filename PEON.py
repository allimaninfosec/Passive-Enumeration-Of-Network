from scapy.all import sniff
import socket
import os 
import module.decode as decode
import module.pusher as pusher
import configparser
from distutils.command.config import config
from socket import gethostname
from elasticsearch import Elasticsearch
import os
from datetime import datetime

def detect (pkt):
        if pkt.proto == 6 and (pkt['TCP'].flags == 'S' or pkt['TCP'].flags =='SA'):
            frag = decode.convert_fragment(str(pkt.flags))
            tcp_options = decode.decode_options(pkt['TCP'].options)
            #print (str(pkt.flags) + " " + str(pkt['TCP'].flags) + " " + )
            options = str(pkt['TCP'].window)+":"+str(pkt.ttl)+":"+str(frag)+":"+str(pkt['IP'].len)+":"+str(tcp_options)
            pusher.send_me(str(pkt.src),pkt['IP'].src,pkt['IP'].dst,str(pkt.dst),pkt.dport, options, str(pkt['TCP'].flags))
if __name__ == '__main__':
    sniff(filter="ip", prn=detect, iface="wlp0s20f3")