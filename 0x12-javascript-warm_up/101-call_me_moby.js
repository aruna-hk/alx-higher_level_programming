#!/usr/bin/python3
/**
 * execute function several times
 */
exports.callMeMoby = function(x, thefunction) {
  let i = 0;
  while (i < x) {
    thefunction();
    i++;
  }
}
