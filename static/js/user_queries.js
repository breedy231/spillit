var userId, questionType;

var socket = io.connect('https://' + document.domain + ':' + location.port);
socket.on('connect', function() {
    socket.emit('message', "Someone new is on the site");
});
socket.on('response', function(data) {
    userId = data
    $("#userId").text(userId +"");
});
$('#addUserButton').click(function () {
    socket.emit('newUser', $('#nameTextField').val());
})

socket.on('questionSend', function(data) {
      console.log("user " + data);
    questionType = data[1];
});

$('#addResponseButton').click(function () {
    socket.emit('newResponse', [userId, questionType, $('#responseTextField').val()]);
})
