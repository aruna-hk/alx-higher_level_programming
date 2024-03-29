#!/usr/bin/node
const f = require('fs');
const first_arg = f.readFileSync(process.argv[2]).toString();
const scond_arg = f.readFileSync(process.argv[3]).toString();
f.writeFileSync(process.argv[4], first_arg + second_arg);
