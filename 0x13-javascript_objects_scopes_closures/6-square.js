#!/usr/bin/node

const squareOne = require('./5-square');

class Square extends squareOne {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    const sqr = c.repeat(this.width);
    for (let y = 0; y < this.height; y++) {
      console.log(sqr);
    }
  }
}

module.exports = Square;
