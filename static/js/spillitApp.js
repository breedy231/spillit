//import "../static/css/style.less";

// create the module and name it spillitApp
var spillitApp = angular.module('spillitApp', ['ngRoute']);

// configure our routes
spillitApp.config(function($routeProvider) {
	$routeProvider

		// route for the home page
		.when('/', {
			templateUrl : '/templates/lobby.html',
			controller  : 'mainController'
		})

		// route for the about page
		.when('/submit', {
			templateUrl : '/templates/submit.html',
			controller  : 'aboutController'
		})

});

// create the controller and inject Angular's $scope
spillitApp.controller('mainController', function($scope) {

	// create a message to display in our view
	$scope.message = 'Everyone come and see how good I look!';
});

spillitApp.controller('aboutController', function($scope) {
	$scope.message = 'Look! I am an about page.';
});
