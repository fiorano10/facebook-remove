#!usr/bin/env python

import re
import os
import sys
import glob
import errno

path = '/Users/VibhorSood/Library/Caches/com.apple.Safari/WebKitCache/Version 11/Blobs/*'
path2 = '/Users/VibhorSood/Library/Caches/com.apple.Safari/fsCachedData/*'
rootdir = '/Users/VibhorSood/Library/Caches/com.apple.Safari/WebKitCache/Version 11/Records'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        cont = f.read()
    #if re.match ("(.*)(f||F)acebook(.*)",cont):
    if 'facebook' in cont:
        #print ("Facebook is tracking you!")
        #print name
        os.remove(name)
#Removing files from folder #2
files2 = glob.glob(path2)
for name2 in files2:
    with open(name2) as f:
        cont2 = f.read()
    if 'facebook' in cont2:
        os.remove(name2)
#Removing files from folder #3
for subdir, dirs, files3 in os.walk(rootdir):
    for file in files3:
        filepath = os.path.join(subdir,file)
        with open(filepath,'rb') as f:
            cont3 = f.read()
        if 'facebook' in cont3:
            os.remove(os.path.join(subdir,file))
            #print os.path.join(subdir, file)
