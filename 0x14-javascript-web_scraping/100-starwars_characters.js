#!/usr/bin/node
/* makes a request to the Star Wars API (SWAPI) 
to retrieve information about a specific movie. */
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/${movieId}/';

request(url, (err, resp, body) => {
  if (err) { console.log(err); return; }

  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request(character, (e, res, b) => {
      if (e) { console.log(e); return; }
      console.log(JSON.parse(b).name);
    });
  }
});
