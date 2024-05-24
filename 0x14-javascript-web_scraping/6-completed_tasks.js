#!/usr/bin/node

const req = require('request');
req(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const user = JSON.parse(body);
  const cuser = [];
  for (let i = 0; i < user.length; i++) {
    if (user[i].completed) {
      cuser.push(user[i]);
    }
  }
  const userAdict = {};
  for (let i = 0; i < cuser.length; i++) {
    const userAid = cuser[i].userId.toString();
    if (userAid in userAdict) {
      userAdict[userAid] = userAdict[userAid] + 1;
    } else {
      userAdict[userAid] = 1;
    }
  }
  console.log(userAdict);
});
