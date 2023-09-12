#!/usr/bin/node

function computeFactorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0) {
    return 1;
  }

  return n * computeFactorial(n - 1);
}

const arg = parseInt(process.argv[2]);

console.log(computeFactorial(arg));