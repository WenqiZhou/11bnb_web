var gulp = require('gulp');
var react = require('gulp-react');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var less = require('gulp-less');
var minifyCSS = require('gulp-minify-css');
var imagemin = require('gulp-imagemin');
var msg = require('gulp-msg');
var connect = require("gulp-connect");
var Reproxy = require("gulp-connect-reproxy");

var userpath = '../../';


var srcpath = 'src/';

var basepath = 'src/base/';
var lesspath = 'src/less/';
var vendorpath = 'src/vendor/';

var tobasepath = userpath + '11bnb_backend/static/nh5/act/';
var toviewpath = userpath + '11bnb_backend/templates/nh5/act/';


gulp.task('connect', function () {
    connect.server({
        root: "build",
        port: 3000,
        livereload: true,
        middleware: function (connect, options) {
            options.rule = [/^\/app\//];
            options.server = "dev.11bnb.com:11990";
            var proxy = new Reproxy(options);
            return [proxy];
        }
    });
});


function compress(comp, cb, devinfo) {
    if (comp && cb)return cb();
    return msg.info(devinfo || 'not compress!');
}

function startWord(source, target, comp) {

    //base
    gulp.task('base-vendor', function () {
        gulp.src(vendorpath + '**/*')
            .pipe(gulp.dest(tobasepath + 'vendor/'));
    });

    gulp.task('concat-react', function () {
        gulp.src([
            vendorpath + 'react/react.min.js',
            vendorpath + 'react/react-dom.min.js'
        ])
            .pipe(concat('react-bd-min.js'))
            .pipe(gulp.dest(tobasepath + 'js/'));
    });
    gulp.task('base-js', function () {
        gulp.src(basepath + 'js/**/*.js')
            .pipe(react())
            .pipe(uglify())
            .pipe(gulp.dest(tobasepath + 'js/'));
    });
    gulp.task('base-img', function () {
        return gulp.src(basepath + 'images/**/*')
            .pipe(imagemin())
            .pipe(gulp.dest(tobasepath + 'images/'))
    });

    gulp.task('base', ['base-vendor', 'concat-react', 'base-js', 'base-img'],
        function () {
            gulp.watch(vendorpath + '**/*', ['base-vendor']);
            gulp.watch(basepath + 'js/**/*.js', ['base-js']);
            gulp.watch(basepath + 'images/**/*', ['base-img']);
        }
    );

    //app
    source += '/';
    target += '/';
    gulp.task('js', function () {
        gulp.src(srcpath + source + 'js/**/*.js')
            .pipe(react())
            .on('error', function (err) {
                console.error('react error!', err.message);
                this.emit('end');
            })
            .pipe(compress(comp, function () {
                return uglify();
            }))
            .pipe(gulp.dest(tobasepath + target + 'js/'));
    });

    gulp.task('css', function () {
        return gulp.src(srcpath + source + 'css/**/*.less')
            .pipe(less())
            .on('error', function (err) {
                console.error('less error!', err.message);
                this.emit('end');
            })
            .pipe(compress(comp, function () {
                return minifyCSS();
            }))
            .pipe(gulp.dest(tobasepath + target + 'css/'))
    });
    gulp.task('img', function () {
        return gulp.src(srcpath + source + 'images/**/*')
            .pipe(imagemin())
            .pipe(gulp.dest(tobasepath + target + 'images/'))
    });
    gulp.task('html', function () {
        return gulp.src(srcpath + source + '**/*.html')
            .pipe(gulp.dest(toviewpath + target))
    });
    gulp.task('default', ['base', 'js', 'css', 'img', 'html'], function () {
        gulp.watch(srcpath + source + 'js/**/*.js', ['js']);
        gulp.watch([
            srcpath + source + 'css/**/*.less',
            lesspath + '**/*.less'
        ], ['css']);
        gulp.watch(srcpath + source + 'images/**/*', ['img']);
        gulp.watch(srcpath + source + '**/*.html', ['html']);
    });
}
var basecomp = true;
startWord('ggk', '100002', true);




