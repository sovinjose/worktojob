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

ruckusTool.controller("CreateJobProfileControeller", function($scope, $http, $location) {

    $scope.salary_error_msg = false

    $scope.start_date_model = (new Date()).toISOString().split(':')[0].split('T')[0]
    $scope.tomorrow = new Date();
    var offset = 28 * 24 * 60 * 60 * 1000;
    $scope.end_date_model = new Date($scope.tomorrow.getTime() + offset)
    $scope.time_diff = 28
    $scope.end_date_model = $scope.end_date_model.toISOString().split(':')[0].split('T')[0]

    $scope.change_date_diff = function(){
      $scope.date1 = new Date($scope.start_date_model);
      $scope.date2 = new Date($scope.end_date_model);
      $scope.time_diff = parseInt(( $scope.date2 -  $scope.date1) / (1000 * 60 * 60 * 24))
    }

    $scope.validate_salary_max = function(){
        if ($scope.salary_min <= $scope.salary_max){
            $scope.salary_error_msg = false
        }else{
            $scope.salary_max = null
            $scope.salary_error_msg = true
        }
    }

    $scope.validate_job_type = function(){

      if($scope.job_type == 'Temporary' ||  $scope.job_type == 'Internship' || $scope.job_type == 'Apprenticeship' || $scope.job_type == 'Volunteer'){
        return true
      }else
      return false

    }

});

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
              $location.url('/payment');
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



    $scope.processForm = function(){
      if(!$scope.myform.$valid) {
        $scope.profile_validation = true
      }else{
        $scope.profile_validation = false
        $scope.go_for_submit_form();
      }
    }



    $scope.go_for_submit_form = function() {

      console.log($scope.formData)
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





