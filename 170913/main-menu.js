$(document).ready(function() {
  var menu = $('.menu > li');
  // var span = $('.menu span');
  var last_item = $('.sub-menu li:last-child a');

  menu.hover(function() {
    $(this).find('.sub-menu').toggleClass('sub-menu-active');
  });
  menu.focusin(function() {
    $(this).find('.sub-menu').addClass('sub-menu-active');
  });
  last_item.focusout(function() {
    $(this).parents(".sub-menu").removeClass('sub-menu-active');
  });
  var tab = $('.tab');
  tab.on('click focusin', function() {
    $(this).parent().addClass('sub-menu-active')
      .siblings().removeClass('sub-menu-active');
  });
});