#!/usr/bin/node

const Arguments = process.argv.slice(2);

function secondLargest (args) {
  if (args.length <= 1) {
    return 0;
  }

  const numbers = args.map(arg => parseInt(arg));
  const sortedNum = numbers.sort((a, b) => b - a);
  const secLargest = sortedNum[1];
  return secLargest;
}

console.log(secondLargest(Arguments));
