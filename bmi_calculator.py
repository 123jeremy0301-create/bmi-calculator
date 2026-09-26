"""
BMI (Body Mass Index) 計算機
計算公式：BMI = 體重(公斤) / 身高(公尺)^2
"""

def calculate_bmi(height_cm: float, weight_kg: float) -> tuple[float, str, tuple[float, float]]:
    """
    計算 BMI 值、體位判定與理想體重區間。

    參數:
        height_cm (float): 身高 (公分)
        weight_kg (float): 體重 (公斤)

    回傳:
        (bmi, category, (min_ideal_weight, max_ideal_weight))
    """
    if height_cm <= 0 or weight_kg <= 0:
        raise ValueError("身高與體重必須大於 0")

    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)

    # 體位判定標準（衛福部標準）
    if bmi < 18.5:
        category = "體重過輕 (Underweight)"
    elif 18.5 <= bmi < 24.0:
        category = "健康正常範圍 (Normal)"
    elif 24.0 <= bmi < 27.0:
        category = "體重過重 (Overweight)"
    elif 27.0 <= bmi < 30.0:
        category = "輕度肥胖 (Mild obesity)"
    elif 30.0 <= bmi < 35.0:
        category = "中度肥胖 (Moderate obesity)"
    else:
        category = "重度肥胖 (Severe obesity)"

    # 理想體重範圍 (BMI 18.5 ~ 24.0)
    ideal_min_weight = 18.5 * (height_m ** 2)
    ideal_max_weight = 24.0 * (height_m ** 2)

    return round(bmi, 2), category, (round(ideal_min_weight, 1), round(ideal_max_weight, 1))


def main():
    print("=" * 45)
    print("         歡迎使用 BMI 計算機 (BMI Calculator)")
    print("=" * 45)

    try:
        height_input = input("請輸入您的身高 (公分 cm): ").strip()
        height_cm = float(height_input)

        weight_input = input("請輸入您的體重 (公斤 kg): ").strip()
        weight_kg = float(weight_input)

        bmi, category, (min_w, max_w) = calculate_bmi(height_cm, weight_kg)

        print("\n" + "-" * 45)
        print("【計算結果】")
        print(f"  身高: {height_cm} cm")
        print(f"  體重: {weight_kg} kg")
        print(f"  BMI 值: {bmi}")
        print(f"  體位評估: {category}")
        print(f"  您的理想健康體重區間: {min_w} ~ {max_w} kg")
        print("-" * 45)

    except ValueError as e:
        print(f"\n[錯誤] 輸入格式不正確: 請輸入有效的數字 ({e})")
    except Exception as e:
        print(f"\n[錯誤] 發生未知錯誤: {e}")


if __name__ == "__main__":
    main()
