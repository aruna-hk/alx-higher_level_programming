#!/usr/bin/node

const req = require("request");
urlc = "https://swapi-api.alx-tools.com/api/people/18/"

req(process.argv[2], (error, response, body) => {
    let count = 0;
    let data = JSON.parse(body);
    let movies = data.results;
    for (let i = 0; i < movies.length; i++) {
        if (movies[i].characters.includes(urlc)) {
            count = count + 1;
        }
    }
    console.log(count);
});
