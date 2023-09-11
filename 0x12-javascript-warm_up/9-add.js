#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const parsedInt1 = parseInt(process.argv[2]);
const parsedInt2 = parseInt(process.argv[3]);

if (!isNaN(parsedInt1) && !isNaN(parsedInt2)) {
  add(parsedInt1, parsedInt2);
} else {
  console.log('NaN');
}
