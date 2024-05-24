#!/usr/bin/node

const request = require('request');

async function fetchData (url) {
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
  try {
    const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';
    const body = await fetchData(url);
    const actors = JSON.parse(body).characters;

    for (let i = 0; i < actors.length; i++) {
      const actor = await fetchData(actors[i]);
      console.log(JSON.parse(actor).name);
    }
  } catch (error) {
    console.error(error);
  }
}

main();
