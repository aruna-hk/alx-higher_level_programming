#!/usr/bin/node
//command line argument
let count = 0;
for (arg in process.argv) {
  if (count === 2) {
    console.log(process.argv[arg]);
    count++;
    break;
  }
  count++;
}
if (count === 2) {
  console.log('No argument');
}
