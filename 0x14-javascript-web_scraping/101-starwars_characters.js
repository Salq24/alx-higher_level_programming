#!/usr/bin/node

const request = require('request');
const movieid = process.argv[2];
const link = `https://swapi.dev/api/films/${movieid}/`;

request.get(link, (err, response, data) => {
  if (err) {
    console.log(err);
  } else {
    const movie = JSON.parse(data);
    const xters = movie.characters;
    for (const xter of xters) {
      request.get(xter, (err, response, data) => {
        if (err) {
          console.log(err);
        } else {
          const xterdata = JSON.parse(data);
          console.log(xterdata.name);
        }
      });
    }
  }
});
