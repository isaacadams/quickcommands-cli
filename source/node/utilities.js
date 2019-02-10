
let path = require('path');
let { exec } = require('child_process');

export function runCommand(command, callback){
    command = command.replace(/\r?\n|\r/g, " ");
    exec(command, function (err, stdout, stderr) {
        log(stdout);
        log(stderr);
        if(err)            
            callback(err);
            
    });
}

export function getCLIArgument(name) {
    var i = process.argv.indexOf(`--${name}`);
    return (i>-1) ? process.argv[i+1] : null;
}

export function isNullUndefinedOrEmpty(value){
    return value === null || value === undefined || value === '';
}

function log(message){
    if(message){
        console.log(message);
    }
}

export function getFullFilePath(directPathToFileFromRoot) {
    // get current directory: ../quickcommands-cli/dist
    let dirname = path.dirname(__filename);
    // go up one level to get root directory: ../quickcommands-cli
    let abspath = path.resolve(path.join(dirname, '..'));
    // join root with the given path
    let file = path.join(abspath, directPathToFileFromRoot);
    return file;
}