#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import random

servers = [ '37.130.227.140:1935',
            '46.28.49.36:1935',
            '46.28.55.182:1935',
            '46.28.55.217:1935',
            '91.109.247.180:1935',
            '91.109.247.184:1935',
            '91.109.247.186:1935',
            '109.123.113.94:1935',
            '109.202.101.108:1935',
            '109.232.224.37:1935',
            '146.185.16.46:1935',
            '146.185.16.50:1935',
            '146.185.16.6:1935',
            '146.185.16.74:1935',
            '146.185.25.130:1935',
            '146.185.25.162:1935',
            '146.185.25.186:1935',
            '159.8.244.200:1935',
            '159.8.244.201:1935',
            '159.8.244.202:1935',
            '159.8.244.253:1935',
            '176.67.175.156:1935',
            '179.43.158.195:1935',
            '179.43.158.196:1935',
            '179.43.158.197:1935',
            '179.43.158.198:1935',
            '179.43.158.199:1935',
            '179.43.158.200:1935',
            '179.43.158.201:1935',
            '179.43.158.202:1935',
            '179.43.158.203:1935',
            '185.80.220.7:1935',
            '185.80.220.8:1935',
            '185.80.220.9:1935',
            '188.95.48.71:1935',
            '209.95.51.122:1935',
            '209.95.51.123:1935',
            '209.95.51.144:1935',
            '209.95.51.145:1935',
            '213.152.162.122:1935',
            '213.152.180.151:1935',
            '213.152.180.243:1935',
            '213.152.180.250:1935',
            '213.152.181.10:1935',
            '213.152.181.11:1935',
            '213.152.181.12:1935' ]


def get():
    return random.choice(servers)
