function initnav() {

    var ua = navigator.userAgent;
    $("header nav a").each(function () {
        var url = $(this).attr("href");
        $(this).attr("href", "javascript:void(0);");
        $(this).attr("url", url);
    });
    $("header nav a").on("click", function () {
        var index = $(this).parent().index();
        var url = $(this).attr("url");
        $(".bor").animate({
            "left": ($(this).parent().index() ) * 25 + "%"
        }, 300, "", function () {
            navtimer();
            location.href = url;
        });
        if (ua.indexOf('Safari') > -1 && !(ua.indexOf('Chrome') > -1)) {
            var _location = url.split('/');
            var addClass = _location[_location.length - 1].split('.')[0];
            $('.bor').addClass(addClass);
            setTimeout(function () {
                location.href = url;
            }, 300);
        } else {

            $(".bor").animate({
                "left": (index ) * 25 + "%"
            }, 300, "", function () {
                location.href = url;
            });
        }
    });

}
//function initnav() {
//    var ua = navigator.userAgent;
//    if(ua.indexOf('Safari') > -1 && !(ua.indexOf('Chrome') > -1)){
//        var list = [];
//        $('nav a').each(function(index,ele){
//
//            list.push($(this).attr('href'));
//        });
//
//
//        })
//    }else{
//        $("header nav a").each(function () {
//            var url = $(this).attr("href");
//            $(this).attr("href", "javascript:void(0);");
//            $(this).attr("url", url);
//        });
//        $("header nav a").on("click", function () {
//            var url = $(this).attr("url");
//            $(".bor").animate({
//                "left": ($(this).parent().index() ) * 25 + "%"
//            }, 300, "", function () {
//                location.href = url;
//            });
//        });
//    }
//
//}


function isWeiXin() {
    var ua = window.navigator.userAgent.toLowerCase();
    if (ua.match(/MicroMessenger/i) == 'micromessenger') {
        return true;
    } else {
        return false;
    }
}
function getWidth(container, scale) {
    var $imgBox = $(container);
    var deviceWidth = $(document).width();
    $imgBox.height(deviceWidth * scale);
}


function navtimer() {
    var left = $(".bor").css("left");
    var _this = this;
    _this.run = function () {
        _this.timer = setInterval(function () {
            $(".bor").css("left", left);
            console.log(123);
        }, 1000);
    }
    _this.sleep = function () {
        clearInterval(_this.timer);
        setTimeout(_this.run, 2000);
    }
}
