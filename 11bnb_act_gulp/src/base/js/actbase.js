//获取url参数
(function ($) {
    function getRequest() {
        var url = location.search;
        var theRequest = {};
        if (url.indexOf("?") > -1) {
            var str = url.substr(1);
            strs = str.split("&");
            for (var i = 0; i < strs.length; i++) {
                var str = strs[i];
                if (str.indexOf("=" > -1)) {
                    theRequest[str.split("=")[0]] = (str.split("=")[1]);
                } else {
                    theRequest[str.split("=")[0]] = "";
                }
            }
        }
        return theRequest;
    }

    function getParameter(key) {
        return getRequest()[key];
    }

    window.getRequest = getRequest;
    window.getParameter = getParameter;
})($);
function is_online() {
    return location.host === 'h5.11bnb.com';
}
function is_weixn() {
    var ua = navigator.userAgent.toLowerCase();
    if (ua.match(/MicroMessenger/i) == "micromessenger") {
        return true;
    } else {
        return false;
    }
}
function is_ios() {
    var ua = navigator.userAgent.toLowerCase();
    return ua.match(/iphone/i) == "iphone";
}
function is_android() {
    var ua = navigator.userAgent.toLowerCase();
    return ua.match(/android/i) == "android";
}
//电话号码格式化
function formatPhone(phone, fmt, cb) {
    var str = "";
    var phoneval = "";
    for (var i = 0, pi = 0; i < fmt.length; i++) {
        var c = fmt.charAt(i);
        if (/^[0-9]$/.test(c)) {
            if (/^[0-9]$/.test(fmt.charAt(i + 1))) {
                c += fmt.charAt(i + 1);
                i++;
            }
            c = parseInt(c);
            for (; c > 0; c--) {
                if (phone.length > pi) {
                    while (phone.length >= pi) {
                        var num = phone.charAt(pi++);
                        if (/^[0-9]$/.test(num)) {
                            phoneval += num;
                            str += num;
                            break;
                        }
                    }
                } else {
                    if (cb)cb(str, phoneval, fmt, false);
                    return str;
                }
            }
        } else {
            str += c;
        }
    }
    if (cb)cb(str, phoneval, fmt, true);
    return str;
}
//转菊花
var pageloading = (function () {
    var html = '' +
        '<div id="pageloading">' +
        '   <div class="layer"></div>' +
        '   <div class="imgbox">' +
        '       <img src="/static/nh5/images/loading.gif">' +
        '   </div>' +
        '</div>';

    function Pageloading() {
        this.sto = null;
    }

    Pageloading.prototype.open = function (ms) {
        this.close();
        var _this = this;
        clearTimeout(this.sto);
        $("body").append(html);
        if (ms) {
            this.sto = setTimeout(function () {
                _this.close();
            }, ms);
        }
    };
    Pageloading.prototype.close = function () {
        clearTimeout(this.sto);
        $("#pageloading").remove();
    };
    return new Pageloading();
})();
//获取用户信息
function getUserInfo(uin, cb) {
    $.ajax({
        url: '/app/user/getUserInfo/' + (uin || 100000) + '/', timeout: 10000, dataType: 'json',
        success: function (data) {
            if (cb) {
                cb(data);
            }
        },
        error: function (error) {
            console.log(error);
        }
    });
}

