#!/usr/bin/node
/*
 * read response status code
 */
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log('code:', response.statusCode);
});
