#!/usr/bin/node
/**
 * print square
 */
if (process.argv[2]) {
  if (Number(process.argv[2])) {
    let i = 0;
    while (i < Number(process.argv[2])) {
      let j = 0;
      let list = [];
      while (j < Number(process.argv[2])) {
        list.push('X');
        j++;
      }
      console.log(list.join(''));
      i++;
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
