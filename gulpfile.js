let gulp = require('gulp'), 
    insert = require('gulp-insert-lite'),
    babel = require("gulp-babel"),
    merge = require('merge-stream');

let projects = 
    CreateProject('', 'source/node/', 'dist/', [
        'cli',
        'utilities'
    ]);

gulp.task('build', function() {
    return transpile(projects);
});

function CreateProject(folder, source, destination, scripts) {
    return {
        folder: folder,
        source: source,
        destination: destination,
        scripts: scripts
    };
}

function transpile({folder, scripts, source, destination}) {

    let streams = [];

    //prepends a comment to the babelified .js file so that developers know to look for the source version and make changes there
    let devNotice =
    `/* 
        NOTICE NOTICE NOTICE 
                         
        THIS IS AN AUTOMATICALLY GENERATED FILE BY GULP

        DO NOT EDIT THIS FILE DIRECTLY

        MAKE EDITS TO THE SAME FILE LOCATED IN THE 'SRC' FOLDER
    */`;

    for (let i = 0; i < scripts.length; i++) {
        let script = scripts[i];

        let sourceFile = folder + source + script + '.js';

        console.log('Transpiling ' + sourceFile);
        
        streams.push(
            gulp.src(sourceFile)
                .pipe(babel({
                    presets: ['@babel/env']
                }))
                .pipe(insert.prepend(devNotice))
                .pipe(gulp.dest(folder + destination))
        );
    }

    return merge(streams);
}