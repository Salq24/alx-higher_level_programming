#!/usr/bin/node

const request = require('request');
const movieid = process.argv[2];
const link = `https://swapi.dev/api/films/${movieid}/`;
let xters = [];

request(link, (err, response, data) => {
  if (err) {
    console.log(err);
    return;
  }

  const movie = JSON.parse(data);
  xters = movie.characters;
  xterget(0);
});

const xterget = (ind) => {
  if (ind === xters.length) {
    return;
  }
  request.get(xters, (err, response, data) => {
    if (err) {
      console.log(err);
      return;
    }
    const xterdata = JSON.parse(data);
    console.log(xterdata.name);
    xterget(ind + 1);
  });
};
