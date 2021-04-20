# !/bin/bash

STRING="START"
echo $STRING

cd /Users/brownscholar/documents/intern/New

#compiling files
gfortran -O3 -o vectorq.exe vectorq.f
gfortran -O3 -o omegainv.exe omegainv.f

#dateList= '/Users/brownscholar/documents/intern/ocean-motion-2021/3-23/date_list_04-16.txt'
dateList= '/Users/brownscholar/documents/intern/ocean-motion-2021/3-23/date_list-t2'
# dateList= '/Users/brownscholar/documents/intern/ocean-motion-2021/3-23/date_list-t3'
# dateList= '/Users/brownscholar/documents/intern/ocean-motion-2021/3-23/date_list-t4'
# dateList= '/Users/brownscholar/documents/intern/ocean-motion-2021/3-23/date_list-t5'

while read p; do
	echo $p
	pwd

	#creating exec files with all dates
	python writing-exec-files-1.py $p
	python writing-exec-files-2.py $p

	#running exec files
	chmod +x vectorq.exec
	chmod +x omegainv.exec
	./vectorq.exec
	./omegainv.exec
	
done </Users/brownscholar/documents/intern/ocean-motion-2021/3-23/date_list_04-16.txt

STRING="DONE"
echo $STRING