#TODO: 算 BMI 數值

h = float( input("請輸入身高") );
w = float( input("請輸入體重") );
bmi = w/(h ** 2);

print(type(h)); # h 因為外層有包 float, 所以從 string 轉 float

print("您的BMI值為:" + str(bmi));

if (bmi > 18 and bmi <= 24):
    print("合格")
elif(bmi > 24):
    print("不合格")

