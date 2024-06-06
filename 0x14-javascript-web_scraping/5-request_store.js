#!/usr/bin/node

const request = require('request');
const filesys = require('fs');
const link = process.argv[2];
const file = process.argv[3];

request(link, (err, response, data) => {
  if (err) {
    console.log(err);
  } else {
    filesys.writeFile(file, data, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
