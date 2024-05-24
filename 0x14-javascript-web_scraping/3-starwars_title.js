#!/usr/bin/node

const req = require("request");

url = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];

req(url, (error, response, body) => {
    if (error) {
        console.log(error);
        return;
    }
    if (response.statusCode != 200) {
        return;
    }
    movies = JSON.parse(body);
    console.log(movies.title);
});
