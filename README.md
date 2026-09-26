# 🧮 多語言 BMI 計算機 / Multilingual BMI Calculator

一個支援 **繁體中文、English、日本語、한국어** 四國語言的命令列 BMI (Body Mass Index) 計算機工具。

A lightweight, multilingual command-line BMI calculator supporting **Traditional Chinese, English, Japanese, and Korean**.

---

## 🌟 功能特點 / Features

- 🌐 **四國語言支援 / Multilingual Support**:
  - 繁體中文 (Traditional Chinese)
  - English
  - 日本語 (Japanese - 採用日本肥満学会標準)
  - 한국어 (Korean - 採用大韓肥胖學會標準)
  - 多語言對照 (All Languages Side-by-Side)
- ⚖️ **理想體重計算 / Ideal Weight**: 自動計算符合健康 BMI (18.5 ~ 24.0) 的目標體重區間。
- 🛡️ **防呆機制 / Robust Input Handling**: 完善的輸入驗證與防崩潰處理。
- 🪟 **跨平台與 Windows 優化 / Cross-platform**: 內建 UTF-8 控制台處理，避免 Windows 控制台多國語言編碼亂碼。

---

## 🚀 快速開始 / Quick Start

### 系統需求 / Requirements
- Python 3.8+
- Git

### 執行程式 / Run

```bash
python bmi_calculator.py
```

### 操作示範 / Example Usage

```text
============================================================
  BMI 計算機 / BMI Calculator (Multilingual)
============================================================
語言選擇 / Select Language / 言語選択 / 언어 선택:
  1. 繁體中文 (Traditional Chinese)
  2. English
  3. 日本語 (Japanese)
  4. 한국어 (Korean)
  5. 多語言對照 / All Languages (預設 / Default)
請選擇 / Please choose [1/2/3/4/5] (Enter for 5): 5
------------------------------------------------------------
請輸入身高 / Height / 身長 / 키 (cm): 175
請輸入體重 / Weight / 体重 / 몸무게 (kg): 65

============================================================
【計算結果 / Calculation Results / 計算結果 / 계산 결과】
  身高 / Height / 身長 / 키: 175.0 cm
  體重 / Weight / 体重 / 몸무게: 65.0 kg
  BMI 值 / Value / 値 / 지수: 21.22
  體位評估 (中文): 健康正常範圍
  Status (English): Normal weight
  肥満度判定 (日本語): 普通体重 (標準)
  비만도 판定 (한국어): 정상 체중
  理想體重 / Ideal Weight: 56.7 ~ 73.5 kg
============================================================
```

---

## 📐 BMI 計算公式 / Formula

$$\text{BMI} = \frac{\text{體重 (kg)}}{\text{身高 (m)}^2}$$

| BMI 數值範圍 | 體位判定 (中文) | Status (EN) | 肥満度判定 (JA) | 비만도 판정 (KO) |
|---|---|---|---|---|
| `< 18.5` | 體重過輕 | Underweight | 低体重 (痩せ型) | 저체중 |
| `18.5 ~ 24.0` | 健康正常範圍 | Normal weight | 普通体重 (標準) | 정상 체중 |
| `24.0 ~ 27.0` | 體重過重 | Overweight | 肥満 (1度) | 과체중 |
| `27.0 ~ 30.0` | 輕度肥胖 | Mild obesity | 肥満 (2度) | 경도 비만 |
| `30.0 ~ 35.0` | 中度肥胖 | Moderate obesity | 肥満 (3度) | 중등도 비만 |
| `≥ 35.0` | 重度肥胖 | Severe obesity | 肥満 (4度) | 고도 비만 |

---

## 📄 授權條款 / License
MIT License
