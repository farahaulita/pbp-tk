$(document).ready(function(){
    $(window).scroll(function(){
        var scroll = $(window).scrollTop();
        if (scroll > 1) {
          $(".navbar").css("background-color" , "blue");
        }
  
        else{
            $(".navbar").css("background-color" , "#333333");  	
        }
    })
  })