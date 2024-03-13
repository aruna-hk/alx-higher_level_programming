#!/usr/bin/node
/**
 * js script to perfome addition
 */
function add(a, b) {
  return (Number(a) + Number(b));
}
console.log(add(process.argv[2], process.argv[3]));
