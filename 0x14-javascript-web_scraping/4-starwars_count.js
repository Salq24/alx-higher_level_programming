#!/usr/bin/node

const request = require('request');
const link = process.argv[2];
let cnt = 0;

request.get(link, (error, response, data) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(data);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          cnt += 1;
        }
      });
    });
    console.log(cnt);
  }
});
