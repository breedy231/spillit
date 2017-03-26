//import "../static/css/style.less";

// create the module and name it spillitApp
var spillitApp = angular.module('spillitApp', ['ngRoute']);

// configure our routes
spillitApp.config(function($routeProvider, $locationProvider) {
	$routeProvider

		// route for the home page
		.when('/', {
			templateUrl : '/',
			controller  : 'mainController'
		})
//		.when('/lobby', {
//			templateUrl : 'templates/lobby.html',
//			controller  : 'aboutController'
//		})
//
//		// route for the about page
//		.when('/submit', {
//			templateUrl : 'templates/submit.html',
//			controller  : 'aboutController'
//		})

	$locationProvider.html5Mode(true);
});

spillitApp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('({(');
    $interpolateProvider.endSymbol(')})');
});

// create the controller and inject Angular's $scope
spillitApp.controller('mainController', function($scope) {
	// create a message to display in our view
	this.message = 'Everyone come and see how good I look!';
	    console.log(this);

});

spillitApp.controller('aboutController', function($scope) {
	$scope.message = 'Look! I am an about page.';
});
