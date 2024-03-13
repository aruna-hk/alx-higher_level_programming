#!/usr/bin/node
/**
 * command line arguments
 */
let str = 'My number: ';
number = Number(process.argv[2]);
if (!number) {
  console.log(str + 'Not a Number');
}
else{
  console.log(str + number);
}
