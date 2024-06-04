#!/usr/bin/node

const request = require('request');
const link = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(link, (error, response, data) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(data);
    console.log(content.title);
  }
});
