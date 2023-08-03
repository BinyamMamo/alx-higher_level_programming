/* adds a 'li' element to the ul_my_lis tag */
$('div#add_item').click(() => {
  $('ul.my_list').append('<li>item</li>');
});

