# quickcommands-cli
A cli with commands for doing daily developer activities in one command

An example of how to see help information for a command: `qcmd git.addremote --help`

For the node.js based commands, [commander](https://www.npmjs.com/package/commander) is used to build the options

### qcmd git.report
- this command will run a report on all the git commits you have made from the past week
- It only reports commits that were made by users 'Isaac Adams' and/or 'iadams' because I haven't figured out how to parse inputs in python yet

### qcmd git.addremote
- this command streamlines the process of adding an existing remote repo to a local repo

### qcmd git.addignore
- this command is a fast way of adding a .gitignore to your project
