#!/usr/bin/env python

import re
import os
import sys
import glob
import errno

rootdir = '/Users/VibhorSood/Library/Safari/'
<<<<<<< HEAD
=======
#Removing Facebook cache from all folders under Safari

>>>>>>> cf53370502acd3eee9ceb4d79af33f92159d09fb
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = os.path.join(subdir,file)
        with open(filepath,'rb') as f:
            cont = f.read()
        if 'facebook' in cont:
            os.remove(os.path.join(subdir,file))
            #print os.path.join(subdir, file)

newdir = '/Users/VibhorSood/Library/Caches/com.apple.Safari/'
for subdir2, dirs2, files2 in os.walk(newdir):
    for file in files2:
        filepath2 = os.path.join(subdir2,file)
        with open(filepath2,'rb') as f2:
            cont2 = f2.read()
        if 'facebook' in cont2:
            os.remove(os.path.join(subdir2,file))
