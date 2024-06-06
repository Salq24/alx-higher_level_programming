#!/usr/bin/node

const request = require('request');
const link = process.argv[2];

request.get(link, { json: true }, (err, response, data) => {
  if (err) {
    console.log(err);
    return;
  }

  const completedTasks = {};
  data.forEach((toDo) => {
    if (toDo.completed) {
      if (!completedTasks[toDo.userId]) {
        completedTasks[toDo.userId] = 1;
      } else {
        completedTasks[toDo.userId] += 1;
      }
    }
  });
  console.log(completedTasks);
});
