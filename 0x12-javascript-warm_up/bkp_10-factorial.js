#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined || process.argv[2] === '') {
  console.log(1);
} else {
  let y = 1;
  for (let x = parseInt(process.argv[2]); x > 0; x--) {
    y *= x;
  }
  console.log(y);
}
