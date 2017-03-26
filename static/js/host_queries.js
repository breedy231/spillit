var users = [];
var question, questionType;

var socket = io.connect('https://' + document.domain + ':' + location.port);
socket.on('connect', function() {
    socket.emit('message', "The host is connected!");
});
socket.on('response', function(data) {
    console.log(data);
    users.push(data);
    $("#users").text(users);
});

$(document).ready(function() {
    socket.emit('questionRequest', 'host is requesting a question');
});

socket.on('questionSend', function(data) {
    console.log(data);
    question = data[0];
    questionType = data[1];
    $("#question").text(data[0]);
});
