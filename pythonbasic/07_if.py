print ("超市公告：")
print ("消费满100元的客户可以打九折")
money=float(input("请输入您消费的金额："))
if money >= 100:
    print("打折后的金额为：",money*0.9)
else:
    print("未满100元原价金额为：",money)
    
          