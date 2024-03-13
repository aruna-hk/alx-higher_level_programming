#!/usr/bin/node
//command line argument
let count = 0;
for (const arg of process.argv) {
  if (count === 2) {
    console.log(arg);
    count++;
    break;
  }
  count++;
}
if (count === 2) {
  console.log('No argument');
}
