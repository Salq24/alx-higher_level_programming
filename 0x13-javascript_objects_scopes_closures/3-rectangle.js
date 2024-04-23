#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return ('Rectangle {}');
    }
    this.width = w;
    this.height = h;
  }

  print () {
    const rec = 'X'.repeat(this.width);
    for (let y = 0; y < this.height; y++) {
      console.log(rec);
    }
  }
}
module.exports = Rectangle;
