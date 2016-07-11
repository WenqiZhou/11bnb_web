const gulp = require('gulp');
const less = require('gulp-less');
const minifyCSS = require('gulp-minify-css');
const imgmin = require('gulp-imagemin');
const babel = require('gulp-babel');
gulp.task('less', () => {
    return gulp.src('v2/less/**/*.less')
        .pipe(less())
        .on('error', function (err) {
            console.error('less error!', err.message);
            this.emit('end');
        })
        .pipe(minifyCSS())
        .pipe(gulp.dest('v2/css'))
});
//gulp.task('babel', ()=> {
//    gulp.src('v2/es6js/**/*.js')
//        .pipe(babel({
//            presets: ['es2015']
//        }))
//        .on('error', function (err) {
//            console.error('less error!', err.message);
//            this.emit('end');
//        })
//        .pipe(gulp.dest('v2/js/'))
//});
gulp.task('imgmin', ()=> {
    return gulp.src('../newsdetail/**/*.png')
        .pipe(imgmin())
        .on('error', function (err) {
            console.error('imgmin error!', err.message);
            this.emit('end');
        })
        .pipe(gulp.dest('../newsdetail/'))
});
gulp.task('default', ['less','imgmin'], () => {
    gulp.watch('v2/less/**/*.less', ['less']);
    gulp.watch('../newsdetail/**/*.png', ['imgmin']);
});
