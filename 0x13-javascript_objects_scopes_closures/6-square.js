#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let ch = '';
      for (let j = 0; j < this.width; j++) {
        ch += c;
      }
      console.log(ch);
    }
  }
}

module.exports = Square;
