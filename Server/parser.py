#!/bin/python3

import requests
import xml.etree.ElementTree as ET

def load_def():
    url = 'https://raw.githubusercontent.com/xnih/satori/04f4bbf731675ccca7d9c0eefe27d6d25b3c4d12/fingerprints/tcp.xml'
    resp = requests.get(url)
    tree = ET.parse('./tcp.xml')
    root = tree.getroot()
    for fingerprints in root:
        for fingerprint in fingerprints:
            print('fp' + fingerprint)

load_def()

