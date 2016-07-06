/**
 * Created by tuobaocheng on 16/7/5.
 */
function Page(length, container) {
    this.length = length;
    this.container = container;
    this.btn = null;
}

Page.prototype.getNumber = function () {
    return Math.ceil(this.length / 5);
}

Page.prototype.setBtn = function () {
    var html = '<li class="page_item page_top">上一页</li>', len = this.getNumber();
    for (var i = 0; i < len; i++) {
        html += '<li class="page_item btn">' + (i + 1) + '</li>';
    }
    html += '<li class="page_item page_down">下一页</li>';
    this.container.empty().append(html);
    return this;
}

Page.prototype.setDefaultActive = function (cb) {
    this.btn = this.container.find('.btn');
    this.pageTop = this.container.find('.page_top');
    this.pageTop.hide();
    this.btn.eq(0).addClass('active');
    if (cb)cb();
    return this;
}

Page.prototype.btnClick = function (cb) {
    this.container.on('click', '.btn', function (e) {
        if ($(e.target).hasClass('active')) return false;
        var x = $(e.target).index();
        this.btn.eq(x - 1).addClass('active').siblings().removeClass('active');
        if (cb) return cb(x);
    })
}

Page.prototype.pageClick = function (cb) {
    this.container.on('click', '.page_top', function () {
        var pageTop = this.container.find('.page_top');
        if (pageTop.hasClass('disabled')) return false;
        if (cb) {
            return cb(true)
        }
    });
    this.container.on('click', '.page_down', function () {
        var pageTop = this.container.find('.page_down');
        if (pageTop.hasClass('disabled')) return false;
        if (cb) {
            return cb(false)
        }
    });
}

Page.prototype.init = function (cb) {
    this.setBtn().setDefaultActive(cb);
}
