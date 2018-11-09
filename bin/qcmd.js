#!/usr/bin/env node
//console.log();
require('../dist/index').cli(process.argv[2], log);

function log(message) {
    console.log(message);
}