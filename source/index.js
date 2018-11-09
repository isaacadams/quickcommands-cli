import { runCommand, getCLIArgument, isNullUndefinedOrEmpty }  from './cli';

let cli = function(arg, cb) {
    
    switch(arg){
        case 'git.addremote':
        gitaddremote(cb);
        break;

        case 'git.addignore':
        gitaddignore(cb);    
        break;
    }


    function gitaddremote(cb) {
        let nickname = getCLIArgument('nickname');
        let link = getCLIArgument('link');
    
        if(isNullUndefinedOrEmpty(nickname) || isNullUndefinedOrEmpty(link)){
            return cb('required arguments --nickname and --link are missing');
        }       
    
        let command = `
            git checkout master &&
            git remote add ${nickname} ${link} &&
            git fetch ${nickname} &&
            git pull ${nickname} master --allow-unrelated-histories &&
            git branch -u ${nickname}/master master &&
            git add *
            git push
        `;
    
        runCommand(command, cb);
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

}



module.exports.cli = cli;