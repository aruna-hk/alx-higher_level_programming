#!/usr/bin/node

const f = require('fs');
const f1_c = f.readFileSync(process.argv[2]).toString();
const f2_c = f.readFileSync(process.argv[3]).toString();
f.writeFileSync(process.argv[4], f1_c + f2_c);
