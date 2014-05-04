#!/usr/bin/env python3
# KMeansMapper.py

import sys
import linecache
import random
centerList = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.20189701897, 4.9891598916, 9.256097560975, 12.325203252000001, 12.787262872649999, 13.424119241199998, 11.8536585366, 10.836043360435, 10.810298102974999, 10.43360433605, 0.6517615176135, 0.607046070461, 0.79945799458, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.1653116531200003, 6.081300813005, 9.054200542004999, 11.111111111125, 11.146341463399999, 12.73577235775, 12.517615176150002, 13.021680216799998, 11.989159891599998, 9.63008130081, 0.966124661247, 0.7777777777765, 0.3644986449865, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.5840108401050004, 5.8116531165300005, 9.868563685634998, 13.77642276425, 10.2791327913, 11.619241192395, 11.800813008140002, 10.054200541999998, 9.925474254739997, 10.23577235771, 0.47289972899700006, 0.758807588076, 0.5609756097549999, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.5216802168, 6.991869918700001, 7.852303523035, 11.607046070449998, 11.6368563686, 11.38753387535, 12.86314363145, 13.28861788615, 11.276422764200001, 10.753387533850002, 0.43902439024400003, 0.710027100271, 0.4444444444445, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.178861788615, 6.604336043365, 8.7588075881, 13.907859078549999, 10.52981029812, 13.128726287249998, 10.5135501355, 12.98780487805, 12.864498645, 11.8292682927, 0.9132791327915001, 0.9607046070465, 0.9254742547404998, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2439024390245, 0.5, 0.1355013550135, 0.39159891598900004, 0.3048780487805, 0.682926829266, 0.4471544715445, 0.775067750677, 0.1355013550135, 0.4471544715445, 0.6951219512210001, 0.108401084011, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.08672086720850002, 0.527100271005, 0.1355013550135, 0.2560975609755, 0.8048780487805001, 0.45528455284550007, 1.0487804878029998, 0.707317073171, 1.1016260162579998, 0.330623306233, 0.9905149051479999, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.10840108401100002, 0.0, 0.0, 2.3617886178850003, 0.108401084011, 0.16937669376700001, 0.0, 0.0, 0.379403794038, 0.16937669376699996, 0.10840108401100002, 0.21680216802149999, 0.0, 1.6829268292700001, 0.9552845528459999, 1.135501355012, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.037940379405, 0.5487804878050001, 0.3089430894310001, 0.22222222222199997, 0.16937669376699996, 0.08672086720849999, 0.3387533875339999, 0.0, 0.08672086720850002, 0.16937669376699996, 1.0650406504080001, 1.7981029810299998, 1.451219512195, 0.08672086720849999, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.422764227645, 0.0, 0.1355013550135, 0.108401084011, 0.277777777778, 0.19512195121950002, 0.0, 0.0, 0.2560975609755, 0.08672086720849999, 0.7479674796770001, 0.7344173441719999, 0.9390243902445, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.8888888888899995, 0.08672086720850002, 0.1355013550135, 0.0, 0.16937669376699996, 0.08672086720849999, 0.0, 0.1355013550135, 0.0, 0.0, 0.7940379403779999, 0.9810298102979998, 1.2818428184299997, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.944444444445, 0.3048780487805, 0.0, 0.16937669376700001, 0.0, 0.0, 0.0, 0.08672086720849999, 0.2560975609755, 0.0, 1.4146341463449998, 1.833333333335, 0.42547425474250006, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.10840108401100002, 0.08672086720850002, 0.108401084011, 0.08672086720850002, 0.2439024390245, 0.9512195121940001, 0.39159891598900004, 1.4471544715450004, 0.30894308943099996, 0.41734417344200003, 0.6951219512194999, 0.6084010840085, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.277777777778, 0.3428184281845, 0.08672086720849999, 0.5609756097559999, 0.16937669376700001, 0.7222222222244999, 0.865853658537, 0.60840108401, 0.6693766937685002, 0.4173441734415, 0.5867208672084999, 0.5, 0.560975609756, 0.0]]

def distanceOfTwoProperty(property1, property2):
    temp = [(property1[i] - property2[i]) ** 2 for i in range(0, len(property1))]
    return sum(temp)

if __name__ == "__main__":
    for line in sys.stdin:
        val = [float(i) for i in line.strip().split(",")[1:24*7+1]]
        minDistance = distanceOfTwoProperty(val, centerList[0])
        minCenter = centerList[0]
        
        for i in range(1, len(centerList)):
            dist = distanceOfTwoProperty(val, centerList[i])
            if dist < minDistance:
                minCenter = centerList[i]
                minDistance = dist
        print('%s\t%s'%(minCenter, val))
