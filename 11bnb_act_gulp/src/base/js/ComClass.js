var PhoneInputClass = React.createClass({
    getInitialState: function () {
        return {};
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
    render: function () {
        return (
            <input
                className={this.props.className || this.state.className || ""}
                onChange={this.onPhoneInputChange}
                value={this.state.phonestr}
                type="tel"placeholder="请输入您的手机号"
            />
        );
    }
});
var YzmInputClass = React.createClass({
    getInitialState: function () {
        return {};
    },
    onYzmInputChange: function (event) {
        if (event.target.value.length == 4) {
            event.target.blur();
        }
    },
    render: function () {
        return (
            <input
                className={this.props.className || this.state.className || ""}
                onChange={this.onYzmInputChange}
                ref="yzm"type="tel"maxLength="4"placeholder="请输入验证码"
            />
        );
    }
});
