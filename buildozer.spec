Write-Host "🚀 完整修復 GitHub Actions 建置問題" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan

# 1. 確保在正確目錄
Write-Host "`n1️⃣ 檢查當前目錄..." -ForegroundColor Cyan
$currentDir = pwd
Write-Host "當前目錄: $currentDir" -ForegroundColor White

if ($currentDir -notlike "*fruit-app") {
    Write-Host "⚠  不在專案目錄，切換到 fruit-app..." -ForegroundColor Yellow
    if (Test-Path "C:\Users\User\fruit-app") {
        cd C:\Users\User\fruit-app
        Write-Host "✅ 已切換到專案目錄" -ForegroundColor Green
    } else {
        Write-Host "❌ 專案目錄不存在，創建新專案..." -ForegroundColor Red
        mkdir C:\Users\User\fruit-app -Force
        cd C:\Users\User\fruit-app
        
        # 創建必要檔案
        # main.py
        @"
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class FruitApp(App):
    def build(self):
        self.title = "水果新鮮度診斷"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        title = Label(text="🍎 水果新鮮度診斷系統", font_size=24)
        layout.add_widget(title)
        
        btn = Button(text="🧠 開始分析", size_hint=(1, 0.3), background_color=(0.2, 0.6, 0.2, 1))
        btn.bind(on_press=self.analyze)
        layout.add_widget(btn)
        
        self.result = Label(text="點擊上方按鈕開始分析", font_size=16, size_hint=(1, 0.7))
        layout.add_widget(self.result)
        
        return layout
    
    def analyze(self, instance):
        import random
        fruits = ["蘋果", "香蕉", "橙子", "草莓", "葡萄", "西瓜"]
        freshness = random.randint(60, 100)
        self.result.text = f"分析結果：\n\n🍎 水果：{random.choice(fruits)}\n⭐ 新鮮度：{freshness}/100\n💡 建議：建議立即食用"

if __name__ == '__main__':
    FruitApp().run()
"@ | Out-File -FilePath "main.py" -Encoding UTF8
        
        # buildozer.spec
        @'
[app]
title = 水果新鮮度診斷
package.name = fruitfreshness
package.domain = com.example
source.dir = .
source.main = main.py
version = 1.0.0
requirements = python3,kivy
android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk = 23
android.ndk = 23b
orientation = portrait
android.arch = arm64-v8a,armeabi-v7a
