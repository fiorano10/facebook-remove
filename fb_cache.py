#!usr/bin/env python

import re
import os
import sys
import glob
import errno

rootdir = '/Users/VibhorSood/Library/Safari/'
#Removing Facebook cache from all folders under Safari

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = os.path.join(subdir,file)
        with open(filepath,'rb') as f:
            cont = f.read()
        if 'facebook' in cont:
            os.remove(os.path.join(subdir,file))
            #list all files that contain the keyword
            #print os.path.join(subdir, file)
