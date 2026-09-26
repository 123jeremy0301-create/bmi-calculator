"""
BMI (Body Mass Index) 計算機 / BMI Calculator
多語言支援 (Multilingual Support: 繁體中文 / English / 日本語 / 한국어)
計算公式 / Formula: BMI = 體重(kg) / 身高(m)^2
"""

import sys

# 確保 Windows 終端機能正常印出日文與韓文字元 (Ensure UTF-8 encoding on Windows console)
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stdin, "reconfigure"):
    try:
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

MESSAGES = {
    "zh": {
        "name": "繁體中文",
        "title": "歡迎使用 BMI 計算機",
        "prompt_height": "請輸入您的身高 (公分 cm): ",
        "prompt_weight": "請輸入您的體重 (公斤 kg): ",
        "result_title": "【計算結果】",
        "height": "身高",
        "weight": "體重",
        "bmi": "BMI 值",
        "status": "體位評估",
        "ideal_range": "理想健康體重區間",
        "err_number": "輸入格式錯誤，請輸入正數。",
        "err_positive": "身高與體重必須大於 0。",
        "categories": {
            "underweight": "體重過輕",
            "normal": "健康正常範圍",
            "overweight": "體重過重",
            "mild_obesity": "輕度肥胖",
            "moderate_obesity": "中度肥胖",
            "severe_obesity": "重度肥胖",
        },
    },
    "en": {
        "name": "English",
        "title": "Welcome to BMI Calculator",
        "prompt_height": "Please enter your height (cm): ",
        "prompt_weight": "Please enter your weight (kg): ",
        "result_title": "[Calculation Results]",
        "height": "Height",
        "weight": "Weight",
        "bmi": "BMI Value",
        "status": "Weight Category",
        "ideal_range": "Ideal Healthy Weight Range",
        "err_number": "Invalid input format. Please enter positive numbers.",
        "err_positive": "Height and weight must be greater than 0.",
        "categories": {
            "underweight": "Underweight",
            "normal": "Normal weight",
            "overweight": "Overweight",
            "mild_obesity": "Mild obesity (Class 1)",
            "moderate_obesity": "Moderate obesity (Class 2)",
            "severe_obesity": "Severe obesity (Class 3)",
        },
    },
    "ja": {
        "name": "日本語 (Japanese)",
        "title": "BMI 計算機へようこそ",
        "prompt_height": "身長を入力してください (cm): ",
        "prompt_weight": "体重を入力してください (kg): ",
        "result_title": "【計算結果】",
        "height": "身長",
        "weight": "体重",
        "bmi": "BMI 値",
        "status": "肥満度判定",
        "ideal_range": "適正体重の範囲",
        "err_number": "入力形式が正しくありません。正の数値を入力してください。",
        "err_positive": "身長と体重は 0 より大きい必要があります。",
        "categories": {
            "underweight": "低体重 (痩せ型)",
            "normal": "普通体重 (標準)",
            "overweight": "肥満 (1度) / 過体重",
            "mild_obesity": "肥満 (2度)",
            "moderate_obesity": "肥満 (3度)",
            "severe_obesity": "肥満 (4度 / 高度肥満)",
        },
    },
    "ko": {
        "name": "한국어 (Korean)",
        "title": "BMI 계산기에 오신 것을 환영합니다",
        "prompt_height": "키(신장)를 입력해 주세요 (cm): ",
        "prompt_weight": "몸무게(체중)를 입력해 주세요 (kg): ",
        "result_title": "【계산 결과】",
        "height": "신장(키)",
        "weight": "체중(몸무게)",
        "bmi": "BMI 지수",
        "status": "비만도 판정",
        "ideal_range": "적정(표준) 체중 범위",
        "err_number": "입력 형식이 올바르지 않습니다. 양수를 입력해 주세요.",
        "err_positive": "키와 몸무게는 0보다 커야 합니다.",
        "categories": {
            "underweight": "저체중",
            "normal": "정상 체중",
            "overweight": "과체중",
            "mild_obesity": "경도 비만 (1단계)",
            "moderate_obesity": "중등도 비만 (2단계)",
            "severe_obesity": "고도 비만 (3단계)",
        },
    },
}


