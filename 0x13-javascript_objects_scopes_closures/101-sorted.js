#!/usr/bin/node
const dict = require('./101-data').dict;

const list = Object.entries(dict);
const values = Object.values(dict);
const uniqe_values = [...new Set(values)];
const Dict = {};
for (const i in uniqe_values) {
  const list_ = [];
  for (const j in list) {
    if (list[j][1] === uniqe_values[i]) {
      list_.unshift(list[j][0]);
    }
  }
  Dict[uniqe_values[i]] = list_;
}
console.log(Dict);
