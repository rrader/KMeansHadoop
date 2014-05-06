#!/bin/bash
# job.sh

DATA="../pig-tools/patterns/part-r-00000"

echo "Generating initial centers"
rm -f foundCenters.py
for i in {1..2}
do
	echo $i
	res="`cat $DATA | ./GenerateCentersPlusPlus.py`"
	echo "$res" > foundCenters.py
done

rm -f c.data
res="`cat foundCenters.py`"
sed -i "7s/^.*$/$res/" KMeansMapper.py

echo "Running K-Means"
for i in {1..5}
do
	echo $i
	res=`cat $DATA |./KMeansMapper.py |sort|./KMeansReduce.py`
	#echo '['$res']'
	echo '['$res']' >> c.data
	sed -i "7s/^.*$/centerList\ = [$res]/" KMeansMapper.py
done

cat $DATA | ./KMeansClassifier.py > clusters.dat
while read line
do
	redis-cli SET `echo "class:$line" | tr ',' ' '`
done < clusters.dat