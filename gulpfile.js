const { resolve } = require("path");
const gulp = require("gulp");
const if_ = require("gulp-if");
const less = require("gulp-less");
const sourcemaps = require("gulp-sourcemaps");
const touch = require("gulp-touch-fd");
const cleanCss = require("gulp-clean-css");

const isDev = () => !!process.env.DEBUG;

const themeDir = resolve("ckanext/latex/theme");
const assetsDir = resolve("ckanext/latex/assets");

const build = () =>
  gulp
    .src(resolve(themeDir, "latex.less"))
    .pipe(if_(isDev, sourcemaps.init()))
    .pipe(less())
    .pipe(if_(() => !isDev(), cleanCss()))
    .pipe(if_(isDev, sourcemaps.write()))
    .pipe(gulp.dest(resolve(assetsDir, "styles")))
    .pipe(touch());

const watch = () =>
  gulp.watch(resolve(themeDir, "*.less"), { ignoreInitial: false }, build);

exports.build = build;
exports.watch = watch;