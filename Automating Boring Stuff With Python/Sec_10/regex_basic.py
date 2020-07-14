import re
message = 'Call me at 042-5169141 or 0320-0514147'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\d\d\d\d')
mo = phoneNumRegex.findall(message)
print(mo)
