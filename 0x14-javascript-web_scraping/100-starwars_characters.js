#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const Actors = JSON.parse(body).characters;
  for (let i = 0; i < Actors.length; i++) {
    request(Actors[i], (error, response, body) => {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
