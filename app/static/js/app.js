$(document).ready(function () {
  namespace = '/etv';
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

  socket.on('connect', function () {
    socket.emit('my_event', {data: 'I\'m connected!'});
  });

  socket.on('countdown_response', function (msg) {
    $('#countdown-display').html(msg.countdown);
  });


  $('form#start-reset').submit(function (event) {
    socket.emit('start_reset_event', {data: $('#start-reset-data').val()});
    return false;
  });

  $('#stop').click(function (event) {
    socket.emit('stop_event');
    return false;
  });

  $('form#add').submit(function (event) {
    socket.emit('add_event', {data: $('#add-data').val()});
    return false;
  });

  $('form#subtract').submit(function (event) {
    socket.emit('subtract_event', {data: $('#subtract-data').val()});
    return false;
  });

  $('#add_minute').click(function (event) {
    socket.emit('add_event', {data: 1});
    return false;
  });

  $('#subtract_minute').click(function (event) {
    socket.emit('subtract_event', {data: 1});
    return false;
  });

});