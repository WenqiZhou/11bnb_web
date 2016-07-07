/**
 * Created by tuobaocheng on 16/7/5.
 */
const gulp = require('gulp'),
    connect = require('gulp-connect');

gulp.task('connect', function() {
    connect.server({
        root: 'official',
        livereload: true,
        port:9999
    });
});

gulp.task('html', function () {
    gulp.src('./official/*.html')
        .pipe(connect.reload());
});

gulp.task('watch', function () {
    gulp.watch(['./official/*.html'], ['html']);
});

gulp.task('default', ['connect', 'watch']);