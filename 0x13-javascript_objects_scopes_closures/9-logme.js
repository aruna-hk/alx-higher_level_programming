#!/usr/bin/node
let argno = 0;

exports.logMe = function (item) {
  console.log(argno + ': ' + item);
  argno++;
};
