$(document).ready(function(){



    $(function (){
        var ua = navigator.userAgent.toLowerCase();
        if(ua.match(/iphone/i)=="iphone" || ua.match(/android/i)=="android")
            {
                $(".hero .caption").css("top","40%");
             }
         else if(ua.match(/MicroMessenger/i)=="micromessenger")  
            {
                $(".hero .caption").css("top","70%");
                $("h4.properties").html('长按二维码关注公众号');
            }
         else
            {
                $(".erweima").css("margin-top","70px");
                $(".hero .caption").css("top","50%");
            }

        });



	/*  Hamburger Menu & Icon  */
	$('.hamburger').on('click', function(e){
		
		e.preventDefault();
		$(this).toggleClass('opned');
		$('header nav').toggleClass('active');
		
	});




	/*  Advanced search form & Icon  */
	$('#advanced_search_btn').on("click", function(e){
		e.preventDefault();

		var ads_box =$('.advanced_search');
		
		if(!ads_box.hasClass('advanced_displayed')){

			$(this).addClass('active');
			ads_box.stop().fadeIn(200).addClass('advanced_displayed');

		}else{

			$(this).removeClass('active');
			ads_box.stop().fadeOut(200).removeClass('advanced_displayed');

		}

	});




});

 function clicka()
		{
		var ua = navigator.userAgent.toLowerCase();
		 if(ua.match(/iphone/i)=="iphone" || ua.match(/android/i)=="android")
            {
                window.location.href="about-phone.html"; 
             }
         else if(ua.match(/MicroMessenger/i)=="micromessenger")  
            {
                window.location.href="about-phone.html"; 
            }
         else
            {
               window.location.href="about-pc.html"; 
            }
         }
