function IndexPage($scope) {
	this.msg = 'test';
	this.term = "aaa";
	$scope.$watch(() => this.term, (value) => console.log(value));

}

var app = angular.module('mainApp', ['ngRoute'])
.config(['$routeProvider', '$locationProvider',
  function($routeProvider, $locationProvider) {
    $routeProvider
      // .when('/Book/:bookId', {
      //   templateUrl: 'book.html',
      //   controller: 'BookCtrl',
      //   controllerAs: 'book'
      // })
      .when('/', {
        templateUrl: '/st/index.ng',
        controller: 'IndexPage',
        controllerAs: 'ctrl'
      })
      .otherwise({redirectTo:'/'});

    $locationProvider.html5Mode(true);
}])
.controller('IndexPage', ['$scope', IndexPage])