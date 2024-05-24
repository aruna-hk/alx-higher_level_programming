#!/usr/bin/node
/*
 * read response status code
 */
const request = require("request");
request(process.argv[2], (error, response, body) => {
    console.log("code:",response.statusCode);
});
