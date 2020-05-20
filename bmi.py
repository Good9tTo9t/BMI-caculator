print("BMI計算機，By Hiro 2020/03/28 ver 1.0")
weight = float(input("請輸入體重(公斤): "))
heightCM = float(input("請輸入身高(公分): "))
print("計算中...")
heightM = heightCM / 100
BMI = weight / (heightM ** 2)

if BMI < 19:
    print("BMI為%f，太瘦了啦"%(BMI))
elif BMI > 19 and BMI < 24:
    print("BMI為%f，正常的啦"%(BMI))
elif BMI > 24 and BMI < 28:
    print("BMI為%f，有點胖啦"%(BMI))
elif BMI >= 28:
    print("BMI為%f，太胖了啦"%(BMI))
input("按enter離開:")
exit()