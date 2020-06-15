# Break breaks the loop

name = ''
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

# continue statement jumps back to the start to of the loop statement
# to recheck the statement

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('Your spam is ' + str(spam))
