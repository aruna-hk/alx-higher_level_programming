#!/usr/bin/node
/**
 * increment and call display
 */
exports.addMeMaybe = function(number, thefunction) {
  number++;
  thefunction(number);
}
