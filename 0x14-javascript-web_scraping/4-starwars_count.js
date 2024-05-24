#!/usr/bin/node

const req = require('request');
const urlc = 'https://swapi-api.alx-tools.com/api/people/18/';

req(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  let count = 0;
  const data = JSON.parse(body);
  const movies = data.results;
  for (let i = 0; i < movies.length; i++) {
    if (movies[i].characters.includes(urlc)) {
      count = count + 1;
    }
  }
  console.log(count);
});
