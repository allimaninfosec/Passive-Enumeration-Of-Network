import configparser
from distutils.command.config import config
from socket import gethostname
from elasticsearch import Elasticsearch, helpers
import os
from datetime import datetime