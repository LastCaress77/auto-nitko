#!/usr/bin/env python3

import sys
import socket

if len(sys.argv) == 2:
    scantarget = socket.gethostbyname(sys.argv[1])
else:
    print("Syntax: auto-nitko.py <ip>")