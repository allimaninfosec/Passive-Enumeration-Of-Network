import configparser
from distutils.command.config import config
from socket import gethostname
from elasticsearch import Elasticsearch
import os
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
        'tcp_sig': tcp_fp,
        'tcp_flag': flag
    }
    resp = es.index(index="tcp_trans", document=doc)
    print(str(datetime.utcnow()) + ' ' +resp['result'])
    es
    