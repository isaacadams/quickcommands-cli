import os
from source.python.utilities import runCommand

def displayCommits(directory, user):
        if not os.path.isdir(directory):
            return

        time = '1 week ago'

        cmd = f"""cd {directory} && git log --branches=* --author="{user}" --after="{time}" --oneline --reverse"""
        
        commits = runCommand(cmd)
        isCommit = len(commits) > 0 and "Not a directory" not in commits and "Not a git repository" not in commits 

        if isCommit:
            print (directory)
            # Remove hash
            #commits = [' '.join(['-'] + commit.split(' ')[1:]) for commit in commits.split('\n')]
            #print ('\n'.join(commits) + '\n')
            print(commits)
        
        return isCommit

def isGitOrNodeModules(directory):
    return os.path.basename(directory) == ".git" or os.path.basename(directory) == "node_modules"

def listdir_fullpath(d):
    if os.path.isdir(d):
        return [os.path.join(d, f) for f in os.listdir(d)]
    
    return []

def searchForRepo(parent, users):
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
        searchForRepo(subs, users)
    

def gitReport(reposDir, users):
    searchForRepo(reposDir, users)

#searchForRepo(bases[0], users)