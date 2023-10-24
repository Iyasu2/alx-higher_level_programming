#!/usr/bin/node

const request = require('request');

const apiurl = process.argv[2];
const url = `${apiurl.replace('/films', '/people/18')}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(response.statusCode);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.films.length);
  }
});
