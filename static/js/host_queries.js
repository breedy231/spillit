var users = [], responses = [], emotions=[];
var question, questionType;

var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function() {
    socket.emit('message', "The host is connected!");
});

socket.on('response', function(data) {
    console.log(data);
    users.push(data);
    $("#users").text(users);
});

$(document).ready(function() {
    //socket.emit('questionRequest', 'host is requesting a question');
    $('#evaluateEmotionButton').hide();
});

$('#startGameButton').click(function () {
    socket.emit('startGame', 'host started game');
    socket.emit('questionRequest', 'host is requesting a question');
})

$('#evaluateEmotionButton').click(function () {
    users.forEach(function(userid) {
      console.log(userid);
      socket.emit('evaluateEmotion', userid +"");
    });
})

socket.on('sendingEmotion', function(response) {
    console.log(response);
    emotions.push(response);
    $("#emotions").text(emotions);
});

socket.on('startGame', function(data) {
    $('#startGameButton').hide();
    $('#evaluateEmotionButton').show();
});

socket.on('newResponse', function(response) {
    console.log(response);
    responses.push(response[2]);
    $("#responses").text(responses);
});

socket.on('questionSend', function(data) {
    console.log(data);
    question = data[0];
    questionType = data[1];
    $("#question").text(data[0]);
});