def calculate_bmi(height_cm: float, weight_kg: float) -> tuple[float, str, dict[str, str], tuple[float, float]]:
    """
    計算 BMI 值、體位鍵值、多語言對照體位判定與理想體重區間。
    Calculate BMI value, category key, multilingual categories, and ideal weight range.

    回傳 / Returns:
        (bmi, category_key, category_names_dict, (ideal_min_kg, ideal_max_kg))
    """
    if height_cm <= 0 or weight_kg <= 0:
        raise ValueError("Height and weight must be positive.")

    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)

    # 體位標準 (Taiwan MOHW & WHO standards)
    if bmi < 18.5:
        key = "underweight"
    elif 18.5 <= bmi < 24.0:
        key = "normal"
    elif 24.0 <= bmi < 27.0:
        key = "overweight"
    elif 27.0 <= bmi < 30.0:
        key = "mild_obesity"
    elif 30.0 <= bmi < 35.0:
        key = "moderate_obesity"
    else:
        key = "severe_obesity"

    category_names = {
        lang: MESSAGES[lang]["categories"][key] for lang in MESSAGES
    }

    ideal_min_kg = 18.5 * (height_m ** 2)
    ideal_max_kg = 24.0 * (height_m ** 2)

    return round(bmi, 2), key, category_names, (round(ideal_min_kg, 1), round(ideal_max_kg, 1))


def main():
    print("=" * 60)
    print("  BMI 計算機 / BMI Calculator (Multilingual)")
    print("=" * 60)
    print("語言選擇 / Select Language / 言語選択 / 언어 선택:")
    print("  1. 繁體中文 (Traditional Chinese)")
    print("  2. English")
    print("  3. 日本語 (Japanese)")
    print("  4. 한국어 (Korean)")
    print("  5. 多語言對照 / All Languages (預設 / Default)")

    lang_choice = input("請選擇 / Please choose [1/2/3/4/5] (Enter for 5): ").strip()
    lang_map = {
        "1": "zh",
        "2": "en",
        "3": "ja",
        "4": "ko",
    }
    mode = lang_map.get(lang_choice, "all")

    print("-" * 60)

    try:
        if mode in MESSAGES:
            h_prompt = MESSAGES[mode]["prompt_height"]
            w_prompt = MESSAGES[mode]["prompt_weight"]
        else:
            h_prompt = "請輸入身高 / Height / 身長 / 키 (cm): "
            w_prompt = "請輸入體重 / Weight / 体重 / 몸무게 (kg): "

        height_cm = float(input(h_prompt).strip())
        weight_kg = float(input(w_prompt).strip())

        bmi, cat_key, cat_names, (min_w, max_w) = calculate_bmi(height_cm, weight_kg)

        print("\n" + "=" * 60)
        if mode in MESSAGES:
            msg = MESSAGES[mode]
            print(msg["result_title"])
            print(f"  {msg['height']}: {height_cm} cm")
            print(f"  {msg['weight']}: {weight_kg} kg")
            print(f"  {msg['bmi']}: {bmi}")
            print(f"  {msg['status']}: {cat_names[mode]}")
            print(f"  {msg['ideal_range']}: {min_w} ~ {max_w} kg")
        else:
            print("【計算結果 / Calculation Results / 計算結果 / 계산 결과】")
            print(f"  身高 / Height / 身長 / 키: {height_cm} cm")
            print(f"  體重 / Weight / 体重 / 몸무게: {weight_kg} kg")
            print(f"  BMI 值 / Value / 値 / 지수: {bmi}")
            print(f"  體位評估 (中文): {cat_names['zh']}")
            print(f"  Status (English): {cat_names['en']}")
            print(f"  肥満度判定 (日本語): {cat_names['ja']}")
            print(f"  비만도 판정 (한국어): {cat_names['ko']}")
            print(f"  理想體重 / Ideal Weight: {min_w} ~ {max_w} kg")
        print("=" * 60)

    except ValueError:
        if mode in MESSAGES:
            print(f"\n[錯誤/Error] {MESSAGES[mode]['err_number']}")
        else:
            print("\n[錯誤 / Error] 請輸入有效的正數數字 / Please enter valid positive numbers.")


if __name__ == "__main__":
    main()
