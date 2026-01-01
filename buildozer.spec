[app]

# 應用程式資訊
title = 水果新鮮度診斷
package.name = fruitfreshness
package.domain = com.example

# 版本資訊
version = 1.0.0

# 來源檔案
source.dir = .
source.main = main.py

# 需求套件
requirements = python3,kivy

# Android 設定
android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk = 23
android.ndk = 23b
android.ndk_api = 21

# 螢幕方向
orientation = portrait

# 架構
android.arch = arm64-v8a,armeabi-v7a

# 圖示（可以稍後添加）
# icon.filename = icon.png

# 其他設定
fullscreen = 0
log_level = 2
