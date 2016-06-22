var shareuin = getParameter("uin");
var l = getParameter("l");
var sig = getParameter("sig");
//领取接口
function h5_get_card(shareuin, sig, cb) {
    pageloading.open();
    $.ajax({
        url: '/app/ggk/h5_get_card/' + shareuin + '/' + sig, timeout: 10000, dataType: "json",
        success: function (data) {
            pageloading.close();
            if (cb)cb(data);
        },
        error: function (error) {
            pageloading.close();
            Message.error(error.status + " : " + error.statusText);
        }
    });
}
var NAME_LIST = ["马云", "马化腾", "王健林", "李彦宏", "比尔盖茨", "巴菲特"];
function getName(luck) {
    luck = luck || 0;
    return NAME_LIST[luck % NAME_LIST.length];
}
function checkLuck(luck) {
    if (luck && typeof (luck - 0) == 'number') {
        return luck;
    }
    return 90;
}
//活动规则
var RuleClass = React.createClass({
    getInitialState: function () {
        return {};
    },
    render: function () {
        return (
            <div className="panel panel-white">
                <div className="panel-header ft-c-r">
                    <span className="decorate decorate-l"></span>
                    活动规则
                    <span className="decorate decorate-r"></span>
                </div>
                <div className="panel-content">
                    <ul>
                        <li>
                            <span className="index">1</span>
                            每个用户输入手机号和验证码领取幸运刮刮卡；</li>
                        <li>
                            <span className="index">2</span>
                            领取成功后下载依依短租APP参与刮卡抽奖；</li>
                        <li>
                            <span className="index">3</span>
                            分享好友越多，获得的刮刮卡越多。</li>
                        <li>
                            <span className="index">4</span>
                            关于1元民宿基金：由中国民宿研究院和依依短租帮助贫困农户装修村屋，从事民宿行业，脱贫致富。民宿公益基金1年帮扶1户。</li>
                    </ul>
                </div>
                <div className="panel-footer">
                    <img src="/static/nh5/act/100002/images/logo-f.png" alt=""/>
                </div>
            </div>
        );
    }
});
//页面顶部
var HeaderClass = React.createClass({
    getInitialState: function () {
        return {
            dfi: Math.floor(Math.random() * 7)
        };
    },
    render: function () {
        var dfi = this.state.dfi;
        var headhtml = null;
        if (this.props.shareUser && this.props.shareUser.head_url) {
            headhtml = (
                <img className="head" src={this.props.shareUser.head_url + "_337"} alt=""/>
            );
        } else {
            headhtml = (
                <img className="head" src={dfi == 0 ? "/static/nh5/act/images/df-head.png" : "/static/nh5/act/images/df-head-" + dfi + ".png"} alt=""/>
            );
        }
        return (
            <div className="box">
                <img className="bc" src="/static/nh5/act/100002/images/bc.png?v=1" alt=""/>
                <img className="s s-l1-2" src="/static/nh5/act/100002/images/s-l1-2.png" alt=""/>
                <img className="s s-l2-2" src="/static/nh5/act/100002/images/s-l2-2.png" alt=""/>
                <img className="s s-r1-2" src="/static/nh5/act/100002/images/s-r1-2.png" alt=""/>
                <img className="s s-r2-2" src="/static/nh5/act/100002/images/s-r2-2.png" alt=""/>
                <img className="logo" src="/static/nh5/act/100002/images/logo.png" alt=""/>
            {headhtml}
                <p>
                    {this.props.shareUser && this.props.shareUser.real_name ? this.props.shareUser.real_name : '小蘑菇'}刮出幸运值堪比
                    <span className="nickname">{getName(l)}</span>
                    ,
                    喊你来一起刮！
                </p>
            </div>
        );
    }
});
//登陆form
var FormClass = React.createClass({
    getInitialState: function () {
        return {
            phonestr: "",
            phoneval: "",
            sendable: false,
            sendtext: "发送验证码",
            yzm: ""
        };
    },
    onYzmInputChange: function (event) {
        if (event.target.value.length == 4) {
            event.target.blur();
        }
    },
    onPhoneInputChange: function (event) {
        var _this = this;
        var value = event.target.value;
        event.target.value = "";
        if (value.length > this.state.phonestr.length) {
            formatPhone(value, "3 4 4", function (str, phoneval, fmt, isend) {
                _this.setState({
                    phonestr: str,
                    sendable: false
                });
                if (isend) {
                    event.target.blur();
                    _this.setState({
                        sendable: true,
                        phoneval: phoneval
                    });
                }
            });
        } else {
            _this.setState({
                phonestr: value,
                sendable: false
            });
        }
    },
    onClickSendYzm: function (event) {
        var _this = this;
        if (!this.state.sendable) return false;
        sendYzm("", this.state.phoneval, function (data) {
            if (data.ret === undefined || data.ret == 0) {
                var i = 30;
                _this.setState({
                    sendtext: i + 's',
                    sendable: false
                });
                _this.state.sendInterval = setInterval(function () {
                    i--;
                    if (i > 0) {
                        _this.setState({
                            sendtext: i + 's',
                            sendable: false
                        });
                    } else {
                        clearInterval(_this.state.sendInterval);
                        _this.setState({
                            sendtext: '发送验证码',
                            sendable: true
                        });
                    }
                }, 1000);
            } else {
                Message.error(data.err);
            }
        })
    },
    onClickLogin: function (event) {
        var _this = this;
        if (_this.state.phoneval.length != 11) return false;
        if (_this.refs.yzm.value.length != 4)return false;
        login("+86", this.state.phoneval, _this.refs.yzm.value, function (data) {
            if (data.ret === undefined || data.ret == 0) {
                if (_this.props.onLoginSuccess)_this.props.onLoginSuccess();

            } else {
                Message.error(data.err);
            }
        });
    },
    render: function () {
        return (
            <div className="panel panel-white">
                <div className="panel-header ft-c-r">
                    <span className="decorate decorate-l"></span>
                    依依短租
                    <span className="decorate decorate-r"></span>
                </div>
                <div className="panel-content">
                    <div className="input">
                        <input value={this.state.phonestr} onChange={this.onPhoneInputChange} type="tel" placeholder="请输入您的手机号"/>
                    </div>
                    <div className="input">
                        <input ref="yzm" type="tel" maxLength="4" placeholder="请输入验证码"onChange={this.onYzmInputChange}/>
                        <span className={this.state.sendable ? "" : "disabled"} onClick={this.onClickSendYzm}>{this.state.sendtext}</span>
                    </div>
                    <p className="msg">{this.props.shareUser && this.props.shareUser.real_name ? this.props.shareUser.real_name : '小蘑菇'}的幸运值{l}</p>
                    <div onClick={this.onClickLogin} className="btn btn-submit">领取刮刮卡，PK{this.props.shareUser && this.props.shareUser.real_name ? this.props.shareUser.real_name : '小蘑菇'}</div>
                </div>
            </div>
        );
    }
});
//领取成功页
var SuccessClass = React.createClass({
    getInitialState: function () {
        return {};
    },
    downloadApp: function () {
        downloadApp({
            guidefn: function () {
                Message.msg("请使用浏览器打开！");
            },
            dpurl: "ggk?u=" + shareuin
        });
    },
    render: function () {
        return (
            <div className="panel panel-white">
                <div className="panel-header">
                    <span className="decorate decorate-l"></span>
                    恭喜您获得
                    <span className="decorate decorate-r"></span>
                </div>
                <div className="panel-content">
                    <p className="bigmsg">{this.props.shareUser && this.props.shareUser.real_name ? this.props.shareUser.real_name : '小蘑菇'}送给您的幸运刮刮卡</p>
                    <p className="msg">我的幸运值{this.props.userluck}，堪比{getName(this.props.userluck)}，
                        <br/>
                    {this.props.userluck > l ?
                    "超过了" + (this.props.shareUser && this.props.shareUser.real_name ? this.props.shareUser.real_name : '小蘑菇') + "!"
                        : (this.props.shareUser && this.props.shareUser.real_name ? this.props.shareUser.real_name : '小蘑菇') + "传递幸运给我！"}
                    </p>
                    <div className="btn btn-submit" onClick={this.downloadApp}>马上刮奖</div>
                </div>
            </div>
        );
    }
});
//页面入口
var AppClass = React.createClass({
    getInitialState: function () {
        return {};
    },
    onLoginSuccess: function () {
        var _this = this;
        h5_get_card(shareuin, sig, function (data) {
            if (data.ret === undefined || data.ret == 0) {
                document.body.scrollTop = 0;
                _this.setState({
                    received: true,
                    userluck: data.luck
                });
            } else {
                Message.error(data.err);
                if (data.ret == -16005) {
                    document.body.scrollTop = 0;
                    _this.setState({
                        received: true,
                        userluck: data.luck
                    });
                }
            }
        });
    },
    render: function () {
        var views = [];
        if (this.state.shareUser) {
            views.push(
                <HeaderClass shareUser={this.state.shareUser}/>
            );
            if (this.state.userinit) {
                if (this.state.received) {
                    views.push(
                        <SuccessClass shareUser={this.state.shareUser} user={this.state.user} userluck={this.state.userluck}/>
                    );
                } else {
                    views.push(
                        <FormClass shareUser={this.state.shareUser} user={this.state.user} onLoginSuccess={this.onLoginSuccess}/>
                    );
                }
            }
        }
        views.push(
            <RuleClass/>
        );
        return (
            <div>
            {views}
            </div>
        );
    }
});
var render;
//获取分享人信息
getUserInfo(shareuin, function (data) {
    render = ReactDOM.render(
        <AppClass/>
        , document.getElementById("main"));
    render.setState({
        shareUser: data.user,
        userinit: true
    });
    var fxdata = {
        title: 'XXX喊你来领依依短租幸运刮刮卡！',
        desc: '5000元旅行基金、1元住民宿、330元现金券天天送',
        imgUrl: location.origin + '/static/nh5/act/100002/images/share.png'
    };
    if (data.user) {
        fxdata.title = data.user.real_name + '喊你来领依依短租幸运刮刮卡！';
    }
    initWxFx(fxdata, 0, false);
});