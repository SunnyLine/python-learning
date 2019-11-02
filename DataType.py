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

print("e 是否是浮点型 ： ", isinstance(e, float), "\n")

print("5 + 4 = ", 5 + 4)
print("99.34 - 72.01 = ", 99.34 - 72.01)
print("3 * 7 = ", 3 * 7)
print("4 / 3 = ", 4 / 3)
print("99 / 24 = ", 99 / 24)
print("99 // 24 = ", 99 // 24)
print("6 % 4 = ", 6 % 4)
print("2 ^ 10 = ", 2 ** 10, "\n")

# String 字符串
string = "hellow-world"
print("string size = ", len(string))
print("string 截取前五个字符", string[0:1])
print("string 截取到倒数第一个数", string[0:-1])
print("string 输出倒数第一个数", string[-1])
print("string 输出第6位及其以后的字符串", string[5:])
print("string 输出三遍", string * 3, "\n")

# 反义字符\
print("hello \n world")
print(r"hello \n world", "\n")

# 列表 List
strList = ["123", 45.23, "789"]
lit = ["abc", "def", "ghi", 999, "mno"]
print("strList = ", strList)
print("list = ", lit)
print("strList [1] = ", strList[1])
print("strList [1,) = ", strList[1:])
print("strList [1,3) = ", lit[1:3])
print("strList [1,-1) = ", lit[1:-1])
print("strList * 2 = ", strList * 2)
print("strList + list = ", strList + lit)
print("list [0::2] = ", lit[0::2])
print("list [-1::-2] = ", lit[-1::-2], "\n")

# Tuple 元组
tuple1 = ("abc", "def", 66.99, "jkl", "mno")
tuple2 = (123, "run")
tuple3 = tuple("12345678")
emptyTuple = ()
onlyOneTuple = (123,)
print("tuple1 = ", tuple1)
print("tuple2 = ", tuple2)
print("tuple3 = ", tuple3)
print("emptyTuple = ", emptyTuple)
print("onlyOneTuple = ", onlyOneTuple)
print("tuple1 [0] = ", tuple1[0])
print("tuple1 [1:3] = ", tuple1[1:3])
print("tuple1 [1:] = ", tuple1[1:])
print("tuple1 [1,-1] = ", tuple1[1:-1])
print("tuple1 * 2 = ", tuple1 * 2)
print("tuple1 + tuple2 = ", tuple1 + tuple2)
print("tuple1 [0::2] = ", tuple1[0::2])
print("tuple1 [-1::-2] = ", tuple1[-1::-2], "\n")

# Set 集合
setOne = {"123", "456", 789, 333}
print("setOne = ", setOne)
if 333 in setOne:
    print("333 在集合中")
else:
    print("333 不在集合中")

a = set("abcde")
b = set("defgh")
print("a = ", a)
print("b = ", b)
print("a - b = ", a - b)
print("a | b = ", a | b)
print("a & b = ", a & b)
print("a ^ b = ", a ^ b, "\n")

# Dictionary 字典
dict1 = {}
dict1["one"] = "python语言"
dict1[2] = "天下第一最牛B"
dict2 = {"name": "李明", "成绩": 92, "学校": "合工大"}
dict3 = dict([("province", "安徽省"), ("city", "合肥市"), ("district", "经开区")])

print("dict1 = ", dict1)
print("dict2 = ", dict2)
print("dict3 = ", dict3)
print("dict1[\"one\"] = ", dict1["one"])
print("dict1[2] = ", dict1[2])
print("dict2.keys = ", dict2.keys())
print("dict2.values = ", dict2.values())
print("dict2.get(\"name\") = ", dict2.get("name"), "\n")
