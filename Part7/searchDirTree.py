'''
Created on Sep 10, 2021

@author: osboxes
'''

import os, glob, pprint
dirname = r'/home/osboxes/eclipse-workspace/python/Part7'

allsizes = []
apply = glob.glob(dirname + os.sep + "*.py")
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    for filename in filesHere:
        if filename.endswith('.py'):
            fullname = os.path.join(thisDir, filename)
            filesize = os.path.getsize(fullname)
            allsizes.append((filesize, fullname))
    
allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
# print(allsizes)