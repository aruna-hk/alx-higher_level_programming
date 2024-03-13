#!/usr/bin/node
/**
 * js factorial function
 */
function fact(intn) {
  if (intn === 1 || !intn) {
    return 1;
  }
  return intn * fact(intn - 1);
}
console.log(fact(Number(process.argv[2])));
