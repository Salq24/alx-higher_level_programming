#!/usr/bin/node

const fsys = require('fs');
const filenm = process.argv[2];
const data = process.argv[3];

fsys.writeFile(filenm, data, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
