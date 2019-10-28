# 缩进
i = 10
if i == 10:
    print("True")
    print("厉害了")
else:
    print("False")

# 多语句
if i == 10:
    print("i = 10")
elif i == 20:
    print("i = 20")
elif i == 30:
    print("i= 30")
else:
    print("i = other")
    print("Over")

# Print 输出
x = "a"
y = "b"
# 换行输出
print("x = " + x)
print("y = " + y)
print("-----------------")
#不换行输出  end 关键字
print("x = " + x, end=" ")
print("y = " + y, end=" ")

#import与from...import
"""
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
"""
import sys
print("=============Python import mode=============")
print("命令行参数为:")
for i in sys.argv:
    print(i)
print("\npython路径为",sys.path)
print("\npython api 版本为",sys.api_version)

from sys import argv,path,api_version   #导入特定成员
print("=============Python from import=============")
for i in sys.argv:
    print(i)
print("path:",path)
print("api 版本",api_version)