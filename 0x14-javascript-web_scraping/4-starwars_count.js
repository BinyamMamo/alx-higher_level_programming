#!/usr/bin/node
const request = require('request');
// const url =  process.argv[2] + '/18'; // films not people
const url = 'https://swapi-api.alx-tools.com/api/people/18';
request(url, (err, resp, body) => {
  if (err) { console.log(err); }
  console.log(JSON.parse(body).films.length);
});
