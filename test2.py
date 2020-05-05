hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try :
    h = float(hrs)
    r = float(rate)
except:
    print("Enter numeric imput!")
if h <=40 :
    pay = h * r
elif h > 40 :
    d = h - 40
    pay = (d*1.5 + 40) * r
print(pay)