#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const one = parseInt(process.argv[2]);
const two = parseInt(process.argv[3]);

console.log(add(one, two));
