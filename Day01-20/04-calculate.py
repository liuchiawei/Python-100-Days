# 海象運算符
a = 10
print((a := 10))  # 10
# print(a = 10)  # SyntaxError: invalid syntax
print(a)          # 10

# 賦值運算符
a = 10
a += 10
print(a)          # 20
a *= (a + 2)
print(a)          # 440

# 比較運算符 >, <, ==, !=, >=, <=
a = 10
b = 20
print(a > b)      # False
print(a < b)      # True
print(a == b)     # False
print(a != b)     # True
print(a >= b)     # False
print(a <= b)     # True

# 邏輯運算符 and, or, not
a = True
b = False
print(a and b)     # False
print(a or b)      # True
print(not a)       # False
print(not b)       # True

# 成員運算符 in, not in
a = [1, 2, 3, 4, 5]
print(1 in a)      # True
print(1 not in a)  # False

# 身份運算符 is, is not
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
print(a is b)      # False
print(a is not b)  # True

# 位運算符 &, |, ^, ~, <<, >>
a = 10
b = 20
print(a & b)      # 8
print(a | b)      # 30
print(a ^ b)      # 22
print(~a)         # -11
print(a << 2)     # 40
print(a >> 2)     # 2

# 應用（華氏溫度轉攝氏溫度）
f = float(input('請輸入華氏溫度: '))
c = (f - 32) / 1.8
print('%.1f華氏溫度 = %.1f攝氏溫度' % (f, c))

# 應用（計算圓的周長和面積）
r = float(input('請輸入圓的半徑: '))
pi = 3.1415926
p = 2 * pi * r
area = pi * r ** 2
print(f'圓的周長: {p:.2f}')
print(f'圓的面積: {area:.2f}')

# 應用（判斷是否為閏年）
y = int(input('請輸入年份: '))
is_leap = y % 4 == 0 and y % 100 != 0 or y % 400 == 0
print(f'{is_leap = }')