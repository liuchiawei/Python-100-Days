# BMI計算器
h = float(input("請輸入身高(cm): "))
w = float(input("請輸入體重(kg): "))
bmi = w / (h / 100) ** 2
print(f'{bmi = :.1f}')
if bmi < 18.5:
    print('體重過輕')
elif bmi < 24:
    print('正常範圍')
elif bmi < 27:
    print('體重過重')
else:
    print('肥胖')

match bmi:
    case _ if bmi < 18.5:
        description = '體重過輕'
    case _ if 18.5 <= bmi < 24:
        description = '正常範圍'
    case _ if 24 <= bmi < 27:
        description = '體重過重'
    case _:
        description = '肥胖'
print(f'{description = }')

# 成績換算
score = float(input('請輸入成績: '))

match score:
    case _ if score >= 90: grade = 'A'
    case _ if score >= 80: grade = 'B'
    case _ if score >= 70: grade = 'C'
    case _ if score >= 60: grade = 'D'
    case _: grade = 'F'
print(f'{grade = }')