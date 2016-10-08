/**
 * Index page view controller.
 */
function IndexPage($location, apiService) {
	this.location = $location;
  this.apiService = apiService;

  this.selectedItem = null;
  this.searchText = "";
  this.selectedGenes = [];
  this.showSearchButton = true;
}
IndexPage.prototype.querySearch = function(q) {
  return this.apiService.getSuggestions(q).then(function(data) {
    return data;
  });
};

// IndexPage.prototype.searchTextChange = function(value) {
//   // console.log("searchTextChange:", value);
// };

// IndexPage.prototype.transformChip = function(chip) {
//   console.log("transformChip:", chip);
// };
IndexPage.prototype.submitSearch = function() {
  console.log("submitSearch:", this.selectedGenes);
  if (this.selectedGenes.length > 0) {
    var params = this.selectedGenes.join(",");
    console.log("move to", params)
    this.location.url("/g/" + params);
  }
};

/**
 * Gene variants view controller.
 */
function GeneCtrl($routeParams, $location, apiService) {
  this.apiService = apiService;
  this.location = $location;

  this.query = $routeParams.gene;
  this.header = [];
  this.variants = [];

  this.selectedItem = null;
  this.searchText = "";
  this.selectedGenes = this.query ? this.query.split(",") : [];
  this.showSearchButton = false;

  this.apiService
    .getVariants(this.query)
    .then(angular.bind(this, function(data) {
      this.header = data.header;
      this.variants = data.variants;
    }));
}
GeneCtrl.prototype.querySearch = function(q) {
  return this.apiService.getSuggestions(q).then(function(data) {
    return data;
  });
};
GeneCtrl.prototype.onAddChip = function(chip) {
  console.log("onAddChip:", chip);
  this.location.url("/g/" + this.selectedGenes.join(","));
};
GeneCtrl.prototype.onRemoveChip = function(chip) {
  console.log("onRemoveChip:", chip);
  this.location.url("/g/" + this.selectedGenes.join(","));
};

/**
 * ApiService
 */
function ApiService($http) {
  this.http = $http;
}
ApiService.prototype.getSuggestions = function(q) {
  return this.http.get("/api/v1/suggest", {params: {genes: q}}).then(function(response) {
    return response.data;
  })
}
ApiService.prototype.getVariants = function(q) {
  return this.http.get("/api/v1/variants", {params: {q: q}}).then(function(response) {
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
        controllerAs: "ctrl"
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
.controller("GeneCtrl", ["$routeParams", "$location", "ApiService", GeneCtrl]);
