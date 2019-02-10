import { runCommand, getCLIArgument, isNullUndefinedOrEmpty, getFullFilePath }  from './utilities';
//import path from 'path';
import program from 'commander';
import colors from 'colors';

let cli = function (arg, cb) {

    switch (arg) {
        case 'git.addremote':   
            gitaddremote();
            break;

        case 'git.addignore':
            gitaddignore();
            break;

        case 'git.report':
            let filePath = getFullFilePath('source/python/cli.py');
            runCommand(`python "${filePath}" -d C:\\source -u iadams "Isaac Adams" -t "1 week ago"`, cb);
            break;

        default:
            cb('no such command exists');
            break;
    }

    function gitaddremote() {
        
        program
        .option('-n, --nickname <n>', 'Give the nickname for the remote repo')
        .option('-u, --url <u>', 'Give the url that points to the remote repo')
        .parse(process.argv); 
            
        let nickname = program.nickname;
        let url = program.url;

        if (!nickname || !url) {
            program.help((help) => colors.red('\nmissing required arguments!\n\n') + help);
        }
        
        try {
            let command = `
                git checkout master &&
                git remote add ${nickname} ${url} &&
                git fetch ${nickname} &&
                git pull ${nickname} master --allow-unrelated-histories &&
                git branch -u ${nickname}/master master &&
                git add *
                git push
            `;

            runCommand(command, cb);
        }
        catch {
            let command = `
                git remote add ${nickname} ${url}
                git push -u ${nickname} master
            `;

            runCommand(command, cb);
        }
        
    }

    function gitaddignore(cb) {
        let command = `
            echo node_modules/>> .gitignore && 
            git reset && 
            git add .gitignore && 
            git commit -m "added git ignore and ignoring node_modules folder"
        `;
        runCommand(command, cb);
    }

};

module.exports.cli = cli;