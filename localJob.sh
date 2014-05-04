#!/bin/bash
# job.sh

res="`./GenerateCenters.py 2`"
sed -i "7s/^.*$/centerList\ = $res/" KMeansMapper.py

for i in {1..50}
do
	echo $i
	res=`cat ../pig-tools/patterns/part-r-00000 |./KMeansMapper.py |sort|./KMeansReduce.py`
	echo '['$res']'
	echo '['$res']' >> c.data
	sed -i "7s/^.*$/centerList\ = [$res]/" KMeansMapper.py
done

