#!/usr/bin/node

const request = require('request');
const process = require('process');
const movieId = process.argv[2];
const url = ('https://swapi.dev/api/films/' + movieId);
let charList = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const content = JSON.parse(body);
  charList = content.characters;
  charCall(0);
});

const charCall = (i) => {
  if (i === charList.length) {
    return;
  }

  request(charList[i], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const charContent = JSON.parse(body);
    console.log(charContent.name);
    charCall(i + 1);
  });
};
