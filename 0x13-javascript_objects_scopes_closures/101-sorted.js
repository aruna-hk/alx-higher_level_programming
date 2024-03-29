#!/usr/bin/node
const dict = require('./101-data').dict;

const list = Object.entries(dict);
const values = Object.values(dict);
const uniqeValues = [...new Set(values)];
const Dict = {};
for (const i in uniqeValues) {
  const list_ = [];
  for (const j in list) {
    if (list[j][1] === uniqeValues[i]) {
      list_.unshift(list[j][0]);
    }
  }
  Dict[uniqeValues[i]] = list_;
}
console.log(Dict);
