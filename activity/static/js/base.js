/**
 * Created by tuobaocheng on 16/6/15.
 */

//百度统计
var _hmt = _hmt || [];
(function () {
    var hm = document.createElement("script");
    hm.src = "//hm.baidu.com/hm.js?ba4bfbfa549e4b97b31d472281fe3377";
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(hm, s);
})();

//微信分享
(function ($) {
    var URL_GET_SIGNATURE = "/app/genWXSignature";

    function mkcburl(url) {
        return url;
    }

    function initWxFxImpl(fxdata, rep, n, debug, cburl) {
        $.ajax({
            url: URL_GET_SIGNATURE, data: JSON.stringify({
                "url": decodeURIComponent(location.href)
            }),
            type: "post", dataType: "json",
            success: function (data) {
                var timestamp = data.timestamp;
                var nonceStr = data.nonceStr;
                var signature = data.signature;
                var appId = data.appId;
                var title = fxdata.title;
                var desc = fxdata.desc;
                var link = fxdata.link;
                if (!title) {
                    title = $("html > head > title").text();
                }
                if (!desc) {
                    desc = $("html > head > meta[name=description]").attr("content");
                }
                if (!link) {
                    link = location.href;
                }
                if (cburl === true) {
                    link = mkcburl(link);
                }
                var imgUrl = fxdata.imgUrl;
                wx.config({
                    debug: debug, appId: appId, timestamp: timestamp, nonceStr: nonceStr, signature: signature,
                    jsApiList: ["onMenuShareTimeline", "onMenuShareAppMessage", "onMenuShareQQ", "onMenuShareWeibo", "onMenuShareQZone"]
                });
                wx.ready(function () {
                    wx.onMenuShareTimeline({
                        title: title, link: link, imgUrl: imgUrl,
                        success: function () {
                            if (fxdata.success_onMenuShareTimeline)fxdata.success_onMenuShareTimeline();
                            else if (fxdata.success)fxdata.success();
                        },
                        cancel: function () {
                            if (fxdata.cancel_onMenuShareTimeline)fxdata.cancel_onMenuShareTimeline();
                            else if (fxdata.cancel)fxdata.cancel();
                        }
                    });
                    wx.onMenuShareAppMessage({
                        title: title, desc: desc, link: link, imgUrl: imgUrl, type: '', dataUrl: '',
                        success: function () {
                            if (fxdata.success_onMenuShareAppMessage)fxdata.success_onMenuShareAppMessage();
                            else if (fxdata.success)fxdata.success();
                        },
                        cancel: function () {
                            if (fxdata.cancel_onMenuShareAppMessage)fxdata.cancel_onMenuShareAppMessage();
                            else if (fxdata.cancel)fxdata.cancel();
                        }

                    });
                    wx.onMenuShareQQ({
                        title: title, desc: desc, link: link, imgUrl: imgUrl,
                        success: function () {
                            if (fxdata.success_onMenuShareQQ)fxdata.success_onMenuShareQQ();
                            else if (fxdata.success)fxdata.success();
                        },
                        cancel: function () {
                            if (fxdata.cancel_onMenuShareQQ)fxdata.cancel_onMenuShareQQ();
                            else if (fxdata.cancel)fxdata.cancel();
                        }
                    });
                    wx.onMenuShareWeibo({
                        title: title, desc: desc, link: link, imgUrl: imgUrl,
                        success: function () {
                            if (fxdata.success_onMenuShareWeibo)fxdata.success_onMenuShareWeibo();
                            else if (fxdata.success)fxdata.success();
                        },
                        cancel: function () {
                            if (fxdata.cancel_onMenuShareWeibo)fxdata.cancel_onMenuShareWeibo();
                            else if (fxdata.cancel)fxdata.cancel();
                        }
                    });
                    wx.onMenuShareQZone({
                        title: title, desc: desc, link: link, imgUrl: imgUrl,
                        success: function () {
                            if (fxdata.success_onMenuShareQZone)fxdata.success_onMenuShareQZone();
                            else if (fxdata.success)fxdata.success();
                        },
                        cancel: function () {
                            if (fxdata.cancel_onMenuShareQZone)fxdata.cancel_onMenuShareQZone();
                            else if (fxdata.cancel)fxdata.cancel();
                        }
                    });
                });
                wx.error(function (res) {
                    if (rep && rep >= ++n) {
                        initWxFxImpl(fxdata, rep, ++n);
                    }
                });
            }
        });
    }

    function initWxFx(fxdata, rep, debug, cburl) {
        initWxFxImpl(fxdata, rep ? ((1 <= rep && rep <= 5) ? rep : 0) : 0, 0, debug ? true : false, cburl ? true : false);
    }

    window.initWxFx = initWxFx;
})($);

