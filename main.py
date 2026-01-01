# -*- coding: utf-8 -*-
# 水果新鮮度診斷手機應用程式

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class FruitApp(App):
    def build(self):
        self.title = "水果新鮮度診斷"
        
        # 主佈局
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # 標題
        title = Label(
            text="🍎 水果新鮮度診斷系統",
            font_size=24,
            size_hint=(1, 0.2)
        )
        layout.add_widget(title)
        
        # 功能按鈕
        btn1 = Button(
            text="📸 拍照分析",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 0.2, 1)
        )
        btn1.bind(on_press=self.take_photo)
        layout.add_widget(btn1)
        
        btn2 = Button(
            text="📁 選擇圖片",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.4, 0.8, 1)
        )
        btn2.bind(on_press=self.select_image)
        layout.add_widget(btn2)
        
        # 結果顯示
        self.result = Label(
            text="歡迎使用水果新鮮度診斷系統！\n請選擇功能開始分析。",
            font_size=16,
            size_hint=(1, 0.4),
            halign='center',
            valign='middle'
        )
        layout.add_widget(self.result)
        
        return layout
    
    def take_photo(self, instance):
        self.result.text = "📸 拍照功能\n（實際應用中會啟動相機）\n\n模擬分析結果：\n🍎 水果：蘋果\n⭐ 新鮮度：85/100\n💡 建議：可以保存2-3天"
    
    def select_image(self, instance):
        self.result.text = "🖼️ 選擇圖片功能\n（實際應用中會開啟檔案選擇器）\n\n模擬分析結果：\n🍌 水果：香蕉\n⭐ 新鮮度：72/100\n💡 建議：建議盡快食用"

if __name__ == '__main__':
    FruitApp().run()
