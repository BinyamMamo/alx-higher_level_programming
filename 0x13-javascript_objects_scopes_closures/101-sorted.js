#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = dict.map((key, value) => value * key);

console.log(newDict);
