#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];
request(url, (err, resp, body) => {
  if (err) { console.log(err); return; }
  fs.writeFile(fileName, body, 'utf8', err => {
    if (err) console.log(err);
  });
});
