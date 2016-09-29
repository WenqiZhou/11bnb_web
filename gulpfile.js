/**
 * Created by tuobaocheng on 16/7/5.
 */
var gulp = require('gulp');
var connect = require('gulp-connect');
var plumber = require('gulp-plumber');
var less = require('gulp-less');


gulp.task('css', function () {
    gulp.src('./official/static/v2/less/*.less')
        .pipe(plumber())
        .pipe(less())
        //.pipe(autoprefixer(autoprefixerConfig))
        //.pipe(gulpif(options.compress, minifyCSS()))
        .pipe(gulp.dest('./official/static/v2/css/'))
});

gulp.task('connect', function () {
    connect.server({
        root: 'official',
        livereload: true,
        port: 9999
    });
});

gulp.task('html', function () {
    gulp.src('./official/*.html')
        .pipe(plumber())
        .pipe(connect.reload());
});

gulp.task('watch', function () {
    gulp.watch(['./official/*.html'], ['html']);
    gulp.watch('./official/static/v2/less/**/*.less', ['css']);
});

gulp.task('default', ['connect', 'css', 'watch']);