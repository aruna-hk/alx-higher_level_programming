#!/usr/bin/node

const request = require('request');

async function fetchMovies (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function main () {
  const urlc = 'https://swapi-api.alx-tools.com/api/people/18/';
  let count = 0;
  const response = await fetchMovies(process.argv[2]);
  const movies = JSON.parse(response).results;
  for (let i = 0; i < movies.length; i++) {
    if (movies[i].characters.includes(urlc)) {
      count = count + 1;
    }
  }
  console.log(count);
}

main();
