import xml.etree.ElementTree as ET
import os
import module.pusher as pusher
def update():
    update_file = str(os.getcwd()) + '/tcp.xml'
    tree = ET.parse(update_file)
    root = tree.getroot()
    for fingerprints in root:
        for fingerprint in fingerprints:
            for testtype in fingerprint:
                for test in testtype:
                    pusher.update_me(fingerprint.attrib['name'] ,fingerprint.attrib['os_name'] ,fingerprint.attrib['os_vendor'] , fingerprint.attrib['os_class'], fingerprint.attrib['device_type'], fingerprint.attrib['device_vendor'], test.attrib['weight'], test.attrib['matchtype'],test.attrib['tcpflag'] , test.attrib['tcpsig'])
if __name__ == '__main__':
    update()
#def 
