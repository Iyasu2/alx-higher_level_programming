#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(response.statusCode);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    let currentIndex = 0;

    const retrieveCharacter = () => {
      if (currentIndex >= characters.length) {
        return;
      }

      const characterUrl = characters[currentIndex];

      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else if (response.statusCode !== 200) {
          console.error(response.statusCode);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }

        currentIndex++;
        retrieveCharacter();
      });
    };
    retrieveCharacter();
  }
});
