#!/bin/env python
#-*- coding: utf-8 -*-

#-*- coding: utf-8 -*-

import os
import sys
import datetime
import platform
import multiprocessing
from multiprocessing import Pool
from mylog import get_log_data
from time import sleep

print "운영체제: ", platform.system()
print "운영체제의 상세정보: ", platform.platform()
print "운영체제 버전: ", platform.version()
print "프로세서: ", platform.processor()
print "CPU 수: ", multiprocessing.cpu_count()

def f(x):
    # Put any cpu (only) consuming operation here. I have given 1 below -
    while True:
        x * x
        
        
for ____

# decide how many cpus you need to load with.
no_of_cpu_to_be_consumed = 3

p = Pool(processes=no_of_cpu_to_be_consumed)
p.map(f, range(no_of_cpu_to_be_consumed))
