#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  for (let y = 0; y < list.length; y++) {
    if (list[y] === searchElement) {
      cnt++;
    }
  }
  return cnt;
};
