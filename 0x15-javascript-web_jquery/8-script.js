/* gets data from an API and displays it in a list */
const uri = "https://swapi-api.alx-tools.com/api/films/?format=json";
$.get(uri, (resp) => {
  for (const film of resp.results) {
    $('ul#list_movies').append('<li>' + film.title + '</li>');
  }
});

