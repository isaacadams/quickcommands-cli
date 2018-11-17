let exec = require('child_process').exec;

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