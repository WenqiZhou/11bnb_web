function initnav() {
    $("header nav a").each(function () {
        var url = $(this).attr("href");
        $(this).attr("href", "javascript:void(0);");
        $(this).attr("url", url);
    });
    $("header nav a").on("click", function () {
        var url = $(this).attr("url");
        $(".bor").animate({
            "left": ($(this).parent().index() ) * 25 + "%"
        }, 300, "", function () {
            location.href = url;
        });
    });
}


function isWeiXin() {
    var ua = window.navigator.userAgent.toLowerCase();
    if (ua.match(/MicroMessenger/i) == 'micromessenger') {
        return true;
    } else {
        return false;
    }
}
function getWidth(container,scale){
    var $imgBox = $(container);
    var deviceWidth = $(document).width();
    $imgBox.height(deviceWidth*scale);
}