var ruckusTool	 = angular.module('workTojob', ['ngRoute']);


ruckusTool.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});



ruckusTool.config(function($routeProvider) {
    $routeProvider
        .when('/view1', {
          templateUrl: '/static/pages/create_basic_details.html',
          controller: 'CreateProfileTab1Controeller'
        })
        .when('/view2', {
          templateUrl: '/static/pages/create_tab2.html',
          controller: 'CreateProfileTab2Controeller'
        })
        .when('/view3', {
          templateUrl: '/static/pages/create_tab3.html',
          controller: 'CreateProfileTab3Controeller'
        })
        .otherwise({
          redirectTo: '/'
        });
});

ruckusTool.controller("JobDetailPage", function($scope, $http) {
    $scope.close_job_position_popup = function() {
        $('#myModal').modal('show');
    }
})



ruckusTool.controller("CreateProfileTab1Controeller", function($scope, $http, $location) {

    $scope.tabActiveStatus = { 'first':true, 'second':false, 'last':false,}

    $scope.submitProfile = function() {
        console.log('>>>>>>>>>>>>>>>>>>>>>>>>', this.formData)
        url = '/create/user/profile'
        $scope.submitDataToAjax(this.formData, url)
        $location.url('/view2');
    }

    $scope.submitDataToAjax = function(form_data, url){
      $http.defaults.headers.post['X-CSRFToken'] = document.querySelector('[name="csrfmiddlewaretoken"]').value;
      $http({
            method: "POST",
            data: form_data,
            url:url,
            

      }).success(function(data){
                console.log('>>>>>>>>>>>>>>>>>>>>>>>>>>>' ,data.status)
      }).error(function(data, status, headers, config) {});

    }

    $location.url('/view1');


})


ruckusTool.controller("CreateProfileTab2Controeller", function($scope, $http, $location) {



    $scope.tabActiveStatus['first'] = false
    $scope.tabActiveStatus['second'] = true

    console.log($scope.tab2ActiveStatus, $scope.tab1ActiveStatus)

    $scope.submitProfile = function() {
        console.log('>>>>>>>>>>>>>>>>>>>>>>>>', this.formData)
        url = 'update/user/profile'
        $scope.submitDataToAjax(this.formData, url)
        $location.url('/view3');
    }

    $location.url('/view2');
})

ruckusTool.controller("CreateProfileTab3Controeller", function($scope, $http, $location) {


    $scope.tabActiveStatus['first'] = false
    $scope.tabActiveStatus['second'] = false
    $scope.tabActiveStatus['last'] = true

    $scope.submitProfile = function() {
        url = 'update/user/profile'
        $scope.submitDataToAjax(this.formData, url)
    }

    $location.url('/view3');
})








