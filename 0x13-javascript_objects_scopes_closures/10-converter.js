#!/usr/bin/node
exports.converter = function (base) {
  return function (numb) {
    return parseInt(numb, 10).toString(base);
  };
};
