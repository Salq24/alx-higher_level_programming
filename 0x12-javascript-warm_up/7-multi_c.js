#!/usr/bin/node

const conv = process.argv[2];
const num = parseInt(conv);

if (!isNaN(num)) {
  for (let x = 0; x < num; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
