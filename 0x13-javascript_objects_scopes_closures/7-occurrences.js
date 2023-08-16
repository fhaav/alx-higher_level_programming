#!/usr/bin/node

exports.nbOccurences = (list, searchElement) => list.reduce((count, el) => count + (el === searchElement), 0);
