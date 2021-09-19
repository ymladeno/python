'''
Created on Sep 10, 2021

@author: osboxes
'''

import os, glob
dirname = r'/home/osboxes/eclipse-workspace/python/Part7'

allsizes = []
apply = glob.glob(dirname + os.sep + "*.py")
for filename in apply:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))
    
allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])
print(allsizes)