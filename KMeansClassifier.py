#!/usr/bin/env python3
# KMeansMapper.py

import sys
from KMeansMapper import centerList, distanceOfTwoProperty

if __name__ == "__main__":
    for line in sys.stdin:
        val = [float(i) for i in line.strip().split(",")[1:24*7+1]]
        dists = [distanceOfTwoProperty(val, center) for center in centerList]
        center_id, distance = min(enumerate(dists), key=lambda x:x[1])
        print(center_id)
