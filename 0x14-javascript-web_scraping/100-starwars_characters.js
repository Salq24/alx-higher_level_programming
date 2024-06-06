#!/usr/bin/node

const request = require('request');
const movieid = process.argv[2];
const link = `https://swapi.dev/api/films/${movieid}/`;

request.get(link, (err, response, data) => {
  if (err) {
    console.log(err);
    return;
  }

  const movie = JSON.parse(data);
  const xters = movie.characters;
  for (const xter of xters) {
    request(xter, (err, response, data) => {
      if (err) {
        console.log(err);
        return;
      }
      const xterdata = JSON.parse(data);
      console.log(xterdata.name);
    });
  }
});
