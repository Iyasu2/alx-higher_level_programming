#!/usr/bin/node

function findSecondLargest (numbers) {
  if (numbers.length === 0 || numbers.length === 1) {
    console.log(0);
    return;
  }

  let largest = Number.MIN_SAFE_INTEGER;
  let secondLargest = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < numbers.length; i++) {
    const currentNumber = numbers[i];

    if (currentNumber > largest) {
      secondLargest = largest;
      largest = currentNumber;
    } else if (currentNumber > secondLargest && currentNumber < largest) {
      secondLargest = currentNumber;
    }
  }

  if (secondLargest === Number.MIN_SAFE_INTEGER) {
    console.log('There is no second largest number.');
  } else {
    console.log(secondLargest);
  }
}

const args = process.argv.slice(2).map(Number);

findSecondLargest(args);
