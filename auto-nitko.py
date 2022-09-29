#!/usr/bin/env python3

# Author     : William Lorenzo
# Tool       : Auto Nitko
# Usage      : python3 auto-nitko.py ipaddress
# Description: Find open HTTP/s Port and check them with Nitko

import sys
import argparse
import ipaddress

# Setup our help
usage="%s -i IPv4 Address" % sys.argv[0]
parser=argparse.ArgumentParser()
parser.add_argument("-i","--ip-address", help="IPv4 Address")
args = parser.parse_args()

# Make sure this is really an IP address
try:
    ip = ipaddress.ip_address(sys.argv[2])
except ValueError:
    print('%s is an invalid IP Address' % sys.argv[2])
except:
    print('Syntax: %s -i <ip>' % sys.argv[0])
