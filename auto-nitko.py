#!/usr/bin/env python3

# Author     : William Lorenzo
# Tool       : Auto Nitko
# Usage      : python3 auto-nitko.py ipaddress
# Description: Find open HTTP/s Port and check them with Nitko

import sys
import socket

if len(sys.argv) == 2:
    scantarget = socket.gethostbyname(sys.argv[1])
else:
    print("Syntax: auto-nitko.py <ip>")