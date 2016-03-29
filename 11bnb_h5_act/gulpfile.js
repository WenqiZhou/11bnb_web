var gulp = require('gulp'),
    uglify = require('gulp-uglify'),
    htmlmin = require('gulp-htmlmin'), //html压缩
    imagemin = require('gulp-imagemin'),//图片压缩
    pngcrush = require('imagemin-pngcrush'),
    pngquant = require('imagemin-pngquant'),
    minifycss = require('gulp-minify-css'),//css压缩
//jshint = require('gulp-jshint'),//js检测
    uglify = require('gulp-uglify'),//js压缩
    concat = require('gulp-concat'),//文件合并
    rename = require('gulp-rename'),//文件更名
    notify = require('gulp-notify');//提示信息

var connect = require('gulp-connect');

var less = require('gulp-less');
var path = require('path');


var http = require('http');
var fs = require('fs');
var oppressor = require('oppressor');


gulp.task('webserver', function () {
    connect.server({
        port: 3000,
        root: 'dest',
    });
});


gulp.task('less', function () {
    gulp.src('src/less/*.less')
        .pipe(less())
        .pipe(minifycss())
        .pipe(gulp.dest('dest/css'));

});


// 压缩html
gulp.task('html', function () {
    return gulp.src('src/*.html')
        //.pipe(htmlmin({collapseWhitespace: true}))
        .pipe(gulp.dest('dest'))
    //.pipe(notify({message: 'html task ok'}));

});

// 压缩图片
gulp.task('img', function () {
    return gulp.src('src/images/*')

        .pipe(imagemin({
            progressive: true,
            svgoPlugins: [{removeViewBox: false}],
            use: [pngcrush()]
        }))
        .pipe(gulp.dest('dest/images/'))

    //.pipe(notify({message: 'img task ok'}));
});


// 合并、压缩、重命名css
gulp.task('css', function () {
    return gulp.src('src/css/*.css')
        //.pipe(concat('main.css'))
        .pipe(gulp.dest('dest/css'))
    //.pipe(rename({suffix: '.min'}))
    //.pipe(minifycss())
    //.pipe(gulp.dest('dest/css'))
    // .pipe(notify({message: 'css task ok'}));

});


// 合并、压缩js文件
gulp.task('js', function () {

    gulp.src('src/js/*.js')
        // .pipe(concat('controller.js'))
        // .pipe(gulp.dest('dest/js'))
        .pipe(uglify())
        // .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('dest/js'));
});


// 默认任务
gulp.task('default', function () {
    gulp.run('img', 'css', 'js', 'html', 'less');
    gulp.run('webserver');

    // 监听less文件变化
    gulp.watch('src/less/*/*.less', ['less']);
    gulp.watch('src/less/*.less', ['less']);

    // 监听html文件变化
    gulp.watch('src/*.html', ['html']);

    // // 监听tpls文件变化
    // gulp.watch('src/tpls/*', ['tpls']);
    // gulp.watch('src/tpls/*/*', ['tpls']);

    // Watch .css files
    gulp.watch('src/css/*.css', ['css']);

    // Watch .js files
    gulp.watch('src/js/*.js', ['js']);

    // Watch image files
    gulp.watch('src/images/*', ['img']);


});







