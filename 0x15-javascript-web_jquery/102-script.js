/* displays the translation of hello in the lang specified */
$(document).ready(function () {
    $('INPUT#btn_translate').click(function () {
        $.ajax({
          type: 'GET',
          url: 'https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(),
          success: (resp) => {
            $('DIV#hello').html(resp.hello);
          }
        });
    });
});

