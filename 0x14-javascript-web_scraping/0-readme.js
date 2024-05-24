#!/usr/bin/node
/*
  javascipt sript to read file
*/
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, data) => {
    console.error(err || data);
});
