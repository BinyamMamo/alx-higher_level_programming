#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined || process.argv[2] === '') {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < parseInt(process.argv[2]); x++) {
    console.log('x'.repeat(parseInt(process.argv[2])));
  }
}
