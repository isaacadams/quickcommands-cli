import os
import sys

def addDirectoryToPaths(pathToDir, verbose = False):
    #get the immediate parent directory name of this file
    Directory = os.path.dirname(__file__)
    #join the parent directory to the given relative path
    Join = os.path.join(Directory, pathToDir)
    #convert to an absolute path
    Abs = os.path.abspath(Join)
    #add it to the system paths
    sys.path.insert(0, Abs)
    if(verbose):
        print(f"\n\nAdding '{Abs}' to system paths")
        print("\nSystem Paths:")
        for path in sys.path:
            print(path)

addDirectoryToPaths('../..')

from source.python.git.report import GitReport

import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help='add the full path to the directory you want to look in, example: C:\\source', required=True)
parser.add_argument('-u', '--users', help='add the names of the users you would like to generate the report on, example: iadams, "Isaac Adams"', nargs='+', required=True)
parser.add_argument('-t', '--time', help='the timeframe that you want to report on example: "1 week ago"', required=True)
args = parser.parse_args()

GitReport(args.directory, args.users, args.time).report()


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