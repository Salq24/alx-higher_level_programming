#!/usr/bin/node

value = process.argv[2];
if (!value) {
  console.log('No argument');
} else {
  console.log(value);
}
