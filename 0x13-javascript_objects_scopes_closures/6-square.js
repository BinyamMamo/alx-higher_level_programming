#!/usr/bin/node

const SquareParent = require('./5-square');
class Square extends SquareParent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let y = 0; y < super.width; y++) {
      console.log(`${c}`.repeat(super.height));
    }
  }
}
module.exports = Square;
