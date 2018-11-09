/* 
        NOTICE NOTICE NOTICE 
                         
        THIS IS AN AUTOMATICALLY GENERATED FILE BY GULP

        DO NOT EDIT THIS FILE DIRECTLY

        MAKE EDITS TO THE SAME FILE LOCATED IN THE 'SRC' FOLDER
    */

"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.runCommand = runCommand;
exports.getCLIArgument = getCLIArgument;
exports.isNullUndefinedOrEmpty = isNullUndefinedOrEmpty;

var exec = require('child_process').exec;

function runCommand(command, callback) {
  command = command.replace(/\r?\n|\r/g, " ");
  exec(command, function (err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
    callback(err);
  });
}

function getCLIArgument(name) {
  var i = process.argv.indexOf("--".concat(name));
  return i > -1 ? process.argv[i + 1] : null;
}

function isNullUndefinedOrEmpty(value) {
  return value === null || value === undefined || value === '';
}