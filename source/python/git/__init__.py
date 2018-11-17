#!/usr/bin/env python
import os
import sys

def addDirectoryToPaths(pathToDir, verbose = False):
    Directory = os.path.dirname(__file__)
    Join = os.path.join(Directory, pathToDir)
    Abs = os.path.abspath(Join)
    sys.path.insert(0, Abs)
    if(verbose):
        print(f"Adding {Abs} to system paths")
        print("System Paths:")
        for path in sys.path:
            print(path)

addDirectoryToPaths('../../..')

from source.python.git.report import gitReport

bases = ['C:\\source', 'C:\\source\\LBS']
users = ['Isaac Adams', 'iadams']

gitReport(bases[0], users)



#For understanding what adding a directory to path is doing
def SuperVerbose():
    print("File: " + __file__)
    Directory = os.path.dirname(__file__)
    print("Directory: " + Directory)
    Join = os.path.join(Directory, '..')
    print("Join: " + Join)
    Abs = os.path.abspath(Join)
    print("Absolute: " + Abs)
    print("System Paths:")
    for path in sys.path:
        print(path)
    sys.path.insert(0, Abs)
    print("New System Paths:")
    for path in sys.path:
        print(path)