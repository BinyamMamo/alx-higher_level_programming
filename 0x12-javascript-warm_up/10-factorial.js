#!/usr/bin/node

function factorial (x) {
  if (x === 0 || x === 1)
    return (1);
  return (x * factorial(--x));
}

if (isNaN(process.argv[2]) || process.argv[2] === undefined || process.argv[2] === '') {
  console.log(1);
} else {
  console.log(factorial(parseInt(process.argv[2])));
}
