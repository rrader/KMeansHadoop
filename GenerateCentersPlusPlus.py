#!/usr/bin/env python3

import sys
import random

from KMeansMapper import distanceOfTwoProperty

try:
    from foundCenters import centerList
except ImportError:
    centerList = []

def parse(line):
    return [float(i) for i in line.strip().split(",")[1:24*7+1]]

if __name__ == "__main__":
    if not centerList:
        print("centerList = " + str([parse(next(sys.stdin))]))
        sys.exit()
    distances = []
    max_distance = 0
    fCenter = None
    for line in sys.stdin:
        line = parse(line)
        if line in centerList:
            continue
        dists = [distanceOfTwoProperty(line, center) for center in centerList]
        center_id, distance = min(enumerate(dists), key=lambda x:x[1])
        if distance > max_distance:
            max_distance = distance
            fCenter = line
    centerList.append(fCenter)
    print("centerList = " + str(centerList))
