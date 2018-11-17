from subprocess import check_output

def runCommand( cmd ):      
   return check_output(cmd, shell=True).decode("utf-8")
