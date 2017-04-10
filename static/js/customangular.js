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



ruckusTool.config(function($routeProvider) {

  $routeProvider
      .when('/profile', {
        templateUrl: '/static/pages/form-profile.html',
        controller: 'profileFormController'
      })
      .when('/interests', {
        templateUrl: '/static/pages/form-interests.html',
        controller: 'companyFormController'
      })        
      .when('/payment', {
        templateUrl: '/static/pages/form-payment.html',
        controller: 'submitFormController'
      })
      .otherwise({
        redirectTo: '/profile'
  });

})



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

ruckusTool.controller("CreateJobProfileControeller", function($scope, $http, $location) {});

ruckusTool.controller("registorFormController", function($scope, $http, $rootScope, $location) {

    $scope.location = $location.path();
    $rootScope.$on('$routeChangeSuccess', function() {
        $scope.location = $location.path();
    });
    // we will store all of our form data in this object
    $scope.formData = {};
    // function to process the form


});


ruckusTool.controller('profileFormController', function($scope, $http, $location) {
    $scope.profile_validation = false
    $scope.message_status = false
    $scope.go_to_intrest = function(){
      if(!$scope.myform.$valid) {
        $scope.profile_validation = true
      }else{
        $scope.check_username_existance($scope.formData.email)
        $scope.profile_validation = false
      }
    }

    $scope.check_username_existance = function(username){
        url = '/register/check/'+$scope.formData.email+'/availability'
        $http({
              method: "get",
              url:url,
        }).success(function(data){
            if(data.status == true){
              $scope.message_status = true
              $scope.error_message = 'the email already exists.'
            }else{
              $scope.message_status = false
              $location.url('/interests');
            }
        }).error(function(data, status, headers, config) {});

    }
});

ruckusTool.controller('companyFormController', function($scope, $controller, $location) {
    $scope.profile_validation = false
    
    $scope.go_to_intrest = function(){
      if(!$scope.myform.$valid) {
        $scope.profile_validation = true
      }else{
        $scope.profile_validation = false
        $location.url('/payment');
      }
    }
   if($scope.formData.email==undefined){
      $location.url('/profile');
    } 
});


ruckusTool.controller('submitFormController', function($scope, $http, $location) {

   if($scope.formData.email==undefined){
      $location.url('/profile');
    } 
    $scope.processForm = function() {
      url = '/register/create/company/profile'
      $http.defaults.headers.post['X-CSRFToken'] = document.querySelector('[name="csrfmiddlewaretoken"]').value;
      $http({
            method: "POST",
            data: $scope.formData,
            url:url,
      }).success(function(data){
          window.location.assign("/");

      }).error(function(data, status, headers, config) {});
    };
});





