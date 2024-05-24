#!/usr/bin/node

const request = require('request');
const urlc = 'https://swapi-api.alx-tools.com/api/people/18/';
request(process.argv[2], (error, response, body) => {
  if (error) {
    return;
  }
  let count = 0;
  const movies = JSON.parse(body).results;
  for (let i = 0; i < movies.length; i++) {
    if (movies[i].characters.includes(urlc)) {
      count = count + 1;
    }
  }
  console.log(count);
});
