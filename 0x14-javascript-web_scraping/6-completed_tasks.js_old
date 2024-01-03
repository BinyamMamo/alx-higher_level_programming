#!/usr/bin/node
const request = require('request');
const url = process.argv[2] + '?completed=true';

request(url, (err, resp, body) => {
  if (err) { console.log(err); return; }
  const todos = JSON.parse(body);
  const todoDict = {};
  for (const todo of todos) {
    if (todo.userId in todoDict) {
      todoDict[todo.userId] += 1;
    } else {
      todoDict[todo.userId] = 1;
    }
  }
  console.log(todoDict);
});
