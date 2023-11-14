#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

const values = Object.values(dict);

values.forEach(item => {
  newDict[item] = [];
  for (const key of Object.keys(dict)) {
    if (dict[key] === item) {
      newDict[item].push(key);
    }
  }
});
console.log(newDict);
