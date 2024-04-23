#!/usr/bin/node

exports.esrever = function (list) {
  const listRev = [];
  for (let y = list.length - 1; y >= 0; y--) {
    listRev.push(list[y]);
  }
  return listRev;
};
