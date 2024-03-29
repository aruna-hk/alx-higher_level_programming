#!/usr/bin/node
const f = require('fs');
const firstArg = f.readFileSync(process.argv[2]).toString();
const secondArg = f.readFileSync(process.argv[3]).toString();
f.writeFileSync(process.argv[4], firstArg + secondArg);
