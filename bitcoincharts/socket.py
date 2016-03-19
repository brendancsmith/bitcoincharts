# based on
# https://github.com/crschmidt/bitcoincharts/blob/8b168c963a517832b000fca113733d30db685c65/chart.py

import json
import socket


def open():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("bitcoincharts.com", 27007))

    return s


def receive(socket):
    f = socket.makefile()
    line = f.readline()
    obj = json.loads(line)
    return obj
