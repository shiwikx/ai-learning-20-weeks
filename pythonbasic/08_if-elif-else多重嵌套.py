score=int(input("输入一个分数:"))
if score>=90:
    print("优秀")
elif score>=80:
    print("良好")
elif score>=60:
    print("及格")
elif score<=60:
    print("不及格")


year=int(input("请输入一个年份："))
if year%4==0:
    if year%100!=0:
        print("为闰年")
    else:
        if year%400==0:
            print("为闰年")
        else:
            print("不为闰年")
else:
    print("不为闰年")