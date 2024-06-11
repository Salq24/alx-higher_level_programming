// fetches and lists the title for all movies by using this
// URL: https://swapi-api.alx-tools.com/api/films/?format=json

let link = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(link, function (data) {
  let movies = data.results;
  for (let movie of movies) {
    $('ul#list_movies').append(`<li>${movie.title}</li>`);
  }
});
