import re
message = 'Call me at 042-5169141   '
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d\d\d\d\d)')
mo = phoneNumRegex.search(message)
print(mo)
print(mo.group())
print(mo.group(1))
print(mo.group(2))

# pipe character
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
moBat = batRegex.search('Batmobile has lost a wheel')
print(moBat)
