#!/usr/bin/node

const conv = process.argv[2];
const num = parseInt(conv);

if (!isNaN(num)) {
  console.log('My number:',num);
} else {
  console.log('Not a number');
}
