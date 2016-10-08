function IndexPage($location, apiService) {
	this.location = $location;
  this.apiService = apiService;

  this.selectedItem = null;
  this.searchText = "";
}

IndexPage.prototype.selectedItemChange = function(item) {
  console.log("selectedItemChange:", item);
  if (item && item.value) {
    this.location.url("/g/" + item.value);
  }
}

IndexPage.prototype.querySearch = function(q) {
  return this.apiService.getSuggestions(q).then(function(data) {
    return data.map(function(n) {
      return {
        value: n,
        display: n
      }
    });
  });
}

IndexPage.prototype.searchTextChange = function(value) {
  // console.log("searchTextChange:", value);
}

function GeneCtrl($routeParams, apiService) {
  this.apiService = apiService;
  this.gene = $routeParams.gene;
}

function ApiService($http) {
  this.http = $http;
}
ApiService.prototype.getSuggestions = function(q) {
  return this.http.get("/api/v1/suggest", {params: {genes: q}}).then(function(response) {
    return response.data;
  })
}

angular.module("MainApp", [
  "ngRoute",
  "ngMaterial",
  "ngMessages",
])
.config(["$routeProvider", "$locationProvider",
  function($routeProvider, $locationProvider) {
    $routeProvider
      .when("/g/:gene", {
        templateUrl: "/st/gene.ng",
        controller: "GeneCtrl",
        controllerAs: "geneCtrl"
      })
      .when("/", {
        templateUrl: "/st/index.ng",
        controller: "IndexPage",
        controllerAs: "ctrl"
      })
      .otherwise({redirectTo:'/'});

    $locationProvider.html5Mode(true);
}])
.service("ApiService", ["$http", ApiService])
.controller("IndexPage", ["$location", "ApiService", IndexPage])
.controller("GeneCtrl", ["$routeParams", "ApiService", GeneCtrl]);
