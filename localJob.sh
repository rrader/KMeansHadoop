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
for i in {1..50}
do
	echo $i
	res=`cat $DATA |./KMeansMapper.py |sort|./KMeansReduce.py`
	#echo '['$res']'
	echo '['$res']' >> c.data
	sed -i "7s/^.*$/centerList\ = [$res]/" KMeansMapper.py

	python -c "from KMeansMapper import centerList, distanceOfTwoProperty; print(distanceOfTwoProperty(centerList[0], centerList[1]))"
done

cat $DATA | ./KMeansClassifier.py
