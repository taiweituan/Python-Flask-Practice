angular.module('mainApp', [
    'ngRoute',
    'ngCookies'
])

.config(['$interpolateProvider', function($interpolateProvider) {
    // avoid conflict with flask's double brace
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
}])

.controller('mainController', ['$scope', function($scope){
    console.log('main controller');
    
    $scope.list = ['1','2','3'];

    console.log('tewr');
}])
;