//验证手机号
function yzphone(phone) {
    return /^((13[0-9])|(15[0-9])|(17[0-9])|(18[0-9])|(11[0-9]))[0-9]{8}$/.test(phone);
}
//发送验证码
function sendYzm(coucode, phone, cb) {
    pageloading.open();
    $.ajax({
        url: "/app/login/getverificationcode?xxx", type: "post", timeout: 10000, dataType: 'json',
        data: JSON.stringify({phone: coucode + phone}),
        headers: {"user-uin": 100000},
        success: function (data) {
            pageloading.close();
            if (cb)cb(data);
        },
        error: function (msg) {
            pageloading.close();
            Message.error(error.status + " : " + error.statusText);
        }
    });
}
//发送语音
function sendYy(coucode, phone, cb) {
    pageloading.open();
    $.ajax({
        url: "/app/login/getverificationcode?xxx", type: "post", timeout: 10000, dataType: 'json',
        data: JSON.stringify({phone: coucode + phone, msg_type: 2}),
        headers: {"user-uin": 100000},
        success: function (data) {
            pageloading.close();
            if (cb)cb(data);
        },
        error: function (msg) {
            pageloading.close();
            Message.error(error.status + " : " + error.statusText);
        }
    });
}
//登出
function logout(cb) {
    pageloading.open();
    $.ajax({
        url: "/app/svr/logout?xxx", type: "post", dataType: "json", timeout: 10000,
        success: function (data) {
            pageloading.close();
        },
        error: function (msg) {
            pageloading.close();
        }
    });
}
//登陆
function login(coucode, phone, yzm, cb, err) {
    pageloading.open();
    $.ajax({
        url: "/app/login/signup_v2?xxx", type: "post", dataType: "json", timeout: 10000,
        data: JSON.stringify({phone: coucode + phone, verify_code: yzm}),
        headers: {"user-uin": 100000},
        success: function (data) {
            pageloading.close();
            if (cb)cb(data);
        },
        error: function (msg) {
            pageloading.close();
            Message.error(error.status + " : " + error.statusText);
        }
    });
}
//微信分享
(function ($) {
    var URL_GET_SIGNATURE = "/app/genWXSignature";

    function initWxFxImpl(fxdata, rep, n, debug) {
        $.ajax({
            url: URL_GET_SIGNATURE, data: JSON.stringify({"url": decodeURIComponent(location.href)}),
            type: "post", dataType: "json",
            success: function (data) {
                var timestamp = data.timestamp, nonceStr = data.nonceStr, signature = data.signature, appId = data.appId;
                var title = fxdata.title, desc = fxdata.desc, link = fxdata.link, imgUrl = fxdata.imgUrl;
                if (!title)title = $("html > head > title").text();
                if (!desc)desc = $("html > head > meta[name=description]").attr("content");
                if (!link)link = location.href;
                wx.config({
                    debug: debug, appId: appId, timestamp: timestamp, nonceStr: nonceStr, signature: signature,
                    jsApiList: ["onMenuShareTimeline", "onMenuShareAppMessage", "onMenuShareQQ", "onMenuShareWeibo", "onMenuShareQZone"]
                });
                wx.ready(function () {
                    wx.onMenuShareTimeline({
                        title: title, link: link, imgUrl: imgUrl,
                        success: function () {
                            if (fxdata.success)fxdata.success();
                        },
                        cancel: function () {
                            if (fxdata.cancel)fxdata.cancel();
                        }
                    });
                    wx.onMenuShareAppMessage({
                        title: title, desc: desc, link: link, imgUrl: imgUrl, type: '', dataUrl: '',
                        success: function () {
                            if (fxdata.success)fxdata.success();
                        },
                        cancel: function () {
                            if (fxdata.cancel)fxdata.cancel();
                        }

                    });
                    wx.onMenuShareQQ({title: title, desc: desc, link: link, imgUrl: imgUrl});
                    wx.onMenuShareWeibo({title: title, desc: desc, link: link, imgUrl: imgUrl});
                    wx.onMenuShareQZone({title: title, desc: desc, link: link, imgUrl: imgUrl});
                });
                wx.error(function (res) {
                    if (rep && rep >= ++n)initWxFxImpl(fxdata, rep, ++n);
                });
            }
        });
    }

    function initWxFx(fxdata, rep, debug) {
        initWxFxImpl(fxdata, rep ? ((1 <= rep && rep <= 5) ? rep : 0) : 0, 0, debug ? true : false);
    }

    window.initWxFx = initWxFx;
})($);
//消息提示框
var Message = (function () {
    function _Message() {
    }

    _Message.prototype.msg = function (text, ms) {
        var _this = this;
        this.clear();
        var html = "<div " +
            "id='message-msg'>" + text + "</div>";
        $(document.body).append(html);
        this.sto_msg = setTimeout(function () {
            _this.clear();
        }, ms ? ms : 2000);

    };
    _Message.prototype.clear = function () {
        clearTimeout(this.sto_msg);
        $("#message-msg").remove();
    };
    _Message.prototype.error = function (text, ms) {
        ms = ms || 3000;
        this.msg(text, ms);
    };
    return new _Message();
})();
//打开或下载App
function downloadApp(opt) {
    if (is_weixn()) {
        location.href = "http://a.app.qq.com/o/simple.jsp?pkgname=com.YYB.yiyibnb_android";
    } else {
        window.setTimeout(function () {
            window.location = "http://a.app.qq.com/o/simple.jsp?pkgname=com.YYB.yiyibnb_android";
        }, 3000);
        location.href = is_online() ? "yiyibnb://11bnb.com/" : "yiyibnbt://11bnb.com/";
    }
}
