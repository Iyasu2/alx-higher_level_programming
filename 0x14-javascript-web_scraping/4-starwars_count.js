#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(response.statusCode);
  } else {
    const count = body.split('/people/18/').length - 1;

    console.log(count);
  }
});
