#!/usr/bin/node

const SquareParent = require('./5-square');
class Square extends SquareParent {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let y = 0; y < this.size; y++) {
      console.log(`${c}`.repeat(this.size));
    }
  }
}
module.exports = Square;
