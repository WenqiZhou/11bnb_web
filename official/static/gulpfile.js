var gulp = require('gulp');
var less = require('gulp-less');
var minifyCSS = require('gulp-minify-css');
gulp.task('less', function () {
    gulp.src('v2/less/**/*.less')
        .pipe(less())
        .on('error', function (err) {
            console.error('less error!', err.message);
            this.emit('end');
        })
        .pipe(minifyCSS())
        .pipe(gulp.dest('v2/css'))
});

gulp.task('default',['less'], function () {
    gulp.watch('v2/less/**/*.less',['less'])
});