def computepay(h,r):
    if h <= 40:
        return h * r
    else:
        d = h - 40
        p = (d*1.5 + 40)* r
        return p
             
h = input("Enter Hours:")
h = float (h)
r = input("Enter Rate:")
r = float(r)
print("Pay", computepay(h,r))