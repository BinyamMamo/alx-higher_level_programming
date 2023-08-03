/* gets data from an API and displays it in div#character */
const uri = "https://swapi.co/api/people/5/?format=json";
$.get(uri, (resp) => {
  $('div#character').text(resp.name);
});

