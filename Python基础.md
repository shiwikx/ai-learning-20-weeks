# Python

### 变量名

组成：字母，下划线，数字

禁止：数字开头、特殊符号、使用空格、引号

#### 命名规则：

1、变量名&函数名：下划线命名法——全小写字母，单词间用下划线_分隔

2、类名：大驼峰命名法——单词首字母大小无分隔符

3、常量名：全大写蛇形命名法——全大写字母，单词间用下划线分隔



#### 变量输出：

f-string拼接

例：number=666

print（f“你的操作{number}”）



#### 变量赋值：

variable1，variable2=“变量1”，“变量2”

print（variable1，variable2）



### 注释

过时注释：代码逻辑改变但注释未更新

明确含义：注释应该解释为什么这样做



### 数据类型

#### 字符串——一段文本使用引号标记起来

text=“我是一个字符串”

print（text）

print（len（text））——len函数获取字符串有多少字符



#### 数值类型

1、整形int

2、浮点型float（小数）



### 布尔型

1、真 变量名=True 1

2、假 变量名=False 0



### 空值

None  Type



### 数据类型的查看和转换

type()数据/变量

#### 显式转换：强制转换

字符串类型：str()

布尔型：bool()

整形转换：int()，只能有数字

浮点型转换：float()

整形和浮点型可以相互转换：print(int(1.2))——1

print(float(1))——1.0



#### 隐式转换：

整型、浮点型

print(1+2.0)

print(1+True)



### input函数

input("提示用户需要输入什么内容")

例：

username=input("请输入你的用户名：")

print("欢迎"+usrname+"进入系统")



### if语句

if条件表达式(True)：

​	执行的代码块

#### 比较运算符

1.==  5==5 True

2.！=  5！=3  True

3.>    5>3   True

4.<    3<5    True

5.<=   3<=5    True

6.>=   5>=3     True

例：

money=20

if money>=15

​	print("中午吃辣椒炒肉")



if条件表达式(True/Fales)：

​	则执行第一个代码块

else：

​	则执行第二个代码块

例：

money=int(input("请输入您有多少钱"))

if money>=15：

​	print("中午吃辣椒炒肉")

else：

​	print("中午吃蛋炒饭")



### elif

if条件表达式：

​	执行代码块1

elif条件表达式：

​	执行代码块2

elif条件表达式：

​	执行代码块3

else：（只有if和elif均为false时才会执行）

​	以上条件都不满足执行的代码块4



### if语句的嵌套使用

if条件一：

​	if条件二：

​		满足条件执行的代码块1

​	else：

​	        不满足条件执行的代码块2

else：

​	不满足条件执行的代码块3



### 逻辑运算符

#### and运算符（并且）

条件表达式1 and 条件表达式2 （布尔类型需满足两个条件为真）



#### or运算符（或者）

条件表达式1 or 条件表达式2 （布尔类型，两个表达式都为真则为真；一个表达式为false，一个表达式为真，则结果仍然为真）



#### not运算符（非）

not条件表达式（当条件表达式为true时，则为条件表达式false，反之条件表达式为false时，则为条件表达式true）



#### and运算符（并且）、or运算符（或者）、not运算符（非）的优先级

##### not>and>or

例：

x=8

not(x>5 and x<10 or x== 20)

1：x>5 and x<10 为true

2：x>5 and x<10 or x== 20  为true

3：not(x>5 and x<10 or x== 20) 为false



用小括号可改变优先级

例：

x=8

not(x>5 and （x<10 or x== 20）)

1：（x<10 or x== 20）为true

2：x>5 and （x<10 or x== 20）为true

3：not(x>5 and （x<10 or x== 20）) 为false



