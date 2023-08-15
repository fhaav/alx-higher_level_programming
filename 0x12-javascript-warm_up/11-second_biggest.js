#!/usr/bin/node
function secondB (args) {
  args = args.map(Number);

  if (args.length < 2) {
    return 0;
  }

  let maxnum = args[0];
  for (let i = 0; i < args.length; i++) {
    if (maxnum < args[i]) {
      maxnum = args[i];
    }
  }

  let secondn = args[0];
  for (let i = 0; i < args.length; i++) {
    if ((secondn === maxnum || secondn < args[i]) && args[i] !== maxnum) {
      secondn = args[i];
    }
  }

  return secondn;
}

const result = secondB(process.argv.slice(2));

console.log(result);
