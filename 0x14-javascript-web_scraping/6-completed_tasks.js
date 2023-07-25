#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2] + '?completed=true';

request(url, (err, resp, body) => {
  if (err) { console.log(err); return; }
  const todos = JSON.parse(body);
  let todo_dict = {};
  for (const todo of todos) {
    if (todo.userId in todo_dict) {
      todo_dict[todo.userId] += 1;
    } else {
      todo_dict[todo.userId] = 1;
    }
  }
  console.log(todo_dict);
});
