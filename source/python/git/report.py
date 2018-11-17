import os
from source.python.utilities import runCommand


def isGitOrNodeModules(directory):
    return os.path.basename(directory) == ".git" or os.path.basename(directory) == "node_modules"

def listdir_fullpath(d):
    if os.path.isdir(d):
        return [os.path.join(d, f) for f in os.listdir(d)]
    
    return []
    

class GitReport:
    def __init__(self, directory, users, time):
        self.directory = directory
        self.users = users
        self.time = time


    def searchForRepos(self, directory):
        for subDir in listdir_fullpath(directory):
            #process each directory in the parent, unless they are .git or node_modules folder
            if isGitOrNodeModules(subDir):
                continue
            
            hasgit = os.path.isdir(os.path.join(subDir, ".git"))
            if hasgit:
                for user in self.users:
                    #if there were commits to be displayed, then don't try another user name
                    if self.displayCommits(subDir, user):
                        break
            
            #also check subdirectories
            self.searchForRepos(subDir)
            

    def report(self):
        self.searchForRepos(self.directory)


    def displayCommits(self, directory, user):
        if not os.path.isdir(directory):
            return
        
        cmd = f"""cd {directory} && git log --branches=* --author="{user}" --after="{self.time}" --oneline --reverse"""
        
        commits = runCommand(cmd)
        isCommit = len(commits) > 0 and "Not a directory" not in commits and "Not a git repository" not in commits 

        if isCommit:
            print (directory)
            # Remove hash
            #commits = [' '.join(['-'] + commit.split(' ')[1:]) for commit in commits.split('\n')]
            #print ('\n'.join(commits) + '\n')
            print(commits)
        
        return isCommit