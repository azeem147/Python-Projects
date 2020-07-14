# ? means that it should appear zero or one time
# * means zero or more times
# + means at least one or more times
# {} means that it should match exactcly this much times depending on the no.
# inside {} you can specify the range as well
import re
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
