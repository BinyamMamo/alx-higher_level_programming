#!/usr/bin/node
const argc = process.argv.length;
if (argc <= 3) {
  console.log(0);
} else {
  let max = Number.NEGATIVE_INFINITY;
  let secMax = Number.NEGATIVE_INFINITY;
  for (let x = 2; x < argc; x++) {
    if (parseInt(process.argv[x]) > max) {
      max = parseInt(process.argv[x]);
    }
  }
  for (let x = 2; x < argc; x++) {
    if (parseInt(process.argv[x]) > secMax && parseInt(process.argv[x]) !== max) {
      secMax = parseInt(process.argv[x]);
    }
  }
  console.log(secMax);
}
