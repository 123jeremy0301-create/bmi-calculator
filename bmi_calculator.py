"""
BMI (Body Mass Index) 計算機 / BMI Calculator
雙語支援 (Bilingual Support: Traditional Chinese / English)
計算公式 / Formula: BMI = 體重(kg) / 身高(m)^2
"""

MESSAGES = {
    "zh": {
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
}


def calculate_bmi(height_cm: float, weight_kg: float) -> tuple[float, str, str, tuple[float, float]]:
    """
    計算 BMI 值、雙語體位判定與理想體重區間。
    Calculate BMI value, bilingual category, and ideal weight range.

    回傳 / Returns:
        (bmi, category_zh, category_en, (ideal_min_kg, ideal_max_kg))
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

    category_zh = MESSAGES["zh"]["categories"][key]
    category_en = MESSAGES["en"]["categories"][key]

    ideal_min_kg = 18.5 * (height_m ** 2)
    ideal_max_kg = 24.0 * (height_m ** 2)

    return round(bmi, 2), category_zh, category_en, (round(ideal_min_kg, 1), round(ideal_max_kg, 1))


def main():
    print("=" * 55)
    print("  BMI 計算機 / BMI Calculator (Bilingual)")
    print("=" * 55)
    print("語言選擇 / Select Language:")
    print("  1. 繁體中文 (Traditional Chinese)")
    print("  2. English")
    print("  3. 雙語並列 / Bilingual (預設 / Default)")

    lang_choice = input("請選擇 / Please choose [1/2/3] (Enter for 3): ").strip()
    if lang_choice == "1":
        mode = "zh"
    elif lang_choice == "2":
        mode = "en"
    else:
        mode = "bilingual"

    print("-" * 55)

    try:
        if mode == "zh":
            h_prompt = MESSAGES["zh"]["prompt_height"]
            w_prompt = MESSAGES["zh"]["prompt_weight"]
        elif mode == "en":
            h_prompt = MESSAGES["en"]["prompt_height"]
            w_prompt = MESSAGES["en"]["prompt_weight"]
        else:
            h_prompt = "請輸入身高 / Enter height (cm): "
            w_prompt = "請輸入體重 / Enter weight (kg): "

        height_cm = float(input(h_prompt).strip())
        weight_kg = float(input(w_prompt).strip())

        bmi, cat_zh, cat_en, (min_w, max_w) = calculate_bmi(height_cm, weight_kg)

        print("\n" + "=" * 55)
        if mode == "zh":
            print(MESSAGES["zh"]["result_title"])
            print(f"  {MESSAGES['zh']['height']}: {height_cm} cm")
            print(f"  {MESSAGES['zh']['weight']}: {weight_kg} kg")
            print(f"  {MESSAGES['zh']['bmi']}: {bmi}")
            print(f"  {MESSAGES['zh']['status']}: {cat_zh}")
            print(f"  {MESSAGES['zh']['ideal_range']}: {min_w} ~ {max_w} kg")
        elif mode == "en":
            print(MESSAGES["en"]["result_title"])
            print(f"  {MESSAGES['en']['height']}: {height_cm} cm")
            print(f"  {MESSAGES['en']['weight']}: {weight_kg} kg")
            print(f"  {MESSAGES['en']['bmi']}: {bmi}")
            print(f"  {MESSAGES['en']['status']}: {cat_en}")
            print(f"  {MESSAGES['en']['ideal_range']}: {min_w} ~ {max_w} kg")
        else:
            print("【計算結果 / Calculation Results】")
            print(f"  身高 / Height: {height_cm} cm")
            print(f"  體重 / Weight: {weight_kg} kg")
            print(f"  BMI 值 / BMI Value: {bmi}")
            print(f"  體位評估 / Status: {cat_zh} / {cat_en}")
            print(f"  理想體重 / Ideal Weight: {min_w} ~ {max_w} kg")
        print("=" * 55)

    except ValueError:
        if mode == "zh":
            print(f"\n[錯誤] {MESSAGES['zh']['err_number']}")
        elif mode == "en":
            print(f"\n[Error] {MESSAGES['en']['err_number']}")
        else:
            print("\n[錯誤 / Error] 請輸入有效的正數數字 / Please enter valid positive numbers.")


if __name__ == "__main__":
    main()
