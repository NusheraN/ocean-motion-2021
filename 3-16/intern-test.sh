# !/bin/bash

STRING="START"
echo $STRING

cd /Users/brownscholar/documents/intern/ocean-motion-2021/2-25

#compiling files
gfortran -O3 -o vectorq.exe vectorq.f
gfortran -O3 -o omegainv.exe omegainv.f

dateList= '/Users/brownscholar/documents/intern/ocean-motion-2021/3-16/date_list.txt'

while read p; do
	echo $p

	#creating exec files with all dates
	python writing-exec-files-1.py $p
	python writing-exec-files-2.py $p

	#running exec files
	./vectorq.exec
	./omegainv.exec
	
done </Users/brownscholar/documents/intern/ocean-motion-2021/3-16/date_list.txt

STRING="DONE"
echo $STRING