#!/usr/bin/node
function factorial (b) {
  if (isNaN(b) || b === 1) {
    return 1;
  }
  return b * factorial(b - 1);
}

const result = factorial(parseInt(process.argv[2]));

console.log(result);
