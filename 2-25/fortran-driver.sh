#!/bin/bash

cd /Users/brownscholar/Documents/Intern/ocean-motion-2021/2-25 
python Writing-to-file-practice-2.py 930120
python Writing-to-file-practice-1.py 930120

gfortran -O3 -o vectorq.exe vectorq.f
gfortran -O3 -o omegainv.exe omegainv.f

./vectorq.exec
./omegainv.exec

