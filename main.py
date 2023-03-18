numbers = [] # لیستی برای ذخیره اعداد وارد شده
 
n = int(input("تعداد اعداد مورد نظر را وارد کنید: ")) # دریافت تعداد اعداد از کاربر
 
for i in range(n):
    number = int(input("عدد بعدی را وارد کنید: ")) 
    numbers.append(number) # اضافه کردن هر اعداد وارد شده به لیست
   
average = sum(numbers)/n # حساب میانگین
 
print("میانگین اعداد وارد شده برابر است با:", average)
