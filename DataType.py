# Python3 基本数据类型

counter = 100  # 整型变量
miles = 100.1  # 浮点型变量
name = "runoob"  # 字符串变量

print(counter)
print(miles)
print(name)
print(counter + miles)

a = b = c = 14
print("a = ", a, ", b = ", b, ", c = ", c)

d, e, f = 1.87, True, "string"
print("d = ", d, ", e = ", e, ", f = ", f)

print("a type =", type(a), ", b type = ", type(b), ", c type = ", type(c), ", d type = ", type(d), ", e type = ",
      type(e), ", f type = ", type(f))

print("e 是否是浮点型 ： ", isinstance(e, float))

print("5 + 4 = ", 5 + 4)
print("99.34 - 72.01 = ", 99.34 - 72.01)
print("3 * 7 = ", 3 * 7)
print("4 / 3 = ", 4 / 3)
print("99 / 24 = ", 99 / 24)
print("99 // 24 = ", 99 // 24)
print("6 % 4 = ", 6 % 4)
print("2 ^ 10 = ", 2 ** 10)

