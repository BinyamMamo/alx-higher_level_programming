#!/usr/bin/node

const SquareParent = require('./5-square');
class Square extends SquareParent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let y = 0; y < this.width; y++) {
      console.log(`${c}`.repeat(this.height));
    }
  }
}
module.exports = Square;
