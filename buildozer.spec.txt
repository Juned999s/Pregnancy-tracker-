[app]
title = Pregnancy Tracker
package.name = pregnancytracker
package.domain = org.myapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 1.0
requirements = python3,kivy,plyer
orientation = portrait
fullscreen = 0

android.permissions = VIBRATE,POST_NOTIFICATIONS
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
