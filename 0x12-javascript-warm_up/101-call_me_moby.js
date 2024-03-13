#!/usr/bin/node
//call and execute function some numeber of times
exports.callMeMoby = function(x, thefunction) {
  let i = 0;
  while (i < x) {
    thefunction();
    i++;
  }
}
