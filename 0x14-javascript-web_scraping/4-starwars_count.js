#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, resp, body) => {
  if (err) { console.log(err); return; }
  let count = 0;
  console.log(JSON.parse(body).results[0].characters);
  const results = JSON.parse(body).results;
  for (const film of results) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        ++count;
      }
    }
  }

  console.log(count);
});
