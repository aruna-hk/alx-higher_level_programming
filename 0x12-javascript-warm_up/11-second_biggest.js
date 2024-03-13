#!/usr/bin/node
/**
 * find the largest int in a list
 */
if (process.argv.length <= 2) {
	console.log(0)
} else {
  let secondl = Number(process.argv[2]);
  for (let i = 3; i < process.argv.length - 1; i++) {
    let n1 = Number(process.argv[i]);
    let n2 = Number(process.argv[i + 1]);
    if (n1 < secondl && n2 < secondl) {
       if (n1 < n2) {
         secondl = n2 
       } else { 
           secondl = n1
       }
    }
    if (n1 > secondl && n2 > secondl) {
       if (n1 > n2) {
         secondl = n2
       } else {
           secondl = n1
      }
    }
  console.log(secondl);
  }
  console.log(secondl);
}
