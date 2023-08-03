/* gathers data from url using ajax and displays it on div#hello */
$(document).ready(() => {
$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: (resp) => {
    $('div#hello').text(resp.hello);
  }
});
});

