/**
 * Created by tuobaocheng on 16/7/5.
 */
class Page {
    constructor(length, container) {
        this.length = length;
        this.container = container;
        this.btn = null;
    }

    getNumber() {
        return Math.ceil(this.length / 5);
    }

    setBtn() {
        var html = '<li class="page_item page_top">上一页</li>', len = this.getNumber();
        for (let i = 0; i < len; i++) {
            html += '<li class="page_item btn">' + (i + 1) + '</li>';
        }
        html += '<li class="page_item page_down">下一页</li>';
        this.container.empty().append(html);
        return this;
    }

    setDefaultActive(cb) {
        this.btn = this.container.find('.btn');
        this.pageTop = this.container.find('.page_top');
        this.pageTop.hide();
        this.btn.eq(0).addClass('active');
        if (cb)cb();
        return this;
    }

    btnClick(cb) {
        this.container.on('click', '.btn', (e = e)=> {
            if ($(e.target).hasClass('active')) return false;
            let x = $(e.target).index();
            this.btn.eq(x-1).addClass('active').siblings().removeClass('active');
            if (cb) return cb(x);
        })
    }

    pageClick(cb) {
        this.container.on('click', '.page_top', ()=> {
            let pageTop = this.container.find('.page_top');
            if (pageTop.hasClass('disabled')) return false;
            if (cb) {
                return cb(true)
            }
        });
        this.container.on('click', '.page_down', ()=> {
            let pageTop = this.container.find('.page_down');
            if (pageTop.hasClass('disabled')) return false;
            if (cb) {
                return cb(false)
            }
        });
    }

    init(cb) {
        this.setBtn().setDefaultActive(cb);
    }
}