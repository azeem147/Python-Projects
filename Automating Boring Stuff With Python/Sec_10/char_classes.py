import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# find all method finds everything that matches the pattern. Returns the list
phoneRegex.findall()
# making your own char classes
objRejex = re.compile(r'[aeiou]')  # Replace 'aeiou' with whatever chars
