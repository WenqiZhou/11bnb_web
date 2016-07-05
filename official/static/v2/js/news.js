'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

/**
 * Created by tuobaocheng on 16/7/5.
 */

var Page = function () {
    function Page(length, container) {
        _classCallCheck(this, Page);

        this.length = length;
        this.container = container;
        this.btn = null;
    }

    _createClass(Page, [{
        key: 'getNumber',
        value: function getNumber() {
            return Math.ceil(this.length / 5);
        }
    }, {
        key: 'setBtn',
        value: function setBtn() {
            var html = '<li class="page_item page_top">上一页</li>',
                len = this.getNumber();
            for (var i = 0; i < len; i++) {
                html += '<li class="page_item btn">' + (i + 1) + '</li>';
            }
            html += '<li class="page_item page_down">下一页</li>';
            this.container.empty().append(html);
            return this;
        }
    }, {
        key: 'setDefaultActive',
        value: function setDefaultActive(cb) {
            this.btn = this.container.find('.btn');
            this.pageTop = this.container.find('.page_top');
            this.pageTop.hide();
            this.btn.eq(0).addClass('active');
            if (cb) cb();
            return this;
        }
    }, {
        key: 'btnClick',
        value: function btnClick(cb) {
            var _this = this;

            this.container.on('click', '.btn', function () {
                var e = arguments.length <= 0 || arguments[0] === undefined ? e : arguments[0];

                if ($(e.target).hasClass('active')) return false;
                var x = $(e.target).index();
                _this.btn.eq(x - 1).addClass('active').siblings().removeClass('active');
                if (cb) return cb(x);
            });
        }
    }, {
        key: 'pageClick',
        value: function pageClick(cb) {
            var _this2 = this;

            this.container.on('click', '.page_top', function () {
                var pageTop = _this2.container.find('.page_top');
                if (pageTop.hasClass('disabled')) return false;
                if (cb) {
                    return cb(true);
                }
            });
            this.container.on('click', '.page_down', function () {
                var pageTop = _this2.container.find('.page_down');
                if (pageTop.hasClass('disabled')) return false;
                if (cb) {
                    return cb(false);
                }
            });
        }
    }, {
        key: 'init',
        value: function init(cb) {
            this.setBtn().setDefaultActive(cb);
        }
    }]);

    return Page;
}();