#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  for (let i = 0; i < list.length; i++) {
    reversed.unshift(list[i]);
  }
  return reversed;
};
