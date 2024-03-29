#!/usr/bin/node
const dict = require('./101-data').dict;

const list = Object.entries(dict);
const values = Object.values(dict);
const uniqe_values = [...new Set(vals)];
const Dict = {};
for (const i in uniqe_values) {
  const list_ = [];
  for (const j in list) {
    if (list[k][1] === uniqe_values[j]) {
      list_.unshift(list[k][0]);
    }
  }
  Dict[valsUniq[j]] = list_;
}
console.log(Dict);
