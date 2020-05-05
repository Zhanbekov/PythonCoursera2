counter = 0
while True:

    num = input('Enter a number:')
    if counter == 0:
        largest = int(num)
        smallest = int(num)
        counter+=1

    if num == "done" : 
        break 
    try : 
       num = int(num)
    except :
       print('Invalid input')
       continue
        
    if num < smallest:
        smallest = num
    
    if num > largest:
        largest = num
        
print("Maximum is",largest)
print("Minimum is",smallest)