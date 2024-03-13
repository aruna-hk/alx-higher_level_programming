#!/usr/bin/node
//command line arguments
let arglen = process.argv.length;
if (arglen <= 2) {
  console.log('No arguments');
}
else if (arglen === 3){
  console.log('Argument found');
}
else {
  console.log('Arguments found');
}
