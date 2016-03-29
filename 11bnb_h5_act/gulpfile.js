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
        root: 'build',
    });


    // var server = http.createServer(function (req, res) {
    //     var stream = fs.createReadStream("build");
    //     stream.pipe(oppressor(req)).pipe(res);
    // });
    // server.listen(8000);

});


gulp.task('less', function () {
    gulp.src('app/less/*.less')
        .pipe(less())
        .pipe(gulp.dest('app/css'))
        .pipe(gulp.dest('build/css'));

});


//gulp.task('bower', function () {
//    gulp.src('bower_components/angular/*')
//        .pipe(gulp.dest('build/components/angular/')).pipe(gulp.dest('app/components/angular/'))
//});


// tpls
gulp.task('tpls', function () {
    return gulp.src('app/tpls/**/*.html')
        //.pipe(htmlmin({collapseWhitespace: true}))
        .pipe(gulp.dest('build/tpls'))
    //.pipe(notify({message: 'html task ok'}));

});

// 压缩html
gulp.task('html', function () {
    return gulp.src('app/*.html')
        //.pipe(htmlmin({collapseWhitespace: true}))
        .pipe(gulp.dest('build'))
    //.pipe(notify({message: 'html task ok'}));

});

// 压缩图片
gulp.task('img', function () {
    return gulp.src('app/images/*')
        .pipe(imagemin({
            progressive: true,
            svgoPlugins: [{removeViewBox: false}],
            use: [pngcrush()]
        }))
        .pipe(gulp.dest('build/images/'))
    //.pipe(notify({message: 'img task ok'}));
});


// 合并、压缩、重命名css
gulp.task('css', function () {
    return gulp.src('app/css/*.css')
        //.pipe(concat('main.css'))
        .pipe(gulp.dest('build/css'))
        //.pipe(rename({suffix: '.min'}))
        //.pipe(minifycss())
        //.pipe(gulp.dest('build/css'))
        .pipe(notify({message: 'css task ok'}));
});


// 检查js
//gulp.task('lint', function () {
//    return gulp.src('app/js/*.js')
//        .pipe(jshint())
//        .pipe(jshint.reporter('default'))
//        .pipe(notify({message: 'lint task ok'}));
//});


// 合并、压缩js文件
gulp.task('js', function () {

    gulp.src('app/js/controller/*.js')
        .pipe(concat('controller.js'))
        .pipe(gulp.dest('build/js'))
    //.pipe(rename({suffix: '.min'}))
    //.pipe(uglify())
    //.pipe(gulp.dest('build/js'));
    gulp.src('app/js/directive/*.js')
        .pipe(concat('directive.js'))
        .pipe(gulp.dest('build/js'))
    //.pipe(rename({suffix: '.min'}))
    //.pipe(uglify())
    //.pipe(gulp.dest('build/js'));
    gulp.src('app/js/filter/*.js')
        .pipe(concat('filter.js'))
        .pipe(gulp.dest('build/js'))
    //.pipe(rename({suffix: '.min'}))
    //.pipe(uglify())
    //.pipe(gulp.dest('build/js'));
    gulp.src('app/js/service/*.js')
        .pipe(concat('service.js'))
        .pipe(gulp.dest('build/js'))
    //.pipe(rename({suffix: '.min'}))
    //.pipe(uglify())
    //.pipe(gulp.dest('build/js'));
    gulp.src('app/js/*.js')
        //.pipe(concat('controller.js'))
        .pipe(gulp.dest('build/js'))
    //.pipe(rename({suffix: '.min'}))
    //.pipe(uglify())
    //.pipe(gulp.dest('build/js'));
});


// 默认任务
gulp.task('default', function () {
    gulp.run('img', 'css', 'js', 'html', 'tpls', 'less');
    gulp.run('webserver');

    // 监听less文件变化
    gulp.watch('app/less/*/*.less', ['less']);
    gulp.watch('app/less/*.less', ['less']);

    // 监听html文件变化
    gulp.watch('app/*.html', ['html']);

    // 监听tpls文件变化
    gulp.watch('app/tpls/*', ['tpls']);
    gulp.watch('app/tpls/*/*', ['tpls']);

    // Watch .css files
    gulp.watch('app/css/*.css', ['css']);

    // Watch .js files
    gulp.watch('app/js/*.js', ['js']);

    // Watch image files
    gulp.watch('app/images/*', ['img']);

});







