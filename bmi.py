print("BMI計算機，By Hiro 2020/03/28 ver 1.0")
weight = input("請輸入體重(公斤): ")
weight = float(weight)
heightCM = input("請輸入身高(公分): ")
heightCM = float(heightCM)
print("計算中...")
heightM = float(heightCM / 100)
heightSquared = heightM ** 2
BMI = weight // heightSquared
BMIStr = str(BMI)

if BMI < 19:
    print("BMI為" + BMIStr + "，太瘦了啦")
elif BMI > 19 and BMI < 24:
    print("BMI為" + BMIStr + "，正常的啦")
elif BMI > 24 and BMI < 28:
    print("BMI為" + BMIStr + "，有點胖啦")
elif BMI >= 28:
    print("BMI為" + BMIStr + "，太胖了啦")