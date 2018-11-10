#!/usr/bin/env python

import os
from subprocess import check_output

bases = ['C:\\source', 'C:\\source\\LBS']
users = ['Isaac Adams', 'iadams']

def runCommand( cmd ):      
   return check_output(cmd, shell=True).decode("utf-8")

def displayCommits(dir, user):
        if not os.path.isdir(dir):
            return

        cmd = 'cd ' + dir + ' && git log --branches=* ' + \
            '--author="' + user + '" --after="1 week ago" --oneline --reverse'
        
        commits = runCommand(cmd)
        isCommit = len(commits) > 0 and "Not a directory" not in commits and "Not a git repository" not in commits 

        if isCommit:
            print (dir)
            # Remove hash
            #commits = [' '.join(['-'] + commit.split(' ')[1:]) for commit in commits.split('\n')]
            #print ('\n'.join(commits) + '\n')
            print(commits)
        
        return isCommit

def isGitOrNodeModules(dir):
    return os.path.basename(dir) == ".git" or os.path.basename(dir) == "node_modules"

def listdir_fullpath(d):
    if os.path.isdir(d):
        return [os.path.join(d, f) for f in os.listdir(d)]
    
    return []

def searchForRepo(parent):
    for subs in listdir_fullpath(parent):
        #process each directory in the parent, unless they are .git or node_modules folder
        if isGitOrNodeModules(subs):
            continue
        
        hasgit = os.path.isdir(os.path.join(subs, ".git"))

        if hasgit:
            for user in users:
                #if there were commits to be displayed, then don't try another user name
                if displayCommits(subs, user):
                    break

        #also check subdirectories
        searchForRepo(subs)

searchForRepo(bases[0])