#!/usr/bin/node

const conv = process.argv[2];
const num = parseInt(conv);
const sq = 'X'

if (!isNaN(num)) {
  for (let x = 0; x < num; x++) {
    console.log(sq.repeat(num));
  }
} else {
  console.log('Missing size');
}
