var userId, questionType;


var socket = io.connect('http://' + document.domain + ':' + location.port, {secure: true});
socket.on('connect', function() {
    socket.emit('message', "A user has opened the site");
});

socket.on('response', function(data) {
    userId = data;
    $("#userId").text(userId +"");
});

$(document).ready(function() {
    $(".waitGame").hide();
    $(".waitPlayers").hide();
    $(".response").hide();
});


$('#addUserButton').click(function () {
    socket.emit('newUser', $('#nameTextField').val());
    $(".pre").hide();
    $(".waitGame").show();
});

socket.on('questionSend', function(data) {
    console.log("user " + data[0]);
    questionType = data[1];
});


$('#sendResponseButton').click(function () {
    socket.emit('newResponse', [userId, questionType, $('#responseTextField').val()]);
    $(".response").hide();
    $(".waitPlayers").show();

});

socket.on('startGame', function(data) {
    $(".waitGame").hide();
    $(".response").show();
});
