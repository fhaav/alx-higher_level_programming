#!/usr/bin/node
function secondB (args) {
  args = args.map(Number);

  if (args.length <= 2) {
    return 0;
  }

  let firstMax = Math.max(args[0], args[1]);
  let secondMax = Math.min(args[0], args[1]);

  for (let i = 2; i < args.length; i++) {
    if (args[i] > firstMax) {
      secondMax = firstMax;
      firstMax = args[i];
    } else if (args[i] > secondMax && args[i] !== firstMax) {
      secondMax = args[i];
    }
  }

  return secondMax;
}

const result = secondB(process.argv.slice(2));

console.log(result);
