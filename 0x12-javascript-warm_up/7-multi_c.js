#!/usr/bin/node

const firstArg = process.argv[2];
const num = parseInt(firstArg);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let loopNum = 0;

  while (loopNum < num) {
    console.log('C is fun');
    loopNum++;
  }
}
