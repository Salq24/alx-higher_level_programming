#!/usr/bin/node

const { dict } = require('./101-data');

const occDict = {};

for (const userId in dict) {
  const occ = dict[userId];
  if (!occDict[occ]) {
    occDict[occ] = [];
  }
  occDict[occ].push(userId);
}
console.log(occDict);
