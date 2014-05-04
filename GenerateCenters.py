#!/usr/bin/env python3

import sys
import random


count = int(sys.argv[1])
centerList = [[float(random.random()*15) for _ in range(0,24*7)] for _ in range(count)]
print(centerList)
