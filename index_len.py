fruit = 'Banana'
index = 0
while index <len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index+1

######

fruit = 'Apple'
for letter in fruit :
    print(letter)

#####

word = 'banana'
count = 0
for letter in word:
    if letter == 'n':
        count = count+1
print(count)

######

s = 'Monthy Python'
print(s[0:4]) #от нулевой буквы до 4 не включительно

#####

fruit = "Banana"
if 'n' in fruit:
    print('found it!')
#####