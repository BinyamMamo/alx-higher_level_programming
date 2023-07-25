#!/usr/bin/node
const request = require('request');
const url = process.argv[2].replace('films', 'people') + '18';
request(url, (err, resp, body) => {
  if (err) { console.log(err); return; }
  console.log(JSON.parse(body).films.length);
});
