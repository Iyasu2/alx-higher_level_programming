#!/usr/bin/node

const parsedInt = parseInt(process.argv[2]);
let output = '';

if (isNaN(parsedInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parsedInt; i++) {
    for (let j = 0; j < parsedInt; j++) {
      output += 'X';
    }
    console.log(output);
    output = '';
  }
}
