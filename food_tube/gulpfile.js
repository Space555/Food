var gulp = require('gulp');
var sass = require('gulp-sass');
var browserSync = require('browser-sync').create();
var exec = require('child_process').exec;

gulp.task('sass', function() {
  return gulp.src('app_recipes/static/ft/css/**/*.css')
    .pipe(sass())
    .pipe(gulp.dest('app_recipes/static/ft/css/'))
    .pipe(browserSync.reload({
      stream: true
    }))
});

gulp.task('runserver', function() {
  var proc = exec('python manage.py runserver')
})

gulp.task('browserSync', ['runserver'], function() {
  browserSync.init({
    notify: false,
    port: 8000,
    proxy: 'localhost:8000'
  })
});

gulp.task('watch', gulp.series('browserSync', 'sass'), function() {
  gulp.watch('app_recipes/static/ft/css/**/*.css', ['sass']);
  gulp.watch('app_recipes/static/ft/Js/**/*.js', browserSync.reload);
  gulp.watch('app_recipes/templates/**/*.html', browserSync.reload);
})