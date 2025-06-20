# shotshotshot
# TouchDesigner + Arduino + 超音波感測器 × Weather API 互動專案

## 專案簡介

本專案結合 TouchDesigner、Arduino、超音波感測器與 Weather API，創造一套可以「用身體感受天氣」的互動體驗。使用者可在 TouchDesigner 輸入任意城市，取得即時天氣資訊，並透過超音波感測器調節手與感測器距離，讓畫面色彩產生變化──將天氣數據轉譯成可見、可觸碰的視覺語言。

---

## 發想源起

在現代生活裡，天氣資訊多半以冷冰冰的數字與圖表呈現。人們習慣被動接受天氣變化，卻很少真正「感受到」天氣的氛圍。本專案希望打破這種無感的資料閱讀方式──即使只是最簡單的畫面變化，只要加入身體互動，天氣也能變得有情緒、有參與感。  
我們相信，「讓天氣多一點感覺，讓互動多一點詩意」，能幫助使用者重新連結城市、氣候與自己的生活狀態。

---

## 系統架構

```mermaid
graph TD
    A[超音波感測器<br>HC-SR04] -- 距離數值 --> B[Arduino]
    B -- Serial (USB) --> C[TouchDesigner]
    C -- Weather API請求 --> D[氣象資料庫]
    C -- 色彩/動畫變化 --> E[互動視覺畫面]

## 功能說明
城市天氣查詢：於 TouchDesigner 輸入任意城市，Weather API 回傳溫度、天氣狀態等資訊
互動色彩體驗：用戶可移動手與超音波感測器的距離，改變畫面色溫、簡易動畫色彩
多模組資料同步：距離數據同步顯示於 TouchDesigner，可用於觸發更複雜的互動或音效

## 硬體需求
Arduino Uno/Nano/ESP32 等開發板
超音波感測器 HC-SR04
USB 連接線
電腦（安裝 TouchDesigner）
