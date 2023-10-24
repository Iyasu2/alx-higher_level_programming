#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const charurl = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(response.statusCode);
  } else {
    const movie = JSON.parse(body).results;
    let count = 0;

    movie.forEach((film) => {
      if (film.characters.includes(charurl)) {
        count++;
      }
    });

    console.log(count);
  }
});
