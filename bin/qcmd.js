#!/usr/bin/env node

require('../dist/cli').cli(process.argv[2], log);

function log(message) {
    console.log(message);
}