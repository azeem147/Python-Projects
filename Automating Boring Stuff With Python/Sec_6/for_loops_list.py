# A for loop on the list is executed depending on the no. of values
for i in range(4):
    print(i)

# range object returns a list
print(list(range(0, 100, 2)))

# An example
supplies = ['pens', 'flamethrowers', 'binders', 'scales']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# Multiple assignment is handy trick. Write what you want to assign on right
# side of '=', and assignee on the left side
