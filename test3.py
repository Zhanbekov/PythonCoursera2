score = input("Enter Score: ")
try :
    score = float(score)
except :
    print("Enter numeric input!")
if score > 0 and  score <0.6 :
    print("F")
elif score >=0.6 and score <0.7 :
    print("D")
elif score >=0.7 and score <0.8 :
    print("C")
elif score >=0.8 and score <0.9 :
    print("B")
elif score >=0.9 and score <=1 :
    print("A")
else :
    print("Print score between 0 and 1")