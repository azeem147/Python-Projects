import re
# this will only serach for 'hello' that is in the begining of the string
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))
# to serach for whatever that is at the end of the string use '$'
