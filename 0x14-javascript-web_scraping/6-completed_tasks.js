#!/usr/bin/node
/**
 * makes a request to a specified URL and retrieves data
 * parses the response body as JSON and
 * creates a dictionary called `todoDict`
 */
const request = require('request');
const url = process.argv[2] + '/';

request(url, (err, resp, body) => {
  if (err) { console.log(err); return; }
  const todos = JSON.parse(body);
  const todoDict = {};
  for (const todo of todos) {
    if (todo.completed) {
      if (todo.userId in todoDict) {
        todoDict[todo.userId] += 1;
      } else {
        todoDict[todo.userId] = 1;
      }
    }
  }
  console.log(todoDict);
});
