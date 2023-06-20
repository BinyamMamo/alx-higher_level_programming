#!/usr/bin/node
const argc = process.argv.length;
if (argc <= 4) {
  console.log(0);
} else {
  let max = 0;
  let secMax = 0;
  for (let x = 2; x < argc; x++) {
    if (process.argv[x] > max) {
      max = process.argv[x];
    }
  }
  for (let x = 2; x < argc; x++) {
    if (process.argv[x] > secMax && process.argv[x] !== max) {
      secMax = process.argv[x];
    }
  }
  console.log(secMax);
}
