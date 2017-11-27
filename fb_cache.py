#!usr/bin/env python

import re
import os
import sys
import glob
import errno

rootdir = '/Users/VibhorSood/Library/Caches/com.apple.Safari/'
#Removing Facebook cache from all folders under Safari

for subdir, dirs, files3 in os.walk(rootdir):
    for file in files3:
        filepath = os.path.join(subdir,file)
        with open(filepath,'rb') as f:
            cont3 = f.read()
        if 'facebook' in cont3:
            os.remove(os.path.join(subdir,file))
            #list all files that contain the keyword
            #print os.path.join(subdir, file)
