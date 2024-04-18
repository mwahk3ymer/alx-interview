#!/usr/bin/node

// Importing required modules
const request = require('request');

// Function to fetch and print characters of a Star Wars movie
function printCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;
    request(url, (error, response, body) => {
        if (!error && response.statusCode === 200) {
            const film = JSON.parse(body);
            console.log(`Characters in ${film.title}:`);
            film.characters.forEach((characterUrl) => {
                request(characterUrl, (error, response, body) => {
                    if (!error && response.statusCode === 200) {
                        const character = JSON.parse(body);
                        console.log(character.name);
                    } else {
                        console.error(`Failed to fetch character: ${error}`);
                    }
                });
            });
        } else {
            console.error(`Failed to fetch movie: ${error}`);
        }
    });
}

// Extracting movie ID from command-line arguments
const movieId = process.argv[2];

// Printing characters of the specified movie
if (movieId) {
    printCharacters(movieId);
} else {
    console.error('Please provide the Movie ID as a command-line argument.');
}
