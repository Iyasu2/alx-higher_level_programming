#!/usr/bin/node

const parsedInt = parseInt(process.argv[2]);

if (isNaN(parsedInt)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parsedInt; i++) {
    console.log('C is fun');
  }
}
