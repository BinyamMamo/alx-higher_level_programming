#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occr = 0;
  list.forEach(element => {
    if (searchElement === element) {
      occr += 1;
    }
  });
  return (occr);
};
