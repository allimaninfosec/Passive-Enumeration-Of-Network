import configparser
from distutils.command.config import config
from socket import gethostname
from elasticsearch import Elasticsearch
import os
import re
from datetime import datetime

current_directory = os.getcwd()
config_file = current_directory + "/config.ini" 
config = configparser.ConfigParser()
config.read(config_file)
print ('Loading configuration from: ' + config_file)
es_host = config['ELASTIC']['server']
es = Elasticsearch(hosts=es_host)
#print (es.info())
def send_me(src_mac, src_ip, dest_ip,dest_mac , dest_port, tcp_fp, flag):
    hname = str(gethostname())
    doc ={
        '@timestamp': datetime.utcnow(),
        'sensor': hname,
        'dest_ip': dest_ip,
        'dest_mac': dest_mac,
        'dest_port': dest_port,
        'src_ip': src_ip,
        'src_mac': src_mac,
        'signature': tcp_fp,
        'tcp_flag': flag
    }
    resp = es.index(index="tcp_trans", document=doc)
    print(str(datetime.utcnow()) + ' ' +resp['result'])
    es
def update_me(name, os_name, os_vendor, os_class, device_type, device_vendor, sig_weight, sig_matchtype, sig_tcpflag, signature):
    doc = {
        "os_vendor": os_vendor ,
        "sig_matchtype": sig_matchtype,
        "signature": clean_sig(signature),
        "name": name,
        "os_name": os_name,
        "device_type": device_type,
        "device_vendor": device_vendor,
        "os_class": os_class,
        "sig_weight": sig_weight,
        "sig_tcpflag": sig_tcpflag
    }
    print  (doc)
    resp = es.index(index="tcp_sigs", document=doc)
    print(str(datetime.utcnow()), resp['result'])
def clean_sig(sig):
    #print(sig)
    regex = '(?P<sig>(((\d{1,5}|\S)\:){4}.+?))\:'
    try:    
        r = re.compile(regex)
        clean_sig = r.match(sig)
        clean_sig = str(clean_sig.group('sig'))
    except:
        clean_sig = sig[:-1]
    #clean_sig = clean_sig[:-1]
    return clean_sig