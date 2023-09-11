#!/usr/bin/node

const parsedInt = parseInt(process.argv[2]);

if (!isNaN(parsedInt)) {
  console.log('My number:', parsedInt);
} else {
  console.log('Not a number');
}
